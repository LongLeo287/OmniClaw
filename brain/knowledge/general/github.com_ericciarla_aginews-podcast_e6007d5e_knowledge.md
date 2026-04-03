---
id: github.com-ericciarla-aginews-podcast-e6007d5e-kno
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:45.524591
---

# KNOWLEDGE EXTRACT: github.com_ericciarla_aginews-podcast_e6007d5e
> **Extracted on:** 2026-04-01 09:09:14
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007519957/github.com_ericciarla_aginews-podcast_e6007d5e

---

## File: `.gitignore`
```
node_modules
.env
.vercel
dist
```

## File: `README.md`
```markdown
# AGI News Podcast ✨
```

## File: `package.json`
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
    "playht": "^0.13.0",
    "resend": "^4.0.1-alpha.0",
    "together-ai": "^0.9.0",
    "ts-node-dev": "^2.0.0"
  }
}
```

## File: `requests.http`
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

## File: `tsconfig.json`
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

## File: `src/index.ts`
```typescript
import { handleCron } from "./controllers/cron"
import cron from 'node-cron';
import dotenv from 'dotenv';

dotenv.config();

async function main() {
  console.log(`Starting process to generate podcast...`);
  await handleCron();
}
main();


// If you want to run the cron job manually, uncomment the following line:
//cron.schedule(`0 14 * * *`, async () => {
//  console.log(`Starting process to send podcast...`);
//  await handleCron();
//});
```

## File: `src/controllers/cron.ts`
```typescript
import { scrapeSources } from '../services/scrapeSources';
import { getCronSources } from '../services/getCronSources';
import { generatePodcastScript } from '../services/generatePodcastScript'
import { sendPodcast } from '../services/sendPodcast'
import { generatePodcast } from '../services/generatePodcast';

export const handleCron = async (): Promise<void> => {
  try {
    const cronSources = await getCronSources();
    const rawStories = await scrapeSources(cronSources!);
    const rawStoriesString = JSON.stringify(rawStories);
    const podcastScript = await generatePodcastScript(rawStoriesString);
    const podcastUrl = await generatePodcast(podcastScript);
    const result = await sendPodcast(podcastUrl!, "enter email here");
    console.log(result);
  } catch (error) {
    console.error(error);
  }
}
```

## File: `src/services/generatePodcast.ts`
```typescript

import FirecrawlApp from '@mendable/firecrawl-js';
import dotenv from 'dotenv';
import OpenAI from 'openai';
import * as PlayHT from 'playht';


dotenv.config();

export async function generatePodcast(podcastScript: string) {
  console.log(`Generating podcast with podcast script (${podcastScript.length} characters)...`)


        try {
          

          PlayHT.init({
            apiKey: process.env.PLAY_HT_API_KEY!,
            userId: process.env.PLAY_HT_USER_ID!,
            defaultVoiceId: 's3://voice-cloning-zero-shot/9270311b-7879-4bef-bc44-03bc04785a59/original/manifest.json',
            defaultVoiceEngine: 'PlayHT2.0',
          });

          // Generate podcast audio
          const generated = await PlayHT.generate(podcastScript!);
          const { audioUrl } = generated;

          return audioUrl;
    
        } catch (error) {
          console.log("error generating podcast:")
          console.log(error)
          console.log("podcast script:")
          console.log(podcastScript)
        }
}
    
    
```

## File: `src/services/generatePodcastScript.ts`
```typescript


import dotenv from 'dotenv';
import OpenAI from 'openai';
import Together from "together-ai";

dotenv.config();

export async function generatePodcastScript(rawStories: string) {
  console.log(`Generating podcast script with raw stories (${rawStories.length} characters)...`)


        try {
          const together = new Together({ apiKey: process.env.TOGETHER_API_KEY });

          const podcastScriptResponse = await together.chat.completions.create({
            model: "meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo",
            messages: [{ role: 'user', content: `Given a list of raw AI and LLM-related stories sourced from various platforms, create a podcast script for 'AGI News Podcast' featuring Eric, the co-founder of Firecrawl. The output format should be a 'script' object like this containing Eric's script:

{
  "podcast_script": "Podcast script here"
}
  
Do not include any other text or formatting like \`\`\`json or \`\`\` just output the JSON object.


The podcast should have the following structure:

A charming and funny yet professional introduction by Eric followed by a discussion of up to 2 stories.

Each story discussion should include:

- Story Headline: Introduced by Eric. 1 sentence.
- Key Highlights: Discussed by Eric, mentioning the significance or implications of the story. 1 sentences.
- Personal Insights: Eric shares thoughts or experiences related to the story. 1 sentence.

Closing with thanks for listening and a call to action for listeners to subscribe to the podcast.

Ensure the script is engaging and informative, maintaining a professional yet friendly tone. Avoid discussing any stories not present in the raw stories or unrelated to AI or LLM. Format the script in JSON without including any HTML tags. The output format should be a 'script' object like this:

{
  "podcast_script": "Podcast script here"
}

Do not include any other text or formatting like \`\`\`json or \`\`\` just output the JSON object.

Here are the raw stories: ${rawStories}\n\n\n JSON output here (no other text or formatting):` }],
        
          });
          

         // Clean the JSON string inline by removing control characters
          const cleanedPodcastScriptRaw = podcastScriptResponse.choices[0].message?.content?.replace(/[\u0000-\u001F]+/g, '');
            
          // Parse the cleaned JSON string
          const podcast_script = JSON.parse(cleanedPodcastScriptRaw!).podcast_script;

    
          
          return podcast_script;
    
        } catch (error) {
          console.log("error generating podcast")
          console.log(error)
          
      
        }
}
    
    
```

## File: `src/services/getCronSources.ts`
```typescript

import dotenv from 'dotenv';

dotenv.config();



export async function getCronSources() {
  try {
    console.log("Fetching sources...");

    // Hardcoded list of sources
    const sources = [
      { identifier: 'https://news.ycombinator.com/' },
      { identifier: 'https://www.producthunt.com/' },
      { identifier: 'https://www.reuters.com/technology/artificial-intelligence/' },
      { identifier: 'https://simonwillison.net/' },
    ];

    return sources.map(source => source.identifier);
  } catch (error) {
    console.error(error);
  }
} 
  
```

## File: `src/services/scrapeSources.ts`
```typescript

import FirecrawlApp from '@mendable/firecrawl-js';
import dotenv from 'dotenv';
import OpenAI from 'openai';


dotenv.config();

const app = new FirecrawlApp({apiKey: process.env.FIRECRAWL_API_KEY});

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

## File: `src/services/sendPodcast.ts`
```typescript

import dotenv from 'dotenv';
import { Resend } from 'resend';

dotenv.config();

const resend = new Resend(process.env.RESEND_API_KEY);


export async function sendPodcast(podcast_url: string, reciever_email: string) {
  try {

    await resend.emails.send({
      from: 'Eric <eric@tryfirecrawl.com>',
      to: reciever_email,
      subject: 'AGI News Podcast with Eric',
      html: `Your podcast is ready to listen to: ` + podcast_url
    });

    return "Success sending newsletter to " + reciever_email + " on " + new Date().toISOString();
  } catch (error) {
    console.log("error sending newsletter");
  }
}
```

