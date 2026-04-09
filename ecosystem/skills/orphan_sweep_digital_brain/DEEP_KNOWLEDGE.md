# Deep Matrix Profile: ORPHAN_SWEEP_digital_brain

# Deep Knowledge Report

## Architectural Patterns

The `agents\scripts` directory contains several Python scripts that serve as components of the Digital Brain system. These scripts are designed to operate independently but interact with shared data stores managed by the Digital Brain's knowledge management framework.

### Content Ideas Generator (`content_ideas.py`)

- **Purpose**: Generates content ideas based on past successful content and recent bookmarks.
- **Key Components**:
  - `load_jsonl()`: A utility function for loading JSON Lines (JSONL) files, skipping schema lines.
  - `get_top_performing_content()`: Retrieves the top-performing posts based on engagement metrics.
  - `get_recent_bookmarks()`: Fetches recent bookmarks optionally filtered by category.
  - `get_undeveloped_ideas()`: Lists ideas that haven't been developed yet.
  - `generate_suggestions()`: Generates content suggestions, combining insights from top-performing content and recent research.

### Idea to Draft Expander (`idea_to_draft.py`)

- **Purpose**: Takes an idea ID and creates a draft scaffold with relevant context.
- **Key Components**:
  - `load_jsonl()`: Similar utility function for loading JSONL files.
  - `find_idea()`: Finds an idea by ID or partial match.
  - `find_related_bookmarks()`: Identifies related bookmarks based on tags and category.
  - `find_similar_posts()`: Fetches past posts in the same pillar for reference.
  - `generate_draft_scaffold()`: Generates a draft scaffold from an idea, including metadata, original idea, hook options, main points, and supporting evidence.

### Stale Contacts Finder (`stale_contacts.py`)

- **Purpose**: Identifies contacts that haven't been reached out to recently.
- **Key Components**:
  - `load_jsonl()`: Utility function for loading JSONL files.
  - `days_since()`: Calculates the number of days since a date string.
  - `find_stale_contacts()`: Finds contacts needing outreach based on their last contact date and circle threshold.
  - `generate_report()`: Generates a report listing urgent, due, and coming up contacts.

### Weekly Review Generator (`weekly_review.py`)

- **Purpose**: Compiles data from Digital Brain into a weekly review document.
- **Key Components**:
  - `load_jsonl()`: Utility function for loading JSONL files.
  - `get_week_range()`: Determines the start and end of the current week.
  - `analyze_content()`: Analyzes content published this week, including posts and new ideas.
  - `analyze_network()`: Analyzes network activity this week, including interactions.
  - `analyze_metrics()`: Retrieves latest metrics if available.
  - `generate_review()`: Generates the weekly review output, summarizing content, network, and metrics.

## Core Algorithms

- **Engagement Scoring**: The `engagement_score()` function in `content_ideas.py` calculates a score for posts based on engagement metrics like likes, comments, and reposts.
- **Threshold-Based Contact Identification**: In `stale_contacts.py`, the script identifies contacts that are overdue for outreach based on predefined thresholds for different circles of contacts.

## Primary Mechanisms

- **Data Loading and Parsing**: The scripts use a common utility function `load_jsonl()` to load JSONL files, ensuring consistency in data handling.
- **Filtering and Sorting**: Various functions filter and sort data based on specific criteria (e.g., engagement score, recent date) to generate insights and suggestions.
- **Report Generation**: Each script generates a structured report or output that can be used for decision-making or further processing.

## Conclusion

The scripts in the `agents\scripts` directory are integral components of the Digital Brain system. They leverage shared data stores managed by the knowledge management framework to provide actionable insights, generate content ideas, expand drafts, identify stale contacts, and compile weekly reviews. The modular design ensures that each script can be run independently while contributing to a cohesive workflow within the system.

## Next Steps

1. Review the performance of generated content.
2. Plan next week's content strategy based on insights from the review.
3. Ensure all scripts are well-documented for future maintenance and updates.