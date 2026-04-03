---
id: github.com-codebuffai-codebuff-community-68be367c-
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:40.801819
---

# KNOWLEDGE EXTRACT: github.com_CodebuffAI_codebuff-community_68be367c
> **Extracted on:** 2026-04-01 09:11:51
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007519999/github.com_CodebuffAI_codebuff-community_68be367c

---

## File: `.gitignore`
```
# ... existing content ...
**/comm/
.DS_Store
```

## File: `.gitmodules`
```
[submodule "showcase/later"]
	path = showcase/later
	url = https://github.com/narthur/later
[submodule "showcase/game-of-life"]
	path = showcase/game-of-life
	url = https://github.com/narthur/game-of-life
[submodule "showcase/bayes"]
	path = showcase/bayes
	url = https://github.com/narthur/bayes
[submodule "showcase/maze-gen"]
	path = showcase/maze-gen
	url = https://github.com/narthur/maze-gen
[submodule "showcase/codebuff-tricks"]
	path = showcase/codebuff-tricks
	url = https://github.com/narthur/codebuff-tricks
[submodule "showcase/calendar-on-air"]
	path = showcase/calendar-on-air
	url = https://gist.github.com/dhunten/7f88654f3972bfe0fc6d70a1b5fa024a
[submodule "showcase/vending-machine"]
	path = showcase/vending-machine
	url = https://github.com/ShAIWhisperer/vending-machine.git
[submodule "showcase/tdd-web-automation"]
	path = showcase/tdd-web-automation
	url = https://github.com/ShAIWhisperer/tdd-web-automation.git
[submodule "showcase/timer"]
	path = showcase/timer
	url = https://github.com/charleslien/timer.git
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2025 Codebuff

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## File: `README.md`
```markdown
# Codebuff Community

Welcome to the [Codebuff](https://codebuff.com) community repository! This is where you'll find starter templates and showcase projects created by our community.

## Getting Started

First, install Codebuff globally:

```bash
npm install -g codebuff
```

## Starting a Project

Use codebuff to create a new project from a template. Templates are the names of subdirectories in `/starter-templates` or `/showcase`:
```bash
codebuff --create nextjs my-project
```

OR

You can also start codebuff in an existing project directory:
```bash
cd my-project
codebuff
```

## Repository Structure

### `/starter-templates`

A collection of pre-configured project templates for various tech stacks. These templates provide a solid foundation for building new projects with best practices and common configurations already set up.

### `/showcase`

A curated collection of projects built by the community using Codebuff. Get inspired by what others have created!

## Contributing

We'd love to see what you build with Codebuff! You can contribute in two ways:

1. **Add a Starter Template**: Have a well-structured project setup that others might find useful? Share it as a starter template!

2. **Share Your Project**: Built something cool with Codebuff? Open a PR with a submodule linking to your public repo (if you don't know what that means, ask Codebuff to do it for you). Help us inspire others!

To contribute:
1. Fork this repository
2. Add your project to either `/starter-templates` or `/showcase`. For showcase projects, you can either:
   - Copy your project files directly into the showcase directory
   - Add your GitHub repository as a git submodule in the showcase directory
3. Submit a pull request

Please ensure your contribution includes clear documentation and follows our existing structure.

## License

This repository is MIT licensed. See [LICENSE](./LICENSE) for details.
```

## File: `knowledge/convex.knowledge.md`
```markdown
---
description: Guidelines and best practices for building Convex projects, including database schema design, queries, mutations, and real-world examples
globs: **/*.{ts,tsx,js,jsx}
---

Downloaded from: https://docs.convex.dev/ai

<convex_guidelines>
  <function_guidelines>
    <new_function_syntax>
      - ALWAYS use the new function syntax for Convex functions. For example:
      ```typescript
      import { query } from "./_generated/server";
      import { v } from "convex/values";
      export const f = query({
          args: {},
          returns: v.null(),
          handler: async (ctx, args) => {
          // Function body
          },
      });
      ```
    </new_function_syntax>
    <http_endpoint_syntax>
      - HTTP endpoints are defined in `convex/http.ts` and require an `httpAction` decorator. For example:
      ```typescript
      import { httpRouter } from "convex/server";
      import { httpAction } from "./_generated/server";
      const http = httpRouter();
      http.route({
          path: "/echo",
          method: "POST",
          handler: httpAction(async (ctx, req) => {
          const body = await req.bytes();
          return new Response(body, { status: 200 });
          }),
      });
      ```
      - HTTP endpoints are always registered at the exact path you specify in the `path` field. For example, if you specify `/api/someRoute`, the endpoint will be registered at `/api/someRoute`.
    </http_endpoint_syntax>
    <function_registration>
      - Use `internalQuery`, `internalMutation`, and `internalAction` to register internal functions. These functions are private and aren't part of an app's API. They can only be called by other Convex functions.
      - Use `query`, `mutation`, and `action` to register public functions. These functions are part of the public API and are exposed to the public Internet. Do NOT use `query`, `mutation`, or `action` to register sensitive internal functions that should be kept private.
      - You CANNOT register a function through the `api` or `internal` objects.
      - ALWAYS include argument and return validators for all Convex functions. If a function doesn't return anything, include `returns: v.null()` as its output validator.
      - If the JavaScript implementation of a Convex function doesn't have a return value, it implicitly returns `null`.
    </function_registration>
    <function_calling>
      - Use `ctx.runQuery` to call a query from a query, mutation, or action.
      - Use `ctx.runMutation` to call a mutation from a mutation or action.
      - Use `ctx.runAction` to call an action from an action.
      - ONLY call an action from another action if you need to cross runtimes (e.g. from V8 to Node). Otherwise, pull out the shared code into a helper async function and call that directly instead.
      - Try to use as few calls from actions to queries and mutations as possible. Queries and mutations are transactions, so splitting logic up into multiple calls introduces the risk of race conditions.
      - All of these calls take in a `FunctionReference`. Do NOT try to pass the callee function directly into one of these calls.
      - When using `ctx.runQuery`, `ctx.runMutation`, or `ctx.runAction` to call a function in the same file, specify a type annotation on the return value to work around TypeScript circularity limitations. For example,
                            ```
                            export const f = query({
                              args: { name: v.string() },
                              returns: v.string(),
                              handler: async (ctx, args) => {
                                return "Hello " + args.name;
                              },
                            });

                            export const g = query({
                              args: {},
                              returns: v.null(),
                              handler: async (ctx, args) => {
                                const result: string = await ctx.runQuery(api.example.f, { name: "Bob" });
                                return null;
                              },
                            });
                            ```
    </function_calling>
    <function_references>
      - Function references are pointers to registered Convex functions.
      - Use the `api` object defined by the framework in `convex/_generated/api.ts` to call public functions registered with `query`, `mutation`, or `action`.
      - Use the `internal` object defined by the framework in `convex/_generated/api.ts` to call internal (or private) functions registered with `internalQuery`, `internalMutation`, or `internalAction`.
      - Convex uses file-based routing, so a public function defined in `convex/example.ts` named `f` has a function reference of `api.example.f`.
      - A private function defined in `convex/example.ts` named `g` has a function reference of `internal.example.g`.
      - Functions can also registered within directories nested within the `convex/` folder. For example, a public function `h` defined in `convex/messages/access.ts` has a function reference of `api.messages.access.h`.
    </function_references>
    <api_design>
      - Convex uses file-based routing, so thoughtfully organize files with public query, mutation, or action functions within the `convex/` directory.
      - Use `query`, `mutation`, and `action` to define public functions.
      - Use `internalQuery`, `internalMutation`, and `internalAction` to define private, internal functions.
    </api_design>
  </function_guidelines>
  <validator_guidelines>
    - `v.bigint()` is deprecated for representing signed 64-bit integers. Use `v.int64()` instead.
    - Use `v.record()` for defining a record type. `v.map()` and `v.set()` are not supported.
  </validator_guidelines>
  <schema_guidelines>
    - Always define your schema in `convex/schema.ts`.
    - Always import the schema definition functions from `convex/server`:
    - System fields are automatically added to all documents and are prefixed with an underscore.
  </schema_guidelines>
  <typescript_guidelines>
    - You can use the helper typescript type `Id` imported from './_generated/dataModel' to get the type of the id for a given table. For example if there is a table called 'users' you can use `Id<'users'>` to get the type of the id for that table.
    - If you need to define a `Record` make sure that you correctly provide the type of the key and value in the type. For example a validator `v.record(v.id('users'), v.string())` would have the type `Record<Id<'users'>, string>`.
    - Be strict with types, particularly around id's of documents. For example, if a function takes in an id for a document in the 'users' table, take in `Id<'users'>` rather than `string`.
  </typescript_guidelines>
  <full_text_search_guidelines>
    - A query for "10 messages in channel '#general' that best match the query 'hello hi' in their body" would look like:

const messages = await ctx.db
  .query("messages")
  .withSearchIndex("search_body", (q) =>
    q.search("body", "hello hi").eq("channel", "#general"),
  )
  .take(10);
  </full_text_search_guidelines>
  <query_guidelines>
    - Do NOT use `filter` in queries. Instead, define an index in the schema and use `withIndex` instead.
    - Convex queries do NOT support `.delete()`. Instead, `.collect()` the results, iterate over them, and call `ctx.db.delete(row._id)` on each result.
    - Use `.unique()` to get a single document from a query. This method will throw an error if there are multiple documents that match the query.
    <ordering>
      - By default Convex always returns documents in ascending `_creationTime` order.
      - You can use `.order('asc')` or `.order('desc')` to pick whether a query is in ascending or descending order. If the order isn't specified, it defaults to ascending.
      - Document queries that use indexes will be ordered based on the columns in the index and can avoid slow table scans.
    </ordering>
  </query_guidelines>
  <mutation_guidelines>
    - Use `ctx.db.replace` to fully replace an existing document. This method will throw an error if the document does not exist.
    - Use `ctx.db.patch` to shallow merge updates into an existing document. This method will throw an error if the document does not exist.
  </mutation_guidelines>
  <scheduling_guidelines>
    <cron_guidelines>
      - Only use the `crons.interval` or `crons.cron` methods to schedule cron jobs. Do NOT use the `crons.hourly`, `crons.daily`, or `crons.weekly` helpers.
      - Both cron methods take in a FunctionReference. Do NOT try to pass the function directly into one of these methods.
      - Define crons by declaring the top-level `crons` object, calling some methods on it, and then exporting it as default. For example,
                            ```ts
                            import { cronJobs } from "convex/server";
                            import { internal } from "./_generated/api";

                            const crons = cronJobs();

                            // Run `internal.users.deleteInactive` every two hours.
                            crons.interval("delete inactive users", { hours: 2 }, internal.users.deleteInactive, {});

                            export default crons;
                            ```
      - You can register Convex functions within `crons.ts` just like any other file.
      - If a cron calls an internal function, always import the `internal` object from '_generated/api`, even if the internal function is registered in the same file.
    </cron_guidelines>
  </scheduling_guidelines>
  <file_storage_guidelines>
    - Convex includes file storage for large files like images, videos, and PDFs.
    - The `ctx.storage.getUrl()` method returns a signed URL for a given file. It returns `null` if the file doesn't exist.
    - Do NOT use the deprecated `ctx.storage.getMetadata` call for loading a file's metadata.

                    Instead, query the `_storage` system table. For example, you can use `ctx.db.system.get` to get an `Id<"_storage">`.
                    ```
                    import { query } from "./_generated/server";
                    import { Id } from "./_generated/dataModel";

                    type FileMetadata = {
                        _id: Id<"_storage">;
                        _creationTime: number;
                        contentType?: string;
                        sha256: string;
                        size: number;
                    }

                    export const exampleQuery = query({
                        args: { fileId: v.id("_storage") },
                        returns: v.null();
                        handler: async (ctx, args) => {
                            const metadata: FileMetadata | null = await ctx.db.system.get(args.fileId);
                            console.log(metadata);
                            return null;
                        },
                    });
                    ```
  </file_storage_guidelines>
</convex_guidelines>


<examples>
<example name="chat-app">
  <task>
    Create a real-time chat application backend with AI responses. The app should:
- Allow creating users with names
- Support multiple chat channels
- Enable users to send messages to channels
- Automatically generate AI responses to user messages
- Show recent message history

The backend should provide APIs for:
1. User management (creation)
2. Channel management (creation)
3. Message operations (sending, listing)
4. AI response generation using OpenAI's GPT-4

Messages should be stored with their channel, author, and content. The system should maintain message order
and limit history display to the 10 most recent messages per channel.

  </task>
  <response>
    <analysis>
      1. Task Requirements Summary:
- Build a real-time chat backend with AI integration
- Support user creation
- Enable channel-based conversations
- Store and retrieve messages with proper ordering
- Generate AI responses automatically

2. Main Components Needed:
- Database tables: users, channels, messages
- Public APIs for user/channel management
- Message handling functions
- Internal AI response generation system
- Context loading for AI responses

3. Public API and Internal Functions Design:
Public Mutations:
- createUser:
  - file path: convex/index.ts
  - arguments: {name: v.string()}
  - returns: v.object({userId: v.id("users")})
  - purpose: Create a new user with a given name
- createChannel:
  - file path: convex/index.ts
  - arguments: {name: v.string()}
  - returns: v.object({channelId: v.id("channels")})
  - purpose: Create a new channel with a given name
- sendMessage:
  - file path: convex/index.ts
  - arguments: {channelId: v.id("channels"), authorId: v.id("users"), content: v.string()}
  - returns: v.null()
  - purpose: Send a message to a channel and schedule a response from the AI

Public Queries:
- listMessages:
  - file path: convex/index.ts
  - arguments: {channelId: v.id("channels")}
  - returns: v.array(v.object({
    _id: v.id("messages"),
    _creationTime: v.number(),
    channelId: v.id("channels"),
    authorId: v.optional(v.id("users")),
    content: v.string(),
    }))
  - purpose: List the 10 most recent messages from a channel in descending creation order

Internal Functions:
- generateResponse:
  - file path: convex/index.ts
  - arguments: {channelId: v.id("channels")}
  - returns: v.null()
  - purpose: Generate a response from the AI for a given channel
- loadContext:
  - file path: convex/index.ts
  - arguments: {channelId: v.id("channels")}
  - returns: v.array(v.object({
    _id: v.id("messages"),
    _creationTime: v.number(),
    channelId: v.id("channels"),
    authorId: v.optional(v.id("users")),
    content: v.string(),
  }))
- writeAgentResponse:
  - file path: convex/index.ts
  - arguments: {channelId: v.id("channels"), content: v.string()}
  - returns: v.null()
  - purpose: Write an AI response to a given channel

4. Schema Design:
- users
  - validator: { name: v.string() }
  - indexes: <none>
- channels
  - validator: { name: v.string() }
  - indexes: <none>
- messages
  - validator: { channelId: v.id("channels"), authorId: v.optional(v.id("users")), content: v.string() }
  - indexes
    - by_channel: ["channelId"]

5. Background Processing:
- AI response generation runs asynchronously after each user message
- Uses OpenAI's GPT-4 to generate contextual responses
- Maintains conversation context using recent message history

    </analysis>
    <file path="package.json">
      {
  "name": "chat-app",
  "description": "This example shows how to build a chat app without authentication.",
  "version": "1.0.0",
  "dependencies": {
    "convex": "^1.17.4",
    "openai": "^4.79.0"
  }
}
    </file>
    <file path="convex/index.ts">
      import {
  query,
  mutation,
  internalQuery,
  internalMutation,
  internalAction,
} from "./_generated/server";
import { v } from "convex/values";
import OpenAI from "openai";
import { internal } from "./_generated/api";

/**
 * Create a user with a given name.
 */
export const createUser = mutation({
  args: {
    name: v.string(),
  },
  returns: v.id("users"),
  handler: async (ctx, args) => {
    return await ctx.db.insert("users", { name: args.name });
  },
});

/**
 * Create a channel with a given name.
 */
export const createChannel = mutation({
  args: {
    name: v.string(),
  },
  returns: v.id("channels"),
  handler: async (ctx, args) => {
    return await ctx.db.insert("channels", { name: args.name });
  },
});

/**
 * List the 10 most recent messages from a channel in descending creation order.
 */
export const listMessages = query({
  args: {
    channelId: v.id("channels"),
  },
  returns: v.array(
    v.object({
      _id: v.id("messages"),
      _creationTime: v.number(),
      channelId: v.id("channels"),
      authorId: v.optional(v.id("users")),
      content: v.string(),
    }),
  ),
  handler: async (ctx, args) => {
    const messages = await ctx.db
      .query("messages")
      .withIndex("by_channel", (q) => q.eq("channelId", args.channelId))
      .order("desc")
      .take(10);
    return messages;
  },
});

/**
 * Send a message to a channel and schedule a response from the AI.
 */
export const sendMessage = mutation({
  args: {
    channelId: v.id("channels"),
    authorId: v.id("users"),
    content: v.string(),
  },
  returns: v.null(),
  handler: async (ctx, args) => {
    const channel = await ctx.db.get(args.channelId);
    if (!channel) {
      throw new Error("Channel not found");
    }
    const user = await ctx.db.get(args.authorId);
    if (!user) {
      throw new Error("User not found");
    }
    await ctx.db.insert("messages", {
      channelId: args.channelId,
      authorId: args.authorId,
      content: args.content,
    });
    await ctx.scheduler.runAfter(0, internal.index.generateResponse, {
      channelId: args.channelId,
    });
    return null;
  },
});

const openai = new OpenAI();

export const generateResponse = internalAction({
  args: {
    channelId: v.id("channels"),
  },
  returns: v.null(),
  handler: async (ctx, args) => {
    const context = await ctx.runQuery(internal.index.loadContext, {
      channelId: args.channelId,
    });
    const response = await openai.chat.completions.create({
      model: "gpt-4o",
      messages: context,
    });
    const content = response.choices[0].message.content;
    if (!content) {
      throw new Error("No content in response");
    }
    await ctx.runMutation(internal.index.writeAgentResponse, {
      channelId: args.channelId,
      content,
    });
    return null;
  },
});

export const loadContext = internalQuery({
  args: {
    channelId: v.id("channels"),
  },
  returns: v.array(
    v.object({
      role: v.union(v.literal("user"), v.literal("assistant")),
      content: v.string(),
    }),
  ),
  handler: async (ctx, args) => {
    const channel = await ctx.db.get(args.channelId);
    if (!channel) {
      throw new Error("Channel not found");
    }
    const messages = await ctx.db
      .query("messages")
      .withIndex("by_channel", (q) => q.eq("channelId", args.channelId))
      .order("desc")
      .take(10);

    const result = [];
    for (const message of messages) {
      if (message.authorId) {
        const user = await ctx.db.get(message.authorId);
        if (!user) {
          throw new Error("User not found");
        }
        result.push({
          role: "user" as const,
          content: `${user.name}: ${message.content}`,
        });
      } else {
        result.push({ role: "assistant" as const, content: message.content });
      }
    }
    return result;
  },
});

export const writeAgentResponse = internalMutation({
  args: {
    channelId: v.id("channels"),
    content: v.string(),
  },
  returns: v.null(),
  handler: async (ctx, args) => {
    await ctx.db.insert("messages", {
      channelId: args.channelId,
      content: args.content,
    });
    return null;
  },
});
    </file>
    <file path="convex/schema.ts">
      import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  channels: defineTable({
    name: v.string(),
  }),

  users: defineTable({
    name: v.string(),
  }),

  messages: defineTable({
    channelId: v.id("channels"),
    authorId: v.optional(v.id("users")),
    content: v.string(),
  }).index("by_channel", ["channelId"]),
});
    </file>
  </response>
</example>
</examples>
```

## File: `knowledge/react-optimization.knowledge.md`
```markdown
# React Code Optimization Guidelines

When analyzing and modifying React code, examine the following patterns and implement the corresponding optimizations:

<Unnecessary Rerenders>

1. **Component-Level Rerendering:** When analyzing code, identify if components are rerendering unnecessarily. Look for and fix the following patterns:

- **State Changes High in the Tree:** Search for state changes high in the component tree that cause children to rerender unnecessarily. For example, if you see this pattern:

```jsx
function ParentComponent() {
  const [count, setCount] = useState(0)
  return (
    <div>
      <ExpensiveChild unrelatedProp="something" />
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  )
}
```

Modify the code to isolate state updates through component splitting or lifting state.

- **Lack of Memoization:** When child components rerender even though their props haven't changed, implement `React.memo`. For example, transform this:

```jsx
const ChildComponent = ({ style }) => {
  console.log("ChildComponent rendering")
  return <div style={style}>Child</div>
}
```

Into this:

```jsx
const ChildComponent = React.memo(({ style }) => {
  console.log("ChildComponent rendering")
  return <div style={style}>Child</div>
})
```

2. **Prop Instability:**

- **Inline Objects/Arrays:** Look for and fix object or array literals passed as props inline. For example, transform this problematic pattern:

```jsx
function ParentComponent() {
  const [count, setCount] = useState(0)
  return (
    <div>
      <ChildComponent style={{ color: "blue" }} />
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  )
}
```

Into either this:

```jsx
const childStyle = { color: "blue" }

function ParentComponent() {
  const [count, setCount] = useState(0)
  return (
    <div>
      <ChildComponent style={childStyle} />
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  )
}
```

Or using `useMemo`:

```jsx
function ParentComponent() {
  const [count, setCount] = useState(0)
  const childStyle = useMemo(() => ({ color: "blue" }), [])
  return (
    <div>
      <ChildComponent style={childStyle} />
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  )
}
```

- **Inline Functions:** Search for and fix functions defined inline within props. Transform this:

```jsx
<button onClick={() => handleClick()}>Click Me</button>
```

Into this:

```jsx
const handleButtonClick = useCallback(() => handleClick(), [])
// ...
<button onClick={handleButtonClick}>Click Me</button>
```

When dependencies are needed:

```jsx
const handleButtonClick = useCallback(() => handleClick(id), [id])
```

- **Inline Function, Stable Value:** When reviewing memoized functions, verify that the dependency array is correctly managed.

3. **Context Usage:** When examining React Context usage, check if context changes cause widespread rerendering. If found, implement more granular contexts or alternative state management. For example, transform this problematic pattern:

```jsx
const BigContext = React.createContext()

function Provider({ children }) {
  const [frequently, setFrequently] = useState(0)
  const [rarely, setRarely] = useState(0)
  
  const value = { frequently, rarely, setFrequently, setRarely }
  
  return (
    <BigContext.Provider value={value}>
      {children}
    </BigContext.Provider>
  )
}
```

Into this optimized version:

```jsx
const FrequentContext = React.createContext()
const RareContext = React.createContext()

function Provider({ children }) {
  const [frequently, setFrequently] = useState(0)
  const [rarely, setRarely] = useState(0)
  
  const frequentValue = useMemo(() => ({ frequently, setFrequently }), [frequently])
  const rareValue = useMemo(() => ({ rarely, setRarely }), [rarely])
  
  return (
    <FrequentContext.Provider value={frequentValue}>
      <RareContext.Provider value={rareValue}>
        {children}
      </RareContext.Provider>
    </FrequentContext.Provider>
  )
}
```

</Unnecessary Rerenders>

<Virtual DOM and Reconciliation>

When optimizing code, remember that React's rerendering process (running the component's function and performing the virtual DOM diff) is separate from actual DOM updates. While a rerender doesn't always mean a DOM update, unnecessary rerenders still consume computational resources and should be eliminated through the patterns above.

</Virtual DOM and Reconciliation>

When analyzing and modifying code, structure the changes as follows:

- **Problem Identification:** Identify the specific performance issue in the code.
- **Code Modification:** Apply the appropriate optimization pattern from above.
- **Verification:** Explain how the modification prevents unnecessary rerenders.
- **Testing:** Verify the optimization through React DevTools and performance monitoring.

Continue this process for each component or section of code being optimized.
```

## File: `showcase/README.md`
```markdown
# showcase

Community showcase of projects built by Codebuff

## Projects

