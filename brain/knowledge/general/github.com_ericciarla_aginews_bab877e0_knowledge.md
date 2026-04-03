---
id: github.com-ericciarla-aginews-bab877e0-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:45.559736
---

# KNOWLEDGE EXTRACT: github.com_ericciarla_aginews_bab877e0
> **Extracted on:** 2026-04-01 13:52:05
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007523510/github.com_ericciarla_aginews_bab877e0

---

## File: `.gitignore`
```
# See https://help.github.com/articles/ignoring-files/ for more about ignoring files.

# dependencies
/node_modules
/.pnp
.pnp.*
.yarn/*
!.yarn/patches
!.yarn/plugins
!.yarn/releases
!.yarn/versions

# testing
/coverage

# next.js
/.next/
/out/

# production
/build

# misc
.DS_Store
*.pem

# debug
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# env files (can opt-in for committing if needed)
.env*

# vercel
.vercel

# typescript
*.tsbuildinfo
next-env.d.ts
```

## File: `README.md`
```markdown
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

## File: `backend/.gitignore`
```
node_modules
.env
.vercel
dist
```

## File: `backend/combinedText.json`
```json
{
  "stories": [
    {
      "headline": "Large Language Models in National Security Applications",
      "link": "https://arxiv.org/abs/2407.03453"
    },
    {
      "headline": "Artificial Intelligence, Scientific Discovery, and Product Innovation [pdf]",
      "link": "https://aidantr.github.io/files/AI_innovation.pdf"
    },
    {
      "headline": "A stubborn computer scientist accidentally launched the deep learning boom",
      "link": "https://arstechnica.com/ai/2024/11/how-a-stubborn-computer-scientist-accidentally-launched-the-deep-learning-boom/"
    },
    {
      "headline": "Announcing llama-ocr –  a free + open source OCR tool!\n\nIt takes documents (images for now) &amp; outputs markdown, and does really well for complex receipts, PDFs with tables/charts, ect...\n\nPowered by Llama 3.2 vision on @togethercompute &amp; available on npm today! https://t.co/OZFinqU6QW https://t.co/6J6Gr5C5Xe",
      "link": "https://x.com/i/status/1856402928086725020"
    },
    {
      "headline": "Can #AI truly understand long videos? Tobias Weyand &amp; the Google Research team are testing the limits w/ Neptune, an open-source benchmark for long video understanding. Dive into the details &amp; see how AI tackles temporal reasoning, cause &amp; effect, &amp; more →https://t.co/jNkgEYkdFA https://t.co/rXPBdRS9TM",
      "link": "https://x.com/i/status/1856394450445996405"
    },
    {
      "headline": "Google Research is helping firefighters with FireSat, an innovative satellite constellation that delivers real-time, high-resolution wildfire imagery so firefighters can detect and respond to fires faster. Learn how FireSat is making a difference: https://t.co/RcKhZSihaP https://t.co/YLPsMg2Vzd",
      "link": "https://x.com/i/status/1856101172634902898"
    },
    {
      "headline": "Introducing a novel zero-shot image-to-image model designed for personalized and stylized portraits. Learn how it both accurately preserves the similarity of the input facial image and faithfully applies the artistic style specified in the text prompt →https://t.co/ULxXfeOJl3 https://t.co/8trUi8yjZb",
      "link": "https://x.com/i/status/1856072910412112207"
    },
    {
      "headline": "Floods are among the most widespread natural disasters. Here we describe our new flood forecasting model for state-of-the-art 7-day lead time prediction, expanded forecasts on ungauged watersheds for expert use, and a new reanalysis &amp; re-forecast dataset. https://t.co/mJZWxkpD7C https://t.co/hIUX61NxDc",
      "link": "https://x.com/i/status/1856004232626774409"
    },
    {
      "headline": "What if AI could book your appointments, collaborate with others, and navigate life’s complexities on your behalf?\n\nOur latest podcast with @FryRsquared and Senior Research Scientist @IasonGabriel explores the exciting possibilities and ethical challenges of a world with AI… https://t.co/DzsULZOrWR https://t.co/y8skAqoQIZ",
      "link": "https://x.com/i/status/1856037194089074773"
    },
    {
      "headline": "Introducing generative ads on @everartai. ✨\n\nGenerate ad-format images from existing ones, filling in missing pixels.\n\nCompatible with Instagram, Facebook, and Google ads. https://t.co/w7eNRhzHHU",
      "link": "https://x.com/i/status/1856067458546946300"
    },
    {
      "headline": "👀 https://t.co/vVOyxxzRak",
      "link": "https://x.com/i/status/1856415244140347652"
    },
    {
      "headline": "Build distributed AI agent networks with type-safe async messaging with autogen from @Microsoft \n\n33.6K stars 🌟 in Github\n\nWhat it offers:\n\n→ Multi-language support (Python, .NET) with typed interfaces and enforced type checking\n\n→ Modular architecture with three API layers:… https://t.co/sUOBOH7PQq https://t.co/8ZyKAaqhzE",
      "link": "https://x.com/i/status/1856409023798812953"
    },
    {
      "headline": "This study released on 5-Nov predicted Trump victory for 2024 with ~300 electoral votes.\n\nThe methodology was about finding if virtual voters in AI's head predict real voters at the polls. \n\nBasically, AI mimics voters to see election's future.\n\nUsed demographic data to simulate… https://t.co/QiZemnsacT https://t.co/Xe3MYVXKBL",
      "link": "https://x.com/i/status/1856391768696336425"
    },
    {
      "headline": "Audiobook recommendations from Elon Musk https://t.co/kFp0Eic1oM https://t.co/gqfBC0lIDv",
      "link": "https://x.com/i/status/1856382382414459233"
    },
    {
      "headline": "Open-source alternative to OpenAI's voice.\n\nExtends text-based LLM to have native \"listening\" ability. Think of it as an open data, open weight, on device Siri.\n\nWhat it offers:\n\n📌 Implements native \"listening\" abilities in LLMs, similar to Siri but runs locally on-device\n\n📌… https://t.co/DPvM6DK1TK https://t.co/RbLvLdVEpX",
      "link": "https://x.com/i/status/1856356418582110492"
    },
    {
      "headline": "🚀 Very interesting paper from the Tianqiao &amp; Chrissy Chen Institute (TCCI / @ChenInstitute) that takes AI Long-Term Memory to the next level!\n\n🏆 Achieved first place on GAIA benchmark with 40.53% accuracy on test set\n\n🧠 TCCI's AI researchers applied neuroscience knowledge to… https://t.co/4Odkq7xiMu https://t.co/ln50eGqISO",
      "link": "https://x.com/i/status/1856323830232559951"
    },
    {
      "headline": "The upper bounds of AI's capability stretch far beyond human cognition.\n\n- Anthropic CEO Dario Amodei\n\nFrom the 5-hour long Lex Fridman's new podcast. (link in comment) https://t.co/yBZ1BhqG9w",
      "link": "https://x.com/i/status/1856257625652113809"
    },
    {
      "headline": "The AGI Countdown Begins: 2026 / 2027 - Anthropic CEO Dario Amodei's .\n\nLove is infectious confidence and excitement.\n\nFrom the 5-hour long Lex Fridman's new podcast. (link in comment)\n\nThis is one of the best 5 hours you can spend to understand AI and its future timeline. https://t.co/AnyOFY46S9",
      "link": "https://x.com/i/status/1856248602395594784"
    },
    {
      "headline": "Layer-of-Thoughts (LoT) prompting filters LLM outputs through hierarchical layers, like a smart document sieve.\n\nAnd this structured thought layers turn messy LLM responses into precise legal document retrieval, as proposed in this paper,\n\nOriginal Problem 🎯:\n\nCurrent prompting… https://t.co/nAqranZjo8 https://t.co/vdZCqpcCcF",
      "link": "https://x.com/i/status/1856084192469381455"
    },
    {
      "headline": "Small models learn developer preferences by studying how code naturally evolves.\n\nCODEFAVOR, proposed in this paper, trains small models to judge code quality like expert developers, but 34x cheaper vs models with 6 ∼ 9× more parameters.\n\nOriginal Problem 🎯:\n\nEvaluating code… https://t.co/Rxf7laLC58 https://t.co/AOBglXpzwX",
      "link": "https://x.com/i/status/1856083013458898969"
    },
    {
      "headline": "🚀Now it is the time, Nov. 11 10:24! The perfect time for our best coder model ever! Qwen2.5-Coder-32B-Instruct! \n\nWait wait... it's more than a big coder! It is a family of coder models! Besides the 32B coder, we have coders of 0.5B / 1.5B / 3B / 7B / 14B! As usual, we not only… https://t.co/gnH9H2Udsq https://t.co/PjCaXRMdiC",
      "link": "https://x.com/i/status/1856040217897251044"
    },
    {
      "headline": "Agree.com—Free e-signature for everyone",
      "link": "https://www.producthunt.com/posts/agree-com-2"
    },
    {
      "headline": "Segwise—Automatically catches issues that affect your mobile ROAS",
      "link": "https://www.producthunt.com/posts/segwise"
    },
    {
      "headline": "EarlyAI—AI Agent for test code generation",
      "link": "https://www.producthunt.com/posts/earlyai"
    },
    {
      "headline": "Cerebrium—Serverless infra for AI/ML apps - Build faster and cheaper",
      "link": "https://www.producthunt.com/posts/cerebrium"
    },
    {
      "headline": "Universal-2 by AssemblyAI—Speech-to-Text API for conversational data",
      "link": "https://www.producthunt.com/posts/universal-2-by-assemblyai"
    },
    {
      "headline": "Luqo AI—The new AI language learning experience",
      "link": "https://www.producthunt.com/posts/luqo-ai"
    },
    {
      "headline": "Draft—AI powered to-do list",
      "link": "https://www.producthunt.com/posts/draft-27844448-74c3-451d-919b-116c24c23098"
    },
    {
      "headline": "Inquir—Search-as-a-service and RAG builder",
      "link": "https://www.producthunt.com/posts/inquir"
    },
    {
      "headline": "CuriosityXR—Learn with 1M+ 3D models & AI in Mixed Reality",
      "link": "https://www.producthunt.com/posts/curiosityxr"
    },
    {
      "headline": "Endgame 2.0—Automate your account research and planning with AI",
      "link": "https://www.producthunt.com/posts/endgame-2-0"
    },
    {
      "headline": "New SoTA Open Background Removal model: RMBG 2.0 🔥\n\n&gt; On the Hub &amp; Transformers! 🤗 https://t.co/TfjRAJc2Gg",
      "link": "https://x.com/i/status/1856423773794148862"
    },
    {
      "headline": "Enjoy Qwen 2.5 Coder 32B aka Smol AGI on Hugging Chat - 100% free and unlimited queries 🔥 https://t.co/1z1d7IkQbi https://t.co/Yq9On1TfWK",
      "link": "https://x.com/i/status/1856111604988842357"
    },
    {
      "headline": "Beats GPT4o, rivals Claude Sonnet - can run on the cheapest GPU VPS available!\n\nOpen source is the way to go! https://t.co/sbD0K3rjwF https://t.co/Yq9On1TfWK",
      "link": "https://x.com/i/status/1856081075853770795"
    },
    {
      "headline": "If this doesn’t make you bullish on Open Source - I don’t know what will! 🔥\n\nThat’s a 32B LLM that can easily fit on a\n ~0.8 USD/ hour GPU - spitting ungodly num of tokens\n\nBack of the napkin math:\n- fp16/ bf16 - 32GB VRAM (would fit on a L40S)\n- 8-bit - 16GB VRAM (L4)\n- 4-bit -… https://t.co/C1P0X31HOx https://t.co/7UHdB2jjwl",
      "link": "https://x.com/i/status/1856032158814519338"
    },
    {
      "headline": "Wohoo! DeepMind released AlphaFold 3 inference codebase, model weights and an on-demand server! ⚡\n\nAlphaFold  can generate highly accurate biomolecular structure predictions containing proteins, DNA, RNA, ligands, ions, and also model chemical modifications for proteins and… https://t.co/K7bvKclMz1 https://t.co/XeQ0XJZpPE",
      "link": "https://x.com/i/status/1855956584981020901"
    },
    {
      "headline": "Amazon offers free computing power to AI researchers, aiming to challenge Nvidia",
      "link": "https://www.reuters.com/technology/artificial-intelligence/amazon-offers-free-computing-power-ai-researchers-aiming-challenge-nvidia-2024-11-12/"
    },
    {
      "headline": "Baidu bolsters AI lineup with enhanced text-to-image tech, no-code app builder",
      "link": "https://www.reuters.com/technology/artificial-intelligence/baidu-bolsters-ai-lineup-with-text-to-image-generator-no-code-app-builder-2024-11-12/"
    }
  ]
}
```

## File: `backend/package.json`
```json
{
  "name": "researcher-backend",
  "version": "1.0.0",
  "main": "src/index.ts",
  "scripts": {
    "start": "nodemon src/index.ts",
    "build": "tsc",
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "@types/express": "^4.17.21",
    "@types/node": "^20.10.2",
    "@types/node-cron": "^3.0.11",
    "nodemon": "^3.0.2",
    "pre-commit": "^1.2.2",
    "rimraf": "^5.0.5",
    "ts-node": "^10.9.1",
    "typescript": "^5.3.2"
  },
  "dependencies": {
    "@mendable/firecrawl-js": "^1.8.1",
    "@supabase/supabase-js": "^2.46.1",
    "dotenv": "^14.3.2",
    "express": "^4.18.2",
    "express-async-handler": "^1.2.0",
    "firecrawl": "^1.7.2",
    "node-cron": "^3.0.3",
    "openai": "^4.72.0",
    "resend": "^4.0.1-alpha.0",
    "together-ai": "^0.9.0",
    "ts-node-dev": "^2.0.0"
  }
}
```

## File: `backend/requests.http`
```
### LOCAL
POST http://localhost:8000/query HTTP/1.1
Content-Type: application/json

