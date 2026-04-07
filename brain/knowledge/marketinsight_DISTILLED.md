---
id: marketinsight
type: knowledge
owner: OA_Triage
---
# marketinsight
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: main.py
```py
import os
import uvicorn
from fastapi import FastAPI
from langfuse import Langfuse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from langchain_core.messages import SystemMessage, HumanMessage
from config.config import RequestObject
from MarketInsight.components.agent import agent
from MarketInsight.utils.logger import get_logger

logger = get_logger(__name__)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with your Vercel URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

langfuse = Langfuse(
    public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
    secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
    host=os.getenv("LANGFUSE_HOST")
)


@app.get("/health")
async def health_check():
    """Health check endpoint for service monitoring and keep-alive pings"""
    return {"status": "ok", "message": "Service is running"}


@app.post("/api/chat")
async def chat(request: RequestObject):
    config = {'configurable': {'thread_id': request.threadId}}
    async def generate():
        try:
            # Create a span for the entire request
            with langfuse.start_as_current_observation(
                as_type="span", 
                name="chat-request",
                input=request.prompt.content
            ) as span:
                # Set user_id as metadata
                span.update(metadata={"user_id": request.threadId})
                
                # Create a nested generation for the LLM/agent call
                with langfuse.start_as_current_observation(
                    as_type="generation",
                    name="agent-stream",
                    model="agentic-workflow",
                    input=request.prompt.content
                ) as generation:
                    
                    full_response = ""
                    for token, _ in agent.stream(
                        {
                            'messages': [
                                SystemMessage(content="You are a professional stock market analyst. For every user query, first determine whether a relevant tool can provide accurate or real-time data. If an appropriate tool exists, you must use it before answering. If the user does not provide an exact stock ticker, use the available tool to identify or resolve the correct ticker when required. Only when no suitable tool applies should you respond using your own reasoning and general market knowledge. Never guess, assume, or fabricate any financial data."),
                                HumanMessage(content=request.prompt.content)
                            ]
                        },
                        stream_mode='messages',
                        config=config
                    ):
                        full_response += token.content
                        yield token.content
                    
                    # Update generation with the complete output
                    generation.update(output=full_response)
                
                # Update span with completion status
                span.update(output="Request completed successfully")
                
        except Exception as e:
            logger.error(f"Error in chat: {e}")
            raise
    
    return StreamingResponse(generate(), media_type='text/event-stream',
        headers={
            'cache-control': 'no-cache, no-transform', 
            'connection': 'keep-alive'
        })

if __name__ == '__main__':
    logger.info("App Initiated Successfully")
    uvicorn.run(app, host='0.0.0.0', port=8000)
```

### File: package.json
```json
{
  "name": "market-insight",
  "version": "1.0.0",
  "description": "Market Insight - Stock Analysis Platform",
  "scripts": {
    "dev": "concurrently \"npm run dev:backend\" \"npm run dev:frontend\"",
    "dev:backend": "cd . && python main.py",
    "dev:frontend": "cd frontend && npm run dev",
    "install:all": "cd frontend && npm install"
  },
  "devDependencies": {
    "concurrently": "^9.1.0"
  }
}

```

### File: README.md
```md
# Market Insight

An AI-powered stock market analysis platform that provides comprehensive financial data and intelligent insights through a conversational interface.

## Overview

Market Insight leverages advanced AI agents to deliver real-time stock market information, financial analysis, and investment insights. The platform combines the power of LangChain and OpenAI's language models with Yahoo Finance data to create an intelligent assistant for stock market research.

## Technology Stack

**Backend:**
- FastAPI for high-performance API endpoints
- LangChain & LangGraph for AI agent orchestration
- OpenAI GPT models for intelligent responses
- YFinance for financial data retrieval
- Langfuse for observability and tracing

**Frontend:**
- Modern React-based interface
- Real-time streaming responses
- Responsive design for all devices

## Getting Started

### Prerequisites
- Python 3.x
- Node.js (for frontend)
- OpenAI API key

### Installation

1. Clone the repository
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables in `.env` file
4. Install frontend dependencies:
   ```bash
   cd frontend
   npm install
   ```
5. Run the backend server:
   ```bash
   python main.py
   ```
6. Run the frontend development server:
   ```bash
   cd frontend
   npm run dev
   ```
7. Access the API at `http://localhost:8000` and frontend at `http://localhost:5173`

## Project Structure

```
MarketInsight/
├── components/     # AI agent configuration
├── utils/          # Tools and utilities
├── config/         # Configuration files
├── frontend/       # React frontend application
└── main.py         # FastAPI server entry point
```

## API Capabilities