- [Later](https://github.com/narthur/later) - A task management app inspired by Do It (Tomorrow), built with Svelte
- [Game of Life](https://github.com/narthur/game-of-life) - Conway's Game of Life implementation with TypeScript
- [Bayes](https://github.com/narthur/bayes) - A web application for applying Bayesian reasoning to everyday life
- [Maze Generator](https://github.com/narthur/maze-gen) - A maze generation visualization built with TypeScript
- [Codebuff Tricks](https://github.com/narthur/codebuff-tricks) - A community-built wizard to help you set up new projects with Codebuff
- Minecraft simple - A basic version of Minecraft running in the browser!
- Minecraft complex - A more complex version of Minecraft running in the browser!
- Fishies - An aquarium with various fishies
- Code Analysis - A project by [Lachlan Gray](https://github.com/LachlanGray) to show interesting stats on any Github repo
- [Calendar On Air](https://gist.github.com/dhunten/7f88654f3972bfe0fc6d70a1b5fa024a/b2e2b25e788ca7a50c42f3a5a991f4b860e37306) - An app built with CircuitPython that pulls time and weather data + a user's calendar events from the internet and displays it on an LCD screen
- [TDD Web Automation](https://github.com/ShAIWhisperer/tdd-web-automation) - A React-based web application demonstrating form automation testing using Playwright, uisng Test Driven Development (TDD)
- [Vending Machine](https://github.com/ShAIWhisperer/vending-machine) - A fun little vending machine web and cli
- [Timer App](https://github.com/charleslien/timer.git) - A timer app by [Charles Lien](https://github.com/charleslien) to track various tasks over the years.

## Cloning

This repository contains submodules. To clone including all showcase projects, use:

```bash
git clone --recursive https://github.com/CodebuffAI/codebuff-community.git
```

Or if you've already cloned the repository:

```bash
git submodule update --init --recursive
```
```

## File: `showcase/code-analysis/.gitignore`
```
__pycache__/
*.py[cod]
*$py.class
.env
.venv/
venv/
.DS_Store
*.log
dist/
build/
*.egg-info/
```

## File: `showcase/code-analysis/README.md`
```markdown
# GitHub Repository Analyzer

A Chrome extension that analyzes GitHub repositories for development patterns and metrics!

<p align="center">
  <img src="images/img1.png" width="45%" />
  <img src="images/img2.png" width="45%" />
</p>


## Features
- Commit frequency analysis
- Contributor activity tracking
- Commit patterns by weekday
- Average commit size metrics

## Prerequisites
- Python 3.8 or higher
- Google Chrome browser
- Git

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd code-analysis
```

### 2. Set Up Python Environment
```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

# Install dependencies
pip install -e .

# Install development dependencies (optional)
pip install -e ".[dev]"
```

### 3. Start the Backend Server
```bash
# Start the FastAPI server
./start_server.sh
```
The server will run at http://localhost:8000

### 4. Install Chrome Extension
1. Open Chrome and navigate to `chrome://extensions/`
2. Enable "Developer mode" in the top right
3. Click "Load unpacked"
4. Select the `extension` directory from this project

### 5. Using the Extension
1. Navigate to any GitHub repository
2. Click the extension icon in Chrome's toolbar
3. Click "Analyze Repository" to see metrics

## Development

### Running Type Checks
```bash
mypy cli app
```

### Format Code
```bash
black cli app
```

### API Documentation
When the server is running, visit:
- http://localhost:8000/docs for interactive API documentation
- http://localhost:8000/redoc for alternative documentation view

## Troubleshooting

### Common Issues
1. If the extension shows "No repository detected":
   - Refresh the GitHub page
   - Make sure you're on a repository page

2. If analysis fails:
   - Check that the backend server is running
   - Look for errors in the server logs

3. If the extension doesn't load:
   - Check Chrome's extension page for errors
   - Try reloading the extension

### Server Logs
The FastAPI server logs all operations. Check the terminal where you ran `start_server.sh` for detailed error messages.

## Architecture
- `cli/`: Command-line interface for git analysis
- `app/`: FastAPI web service
- `extension/`: Chrome extension files
```

## File: `showcase/code-analysis/knowledge.md`
```markdown
# Python CLI Template Knowledge

## Project Overview
A minimal Python CLI application template with modern Python features and type hints.

## Key Features
- Uses virtual environments for isolation
- Type hints and mypy for static type checking
- Modern Python packaging with pyproject.toml
- Black for code formatting

## Verifying changes
After every change, run:
```bash
mypy cli app && black --check cli app
```
This will check for type errors and formatting issues.

## Project Structure
- `cli/`: Command-line interface for git analysis
- `app/`: FastAPI web service for git analysis
- `extension/`: Chrome extension for GitHub integration

## Chrome Extension
The extension activates on GitHub repository pages and provides:
- Analysis popup accessible via toolbar icon
- Direct integration with local FastAPI server
- JSON visualization of repository metrics

### Architecture Constraints
Git analysis requires a backend service because:
- GitPython needs filesystem access
- Git operations require system-level access
- Cannot run Python directly in extension

### Chrome Extension Architecture
- Use background script for persistent state between content script and popup
- Content script injects into GitHub pages to extract repo info
- Popup must handle case where content script isn't ready
- Always use DOMContentLoaded in popup script

### Alternative Approaches Investigated
Client-side options have limitations:
- Pyodide (WASM Python): No filesystem/git access
- WebContainer API: Limited browser support, sandboxed
  - Requires 'wasm-unsafe-eval' in CSP
  - Must load from CDN or package
  - Resets on popup close
- isomorphic-git: Requires fetching full repo data first

## Project Structure
- `cli/`: Command-line interface for git analysis
- `app/`: FastAPI web service for git analysis
- `extension/`: Chrome extension for GitHub integration

## Chrome Extension
The extension activates on GitHub repository pages and provides:
- Analysis popup accessible via toolbar icon
- Direct integration with local FastAPI server
- JSON visualization of repository metrics

### Architecture Constraints
Git analysis requires a backend service because:
- GitPython needs filesystem access
- Git operations require system-level access
- Cannot run Python directly in extension

### Alternative Approaches Investigated
Client-side options have limitations:
- Pyodide (WASM Python): No filesystem/git access
- WebContainer API: Limited browser support, sandboxed
  - Requires 'wasm-unsafe-eval' in CSP
  - Must load from CDN or package
  - Resets on popup close
- isomorphic-git: Requires fetching full repo data first
```

## File: `showcase/code-analysis/pyproject.toml`
```
[project]
name = "cli"
version = "0.1.0"
description = "A Python CLI application for analyzing GitHub repository complexity"
requires-python = ">=3.8"
dependencies = [
    "gitpython>=3.1.42",
    "fastapi>=0.109.2",
    "uvicorn>=0.27.1",
]

[project.optional-dependencies]
dev = [
    "mypy>=1.8.0",
    "black>=24.1.1",
    "pytest>=8.0.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.mypy]
python_version = "3.8"
strict = true
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true

[tool.black]
line-length = 88
target-version = ['py38']
```

## File: `showcase/code-analysis/start_server.sh`
```bash
#!/bin/bash
uvicorn app.main:app --reload --port 8000
```

## File: `showcase/code-analysis/app/__init__.py`
```python
"""FastAPI application for git repository analysis."""
```

## File: `showcase/code-analysis/app/main.py`
```python
import os
import tempfile
import logging
from git import Repo
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, Union
from pydantic import BaseModel
from cli.git_analysis import (
    analyze_commit_frequency,
    analyze_contributor_activity,
    analyze_commit_frequency_by_weekday,
    analyze_commit_frequency_by_hour,
    analyze_average_commit_size,
    analyze_file_change_frequency,
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Git Analysis API")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["chrome-extension://*"],  # Allow requests from any Chrome extension
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Store repo paths temporarily
repo_cache: Dict[str, str] = {}


class CloneRequest(BaseModel):
    url: str


@app.post("/clone")
async def clone_repository(request: CloneRequest) -> Dict[str, str]:
    """Clone a git repository and return a temporary ID to reference it."""
    try:
        # Create a temporary directory
        temp_dir = tempfile.mkdtemp()
        logger.info(f"Created temp directory: {temp_dir}")

        # Clone the repository
        logger.info(f"Cloning repository from {request.url}")
        repo = Repo.clone_from(request.url, temp_dir)

        # Generate a simple ID (you might want to use UUID in production)
        repo_id = str(hash(request.url))

        # Store the mapping
        repo_cache[repo_id] = temp_dir
        logger.info(f"Successfully cloned repository. ID: {repo_id}")

        return {"repo_id": repo_id}
    except Exception as e:
        logger.error(f"Error cloning repository: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/analyze/{analysis_type}")
async def analyze_repo(
    analysis_type: str, repo_id: str
) -> Dict[str, Union[int, float]]:
    """Analyze a git repository using the specified analysis type."""
    try:
        # Get repo path from cache
        repo_path = repo_cache.get(repo_id)
        if not repo_path:
            logger.error(f"Repository not found for ID: {repo_id}")
            raise HTTPException(
                status_code=404, detail="Repository not found. Please clone it first."
            )

        logger.info(f"Analyzing repository at {repo_path}")

        analysis_functions = {
            "commit-frequency": analyze_commit_frequency,
            "contributor-activity": analyze_contributor_activity,
            "commit-frequency-by-weekday": analyze_commit_frequency_by_weekday,
            "commit-frequency-by-hour": analyze_commit_frequency_by_hour,
            "average-commit-size": analyze_average_commit_size,
            "file-change-frequency": analyze_file_change_frequency,
        }

        if analysis_type not in analysis_functions:
            logger.error(f"Invalid analysis type: {analysis_type}")
            raise HTTPException(
                status_code=400,
                detail=f"Invalid analysis type. Must be one of: {', '.join(analysis_functions.keys())}",
            )  # Execute analysis
        logger.info(f"Running {analysis_type} analysis")
        results = analysis_functions[analysis_type](repo_path)
        logger.info(f"Analysis complete: {results}")

        # Cast the dictionary to the expected type
        if not isinstance(results, dict):
            raise HTTPException(
                status_code=500, detail="Analysis returned invalid type"
            )
        return results
    except Exception as e:
        logger.error(f"Error during analysis: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))
```

## File: `showcase/code-analysis/cli/__init__.py`
```python
"""A Python CLI application."""

__version__ = "0.1.0"
```

## File: `showcase/code-analysis/cli/__main__.py`
```python
#!/usr/bin/env python3
from typing import Any, Callable, Dict
import argparse
from cli.git_analysis import (
    analyze_commit_frequency,
    analyze_contributor_activity,
    analyze_commit_frequency_by_weekday,
    analyze_commit_frequency_by_hour,
    analyze_average_commit_size,
    analyze_file_change_frequency,
)

# Dictionary mapping command names to their corresponding functions
COMMANDS: Dict[str, Callable[..., Dict[str, Any]]] = {
    "analyze_commit_frequency": analyze_commit_frequency,
    "analyze_contributor_activity": analyze_contributor_activity,
    "analyze_commit_frequency_by_weekday": analyze_commit_frequency_by_weekday,
    "analyze_commit_frequency_by_hour": analyze_commit_frequency_by_hour,
    "analyze_average_commit_size": analyze_average_commit_size,
    "analyze_file_change_frequency": analyze_file_change_frequency,
}


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze GitHub repository complexity")
    parser.add_argument(
        "command",
        choices=list(COMMANDS.keys()),
        help="The analysis command to run",
    )
    parser.add_argument(
        "repo_path",
        help="Path to the git repository to analyze",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results in JSON format",
    )

    args = parser.parse_args()

    try:
        # Get the function corresponding to the command
        command_func = COMMANDS[args.command]

        # Execute the command and get the results
        results = command_func(args.repo_path)

        # Print results
        if args.json:
            import json

            print(json.dumps(results, indent=2))
        else:
            print(f"\n{args.command} results:")
            for key, value in sorted(results.items()):
                print(f"{key}: {value}")

    except Exception as e:
        print(f"Error analyzing repository: {e}")


if __name__ == "__main__":
    main()
```

## File: `showcase/code-analysis/cli/git_analysis.py`
```python
from typing import Dict
from git import Repo
from datetime import datetime, timezone
from collections import defaultdict


def analyze_commit_frequency(repo_path: str) -> Dict[str, int]:
    """Analyze commit frequency by day for a git repository."""
    repo = Repo(repo_path)
    frequency: Dict[str, int] = defaultdict(int)

    for commit in repo.iter_commits():
        date = datetime.fromtimestamp(commit.committed_date, timezone.utc)
        day = date.strftime("%Y-%m-%d")
        frequency[day] += 1

    return dict(frequency)


def analyze_commit_frequency_by_weekday(repo_path: str) -> Dict[str, int]:
    """
    Analyze commit frequency by weekday (e.g., Monday, Tuesday).
    """
    repo = Repo(repo_path)
    # Initialize all weekdays with zero count
    frequency = {
        "Monday": 0,
        "Tuesday": 0,
        "Wednesday": 0,
        "Thursday": 0,
        "Friday": 0,
        "Saturday": 0,
        "Sunday": 0,
    }

    for commit in repo.iter_commits():
        date = datetime.fromtimestamp(commit.committed_date, timezone.utc)
        weekday = date.strftime("%A")  # e.g., "Monday"
        frequency[weekday] += 1

    return frequency


def analyze_commit_frequency_by_hour(repo_path: str) -> Dict[str, int]:
    """
    Analyze commit frequency by hour of day (0-23).
    """
    repo = Repo(repo_path)
    # Initialize all hours with zero count
    frequency = {f"{hour:02d}": 0 for hour in range(24)}

    for commit in repo.iter_commits():
        date = datetime.fromtimestamp(commit.committed_date, timezone.utc)
        hour = date.strftime("%H")  # e.g., "13" for 1pm
        frequency[hour] += 1

    return frequency


def analyze_average_commit_size(repo_path: str) -> Dict[str, float]:
    """
    Compute the average commit size (approximate lines added or removed per commit).
    """
    repo = Repo(repo_path)
    total_changes = 0
    commit_count = 0

    for commit in repo.iter_commits():
        # If the commit has no parent (e.g., the initial commit), skip
        if not commit.parents:
            continue

        # Compare commit to its first parent
        diffs = commit.diff(commit.parents[0], create_patch=True)
        changes_in_commit = 0
        for diff in diffs:
            if not diff.diff:
                continue
            # diff.diff can be either string or bytes
            # A rough approach is to count the number of lines that start with "+" or "-"
            # ignoring lines that start with "+++" or "---" in the patch header
            if isinstance(diff.diff, bytes):
                patch_lines = diff.diff.decode("utf-8", errors="ignore").split("\n")
            else:
                patch_lines = diff.diff.split("\n")
            for line in patch_lines:
                if line.startswith("+") and not line.startswith("+++"):
                    changes_in_commit += 1
                elif line.startswith("-") and not line.startswith("---"):
                    changes_in_commit += 1

        total_changes += changes_in_commit
        commit_count += 1

    average_changes = total_changes / commit_count if commit_count else 0
    return {"average_commit_size": average_changes}


def analyze_file_change_frequency(repo_path: str) -> Dict[str, int]:
    """
    Analyze how often each file is changed in the repository.
    """
    repo = Repo(repo_path)
    file_frequency: Dict[str, int] = defaultdict(int)

    for commit in repo.iter_commits():
        # Skip the initial commit (no parent to compare against)
        if not commit.parents:
            continue

        parent = commit.parents[0]
        # diff() returns a list of diff objects representing file changes
        diffs = commit.diff(parent)

        for diff in diffs:
            # a_path and b_path might be different if the file was renamed
            file_path = diff.a_path or diff.b_path
            if file_path:  # Only count if we have a valid path
                file_frequency[file_path] += 1

    return dict(file_frequency)


def analyze_contributor_activity(repo_path: str) -> Dict[str, int]:
    """Analyze commit count per contributor in a git repository."""
    repo = Repo(repo_path)
    activity: Dict[str, int] = defaultdict(int)

    for commit in repo.iter_commits():
        author = f"{commit.author.name} <{commit.author.email}>"
        activity[author] += 1

    return dict(activity)
```

## File: `showcase/code-analysis/extension/background.js`
```javascript
// Store repository info from content scripts
let currentRepoInfo = null;

// Listen for messages from content script
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === 'REPO_DETECTED') {
    currentRepoInfo = message.data;
  }
});

// Listen for messages from popup
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === 'GET_REPO_INFO') {
    sendResponse({ data: currentRepoInfo });
  }
  return true; // Keep channel open for async response
});
```

## File: `showcase/code-analysis/extension/content.js`
```javascript
// Check if we're on a repository page
function isRepositoryPage() {
  // GitHub repository URLs follow the pattern: github.com/owner/repo
  const path = window.location.pathname;
  const pathParts = path.split('/').filter(Boolean);
  return pathParts.length >= 2;
}

// Extract repository information
function getRepositoryInfo() {
  if (!isRepositoryPage()) return null;
  
  const [owner, repo] = window.location.pathname
    .split('/')
    .filter(Boolean)
    .slice(0, 2);
  
  return {
    owner,
    repo,
    url: window.location.href
  };
}

// Initialize when the page loads
function init() {
  const repoInfo = getRepositoryInfo();
  if (repoInfo) {
    console.log('GitHub Repository Analyzer activated:', repoInfo);
    // Send repository information to the extension
    chrome.runtime.sendMessage({
      type: 'REPO_DETECTED',
      data: repoInfo
    });
  }
}

// Run initialization
init();

// Listen for navigation changes (for single page app navigation)
let lastPath = window.location.pathname;
new MutationObserver(() => {
  const currentPath = window.location.pathname;
  if (currentPath !== lastPath) {
    lastPath = currentPath;
    init();
  }
}).observe(document.body, { childList: true, subtree: true });

// Listen for messages from the popup
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === 'GET_REPO_INFO') {
    sendResponse({ data: getRepositoryInfo() });
  }
  return true; // Required to use sendResponse asynchronously
});
```

## File: `showcase/code-analysis/extension/manifest.json`
```json
{
  "manifest_version": 3,
  "name": "GitHub Repository Analyzer",
  "version": "1.0",
  "description": "Analyzes GitHub repositories for complexity and development patterns",
  "permissions": [
    "activeTab"
  ],
  "host_permissions": [
    "https://github.com/*",
    "http://localhost:8000/*"
  ],
  "action": {
    "default_popup": "popup.html"
  },
  "background": {
    "service_worker": "background.js"
  },
  "content_scripts": [
    {
      "matches": ["https://github.com/*"],
      "js": ["content.js"]
    }
  ],
  "content_security_policy": {
    "extension_pages": "script-src 'self'; object-src 'self'"
  }
}
```

## File: `showcase/code-analysis/extension/popup.html`
```html
<!DOCTYPE html>
<html>
<head>
  <title>GitHub Repository Analyzer</title>
  <style>
    body {
      width: 400px;
      padding: 10px;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    }
    .container {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .analysis-section {
      margin-top: 10px;
    }
    .analysis-type {
      margin: 5px 0;
    }
    pre {
      background: #f6f8fa;
      padding: 8px;
      border-radius: 4px;
      overflow-x: auto;
      font-size: 12px;
    }
    button {
      padding: 6px 12px;
      background: #2ea44f;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    button:disabled {
      background: #94d3a2;
      cursor: not-allowed;
    }
  </style>
</head>
<body>
  <div class="container">
    <h2>GitHub Repository Analyzer</h2>
    <div id="repo-info">
      <p>Navigate to a GitHub repository to analyze it.</p>
    </div>
    <div id="analysis-controls" style="display: none;">
      <button id="analyze-btn">Analyze Repository</button>
      <div id="analysis-results" class="analysis-section"></div>
    </div>
  </div>
  <script src="popup.js"></script>
</body>
</html>
```

## File: `showcase/code-analysis/extension/popup.js`
```javascript
const API_URL = 'http://localhost:8000';

// Helper to format JSON for display
function formatJSON(obj) {
  return JSON.stringify(obj, null, 2);
}

// Clone repository and get repo ID
async function cloneRepository(repoUrl) {
  try {
    const response = await fetch(`${API_URL}/clone`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ url: repoUrl }),
    });
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error('Error cloning repository:', error);
    throw error;
  }
}

// Fetch analysis results from the API
async function fetchAnalysis(analysisType, repoId) {
  try {
    const response = await fetch(
      `${API_URL}/analyze/${analysisType}?repo_id=${encodeURIComponent(repoId)}`
    );
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error('Error fetching analysis:', error);
    return { error: error.message };
  }
}

// Display analysis results in the popup
function displayResults(results, analysisType) {
  const resultsDiv = document.getElementById('analysis-results');
  const section = document.createElement('div');
  section.className = 'analysis-type';
  section.innerHTML = `
    <h3>${analysisType}</h3>
    <pre>${formatJSON(results)}</pre>
  `;
  resultsDiv.appendChild(section);
}

// Initialize popup
document.addEventListener('DOMContentLoaded', () => {
  // Query for active tab
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    const tab = tabs[0];
    if (!tab.url?.includes('github.com')) {
      document.getElementById('repo-info').innerHTML = `
        <p>Please navigate to a GitHub repository to analyze it.</p>
      `;
      return;
    }

    // Get repository info from background script
    chrome.runtime.sendMessage({ type: 'GET_REPO_INFO' }, (response) => {
      const repoInfo = document.getElementById('repo-info');
      const analysisControls = document.getElementById('analysis-controls');
      
      if (response?.data) {
        const { owner, repo } = response.data;
        const repoUrl = `https://github.com/${owner}/${repo}.git`;
        
        repoInfo.innerHTML = `
          <p><strong>Owner:</strong> ${owner}</p>
          <p><strong>Repository:</strong> ${repo}</p>
        `;
        
        // Show analysis controls
        analysisControls.style.display = 'block';
        
        // Setup analyze button
        const analyzeBtn = document.getElementById('analyze-btn');
        analyzeBtn.addEventListener('click', async () => {
          try {
            analyzeBtn.disabled = true;
            analyzeBtn.textContent = 'Cloning...';
            
            // First clone the repository
            const { repo_id } = await cloneRepository(repoUrl);
            
            analyzeBtn.textContent = 'Analyzing...';
            
            // Clear previous results
            document.getElementById('analysis-results').innerHTML = '';
            
            // Fetch each type of analysis
            const analysisTypes = [
              'commit-frequency',
              'contributor-activity',
              'commit-frequency-by-weekday',
              'average-commit-size'
            ];
            
            for (const type of analysisTypes) {
              const results = await fetchAnalysis(type, repo_id);
              displayResults(results, type);
            }
          } catch (error) {
            document.getElementById('analysis-results').innerHTML = `
              <div class="error">
                Error: ${error.message}
              </div>
            `;
          } finally {
            analyzeBtn.disabled = false;
            analyzeBtn.textContent = 'Analyze Repository';
          }
        });
      } else {
        repoInfo.innerHTML = `
          <p>No repository detected. Please refresh the page if you're on a GitHub repository.</p>
        `;
      }
    });
  });
});
```

## File: `showcase/fishies/.gitignore`
```
# Dependencies
node_modules
.pnp
.pnp.js

# Production build
dist
build

# Testing
coverage

# Environment
.env
.env.local
.env.development.local
.env.test.local
.env.production.local

# Logs
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*

# Editor directories and files
.vscode/*
!.vscode/extensions.json
.idea
.DS_Store
*.suo
*.ntvs*
*.njsproj
*.sln
*.sw?

# TypeScript
*.tsbuildinfo
```

## File: `showcase/fishies/README.md`
```markdown
# Vite + React Template

A minimal React + TypeScript starter template using [Vite](https://vitejs.dev/) for fast development and building.

## Getting Started

```bash
codebuff --create vite my-app

# In another terminal window:
npm run dev
```

## Available Scripts
- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run lint` - Run ESLint
- `npm run preview` - Preview production build locally

## Learn More
- [Vite Documentation](https://vitejs.dev/)
- [React Documentation](https://react.dev/)
```

## File: `showcase/fishies/eslint.config.js`
```javascript
import js from '@eslint/js'
import globals from 'globals'
import reactHooks from 'eslint-plugin-react-hooks'
import reactRefresh from 'eslint-plugin-react-refresh'
import tseslint from 'typescript-eslint'

export default tseslint.config(
  { ignores: ['dist'] },
  {
    extends: [js.configs.recommended, ...tseslint.configs.recommended],
    files: ['**/*.{ts,tsx}'],
    languageOptions: {
      ecmaVersion: 2020,
      globals: globals.browser,
    },
    plugins: {
      'react-hooks': reactHooks,
      'react-refresh': reactRefresh,
    },
    rules: {
      ...reactHooks.configs.recommended.rules,
      'react-refresh/only-export-components': [
        'warn',
        { allowConstantExport: true },
      ],
    },
  },
)
```

## File: `showcase/fishies/index.html`
```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Vite + React + TS</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
```

## File: `showcase/fishies/knowledge.md`
```markdown
# Vite + React Template Knowledge

## Project Overview
A fish tank simulation with swimming fish, predator behavior, and interactive elements.

## Key Features
- Fish swim with natural movement patterns
- Fish speed up to escape when predators are nearby
- Predators chase nearest prey
- Collision detection between creatures
- Death animations for caught fish

## Animation Guidelines
- Use CSS transitions for smooth movement
- Use 3D transforms for depth
- Scale with depth for dramatic effect
- Use rotateY for direction changes
- Remove transitions for immediate reactions

## Combat Mechanics
- Shark must be moving towards fish to attack
- Fish speed increases near predators
- Whale shark protects fish from sharks

## Game Balance
- Base fish speed: 0.5 units
- Shark speed: 3 units
- Whale shark speed: 4 units
- Protection radius: 100px for whale shark

## Interactive Elements
- Click for bubbles
- Shift+click for food
- Ctrl/Cmd+click for sparkles
- Ripple effects under fast predators

## Fish Behavior
- School with nearby fish
- Avoid predators
- Seek food
- Hide near decorations when threatened

## Ecosystem Interactions
- Predator competition
- Safe zones near decorations
- Territorial behaviors
- Water current effects

## Verifying changes
After every change, run:
```bash
npm run lint && npm run typecheck
```
```

## File: `showcase/fishies/package.json`
```json
{
  "name": "vite",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc -b && vite build",
    "lint": "eslint .",
    "preview": "vite preview",
    "typecheck": "tsc -b"
  },
  "dependencies": {
    "react": "^18.3.1",
    "react-dom": "^18.3.1"
  },
  "devDependencies": {
    "@eslint/js": "^9.17.0",
    "@types/react": "^18.3.18",
    "@types/react-dom": "^18.3.5",
    "@vitejs/plugin-react": "^4.3.4",
    "eslint": "^9.17.0",
    "eslint-plugin-react-hooks": "^5.0.0",
    "eslint-plugin-react-refresh": "^0.4.16",
    "globals": "^15.14.0",
    "typescript": "~5.6.2",
    "typescript-eslint": "^8.18.2",
    "vite": "^6.0.5"
  }
}
```

## File: `showcase/fishies/tsconfig.app.json`
```json
{
  "compilerOptions": {
    "tsBuildInfoFile": "./node_modules/.tmp/tsconfig.app.tsbuildinfo",
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,
    "incremental": true,

    /* Bundler mode */
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "isolatedModules": true,
    "moduleDetection": "force",
    "noEmit": true,
    "jsx": "react-jsx",

    /* Linting */
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true,
  },
  "include": ["src"]
}
```

## File: `showcase/fishies/tsconfig.json`
```json
{
  "files": [],
  "references": [
    { "path": "./tsconfig.app.json" },
    { "path": "./tsconfig.node.json" }
  ]
}
```

## File: `showcase/fishies/tsconfig.node.json`
```json
{
  "compilerOptions": {
    "tsBuildInfoFile": "./node_modules/.tmp/tsconfig.node.tsbuildinfo",
    "target": "ES2022",
    "lib": ["ES2023"],
    "module": "ESNext",
    "skipLibCheck": true,
    "incremental": true,

    /* Bundler mode */
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "isolatedModules": true,
    "moduleDetection": "force",
    "noEmit": true,

    /* Linting */
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true,
  },
  "include": ["vite.config.ts"]
}
```

## File: `showcase/fishies/vite.config.ts`
```typescript
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
})
```

## File: `showcase/fishies/src/App.css`
```css
.app {
  width: 100vw;
  height: 100vh;
  overflow: hidden;
  background: linear-gradient(180deg, #0f4c81 0%, #1e90ff 50%, #0d3b66 100%);
  perspective: 2000px;
  transform-style: preserve-3d;
  0% { transform: translate3d(0, 0, 0) scale(1); }
  50% { transform: translate3d(20px, -30px, 100px) scale(1.3) rotate(10deg); }
  100% { transform: translate3d(0, 0, 0) scale(1); }
}

/* The fish-tank container holds all moving parts */
.fish-tank {
  width: 100%;
  height: 100%;
  position: relative;
  animation: tank-depth 20s infinite ease-in-out, tank-current 10s ease-in-out infinite;
  cursor: pointer;
}

/* Caustics overlay for dynamic lighting */
.caustics-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 0;
  background: radial-gradient(
    circle at 50% 50%,
    rgba(255, 255, 255, 0.05),
    transparent 60%
  );
  opacity: 0.7;
  animation: caustics 8s ease-in-out infinite alternate;
}

/* Ambient light overlay */
.ambient-light {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 0;
  background: linear-gradient(45deg, rgba(255,255,255,0.05), transparent);
  animation: ambient-light-move 15s ease-in-out infinite;
}

/* Subtle light-ray overlay for extra depth */
.fish-tank::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: radial-gradient(
    ellipse at center,
    rgba(255, 255, 255, 0.1),
    transparent
  );
  pointer-events: none;
  z-index: -1;
}

@keyframes tank-depth {
  0%, 100% {
    transform: translate3d(0, 0, 0) rotate3d(1, 1, 0, 0deg);
  }
  50% {
    transform: translate3d(50px, 30px, -200px) rotate3d(1, 1, 0, 3deg);
  }
}

@keyframes tank-current {
  0%, 100% { transform: translate3d(0, 0, 0); }
  50% { transform: translate3d(10px, -5px, 0); }
}

@keyframes jellyfish-float {
  0% {
    transform: translate3d(0, 0, 0) rotate(0deg) scale(1);
  }
  50% {
    transform: translate3d(10px, -20px, 100px) rotate(5deg) scale(1.1);
  }
  100% {
    transform: translate3d(0, 0, 0) rotate(0deg) scale(1);
  }
}

@keyframes jellyfish-playful {
  0% {
    transform: translate3d(0, 0, 0) rotate(0deg) scale(1);
  }
  50% {
    transform: translate3d(10px, -20px, 100px) rotate(5deg) scale(1.1);
  }
  100% {
    transform: translate3d(0, 0, 0) rotate(0deg) scale(1);
  }
}

@keyframes bubble-rise {
  0% {
    transform: translate3d(0, 0, 0) scale(1);
    opacity: 1;
  }
  100% {
    transform: translate3d(var(--drift-x, 20px), -100px, 50px) scale(0.5);
    opacity: 0;
  }
}

@keyframes sway {
  0%, 100% {
    transform: rotate(0deg) translate3d(0, 0, 20px);
  }
  50% {
    transform: rotate(5deg) translate3d(0, 0, 40px);
  }
}

@keyframes starfish-rotate {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(15deg);
  }
}

@keyframes crab-walk {
  0% { 
    transform: translate3d(0, 0, 10px) rotate(-2deg); 
  }
  25% { 
    transform: translate3d(5px, 0, 10px) rotate(0deg); 
  }
  75% { 
    transform: translate3d(-5px, 0, 10px) rotate(0deg); 
  }
  100% { 
    transform: translate3d(0, 0, 10px) rotate(-2deg); 
  }
}

@keyframes caustics {
  0% {
    transform: translate3d(0, 0, 0);
    opacity: 0.7;
  }
  50% {
    transform: translate3d(10px, -10px, 0);
    opacity: 0.8;
  }
  100% {
    transform: translate3d(-10px, 10px, 0);
    opacity: 0.7;
  }
}

@keyframes ambient-light-move {
  0% { transform: translate(0, 0); }
  50% { transform: translate(20px, 20px); }
  100% { transform: translate(0, 0); }
}

@keyframes food-pulse {
  0%, 100% { transform: scale(1); opacity: 1; }
  50% { transform: scale(1.2); opacity: 0.8; }
}

@keyframes water-ripple {
  0%   { transform: scale(0); opacity: 0.5; }
  100% { transform: scale(4); opacity: 0; }
}

@keyframes plankton-drift {
  0%   { transform: translate(0, 0); opacity: 0; }
  50%  { opacity: 1; }
  100% { transform: translate(50px, -50px); opacity: 0; }
}

@keyframes turtle-swim {
  0%   { transform: translate3d(0, 0, 0) rotate(0deg); }
  50%  { transform: translate3d(20px, -10px, 50px) rotate(5deg); }
  100% { transform: translate3d(0, 0, 0) rotate(0deg); }
}

@keyframes dolphin-swim {
  0% {
    transform: translate3d(0, 0, 0) rotate(0deg);
  }
  50% {
    transform: translate3d(20px, -10px, 50px) rotate(5deg);
  }
  100% {
    transform: translate3d(0, 0, 0) rotate(0deg);
  }
}

@keyframes sparkle-fade {
  0% {
    transform: scale(0.5);
    opacity: 1;
  }
  100% {
    transform: scale(1.5);
    opacity: 0;
  }
}
```

## File: `showcase/fishies/src/App.tsx`
```tsx
import { FishTank } from './components/FishTank'
import './App.css'

function App() {
  return (
    <div className="app">
      <FishTank />
    </div>
  )
}

export default App
```

## File: `showcase/fishies/src/index.css`
```css
:root {
  font-family: Inter, system-ui, Avenir, Helvetica, Arial, sans-serif;
  line-height: 1.5;
  font-weight: 400;

  color-scheme: light dark;
  color: rgba(255, 255, 255, 0.87);
  background-color: #242424;

  font-synthesis: none;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  margin: 0;
  display: flex;
  min-width: 320px;
  min-height: 100vh;
}

#root {
  width: 100%;
  height: 100vh;
}
```

## File: `showcase/fishies/src/main.tsx`
```tsx
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
```

## File: `showcase/fishies/src/types.ts`
```typescript
export interface Position {
  x: number;
  y: number;
}

export interface FishState extends Position {
  id: number;
  direction: number;
  color: string;
  speedX: number;
  speedY: number;
  isDying?: boolean;
  dyingStartTime?: number;
  isBeingEaten?: boolean;
  isHiding?: boolean;
}
```

## File: `showcase/fishies/src/vite-env.d.ts`
```typescript
/// <reference types="vite/client" />
```

## File: `showcase/fishies/src/components/Bubble.tsx`
```tsx
// src/components/Bubble.tsx
import { CSSProperties } from "react";

interface BubbleProps {
  x: number;
  y: number;
  size?: number;
  duration?: number;
}

export const Bubble: React.FC<BubbleProps> = ({
  x,
  y,
  size = 10,
  duration = 4,
}) => {
  const style: CSSProperties = {
    position: "absolute",
    left: `${x}px`,
    top: `${y}px`,
    width: `${size}px`,
    height: `${size}px`,
    backgroundColor: "rgba(255, 255, 255, 0.7)",
    borderRadius: "50%",
    zIndex: 0,
    animation: `bubble-rise ${duration}s linear infinite`,
  };

  return <div style={style}></div>;
};
```

## File: `showcase/fishies/src/components/Coral.tsx`
```tsx
// src/components/Coral.tsx
import { CSSProperties } from "react";

interface CoralProps {
  x: number;
  y: number;
  size?: number;
}

export const Coral: React.FC<CoralProps> = ({ x, y, size = 40 }) => {
  const style: CSSProperties = {
    position: "absolute",
    left: `${x}px`,
    top: `${y}px`,
    fontSize: `${size}px`,
    zIndex: 0,
  };

  return <div style={style}>🪸</div>;
};
```

## File: `showcase/fishies/src/components/Crab.tsx`
```tsx
import { CSSProperties } from "react";

interface CrabProps {
  x: number;
  y: number;
  size?: number;
}

export const Crab: React.FC<CrabProps> = ({ x, y, size = 40 }) => {
  const style: CSSProperties = {
    position: "absolute",
    left: `${x}px`,
    top: `${y}px`,
    fontSize: `${size}px`,
    zIndex: 0,
    animation: "crab-walk 4s linear infinite",
  };

  return <div style={style}>🦀</div>;
};
```

## File: `showcase/fishies/src/components/Dolphin.tsx`
```tsx
import { CSSProperties } from "react";

interface DolphinProps {
  x: number;
  y: number;
  size?: number;
}

export const Dolphin: React.FC<DolphinProps> = ({ x, y, size = 40 }) => {
  const style: CSSProperties = {
    position: "absolute",
    left: `${x}px`,
    top: `${y}px`,
    fontSize: `${size}px`,
    zIndex: 1,
    transform: `
      translate3d(0, 0, ${Math.sin(Date.now() / 2500) * 150}px)
      rotateY(${Math.random() < 0.5 ? 0 : 180}deg)
    `,
    animation: "dolphin-swim 6s ease-in-out infinite",
  };

  return <div style={style}>🐬</div>;
};
```

## File: `showcase/fishies/src/components/Fish.tsx`
```tsx
// src/components/Fish.tsx
import { CSSProperties } from "react";

interface FishProps {
  x: number;
  y: number;
  direction: number;
  color: string;
  isDying?: boolean;
  dyingStartTime?: number;
  isBeingEaten?: boolean;
  isHiding?: boolean;
}

export const Fish: React.FC<FishProps> = ({
  x,
  y,
  direction,
  color,
  isDying,
  dyingStartTime,
  isBeingEaten,
  isHiding,
}) => {
  const style: CSSProperties = {
    position: "absolute",
    left: `${x}px`,
    top: `${y}px`,
    // Ensure fish (and later, predators) are rendered above decorations
    zIndex: 1,
    transform: `
      translate3d(0, 0, ${Math.sin(Date.now() / 1000) * 200}px)
      rotateY(${direction > 0 ? 0 : 180}deg)
      ${
        isDying
          ? "rotateZ(180deg)"
          : isBeingEaten
          ? "rotateZ(0deg)"
          : "rotateZ(-15deg)"
      }
      scale(${1 + Math.sin(Date.now() / 1000) * 0.1})
    `,
    transition: isDying ? "opacity 1s ease-out" : "none",
    fontSize: "24px",
    color,
    opacity: isDying ? (Date.now() - dyingStartTime! > 500 ? 0 : 1) : isHiding ? 0.6 : 1,
  };

  return (
    <div style={style}>
      {isDying && Date.now() - dyingStartTime! > 500 ? "☠️" : "🐠"}
    </div>
  );
};
```

## File: `showcase/fishies/src/components/FishTank.tsx`
```tsx
import { useEffect, useState, useCallback, useRef } from "react";
import { Fish } from "./Fish";
import { Shark } from "./Shark";
import { WhaleShark } from "./WhaleShark";
import { UnderwaterDecorations } from "./UnderwaterDecorations";
import { Bubble } from "./Bubble";
import { FoodPellet } from "./FoodPellet";
import { RippleEffect } from "./RippleEffect";
import { SeaSparkle } from "./SeaSparkle";

interface Position {
  x: number;
  y: number;
}

export interface FishState extends Position {
  id: number;
  direction: number;
  color: string;
  speedX: number;
  speedY: number;
  isDying?: boolean;
  dyingStartTime?: number;
  isBeingEaten?: boolean;
  isHiding?: boolean;
}

interface PredatorState extends Position {
  direction: number;
  speed: number;
}

interface InteractiveBubble {
  id: number;
  x: number;
  y: number;
  size: number;
  duration: number;
}

interface RippleState {
  id: number;
  x: number;
  y: number;
}

interface FoodPelletState {
  id: number;
  x: number;
  y: number;
  size: number;
  duration: number;
}

interface InteractiveSparkle {
  id: number;
  x: number;
  y: number;
  size: number;
  duration: number;
}

const COLORS = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEEAD"];
const SHARK_SPEED = 3;
const WHALE_SHARK_SPEED = 4;
const BASE_FISH_SPEED = 0.5;
const MAX_FISH_SPEED_MULTIPLIER = 1.5;
const COMPETITION_DISTANCE = 50;
const COMPETITION_REPULSION = 0.1;
const DANGER_DISTANCE = 100;

// Define safe zones near decorations
const SAFE_ZONES: Position[] = [
  { x: 80, y: window.innerHeight - 100 },
  { x: 300, y: window.innerHeight - 120 },
  { x: 600, y: window.innerHeight - 90 },
  { x: 800, y: window.innerHeight - 110 },
];

const findNearestSafeZone = (fish: Position): Position | null => {
  if (SAFE_ZONES.length === 0) return null;
  return SAFE_ZONES.reduce((closest, zone) => {
    const dZone = Math.hypot(zone.x - fish.x, zone.y - fish.y);
    const dClosest = Math.hypot(closest.x - fish.x, closest.y - fish.y);
    return dZone < dClosest ? zone : closest;
  }, SAFE_ZONES[0]);
};