{
    "query": "How does a long context LLM work?"
}


### PROD
POST https://researcher-backend-production.up.railway.app/query
Content-Type: application/json

{
    "query": "What is the capital of France?"
}
```

## File: `backend/tsconfig.json`
```json
{
  "compilerOptions": {
    "target": "ES6",                          // Specify ECMAScript target version
    "module": "commonjs",                     // Specify module code generation
    "outDir": "./dist",                       // Redirect output structure to the directory
    "rootDir": "./src",                       // Specify the root directory of input files
    "strict": true,                           // Enable all strict type-checking options
    "esModuleInterop": true,                  // Enables emit interoperability between CommonJS and ES Modules
    "skipLibCheck": true,                     // Skip type checking of declaration files
    "forceConsistentCasingInFileNames": true  // Disallow inconsistently-cased references to the same file
  },
  "include": ["src/**/*"],                    // Include all files in the src directory
  "exclude": ["node_modules", "dist"]         // Exclude node_modules and dist directories
}
```

## File: `backend/src/index.ts`
```typescript
import { handleCron } from "./controllers/cron"
import cron from 'node-cron';
import dotenv from 'dotenv';

dotenv.config();

//async function main() {
//  console.log(`Starting process to send newsletter...`);
//  await handleCron();
//}
// main();

