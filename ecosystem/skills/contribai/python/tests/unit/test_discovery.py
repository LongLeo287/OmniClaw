"""Tests for repository discovery engine."""

from unittest.mock import AsyncMock

import pytest

from contribai.core.config import DiscoveryConfig
from contribai.core.models import DiscoveryCriteria, Repository
from contribai.github.discovery import RepoDiscovery


def make_repo(name: str, stars: int = 500, open_issues: int = 5, **kwargs) -> Repository:
    defaults = dict(
        owner="owner",
        name=name,
        full_name=f"owner/{name}",
        language="python",
        stars=stars,
        forks=50,
        open_issues=open_issues,
        default_branch="main",
        has_license=True,
    )
    defaults.update(kwargs)
    return Repository(**defaults)


@pytest.fixture
def discovery():
    client = AsyncMock()
    config = DiscoveryConfig(languages=["python"], stars_range=[100, 5000])
    return RepoDiscovery(client=client, config=config)


class TestPrioritize:
    def test_sweet_spot_stars_ranked_higher(self, discovery):
        repos = [
            make_repo("low_stars", stars=50),
            make_repo("sweet_spot", stars=500),
            make_repo("high_stars", stars=8000),
        ]
        result = discovery._prioritize(repos)
        assert result[0].name == "sweet_spot"

    def test_contributing_guide_boosts_score(self, discovery):
        repos = [
            make_repo("no_guide", stars=500),
            make_repo("has_guide", stars=500, has_contributing=True),
        ]
        result = discovery._prioritize(repos)
        assert result[0].name == "has_guide"

    def test_more_issues_ranked_higher(self, discovery):
        repos = [
            make_repo("few_issues", open_issues=2),
            make_repo("many_issues", open_issues=50),
        ]
        result = discovery._prioritize(repos)
        assert result[0].name == "many_issues"

    def test_licensed_repo_preferred(self, discovery):
        repos = [
            make_repo("no_license", has_license=False),
            make_repo("has_license", has_license=True),
        ]
        result = discovery._prioritize(repos)
        assert result[0].name == "has_license"


class TestFilterContributable:
    @pytest.mark.asyncio
    async def test_skips_no_issues(self, discovery):
        repos = [make_repo("empty", open_issues=0)]
        result = await discovery._filter_contributable(
            repos, DiscoveryCriteria(languages=["python"])
        )
        assert len(result) == 0

    @pytest.mark.asyncio
    async def test_keeps_repos_with_issues(self, discovery):
        repos = [make_repo("active", open_issues=5)]
        result = await discovery._filter_contributable(
            repos, DiscoveryCriteria(languages=["python"])
        )
        assert len(result) == 1

    @pytest.mark.asyncio
    async def test_requires_contributing_guide(self, discovery):
        discovery._client.get_contributing_guide = AsyncMock(return_value=None)
        repos = [make_repo("no_guide", open_issues=5)]
        criteria = DiscoveryCriteria(languages=["python"], require_contributing_guide=True)
        result = await discovery._filter_contributable(repos, criteria)
        assert len(result) == 0

    @pytest.mark.asyncio
    async def test_passes_with_contributing_guide(self, discovery):
        discovery._client.get_contributing_guide = AsyncMock(return_value="# Contributing")
        repos = [make_repo("has_guide", open_issues=5)]
        criteria = DiscoveryCriteria(languages=["python"], require_contributing_guide=True)
        result = await discovery._filter_contributable(repos, criteria)
        assert len(result) == 1


class TestCriteriaFromConfig:
    def test_builds_criteria(self, discovery):
        criteria = discovery._criteria_from_config()
        assert criteria.languages == ["python"]
        assert criteria.stars_min == 100
        assert criteria.stars_max == 5000