The platform provides 16 specialized tools for comprehensive stock analysis:
- Stock price tracking
- Historical data analysis
- Financial statements (Balance Sheet, Income Statement, Cash Flow)
- Company information and ratios
- Dividend and split history
- Ownership and holder data
- Insider transactions
- Analyst recommendations
- Company ticker lookup
```

### File: requirements.txt
```txt
fastapi
pydantic
uvicorn
python-dotenv
langchain-openai
langgraph
yfinance
langchain
langchain-core
langfuse
```

### File: frontend\package.json
```json
{
  "name": "frontend",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc -b && vite build",
    "lint": "eslint .",
    "preview": "vite preview"
  },
  "dependencies": {
    "@crayonai/react-ui": "^0.9.7",
    "@thesysai/genui-sdk": "^0.7.7",
    "react": "^19.2.0",
    "react-dom": "^19.2.0"
  },
  "devDependencies": {
    "@eslint/js": "^9.39.1",
    "@types/node": "^24.10.1",
    "@types/react": "^19.2.5",
    "@types/react-dom": "^19.2.3",
    "@vitejs/plugin-react": "^5.1.1",
    "eslint": "^9.39.1",
    "eslint-plugin-react-hooks": "^7.0.1",
    "eslint-plugin-react-refresh": "^0.4.24",
    "globals": "^16.5.0",
    "typescript": "~5.9.3",
    "typescript-eslint": "^8.46.4",
    "vite": "^7.2.4"
  }
}

```

### File: render.yaml
```yaml
services:
  - type: web
    name: market-insight-backend
    env: python
    buildCommand: "pip install -r requirements.txt"
    startCommand: "uvicorn main:app --host 0.0.0.0 --port $PORT"
    envVars:
      - key: PYTHON_VERSION
        value: 3.11.0
```

### File: config\config.py
```py
from pydantic import BaseModel

class PromptObject(BaseModel):
    content: str
    id: str
    role: str

class RequestObject(BaseModel):
    prompt: PromptObject
    threadId: str
    responseId: str
```

### File: config\__init__.py
```py

```

### File: frontend\eslint.config.js
```js
import js from '@eslint/js'
import globals from 'globals'
import reactHooks from 'eslint-plugin-react-hooks'
import reactRefresh from 'eslint-plugin-react-refresh'
import tseslint from 'typescript-eslint'
import { defineConfig, globalIgnores } from 'eslint/config'

export default defineConfig([
  globalIgnores(['dist']),
  {
    files: ['**/*.{ts,tsx}'],
    extends: [
      js.configs.recommended,
      tseslint.configs.recommended,
      reactHooks.configs.flat.recommended,
      reactRefresh.configs.vite,
    ],
    languageOptions: {
      ecmaVersion: 2020,
      globals: globals.browser,
    },
  },
])

```

### File: frontend\index.html
```html
<!doctype html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <link rel="icon" type="image/png" href="/icon.png" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Market Insight | AI Analysis</title>
  <meta name="description" content="AI-powered stock market analysis platform with real-time data and insights" />
  <meta name="keywords" content="stock analysis, AI, market insight, financial data" />
  <meta property="og:title" content="Market Insight - AI Stock Analysis" />
  <meta property="og:description" content="Get real-time stock market insights powered by AI" />
</head>

<body>
  <div id="root"></div>
  <script type="module" src="/src/main.tsx"></script>
</body>

</html>
```

### File: frontend\tsconfig.app.json
```json
{
  "compilerOptions": {
    "tsBuildInfoFile": "./node_modules/.tmp/tsconfig.app.tsbuildinfo",
    "target": "ES2022",
    "useDefineForClassFields": true,
    "lib": ["ES2022", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "types": ["vite/client"],
    "skipLibCheck": true,

    /* Bundler mode */
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "verbatimModuleSyntax": true,
    "moduleDetection": "force",
    "noEmit": true,
    "jsx": "react-jsx",

    /* Linting */
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "erasableSyntaxOnly": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedSideEffectImports": true
  },
  "include": ["src"]
}

```

### File: frontend\tsconfig.json
```json
{
  "files": [],
  "references": [
    { "path": "./tsconfig.app.json" },
    { "path": "./tsconfig.node.json" }
  ]
}

```

### File: frontend\tsconfig.node.json
```json
{
  "compilerOptions": {
    "tsBuildInfoFile": "./node_modules/.tmp/tsconfig.node.tsbuildinfo",
    "target": "ES2023",
    "lib": ["ES2023"],
    "module": "ESNext",
    "types": ["node"],
    "skipLibCheck": true,

    /* Bundler mode */
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "verbatimModuleSyntax": true,
    "moduleDetection": "force",
    "noEmit": true,

    /* Linting */
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "erasableSyntaxOnly": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedSideEffectImports": true
  },
  "include": ["vite.config.ts"]
}

```

### File: frontend\vercel.json
```json
{
    "buildCommand": "npm run build",
    "outputDirectory": "dist",
    "devCommand": "npm run dev",
    "installCommand": "npm install"
}
```

### File: frontend\vite.config.ts
```ts
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true
      },
    },
  },
})