cron.schedule(`0 14 * * *`, async () => {
  console.log(`Starting process to send newsletter...`);
  await handleCron();
});
```

## File: `backend/src/controllers/cron.ts`
```typescript
import { scrapeSources } from '../services/scrapeSources';
import { getCronSources } from '../services/getCronSources';
import { generateNewsletter } from '../services/generateNewsletter'
import { sendNewsletter } from '../services/sendNewsletter'
import fs from 'fs';
export const handleCron = async (): Promise<void> => {
  try {
   
    const cronSources = await getCronSources();
    const rawStories = await scrapeSources(cronSources);
    //const rawStories = fs.readFileSync('./combinedText.json', 'utf8').toString();
    const rawStoriesString = JSON.stringify(rawStories);
    const newsletter = await generateNewsletter(rawStoriesString);
    const result = await sendNewsletter(newsletter!, rawStoriesString);
    console.log(result);
  } catch (error) {
    console.error(error);
  }
}
```

## File: `backend/src/services/generateNewsletter.ts`
```typescript

import FirecrawlApp from '@mendable/firecrawl-js';
import dotenv from 'dotenv';
import OpenAI from 'openai';


dotenv.config();

const app = new FirecrawlApp({apiKey: process.env.FIRECRAWL_API_KEY});
const fs = require('fs');