export const FishTank: React.FC = () => {
  const [fishes, setFishes] = useState<FishState[]>(() =>
    Array.from({ length: 12 }, (_, i) => ({
      id: i,
      x: Math.random() * window.innerWidth * 0.8,
      y: Math.random() * window.innerHeight * 0.8,
      direction: Math.random() < 0.5 ? -1 : 1,
      color: COLORS[Math.floor(Math.random() * COLORS.length)],
      speedX:
        (Math.random() * BASE_FISH_SPEED + BASE_FISH_SPEED) *
        (Math.random() < 0.5 ? -1 : 1),
      speedY: (Math.random() - 0.5) * BASE_FISH_SPEED,
    }))
  );

  const [shark, setShark] = useState<PredatorState>(() => ({
    x: window.innerWidth / 2,
    y: window.innerHeight / 2,
    direction: 1,
    speed: SHARK_SPEED,
  }));

  const [whaleShark, setWhaleShark] = useState<PredatorState>(() => ({
    x: window.innerWidth * 0.8,
    y: window.innerHeight * 0.8,
    direction: -1,
    speed: WHALE_SHARK_SPEED,
  }));

  const [interactiveBubbles, setInteractiveBubbles] = useState<InteractiveBubble[]>([]);
  const [foodPellets, setFoodPellets] = useState<FoodPelletState[]>([]);
  const [ripples, setRipples] = useState<RippleState[]>([]);
  const [interactiveSparkles, setInteractiveSparkles] = useState<InteractiveSparkle[]>([]);

  // Refs to throttle ripple effects for predators
  const sharkRippleTimeRef = useRef<number>(0);
  const whaleSharkRippleTimeRef = useRef<number>(0);

  const handleTankClick = (e: React.MouseEvent<HTMLDivElement, MouseEvent>) => {
    const rect = e.currentTarget.getBoundingClientRect();
    
    // If user holds Ctrl (or Command) key, spawn interactive "sea sparkles"
    if (e.ctrlKey || e.metaKey) {
      const sparkleCount = 3 + Math.floor(Math.random() * 3);
      const newSparkles = Array.from({ length: sparkleCount }, () => ({
        id: Date.now() + Math.random(),
        x: e.clientX - rect.left + (Math.random() - 0.5) * 20,
        y: e.clientY - rect.top + (Math.random() - 0.5) * 20,
        size: 12 + Math.random() * 8,
        duration: 1 + Math.random(),
      }));
      setInteractiveSparkles((prev) => [...prev, ...newSparkles]);
      newSparkles.forEach((sparkle) => {
        setTimeout(() => {
          setInteractiveSparkles((prev) =>
            prev.filter((s) => s.id !== sparkle.id)
          );
        }, sparkle.duration * 1000);
      });
      return;
    }

    // Create a ripple effect unless it's a food pellet drop
    if (!e.shiftKey) {
      const ripple = {
        id: Date.now() + Math.random(),
        x: e.clientX - rect.left,
        y: e.clientY - rect.top,
      };
      setRipples((prev) => [...prev, ripple]);
      setTimeout(() => {
        setRipples((prev) => prev.filter((r) => r.id !== ripple.id));
      }, 1000);
    }

    if (e.shiftKey) {
      const pellet = {
        id: Date.now() + Math.random(),
        x: e.clientX - rect.left,
        y: e.clientY - rect.top,
        size: 16,
        duration: 10000,
      };
      setFoodPellets((prev) => [...prev, pellet]);
      setTimeout(() => {
        setFoodPellets((prev) => prev.filter((p) => p.id !== pellet.id));
      }, pellet.duration);
    } else {
      const bubbleCount = 3 + Math.floor(Math.random() * 3);
      const newBubbles = Array.from({ length: bubbleCount }, () => ({
        id: Date.now() + Math.random(),
        x: e.clientX - rect.left + (Math.random() - 0.5) * 20,
        y: e.clientY - rect.top + (Math.random() - 0.5) * 20,
        size: 8 + Math.random() * 12,
        duration: 2 + Math.random() * 2,
      }));

      setInteractiveBubbles((prev) => [...prev, ...newBubbles]);

      newBubbles.forEach((bubble) => {
        setTimeout(() => {
          setInteractiveBubbles((prev) =>
            prev.filter((b) => b.id !== bubble.id)
          );
        }, bubble.duration * 1000);
      });
    }
  };

  const findNearestFish = useCallback(
    (predator: Position, fishes: Position[]): Position | null => {
      if (fishes.length === 0) return null;
      return fishes.reduce((nearest, current) => {
        const distToCurrent = Math.hypot(current.x - predator.x, current.y - predator.y);
        const distToNearest = Math.hypot(nearest.x - predator.x, nearest.y - predator.y);
        return distToCurrent < distToNearest ? current : nearest;
      });
    },
    []
  );

  const moveTowards = (predator: PredatorState, target: Position): PredatorState => {
    const dx = target.x - predator.x;
    const dy = target.y - predator.y;
    const distance = Math.hypot(dx, dy);
    if (distance < 1) return predator;
    return {
      x: predator.x + (dx / distance) * predator.speed,
      y: predator.y + (dy / distance) * predator.speed,
      direction: dx > 0 ? 1 : -1,
      speed: predator.speed,
    };
  };

  const protectFish = useCallback(
    (whaleShark: Position, shark: PredatorState, fishes: FishState[]): PredatorState => {
      const nearestFish = findNearestFish(shark, fishes);
      if (!nearestFish) return shark;
      const sharkToFish = Math.hypot(nearestFish.x - shark.x, nearestFish.y - shark.y);
      const whaleToShark = Math.hypot(whaleShark.x - shark.x, whaleShark.y - shark.y);
      if (sharkToFish < 150 && whaleToShark < 100) {
        const angle = Math.atan2(shark.y - whaleShark.y, shark.x - whaleShark.x);
        return {
          ...shark,
          x: shark.x + Math.cos(angle) * 250,
          y: shark.y + Math.sin(angle) * 250,
          direction: Math.cos(angle) > 0 ? 1 : -1,
          speed: shark.speed,
        };
      }
      return shark;
    },
    [findNearestFish]
  );

  useEffect(() => {
    const interval = setInterval(() => {
      // Global subtle current offsets (very gentle drift)
      const currentX = Math.sin(Date.now() / 2000) * 0.5;
      const currentY = Math.cos(Date.now() / 2000) * 0.5;

      setFishes((prevFishes) =>
        prevFishes.map((fish) => {
          if (fish.isDying) return fish;
          let newSpeedX = fish.speedX;
          let newSpeedY = fish.speedY;

          // Check for nearby predators and seek safety
          // Check for predator proximity
          const distToPredators = {
            shark: Math.hypot(fish.x - shark.x, fish.y - shark.y),
            whaleShark: Math.hypot(fish.x - whaleShark.x, fish.y - whaleShark.y)
          };
          
          if (distToPredators.shark < DANGER_DISTANCE || distToPredators.whaleShark < DANGER_DISTANCE) {
            const safeZone = findNearestSafeZone(fish);
            if (safeZone) {
              const dirX = safeZone.x - fish.x;
              const dirY = safeZone.y - fish.y;
              const norm = Math.hypot(dirX, dirY) || 1;
              newSpeedX = (dirX / norm) * BASE_FISH_SPEED * 2; // Faster when seeking safety
              newSpeedY = (dirY / norm) * BASE_FISH_SPEED * 2;
              fish.isHiding = true;
            }
          } else {
            fish.isHiding = false;
          }

          // Food attraction behavior
          if (foodPellets.length) {
            const nearestPellet = foodPellets.reduce((closest: FoodPelletState | null, pellet) => {
              if (!closest) return pellet;
              return Math.hypot(fish.x - pellet.x, fish.y - pellet.y) <
                Math.hypot(fish.x - closest.x, fish.y - closest.y)
                ? pellet
                : closest;
            }, null);

            if (nearestPellet) {
              const dx = nearestPellet.x - fish.x;
              const dy = nearestPellet.y - fish.y;
              const dist = Math.hypot(dx, dy);
              if (dist > 0) {
                const boostFactor = 1.5;
                newSpeedX = (dx / dist) * (BASE_FISH_SPEED * boostFactor);
                newSpeedY = (dy / dist) * (BASE_FISH_SPEED * boostFactor);
              }
              if (dist < 20) {
                setFoodPellets((prev) =>
                  prev.filter((p) => p.id !== nearestPellet.id)
                );
              }
            }
          }

          // Add a slight random jitter for natural movement
          newSpeedX += (Math.random() - 0.5) * 0.05;
          newSpeedY += (Math.random() - 0.5) * 0.05;

          // Calculate new position with global current offsets added
          let newX = fish.x + newSpeedX + currentX;
          let newY = fish.y + newSpeedY + currentY;
          let newDirection = fish.direction;
          const newXConstrained = Math.max(0, Math.min(newX, window.innerWidth - 40));
          const newYConstrained = Math.max(0, Math.min(newY, window.innerHeight - 40));
          if (newXConstrained !== newX) {
            newDirection *= -1;
          }
          newX = newXConstrained;
          newY = newYConstrained;

          // Schooling behavior: look for neighbors
          const neighbors = prevFishes.filter(
            (other) =>
              other.id !== fish.id &&
              Math.hypot(other.x - fish.x, other.y - fish.y) < 100
          );

          if (neighbors.length > 0) {
            // Alignment: average nearby velocities
            const avgSpeedX = neighbors.reduce((sum, n) => sum + n.speedX, 0) / neighbors.length;
            const avgSpeedY = neighbors.reduce((sum, n) => sum + n.speedY, 0) / neighbors.length;
            
            // Blend current speed with average (small factor)
            const alignmentFactor = 0.1;
            newSpeedX = newSpeedX + (avgSpeedX - newSpeedX) * alignmentFactor;
            newSpeedY = newSpeedY + (avgSpeedY - newSpeedY) * alignmentFactor;

            // Separation: push away from very close neighbors
            neighbors.forEach((n) => {
              const d = Math.hypot(n.x - fish.x, n.y - fish.y);
              if (d < 30 && d > 0) {
                newSpeedX -= ((n.x - fish.x) / d) * 0.05;
                newSpeedY -= ((n.y - fish.y) / d) * 0.05;
              }
            });
          }

          // Retain existing predator avoidance logic
          const distToShark = Math.hypot(shark.x - newX, shark.y - newY);
          let speedMultiplier = 1;
          if (distToShark < 200) {
            const normalizedDist = distToShark / 200;
            const easeOutQuad = 1 - normalizedDist * normalizedDist;
            speedMultiplier = 1 + (MAX_FISH_SPEED_MULTIPLIER - 1) * easeOutQuad;
          }
          newSpeedX =
            (newSpeedX / Math.abs(newSpeedX || 1)) *
            BASE_FISH_SPEED *
            speedMultiplier;
          newSpeedY =
            (newSpeedY / Math.abs(newSpeedY || 1)) *
            BASE_FISH_SPEED *
            0.5 *
            speedMultiplier;

          return {
            ...fish,
            x: newX,
            y: newY,
            direction: newDirection,
            speedX: newSpeedX,
            speedY: newSpeedY,
          };
        })
      );

      setShark((prevShark) => {
        const nearestFish = findNearestFish(prevShark, fishes);
        let newShark = prevShark;
        if (nearestFish) {
          newShark = moveTowards(prevShark, nearestFish);
        }
        newShark = protectFish(whaleShark, newShark, fishes);

        // Add competition repulsion
        const dx = newShark.x - whaleShark.x;
        const dy = newShark.y - whaleShark.y;
        const dist = Math.hypot(dx, dy);
        if (dist < COMPETITION_DISTANCE) {
          newShark = {
            ...newShark,
            x: newShark.x + (dx / dist) * COMPETITION_REPULSION * SHARK_SPEED,
            y: newShark.y + (dy / dist) * COMPETITION_REPULSION * SHARK_SPEED,
          };
        }

        return {
          ...newShark,
          x: Math.max(0, Math.min(newShark.x + currentX, window.innerWidth - 60)),
          y: Math.max(0, Math.min(newShark.y + currentY, window.innerHeight - 60)),
        };
      });

      setWhaleShark((prevWhaleShark) => {
        const nearestFish = findNearestFish(shark, fishes);
        let newWhaleShark = prevWhaleShark;
        if (
          nearestFish &&
          Math.hypot(nearestFish.x - shark.x, nearestFish.y - shark.y) < 150
        ) {
          newWhaleShark = moveTowards(prevWhaleShark, shark);
        } else {
          newWhaleShark = {
            ...prevWhaleShark,
            x: prevWhaleShark.x + Math.cos(Date.now() / 2000) * 2,
            y: prevWhaleShark.y + Math.sin(Date.now() / 1500) * 2,
            direction: Math.cos(Date.now() / 2000) > 0 ? 1 : -1,
          };
        }

        // Add competition repulsion
        const dx = newWhaleShark.x - shark.x;
        const dy = newWhaleShark.y - shark.y;
        const dist = Math.hypot(dx, dy);
        if (dist < COMPETITION_DISTANCE) {
          newWhaleShark = {
            ...newWhaleShark,
            x: newWhaleShark.x + (dx / dist) * COMPETITION_REPULSION * WHALE_SHARK_SPEED,
            y: newWhaleShark.y + (dy / dist) * COMPETITION_REPULSION * WHALE_SHARK_SPEED,
          };
        }

        return {
          ...newWhaleShark,
          x: Math.max(0, Math.min(newWhaleShark.x + currentX, window.innerWidth - 80)),
          y: Math.max(0, Math.min(newWhaleShark.y + currentY, window.innerHeight - 80)),
        };
      });

      setFishes((prevFishes) => {
        const updatedFishes = prevFishes.map((fish) => {
          if (fish.isDying) return fish;
          const dx = fish.x - shark.x;
          const dy = fish.y - shark.y;
          const distance = Math.hypot(dx, dy);
          if (distance < 30) {
            const sharkMovingTowardsFish =
              (dx > 0 && shark.direction > 0) ||
              (dx < 0 && shark.direction < 0);
            if (sharkMovingTowardsFish) {
              return { ...fish, isBeingEaten: true };
            }
          } else if (fish.isBeingEaten) {
            return {
              ...fish,
              isBeingEaten: false,
              isDying: true,
              dyingStartTime: Date.now(),
            };
          }
          return fish;
        });
        return updatedFishes.filter((fish) => {
          if (!fish.isDying) return true;
          const timeSinceDeath = Date.now() - fish.dyingStartTime!;
          return timeSinceDeath < 1000;
        });
      });
    }, 50);

    return () => clearInterval(interval);
  }, [fishes, shark, whaleShark, protectFish, findNearestFish, foodPellets]);

  // Ripple effect for fast-moving predators
  useEffect(() => {
    const now = Date.now();
    if (now - sharkRippleTimeRef.current > 500) {
      setRipples((prev) => [...prev, { id: now + Math.random(), x: shark.x, y: shark.y }]);
      sharkRippleTimeRef.current = now;
    }
  }, [shark.x, shark.y]);

  useEffect(() => {
    const now = Date.now();
    if (now - whaleSharkRippleTimeRef.current > 500) {
      setRipples((prev) => [...prev, { id: now + Math.random(), x: whaleShark.x, y: whaleShark.y }]);
      whaleSharkRippleTimeRef.current = now;
    }
  }, [whaleShark.x, whaleShark.y]);

  return (
    <div className="fish-tank" onClick={handleTankClick}>
      <div className="ambient-light" />
      <div className="caustics-overlay" />
      {ripples.map((r) => (
        <RippleEffect key={`ripple-${r.id}`} x={r.x} y={r.y} />
      ))}
      <UnderwaterDecorations fishes={fishes} />
      {fishes.map((fish) => (
        <Fish
          key={fish.id}
          x={fish.x}
          y={fish.y}
          direction={fish.direction}
          color={fish.color}
          isDying={fish.isDying}
          isBeingEaten={fish.isBeingEaten}
        />
      ))}
      <Shark x={shark.x} y={shark.y} direction={shark.direction} />
      <WhaleShark
        x={whaleShark.x}
        y={whaleShark.y}
        direction={whaleShark.direction}
      />
      {interactiveBubbles.map((b) => (
        <Bubble
          key={`interactive-${b.id}`}
          x={b.x}
          y={b.y}
          size={b.size}
          duration={b.duration}
        />
      ))}
      {foodPellets.map((p) => (
        <FoodPellet
          key={`food-${p.id}`}
          x={p.x}
          y={p.y}
          size={p.size}
        />
      ))}
      {interactiveSparkles.map((s) => (
        <SeaSparkle
          key={`sparkle-${s.id}`}
          x={s.x}
          y={s.y}
          size={s.size}
          duration={s.duration}
        />
      ))}
    </div>
  );
};
```

## File: `showcase/fishies/src/components/FoodPellet.tsx`
```tsx
import { CSSProperties } from "react";

interface FoodPelletProps {
  x: number;
  y: number;
  size?: number;
}

export const FoodPellet: React.FC<FoodPelletProps> = ({
  x,
  y,
  size = 16,
}) => {
  const style: CSSProperties = {
    position: "absolute",
    left: `${x - size / 2}px`,
    top: `${y - size / 2}px`,
    width: `${size}px`,
    height: `${size}px`,
    zIndex: 1,
    fontSize: `${size}px`,
    animation: "food-pulse 2s ease-in-out infinite",
  };

  return <div style={style}>🍤</div>;
};
```

## File: `showcase/fishies/src/components/Jellyfish.tsx`
```tsx
// src/components/Jellyfish.tsx
import { CSSProperties } from "react";

interface JellyfishProps {
  x: number;
  y: number;
  size?: number;
  isPlayful?: boolean;
}

export const Jellyfish: React.FC<JellyfishProps> = ({ x, y, size = 40, isPlayful = false }) => {
  const style: CSSProperties = {
    position: "absolute",
    left: `${x}px`,
    top: `${y}px`,
    fontSize: `${size}px`,
    // Render behind the fish and predators
    zIndex: 0,
    animation: isPlayful
      ? "jellyfish-playful 3s ease-in-out infinite"
      : "jellyfish-float 6s ease-in-out infinite",
  };

  return <div style={style}>🪼</div>;
};
```

## File: `showcase/fishies/src/components/Plankton.tsx`
```tsx
import { CSSProperties } from "react";

interface PlanktonProps {
  x: number;
  y: number;
  size?: number;
  duration?: number;
}

export const Plankton: React.FC<PlanktonProps> = ({
  x,
  y,
  size = 2,
  duration = 6,
}) => {
  const style: CSSProperties = {
    position: "absolute",
    left: `${x}px`,
    top: `${y}px`,
    width: `${size}px`,
    height: `${size}px`,
    borderRadius: "50%",
    backgroundColor: "rgba(255, 255, 255, 0.8)",
    animation: `plankton-drift ${duration}s linear infinite`,
    zIndex: 0,
  };
  return <div style={style} />;
};
```

## File: `showcase/fishies/src/components/RippleEffect.tsx`
```tsx
import { CSSProperties } from "react";

interface RippleEffectProps {
  x: number;
  y: number;
}

export const RippleEffect: React.FC<RippleEffectProps> = ({ x, y }) => {
  const style: CSSProperties = {
    position: "absolute",
    left: `${x}px`,
    top: `${y}px`,
    width: "20px",
    height: "20px",
    borderRadius: "50%",
    backgroundColor: "rgba(255, 255, 255, 0.2)",
    transform: "translate(-50%, -50%)",
    pointerEvents: "none",
    animation: "water-ripple 1s ease-out forwards",
    zIndex: 0,
  };
  return <div style={style} />;
};
```

## File: `showcase/fishies/src/components/SeaSparkle.tsx`
```tsx
import { CSSProperties } from "react";

interface SeaSparkleProps {
  x: number;
  y: number;
  size?: number;
  duration?: number;
}

export const SeaSparkle: React.FC<SeaSparkleProps> = ({
  x,
  y,
  size = 12,
  duration = 1,
}) => {
  const style: CSSProperties = {
    position: "absolute",
    left: `${x}px`,
    top: `${y}px`,
    width: `${size}px`,
    height: `${size}px`,
    fontSize: `${size}px`,
    pointerEvents: "none",
    animation: `sparkle-fade ${duration}s ease-out forwards`,
    zIndex: 2,
  };

  return <div style={style}>✨</div>;
};
```

## File: `showcase/fishies/src/components/SeaTurtle.tsx`
```tsx
import { CSSProperties } from "react";

interface SeaTurtleProps {
  x: number;
  y: number;
  size?: number;
}

export const SeaTurtle: React.FC<SeaTurtleProps> = ({ x, y, size = 50 }) => {
  const style: CSSProperties = {
    position: "absolute",
    left: `${x}px`,
    top: `${y}px`,
    fontSize: `${size}px`,
    zIndex: 0,
    animation: "turtle-swim 12s ease-in-out infinite",
  };

  return <div style={style}>🐢</div>;
};
```

## File: `showcase/fishies/src/components/Seashell.tsx`
```tsx
// src/components/Seashell.tsx
import { CSSProperties } from "react";

interface SeashellProps {
  x: number;
  y: number;
  size?: number;
}

export const Seashell: React.FC<SeashellProps> = ({ x, y, size = 30 }) => {
  const style: CSSProperties = {
    position: "absolute",
    left: `${x}px`,
    top: `${y}px`,
    fontSize: `${size}px`,
    zIndex: 0,
  };

  return <div style={style}>🐚</div>;
};
```

## File: `showcase/fishies/src/components/Seaweed.tsx`
```tsx
// src/components/Seaweed.tsx
import { CSSProperties } from "react";

interface SeaweedProps {
  x: number;
  y: number;
  size?: number;
}

export const Seaweed: React.FC<SeaweedProps> = ({ x, y, size = 50 }) => {
  const style: CSSProperties = {
    position: "absolute",
    left: `${x}px`,
    top: `${y}px`,
    fontSize: `${size}px`,
    zIndex: 0,
    animation: "sway 4s ease-in-out infinite",
  };

  return <div style={style}>🌿</div>;
};
```

## File: `showcase/fishies/src/components/Shark.tsx`
```tsx
// src/components/Shark.tsx
import { CSSProperties } from "react";

interface SharkProps {
  x: number;
  y: number;
  direction: number;
}

export const Shark: React.FC<SharkProps> = ({ x, y, direction }) => {
  const style: CSSProperties = {
    position: "absolute",
    left: `${x}px`,
    top: `${y}px`,
    zIndex: 1,
    transform: `
      translate3d(0, 0, ${Math.sin(Date.now() / 1200) * 300}px)
      rotateY(${direction > 0 ? 0 : 180}deg)
      scale(${1 + Math.sin(Date.now() / 1200) * 0.15})
    `,
    transition: "all 0.3s ease-in-out",
    fontSize: "40px", // Bigger than fish
  };

  return <div style={style}>🦈</div>;
};
```

## File: `showcase/fishies/src/components/Starfish.tsx`
```tsx
import { CSSProperties } from "react";

interface StarfishProps {
  x: number;
  y: number;
  size?: number;
}

export const Starfish: React.FC<StarfishProps> = ({ x, y, size = 30 }) => {
  const style: CSSProperties = {
    position: "absolute",
    left: `${x}px`,
    top: `${y}px`,
    fontSize: `${size}px`,
    zIndex: 0,
    transformOrigin: "center",
    animation: "starfish-rotate 5s ease-in-out infinite alternate",
  };

  return <div style={style}>⭐</div>;
};
```

## File: `showcase/fishies/src/components/TerritorialCrab.tsx`
```tsx
import { CSSProperties } from "react";

interface TerritorialCrabProps {
  x: number;
  y: number;
  size?: number;
  intruderNearby?: boolean;
}

export const TerritorialCrab: React.FC<TerritorialCrabProps> = ({
  x,
  y,
  size = 40,
  intruderNearby = false,
}) => {
  const style: CSSProperties = {
    position: "absolute",
    left: `${x}px`,
    top: `${y}px`,
    fontSize: `${size}px`,
    zIndex: 0,
    animation: intruderNearby
      ? "crab-walk 2s linear infinite" // faster animation
      : "crab-walk 4s linear infinite",
  };

  return <div style={style}>🦀</div>;
};
```

## File: `showcase/fishies/src/components/UnderwaterDecorations.tsx`
```tsx
import { useState, useEffect } from "react";
import { type FishState } from "./FishTank";
import { Jellyfish } from "./Jellyfish";
import { Bubble } from "./Bubble";
import { Coral } from "./Coral";
import { Seashell } from "./Seashell";
import { Seaweed } from "./Seaweed";
import { Starfish } from "./Starfish";
import { TerritorialCrab } from "./TerritorialCrab";
import { SeaTurtle } from "./SeaTurtle";
import { Plankton } from "./Plankton";
import { Dolphin } from "./Dolphin";

interface UnderwaterDecorationsProps {
  fishes: FishState[];
}

export const UnderwaterDecorations: React.FC<UnderwaterDecorationsProps> = ({ fishes }) => {
  // Randomly position jellyfish near the top half
  const [jellyfish, setJellyfish] = useState(() =>
    Array.from({ length: 4 }, (_, i) => ({
      id: i,
      x: Math.random() * window.innerWidth * 0.9,
      y: Math.random() * window.innerHeight * 0.5,
      size: 40 + Math.random() * 20,
      isPlayful: false,
    }))
  );

  // Simulate playful interactions every few seconds
  useEffect(() => {
    const interval = setInterval(() => {
      setJellyfish((prev) =>
        prev.map((j) => ({
          ...j,
          isPlayful: Math.random() < 0.3, // 30% chance to be playful
        }))
      );
    }, 3000);
    return () => clearInterval(interval);
  }, []);

  // Create several bubbles that start near the bottom
  const [bubbles] = useState(() =>
    Array.from({ length: 20 }, (_, i) => ({
      id: i,
      x: Math.random() * window.innerWidth,
      y: window.innerHeight - Math.random() * 100,
      size: 5 + Math.random() * 10,
      duration: 3 + Math.random() * 3,
    }))
  );

  // Place corals along the bottom
  const [corals] = useState(() =>
    Array.from({ length: 6 }, (_, i) => ({
      id: i,
      x: Math.random() * (window.innerWidth - 80),
      y: window.innerHeight - 80,
      size: 40 + Math.random() * 20,
    }))
  );

  // Seashells at the bottom
  const [seashells] = useState(() =>
    Array.from({ length: 4 }, (_, i) => ({
      id: i,
      x: Math.random() * (window.innerWidth - 60),
      y: window.innerHeight - 60,
      size: 30 + Math.random() * 10,
    }))
  );

  // Seaweed that gently sways
  const [seaweeds] = useState(() =>
    Array.from({ length: 5 }, (_, i) => ({
      id: i,
      x: Math.random() * (window.innerWidth - 80),
      y: window.innerHeight - 120,
      size: 50 + Math.random() * 20,
    }))
  );

  // Add starfish along the bottom
  const [starfish] = useState(() =>
    Array.from({ length: 3 }, (_, i) => ({
      id: i,
      x: Math.random() * (window.innerWidth - 50),
      y: window.innerHeight - 150 + Math.random() * 50,
      size: 30 + Math.random() * 10,
    }))
  );

  // Add crabs that walk along the bottom
  const [crabs] = useState(() =>
    Array.from({ length: 2 }, (_, i) => ({
      id: i,
      x: Math.random() * (window.innerWidth - 60),
      y: window.innerHeight - 70,
      size: 25 + Math.random() * 10,
    }))
  );

  // Add sea turtles in the middle area
  const [seaTurtles] = useState(() =>
    Array.from({ length: 2 }, (_, i) => ({
      id: i,
      x: Math.random() * (window.innerWidth - 100),
      y: window.innerHeight * 0.3 + Math.random() * 50,
      size: 50 + Math.random() * 20,
    }))
  );

  // Add plankton particles
  const [planktons] = useState(() =>
    Array.from({ length: 10 }, (_, i) => ({
      id: i,
      x: Math.random() * window.innerWidth,
      y: Math.random() * window.innerHeight,
      size: 2 + Math.random() * 2,
      duration: 4 + Math.random() * 4,
    }))
  );

  // Add dolphins near the top/middle
  const [dolphins] = useState(() =>
    Array.from({ length: 2 }, (_, i) => ({
      id: i,
      x: Math.random() * (window.innerWidth * 0.7),
      y: Math.random() * (window.innerHeight * 0.3),
      size: 30 + Math.random() * 20,
    }))
  );

  return (
    <>
      {planktons.map((p) => (
        <Plankton
          key={`plankton-${p.id}`}
          x={p.x}
          y={p.y}
          size={p.size}
          duration={p.duration}
        />
      ))}
      {jellyfish.map((j) => (
        <Jellyfish
          key={`jelly-${j.id}`}
          x={j.x}
          y={j.y}
          size={j.size}
          isPlayful={j.isPlayful}
        />
      ))}
      {bubbles.map((b) => (
        <Bubble
          key={`bubble-${b.id}`}
          x={b.x}
          y={b.y}
          size={b.size}
          duration={b.duration}
        />
      ))}
      {corals.map((c) => (
        <Coral key={`coral-${c.id}`} x={c.x} y={c.y} size={c.size} />
      ))}
      {seashells.map((s) => (
        <Seashell key={`seashell-${s.id}`} x={s.x} y={s.y} size={s.size} />
      ))}
      {seaweeds.map((sw) => (
        <Seaweed key={`seaweed-${sw.id}`} x={sw.x} y={sw.y} size={sw.size} />
      ))}
      {starfish.map((s) => (
        <Starfish key={`starfish-${s.id}`} x={s.x} y={s.y} size={s.size} />
      ))}
      {crabs.map((c) => {
        // Check if any fish are near this crab's territory
        const hasNearbyFish = fishes.some(
          fish => Math.hypot(fish.x - c.x, fish.y - c.y) < 50
        );
        return (
          <TerritorialCrab
            key={`crab-${c.id}`}
            x={c.x}
            y={c.y}
            size={c.size}
            intruderNearby={hasNearbyFish}
          />
        );
      })}
      {seaTurtles.map((t) => (
        <SeaTurtle key={`turtle-${t.id}`} x={t.x} y={t.y} size={t.size} />
      ))}
      {dolphins.map((d) => (
        <Dolphin key={`dolphin-${d.id}`} x={d.x} y={d.y} size={d.size} />
      ))}
    </>
  );
};
```

## File: `showcase/fishies/src/components/WhaleShark.tsx`
```tsx
// src/components/WhaleShark.tsx
import { CSSProperties } from "react";

interface WhaleSharkProps {
  x: number;
  y: number;
  direction: number;
}

export const WhaleShark: React.FC<WhaleSharkProps> = ({ x, y, direction }) => {
  const style: CSSProperties = {
    position: "absolute",
    left: `${x}px`,
    top: `${y}px`,
    zIndex: 1,
    transform: `
      translate3d(0, 0, ${Math.sin(Date.now() / 1500) * 400}px)
      rotateY(${direction > 0 ? 0 : 180}deg)
      scale(${1 + Math.sin(Date.now() / 1500) * 0.2})
    `,
    transition: "all 0.3s ease-in-out",
    fontSize: "64px", // Much bigger than shark
  };

  return <div style={style}>🐋</div>;
};
```

## File: `showcase/minecraft-complex/.eslintrc.cjs`
```
/**
 * This is intended to be a basic starting point for linting in your app.
 * It relies on recommended configs out of the box for simplicity, but you can
 * and should modify this configuration to best suit your team's needs.
 */

/** @type {import('eslint').Linter.Config} */
module.exports = {
  root: true,
  parserOptions: {
    ecmaVersion: "latest",
    sourceType: "module",
    ecmaFeatures: {
      jsx: true,
    },
  },
  env: {
    browser: true,
    commonjs: true,
    es6: true,
  },
  ignorePatterns: ["!**/.server", "!**/.client"],

  // Base config
  extends: ["eslint:recommended"],

  overrides: [
    // React
    {
      files: ["**/*.{js,jsx,ts,tsx}"],
      plugins: ["react", "jsx-a11y"],
      extends: [
        "plugin:react/recommended",
        "plugin:react/jsx-runtime",
        "plugin:react-hooks/recommended",
        "plugin:jsx-a11y/recommended",
      ],
      settings: {
        react: {
          version: "detect",
        },
        formComponents: ["Form"],
        linkComponents: [
          { name: "Link", linkAttribute: "to" },
          { name: "NavLink", linkAttribute: "to" },
        ],
        "import/resolver": {
          typescript: {},
        },
      },
    },

    // Typescript
    {
      files: ["**/*.{ts,tsx}"],
      plugins: ["@typescript-eslint", "import"],
      parser: "@typescript-eslint/parser",
      settings: {
        "import/internal-regex": "^~/",
        "import/resolver": {
          node: {
            extensions: [".ts", ".tsx"],
          },
          typescript: {
            alwaysTryTypes: true,
          },
        },
      },
      extends: [
        "plugin:@typescript-eslint/recommended",
        "plugin:import/recommended",
        "plugin:import/typescript",
      ],
    },

    // Node
    {
      files: [".eslintrc.cjs"],
      env: {
        node: true,
      },
    },
  ],
};
```

## File: `showcase/minecraft-complex/.gitignore`
```
node_modules

/.cache
/build
.env
```

## File: `showcase/minecraft-complex/README.md`
```markdown
# Remix Starter Template

A minimal Remix starter template with TypeScript and Tailwind CSS.

## Get this project

Run the following to clone this starter template:

```bash
codebuff --create remix my-app
```

## Quick Start

```bash
npm run dev
```