```

### File: frontend\src\App.css
```css
/* CSS Custom Properties */
:root {
  --bg-primary: rgba(10, 10, 15, 0.98);
  --bg-secondary: rgba(20, 20, 30, 0.95);
  --bg-hover: rgba(30, 30, 45, 0.98);
  --border-color: rgba(255, 255, 255, 0.15);
  --border-hover: rgba(255, 255, 255, 0.25);
  --text-primary: rgba(255, 255, 255, 0.95);
  --text-secondary: rgba(255, 255, 255, 0.85);
  --shadow-sm: 0 4px 12px rgba(0, 0, 0, 0.2);
  --shadow-md: 0 8px 20px rgba(0, 0, 0, 0.3);
  --shadow-lg: 0 12px 24px rgba(0, 0, 0, 0.4);
  --transition-smooth: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

/* Base Styles */
html,
body {
  margin: 0;
  padding: 0;
  height: 100%;
  /* Use dvh for better mobile support */
  min-height: 100dvh;
  overflow: hidden;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  /* Prevent white space on mobile keyboard */
  position: fixed;
  width: 100%;
}

#root {
  width: 100%;
  height: 100%;
}

.app-container {
  width: 100%;
  height: 100vh;
  /* Use dvh for mobile viewport */
  min-height: 100dvh;
  overflow: hidden;
  position: relative;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

.app-container * {
  font-family: inherit !important;
}

/* Recommendations Overlay */
.recommendations-overlay {
  position: relative;
  z-index: 10;
  margin-bottom: 1rem;
  width: 100%;
  max-width: 800px;
  margin-left: auto;
  margin-right: auto;
  padding: 0 1rem;
}

/* Recommendations Container */
.recommendations-container {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 0.75rem;
  width: 100%;
}

/* Recommendation Box */
.recommendation-box {
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
  border-radius: 8px;
  padding: 1rem;
  cursor: pointer;
  transition: var(--transition-smooth);
  backdrop-filter: blur(10px);
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
  position: relative;
  overflow: hidden;
  box-shadow: var(--shadow-sm);
}

/* Gradient overlay effect */
.recommendation-box::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg,
      rgba(255, 255, 255, 0.08) 0%,
      transparent 100%);
  opacity: 0;
  transition: opacity 0.3s ease;
  pointer-events: none;
}

.recommendation-box:hover::before {
  opacity: 1;
}

/* Hover state - GPU accelerated */
.recommendation-box:hover {
  background: var(--bg-hover);
  border-color: var(--border-hover);
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg);
}

/* Active state */
.recommendation-box:active {
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

/* Focus state for accessibility */
.recommendation-box:focus {
  outline: 2px solid rgba(99, 102, 241, 0.5);
  outline-offset: 2px;
}

/* Recommendation Icon */
.recommendation-icon {
  font-size: 1.5rem;
  flex-shrink: 0;
  line-height: 1;
  filter: grayscale(0.2);
  transition: filter 0.3s ease, transform 0.3s ease;
}

.recommendation-box:hover .recommendation-icon {
  filter: grayscale(0);
  transform: scale(1.1);
}

/* Recommendation Text */
.recommendation-text {
  margin: 0;
  color: var(--text-secondary);
  font-size: 0.8125rem;
  line-height: 1.4;
  flex: 1;
  transition: color 0.3s ease;
  font-weight: 500;
}

.recommendation-box:hover .recommendation-text {
  color: var(--text-primary);
}

/* Responsive Design */
@media (max-width: 768px) {
  .recommendations-container {
    grid-template-columns: 1fr;
    gap: 0.5rem;
  }

  .recommendation-box {
    padding: 0.875rem;
  }

  .recommendation-icon {
    font-size: 1.25rem;
  }

  .recommendation-text {
    font-size: 0.8125rem;
  }

  .recommendations-overlay {
    padding: 0 0.75rem;
  }
}

/* Tablet breakpoint */
@media (min-width: 769px) and (max-width: 1024px) {
  .recommendations-overlay {
    max-width: 700px;
  }
}

/* Smooth animations */
@media (prefers-reduced-motion: reduce) {

  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