export async function generateNewsletter(rawStories: string) {
  console.log(`Generating newsletter with raw stories (${rawStories.length} characters)...`)


        try {
          const client = new OpenAI();

          const newsletterResponse = await client.chat.completions.create({
            messages: [{ role: 'user', content: `Given a list of raw AI and LLM-related stories sourced from various platforms, create a concise TL;DR-style email newsletter called 'AGI News' with up to the 10 most interesting and impactful stories in HTML format. Prioritize stories that cover product launches, demos, and innovations in AI/LLM technology. Don't forget links!

The newsletter should have the following structure:

Title: 'AGI News – Your Quick Daily Roundup'
Introduction: A one-sentence overview introducing the daily roundup and the newsletter which is a daily AI newsletter sourced by AI agents & Firecrawl 🔥.
Top X Stories: Select up to 10 most noteworthy stories, each summarized in 1-2 sentences with a clickable headline that links to the source.
Each story summary should briefly convey:

Headline: Capture attention with a short, engaging headline.
Highlights: Mention the key takeaway or significance of the story.
Link: Include a hyperlink to the original source for more information.
Example format for each story:

Headline: [Story Headline]
Summary: Brief, compelling summary of the story's main points or implications 1-2 sentences max.
Link: [Insert link]
Prioritize stories that cover product launches, or timely insights relevant to developers, researchers, and founders. Make sure the language is informative but engaging, keeping the overall tone professional and friendly. Do not include any stories that are not in raw stories or are not AI or LLM related. Try not to repeat stories or mention the same company twice in a row (e.g. if you mentioned Anthropic, don't mention Anthropic immediately again in the next story but can mention them later down the list). Ensure the newsletter is formatted in HTML. Do not include \`\`\`html or \`\`\` in the newsletter.  \n\nHere is the raw stories: ${rawStories}` }],
            model: 'o1-preview',
          });
          console.log(`Newsletter generated successfully with ${newsletterResponse.choices[0].message.content?.length} characters.`)

          return newsletterResponse.choices[0].message.content;
    
        } catch (error) {
          console.log("error generating newsletter")
      
        }
}
    
    
```

## File: `backend/src/services/getCronSources.ts`
```typescript
import { createClient } from '@supabase/supabase-js';
import dotenv from 'dotenv';