Visit [http://localhost:3000](http://localhost:3000)

## Development

```bash
# Install dependencies
npm install

# Start dev server
npm run dev

# Type check
npm run typecheck

# Lint
npm run lint

# Build for production
npm run build
```

## Learn More

- [Codebuff Docs](https://www.codebuff.com/docs)
- [Remix Docs](https://remix.run/docs)
- [Tailwind CSS](https://tailwindcss.com)
```

## File: `showcase/minecraft-complex/knowledge.md`
```markdown
# Remix Template Knowledge

## Project Overview
A minimal Remix + TypeScript starter template with Tailwind CSS for styling.

## Verifying changes
After every change, run:
```bash
npm run typecheck && npm run lint
```
This will check for type errors and lint issues.
```

## File: `showcase/minecraft-complex/package.json`
```json
{
  "name": "remix",
  "private": true,
  "sideEffects": false,
  "type": "module",
  "scripts": {
    "build": "remix vite:build",
    "dev": "remix vite:dev",
    "lint": "eslint --ignore-path .gitignore --cache --cache-location ./node_modules/.cache/eslint .",
    "start": "remix-serve ./build/server/index.js",
    "typecheck": "tsc"
  },
  "dependencies": {
    "@remix-run/node": "^2.15.2",
    "@remix-run/react": "^2.15.2",
    "@remix-run/serve": "^2.15.2",
    "@types/three": "^0.173.0",
    "canvas": "^3.1.0",
    "isbot": "^4.1.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "three": "^0.173.0"
  },
  "devDependencies": {
    "@remix-run/dev": "^2.15.2",
    "@types/react": "^18.2.20",
    "@types/react-dom": "^18.2.7",
    "@typescript-eslint/eslint-plugin": "^6.7.4",
    "@typescript-eslint/parser": "^6.7.4",
    "autoprefixer": "^10.4.19",
    "eslint": "^8.38.0",
    "eslint-import-resolver-typescript": "^3.6.1",
    "eslint-plugin-import": "^2.28.1",
    "eslint-plugin-jsx-a11y": "^6.7.1",
    "eslint-plugin-react": "^7.33.2",
    "eslint-plugin-react-hooks": "^4.6.0",
    "postcss": "^8.4.38",
    "tailwindcss": "^3.4.4",
    "typescript": "~5.3.3",
    "vite": "^5.1.0",
    "vite-tsconfig-paths": "^4.2.1"
  },
  "engines": {
    "node": ">=20.0.0"
  }
}
```

## File: `showcase/minecraft-complex/postcss.config.js`
```javascript
export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
};
```

## File: `showcase/minecraft-complex/tailwind.config.ts`
```typescript
import type { Config } from "tailwindcss";

export default {
  content: ["./app/**/{**,.client,.server}/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      fontFamily: {
        sans: [
          "Inter",
          "ui-sans-serif",
          "system-ui",
          "sans-serif",
          "Apple Color Emoji",
          "Segoe UI Emoji",
          "Segoe UI Symbol",
          "Noto Color Emoji",
        ],
      },
    },
  },
  plugins: [],
} satisfies Config;
```

## File: `showcase/minecraft-complex/tsconfig.json`
```json
{
  "include": [
    "**/*.ts",
    "**/*.tsx",
    "**/.server/**/*.ts",
    "**/.server/**/*.tsx",
    "**/.client/**/*.ts",
    "**/.client/**/*.tsx"
  ],
  "compilerOptions": {
    "lib": ["DOM", "DOM.Iterable", "ES2022"],
    "types": ["@remix-run/node", "vite/client"],
    "isolatedModules": true,
    "esModuleInterop": true,
    "jsx": "react-jsx",
    "module": "ESNext",
    "moduleResolution": "Bundler",
    "resolveJsonModule": true,
    "target": "ES2022",
    "strict": true,
    "allowJs": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "baseUrl": ".",
    "paths": {
      "~/*": ["./app/*"]
    },

    // Vite takes care of building everything, not tsc.
    "noEmit": true
  }
}
```

## File: `showcase/minecraft-complex/vite.config.ts`
```typescript
import { vitePlugin as remix } from "@remix-run/dev";
import { defineConfig } from "vite";
import tsconfigPaths from "vite-tsconfig-paths";

declare module "@remix-run/node" {
  interface Future {
    v3_singleFetch: true;
  }
}

export default defineConfig({
  plugins: [
    remix({
      future: {
        v3_fetcherPersist: true,
        v3_relativeSplatPath: true,
        v3_throwAbortReason: true,
        v3_singleFetch: true,
        v3_lazyRouteDiscovery: true,
      },
    }),
    tsconfigPaths(),
  ],
});
```

## File: `showcase/minecraft-complex/app/entry.client.tsx`
```tsx
/**
 * By default, Remix will handle hydrating your app on the client for you.
 * You are free to delete this file if you'd like to, but if you ever want it revealed again, you can run `npx remix reveal` ✨
 * For more information, see https://remix.run/file-conventions/entry.client
 */

import { RemixBrowser } from "@remix-run/react";
import { startTransition, StrictMode } from "react";
import { hydrateRoot } from "react-dom/client";

startTransition(() => {
  hydrateRoot(
    document,
    <StrictMode>
      <RemixBrowser />
    </StrictMode>
  );
});
```

## File: `showcase/minecraft-complex/app/entry.server.tsx`
```tsx
/**
 * By default, Remix will handle generating the HTTP Response for you.
 * You are free to delete this file if you'd like to, but if you ever want it revealed again, you can run `npx remix reveal` ✨
 * For more information, see https://remix.run/file-conventions/entry.server
 */

import { PassThrough } from "node:stream";

import type { AppLoadContext, EntryContext } from "@remix-run/node";
import { createReadableStreamFromReadable } from "@remix-run/node";
import { RemixServer } from "@remix-run/react";
import { isbot } from "isbot";
import { renderToPipeableStream } from "react-dom/server";

const ABORT_DELAY = 5_000;

export default function handleRequest(
  request: Request,
  responseStatusCode: number,
  responseHeaders: Headers,
  remixContext: EntryContext,
  // This is ignored so we can keep it in the template for visibility.  Feel
  // free to delete this parameter in your app if you're not using it!
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  loadContext: AppLoadContext
) {
  return isbot(request.headers.get("user-agent") || "")
    ? handleBotRequest(
        request,
        responseStatusCode,
        responseHeaders,
        remixContext
      )
    : handleBrowserRequest(
        request,
        responseStatusCode,
        responseHeaders,
        remixContext
      );
}

function handleBotRequest(
  request: Request,
  responseStatusCode: number,
  responseHeaders: Headers,
  remixContext: EntryContext
) {
  return new Promise((resolve, reject) => {
    let shellRendered = false;
    const { pipe, abort } = renderToPipeableStream(
      <RemixServer
        context={remixContext}
        url={request.url}
        abortDelay={ABORT_DELAY}
      />,
      {
        onAllReady() {
          shellRendered = true;
          const body = new PassThrough();
          const stream = createReadableStreamFromReadable(body);

          responseHeaders.set("Content-Type", "text/html");

          resolve(
            new Response(stream, {
              headers: responseHeaders,
              status: responseStatusCode,
            })
          );

          pipe(body);
        },
        onShellError(error: unknown) {
          reject(error);
        },
        onError(error: unknown) {
          responseStatusCode = 500;
          // Log streaming rendering errors from inside the shell.  Don't log
          // errors encountered during initial shell rendering since they'll
          // reject and get logged in handleDocumentRequest.
          if (shellRendered) {
            console.error(error);
          }
        },
      }
    );

    setTimeout(abort, ABORT_DELAY);
  });
}

function handleBrowserRequest(
  request: Request,
  responseStatusCode: number,
  responseHeaders: Headers,
  remixContext: EntryContext
) {
  return new Promise((resolve, reject) => {
    let shellRendered = false;
    const { pipe, abort } = renderToPipeableStream(
      <RemixServer
        context={remixContext}
        url={request.url}
        abortDelay={ABORT_DELAY}
      />,
      {
        onShellReady() {
          shellRendered = true;
          const body = new PassThrough();
          const stream = createReadableStreamFromReadable(body);

          responseHeaders.set("Content-Type", "text/html");

          resolve(
            new Response(stream, {
              headers: responseHeaders,
              status: responseStatusCode,
            })
          );

          pipe(body);
        },
        onShellError(error: unknown) {
          reject(error);
        },
        onError(error: unknown) {
          responseStatusCode = 500;
          // Log streaming rendering errors from inside the shell.  Don't log
          // errors encountered during initial shell rendering since they'll
          // reject and get logged in handleDocumentRequest.
          if (shellRendered) {
            console.error(error);
          }
        },
      }
    );

    setTimeout(abort, ABORT_DELAY);
  });
}
```

## File: `showcase/minecraft-complex/app/root.tsx`
```tsx
import {
  Links,
  Meta,
  Outlet,
  Scripts,
  ScrollRestoration,
} from "@remix-run/react";
import type { LinksFunction } from "@remix-run/node";

import "./tailwind.css";

export const links: LinksFunction = () => [
  { rel: "preconnect", href: "https://fonts.googleapis.com" },
  {
    rel: "preconnect",
    href: "https://fonts.gstatic.com",
    crossOrigin: "anonymous",
  },
  {
    rel: "stylesheet",
    href: "https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap",
  },
];

export function Layout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <head>
        <meta charSet="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <Meta />
        <Links />
      </head>
      <body>
        {children}
        <ScrollRestoration />
        <Scripts />
      </body>
    </html>
  );
}

export default function App() {
  return <Outlet />;
}
```

## File: `showcase/minecraft-complex/app/tailwind.css`
```css
@tailwind base;
@tailwind components;
@tailwind utilities;

html,
body {
  @apply bg-white dark:bg-gray-950;

  @media (prefers-color-scheme: dark) {
    color-scheme: dark;
  }
}
```

## File: `showcase/minecraft-complex/app/routes/_index.tsx`
```tsx
import type { MetaFunction } from "@remix-run/node";
import { Link } from "@remix-run/react";

export const meta: MetaFunction = () => {
  return [
    { title: "New Remix App" },
    { name: "description", content: "Welcome to Remix!" },
  ];
};

export default function Index() {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center gap-4">
      <h1 className="text-2xl font-bold mb-4">Minecraft Clone</h1>
      <div className="text-center mb-4">
        <p>A simple Minecraft-like game where you can:</p>
        <ul className="list-disc text-left mt-2 mb-4">
          <li>Move around with WASD</li>
          <li>Look around with the mouse</li>
          <li>Mine blocks with left click</li>
        </ul>
      </div>
      <Link
        to="/minecraft"
        className="px-6 py-3 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition-colors text-lg font-medium"
      >
        Start Playing
      </Link>
    </div>
  );
}
```

## File: `showcase/minecraft-complex/app/routes/minecraft.tsx`
```tsx
import React, { useEffect, useRef } from "react";
import * as THREE from "three";
import { PointerLockControls } from "three/addons/controls/PointerLockControls.js";

export default function Minecraft() {
  const mountRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!mountRef.current) return;

    const mount = mountRef.current; // Store ref value in variable for cleanup

    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0x87ceeb);
    scene.fog = new THREE.Fog(0x87ceeb, 50, 100);

    const camera = new THREE.PerspectiveCamera(
      75,
      window.innerWidth / window.innerHeight,
      0.1,
      1000
    );
    camera.position.set(0, 20, 5);

    const renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.shadowMap.enabled = true;
    mount.appendChild(renderer.domElement);

    const controls = new PointerLockControls(camera, renderer.domElement);
    scene.add(controls.object);

    const moveState = {
      forward: false,
      backward: false,
      left: false,
      right: false,
      jumping: false,
      onGround: false,
      velocity: new THREE.Vector3(),
      direction: new THREE.Vector3(),
    };
    const GRAVITY = 30.0;
    const JUMP_FORCE = 12.0;
    const MOVE_SPEED = 10.0;

    const inventory = { count: 0 };
    function updateInventoryUI() {
      const invElement = document.getElementById("inventory");
      if (invElement) {
        invElement.innerText = "Inventory: " + inventory.count;
      }
    }

    const onKeyDown = (event: KeyboardEvent) => {
      switch (event.code) {
        case "ArrowUp":
        case "KeyW":
          moveState.forward = true;
          break;
        case "ArrowDown":
        case "KeyS":
          moveState.backward = true;
          break;
        case "ArrowLeft":
        case "KeyA":
          moveState.left = true;
          break;
        case "ArrowRight":
        case "KeyD":
          moveState.right = true;
          break;
        case "Space":
          if (moveState.onGround) {
            moveState.velocity.y = JUMP_FORCE;
            moveState.onGround = false;
          }
          break;
      }
    };

    const onKeyUp = (event: KeyboardEvent) => {
      switch (event.code) {
        case "ArrowUp":
        case "KeyW":
          moveState.forward = false;
          break;
        case "ArrowDown":
        case "KeyS":
          moveState.backward = false;
          break;
        case "ArrowLeft":
        case "KeyA":
          moveState.left = false;
          break;
        case "ArrowRight":
        case "KeyD":
          moveState.right = false;
          break;
      }
    };

    mount.addEventListener("click", () => {
      controls.lock();
    });

    document.addEventListener("keydown", onKeyDown);
    document.addEventListener("keyup", onKeyUp);

    const ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
    scene.add(ambientLight);

    const sunLight = new THREE.DirectionalLight(0xffffff, 0.8);
    sunLight.position.set(100, 100, 0);
    sunLight.castShadow = true;
    scene.add(sunLight);

    const blockSize = 1;
    const textureLoader = new THREE.TextureLoader();

    const grassTopTexture = textureLoader.load("/textures/grass.png");
    const grassSideTexture = textureLoader.load("/textures/dirt.png");
    const dirtTexture = textureLoader.load("/textures/dirt.png");
    const stoneTexture = textureLoader.load("/textures/stone.png");

    [grassTopTexture, grassSideTexture, dirtTexture, stoneTexture].forEach(
      (texture) => {
        texture.magFilter = THREE.NearestFilter;
        texture.minFilter = THREE.NearestFilter;
        texture.repeat.set(1, 1);
        texture.wrapS = THREE.RepeatWrapping;
        texture.wrapT = THREE.RepeatWrapping;
      }
    );

    const stoneMaterial = new THREE.MeshStandardMaterial({
      map: stoneTexture,
      roughness: 1,
      metalness: 0,
    });

    const dirtMaterial = new THREE.MeshStandardMaterial({
      map: dirtTexture,
      roughness: 1,
      metalness: 0,
    });

    const grassMaterials = [
      new THREE.MeshStandardMaterial({ map: grassSideTexture }), // right
      new THREE.MeshStandardMaterial({ map: grassSideTexture }), // left
      new THREE.MeshStandardMaterial({ map: grassTopTexture }), // top
      new THREE.MeshStandardMaterial({ map: dirtTexture }), // bottom
      new THREE.MeshStandardMaterial({ map: grassSideTexture }), // front
      new THREE.MeshStandardMaterial({ map: grassSideTexture }), // back
    ];

    const blockGeo = new THREE.BoxGeometry(blockSize, blockSize, blockSize);
    const blocks: THREE.Mesh[] = [];

    const gridSize = 32;
    const maxHeight = 12;

    function noise(x: number, z: number) {
      return (
        Math.sin(x * 0.3) * Math.cos(z * 0.2) * 2 +
        Math.sin(x * 0.1 + z * 0.5) * 3 +
        Math.cos((x + z) * 0.5) * 2
      );
    }

    for (let i = -Math.floor(gridSize / 2); i < Math.floor(gridSize / 2); i++) {
      for (
        let j = -Math.floor(gridSize / 2);
        j < Math.floor(gridSize / 2);
        j++
      ) {
        const height = Math.max(1, Math.floor(maxHeight / 2 + noise(i, j)));

        for (let y = 0; y < height; y++) {
          let material;
          if (y === height - 1) {
            material = grassMaterials;
          } else if (y >= height - 3) {
            material = dirtMaterial;
          } else {
            material = stoneMaterial;
          }

          const block = new THREE.Mesh(blockGeo, material);
          block.position.set(i * blockSize, y, j * blockSize);
          block.castShadow = true;
          block.receiveShadow = true;
          scene.add(block);
          blocks.push(block);
        }
      }
    }

    const raycaster = new THREE.Raycaster();
    const mouse = new THREE.Vector2();

    let lastMineTime = 0;
    const MINE_COOLDOWN = 250;

    function onMouseDown(event: MouseEvent) {
      if (event.button !== 0) return;

      const currentTime = performance.now();
      if (currentTime - lastMineTime < MINE_COOLDOWN) return;

      mouse.set(0, 0);
      raycaster.setFromCamera(mouse, camera);
      const intersects = raycaster.intersectObjects(blocks);
      if (intersects.length > 0) {
        const hitBlock = intersects[0].object as THREE.Mesh;
        scene.remove(hitBlock);
        const index = blocks.indexOf(hitBlock);
        if (index > -1) blocks.splice(index, 1);
        inventory.count++;
        updateInventoryUI();
        lastMineTime = currentTime;
      }
    }
    window.addEventListener("mousedown", onMouseDown);

    function onRightMouseDown(event: MouseEvent) {
      event.preventDefault();
      if (inventory.count <= 0) return;

      mouse.set(0, 0);
      raycaster.setFromCamera(mouse, camera);
      const intersects = raycaster.intersectObjects(blocks);
      if (intersects.length > 0) {
        const intersect = intersects[0];
        const normal = intersect.face?.normal;
        if (!normal) return;

        const newBlockPos = new THREE.Vector3(
          Math.round(intersect.point.x + normal.x * 0.5),
          Math.round(intersect.point.y + normal.y * 0.5),
          Math.round(intersect.point.z + normal.z * 0.5)
        );

        const exists = blocks.some(
          (b) =>
            Math.abs(b.position.x - newBlockPos.x) < 0.1 &&
            Math.abs(b.position.y - newBlockPos.y) < 0.1 &&
            Math.abs(b.position.z - newBlockPos.z) < 0.1
        );

        if (exists) return;

        const block = new THREE.Mesh(blockGeo, grassMaterials);
        block.position.copy(newBlockPos);
        block.castShadow = true;
        block.receiveShadow = true;
        scene.add(block);
        blocks.push(block);
        inventory.count--;
        updateInventoryUI();
      }
    }
    window.addEventListener("contextmenu", onRightMouseDown);

    function onWindowResize() {
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(window.innerWidth, window.innerHeight);
    }
    window.addEventListener("resize", onWindowResize);

    let dayTime = 0;
    const DAY_LENGTH = 600;

    function updateDayNightCycle(delta: number) {
      dayTime = (dayTime + delta) % DAY_LENGTH;
      const time = dayTime / DAY_LENGTH;

      const angle = time * Math.PI * 2;
      sunLight.position.x = Math.cos(angle) * 100;
      sunLight.position.y = Math.sin(angle) * 100;

      const skyColor = new THREE.Color();
      if (time < 0.25 || time > 0.75) {
        skyColor.setRGB(0.1, 0.1, 0.3);
        sunLight.intensity = 0.2;
        ambientLight.intensity = 0.3;
      } else {
        skyColor.setRGB(0.529, 0.808, 0.922);
        sunLight.intensity = 0.8;
        ambientLight.intensity = 0.6;
      }
      scene.background = skyColor;
      if (scene.fog) {
        scene.fog.color = skyColor;
      }
    }

    function getTerrainHeight(x: number, z: number): number {
      const i = Math.round(x);
      const j = Math.round(z);
      return Math.max(1, Math.floor(maxHeight / 2 + noise(i, j)));
    }

    let prevTime = performance.now();
    function animate() {
      const time = performance.now();
      const delta = (time - prevTime) / 1000;

      updateDayNightCycle(delta);

      moveState.velocity.y -= GRAVITY * delta;
      const pos = controls.object.position;
      
      // Calculate potential new positions
      const potentialX = pos.x + moveState.direction.x * MOVE_SPEED * delta;
      const potentialZ = pos.z + moveState.direction.z * MOVE_SPEED * delta;

      // Get current and potential terrain heights
      const currentHeight = getTerrainHeight(pos.x, pos.z);
      const potentialHeightX = getTerrainHeight(potentialX, pos.z);
      const potentialHeightZ = getTerrainHeight(pos.x, potentialZ);

      // Ground collision check
      if (pos.y <= currentHeight + 1) {
        moveState.velocity.y = 0;
        pos.y = currentHeight + 1;
        moveState.onGround = true;
      } else {
        moveState.onGround = false;
      }

      // Update movement direction
      moveState.direction.z = Number(moveState.forward) - Number(moveState.backward);
      moveState.direction.x = Number(moveState.right) - Number(moveState.left);
      moveState.direction.normalize();

      // Block collision checks - only prevent movement if trying to move to higher terrain
      if (potentialHeightX <= currentHeight) {
        if (moveState.forward || moveState.backward) {
          controls.moveForward(moveState.direction.z * MOVE_SPEED * delta);
        }
      }
      if (potentialHeightZ <= currentHeight) {
        if (moveState.left || moveState.right) {
          controls.moveRight(moveState.direction.x * MOVE_SPEED * delta);
        }
      }

      // Apply gravity
      controls.object.position.y += moveState.velocity.y * delta;

      renderer.render(scene, camera);
      prevTime = time;
      requestAnimationFrame(animate);
    }
    animate();

    return () => {
      mount.removeChild(renderer.domElement);
      window.removeEventListener("mousedown", onMouseDown);
      window.removeEventListener("contextmenu", onRightMouseDown);
      window.removeEventListener("resize", onWindowResize);
      document.removeEventListener("keydown", onKeyDown);
      document.removeEventListener("keyup", onKeyUp);
    };
  }, []);

  return (
    <>
      <div ref={mountRef} style={{ width: "100vw", height: "100vh" }} />
      <div
        id="inventory"
        style={{
          position: "fixed",
          top: "10px",
          left: "10px",
          padding: "8px",
          backgroundColor: "rgba(0,0,0,0.5)",
          color: "white",
          borderRadius: "4px",
          fontFamily: "monospace",
        }}
      >
        Inventory: 0
      </div>
      <div
        style={{
          position: "fixed",
          top: "50%",
          left: "50%",
          transform: "translate(-50%, -50%)",
          width: "20px",
          height: "20px",
          pointerEvents: "none",
        }}
      >
        <div
          style={{
            position: "absolute",
            top: "50%",
            left: "0",
            width: "100%",
            height: "2px",
            backgroundColor: "white",
            transform: "translateY(-50%)",
          }}
        />
        <div
          style={{
            position: "absolute",
            left: "50%",
            top: "0",
            width: "2px",
            height: "100%",
            backgroundColor: "white",
            transform: "translateX(-50%)",
          }}
        />
      </div>
      <div
        style={{
          position: "fixed",
          bottom: "20px",
          left: "50%",
          transform: "translateX(-50%)",
          padding: "10px",
          backgroundColor: "rgba(0,0,0,0.5)",
          color: "white",
          borderRadius: "4px",
          fontFamily: "monospace",
          textAlign: "center",
          display: "flex",
          flexDirection: "column",
          gap: "5px",
        }}
      >
        <div>Click to start</div>
        <div>WASD / Arrow Keys - Move</div>
        <div>Space - Jump</div>
        <div>Left Click - Mine</div>
        <div>Right Click - Place Block</div>
        <div>ESC - Pause</div>
      </div>
    </>
  );
}
```

## File: `showcase/minecraft-complex/scripts/generate-textures.js`
```javascript
import { createCanvas } from 'canvas';
import fs from 'fs';

function generateTexture(colors, filename, pattern = 'noise') {
  const canvas = createCanvas(16, 16);
  const ctx = canvas.getContext('2d');
  
  // Base color
  ctx.fillStyle = colors.base;
  ctx.fillRect(0, 0, 16, 16);
  
  if (pattern === 'noise') {
    // Random noise pattern
    for (let x = 0; x < 16; x++) {
      for (let y = 0; y < 16; y++) {
        if (Math.random() < 0.4) {
          ctx.fillStyle = colors.noise;
          ctx.fillRect(x, y, 1, 1);
        }
        if (Math.random() < 0.1) {
          ctx.fillStyle = colors.highlight;
          ctx.fillRect(x, y, 1, 1);
        }
      }
    }
  } else if (pattern === 'grass') {
    // Grass pattern with small clusters
    for (let x = 0; x < 16; x++) {
      for (let y = 0; y < 16; y++) {
        const noise = Math.sin(x * 0.5) * Math.cos(y * 0.5) + Math.random() * 0.5;
        if (noise > 0.5) {
          ctx.fillStyle = colors.noise;
          ctx.fillRect(x, y, 1, 1);
          // Add highlights on top
          if (Math.random() < 0.3) {
            ctx.fillStyle = colors.highlight;
            ctx.fillRect(x, y, 1, 1);
          }
        }
      }
    }
  } else if (pattern === 'stone') {
    // Stone pattern with cracks
    for (let x = 0; x < 16; x++) {
      for (let y = 0; y < 16; y++) {
        const crack = Math.sin(x * 0.8 + y * 0.3) * Math.cos(y * 0.8 + x * 0.3);
        if (crack > 0.7 || Math.random() < 0.2) {
          ctx.fillStyle = colors.noise;
          ctx.fillRect(x, y, 1, 1);
        }
        if (crack > 0.8) {
          ctx.fillStyle = colors.highlight;
          ctx.fillRect(x, y, 1, 1);
        }
      }
    }
  }
  
  const buffer = canvas.toBuffer('image/png');
  fs.writeFileSync(`public/textures/${filename}`, buffer);
}

// Generate dirt texture - warmer, richer colors
generateTexture(
  { 
    base: '#8B4513',      // Saddle brown
    noise: '#654321',     // Darker brown
    highlight: '#A0522D'  // Sienna (lighter accent)
  },
  'dirt.png',
  'noise'
);

// Generate grass texture - more varied greens
generateTexture(
  {
    base: '#4CAF50',      // Material green
    noise: '#388E3C',     // Darker green
    highlight: '#81C784'  // Light green highlights
  },
  'grass.png',
  'grass'
);

// Generate stone texture - more varied grays with subtle blue tint
generateTexture(
  {
    base: '#757575',      // Mid gray
    noise: '#616161',     // Darker gray
    highlight: '#9E9E9E'  // Light gray highlights
  },
  'stone.png',
  'stone'
);
```

## File: `showcase/minecraft-simple/.eslintrc.json`
```json
{
  "env": {
    "browser": true,
    "es2021": true,
    "jest": true
  },
  "extends": ["eslint:recommended", "prettier"],
  "parserOptions": {
    "ecmaVersion": "latest",
    "sourceType": "module"
  },
  "rules": {
    "indent": ["error", 2],
    "linebreak-style": ["error", "unix"],
    "quotes": ["error", "single"],
    "semi": ["error", "always"]
  }
}
```

## File: `showcase/minecraft-simple/.gitignore`
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
.pnpm-debug.log*

# env files (can opt-in for committing if needed)
.env*

# vercel
.vercel

# typescript
*.tsbuildinfo
next-env.d.ts
```

## File: `showcase/minecraft-simple/.prettierignore`
```
node_modules
dist
coverage
```

## File: `showcase/minecraft-simple/.prettierrc`
```
{
  "semi": true,
  "singleQuote": true,
  "tabWidth": 2,
  "trailingComma": "es5"
}
```

## File: `showcase/minecraft-simple/README.md`
```markdown
# Simple Minecraft Clone

A simple 3D Minecraft-style game built with Three.js.
![minecraft gif](https://github.com/user-attachments/assets/e1a5e6f5-a38a-42c2-955c-fa6de86750ec)

## Get this project

Run the following to clone this starter template:

```bash
codebuff --create minecraft-simple
```

## Development

Start the development server:

```bash
npm start
```

This will open the game in your default browser at http://localhost:8080.

## Controls

- WASD - Move around
- Space/Shift - Move up/down
- Middle Mouse + Drag - Rotate view
- Left Click - Place block
- Right Click - Remove block
- 1-5 Keys - Change block type

## Features

- Day/night cycle
- Different block types (dirt, grass, stone, wood, leaves)
- Block breaking particles
- Walking animation
- Castle with moat
- Store building
- Trees and terrain generation

## Take it from here!

Add your own features (it's easier with Codebuff!).
```

## File: `showcase/minecraft-simple/index.html`
```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Codebuff Minecraft</title>
    <link rel="stylesheet" href="styles.css" />
  </head>
  <body>
    <div id="instructions">
      Controls:<br />
      WASD - Move around<br />
      Space/Shift - Move up/down<br />
      Middle Mouse + Drag - Rotate view<br />
      Left Click - Place block<br />
      Right Click - Remove block<br />
      1-5 Keys - Change block type
    </div>
    <canvas id="game"></canvas>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/0.160.0/three.min.js"></script>
    <audio
      id="placeSound"
      src="https://freesound.org/data/previews/277/277021_5356256-lq.mp3"
      preload="auto"
    ></audio>
    <audio
      id="breakSound"
      src="https://freesound.org/data/previews/444/444641_9159316-lq.mp3"
      preload="auto"
    ></audio>
    <script type="module" src="script.js"></script>
  </body>
</html>
```

## File: `showcase/minecraft-simple/knowledge.md`
```markdown
Generated by [Codebuff](https://www.npmjs.com/package/codebuff)

# Simple minecraft

A simple 3D minecraft in your browser.

## Development server

Use `http-server` to run the development server:

```bash
npm start
```

## Verifying changes

After every change, run `npm run format && npm run lint` to format code and check for any errors that should be fixed.
```

## File: `showcase/minecraft-simple/package.json`
```json
{
  "name": "demo",
  "version": "1.0.0",
  "description": "",
  "main": "script.js",
  "type": "module",
  "scripts": {
    "start": "http-server . -o",
    "lint": "eslint .",
    "format": "prettier --write .",
    "format:check": "prettier --check ."
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "@types/jest": "^29.5.11",
    "eslint": "^8.57.1",
    "eslint-config-prettier": "^10.0.1",
    "http-server": "^14.1.1",
    "jest": "^29.7.0",
    "prettier": "^3.4.2"
  },
  "dependencies": {
    "three": "^0.160.0"
  }
}
```

