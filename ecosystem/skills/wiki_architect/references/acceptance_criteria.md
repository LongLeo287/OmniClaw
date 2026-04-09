# Wiki Architect — Acceptance Criteria

## Catalogue Structure

### ✅ Correct
```json
{
  "items": [
    {
      "title": "getting-started",
      "name": "Getting Started with MyProject",
      "prompt": "Generate an overview of the project based on README.md:1 and package.json:1",
      "children": [
        {
          "title": "environment-setup",
          "name": "Environment Setup",
          "prompt": "Document setup steps from Dockerfile:1 and docker-compose.yml:1",
          "children": []
        }
      ]
    },
    {
      "title": "deep-dive",
      "name": "Architecture Deep Dive",
      "prompt": "Analyze architecture based on src/index.ts:1 and src/server.ts:15",
      "children": []
    }
  ]
}
```

### ❌ Incorrect
```json
{
  "items": [
    {
      "title": "getting-started",
      "name": "Component A",
      "prompt": "Generate documentation",
      "children": []
    }
  ]
}
```

## File Citations

### ✅ Correct
```text
"prompt": "Analyze the authentication middleware defined in src/auth/middleware.ts:42 and the token validation in src/auth/jwt.ts:15"
```

### ❌ Incorrect
```text
"prompt": "Document the authentication system"
```

## Nesting Depth

### ✅ Correct
```json
{
  "title": "level-1",
  "children": [
    {
      "title": "level-2",
      "children": [
        {
          "title": "level-3",
          "children": [
            { "title": "level-4", "children": [] }
          ]
        }
      ]
    }
  ]
}
```

### ❌ Incorrect
```json
{
  "title": "level-1",
  "children": [
    {
      "title": "level-2",
      "children": [
        {
          "title": "level-3",
          "children": [
            {
              "title": "level-4",
              "children": [
                { "title": "level-5-too-deep", "children": [] }
              ]
            }
          ]
        }
      ]
    }
  ]
}
```

## Required Fields

### ✅ Correct
```json
{
  "title": "auth-system",
  "name": "Authentication System",
  "prompt": "Document the auth flow in src/auth/index.ts:1 and src/middleware/auth.ts:30",
  "children": []
}
```

### ❌ Incorrect
```json
{
  "title": "auth-system",
  "name": "",
  "prompt": "",
  "children": []
}
```