dotenv.config();

const supabase = createClient(process.env.SUPABASE_URL!, process.env.SUPABASE_SECRET_KEY!);

export async function getCronSources() {
  console.log("Fetching sources...")
    const { data: sources, error } = await supabase
      .from('sources')
      .select('identifier');

    if (error) {
      throw new Error(`Failed to fetch sources: ${error.message}`);
    }

    return sources.map(source => source.identifier);
}
  
```

## File: `backend/src/services/scrapeSources.ts`
```typescript

import FirecrawlApp from '@mendable/firecrawl-js';
import dotenv from 'dotenv';
import OpenAI from 'openai';


dotenv.config();

const app = new FirecrawlApp({apiKey: process.env.FIRECRAWL_API_KEY});
const fs = require('fs');

export async function scrapeSources(sources: string[]) {
  const num_sources = sources.length;
    console.log(`Scraping ${num_sources} sources...`)

    let combinedText: { stories: any[] } = { stories: [] };
    const useTwitter = true;
    const useScrape = true;

    for (const source of sources) {
 
      if (source.includes('x.com')) {
        if (useTwitter) {
        const usernameMatch = source.match(/x\.com\/([^\/]+)/);

        if (usernameMatch) {
            const username = usernameMatch[1];
          
            // Construct and encode the query
            const query = `from:${username} has:media -is:retweet -is:reply`;
            const encodedQuery = encodeURIComponent(query);
          
            // Encode the start time
            const startTime = new Date(Date.now() - 24 * 60 * 60 * 1000).toISOString();
            const encodedStartTime = encodeURIComponent(startTime);
          
            // Corrected API URL with encoded parameters to get tweets and attachments
            const apiUrl = `https://api.x.com/2/tweets/search/recent?query=${encodedQuery}&max_results=10&start_time=${encodedStartTime}`;
          
            // Fetch recent tweets from the Twitter API
            const response = await fetch(apiUrl, {
                headers: {
                  'Authorization': `Bearer ${process.env.X_API_BEARER_TOKEN}`
                }
              });
            
              if (!response.ok) {
                throw new Error(`Failed to fetch tweets for ${username}: ${response.statusText}`);
              }
            
              const tweets = await response.json();
             
            
              if (tweets.meta?.result_count === 0) {
       
          
              } else if (Array.isArray(tweets.data)) {
                console.log(`Tweets found from username ${username}`);
                const stories = tweets.data.map((tweet: any) => {
                  return {
                    headline: tweet.text,
                    link: `https://x.com/i/status/${tweet.id}`,
                    date_posted: startTime
                  };
                });
                combinedText.stories.push(...stories);
              } else {
                console.error('Expected tweets.data to be an array:', tweets.data);
              }
           
            
          }
        }
      } else {
        if (useScrape) {
        const scrapeResponse = await app.scrapeUrl(source, {
          formats: ['markdown'],
        });
        
        if (!scrapeResponse.success) {
          throw new Error(`Failed to scrape: ${scrapeResponse.error}`)
        }

        // Feed the scrape response to GPT-4o and get only stories from today
        
        try {
          const client = new OpenAI();

          const LLMFilterResponse = await client.chat.completions.create({
            messages: [{ role: 'user', content: `Today is ${new Date().toLocaleDateString()}. Return only today's AI or LLM related story or post headlines and links in JSON format from the following scraped content. They must be posted today. The format should be {"stories": [{"headline": "headline1", "link": "link1", "date_posted": "date1"}, {"headline": "headline2", "link": "link2", "date_posted": "date2"}, ...]}. If there are no stories or posts related to AI or LLMs from today, return {"stories": []}. The source link is ${source}. If the story or post link is not absolute, make it absolute with the source link. RETURN ONLY JSON IN THE SPECIFIED FORMAT DO NOT INCLUDE MARKDOWN OR ANY OTHER TEXT JUST THE PURE JSON. Do not include \`\`\`json or \`\`\` or any other markdown formatting. Scraped Content:\n\n\n${scrapeResponse.markdown} JSON:` }],
            model: 'gpt-4o',
          });

          // Validate the response using the schema
          const todayStories = JSON.parse(LLMFilterResponse.choices[0].message.content!.trim());
          console.log(`Found ${todayStories.stories.length} stories from ${source}`)
          combinedText.stories.push(...todayStories.stories);
      
        } catch (error) {
          console.error('Error processing LLM response:', error);
        
        }
      }
    }
    }
    //fs.writeFileSync('./combinedText.json', JSON.stringify(combinedText, null, 2));
    const rawStories = combinedText.stories;
    return rawStories;
  }  