## File: `showcase/minecraft-simple/script.js`
```javascript
const THREE = window.THREE;

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(
  75,
  window.innerWidth / window.innerHeight,
  0.1,
  1000
);
const renderer = new THREE.WebGLRenderer({
  canvas: document.getElementById('game'),
  antialias: true,
});

renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setClearColor(0x87ceeb); // Set sky blue background

// Block types
const blockTypes = {
  dirt: { color: 0x8b4513, name: 'Dirt' },
  grass: { color: 0x55aa55, name: 'Grass' },
  stone: { color: 0x888888, name: 'Stone' },
  wood: { color: 0x6b4423, name: 'Wood' },
  leaves: { color: 0x2d5a27, name: 'Leaves' },
};

let currentBlockType = 'dirt';
const geometry = new THREE.BoxGeometry(1, 1, 1);
const blocks = new Set();

// Create materials for each block type
const materials = {};
for (const [type, data] of Object.entries(blockTypes)) {
  const texture = new THREE.CanvasTexture(createBlockTexture(data.color));
  materials[type] = new THREE.MeshPhongMaterial({
    map: texture,
    color: 0xffffff, // Use white so texture colors show properly
  });
}

// Create a simple textured pattern for blocks
function createBlockTexture(color) {
  const canvas = document.createElement('canvas');
  canvas.width = 64;
  canvas.height = 64;
  const ctx = canvas.getContext('2d');

  // Fill base color
  ctx.fillStyle = '#' + color.toString(16).padStart(6, '0');
  ctx.fillRect(0, 0, 64, 64);

  // Add some noise/texture
  ctx.fillStyle = 'rgba(0,0,0,0.1)';
  for (let i = 0; i < 64; i += 8) {
    for (let j = 0; j < 64; j += 8) {
      if (Math.random() > 0.5) {
        ctx.fillRect(i, j, 8, 8);
      }
    }
  }

  return canvas;
}

function createBlock(position) {
  const block = new THREE.Mesh(geometry, materials[currentBlockType]);
  block.userData.type = currentBlockType;
  block.position.copy(position);
  block.position.round(); // Snap to grid
  scene.add(block);
  blocks.add(block);
  document
    .getElementById('placeSound')
    .play()
    .catch(() => {}); // Ignore if sound fails
  return block;
}

// Cycle block type with number keys
document.addEventListener('keydown', (event) => {
  const num = parseInt(event.key);
  if (!isNaN(num) && num > 0 && num <= Object.keys(blockTypes).length) {
    currentBlockType = Object.keys(blockTypes)[num - 1];
    // Update block type display
    const blockInfo = document.getElementById('instructions');
    const selectedBlock = blockTypes[currentBlockType].name;
    const lastLine = `Selected: ${selectedBlock}`;
    if (blockInfo.innerHTML.includes('Selected:')) {
      blockInfo.innerHTML = blockInfo.innerHTML.replace(
        /Selected:.*$/,
        lastLine
      );
    } else {
      blockInfo.innerHTML += `<br>${lastLine}`;
    }
  }
});

// Create trees
function createTree(basePosition) {
  // Trunk
  for (let y = 0; y < 4; y++) {
    const pos = basePosition.clone().add(new THREE.Vector3(0, y, 0));
    currentBlockType = 'wood';
    createBlock(pos);
  }

  // Leaves
  currentBlockType = 'leaves';
  for (let x = -1; x <= 1; x++) {
    for (let z = -1; z <= 1; z++) {
      for (let y = 3; y <= 5; y++) {
        const pos = basePosition.clone().add(new THREE.Vector3(x, y, z));
        createBlock(pos);
      }
    }
  }
}

// Create castle components
function createCastleWall(startPos, length, height, direction) {
  const wallBlocks = [];
  const dir = direction.clone().normalize();

  for (let i = 0; i < length; i++) {
    for (let y = 0; y < height; y++) {
      // Main wall
      currentBlockType = 'stone';
      const pos = startPos.clone().add(dir.clone().multiplyScalar(i));
      pos.y = y;
      wallBlocks.push(createBlock(pos));

      // Battlements on top
      if (y === height - 1 && i % 2 === 0) {
        const battlement = pos.clone();
        battlement.y = height;
        wallBlocks.push(createBlock(battlement));
      }
    }
  }
  return wallBlocks;
}

function createCastleTower(basePos, height) {
  const towerBlocks = [];
  const radius = 2;

  for (let y = 0; y < height; y++) {
    for (let x = -radius; x <= radius; x++) {
      for (let z = -radius; z <= radius; z++) {
        if (Math.sqrt(x * x + z * z) <= radius) {
          currentBlockType = 'stone';
          const pos = basePos.clone().add(new THREE.Vector3(x, y, z));
          towerBlocks.push(createBlock(pos));
        }
      }
    }
  }

  // Add cone roof with wood
  currentBlockType = 'wood';
  const roofHeight = 3;
  for (let y = 0; y < roofHeight; y++) {
    const roofRadius = radius - (y / roofHeight) * radius;
    for (let x = -radius; x <= radius; x++) {
      for (let z = -radius; z <= radius; z++) {
        if (Math.sqrt(x * x + z * z) <= roofRadius) {
          const pos = basePos.clone().add(new THREE.Vector3(x, height + y, z));
          towerBlocks.push(createBlock(pos));
        }
      }
    }
  }

  return towerBlocks;
}

// Create initial castle
const castleBasePos = new THREE.Vector3(0, 0, 0);
const wallHeight = 6;
const wallLength = 12;

// Create four walls
createCastleWall(
  castleBasePos,
  wallLength,
  wallHeight,
  new THREE.Vector3(1, 0, 0)
);
createCastleWall(
  castleBasePos,
  wallLength,
  wallHeight,
  new THREE.Vector3(0, 0, 1)
);
createCastleWall(
  castleBasePos.clone().add(new THREE.Vector3(wallLength - 1, 0, 0)),
  wallLength,
  wallHeight,
  new THREE.Vector3(0, 0, 1)
);
createCastleWall(
  castleBasePos.clone().add(new THREE.Vector3(0, 0, wallLength - 1)),
  wallLength,
  wallHeight,
  new THREE.Vector3(1, 0, 0)
);

// Create towers at corners
createCastleTower(castleBasePos, wallHeight + 2);
createCastleTower(
  castleBasePos.clone().add(new THREE.Vector3(wallLength - 1, 0, 0)),
  wallHeight + 2
);
createCastleTower(
  castleBasePos.clone().add(new THREE.Vector3(0, 0, wallLength - 1)),
  wallHeight + 2
);
createCastleTower(
  castleBasePos
    .clone()
    .add(new THREE.Vector3(wallLength - 1, 0, wallLength - 1)),
  wallHeight + 2
);

// Create gate in front wall
const gateWidth = 2;
const gateHeight = 4;
const gatePos = castleBasePos
  .clone()
  .add(new THREE.Vector3(wallLength / 2 - gateWidth / 2, 0, 0));
for (let x = 0; x < gateWidth; x++) {
  for (let y = gateHeight; y < wallHeight; y++) {
    currentBlockType = 'stone';
    createBlock(gatePos.clone().add(new THREE.Vector3(x, y, 0)));
  }
}

// Create keep in center
const keepSize = 4;
const keepHeight = wallHeight + 1;
const keepPos = castleBasePos
  .clone()
  .add(
    new THREE.Vector3(
      wallLength / 2 - keepSize / 2,
      0,
      wallLength / 2 - keepSize / 2
    )
  );
for (let x = 0; x < keepSize; x++) {
  for (let z = 0; z < keepSize; z++) {
    for (let y = 0; y < keepHeight; y++) {
      currentBlockType = 'stone';
      createBlock(keepPos.clone().add(new THREE.Vector3(x, y, z)));
    }
  }
}

// Create courtyard decorations
// Training grounds (dirt area)
currentBlockType = 'dirt';
for (let x = 2; x < 5; x++) {
  for (let z = 2; z < 5; z++) {
    createBlock(castleBasePos.clone().add(new THREE.Vector3(x, 0, z)));
  }
}

// Garden (grass and flowers)
currentBlockType = 'grass';
for (let x = 7; x < 10; x++) {
  for (let z = 2; z < 5; z++) {
    createBlock(castleBasePos.clone().add(new THREE.Vector3(x, 0, z)));
  }
}

// Well (stone circle with wood top)
currentBlockType = 'stone';
const wellCenter = castleBasePos.clone().add(new THREE.Vector3(3, 0, 8));
for (let y = 0; y < 2; y++) {
  createBlock(wellCenter.clone().add(new THREE.Vector3(0, y, 0)));
  createBlock(wellCenter.clone().add(new THREE.Vector3(1, y, 0)));
  createBlock(wellCenter.clone().add(new THREE.Vector3(0, y, 1)));
  createBlock(wellCenter.clone().add(new THREE.Vector3(1, y, 1)));
}
currentBlockType = 'wood';
createBlock(wellCenter.clone().add(new THREE.Vector3(0, 2, 0)));
createBlock(wellCenter.clone().add(new THREE.Vector3(1, 2, 0)));

// Create moat around castle
const moatWidth = 2;
const moatDepth = 2;
for (let x = -moatWidth; x < wallLength + moatWidth; x++) {
  for (let z = -moatWidth; z < wallLength + moatWidth; z++) {
    // Skip the actual castle area
    if (x >= 0 && x < wallLength && z >= 0 && z < wallLength) continue;
    // Create water-filled moat
    currentBlockType = 'stone';
    for (let y = 0; y > -moatDepth; y--) {
      createBlock(new THREE.Vector3(x, y, z));
    }
  }
}

// Create store building
function createStore(position) {
  // Main structure
  currentBlockType = 'wood';
  // Floor
  for (let x = 0; x < 5; x++) {
    for (let z = 0; z < 4; z++) {
      createBlock(position.clone().add(new THREE.Vector3(x, 0, z)));
    }
  }

  // Walls
  for (let y = 1; y < 4; y++) {
    for (let x = 0; x < 5; x++) {
      createBlock(position.clone().add(new THREE.Vector3(x, y, 0)));
      createBlock(position.clone().add(new THREE.Vector3(x, y, 3)));
    }
    for (let z = 1; z < 3; z++) {
      createBlock(position.clone().add(new THREE.Vector3(0, y, z)));
      createBlock(position.clone().add(new THREE.Vector3(4, y, z)));
    }
  }

  // Roof
  currentBlockType = 'stone';
  for (let x = 0; x < 5; x++) {
    for (let z = 0; z < 4; z++) {
      createBlock(position.clone().add(new THREE.Vector3(x, 4, z)));
    }
  }

  // Door
  currentBlockType = 'wood';
  for (let y = 1; y < 3; y++) {
    createBlock(position.clone().add(new THREE.Vector3(2, y, 0)));
  }

  // Counter
  currentBlockType = 'wood';
  for (let x = 1; x < 4; x++) {
    createBlock(position.clone().add(new THREE.Vector3(x, 1, 2)));
  }

  // Shelves on back wall
  for (let x = 1; x < 4; x++) {
    createBlock(position.clone().add(new THREE.Vector3(x, 2, 3)));
  }

  // Display items (using different block types as merchandise)
  currentBlockType = 'stone';
  createBlock(position.clone().add(new THREE.Vector3(1, 2, 2)));
  currentBlockType = 'dirt';
  createBlock(position.clone().add(new THREE.Vector3(2, 2, 2)));
  currentBlockType = 'grass';
  createBlock(position.clone().add(new THREE.Vector3(3, 2, 2)));
}

// Create store near the castle
createStore(new THREE.Vector3(-8, 0, 4));

// Create initial terrain with trees and path
for (let x = -20; x <= 20; x += 4) {
  for (let z = -10; z <= 10; z += 4) {
    // Create stone path leading to castle gate
    if (Math.abs(z) < 4 && x < 0) {
      currentBlockType = 'stone';
      createBlock(new THREE.Vector3(x, 0, z));
    }
    // Add trees away from the path
    else if (Math.random() < 0.3) {
      // 30% chance of tree at each spot
      createTree(new THREE.Vector3(x, 0, z));
    }
  }
}

// Create initial block for player reference
createBlock(new THREE.Vector3(0, 0, 0));

// Add lighting
const light = new THREE.DirectionalLight(0xffffff, 1);
light.position.set(5, 10, 5);
scene.add(light);
scene.add(new THREE.AmbientLight(0x808080)); // Brighter ambient light

// Day/night cycle
let timeOfDay = 0;
const dayLength = 900; // 900 seconds = 15 minutes per day
function updateDayNightCycle() {
  timeOfDay = (timeOfDay + 1) % dayLength;
  const time = timeOfDay / dayLength;

  // Adjust sky color
  const skyColorDay = new THREE.Color(0x87ceeb); // Sky blue
  const skyColorNight = new THREE.Color(0x1a2b3c); // Dark blue
  const skyColor = skyColorDay.lerp(skyColorNight, Math.sin(time * Math.PI));
  scene.background = skyColor;

  // Adjust light intensity
  light.intensity = Math.cos(time * Math.PI) * 0.5 + 0.5;
}

// Add sky background
scene.background = new THREE.Color(0x87ceeb);

// Create player model
const playerBody = new THREE.Group();

// Body
const bodyGeometry = new THREE.BoxGeometry(0.6, 0.8, 0.3);
const bodyMaterial = new THREE.MeshPhongMaterial({ color: 0x3366cc });
const body = new THREE.Mesh(bodyGeometry, bodyMaterial);
body.position.y = 0.9;

// Head
const headGeometry = new THREE.BoxGeometry(0.4, 0.4, 0.4);
const headMaterial = new THREE.MeshPhongMaterial({ color: 0xffcc99 });
const head = new THREE.Mesh(headGeometry, headMaterial);
head.position.y = 1.5;

// Sunglasses
const glassesGeometry = new THREE.BoxGeometry(0.45, 0.15, 0.1);
const glassesMaterial = new THREE.MeshPhongMaterial({ color: 0x000000 });
const glasses = new THREE.Mesh(glassesGeometry, glassesMaterial);
glasses.position.z = 0.2;
head.add(glasses);

// Party hat (cone shape using blocks)
currentBlockType = 'grass';
const hat = new THREE.Group();
for (let y = 0; y < 3; y++) {
  const hatGeometry = new THREE.BoxGeometry(0.3 - y * 0.1, 0.1, 0.3 - y * 0.1);
  const hatMaterial = new THREE.MeshPhongMaterial({ color: 0xff00ff });
  const hatPiece = new THREE.Mesh(hatGeometry, hatMaterial);
  hatPiece.position.y = 0.25 + y * 0.1;
  hat.add(hatPiece);
}
hat.position.y = 0.3;
head.add(hat);

// Fire particles on head
const fireParticles = [];
const fireParticleCount = 20;
const fireParticleMaterial = new THREE.MeshBasicMaterial({ color: 0xff4400 });

function updateFireParticles() {
  // Remove old particles
  fireParticles.forEach((p) => {
    if (p.position.y > head.position.y + 2) {
      scene.remove(p);
      const index = fireParticles.indexOf(p);
      if (index > -1) fireParticles.splice(index, 1);
    }
  });

  // Add new particles
  while (fireParticles.length < fireParticleCount) {
    const particle = new THREE.Mesh(
      new THREE.BoxGeometry(0.1, 0.1, 0.1),
      fireParticleMaterial
    );
    particle.position.copy(head.getWorldPosition(new THREE.Vector3()));
    particle.position.y += 0.2;
    particle.velocity = new THREE.Vector3(
      (Math.random() - 0.5) * 0.05,
      0.1,
      (Math.random() - 0.5) * 0.05
    );
    scene.add(particle);
    fireParticles.push(particle);
  }

  // Update particle positions
  fireParticles.forEach((particle) => {
    particle.position.add(particle.velocity);
  });
}

// Arms
const armGeometry = new THREE.BoxGeometry(0.2, 0.6, 0.2);
const armMaterial = new THREE.MeshPhongMaterial({ color: 0x3366cc });
const leftArm = new THREE.Mesh(armGeometry, armMaterial);
leftArm.position.set(0.4, 1.1, 0);
const rightArm = new THREE.Mesh(armGeometry, armMaterial);
rightArm.position.set(-0.4, 1.1, 0);

// Legs
const legGeometry = new THREE.BoxGeometry(0.2, 0.6, 0.2);
const legMaterial = new THREE.MeshPhongMaterial({ color: 0x1a1a1a });
const leftLeg = new THREE.Mesh(legGeometry, legMaterial);
leftLeg.position.set(0.2, 0.3, 0);
const rightLeg = new THREE.Mesh(legGeometry, legMaterial);
rightLeg.position.set(-0.2, 0.3, 0);

// Add parts to player
playerBody.add(body);
playerBody.add(head);
playerBody.add(leftArm);
playerBody.add(rightArm);
playerBody.add(leftLeg);
playerBody.add(rightLeg);
const player = playerBody;
player.position.set(2, 1, 5);
scene.add(player);

// Create cat model
const catBody = new THREE.Group();

// Body
const catBodyGeometry = new THREE.BoxGeometry(0.4, 0.3, 0.6);
const catBodyMaterial = new THREE.MeshPhongMaterial({ color: 0x808080 }); // Gray cat
const catBodyMesh = new THREE.Mesh(catBodyGeometry, catBodyMaterial);
catBodyMesh.position.y = 0.3;

// Head
const catHeadGeometry = new THREE.BoxGeometry(0.3, 0.3, 0.3);
const catHeadMesh = new THREE.Mesh(catHeadGeometry, catBodyMaterial);
catHeadMesh.position.set(0, 0.5, 0.25);

// Ears (triangular prisms using boxes)
const earGeometry = new THREE.BoxGeometry(0.1, 0.1, 0.1);
const leftEar = new THREE.Mesh(earGeometry, catBodyMaterial);
const rightEar = new THREE.Mesh(earGeometry, catBodyMaterial);
leftEar.position.set(0.1, 0.1, 0);
rightEar.position.set(-0.1, 0.1, 0);
catHeadMesh.add(leftEar);
catHeadMesh.add(rightEar);

// Tail (series of small boxes)
const tailGroup = new THREE.Group();
for (let i = 0; i < 5; i++) {
  const tailSegment = new THREE.Mesh(
    new THREE.BoxGeometry(0.1, 0.1, 0.1),
    catBodyMaterial
  );
  tailSegment.position.set(0, 0, -i * 0.1);
  tailGroup.add(tailSegment);
}
tailGroup.position.set(0, 0.3, -0.3);
tailGroup.rotation.x = Math.PI / 4; // Tail up at 45 degrees

// Add all parts to cat
catBody.add(catBodyMesh);
catBody.add(catHeadMesh);
catBody.add(tailGroup);

// Position cat near player
catBody.position.set(4, 1, 5);
scene.add(catBody);

// Position camera behind player
camera.position.set(2, 3, 8);
camera.lookAt(player.position);

// Movement and rotation controls
const moveSpeed = 0.1;
const rotateSpeed = 0.02;
const keysPressed = {};
let isRotating = false;
let lastMouseX = 0;

document.addEventListener('keydown', (event) => {
  keysPressed[event.key.toLowerCase()] = true;
});

document.addEventListener('keyup', (event) => {
  keysPressed[event.key.toLowerCase()] = false;
});

// Block interaction
const raycaster = new THREE.Raycaster();
const mouse = new THREE.Vector2();
let highlightBox = null;

// Create highlight box
const highlightGeometry = new THREE.BoxGeometry(1.001, 1.001, 1.001);
const highlightMaterial = new THREE.MeshBasicMaterial({
  color: 0xffffff,
  opacity: 0.3,
  transparent: true,
  side: THREE.FrontSide,
});

function handleClick(event) {
  mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
  mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;

  raycaster.setFromCamera(mouse, camera);
  const intersects = raycaster.intersectObjects([...blocks]);

  if (event.button === 0) {
    // Left click
    if (intersects.length > 0) {
      // Get block position by adding normal to intersection object position
      const position = intersects[0].object.position
        .clone()
        .add(intersects[0].face.normal);
      createBlock(position);
    } else {
      // Place block at a fixed distance when clicking in empty space
      const direction = raycaster.ray.direction;
      const position = camera.position.clone().add(direction.multiplyScalar(5));
      createBlock(position);
    }
  } else if (event.button === 2 && intersects.length > 0) {
    // Right click
    const block = intersects[0].object;
    createBreakParticles(block.position, block.userData.type);
    scene.remove(block);
    blocks.delete(block);
    document
      .getElementById('breakSound')
      .play()
      .catch(() => {}); // Ignore if sound fails
  }
}

function createBreakParticles(position, blockType) {
  const particleCount = 8;
  const particles = [];
  const material = materials[blockType];

  for (let i = 0; i < particleCount; i++) {
    const particle = new THREE.Mesh(
      new THREE.BoxGeometry(0.2, 0.2, 0.2),
      material
    );

    particle.position.copy(position);
    particle.velocity = new THREE.Vector3(
      (Math.random() - 0.5) * 0.3,
      Math.random() * 0.2,
      (Math.random() - 0.5) * 0.3
    );

    scene.add(particle);
    particles.push(particle);

    // Remove particle after 1 second
    setTimeout(() => {
      scene.remove(particle);
    }, 1000);
  }

  // Animate particles
  const startTime = Date.now();
  function animateParticles() {
    const elapsed = Date.now() - startTime;
    if (elapsed > 1000) return;

    particles.forEach((particle) => {
      particle.position.add(particle.velocity);
      particle.velocity.y -= 0.01; // Gravity
    });

    requestAnimationFrame(animateParticles);
  }
  animateParticles();
}

window.addEventListener('mousemove', (event) => {
  mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
  mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;

  if (isRotating) {
    const deltaX = event.clientX - lastMouseX;
    camera.rotation.y -= deltaX * rotateSpeed;
    lastMouseX = event.clientX;
  }
});

window.addEventListener('mousedown', (event) => {
  if (event.button === 1) {
    // Middle mouse button
    isRotating = true;
    lastMouseX = event.clientX;
  } else {
    handleClick(event);
  }
});

window.addEventListener('mouseup', () => {
  isRotating = false;
});

window.addEventListener('mousemove', (event) => {
  if (isRotating) {
    const deltaX = event.clientX - lastMouseX;
    camera.rotation.y -= deltaX * rotateSpeed;
    lastMouseX = event.clientX;
  }
});

window.addEventListener('contextmenu', (e) => e.preventDefault());

let walkCycle = 0;
let isJumping = false;
let jumpVelocity = 0;
const gravity = 0.005;

function handleMovement() {
  // Get the camera's forward and right vectors for movement direction
  const forward = new THREE.Vector3(0, 0, -1).applyQuaternion(
    camera.quaternion
  );
  const right = new THREE.Vector3(1, 0, 0).applyQuaternion(camera.quaternion);
  forward.y = 0; // Keep movement horizontal
  right.y = 0;
  forward.normalize();
  right.normalize();

  // Move player relative to camera direction
  const isMoving =
    keysPressed['w'] ||
    keysPressed['s'] ||
    keysPressed['a'] ||
    keysPressed['d'];
  if (keysPressed['w']) player.position.addScaledVector(forward, moveSpeed);
  if (keysPressed['s']) player.position.addScaledVector(forward, -moveSpeed);
  if (keysPressed['a']) player.position.addScaledVector(right, -moveSpeed);
  if (keysPressed['d']) player.position.addScaledVector(right, moveSpeed);

  // Walking animation
  if (isMoving) {
    walkCycle += 0.15;
    const leftLeg = player.children[4];
    const rightLeg = player.children[5];
    const leftArm = player.children[2];
    const rightArm = player.children[3];

    // Legs and arms swing in opposite directions for natural walking
    leftLeg.rotation.x = Math.sin(walkCycle) * 0.5;
    rightLeg.rotation.x = Math.sin(walkCycle + Math.PI) * 0.5;
    leftArm.rotation.x = Math.sin(walkCycle + Math.PI) * 0.5;
    rightArm.rotation.x = Math.sin(walkCycle) * 0.5;
  }

  // Jump physics
  if (keysPressed[' '] && !isJumping) {
    jumpVelocity = 0.3;
    isJumping = true;
  }

  if (isJumping) {
    player.position.y += jumpVelocity;
    jumpVelocity -= gravity;

    // Check for landing
    if (player.position.y <= 1) {
      player.position.y = 1;
      isJumping = false;
      jumpVelocity = 0;
    }
  }

  if (keysPressed['shift']) {
    player.position.y -= moveSpeed;
  }

  // Update camera position to follow player
  const cameraOffset = new THREE.Vector3(0, 2, 3);
  camera.position.copy(player.position).add(cameraOffset);
  camera.lookAt(player.position);
}

function updateHighlight() {
  raycaster.setFromCamera(mouse, camera);
  const intersects = raycaster.intersectObjects([...blocks]);

  if (intersects.length > 0) {
    const position = intersects[0].object.position
      .clone()
      .add(intersects[0].face.normal);
    if (!highlightBox) {
      highlightBox = new THREE.Mesh(highlightGeometry, highlightMaterial);
      scene.add(highlightBox);
    }
    highlightBox.position.copy(position).round();
  } else if (highlightBox) {
    scene.remove(highlightBox);
    highlightBox = null;
  }
}

function animate() {
  requestAnimationFrame(animate);
  handleMovement();
  updateHighlight();
  updateDayNightCycle();
  updateFireParticles();
  renderer.render(scene, camera);
}

animate();

// Handle window resizing
window.addEventListener('resize', () => {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
});
```

## File: `showcase/minecraft-simple/styles.css`
```css
body {
  font-family: Arial, sans-serif;
  line-height: 1.6;
  margin: 0;
  padding: 0;
  background-color: #87ceeb; /* Sky blue background */
  overflow: hidden;
}

canvas {
  width: 100vw;
  height: 100vh;
  display: block;
}

#instructions {
  position: fixed;
  top: 10px;
  left: 10px;
  background: rgba(0, 0, 0, 0.7);
  color: white;
  padding: 15px;
  border-radius: 5px;
  font-size: 14px;
  pointer-events: none;
}
```

## File: `starter-templates/README.md`
```markdown
# Codebuff starters
Starter template projects for [Codebuff](https://codebuff.com)!

Run `codebuff --create <template> [project-name]` to start a new project based on the template. You can use the name of any directory here as the template, e.g.:

```bash
codebuff --create nextjs my-app
```
```

## File: `starter-templates/chrome-extension/.eslintrc.json`
```json
{
  "root": true,
  "env": {
    "browser": true,
    "es2020": true,
    "webextensions": true
  },
  "extends": [
    "eslint:recommended",
    "plugin:@typescript-eslint/recommended",
    "plugin:react-hooks/recommended"
  ],
  "ignorePatterns": ["dist", ".eslintrc.json"],
  "parser": "@typescript-eslint/parser",
  "plugins": ["react-refresh"],
  "rules": {
    "react-refresh/only-export-components": [
      "warn",
      { "allowConstantExport": true }
    ]
  }
}
```

## File: `starter-templates/chrome-extension/.gitignore`
```
node_modules/
dist/
.DS_Store
**.log
```

## File: `starter-templates/chrome-extension/README.md`
```markdown
# Chrome Extension Template

A minimal Chrome extension starter template with TypeScript and modern tooling.

## Use this template

```bash
# Create a new project using this template
codebuff --create chrome-extension my-extension
```

## Getting Started

```bash
# Install dependencies
npm install

# Start development build with watch mode
npm run dev

# Build for production
npm run build

# Type check
npm run typecheck
```

## Project Structure
- `src/` - Source files
  - `background/` - Service worker (background script)
  - `content/` - Content scripts
  - `popup/` - Extension popup UI
  - `options/` - Options page
- `public/` - Static assets and manifest.json
- `dist/` - Built extension ready for loading into Chrome

## Loading the extension
1. Build the extension: `npm run build`
2. Open Chrome and navigate to `chrome://extensions`
3. Enable "Developer mode"
4. Click "Load unpacked" and select the `dist` directory

## Learn More
- [Chrome Extension Documentation](https://developer.chrome.com/brain/knowledge/docs_legacy/extensions)
```

## File: `starter-templates/chrome-extension/codebuff.json`
```json
{
  "description": "Template configuration for this project. See https://www.codebuff.com/config for all options.",
  "startupProcesses": [
    {
      "name": "dev",
      "command": "npm run dev",
      "enabled": true,
      "stdoutFile": "logs/dev.log"
    }
  ],
  "fileChangeHooks": [
    {
      "name": "lint",
      "command": "npm run lint -- --fix",
      "enabled": true
    },
    {
      "name": "typecheck",
      "command": "npm run typecheck",
      "enabled": true
    }
  ]
}
```

## File: `starter-templates/chrome-extension/knowledge.md`
```markdown
# Chrome Extension Template Knowledge

## Project Overview
A minimal Chrome extension template with TypeScript, React, and Vite for modern extension development.

## Key Features
- Uses Vite for fast builds and HMR
- React for popup and options pages
- TypeScript for type safety
- Manifest V3 compliant
- Multiple entry points (popup, options, background, content)

## Verifying changes
After every change, run:
```bash
npm run typecheck && npm run lint
```
This will check for type errors and linting issues.

## Best Practices
- Keep service worker (background script) lightweight
- Use content scripts sparingly and only on needed pages
- Prefer using storage.sync over storage.local for user settings
- Follow Chrome's security best practices for CSP

## Development Workflow
- Always test extension in incognito mode to verify permissions
- Test on both HTTP and HTTPS sites if using content scripts
- Keep permissions minimal - request only what you need
- Chrome Web Store requires:
  - One-time $5 USD developer fee
  - Detailed description and screenshots
  - Privacy policy if collecting data
  - Review process takes 1-3 business days

## Common Gotchas
- Service worker cannot use DOM APIs
- Content scripts have limited access to Chrome APIs
- Popup must be loaded from local extension files
- Cross-origin requests need explicit permissions
```

## File: `starter-templates/chrome-extension/package.json`
```json
{
  "name": "chrome-extension",
  "version": "1.0.0",
  "private": true,
  "type": "module",
  "scripts": {
    "dev": "vite build --watch",
    "build": "vite build",
    "typecheck": "tsc --noEmit",
    "lint": "eslint . --ext ts,tsx --report-unused-disable-directives --max-warnings 0"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "devDependencies": {
    "@types/chrome": "^0.0.262",
    "@types/node": "^22.12.0",
    "@types/react": "^18.2.64",
    "@types/react-dom": "^18.2.21",
    "@typescript-eslint/eslint-plugin": "^7.1.1",
    "@typescript-eslint/parser": "^7.1.1",
    "@vitejs/plugin-react": "^4.2.1",
    "eslint": "^8.57.0",
    "eslint-plugin-react-hooks": "^4.6.0",
    "eslint-plugin-react-refresh": "^0.4.5",
    "typescript": "^5.2.2",
    "vite": "^5.1.6"
  }
}
```

## File: `starter-templates/chrome-extension/tsconfig.json`
```json
{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,

    /* Bundler mode */
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx",

    /* Linting */
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true
  },
  "include": ["src"],
  "references": [{ "path": "./tsconfig.node.json" }]
}
```

## File: `starter-templates/chrome-extension/tsconfig.node.json`
```json
{
  "compilerOptions": {
    "composite": true,
    "skipLibCheck": true,
    "module": "ESNext",
    "moduleResolution": "bundler",
    "allowSyntheticDefaultImports": true,
    "types": ["node"]
  },
  "include": ["vite.config.ts"]
}
```

## File: `starter-templates/chrome-extension/vite.config.ts`
```typescript
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { resolve } from 'path'

export default defineConfig({
  plugins: [react()],
  build: {
    rollupOptions: {
      input: {
        popup: resolve(__dirname, 'src/popup/index.html'),
        options: resolve(__dirname, 'src/options/index.html'),
        background: resolve(__dirname, 'src/background/index.ts'),
        content: resolve(__dirname, 'src/content/index.ts'),
      },
      output: {
        entryFileNames: '[name]/index.js',
        chunkFileNames: '[name].js',
        assetFileNames: '[name]/[name].[ext]'
      }
    }
  }
})
```

## File: `starter-templates/chrome-extension/public/manifest.json`
```json
{
  "manifest_version": 3,
  "name": "Chrome Extension",
  "version": "1.0.0",
  "description": "A Chrome extension starter template",
  "permissions": ["storage"],
  "background": {
    "service_worker": "background/index.js",
    "type": "module"
  },
  "action": {
    "default_popup": "popup/index.html"
  },
  "options_page": "options/index.html",
  "content_scripts": [
    {
      "matches": ["<all_urls>"],
      "js": ["content/index.js"]
    }
  ],
  "icons": {
    "16": "icons/icon16.png",
    "32": "icons/icon32.png",
    "48": "icons/icon48.png",
    "128": "icons/icon128.png"
  }
}
```

## File: `starter-templates/chrome-extension/src/background/index.ts`
```typescript
// Example background script (service worker)
chrome.runtime.onInstalled.addListener(() => {
  console.log('Extension installed')
})

// This keeps the service worker active
export {}
```

## File: `starter-templates/chrome-extension/src/content/index.ts`
```typescript
// Example content script
console.log('Content script loaded')
```

## File: `starter-templates/chrome-extension/src/options/Options.tsx`
```tsx
import React from 'react'

const Options: React.FC = () => {
  return (
    <div>
      <h1>Extension Options</h1>
      <p>Configure your extension settings here.</p>
    </div>
  )
}

export default Options
```

## File: `starter-templates/chrome-extension/src/options/index.html`
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Extension Options</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="./main.tsx"></script>
  </body>
</html>
```

## File: `starter-templates/chrome-extension/src/options/main.tsx`
```tsx
import React from 'react'
import ReactDOM from 'react-dom/client'
import Options from './Options'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <Options />
  </React.StrictMode>,
)
```

## File: `starter-templates/chrome-extension/src/popup/Popup.tsx`
```tsx
import { useState, useEffect } from 'react'

export default function Popup() {
  const [count, setCount] = useState(0)

  useEffect(() => {
    // Example of using Chrome APIs
    chrome.storage.sync.get(['count'], (result) => {
      setCount(result.count || 0)
    })
  }, [])

  const increment = () => {
    const newCount = count + 1
    setCount(newCount)
    chrome.storage.sync.set({ count: newCount })
  }

  return (
    <div style={{ width: '300px', padding: '1rem' }}>
      <h1>Chrome Extension</h1>
      <button onClick={increment}>
        Count is {count}
      </button>
    </div>
  )
}
```

## File: `starter-templates/chrome-extension/src/popup/index.html`
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Chrome Extension</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="./main.tsx"></script>
  </body>
</html>
```

## File: `starter-templates/chrome-extension/src/popup/main.tsx`
```tsx
import React from 'react'
import ReactDOM from 'react-dom/client'
import Popup from './Popup'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <Popup />
  </React.StrictMode>,
)
```

## File: `starter-templates/convex/.env`
```
# Production environment variables go here
```

## File: `starter-templates/convex/.gitignore`
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

# local env files
.env*.local

# vercel
.vercel

# typescript
*.tsbuildinfo
next-env.d.ts

# log files
**.log
```

## File: `starter-templates/convex/.prettierignore`
```
.next
convex/_generated
```

## File: `starter-templates/convex/README.md`
```markdown
# Convex

This example demonstrates the [Convex](https://convex.dev) backend platform.

## Get this project

Run the following to clone this starter template:

```bash
codebuff --create convex my-app
```

## Development

While developing:

```bash
npm run dev
```

This command runs `next dev` and `convex dev` at the same time. This command will log you into Convex, so you'll need to create a Convex account if this is your first project.

Once everything is working, commit your code and deploy it to the cloud with [Vercel](https://vercel.com/new?utm_source=github&utm_medium=readme&utm_campaign=next-example) ([Documentation](https://nextjs.org/brain/knowledge/docs_legacy/deployment)).

Use `npx convex deploy --cmd 'npm run build'` as the build command and set the `CONVEX_DEPLOY_KEY` environmental variable in Vercel ([Documentation](https://docs.convex.dev/production/hosting/vercel)).
```

