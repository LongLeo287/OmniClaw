# Deep Matrix Profile: FETCHED_agent-skills_124622

# Deep Knowledge Report for Apify Ultimate Scraper Skills Repository

## Overview

This repository is designed to facilitate the development of specialized AI agents for web scraping, data extraction, and creating Apify Actors. It includes scripts that generate documentation, interact with Apify APIs, run actors, and search the Apify store. The primary mechanisms include:

- **Documentation Generation**: `generate_agents.py` generates a comprehensive `AGENTS.md` file from template files.
- **API Interaction**: Scripts for fetching actor details, running actors, and searching the Apify store.
- **Skill Management**: Organized structure for managing individual skills within the repository.

## Architectural Patterns

### 1. **Modular Structure**

The repository is modularly structured with a clear separation of concerns:

- **Scripts Directory (`scripts`)**: Contains utility scripts for generating documentation and interacting with Apify APIs.
- **Skills Directory (`skills`)**: Houses individual skills, each containing its own `SKILL.md` frontmatter file.

### 2. **Front Matter Parsing**

The repository uses a custom front matter parser to extract metadata from `SKILL.md` files in the `skills` directory. This ensures that all necessary information is consistently structured and easily accessible.

```python
def parse_frontmatter(text: str) -> dict[str, str]:
    """Parse a minimal YAML-ish frontmatter block without external deps."""
    match = re.search(r"^---\s*\n(.*?)\n---\s*", text, re.DOTALL)
    if not match:
        return {}
    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data
```

### 3. **Template Rendering**

The `generate_agents.py` script uses a simple template rendering mechanism to generate the final documentation (`AGENTS.md`). This approach ensures that all skill information is consistently formatted and integrated into the main document.

```python
def render(template: str, skills: list[dict[str, str]]) -> str:
    """Very small Mustache-like renderer that only supports a single skills loop."""
    def repl(match: re.Match[str]) -> str:
        block = match.group(1).strip("\n")
        rendered_blocks = []
        for skill in skills:
            rendered = (
                block.replace("{{name}}", skill["name"])
                .replace("{{description}}", skill["description"])
                .replace("{{path}}", skill["path"])
            )
            rendered_blocks.append(rendered)
        return "\n".join(rendered_blocks)

    # Render loop blocks
    content = re.sub(r"{{#skills}}(.*?){{/skills}}", repl, template, flags=re.DOTALL)
    return content
```

### 4. **API Interaction**

The scripts for fetching actor details and running actors (`fetch_actor_details.js`, `run_actor.js`) interact with the Apify API using standard HTTP requests. They handle authentication via environment variables and provide a user-friendly command-line interface.

```javascript
async function fetchActorInfo(token, actorId) {
    const apiActorId = actorId.replace('/', '~');
    const url = `https://api.apify.com/v2/acts/${apiActorId}?token=${encodeURIComponent(token)}`;

    const response = await fetch(url, {
        headers: { 'User-Agent': `${USER_AGENT}/fetch_actor_info` },
    });

    if (response.status === 404) {
        console.error(`Error: Actor '${actorId}' not found`);
        process.exit(1);
    }

    if (!response.ok) {
        const text = await response.text();
        console.error(`Error: Failed to fetch actor info (${response.status}): ${text}`);
        process.exit(1);
    }

    return (await response.json()).data;
}
```

### 5. **Search Functionality**

The `search_actors.js` script provides a simple interface for searching the Apify store based on keywords. It uses the Apify API to fetch relevant actors and formats the results for display.

```javascript
async function searchStore(query, limit) {
    const params = new URLSearchParams({ search: query, limit: String(limit) });
    const url = `https://api.apify.com/v2/store?${params}`;

    const response = await fetch(url, {
        headers: { 'User-Agent': `${USER_AGENT}/search_actors` },
    });

    if (!response.ok) {
        const text = await response.text();
        console.error(`Error: Store search failed (${response.status}): ${text}`);
        process.exit(1);
    }

    const result = await response.json();
    return result.data?.items || [];
}
```

## Core Algorithms

### 1. **Skill Collection and Documentation Generation**

- **Skill Discovery**: The `collect_skills` function iterates through the `skills` directory, reading each `SKILL.md` file to extract metadata.
- **Template Rendering**: The `render` function uses a simple template engine to integrate skill data into the main documentation.

### 2. **API Interaction Algorithms**

- **Actor Details Fetching**: Uses the Apify API to fetch actor details such as README, input schema, and description.
- **Actor Execution**: Runs actors with specified inputs and handles output in various formats (e.g., CSV, JSON).

### 3. **Search Algorithm**

- **Store Search**: Utilizes the Apify store API to search for actors based on keywords and limits the number of results.

## Primary Mechanisms

1. **Documentation Generation**:
   - **Template Parsing**: Reads `AGENTS_TEMPLATE.md` and uses front matter from `SKILL.md` files.
   - **Rendering**: Uses a simple template engine to generate final documentation.

2. **API Interaction**:
   - **Authentication**: Uses environment variables for API token authentication.
   - **HTTP Requests**: Makes HTTP requests to the Apify API using standard JavaScript fetch methods.

3. **Actor Management**:
   - **Running Actors**: Executes actors with specified inputs and handles output formats.
   - **Search Functionality**: Provides a CLI interface for searching the Apify store.

## Conclusion

This repository provides a robust framework for developing, managing, and deploying specialized AI agents using Apify. The modular structure, front matter parsing, template rendering, and API interaction mechanisms ensure that all components work seamlessly together to streamline the development process.