```

## File: `backend/src/services/sendNewsletter.ts`
```typescript

import dotenv from 'dotenv';
import { Resend } from 'resend';
import { createClient } from '@supabase/supabase-js';

dotenv.config();

const resend = new Resend(process.env.RESEND_API_KEY);


export async function sendNewsletter(newsletter: string, rawStories: string) {
  if (newsletter.length <= 750) {
    console.log("Newsletter is too short to send. See newsletter below:");
    console.log(newsletter);
    console.log("Raw stories below:");
    console.log(rawStories);
    return "Newsletter not sent due to insufficient length.";
  }

  try {
    const supabase = createClient(process.env.SUPABASE_URL!, process.env.SUPABASE_SECRET_KEY!);
    const batchSize = 50;
    let start = 0;
    let hasMore = true;

    while (hasMore) {
      const { data: subscribers, error } = await supabase
        .from('users')
        .select('email')
        .range(start, start + batchSize - 1);

      if (error) {
        throw new Error(`Failed to fetch subscribers: ${error.message}`);
      }

      if (subscribers.length < batchSize) {
        hasMore = false;
      }

      console.log(`Sending newsletter to ${subscribers.length} subscribers`);

      for (const subscriber of subscribers) {
        const unsubscribe_link = `https://www.aginews.io/api/unsubscribe?email=${subscriber.email}`;
       
        await resend.emails.send({
          from: 'Eric <eric@tryfirecrawl.com>',
          to: subscriber.email,
          subject: 'AGI News – Your Quick Daily Roundup',
          html: newsletter + `<br><br><a href="${unsubscribe_link}">Unsubscribe</a>`,
        });
        
      }

      start += batchSize;
    }
    return "Success sending newsletter on " + new Date().toISOString();
  } catch (error) {
    console.log("error generating newsletter");
  }
}
```

## File: `frontend/.gitignore`
```
# See https://help.github.com/articles/ignoring-files/ for more about ignoring files.