## File: `starter-templates/convex/codebuff.json`
```json
{
  "description": "Template configuration for this project. See https://www.codebuff.com/config for all options.",
  "startupProcesses": [
    {
      "name": "dev",
      "command": "npm run dev",
      "enabled": true,
      "stdoutFile": "logs/dev.log"
    }
  ],
  "fileChangeHooks": [
    {
      "name": "typecheck",
      "command": "npm run typecheck",
      "enabled": true
    }
  ]
}
```

## File: `starter-templates/convex/convex.knowledge.md`
```markdown
---
description: Guidelines and best practices for building Convex projects, including database schema design, queries, mutations, and real-world examples
globs: **/*.{ts,tsx,js,jsx}
---

Downloaded from: https://docs.convex.dev/ai

<convex_guidelines>
  <function_guidelines>
    <new_function_syntax>
      - ALWAYS use the new function syntax for Convex functions. For example:
      ```typescript
      import { query } from "./_generated/server";
      import { v } from "convex/values";
      export const f = query({
          args: {},
          returns: v.null(),
          handler: async (ctx, args) => {
          // Function body
          },
      });
      ```
    </new_function_syntax>
    <http_endpoint_syntax>
      - HTTP endpoints are defined in `convex/http.ts` and require an `httpAction` decorator. For example:
      ```typescript
      import { httpRouter } from "convex/server";
      import { httpAction } from "./_generated/server";
      const http = httpRouter();
      http.route({
          path: "/echo",
          method: "POST",
          handler: httpAction(async (ctx, req) => {
          const body = await req.bytes();
          return new Response(body, { status: 200 });
          }),
      });
      ```
      - HTTP endpoints are always registered at the exact path you specify in the `path` field. For example, if you specify `/api/someRoute`, the endpoint will be registered at `/api/someRoute`.
    </http_endpoint_syntax>
    <function_registration>
      - Use `internalQuery`, `internalMutation`, and `internalAction` to register internal functions. These functions are private and aren't part of an app's API. They can only be called by other Convex functions.
      - Use `query`, `mutation`, and `action` to register public functions. These functions are part of the public API and are exposed to the public Internet. Do NOT use `query`, `mutation`, or `action` to register sensitive internal functions that should be kept private.
      - You CANNOT register a function through the `api` or `internal` objects.
      - ALWAYS include argument and return validators for all Convex functions. If a function doesn't return anything, include `returns: v.null()` as its output validator.
      - If the JavaScript implementation of a Convex function doesn't have a return value, it implicitly returns `null`.
    </function_registration>
    <function_calling>
      - Use `ctx.runQuery` to call a query from a query, mutation, or action.
      - Use `ctx.runMutation` to call a mutation from a mutation or action.
      - Use `ctx.runAction` to call an action from an action.
      - ONLY call an action from another action if you need to cross runtimes (e.g. from V8 to Node). Otherwise, pull out the shared code into a helper async function and call that directly instead.
      - Try to use as few calls from actions to queries and mutations as possible. Queries and mutations are transactions, so splitting logic up into multiple calls introduces the risk of race conditions.
      - All of these calls take in a `FunctionReference`. Do NOT try to pass the callee function directly into one of these calls.
      - When using `ctx.runQuery`, `ctx.runMutation`, or `ctx.runAction` to call a function in the same file, specify a type annotation on the return value to work around TypeScript circularity limitations. For example,
                            ```
                            export const f = query({
                              args: { name: v.string() },
                              returns: v.string(),
                              handler: async (ctx, args) => {
                                return "Hello " + args.name;
                              },
                            });

                            export const g = query({
                              args: {},
                              returns: v.null(),
                              handler: async (ctx, args) => {
                                const result: string = await ctx.runQuery(api.example.f, { name: "Bob" });
                                return null;
                              },
                            });
                            ```
    </function_calling>
    <function_references>
      - Function references are pointers to registered Convex functions.
      - Use the `api` object defined by the framework in `convex/_generated/api.ts` to call public functions registered with `query`, `mutation`, or `action`.
      - Use the `internal` object defined by the framework in `convex/_generated/api.ts` to call internal (or private) functions registered with `internalQuery`, `internalMutation`, or `internalAction`.
      - Convex uses file-based routing, so a public function defined in `convex/example.ts` named `f` has a function reference of `api.example.f`.
      - A private function defined in `convex/example.ts` named `g` has a function reference of `internal.example.g`.
      - Functions can also registered within directories nested within the `convex/` folder. For example, a public function `h` defined in `convex/messages/access.ts` has a function reference of `api.messages.access.h`.
    </function_references>
    <api_design>
      - Convex uses file-based routing, so thoughtfully organize files with public query, mutation, or action functions within the `convex/` directory.
      - Use `query`, `mutation`, and `action` to define public functions.
      - Use `internalQuery`, `internalMutation`, and `internalAction` to define private, internal functions.
    </api_design>
  </function_guidelines>
  <validator_guidelines>
    - `v.bigint()` is deprecated for representing signed 64-bit integers. Use `v.int64()` instead.
    - Use `v.record()` for defining a record type. `v.map()` and `v.set()` are not supported.
  </validator_guidelines>
  <schema_guidelines>
    - Always define your schema in `convex/schema.ts`.
    - Always import the schema definition functions from `convex/server`:
    - System fields are automatically added to all documents and are prefixed with an underscore.
  </schema_guidelines>
  <typescript_guidelines>
    - You can use the helper typescript type `Id` imported from './_generated/dataModel' to get the type of the id for a given table. For example if there is a table called 'users' you can use `Id<'users'>` to get the type of the id for that table.
    - If you need to define a `Record` make sure that you correctly provide the type of the key and value in the type. For example a validator `v.record(v.id('users'), v.string())` would have the type `Record<Id<'users'>, string>`.
    - Be strict with types, particularly around id's of documents. For example, if a function takes in an id for a document in the 'users' table, take in `Id<'users'>` rather than `string`.
  </typescript_guidelines>
  <full_text_search_guidelines>
    - A query for "10 messages in channel '#general' that best match the query 'hello hi' in their body" would look like:

const messages = await ctx.db
  .query("messages")
  .withSearchIndex("search_body", (q) =>
    q.search("body", "hello hi").eq("channel", "#general"),
  )
  .take(10);
  </full_text_search_guidelines>
  <query_guidelines>
    - Do NOT use `filter` in queries. Instead, define an index in the schema and use `withIndex` instead.
    - Convex queries do NOT support `.delete()`. Instead, `.collect()` the results, iterate over them, and call `ctx.db.delete(row._id)` on each result.
    - Use `.unique()` to get a single document from a query. This method will throw an error if there are multiple documents that match the query.
    <ordering>
      - By default Convex always returns documents in ascending `_creationTime` order.
      - You can use `.order('asc')` or `.order('desc')` to pick whether a query is in ascending or descending order. If the order isn't specified, it defaults to ascending.
      - Document queries that use indexes will be ordered based on the columns in the index and can avoid slow table scans.
    </ordering>
  </query_guidelines>
  <mutation_guidelines>
    - Use `ctx.db.replace` to fully replace an existing document. This method will throw an error if the document does not exist.
    - Use `ctx.db.patch` to shallow merge updates into an existing document. This method will throw an error if the document does not exist.
  </mutation_guidelines>
  <scheduling_guidelines>
    <cron_guidelines>
      - Only use the `crons.interval` or `crons.cron` methods to schedule cron jobs. Do NOT use the `crons.hourly`, `crons.daily`, or `crons.weekly` helpers.
      - Both cron methods take in a FunctionReference. Do NOT try to pass the function directly into one of these methods.
      - Define crons by declaring the top-level `crons` object, calling some methods on it, and then exporting it as default. For example,
                            ```ts
                            import { cronJobs } from "convex/server";
                            import { internal } from "./_generated/api";

                            const crons = cronJobs();

                            // Run `internal.users.deleteInactive` every two hours.
                            crons.interval("delete inactive users", { hours: 2 }, internal.users.deleteInactive, {});

                            export default crons;
                            ```
      - You can register Convex functions within `crons.ts` just like any other file.
      - If a cron calls an internal function, always import the `internal` object from '_generated/api`, even if the internal function is registered in the same file.
    </cron_guidelines>
  </scheduling_guidelines>
  <file_storage_guidelines>
    - Convex includes file storage for large files like images, videos, and PDFs.
    - The `ctx.storage.getUrl()` method returns a signed URL for a given file. It returns `null` if the file doesn't exist.
    - Do NOT use the deprecated `ctx.storage.getMetadata` call for loading a file's metadata.

                    Instead, query the `_storage` system table. For example, you can use `ctx.db.system.get` to get an `Id<"_storage">`.
                    ```
                    import { query } from "./_generated/server";
                    import { Id } from "./_generated/dataModel";

                    type FileMetadata = {
                        _id: Id<"_storage">;
                        _creationTime: number;
                        contentType?: string;
                        sha256: string;
                        size: number;
                    }

                    export const exampleQuery = query({
                        args: { fileId: v.id("_storage") },
                        returns: v.null();
                        handler: async (ctx, args) => {
                            const metadata: FileMetadata | null = await ctx.db.system.get(args.fileId);
                            console.log(metadata);
                            return null;
                        },
                    });
                    ```
  </file_storage_guidelines>
</convex_guidelines>


<examples>
<example name="chat-app">
  <task>
    Create a real-time chat application backend with AI responses. The app should:
- Allow creating users with names
- Support multiple chat channels
- Enable users to send messages to channels
- Automatically generate AI responses to user messages
- Show recent message history

The backend should provide APIs for:
1. User management (creation)
2. Channel management (creation)
3. Message operations (sending, listing)
4. AI response generation using OpenAI's GPT-4

Messages should be stored with their channel, author, and content. The system should maintain message order
and limit history display to the 10 most recent messages per channel.

  </task>
  <response>
    <analysis>
      1. Task Requirements Summary:
- Build a real-time chat backend with AI integration
- Support user creation
- Enable channel-based conversations
- Store and retrieve messages with proper ordering
- Generate AI responses automatically

2. Main Components Needed:
- Database tables: users, channels, messages
- Public APIs for user/channel management
- Message handling functions
- Internal AI response generation system
- Context loading for AI responses

3. Public API and Internal Functions Design:
Public Mutations:
- createUser:
  - file path: convex/index.ts
  - arguments: {name: v.string()}
  - returns: v.object({userId: v.id("users")})
  - purpose: Create a new user with a given name
- createChannel:
  - file path: convex/index.ts
  - arguments: {name: v.string()}
  - returns: v.object({channelId: v.id("channels")})
  - purpose: Create a new channel with a given name
- sendMessage:
  - file path: convex/index.ts
  - arguments: {channelId: v.id("channels"), authorId: v.id("users"), content: v.string()}
  - returns: v.null()
  - purpose: Send a message to a channel and schedule a response from the AI

Public Queries:
- listMessages:
  - file path: convex/index.ts
  - arguments: {channelId: v.id("channels")}
  - returns: v.array(v.object({
    _id: v.id("messages"),
    _creationTime: v.number(),
    channelId: v.id("channels"),
    authorId: v.optional(v.id("users")),
    content: v.string(),
    }))
  - purpose: List the 10 most recent messages from a channel in descending creation order

Internal Functions:
- generateResponse:
  - file path: convex/index.ts
  - arguments: {channelId: v.id("channels")}
  - returns: v.null()
  - purpose: Generate a response from the AI for a given channel
- loadContext:
  - file path: convex/index.ts
  - arguments: {channelId: v.id("channels")}
  - returns: v.array(v.object({
    _id: v.id("messages"),
    _creationTime: v.number(),
    channelId: v.id("channels"),
    authorId: v.optional(v.id("users")),
    content: v.string(),
  }))
- writeAgentResponse:
  - file path: convex/index.ts
  - arguments: {channelId: v.id("channels"), content: v.string()}
  - returns: v.null()
  - purpose: Write an AI response to a given channel

4. Schema Design:
- users
  - validator: { name: v.string() }
  - indexes: <none>
- channels
  - validator: { name: v.string() }
  - indexes: <none>
- messages
  - validator: { channelId: v.id("channels"), authorId: v.optional(v.id("users")), content: v.string() }
  - indexes
    - by_channel: ["channelId"]

5. Background Processing:
- AI response generation runs asynchronously after each user message
- Uses OpenAI's GPT-4 to generate contextual responses
- Maintains conversation context using recent message history

    </analysis>
    <file path="package.json">
      {
  "name": "chat-app",
  "description": "This example shows how to build a chat app without authentication.",
  "version": "1.0.0",
  "dependencies": {
    "convex": "^1.17.4",
    "openai": "^4.79.0"
  }
}
    </file>
    <file path="convex/index.ts">
      import {
  query,
  mutation,
  internalQuery,
  internalMutation,
  internalAction,
} from "./_generated/server";
import { v } from "convex/values";
import OpenAI from "openai";
import { internal } from "./_generated/api";

/**
 * Create a user with a given name.
 */
export const createUser = mutation({
  args: {
    name: v.string(),
  },
  returns: v.id("users"),
  handler: async (ctx, args) => {
    return await ctx.db.insert("users", { name: args.name });
  },
});

/**
 * Create a channel with a given name.
 */
export const createChannel = mutation({
  args: {
    name: v.string(),
  },
  returns: v.id("channels"),
  handler: async (ctx, args) => {
    return await ctx.db.insert("channels", { name: args.name });
  },
});

/**
 * List the 10 most recent messages from a channel in descending creation order.
 */
export const listMessages = query({
  args: {
    channelId: v.id("channels"),
  },
  returns: v.array(
    v.object({
      _id: v.id("messages"),
      _creationTime: v.number(),
      channelId: v.id("channels"),
      authorId: v.optional(v.id("users")),
      content: v.string(),
    }),
  ),
  handler: async (ctx, args) => {
    const messages = await ctx.db
      .query("messages")
      .withIndex("by_channel", (q) => q.eq("channelId", args.channelId))
      .order("desc")
      .take(10);
    return messages;
  },
});

/**
 * Send a message to a channel and schedule a response from the AI.
 */
export const sendMessage = mutation({
  args: {
    channelId: v.id("channels"),
    authorId: v.id("users"),
    content: v.string(),
  },
  returns: v.null(),
  handler: async (ctx, args) => {
    const channel = await ctx.db.get(args.channelId);
    if (!channel) {
      throw new Error("Channel not found");
    }
    const user = await ctx.db.get(args.authorId);
    if (!user) {
      throw new Error("User not found");
    }
    await ctx.db.insert("messages", {
      channelId: args.channelId,
      authorId: args.authorId,
      content: args.content,
    });
    await ctx.scheduler.runAfter(0, internal.index.generateResponse, {
      channelId: args.channelId,
    });
    return null;
  },
});

const openai = new OpenAI();

export const generateResponse = internalAction({
  args: {
    channelId: v.id("channels"),
  },
  returns: v.null(),
  handler: async (ctx, args) => {
    const context = await ctx.runQuery(internal.index.loadContext, {
      channelId: args.channelId,
    });
    const response = await openai.chat.completions.create({
      model: "gpt-4o",
      messages: context,
    });
    const content = response.choices[0].message.content;
    if (!content) {
      throw new Error("No content in response");
    }
    await ctx.runMutation(internal.index.writeAgentResponse, {
      channelId: args.channelId,
      content,
    });
    return null;
  },
});

export const loadContext = internalQuery({
  args: {
    channelId: v.id("channels"),
  },
  returns: v.array(
    v.object({
      role: v.union(v.literal("user"), v.literal("assistant")),
      content: v.string(),
    }),
  ),
  handler: async (ctx, args) => {
    const channel = await ctx.db.get(args.channelId);
    if (!channel) {
      throw new Error("Channel not found");
    }
    const messages = await ctx.db
      .query("messages")
      .withIndex("by_channel", (q) => q.eq("channelId", args.channelId))
      .order("desc")
      .take(10);

    const result = [];
    for (const message of messages) {
      if (message.authorId) {
        const user = await ctx.db.get(message.authorId);
        if (!user) {
          throw new Error("User not found");
        }
        result.push({
          role: "user" as const,
          content: `${user.name}: ${message.content}`,
        });
      } else {
        result.push({ role: "assistant" as const, content: message.content });
      }
    }
    return result;
  },
});

export const writeAgentResponse = internalMutation({
  args: {
    channelId: v.id("channels"),
    content: v.string(),
  },
  returns: v.null(),
  handler: async (ctx, args) => {
    await ctx.db.insert("messages", {
      channelId: args.channelId,
      content: args.content,
    });
    return null;
  },
});
    </file>
    <file path="convex/schema.ts">
      import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  channels: defineTable({
    name: v.string(),
  }),

  users: defineTable({
    name: v.string(),
  }),

  messages: defineTable({
    channelId: v.id("channels"),
    authorId: v.optional(v.id("users")),
    content: v.string(),
  }).index("by_channel", ["channelId"]),
});
    </file>
  </response>
</example>
</examples>
```

## File: `starter-templates/convex/knowledge.md`
```markdown
Generated by [Codebuff](https://www.npmjs.com/package/codebuff)

# Your project's knowledge

Add any information here or instructions that will help Codebuff maintain your project.

## Verifying changes

After every change, run `npm run typecheck` to check for any errors that should be fixed.
```

## File: `starter-templates/convex/package.json`
```json
{
  "private": true,
  "scripts": {
    "dev": "npm-run-all --parallel dev:backend dev:frontend",
    "build": "tsc && next build",
    "dev:backend": "convex dev",
    "dev:frontend": "next dev",
    "predev": "convex dev --until-success",
    "start": "next start",
    "typecheck": "tsc --noEmit"
  },
  "dependencies": {
    "convex": "^1.12.0",
    "next": "latest",
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "devDependencies": {
    "@types/node": "^18.15.3",
    "@types/react": "18.0.37",
    "@types/react-dom": "18.0.11",
    "npm-run-all": "^4.1.5",
    "typescript": "^4.9.5"
  }
}
```

## File: `starter-templates/convex/tsconfig.json`
```json
{
  "compilerOptions": {
    "target": "es5",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx"],
  "exclude": ["node_modules"]
}
```

## File: `starter-templates/convex/convex/README.md`
```markdown
# Welcome to your Convex functions directory!

Write your Convex functions here.
See https://docs.convex.dev/functions for more.

A query function that takes two arguments looks like:

```ts
// functions.js
import { query } from "./_generated/server";
import { v } from "convex/values";

export const myQueryFunction = query({
  // Validators for arguments.
  args: {
    first: v.number(),
    second: v.string(),
  },

  // Function implementation.
  handler: async (ctx, args) => {
    // Read the database as many times as you need here.
    // See https://docs.convex.dev/database/reading-data.
    const documents = await ctx.db.query("tablename").collect();

    // Arguments passed from the client are properties of the args object.
    console.log(args.first, args.second);

    // Write arbitrary JavaScript here: filter, aggregate, build derived data,
    // remove non-public properties, or create new objects.
    return documents;
  },
});
```

Using this query function in a React component looks like:

```ts
const data = useQuery(api.functions.myQueryFunction, {
  first: 10,
  second: "hello",
});
```

A mutation function looks like:

```ts
// functions.js
import { mutation } from "./_generated/server";
import { v } from "convex/values";

export const myMutationFunction = mutation({
  // Validators for arguments.
  args: {
    first: v.string(),
    second: v.string(),
  },

  // Function implementation.
  handler: async (ctx, args) => {
    // Insert or modify documents in the database here.
    // Mutations can also read from the database like queries.
    // See https://docs.convex.dev/database/writing-data.
    const message = { body: args.first, author: args.second };
    const id = await ctx.db.insert("messages", message);

    // Optionally, return a value from your mutation.
    return await ctx.db.get(id);
  },
});
```

Using this mutation function in a React component looks like:

```ts
const mutation = useMutation(api.functions.myMutationFunction);
function handleButtonPress() {
  // fire and forget, the most common way to use mutations
  mutation({ first: "Hello!", second: "me" });
  // OR
  // use the result once the mutation has completed
  mutation({ first: "Hello!", second: "me" }).then((result) =>
    console.log(result),
  );
}
```

Use the Convex CLI to push your functions to a deployment. See everything
the Convex CLI can do by running `npx convex -h` in your project root
directory. To learn more, launch the docs with `npx convex docs`.
```

## File: `starter-templates/convex/convex/messages.ts`
```typescript
import { query, mutation } from "./_generated/server";
import { Doc, Id } from "./_generated/dataModel";
import { v } from "convex/values";

export const list = query({
  args: {},
  handler: async (ctx): Promise<Doc<"messages">[]> => {
    return await ctx.db.query("messages").collect();
  },
});

export const send = mutation({
  args: { body: v.string(), author: v.string() },
  handler: async (ctx, args): Promise<Id<"messages">> => {
    const { body, author } = args;
    return await ctx.db.insert("messages", { body, author });
  },
});
```

## File: `starter-templates/convex/convex/schema.ts`
```typescript
import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema(
  {
    messages: defineTable({
      author: v.string(),
      body: v.string(),
    }),
  },
  {
    // When you want runtime validation of the schema, set this to true.
    schemaValidation: false,
    // This option allows you to read and write tables not specified here.
    // strictTableNameTypes: false,
  },
);
```

## File: `starter-templates/convex/convex/tsconfig.json`
```json
{
  /* This TypeScript project config describes the environment that
   * Convex functions run in and is used to typecheck them.
   * You can modify it, but some settings required to use Convex.
   */
  "compilerOptions": {
    /* These settings are not required by Convex and can be modified. */
    "allowJs": true,
    "strict": true,

    /* These compiler options are required by Convex */
    "target": "ESNext",
    "lib": ["ES2021", "dom"],
    "forceConsistentCasingInFileNames": true,
    "allowSyntheticDefaultImports": true,
    "module": "ESNext",
    "moduleResolution": "Node",
    "isolatedModules": true,
    "skipLibCheck": true,
    "noEmit": true
  },
  "include": ["./**/*"],
  "exclude": ["./_generated"]
}
```

## File: `starter-templates/convex/convex/_generated/api.d.ts`
```typescript
/* eslint-disable */
/**
 * Generated `api` utility.
 *
 * THIS CODE IS AUTOMATICALLY GENERATED.
 *
 * To regenerate, run `npx convex dev`.
 * @module
 */

import type {
  ApiFromModules,
  FilterApi,
  FunctionReference,
} from "convex/server";
import type * as messages from "../messages.js";

/**
 * A utility for referencing Convex functions in your app's API.
 *
 * Usage:
 * ```js
 * const myFunctionReference = api.myModule.myFunction;
 * ```
 */
declare const fullApi: ApiFromModules<{
  messages: typeof messages;
}>;
export declare const api: FilterApi<
  typeof fullApi,
  FunctionReference<any, "public">
>;
export declare const internal: FilterApi<
  typeof fullApi,
  FunctionReference<any, "internal">
>;
```

## File: `starter-templates/convex/convex/_generated/api.js`
```javascript
/* eslint-disable */
/**
 * Generated `api` utility.
 *
 * THIS CODE IS AUTOMATICALLY GENERATED.
 *
 * To regenerate, run `npx convex dev`.
 * @module
 */

import { anyApi } from "convex/server";

/**
 * A utility for referencing Convex functions in your app's API.
 *
 * Usage:
 * ```js
 * const myFunctionReference = api.myModule.myFunction;
 * ```
 */
export const api = anyApi;
export const internal = anyApi;
```

## File: `starter-templates/convex/convex/_generated/dataModel.d.ts`
```typescript
/* eslint-disable */
/**
 * Generated data model types.
 *
 * THIS CODE IS AUTOMATICALLY GENERATED.
 *
 * To regenerate, run `npx convex dev`.
 * @module
 */

import type {
  DataModelFromSchemaDefinition,
  DocumentByName,
  TableNamesInDataModel,
  SystemTableNames,
} from "convex/server";
import type { GenericId } from "convex/values";
import schema from "../schema.js";

/**
 * The names of all of your Convex tables.
 */
export type TableNames = TableNamesInDataModel<DataModel>;

/**
 * The type of a document stored in Convex.
 *
 * @typeParam TableName - A string literal type of the table name (like "users").
 */
export type Doc<TableName extends TableNames> = DocumentByName<
  DataModel,
  TableName
>;

/**
 * An identifier for a document in Convex.
 *
 * Convex documents are uniquely identified by their `Id`, which is accessible
 * on the `_id` field. To learn more, see [Document IDs](https://docs.convex.dev/using/document-ids).
 *
 * Documents can be loaded using `db.get(id)` in query and mutation functions.
 *
 * IDs are just strings at runtime, but this type can be used to distinguish them from other
 * strings when type checking.
 *
 * @typeParam TableName - A string literal type of the table name (like "users").
 */
export type Id<TableName extends TableNames | SystemTableNames> =
  GenericId<TableName>;

/**
 * A type describing your Convex data model.
 *
 * This type includes information about what tables you have, the type of
 * documents stored in those tables, and the indexes defined on them.
 *
 * This type is used to parameterize methods like `queryGeneric` and
 * `mutationGeneric` to make them type-safe.
 */
export type DataModel = DataModelFromSchemaDefinition<typeof schema>;
```

## File: `starter-templates/convex/convex/_generated/server.d.ts`
```typescript
/* eslint-disable */
/**
 * Generated utilities for implementing server-side Convex query and mutation functions.
 *
 * THIS CODE IS AUTOMATICALLY GENERATED.
 *
 * To regenerate, run `npx convex dev`.
 * @module
 */

import {
  ActionBuilder,
  HttpActionBuilder,
  MutationBuilder,
  QueryBuilder,
  GenericActionCtx,
  GenericMutationCtx,
  GenericQueryCtx,
  GenericDatabaseReader,
  GenericDatabaseWriter,
} from "convex/server";
import type { DataModel } from "./dataModel.js";

/**
 * Define a query in this Convex app's public API.
 *
 * This function will be allowed to read your Convex database and will be accessible from the client.
 *
 * @param func - The query function. It receives a {@link QueryCtx} as its first argument.
 * @returns The wrapped query. Include this as an `export` to name it and make it accessible.
 */
export declare const query: QueryBuilder<DataModel, "public">;

/**
 * Define a query that is only accessible from other Convex functions (but not from the client).
 *
 * This function will be allowed to read from your Convex database. It will not be accessible from the client.
 *
 * @param func - The query function. It receives a {@link QueryCtx} as its first argument.
 * @returns The wrapped query. Include this as an `export` to name it and make it accessible.
 */
export declare const internalQuery: QueryBuilder<DataModel, "internal">;

/**
 * Define a mutation in this Convex app's public API.
 *
 * This function will be allowed to modify your Convex database and will be accessible from the client.
 *
 * @param func - The mutation function. It receives a {@link MutationCtx} as its first argument.
 * @returns The wrapped mutation. Include this as an `export` to name it and make it accessible.
 */
export declare const mutation: MutationBuilder<DataModel, "public">;

/**
 * Define a mutation that is only accessible from other Convex functions (but not from the client).
 *
 * This function will be allowed to modify your Convex database. It will not be accessible from the client.
 *
 * @param func - The mutation function. It receives a {@link MutationCtx} as its first argument.
 * @returns The wrapped mutation. Include this as an `export` to name it and make it accessible.
 */
export declare const internalMutation: MutationBuilder<DataModel, "internal">;

/**
 * Define an action in this Convex app's public API.
 *
 * An action is a function which can execute any JavaScript code, including non-deterministic
 * code and code with side-effects, like calling third-party services.
 * They can be run in Convex's JavaScript environment or in Node.js using the "use node" directive.
 * They can interact with the database indirectly by calling queries and mutations using the {@link ActionCtx}.
 *
 * @param func - The action. It receives an {@link ActionCtx} as its first argument.
 * @returns The wrapped action. Include this as an `export` to name it and make it accessible.
 */
export declare const action: ActionBuilder<DataModel, "public">;

/**
 * Define an action that is only accessible from other Convex functions (but not from the client).
 *
 * @param func - The function. It receives an {@link ActionCtx} as its first argument.
 * @returns The wrapped function. Include this as an `export` to name it and make it accessible.
 */
export declare const internalAction: ActionBuilder<DataModel, "internal">;

/**
 * Define an HTTP action.
 *
 * This function will be used to respond to HTTP requests received by a Convex
 * deployment if the requests matches the path and method where this action
 * is routed. Be sure to route your action in `convex/http.js`.
 *
 * @param func - The function. It receives an {@link ActionCtx} as its first argument.
 * @returns The wrapped function. Import this function from `convex/http.js` and route it to hook it up.
 */
export declare const httpAction: HttpActionBuilder;

/**
 * A set of services for use within Convex query functions.
 *
 * The query context is passed as the first argument to any Convex query
 * function run on the server.
 *
 * This differs from the {@link MutationCtx} because all of the services are
 * read-only.
 */
export type QueryCtx = GenericQueryCtx<DataModel>;

/**
 * A set of services for use within Convex mutation functions.
 *
 * The mutation context is passed as the first argument to any Convex mutation
 * function run on the server.
 */
export type MutationCtx = GenericMutationCtx<DataModel>;

/**
 * A set of services for use within Convex action functions.
 *
 * The action context is passed as the first argument to any Convex action
 * function run on the server.
 */
export type ActionCtx = GenericActionCtx<DataModel>;

/**
 * An interface to read from the database within Convex query functions.
 *
 * The two entry points are {@link DatabaseReader.get}, which fetches a single
 * document by its {@link Id}, or {@link DatabaseReader.query}, which starts
 * building a query.
 */
export type DatabaseReader = GenericDatabaseReader<DataModel>;

/**
 * An interface to read from and write to the database within Convex mutation
 * functions.
 *
 * Convex guarantees that all writes within a single mutation are
 * executed atomically, so you never have to worry about partial writes leaving
 * your data in an inconsistent state. See [the Convex Guide](https://docs.convex.dev/understanding/convex-fundamentals/functions#atomicity-and-optimistic-concurrency-control)
 * for the guarantees Convex provides your functions.
 */
export type DatabaseWriter = GenericDatabaseWriter<DataModel>;
```

## File: `starter-templates/convex/convex/_generated/server.js`
```javascript
/* eslint-disable */
/**
 * Generated utilities for implementing server-side Convex query and mutation functions.
 *
 * THIS CODE IS AUTOMATICALLY GENERATED.
 *
 * To regenerate, run `npx convex dev`.
 * @module
 */

import {
  actionGeneric,
  httpActionGeneric,
  queryGeneric,
  mutationGeneric,
  internalActionGeneric,
  internalMutationGeneric,
  internalQueryGeneric,
} from "convex/server";

/**
 * Define a query in this Convex app's public API.
 *
 * This function will be allowed to read your Convex database and will be accessible from the client.
 *
 * @param func - The query function. It receives a {@link QueryCtx} as its first argument.
 * @returns The wrapped query. Include this as an `export` to name it and make it accessible.
 */
export const query = queryGeneric;

/**
 * Define a query that is only accessible from other Convex functions (but not from the client).
 *
 * This function will be allowed to read from your Convex database. It will not be accessible from the client.
 *
 * @param func - The query function. It receives a {@link QueryCtx} as its first argument.
 * @returns The wrapped query. Include this as an `export` to name it and make it accessible.
 */
export const internalQuery = internalQueryGeneric;

/**
 * Define a mutation in this Convex app's public API.
 *
 * This function will be allowed to modify your Convex database and will be accessible from the client.
 *
 * @param func - The mutation function. It receives a {@link MutationCtx} as its first argument.
 * @returns The wrapped mutation. Include this as an `export` to name it and make it accessible.
 */
export const mutation = mutationGeneric;

/**
 * Define a mutation that is only accessible from other Convex functions (but not from the client).
 *
 * This function will be allowed to modify your Convex database. It will not be accessible from the client.
 *
 * @param func - The mutation function. It receives a {@link MutationCtx} as its first argument.
 * @returns The wrapped mutation. Include this as an `export` to name it and make it accessible.
 */
export const internalMutation = internalMutationGeneric;

/**
 * Define an action in this Convex app's public API.
 *
 * An action is a function which can execute any JavaScript code, including non-deterministic
 * code and code with side-effects, like calling third-party services.
 * They can be run in Convex's JavaScript environment or in Node.js using the "use node" directive.
 * They can interact with the database indirectly by calling queries and mutations using the {@link ActionCtx}.
 *
 * @param func - The action. It receives an {@link ActionCtx} as its first argument.
 * @returns The wrapped action. Include this as an `export` to name it and make it accessible.
 */
export const action = actionGeneric;

/**
 * Define an action that is only accessible from other Convex functions (but not from the client).
 *
 * @param func - The function. It receives an {@link ActionCtx} as its first argument.
 * @returns The wrapped function. Include this as an `export` to name it and make it accessible.
 */
export const internalAction = internalActionGeneric;

/**
 * Define a Convex HTTP action.
 *
 * @param func - The function. It receives an {@link ActionCtx} as its first argument, and a `Request` object
 * as its second.
 * @returns The wrapped endpoint function. Route a URL path to this function in `convex/http.js`.
 */
export const httpAction = httpActionGeneric;
```

## File: `starter-templates/convex/pages/_app.tsx`
```tsx
import "../styles/globals.css";
import type { AppProps } from "next/app";

import { ConvexProvider, ConvexReactClient } from "convex/react";

const address = process.env.NEXT_PUBLIC_CONVEX_URL;
if (!address) {
  throw new Error("Convex deployment url not found in environment.");
}
const convex = new ConvexReactClient(address);

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <ConvexProvider client={convex}>
      <Component {...pageProps} />
    </ConvexProvider>
  );
}

export default MyApp;
```

## File: `starter-templates/convex/pages/index.tsx`
```tsx
import { FormEvent, useEffect, useState } from "react";
import { useMutation, useQuery } from "convex/react";
import { api } from "../convex/_generated/api";

export default function App() {
  const messages = useQuery(api.messages.list);
  const sendMessage = useMutation(api.messages.send);

  const [newMessageText, setNewMessageText] = useState("");
  const [name, setName] = useState("user");

  useEffect(() => {
    setName("User " + Math.floor(Math.random() * 10000));
  }, []);

  async function handleSendMessage(event: FormEvent) {
    event.preventDefault();
    setNewMessageText("");
    await sendMessage({ body: newMessageText, author: name });
  }
  return (
    <main>
      <h1>Convex Chat</h1>
      <p className="badge">
        <span>{name}</span>
      </p>
      <ul>
        {messages?.map((message) => (
          <li key={message._id.toString()}>
            <span>{message.author}:</span>
            <span>{message.body}</span>
            <span>{new Date(message._creationTime).toLocaleTimeString()}</span>
          </li>
        ))}
      </ul>
      <form onSubmit={handleSendMessage}>
        <input
          value={newMessageText}
          onChange={(event) => setNewMessageText(event.target.value)}
          placeholder="Write a message…"
        />
        <input type="submit" value="Send" disabled={!newMessageText} />
      </form>
    </main>
  );
}
```

## File: `starter-templates/convex/styles/globals.css`
```css
/* reset */
* {
  margin: 0;
  padding: 0;
  border: 0;
  line-height: 1.5;
}

body {
  font-family: system-ui, "Segoe UI", Roboto, "Helvetica Neue", helvetica,
    sans-serif;
}

main {
  padding-top: 1em;
  padding-bottom: 1em;
  width: min(800px, 95vw);
  margin: 0 auto;
}

h1 {
  text-align: center;
  margin-bottom: 8px;
  font-size: 1.8em;
  font-weight: 500;
}

.badge {
  text-align: center;
  margin-bottom: 16px;
}
.badge span {
  background-color: #212529;
  color: #ffffff;
  border-radius: 6px;
  font-weight: bold;
  padding: 4px 8px 4px 8px;
  font-size: 0.75em;
}

ul {
  margin: 8px;
  border-radius: 8px;
  border: solid 1px lightgray;
  box-shadow: 0 0.125rem 0.25rem rgba(0, 0, 0, 0.075);
}

ul:empty {
  display: none;
}

li {
  display: flex;
  justify-content: flex-start;
  padding: 8px 16px 8px 16px;
  border-bottom: solid 1px lightgray;
  font-size: 16px;
}

li:last-child {
  border: 0;
}

li span:nth-child(1) {
  font-weight: bold;
  margin-right: 4px;
  white-space: nowrap;
}
li span:nth-child(2) {
  margin-right: 4px;
  word-break: break-word;
}
li span:nth-child(3) {
  color: #6c757d;
  margin-left: auto;
  white-space: nowrap;
}

form {
  display: flex;
  justify-content: center;
}

input:not([type]) {
  padding: 6px 12px 6px 12px;
  color: rgb(33, 37, 41);
  border: solid 1px rgb(206, 212, 218);
  border-radius: 8px;
  font-size: 16px;
}

input[type="submit"],
button {
  margin-left: 4px;
  background: lightblue;
  color: white;
  padding: 6px 12px 6px 12px;
  border-radius: 8px;
  font-size: 16px;
  background-color: rgb(49, 108, 244);
}

input[type="submit"]:hover,
button:hover {
  background-color: rgb(41, 93, 207);
}

input[type="submit"]:disabled,
button:disabled {
  background-color: rgb(122, 160, 248);
}
```

## File: `starter-templates/nextjs/.gitignore`
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
.pnpm-debug.log*

# env files (can opt-in for committing if needed)
.env*

# vercel
.vercel

# typescript
*.tsbuildinfo
next-env.d.ts

# log files
**.log
```

## File: `starter-templates/nextjs/README.md`
```markdown
This is a [Next.js](https://nextjs.org) project bootstrapped with [Codebuff](https://codebuff.com)!

## Get this project

Run the following to clone this starter template:

```bash
codebuff --create nextjs my-app
```

## Getting Started

To get set up, run the development server:

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

## File: `starter-templates/nextjs/codebuff.json`
```json
{
  "description": "Template configuration for this project. See https://www.codebuff.com/config for all options.",
  "startupProcesses": [
    {
      "name": "dev",
      "command": "npm run dev",
      "enabled": true,
      "stdoutFile": "logs/dev.log"
    }
  ],
  "fileChangeHooks": [
    {
      "name": "lint",
      "command": "npm run lint -- --fix",
      "enabled": true
    },
    {
      "name": "typecheck",
      "command": "npm run typecheck",
      "enabled": true
    }
  ]
}
```

## File: `starter-templates/nextjs/eslint.config.mjs`
```
import { dirname } from "path";
import { fileURLToPath } from "url";
import { FlatCompat } from "@eslint/eslintrc";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const compat = new FlatCompat({
  baseDirectory: __dirname,
});

const eslintConfig = [
  ...compat.extends("next/core-web-vitals", "next/typescript"),
];

export default eslintConfig;
```

## File: `starter-templates/nextjs/knowledge.md`
```markdown
Generated by [Codebuff](https://www.npmjs.com/package/codebuff)

# Your project's knowledge

Add any information here or instructions that will help Codebuff maintain your project.

## Verifying changes

After every change, run `npm run checks` to check for any errors that should be fixed.
```

## File: `starter-templates/nextjs/next.config.ts`
```typescript
import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* config options here */
};

export default nextConfig;
```

## File: `starter-templates/nextjs/package.json`
```json
{
  "name": "nextjs",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev --turbopack",
    "build": "next build",
    "start": "next start",
    "lint": "next lint",
    "checks": "tsc --noEmit && npm run lint"
  },
  "dependencies": {
    "react": "^19.0.0",
    "react-dom": "^19.0.0",
    "next": "15.1.5"
  },
  "devDependencies": {
    "typescript": "^5",
    "@types/node": "^20",
    "@types/react": "^19",
    "@types/react-dom": "^19",
    "postcss": "^8",
    "tailwindcss": "^3.4.1",
    "eslint": "^9",
    "eslint-config-next": "15.1.5",
    "@eslint/eslintrc": "^3"
  }
}
```

## File: `starter-templates/nextjs/postcss.config.mjs`
```
/** @type {import('postcss-load-config').Config} */
const config = {
  plugins: {
    tailwindcss: {},
  },
};

