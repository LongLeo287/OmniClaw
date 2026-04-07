---
id: aginews
type: knowledge
owner: OA_Triage
---
# aginews
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# AGI News ✨

AGI News is a daily AI newsletter that's completely sourced by autonomous AI agents.

This is an open-source project built with AI Agents, Resend, and Firecrawl 🔥

## Features

- Autonomous AI agents gather the latest AI news.
- Daily newsletter delivery.
- Frontend for subscribing to the newsletter.

## Installation

Clone the repository:

```bash
git clone https://github.com/ericciarla/aginews.git
```

### Frontend Setup

Navigate to the frontend directory:

```bash
cd /frontend
```

Install dependencies:

```bash
npm install
```

Create a `.env` file with the following variables:

```env
SUPABASE_URL=
SUPABASE_SECRET_KEY=
RESEND_API_KEY=
```

Start the development server:

```bash
npm run dev
```

### Backend Setup

Navigate to the backend directory:

```bash
cd /backend
```

Install dependencies:

```bash
npm install
```

Create a `.env` file with the following variables:

```env
FIRECRAWL_API_KEY=
SUPABASE_URL=
SUPABASE_SECRET_KEY=
X_API_BEARER_TOKEN=
OPENAI_API_KEY=
RESEND_API_KEY=
```

Run the backend cron job:

```bash
ts-node src/index.ts
```

## Environment Variables

### Frontend

- `SUPABASE_URL`
- `SUPABASE_SECRET_KEY`

### Backend

- `FIRECRAWL_API_KEY`
- `SUPABASE_URL`
- `SUPABASE_SECRET_KEY`
- `X_API_BEARER_TOKEN`
- `OPENAI_API_KEY`
- `RESEND_API_KEY`

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

```