# dependencies
/node_modules
/.pnp
.pnp.*
.yarn/*
!.yarn/patches
!.yarn/plugins
!.yarn/releases
!.yarn/versions

# testing
/coverage

# next.js
/.next/
/out/

# production
/build

# misc
.DS_Store
*.pem

# debug
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# env files (can opt-in for committing if needed)
.env*

# vercel
.vercel

# typescript
*.tsbuildinfo
next-env.d.ts
```

## File: `frontend/README.md`
```markdown
This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/brain/knowledge/docs_legacy/app/api-reference/cli/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/brain/knowledge/docs_legacy/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/brain/knowledge/docs_legacy/app/building-your-application/deploying) for more details.
```

## File: `frontend/next.config.ts`
```typescript
import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* config options here */
};

export default nextConfig;
```

## File: `frontend/package.json`
```json
{
  "name": "newslettermaker",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "@supabase/supabase-js": "^2.46.1",
    "dotenv": "^16.4.5",
    "next": "15.0.3",
    "react": "19.0.0-rc-66855b96-20241106",
    "react-dom": "19.0.0-rc-66855b96-20241106",
    "resend": "^4.0.1-alpha.0"
  },
  "devDependencies": {
    "@types/node": "^20",
    "@types/react": "^18",
    "@types/react-dom": "^18",
    "postcss": "^8",
    "tailwindcss": "^3.4.1",
    "typescript": "^5"
  }
}
```

## File: `frontend/postcss.config.mjs`
```
/** @type {import('postcss-load-config').Config} */
const config = {
  plugins: {
    tailwindcss: {},
  },
};

export default config;
```

## File: `frontend/tailwind.config.ts`
```typescript
import type { Config } from "tailwindcss";