export default config;
```

## File: `starter-templates/nextjs/tailwind.config.ts`
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

## File: `starter-templates/nextjs/tsconfig.json`
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

## File: `starter-templates/nextjs/app/globals.css`
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

## File: `starter-templates/nextjs/app/layout.tsx`
```tsx
import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "Create Next App",
  description: "Generated by create next app",
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

## File: `starter-templates/nextjs/app/page.tsx`
```tsx
export default function Home() {
  return (
    <div className="flex min-h-screen flex-col items-center justify-center p-8">
      <h1 className="text-4xl font-bold mb-4">
        <a 
          href="https://www.codebuff.com"
          target="_blank"
          rel="noopener noreferrer"
          className="text-foreground hover:text-blue-500"
        >
          Codebuff
        </a>
        {" + "}
        <a 
          href="https://nextjs.org"
          target="_blank"
          rel="noopener noreferrer"
          className="text-foreground hover:text-blue-500"
        >
          NextJS
        </a>
      </h1>
    </div>
  );
}
```

## File: `starter-templates/node-cli/.gitignore`
```
node_modules/
dist/
.DS_Store
**.log
```

## File: `starter-templates/node-cli/README.md`
```markdown
# Node.js CLI Template

A minimal Node.js CLI application template with TypeScript support.

## Use this template

```bash
# Create a new project using this template
codebuff --create node-cli my-app
```

## Getting Started

```bash
# Install dependencies
npm install

# Run in development mode
npm run dev

# Build for production
npm run build

# Run in production
npm start

# Type check
npm run typecheck
```

## Project Structure
- `src/` - Source files
- `dist/` - Compiled JavaScript files
```

## File: `starter-templates/node-cli/codebuff.json`
```json
{
  "description": "Template configuration for this project. See https://www.codebuff.com/config for all options.",
  "startupProcesses": [
    {
      "name": "dev",
      "command": "npm run dev",
      "enabled": true,
      "stdoutFile": "logs/dev.log"
    }
  ],
  "fileChangeHooks": [
    {
      "name": "typecheck",
      "command": "npm run typecheck",
      "enabled": true
    }
  ]
}
```

## File: `starter-templates/node-cli/knowledge.md`
```markdown
# Node CLI Template Knowledge

## Project Overview
A minimal Node.js CLI application template with TypeScript and modern ES modules.

## Key Features
- Uses `tsx` for development with hot reload
- ES Modules by default (`type: "module"` in package.json)
- Modern Node.js features (ES2022 target)
- Strict TypeScript configuration

## Verifying changes
After every change, run:
```bash
npm run typecheck
```
This will check for type errors.
```

## File: `starter-templates/node-cli/package.json`
```json
{
  "name": "cli",
  "version": "1.0.0",
  "description": "A Node.js CLI application",
  "type": "module",
  "main": "dist/index.js",
  "bin": {
    "cli": "dist/index.js"
  },
  "scripts": {
    "dev": "tsx src/index.ts",
    "build": "tsc",
    "start": "node dist/index.js",
    "typecheck": "tsc --noEmit"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "@types/node": "^20.11.16",
    "tsx": "^4.7.0",
    "typescript": "^5.3.3"
  }
}
```

## File: `starter-templates/node-cli/tsconfig.json`
```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "esModuleInterop": true,
    "strict": true,
    "skipLibCheck": true,
    "outDir": "dist",
    "sourceMap": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

## File: `starter-templates/node-cli/src/index.ts`
```typescript
#!/usr/bin/env node

async function main() {
  console.log('Hello from your CLI app!')
}

main().catch((error) => {
  console.error('Error:', error)
  process.exit(1)
})
```

## File: `starter-templates/python-cli/.gitignore`
```
*$py.class
**.log
*.egg-info/
*.py[cod]
.DS_Store
.env
.python-version
.venv/
__pycache__/
build/
dist/
venv/
```

## File: `starter-templates/python-cli/README.md`
```markdown
# Python CLI Template

A minimal Python CLI application template with modern Python features and type hints.

## Clone this template

```bash
# Create a new project using this template
codebuff --create python-cli my-app
```

## Getting Started

```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

# Install dependencies
pip install -e ".[dev]"

# Run in development mode
python -m cli

# Run type checker
mypy cli

# Build and install
pip install build
python -m build
pip install dist/*.whl
```

## Project Structure

- `cli/` - Source files
- `tests/` - Test files
- `pyproject.toml` - Project configuration
```

## File: `starter-templates/python-cli/codebuff.json`
```json
{
  "description": "Template configuration for this project. See https://www.codebuff.com/config for all options.",
  "startupProcesses": [],
  "fileChangeHooks": [
    {
      "name": "lint",
      "command": "python3 -m flake8 .",
      "enabled": true
    },
    {
      "name": "test",
      "command": "python3 -m unittest discover -s tests",
      "enabled": true
    }
  ]
}
```

## File: `starter-templates/python-cli/knowledge.md`
```markdown
# Python CLI Template Knowledge

## Project Overview

A minimal Python CLI application template with modern Python features and type hints.

## Key Features

- Uses virtual environments for isolation
- Type hints and mypy for static type checking
- Modern Python packaging with pyproject.toml
- Black for code formatting

## Verifying changes

After every change, run:

```bash
mypy cli && black --check cli
```

This will check for type errors and formatting issues.
```

## File: `starter-templates/python-cli/pyproject.toml`
```
[project]
name = "cli"
version = "0.1.0"
description = "A Python CLI application"
requires-python = ">=3.10"
dependencies = []

[project.optional-dependencies]
dev = [
    "black>=25.1.0",
    "mypy>=1.17.1",
    "pytest>=8.4.2",
    "toml>=0.10.2",  # In case someone forgets to run `pip install -e ".[dev]"`
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.black]
line-length = 88
target-version = ['py310']

[tool.mypy]
python_version = "3.10"
strict = true
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
```

## File: `starter-templates/python-cli/cli/__init__.py`
```python
"""A Python CLI application."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("cli")
except PackageNotFoundError:
    # Package not installed, fallback for development
    try:
        import toml  # type: ignore[import-untyped]

        __version__ = toml.load("pyproject.toml")["project"]["version"]
    except Exception:
        __version__ = "unknown"
```

## File: `starter-templates/python-cli/cli/__main__.py`
```python
#!/usr/bin/env python3


def main() -> None:
    print("Hello from your CLI app!")


if __name__ == "__main__":
    main()
```

## File: `starter-templates/remix/.eslintrc.cjs`
```
/**
 * This is intended to be a basic starting point for linting in your app.
 * It relies on recommended configs out of the box for simplicity, but you can
 * and should modify this configuration to best suit your team's needs.
 */

/** @type {import('eslint').Linter.Config} */
module.exports = {
  root: true,
  parserOptions: {
    ecmaVersion: "latest",
    sourceType: "module",
    ecmaFeatures: {
      jsx: true,
    },
  },
  env: {
    browser: true,
    commonjs: true,
    es6: true,
  },
  ignorePatterns: ["!**/.server", "!**/.client"],

  // Base config
  extends: ["eslint:recommended"],

  overrides: [
    // React
    {
      files: ["**/*.{js,jsx,ts,tsx}"],
      plugins: ["react", "jsx-a11y"],
      extends: [
        "plugin:react/recommended",
        "plugin:react/jsx-runtime",
        "plugin:react-hooks/recommended",
        "plugin:jsx-a11y/recommended",
      ],
      settings: {
        react: {
          version: "detect",
        },
        formComponents: ["Form"],
        linkComponents: [
          { name: "Link", linkAttribute: "to" },
          { name: "NavLink", linkAttribute: "to" },
        ],
        "import/resolver": {
          typescript: {},
        },
      },
    },

    // Typescript
    {
      files: ["**/*.{ts,tsx}"],
      plugins: ["@typescript-eslint", "import"],
      parser: "@typescript-eslint/parser",
      settings: {
        "import/internal-regex": "^~/",
        "import/resolver": {
          node: {
            extensions: [".ts", ".tsx"],
          },
          typescript: {
            alwaysTryTypes: true,
          },
        },
      },
      extends: [
        "plugin:@typescript-eslint/recommended",
        "plugin:import/recommended",
        "plugin:import/typescript",
      ],
    },

    // Node
    {
      files: [".eslintrc.cjs"],
      env: {
        node: true,
      },
    },
  ],
};
```

## File: `starter-templates/remix/.gitignore`
```
node_modules

/.cache
/build
.env
**.log
```

## File: `starter-templates/remix/README.md`
```markdown
# Remix Starter Template

A minimal Remix starter template with TypeScript and Tailwind CSS.

## Get this project

Run the following to clone this starter template:

```bash
codebuff --create remix my-app
```

## Quick Start

```bash
npm run dev
```

Visit [http://localhost:3000](http://localhost:3000)

## Development

```bash
# Install dependencies
npm install

# Start dev server
npm run dev

# Type check
npm run typecheck

# Lint
npm run lint

# Build for production
npm run build
```

## Learn More

- [Codebuff Docs](https://www.codebuff.com/docs)
- [Remix Docs](https://remix.run/docs)
- [Tailwind CSS](https://tailwindcss.com)
```

## File: `starter-templates/remix/codebuff.json`
```json
{
  "description": "Template configuration for this project. See https://www.codebuff.com/config for all options.",
  "startupProcesses": [
    {
      "name": "dev",
      "command": "npm run dev",
      "enabled": true,
      "stdoutFile": "logs/dev.log"
    }
  ],
  "fileChangeHooks": [
    {
      "name": "lint",
      "command": "npm run lint -- --fix",
      "enabled": true
    },
    {
      "name": "typecheck",
      "command": "npm run typecheck",
      "enabled": true
    }
  ]
}
```

## File: `starter-templates/remix/knowledge.md`
```markdown
# Remix Template Knowledge

## Project Overview
A minimal Remix + TypeScript starter template with Tailwind CSS for styling.

## Verifying changes
After every change, run:
```bash
npm run typecheck && npm run lint
```
This will check for type errors and lint issues.
```

## File: `starter-templates/remix/package.json`
```json
{
  "name": "remix",
  "private": true,
  "sideEffects": false,
  "type": "module",
  "scripts": {
    "build": "remix vite:build",
    "dev": "remix vite:dev",
    "lint": "eslint --ignore-path .gitignore --cache --cache-location ./node_modules/.cache/eslint .",
    "start": "remix-serve ./build/server/index.js",
    "typecheck": "tsc"
  },
  "dependencies": {
    "@remix-run/node": "^2.15.2",
    "@remix-run/react": "^2.15.2",
    "@remix-run/serve": "^2.15.2",
    "isbot": "^4.1.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "devDependencies": {
    "@remix-run/dev": "^2.15.2",
    "@types/react": "^18.2.20",
    "@types/react-dom": "^18.2.7",
    "@typescript-eslint/eslint-plugin": "^6.7.4",
    "@typescript-eslint/parser": "^6.7.4",
    "autoprefixer": "^10.4.19",
    "eslint": "^8.38.0",
    "eslint-import-resolver-typescript": "^3.6.1",
    "eslint-plugin-import": "^2.28.1",
    "eslint-plugin-jsx-a11y": "^6.7.1",
    "eslint-plugin-react": "^7.33.2",
    "eslint-plugin-react-hooks": "^4.6.0",
    "postcss": "^8.4.38",
    "tailwindcss": "^3.4.4",
    "typescript": "~5.3.3",
    "vite": "^5.1.0",
    "vite-tsconfig-paths": "^4.2.1"
  },
  "engines": {
    "node": ">=20.0.0"
  }
}
```

## File: `starter-templates/remix/postcss.config.js`
```javascript
export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
};
```

## File: `starter-templates/remix/tailwind.config.ts`
```typescript
import type { Config } from "tailwindcss";

export default {
  content: ["./app/**/{**,.client,.server}/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      fontFamily: {
        sans: [
          "Inter",
          "ui-sans-serif",
          "system-ui",
          "sans-serif",
          "Apple Color Emoji",
          "Segoe UI Emoji",
          "Segoe UI Symbol",
          "Noto Color Emoji",
        ],
      },
    },
  },
  plugins: [],
} satisfies Config;
```

## File: `starter-templates/remix/tsconfig.json`
```json
{
  "include": [
    "**/*.ts",
    "**/*.tsx",
    "**/.server/**/*.ts",
    "**/.server/**/*.tsx",
    "**/.client/**/*.ts",
    "**/.client/**/*.tsx"
  ],
  "compilerOptions": {
    "lib": ["DOM", "DOM.Iterable", "ES2022"],
    "types": ["@remix-run/node", "vite/client"],
    "isolatedModules": true,
    "esModuleInterop": true,
    "jsx": "react-jsx",
    "module": "ESNext",
    "moduleResolution": "Bundler",
    "resolveJsonModule": true,
    "target": "ES2022",
    "strict": true,
    "allowJs": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "baseUrl": ".",
    "paths": {
      "~/*": ["./app/*"]
    },

    // Vite takes care of building everything, not tsc.
    "noEmit": true
  }
}
```

## File: `starter-templates/remix/vite.config.ts`
```typescript
import { vitePlugin as remix } from "@remix-run/dev";
import { defineConfig } from "vite";
import tsconfigPaths from "vite-tsconfig-paths";

declare module "@remix-run/node" {
  interface Future {
    v3_singleFetch: true;
  }
}

export default defineConfig({
  plugins: [
    remix({
      future: {
        v3_fetcherPersist: true,
        v3_relativeSplatPath: true,
        v3_throwAbortReason: true,
        v3_singleFetch: true,
        v3_lazyRouteDiscovery: true,
      },
    }),
    tsconfigPaths(),
  ],
});
```

## File: `starter-templates/remix/app/entry.client.tsx`
```tsx
/**
 * By default, Remix will handle hydrating your app on the client for you.
 * You are free to delete this file if you'd like to, but if you ever want it revealed again, you can run `npx remix reveal` ✨
 * For more information, see https://remix.run/file-conventions/entry.client
 */

import { RemixBrowser } from "@remix-run/react";
import { startTransition, StrictMode } from "react";
import { hydrateRoot } from "react-dom/client";

startTransition(() => {
  hydrateRoot(
    document,
    <StrictMode>
      <RemixBrowser />
    </StrictMode>
  );
});
```

## File: `starter-templates/remix/app/entry.server.tsx`
```tsx
/**
 * By default, Remix will handle generating the HTTP Response for you.
 * You are free to delete this file if you'd like to, but if you ever want it revealed again, you can run `npx remix reveal` ✨
 * For more information, see https://remix.run/file-conventions/entry.server
 */

import { PassThrough } from "node:stream";

import type { AppLoadContext, EntryContext } from "@remix-run/node";
import { createReadableStreamFromReadable } from "@remix-run/node";
import { RemixServer } from "@remix-run/react";
import { isbot } from "isbot";
import { renderToPipeableStream } from "react-dom/server";

const ABORT_DELAY = 5_000;

export default function handleRequest(
  request: Request,
  responseStatusCode: number,
  responseHeaders: Headers,
  remixContext: EntryContext,
  // This is ignored so we can keep it in the template for visibility.  Feel
  // free to delete this parameter in your app if you're not using it!
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  loadContext: AppLoadContext
) {
  return isbot(request.headers.get("user-agent") || "")
    ? handleBotRequest(
        request,
        responseStatusCode,
        responseHeaders,
        remixContext
      )
    : handleBrowserRequest(
        request,
        responseStatusCode,
        responseHeaders,
        remixContext
      );
}

function handleBotRequest(
  request: Request,
  responseStatusCode: number,
  responseHeaders: Headers,
  remixContext: EntryContext
) {
  return new Promise((resolve, reject) => {
    let shellRendered = false;
    const { pipe, abort } = renderToPipeableStream(
      <RemixServer
        context={remixContext}
        url={request.url}
        abortDelay={ABORT_DELAY}
      />,
      {
        onAllReady() {
          shellRendered = true;
          const body = new PassThrough();
          const stream = createReadableStreamFromReadable(body);

          responseHeaders.set("Content-Type", "text/html");

          resolve(
            new Response(stream, {
              headers: responseHeaders,
              status: responseStatusCode,
            })
          );

          pipe(body);
        },
        onShellError(error: unknown) {
          reject(error);
        },
        onError(error: unknown) {
          responseStatusCode = 500;
          // Log streaming rendering errors from inside the shell.  Don't log
          // errors encountered during initial shell rendering since they'll
          // reject and get logged in handleDocumentRequest.
          if (shellRendered) {
            console.error(error);
          }
        },
      }
    );

    setTimeout(abort, ABORT_DELAY);
  });
}

function handleBrowserRequest(
  request: Request,
  responseStatusCode: number,
  responseHeaders: Headers,
  remixContext: EntryContext
) {
  return new Promise((resolve, reject) => {
    let shellRendered = false;
    const { pipe, abort } = renderToPipeableStream(
      <RemixServer
        context={remixContext}
        url={request.url}
        abortDelay={ABORT_DELAY}
      />,
      {
        onShellReady() {
          shellRendered = true;
          const body = new PassThrough();
          const stream = createReadableStreamFromReadable(body);

          responseHeaders.set("Content-Type", "text/html");

          resolve(
            new Response(stream, {
              headers: responseHeaders,
              status: responseStatusCode,
            })
          );

          pipe(body);
        },
        onShellError(error: unknown) {
          reject(error);
        },
        onError(error: unknown) {
          responseStatusCode = 500;
          // Log streaming rendering errors from inside the shell.  Don't log
          // errors encountered during initial shell rendering since they'll
          // reject and get logged in handleDocumentRequest.
          if (shellRendered) {
            console.error(error);
          }
        },
      }
    );

    setTimeout(abort, ABORT_DELAY);
  });
}
```

## File: `starter-templates/remix/app/root.tsx`
```tsx
import {
  Links,
  Meta,
  Outlet,
  Scripts,
  ScrollRestoration,
} from "@remix-run/react";
import type { LinksFunction } from "@remix-run/node";

import "./tailwind.css";

export const links: LinksFunction = () => [
  { rel: "preconnect", href: "https://fonts.googleapis.com" },
  {
    rel: "preconnect",
    href: "https://fonts.gstatic.com",
    crossOrigin: "anonymous",
  },
  {
    rel: "stylesheet",
    href: "https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap",
  },
];

export function Layout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <head>
        <meta charSet="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <Meta />
        <Links />
      </head>
      <body>
        {children}
        <ScrollRestoration />
        <Scripts />
      </body>
    </html>
  );
}

export default function App() {
  return <Outlet />;
}
```

## File: `starter-templates/remix/app/tailwind.css`
```css
@tailwind base;
@tailwind components;
@tailwind utilities;

html,
body {
  @apply bg-white dark:bg-gray-950;

  @media (prefers-color-scheme: dark) {
    color-scheme: dark;
  }
}
```

## File: `starter-templates/remix/app/routes/_index.tsx`
```tsx
import type { MetaFunction } from "@remix-run/node";

export const meta: MetaFunction = () => {
  return [
    { title: "New Remix App" },
    { name: "description", content: "Welcome to Remix!" },
  ];
};

export default function Index() {
  return (
    <div className="flex h-screen items-center justify-center">
      <div className="flex flex-col items-center gap-16">
        <header className="flex flex-col items-center gap-9">
          <h1 className="leading text-2xl font-bold text-gray-800 dark:text-gray-100">
            Welcome to <span className="sr-only">Remix</span>
          </h1>
          <div className="h-[144px] w-[434px]">
            <img
              src="/logo-light.png"
              alt="Remix"
              className="block w-full dark:hidden"
            />
            <img
              src="/logo-dark.png"
              alt="Remix"
              className="hidden w-full dark:block"
            />
          </div>
        </header>
        <nav className="flex flex-col items-center justify-center gap-4 rounded-3xl border border-gray-200 p-6 dark:border-gray-700">
          <p className="leading-6 text-gray-700 dark:text-gray-200">
            What&apos;s next?
          </p>
          <ul>
            {resources.map(({ href, text, icon }) => (
              <li key={href}>
                <a
                  className="group flex items-center gap-3 self-stretch p-3 leading-normal text-blue-700 hover:underline dark:text-blue-500"
                  href={href}
                  target="_blank"
                  rel="noreferrer"
                >
                  {icon}
                  {text}
                </a>
              </li>
            ))}
          </ul>
        </nav>
      </div>
    </div>
  );
}

const resources = [
  {
    href: "https://remix.run/start/quickstart",
    text: "Quick Start (5 min)",
    icon: (
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="24"
        height="20"
        viewBox="0 0 20 20"
        fill="none"
        className="stroke-gray-600 group-hover:stroke-current dark:stroke-gray-300"
      >
        <path
          d="M8.51851 12.0741L7.92592 18L15.6296 9.7037L11.4815 7.33333L12.0741 2L4.37036 10.2963L8.51851 12.0741Z"
          strokeWidth="1.5"
          strokeLinecap="round"
          strokeLinejoin="round"
        />
      </svg>
    ),
  },
  {
    href: "https://remix.run/start/tutorial",
    text: "Tutorial (30 min)",
    icon: (
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="24"
        height="20"
        viewBox="0 0 20 20"
        fill="none"
        className="stroke-gray-600 group-hover:stroke-current dark:stroke-gray-300"
      >
        <path
          d="M4.561 12.749L3.15503 14.1549M3.00811 8.99944H1.01978M3.15503 3.84489L4.561 5.2508M8.3107 1.70923L8.3107 3.69749M13.4655 3.84489L12.0595 5.2508M18.1868 17.0974L16.635 18.6491C16.4636 18.8205 16.1858 18.8205 16.0144 18.6491L13.568 16.2028C13.383 16.0178 13.0784 16.0347 12.915 16.239L11.2697 18.2956C11.047 18.5739 10.6029 18.4847 10.505 18.142L7.85215 8.85711C7.75756 8.52603 8.06365 8.21994 8.39472 8.31453L17.6796 10.9673C18.0223 11.0653 18.1115 11.5094 17.8332 11.7321L15.7766 13.3773C15.5723 13.5408 15.5554 13.8454 15.7404 14.0304L18.1868 16.4767C18.3582 16.6481 18.3582 16.926 18.1868 17.0974Z"
          strokeWidth="1.5"
          strokeLinecap="round"
          strokeLinejoin="round"
        />
      </svg>
    ),
  },
  {
    href: "https://remix.run/docs",
    text: "Remix Docs",
    icon: (
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="24"
        height="20"
        viewBox="0 0 20 20"
        fill="none"
        className="stroke-gray-600 group-hover:stroke-current dark:stroke-gray-300"
      >
        <path
          d="M9.99981 10.0751V9.99992M17.4688 17.4688C15.889 19.0485 11.2645 16.9853 7.13958 12.8604C3.01467 8.73546 0.951405 4.11091 2.53116 2.53116C4.11091 0.951405 8.73546 3.01467 12.8604 7.13958C16.9853 11.2645 19.0485 15.889 17.4688 17.4688ZM2.53132 17.4688C0.951566 15.8891 3.01483 11.2645 7.13974 7.13963C11.2647 3.01471 15.8892 0.951453 17.469 2.53121C19.0487 4.11096 16.9854 8.73551 12.8605 12.8604C8.73562 16.9853 4.11107 19.0486 2.53132 17.4688Z"
          strokeWidth="1.5"
          strokeLinecap="round"
        />
      </svg>
    ),
  },
  {
    href: "https://rmx.as/discord",
    text: "Join Discord",
    icon: (
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="24"
        height="20"
        viewBox="0 0 24 20"
        fill="none"
        className="stroke-gray-600 group-hover:stroke-current dark:stroke-gray-300"
      >
        <path
          d="M15.0686 1.25995L14.5477 1.17423L14.2913 1.63578C14.1754 1.84439 14.0545 2.08275 13.9422 2.31963C12.6461 2.16488 11.3406 2.16505 10.0445 2.32014C9.92822 2.08178 9.80478 1.84975 9.67412 1.62413L9.41449 1.17584L8.90333 1.25995C7.33547 1.51794 5.80717 1.99419 4.37748 2.66939L4.19 2.75793L4.07461 2.93019C1.23864 7.16437 0.46302 11.3053 0.838165 15.3924L0.868838 15.7266L1.13844 15.9264C2.81818 17.1714 4.68053 18.1233 6.68582 18.719L7.18892 18.8684L7.50166 18.4469C7.96179 17.8268 8.36504 17.1824 8.709 16.4944L8.71099 16.4904C10.8645 17.0471 13.128 17.0485 15.2821 16.4947C15.6261 17.1826 16.0293 17.8269 16.4892 18.4469L16.805 18.8725L17.3116 18.717C19.3056 18.105 21.1876 17.1751 22.8559 15.9238L23.1224 15.724L23.1528 15.3923C23.5873 10.6524 22.3579 6.53306 19.8947 2.90714L19.7759 2.73227L19.5833 2.64518C18.1437 1.99439 16.6386 1.51826 15.0686 1.25995ZM16.6074 10.7755L16.6074 10.7756C16.5934 11.6409 16.0212 12.1444 15.4783 12.1444C14.9297 12.1444 14.3493 11.6173 14.3493 10.7877C14.3493 9.94885 14.9378 9.41192 15.4783 9.41192C16.0471 9.41192 16.6209 9.93851 16.6074 10.7755ZM8.49373 12.1444C7.94513 12.1444 7.36471 11.6173 7.36471 10.7877C7.36471 9.94885 7.95323 9.41192 8.49373 9.41192C9.06038 9.41192 9.63892 9.93712 9.6417 10.7815C9.62517 11.6239 9.05462 12.1444 8.49373 12.1444Z"
          strokeWidth="1.5"
        />
      </svg>
    ),
  },
];
```

## File: `starter-templates/vite/.gitignore`
```
# Logs
logs
**.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*
lerna-debug.log*

node_modules
dist
dist-ssr
*.local

# Editor directories and files
.vscode/*
!.vscode/extensions.json
.idea
.DS_Store
*.suo
*.ntvs*
*.njsproj
*.sln
*.sw?
```

## File: `starter-templates/vite/README.md`
```markdown
# Vite + React Template

A minimal React + TypeScript starter template using [Vite](https://vitejs.dev/) for fast development and building.

## Getting Started

```bash
codebuff --create vite my-app

# In another terminal window:
npm run dev
```

## Available Scripts
- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run lint` - Run ESLint
- `npm run preview` - Preview production build locally

## Learn More
- [Vite Documentation](https://vitejs.dev/)
- [React Documentation](https://react.dev/)
```

## File: `starter-templates/vite/codebuff.json`
```json
{
  "description": "Template configuration for this project. See https://www.codebuff.com/config for all options.",
  "startupProcesses": [
    {
      "name": "dev",
      "command": "npm run dev",
      "enabled": true,
      "stdoutFile": "logs/dev.log"
    }
  ],
  "fileChangeHooks": [
    {
      "name": "lint",
      "command": "npm run lint -- --fix",
      "enabled": true
    },
    {
      "name": "typecheck",
      "command": "npm run typecheck",
      "enabled": true
    }
  ]
}
```

## File: `starter-templates/vite/eslint.config.js`
```javascript
import js from '@eslint/js'
import globals from 'globals'
import reactHooks from 'eslint-plugin-react-hooks'
import reactRefresh from 'eslint-plugin-react-refresh'
import tseslint from 'typescript-eslint'

export default tseslint.config(
  { ignores: ['dist'] },
  {
    extends: [js.configs.recommended, ...tseslint.configs.recommended],
    files: ['**/*.{ts,tsx}'],
    languageOptions: {
      ecmaVersion: 2020,
      globals: globals.browser,
    },
    plugins: {
      'react-hooks': reactHooks,
      'react-refresh': reactRefresh,
    },
    rules: {
      ...reactHooks.configs.recommended.rules,
      'react-refresh/only-export-components': [
        'warn',
        { allowConstantExport: true },
      ],
    },
  },
)
```

## File: `starter-templates/vite/index.html`
```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Vite + React + TS</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
```

## File: `starter-templates/vite/knowledge.md`
```markdown
# Vite + React Template Knowledge

## Project Overview
A minimal React + TypeScript starter template using Vite for fast development and building.

## Verifying changes
After every change, run:
```bash
npm run lint && npm run typecheck
```
This will check for lint issues and type errors.

```

## File: `starter-templates/vite/package.json`
```json
{
  "name": "vite",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc -b && vite build",
    "lint": "eslint .",
    "preview": "vite preview",
    "typecheck": "tsc -b"
  },
  "dependencies": {
    "react": "^18.3.1",
    "react-dom": "^18.3.1"
  },
  "devDependencies": {
    "@eslint/js": "^9.17.0",
    "@types/react": "^18.3.18",
    "@types/react-dom": "^18.3.5",
    "@vitejs/plugin-react": "^4.3.4",
    "eslint": "^9.17.0",
    "eslint-plugin-react-hooks": "^5.0.0",
    "eslint-plugin-react-refresh": "^0.4.16",
    "globals": "^15.14.0",
    "typescript": "~5.6.2",
    "typescript-eslint": "^8.18.2",
    "vite": "^6.0.5"
  }
}
```

## File: `starter-templates/vite/tsconfig.app.json`
```json
{
  "compilerOptions": {
    "tsBuildInfoFile": "./node_modules/.tmp/tsconfig.app.tsbuildinfo",
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,
    "incremental": true,

    /* Bundler mode */
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "isolatedModules": true,
    "moduleDetection": "force",
    "noEmit": true,
    "jsx": "react-jsx",

    /* Linting */
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true,
  },
  "include": ["src"]
}
```

## File: `starter-templates/vite/tsconfig.json`
```json
{
  "files": [],
  "references": [
    { "path": "./tsconfig.app.json" },
    { "path": "./tsconfig.node.json" }
  ]
}
```

## File: `starter-templates/vite/tsconfig.node.json`
```json
{
  "compilerOptions": {
    "tsBuildInfoFile": "./node_modules/.tmp/tsconfig.node.tsbuildinfo",
    "target": "ES2022",
    "lib": ["ES2023"],
    "module": "ESNext",
    "skipLibCheck": true,
    "incremental": true,

    /* Bundler mode */
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "isolatedModules": true,
    "moduleDetection": "force",
    "noEmit": true,

    /* Linting */
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true,
  },
  "include": ["vite.config.ts"]
}
```

## File: `starter-templates/vite/vite.config.ts`
```typescript
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
})
```

## File: `starter-templates/vite/src/App.css`
```css
#root {
  max-width: 1280px;
  margin: 0 auto;
  padding: 2rem;
  text-align: center;
}

.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.react:hover {
  filter: drop-shadow(0 0 2em #61dafbaa);
}

@keyframes logo-spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

@media (prefers-reduced-motion: no-preference) {
  a:nth-of-type(2) .logo {
    animation: logo-spin infinite 20s linear;
  }
}

.card {
  padding: 2em;
}

.read-the-docs {
  color: #888;
}
```

## File: `starter-templates/vite/src/App.tsx`
```tsx
import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Codebuff + Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
```

## File: `starter-templates/vite/src/index.css`
```css
:root {
  font-family: Inter, system-ui, Avenir, Helvetica, Arial, sans-serif;
  line-height: 1.5;
  font-weight: 400;

  color-scheme: light dark;
  color: rgba(255, 255, 255, 0.87);
  background-color: #242424;

  font-synthesis: none;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

a {
  font-weight: 500;
  color: #646cff;
  text-decoration: inherit;
}
a:hover {
  color: #535bf2;
}

body {
  margin: 0;
  display: flex;
  place-items: center;
  min-width: 320px;
  min-height: 100vh;
}

h1 {
  font-size: 3.2em;
  line-height: 1.1;
}

button {
  border-radius: 8px;
  border: 1px solid transparent;
  padding: 0.6em 1.2em;
  font-size: 1em;
  font-weight: 500;
  font-family: inherit;
  background-color: #1a1a1a;
  cursor: pointer;
  transition: border-color 0.25s;
}
button:hover {
  border-color: #646cff;
}
button:focus,
button:focus-visible {
  outline: 4px auto -webkit-focus-ring-color;
}

@media (prefers-color-scheme: light) {
  :root {
    color: #213547;
    background-color: #ffffff;
  }
  a:hover {
    color: #747bff;
  }
  button {
    background-color: #f9f9f9;
  }
}
```

## File: `starter-templates/vite/src/main.tsx`
```tsx
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
```

## File: `starter-templates/vite/src/vite-env.d.ts`
```typescript
/// <reference types="vite/client" />
```

## File: `utils/docker/Dockerfile`
```
FROM node:20-slim

# Install required packages
RUN apt-get update && \
    apt-get install -y \
    git \
    python3 \
    make \
    g++ \
    procps \
    inotify-tools \
    npm \
    build-essential \
    bsdutils \
    expect \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install/Update codebuff globally and verify installation
RUN npm install -g codebuff

# Copy scripts
COPY codebuff-wrapper.sh /codebuff-wrapper.sh
COPY entrypoint.sh /entrypoint.sh
COPY message-bridge.sh /message-bridge.sh

# Make scripts executable
RUN chmod +x /codebuff-wrapper.sh /entrypoint.sh /message-bridge.sh

# Set entrypoint
ENTRYPOINT ["/entrypoint.sh"]
```

## File: `utils/docker/README.md`
```markdown
# Codebuff Docker Container

This Docker container provides a standardized environment for running codebuff on any local project directory. It handles native dependencies and provides consistent behavior across different host systems.

## Quick Start

From the project root directory:

```bash
./utils/docker/start-codebuff.sh [optional-project-path]
```

This script will:

1. Check if Docker is installed
2. Build the Docker image if needed
3. Set up communication channels between host and container
4. Mount your project directory and credentials
5. Start codebuff in an isolated environment

## Architecture

The system consists of several key components:

### 1. Container Setup (`Dockerfile`)
- Based on node:20-slim for minimal size
- Includes essential build tools and dependencies
- Pre-installs codebuff globally
- Sets up communication scripts

### 2. Entry Point (`entrypoint.sh`)
- Validates environment variables and paths
- Creates communication directory structure
- Sets up working directory with project files
- Handles npm dependencies
- Copies credentials from host
- Launches the codebuff wrapper

### 3. Communication Bridge
The system uses a bidirectional communication system between host and container:

- `message-bridge.sh`: Handles host-side communication
- `codebuff-wrapper.sh`: Manages container-side interaction using expect
- Communication files:
  - `messages.txt`: Commands from host to container
  - `responses.txt`: Output from container to host

### 4. Project Management
- Creates isolated workspace in container
- Preserves original files in mounted volume
- Supports npm package installation
- Handles credentials via ~/.config/manicode mount

## Usage

### Basic Usage
```bash
./utils/docker/start-codebuff.sh
```

When prompted, enter your project path or press Enter to use current directory.

### Advanced Usage
```bash
./utils/docker/start-codebuff.sh /path/to/your/project
```

### Environment Variables
- `DEBUG`: Set to true for verbose logging and automatic container cleanup
- `PROJECT_PATH`: Project directory name (set automatically)
- `PROJECT_NAME`: Project name for prompt (set automatically)

## Directory Structure

The container expects this structure:

```
/workspace/           # Mount point for host directory
  └── your-project/  # Your project files
      └── .codebuff/ # Communication directory
          └── comm/  # Contains messages.txt and responses.txt
```

## Troubleshooting

### Common Issues

1. **Permission Errors**
   - Ensure write permissions on project directory
   - Check if .codebuff/comm directory exists and is writable
   - Verify Docker has necessary permissions

2. **Communication Issues**
   - Check if comm files exist and are writable
   - Verify container is running (`docker ps`)
   - Check container logs (`docker logs <container-id>`)

3. **Path Issues**
   - Use absolute paths when possible
   - Verify project directory exists
   - Check for proper directory structure

### Windows Users
- Use appropriate path format:
  - Git Bash: `/c/Users/YourName/projects`
  - PowerShell: `C:/Users/YourName/projects`
  - WSL: Use native Linux paths

## Security Notes

- Container runs with limited privileges
- Credentials are mounted read-only
- Project files are copied to isolated workspace
- Communication channels are local to project directory

## Development

To modify the container:

1. Update Dockerfile if adding dependencies
2. Modify communication scripts as needed
3. Test with DEBUG=true for verbose logging
4. Rebuild image after changes

## Technical Details

- Uses expect for reliable terminal interaction
- Implements file-based communication protocol
- Supports credential persistence
- Handles npm package management
- Provides isolated workspace per session
```

## File: `utils/docker/codebuff-wrapper.sh`
```bash
#!/usr/bin/expect -f

# Version 1.0.1 - Testing build update
# Log to stderr
proc log {msg} {
    puts stderr "\[WRAPPER\] \[$msg\]"
}

proc debug {msg} {
    puts stderr "\[WRAPPER DEBUG\] \[$msg\]"
}

proc strip_ansi {text} {
    # Strip ANSI escape sequences
    regsub -all {\x1b\[[0-9;]*[mGJK]} $text {} text
    return $text
}

proc write_response {line} {
    if {![info exists ::env(PROJECT_PATH)]} {
        log "ERROR: PROJECT_PATH environment variable not set"
        exit 1
    }

    set project_path $::env(PROJECT_PATH)
    set comm_dir "/workspace/$project_path/.codebuff/comm"
    debug "Writing response to $comm_dir/responses.txt: $line"
    if [catch {
        set f [open "$comm_dir/responses.txt" "a"]
        puts $f $line
        close $f
        debug "Successfully wrote response"
    } err] {
        log "Error writing response: $err"
    }
}

log "Starting codebuff wrapper..."

# Verify required environment variables
if {![info exists ::env(PROJECT_PATH)]} {
    log "ERROR: PROJECT_PATH environment variable not set"
    exit 1
}
if {![info exists ::env(PROJECT_NAME)]} {
    log "ERROR: PROJECT_NAME environment variable not set"
    exit 1
}

set project_name $::env(PROJECT_NAME)
set project_path $::env(PROJECT_PATH)
debug "Project name: $project_name"
debug "Project path: $project_path"
debug "Comm dir: /workspace/$project_path/.codebuff/comm"

# Always enable debugging
exp_internal 1
log_user 1

# Signal ready before starting codebuff
write_response "CONTAINER READY"

# Start codebuff
spawn codebuff
debug "Spawned codebuff process"

# Monitor messages.txt and send input
set timeout -1
while {1} {
    set messages_file "/workspace/$project_path/.codebuff/comm/messages.txt"
    debug "Checking messages file: $messages_file"

    if {[file exists $messages_file]} {
        debug "Found messages.txt file"
        # Wait for a modification event
        debug "Running inotifywait on $messages_file"
        set result [catch {exec inotifywait -q -e modify $messages_file} err]
        if {$result != 0} {
            debug "inotifywait error: $err"
            sleep 0.1
            continue
        }
        debug "Got inotifywait event"

        if [catch {
            set f [open $messages_file r]
            set message [read $f]
            close $f
            debug "Read message content: '$message'"

            if {$message != ""} {
                debug "Sending message to codebuff"
                send "$message"
                sleep 1
                send "\r"
                debug "Message sent"

                # Clear the message file after sending
                debug "Clearing message file..."
                if [catch {
                    set f [open $messages_file w]
                    close $f
                    debug "Message file cleared"
                } err] {
                    log "Error clearing message file: $err"
                }
            } else {
                debug "Message was empty"
            }
        } err] {
            log "Error processing message: $err"
        }
    } else {
        debug "Messages file does not exist"
    }

    # Check for output from codebuff
    expect {
        -re "(.+)\r\n" {
            debug "Got output: $expect_out(1,string)"
            write_response $expect_out(1,string)
            exp_continue
        }
        "$project_name > " {
            debug "Got prompt"
            write_response "$project_name > "
        }
        timeout {
            # No output, continue checking messages
        }
    }

    sleep 0.1
}
```

## File: `utils/docker/entrypoint.sh`
```bash
#!/bin/bash

# Enable error handling
set -e

# Always enable command printing for debugging
set -x

# Add timestamp to logs
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*"
}

debug() {
    log "DEBUG: $*"
}

error() {
    log "ERROR: $*"
    exit 1
}

# Check if a project path was provided
if [ -z "$PROJECT_PATH" ]; then
    error "PROJECT_PATH environment variable is required"
fi

# Strip any leading slashes from PROJECT_PATH to make it relative
RELATIVE_PATH="${PROJECT_PATH#/}"

# Set up communication directory
COMM_DIR="/workspace/$RELATIVE_PATH/.codebuff/comm"
debug "Setting up comm directory at: $COMM_DIR"
mkdir -p "$COMM_DIR" || error "Failed to create $COMM_DIR directory"
chmod 777 "$COMM_DIR" || error "Failed to set permissions on $COMM_DIR"

# Create communication files with proper permissions
touch "$COMM_DIR/messages.txt" "$COMM_DIR/responses.txt" || error "Failed to create communication files"
chmod 666 "$COMM_DIR/messages.txt" "$COMM_DIR/responses.txt" || error "Failed to set permissions on communication files"

# Create a working directory for this session
WORK_DIR="/tmp/codebuff_workspace/$RELATIVE_PATH"
mkdir -p "$WORK_DIR" || error "Failed to create working directory"

# Copy project files to working directory with error handling
debug "Copying project files to working directory..."
cd "/workspace/$RELATIVE_PATH" || error "Failed to change to source directory"

# Copy files individually
for file in .gitignore README.md eslint.config.js index.html knowledge.md package.json pnpm-lock.yaml tsconfig.app.json tsconfig.json tsconfig.node.json vite.config.ts; do
    if [ -f "$file" ]; then
        debug "Copying file: $file"
        cp "$file" "$WORK_DIR/" || log "Failed to copy $file"
    fi
done

# Copy directories individually
for dir in public src; do
    if [ -d "$dir" ]; then
        debug "Copying directory: $dir"
        cp -r "$dir" "$WORK_DIR/" || log "Failed to copy $dir"
    fi
done

# Change to the working directory
cd "$WORK_DIR" || error "Failed to change to working directory"

# Install dependencies if package.json exists
if [ -f "package.json" ]; then
    debug "Setting up npm..."
    source /root/.bashrc
    log "Installing dependencies..."
    npm install --silent || error "Failed to install dependencies"
fi

# Set up credentials directory in container's home directory
CREDS_DIR="$HOME/.config/manicode"
mkdir -p "$CREDS_DIR" || error "Failed to create credentials directory"
if [ -f "/workspace/.config/manicode/credentials.json" ]; then
    if ! cp "/workspace/.config/manicode/credentials.json" "$CREDS_DIR/credentials.json"; then
        debug "Warning: Failed to copy credentials file, continuing without credentials"
    else
        debug "Credentials copied from host to container's home directory"
    fi
fi

# Verify codebuff is available and in PATH
PATH="/usr/local/bin:$PATH"
export PATH

which codebuff || error "codebuff command not found in PATH"
debug "Found codebuff at: $(which codebuff)"

# Start codebuff wrapper
log "Starting codebuff with communication layer..."
exec /codebuff-wrapper.sh
```

## File: `utils/docker/knowledge.md`
```markdown
# Codebuff Docker Container Knowledge

## Docker Image Distribution
- Build images locally rather than distributing via registry
- Benefits:
  - Self-contained, no external dependencies
  - Users can inspect/modify Dockerfile
  - Works offline after first build
  - Automatically stays in sync with code
  - No registry maintenance needed

## Communication Protocol
- Uses `.codebuff/comm` directory in project root
- Files:
  - `messages.txt`: Commands from host to container
  - `responses.txt`: Container output and status
- Permissions: 666 to allow container read/write

## Container Lifecycle
- Build image if:
  1. Image doesn't exist
  2. Dockerfile modified since last build
- Container starts with:
  1. Project directory mount
  2. Credentials mount
  3. Communication directory mount
- Waits for "CONTAINER READY" signal before proceeding

## Container Setup
- Base image: node:20-slim
- Additional packages: git, python3, make, g++, procps
- Working directory: /workspace
- Project files copied to /tmp/codebuff_workspace/[PROJECT_PATH]
- Container must run with --privileged flag for filesystem access

## Communication System
Two approaches available:
1. Named Pipes (FIFO)
   - More traditional but can be tricky with blocking
   - Requires careful handling of read/write operations
   - Better for streaming data

2. File-Based (Current Implementation)
   - More reliable for debugging
   - Uses messages.txt for host→container
   - Uses responses.txt for container→host
   - Monitor file size changes to detect new messages
   - Keep only latest message by overwriting instead of appending
   - Use inotifywait for efficient file change detection when available
   - Fall back to modification time polling if inotifywait not available
   - Append-only operation (>>) for atomic writes
   - Set 666 permissions on shared files

### Test Scripts
- test-comm.sh: Continuous bidirectional testing
- message-bridge.sh: Interactive messaging interface
- test-message.sh: Single message testing utility

## Named Pipe Communication
When using named pipes (FIFOs) for bidirectional communication:
- Create pipes before starting communication
- Handle pipe reads/writes in background to avoid blocking
- Use traps to clean up background processes
- Keep pipe operations simple and robust
- Prefer background writes with & to avoid blocking
- Use sleep between operations to prevent busy waiting
- Set appropriate permissions (666) for pipes
- Clean up pipes on exit
- Docker mounts preserve pipe functionality across container boundary
- Pipe redirection must happen inside container context when using docker exec
- Test pipe communication manually before running complex scripts

## File-Based Communication
For reliable container communication:
- Use regular files instead of pipes for simpler debugging
- Keep only latest message by overwriting instead of appending
- Use inotifywait for efficient file change detection when available
- Fall back to modification time polling if inotifywait not available
- Set 666 permissions on shared files
- Mount comm directory separately from workspace

## Best Practices
- Always use exec in entrypoint.sh to replace shell process
- Log extensively during development
- Test communication before adding application logic
- Clean up resources on container exit
- Use separate volume mounts for code vs communication
- Label all logs with source (HOST/CONTAINER) and timestamp
- Use background writes to avoid blocking
- Monitor file sizes for changes instead of continuous reads
- Keep communication files outside of project directory (in comm/)

## Container Best Practices

- Use node:slim as base to minimize image size
- Clean up package manager cache after installing deps
- Set WORKDIR before COPY/RUN commands that use it
- Make entrypoint scripts executable in Dockerfile
- Never write to mounted volumes - copy to working directory instead
- Keep image names simple and context-aware
- Avoid redundant suffixes like '-docker' in image names
- Use descriptive but concise container and image names
- Order RUN commands by stability:
  - System packages first (apt-get)
  - Build tools second (python, make, g++)
  - npm installs last
- This ordering maximizes Docker layer cache hits
- Cache apt-get lists cleanup in same RUN layer as install

## Path Handling

When mounting directories in Docker:
- Always use relative paths inside container
- Strip leading slashes from paths before concatenating
- Convert host paths to absolute before mounting
- When user provides absolute path, make it relative to mount point
- Handle both relative and absolute paths in bootstrap scripts
- Verify project paths are within mounted directory
- Clean up paths by removing double slashes and trailing slashes
- Add debug output in entrypoint scripts for path diagnostics
- Handle special case where project path is mount directory (".")
- Normalize paths in both bootstrap and entrypoint scripts
- Show explicit path resolution steps in debug output
- Remove leading slashes before any path concatenation
- For project paths, mount the parent directory and use the last component as PROJECT_PATH
- Support both interactive prompts and command-line arguments for automation
- Add debug output showing path resolution steps for easier troubleshooting
- Validate directory existence before proceeding
- Convert paths to absolute form for validation
- Use current directory as default when appropriate
- Show clear error messages for missing directories

## Terminal UI Best Practices

- Use `read -e` for path auto-completion in supported shells
- Show default values in gray using ANSI color codes
- Allow accepting defaults by pressing Enter
- Use colors consistently for different types of output:
  - Gray for defaults/suggestions (including default options in Y/n prompts)
  - Green for success/status
  - Yellow for notes/warnings
  - Red for errors
- Provide visual separation between sections with headers
- Show command previews before execution
- Support both interactive and automated usage through command-line args
- Show default values inline with prompt text
- Use parentheses around default values for clarity
- Keep prompt and input on same line
- Detect shell capabilities for better readline support
- Provide fallbacks for shells without readline
- Format yes/no prompts consistently with other prompts
- Show default option in gray: [Y/n] or [y/N]

### Terminal Color Handling

- Use tput when available for better terminal compatibility
- Provide ANSI color code fallbacks when tput is not available
- Always quote color variables in printf statements
- Use setaf for foreground colors (1=red, 2=green, 3=yellow, 8=gray)
- Use sgr0 to reset all attributes
- Redirect tput stderr to /dev/null to handle non-terminal cases
- Test color output in both terminal and non-terminal environments

## Script Distribution

- Prefer bash scripts over Node.js for setup tools
- Bash provides better cross-platform compatibility
- Avoid unnecessary dependencies on runtimes (Node, Python, etc.)
- Shell scripts work on most Unix-like systems out of the box
- Windows users typically have Git Bash or WSL available
- Keep terminal UI simple and compatible with basic shells
- Stick to standard Unix conventions for prompts and input

## Session Management

Avoid using tmux or other session managers in Docker when:
- The main process is already interactive
- The container is designed to run a single process
- Session management would create recursive execution

Instead:
- Run the interactive process directly
- Use Docker's built-in TTY and interactive mode (-it flags)
- Let Docker handle the container lifecycle

## Terminal Handling
- Use `script` command with `-qf` flags for reliable PTY handling
- Install `bsdutils` package for script command
- Create PTY file with 666 permissions
- Use `tail -f` to continuously read PTY output
- Write to `/dev/pts/0` for PTY input
- When sending input to Node.js readline:
  - Add delay (0.5-1s) between message and Enter key
  - Send \r for Enter key
  - Node.js needs time to process input before receiving Enter
- Use expect's exp_internal 1 for debugging terminal interactions

## File-Based Communication
- Use regular files instead of pipes for simpler debugging
- Keep only latest message by overwriting instead of appending
- Use inotifywait for efficient file change detection when available
- Fall back to modification time polling if inotifywait not available
- Set 666 permissions on shared files
- Mount comm directory separately from workspace

## Error Handling
- Add cleanup trap for process termination
- Check file permissions on startup
- Verify required directories exist
- Kill background processes on exit
- Handle missing files gracefully

## Process Management
- Use background processes with & for async operations
- Store PIDs for cleanup
- Wait for main process to exit
- Use exec to replace shell in entrypoint
- Signal container readiness through response file

## Package Requirements
- inotify-tools: For file change monitoring
- bsdutils: For script command and PTY handling
- procps: For process management
- util-linux: Alternative for script command

## Testing
- Use test mode for verifying communication
- Echo server for basic verification
- Timeout handling for stuck processes
- Clear error messages for debugging

## Interactive Program Handling
- Use expect for interactive program automation
- Wait for specific prompts before sending input
- Clear input files after sending to prevent duplicate sends
- Use inotifywait to detect file changes efficiently
- Flush output buffers after sending commands
```

## File: `utils/docker/message-bridge.sh`
```bash
#!/bin/bash
set -e

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*"
}

debug() {
    if [ "${DEBUG:-false}" = "true" ]; then
        log "DEBUG: $*"
    fi
}

cleanup() {
    log "Cleaning up..."
    exit 0
}
trap cleanup SIGINT SIGTERM EXIT

# Get the project directory from the command line argument
if [ -z "$1" ]; then
    echo "Usage: $0 <project-path>"
    exit 1
fi

PROJECT_DIR="$1"
COMM_DIR="$PROJECT_DIR/.codebuff/comm"
debug "Using comm directory: $COMM_DIR"

# Wait for comm directory and files to exist
log "Waiting for comm directory and files..."
while [ ! -f "$COMM_DIR/responses.txt" ]; do
    sleep 0.1
done

# Main loop - tail the responses file
log "Starting to tail responses.txt..."
tail -f "$COMM_DIR/responses.txt"
```

## File: `utils/docker/start-codebuff.sh`
```bash
#!/bin/bash
set -e

# ANSI color codes - using simpler codes for better compatibility
GRAY="$(tput setaf 8 2>/dev/null || echo '\033[90m')"  # Fallback to 90m if tput not available
RESET="$(tput sgr0 2>/dev/null || echo '\033[0m')"
GREEN="$(tput setaf 2 2>/dev/null || echo '\033[32m')"
YELLOW="$(tput setaf 3 2>/dev/null || echo '\033[33m')"
RED="$(tput setaf 1 2>/dev/null || echo '\033[31m')"

# Add timestamp to logs
log() {
    echo "[HOST] [$(date '+%Y-%m-%d %H:%M:%S')] $*"
}

debug() {
    if [ "${DEBUG}" = true ]; then
        echo "[HOST] [DEBUG] [$(date '+%Y-%m-%d %H:%M:%S')] $*"
    fi
}

error() {
    echo "[HOST] [ERROR] [$(date '+%Y-%m-%d %H:%M:%S')] $*"
}

cleanup() {
    log "Cleaning up..."
    if [ "${DEBUG}" = true ]; then
        debug "Stopping container: $CONTAINER_ID"
        docker stop "$CONTAINER_ID" >/dev/null 2>&1 || true
        debug "Removing container: $CONTAINER_ID"
        docker rm "$CONTAINER_ID" >/dev/null 2>&1 || true
    fi
    exit 0
}
trap cleanup SIGINT SIGTERM EXIT

# Determine correct 'stat' syntax based on platform (BSD/macOS vs GNU/Linux)
if stat -c %Y / >/dev/null 2>&1; then
    # GNU stat (Linux)
    STAT_CMD="stat -c"
else
    # BSD stat (macOS, FreeBSD, etc.)
    STAT_CMD="stat -f"
fi

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    error "Docker is not installed. Please install Docker first."
    exit 1
fi

# Build or rebuild the Docker image
log "Checking Docker image..."
if ! docker images codebuff --format "{{.ID}}" | grep -q .; then
    log "Building Docker image for the first time..."
    docker build -t codebuff "$SCRIPT_DIR" || { error "Failed to build Docker image"; exit 1; }
else
    # Always rebuild if any of the scripts have been modified
    DOCKERFILE_MTIME=$($STAT_CMD %m "$SCRIPT_DIR/Dockerfile")
    WRAPPER_MTIME=$($STAT_CMD %m "$SCRIPT_DIR/codebuff-wrapper.sh")
    ENTRYPOINT_MTIME=$($STAT_CMD %m "$SCRIPT_DIR/entrypoint.sh")
    BRIDGE_MTIME=$($STAT_CMD %m "$SCRIPT_DIR/message-bridge.sh")

    # Get the most recent modification time
    LATEST_MTIME=$DOCKERFILE_MTIME
    for t in $WRAPPER_MTIME $ENTRYPOINT_MTIME $BRIDGE_MTIME; do
        if [ $t -gt $LATEST_MTIME ]; then
            LATEST_MTIME=$t
        fi
    done

    debug "Latest modification time: $LATEST_MTIME"
    debug "Raw modification time: $($STAT_CMD %Sm "$SCRIPT_DIR/Dockerfile")"

    # Always rebuild for now - safer while we're actively developing
    log "Scripts may have been modified. Rebuilding image..."
    docker build -t codebuff "$SCRIPT_DIR" || { error "Failed to rebuild Docker image"; exit 1; }
fi

# ------------------------- Get Project Path ------------------------------------
DEFAULT_PATH="$(pwd)"
if [ -n "$1" ]; then
    SELECTED_PROJECT_PATH="$1"
else
    printf "Enter the project path (%s%s%s): " "${GRAY}" "${DEFAULT_PATH}" "${RESET}"
    read -r SELECTED_PROJECT_PATH
    SELECTED_PROJECT_PATH=${SELECTED_PROJECT_PATH:-$DEFAULT_PATH}
fi

# Convert to absolute path
SELECTED_PROJECT_PATH=$(cd "$SELECTED_PROJECT_PATH" && pwd)

# ------------------------- Get Host Base Directory -----------------------------
# Automatically determine host mount dir as parent of project dir
HOST_MOUNT_DIR=$(dirname "$SELECTED_PROJECT_PATH")
RELATIVE_PATH=$(basename "$SELECTED_PROJECT_PATH")

# Extract project name from path
PROJECT_NAME="$RELATIVE_PATH"

# Debug output
echo
debug "Host mount dir: $HOST_MOUNT_DIR"
debug "Selected path: $SELECTED_PROJECT_PATH"
debug "Resolved to: $RELATIVE_PATH"
debug "Project name: $PROJECT_NAME"
echo

# Create comm directory inside the project directory
debug "Setting up communication directory..."
COMM_DIR="$SELECTED_PROJECT_PATH/.codebuff/comm"
mkdir -p "$COMM_DIR"
touch "$COMM_DIR/messages.txt" "$COMM_DIR/responses.txt"
chmod 666 "$COMM_DIR/messages.txt" "$COMM_DIR/responses.txt"

# Start container in background
log "Starting container..."
CONTAINER_ID=$(docker run -d --privileged \
    -e "PROJECT_PATH=$RELATIVE_PATH" \
    -e "PROJECT_NAME=$PROJECT_NAME" \
    -e "DEBUG=${DEBUG:-false}" \
    -v "$HOME/.config/manicode:/workspace/.config/manicode" \
    -v "$HOST_MOUNT_DIR:/workspace" \
    codebuff)

echo "${GREEN}Started container with ID: $CONTAINER_ID${RESET}"
debug "Container mounts:"
docker inspect "$CONTAINER_ID" --format='{{range .Mounts}}{{.Source}} -> {{.Destination}}{{println}}{{end}}'

# Wait for container to be ready with better error handling
log "Checking container status..."
timeout=300
start_time=$(date +%s)
while true; do
    # Check if container is still running using full container ID
    if ! docker ps --no-trunc -q | grep -q "$CONTAINER_ID"; then
        error "Container stopped unexpectedly"
        log "Container logs:"
        docker logs "$CONTAINER_ID"
        echo
        log "Exit code:"
        docker inspect "$CONTAINER_ID" --format='{{.State.ExitCode}}'
        exit 1
    fi

    # Check for ready signal
    if [ -s "$COMM_DIR/responses.txt" ] && grep -q "CONTAINER READY" "$COMM_DIR/responses.txt"; then
        log "Container started successfully"
        # Clear responses.txt after container is ready
        echo > "$COMM_DIR/responses.txt"
        break
    fi

    # Check timeout
    current_time=$(date +%s)
    if [ $((current_time - start_time)) -gt "$timeout" ]; then
        error "Timeout waiting for container to start"
        log "Container logs:"
        docker logs "$CONTAINER_ID"
        docker stop "$CONTAINER_ID"
        exit 1
    fi
    sleep 1
done

# Start message bridge
debug "Starting message bridge..."
exec "$SCRIPT_DIR/message-bridge.sh" "$SELECTED_PROJECT_PATH"
```