export default {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        background: "var(--background)",
        foreground: "var(--foreground)",
      },
    },
  },
  plugins: [],
} satisfies Config;
```

## File: `frontend/tsconfig.json`
```json
{
  "compilerOptions": {
    "target": "ES2017",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "plugins": [
      {
        "name": "next"
      }
    ],
    "paths": {
      "@/*": ["./*"]
    }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
  "exclude": ["node_modules"]
}
```

## File: `frontend/app/globals.css`
```css
@tailwind base;
@tailwind components;
@tailwind utilities;

:root {
  --background: #ffffff;
  --foreground: #171717;
}

@media (prefers-color-scheme: dark) {
  :root {
    --background: #0a0a0a;
    --foreground: #ededed;
  }
}

body {
  color: var(--foreground);
  background: var(--background);
  font-family: Arial, Helvetica, sans-serif;
}
```

## File: `frontend/app/layout.tsx`
```tsx
import type { Metadata } from "next";
import localFont from "next/font/local";
import "./globals.css";

const geistSans = localFont({
  src: "./fonts/GeistVF.woff",
  variable: "--font-geist-sans",
  weight: "100 900",
});
const geistMono = localFont({
  src: "./fonts/GeistMonoVF.woff",
  variable: "--font-geist-mono",
  weight: "100 900",
});

export const metadata: Metadata = {
  title: "AGI News",
  description: "A daily AI newsletter sourced by AI agents & Firecrawl 🔥",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased`}
      >
        {children}
      </body>
    </html>
  );
}
```

## File: `frontend/app/page.tsx`
```tsx
"use client";
import { useState } from "react";

export default function Home() {
  const [email, setEmail] = useState("");
  const [apiMessage, setApiMessage] = useState("");

  // Handle form submission
  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    try {
      const response = await fetch("/api/service", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ email })
      });
      const data = await response.json();
      setApiMessage("Thank you for adding your email to AGI News 🚀");
    } catch (error) {
      setApiMessage("Error calling API");
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen p-8 pb-20 sm:p-20 font-[family-name:var(--font-geist-sans)] relative">
      {/* Header */}
      <h1 className="text-6xl font-bold mb-2">AGI News ✨</h1>
      <h2 className="text-lg mb-8">A daily AI newsletter that's completely sourced by autonomous AI agents.</h2>
      
      <form onSubmit={handleSubmit} className="flex items-center gap-4">
        {/* Email Input */}
       
        <input 
          type="email"
          id="email"
          placeholder="Enter your email"
          className="border px-4 py-2 mr-4 rounded-full h-10 sm:h-12"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />

        {/* Submit Button */}
        <button
          type="submit"
          className="rounded-full border border-solid border-black/[.08] dark:border-white/[.145] transition-colors flex items-center justify-center hover:bg-[#f2f2f2] dark:hover:bg-[#1a1a1a] hover:border-transparent text-sm sm:text-base h-10 sm:h-12 px-4 sm:px-5"
        >
          Join
        </button>
     
       
      </form>
       {/* API Response Message */}
       {apiMessage && (
          <p className="text-sm font-[family-name:var(--font-geist-mono)] mt-4">
            {apiMessage}
          </p>
        )}
      {/* Footer */}
      <h2 className="absolute bottom-4 text-sm ">
        This is an <a href="https://github.com/ericciarla/aginews" target="_blank" rel="noopener noreferrer">open source project</a> built with AI Agents, <a href="https://resend.com" target="_blank" rel="noopener noreferrer">Resend</a>, and <a href="https://firecrawl.dev" target="_blank" rel="noopener noreferrer">Firecrawl 🔥</a>
      </h2>
    </div>
  );
}
```

## File: `frontend/app/api/service/route.ts`
```typescript
// /pages/api/service.js or /app/api/service/route.js (depending on your Next.js version)
import { NextResponse } from 'next/server';
import { createClient } from '@supabase/supabase-js';
import dotenv from 'dotenv';
import { Resend } from 'resend';

dotenv.config();

// Initialize Supabase client
const supabaseUrl = process.env.SUPABASE_URL;
const supabaseKey = process.env.SUPABASE_SECRET_KEY;
const supabase = createClient(supabaseUrl!, supabaseKey!);

// Handle POST requests
export async function POST(request: Request) {
  try {
    const { email, sources } = await request.json();

    // Check if the user already exists
    let { data: existingUser, error: userError } = await supabase
      .from('users')
      .select('*')
      .eq('email', email)
      .single();

    if (userError && userError.code !== 'PGRST116') {
      // PGRST116: No rows found, which is acceptable
      throw userError;
    }

    // If user doesn't exist, insert them
    let userId;
    if (!existingUser) {
      const { data: newUser, error: insertUserError } = await supabase
        .from('users')
        .insert({ email })
        .select()
        .single();

      if (insertUserError) throw insertUserError;
      userId = newUser.id;
    } else {
      userId = existingUser.id;
    }

    const resend = new Resend(process.env.RESEND_API_KEY);

    const data = await resend.emails.send({
      from: 'eric@tryfirecrawl.com',
      to: email,
      subject: 'Hello from AGI News',
      text: 'Congratulations! You have successfully subscribed to AGI News. We will send you a daily email with the latest news in AI starting tomorrow.',
    });

    return NextResponse.json({ message: 'Data inserted successfully and email sent!' });
  } catch (error) {
    console.error(error);
    if (error instanceof Error) {
      return NextResponse.json({ error: error.message }, { status: 500 });
    } else {
      return NextResponse.json({ error: 'An unknown error occurred' }, { status: 500 });
    }
  }
}
```

## File: `frontend/app/api/unsubscribe/route.ts`
```typescript

import { NextResponse } from 'next/server';
import { createClient } from '@supabase/supabase-js';
import dotenv from 'dotenv';
import { Resend } from 'resend';

dotenv.config();

// Initialize Supabase client
const supabaseUrl = process.env.SUPABASE_URL;
const supabaseKey = process.env.SUPABASE_SECRET_KEY;
const supabase = createClient(supabaseUrl!, supabaseKey!);

// Handle GET requests
export async function GET(request: Request) {
  try {
    const { searchParams } = new URL(request.url);
    const email = searchParams.get('email');

    if (!email) {
      return new Response('<html><body><h1 style="color:red;">Error: Email is required</h1></body></html>', {
        status: 400,
        headers: { 'Content-Type': 'text/html' }
      });
    }

    // Delete the user from the database
    const { error: deleteError } = await supabase
      .from('users')
      .delete()
      .eq('email', email);

    if (deleteError) throw deleteError;

    return new Response('<html><body><h1 style="color:green;">Successfully unsubscribed</h1></body></html>', {
      headers: { 'Content-Type': 'text/html' }
    });
  } catch (error) {
    console.error(error);
    const errorMessage = error instanceof Error ? error.message : 'An unknown error occurred';
    return new Response(`<html><body><h1 style="color:red;">Error: ${errorMessage}</h1></body></html>`, {
      status: 500,
      headers: { 'Content-Type': 'text/html' }
    });
  }
}
```

