---
id: github.com-andorp-order-taking-295ff3a6-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:30.185711
---

# KNOWLEDGE EXTRACT: github.com_andorp_order-taking_295ff3a6
> **Extracted on:** 2026-04-01 14:45:53
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007524116/github.com_andorp_order-taking_295ff3a6

---

## File: `.gitignore`
```
*.ibc
*.o
build/
db/
node_modules/
service/
```

## File: `LICENSE`
```
BSD 3-Clause License (with research publishing addition)

Copyright (c) 2021, Andor Penzes
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

4. In case of any research is derived from this software, the author of
   the software must be notified and an optional co-author position on the research
   paper should be offered. This software must be referred as a source.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```

## File: `Makefile`
```
idris2 = idris2
node = node

init: FORCE
	test -d db      || mkdir db
	test -d build   || mkdir build
	test -d service || mkdir service
	touch service/order-taking-service.js

typecheck: src order-taking-service.ipkg FORCE
	$(idris2) --typecheck order-taking-service.ipkg --codegen node

FORCE:

watch:
	while inotifywait -e close_write -r src; do $(idris2) --typecheck order-taking-service.ipkg; done

clean-lsp-log:
	rm ~/.cache/nvim/lsp.log

clean:
	$(idris2) --clean order-taking-service.ipkg
	rm -r build

repl:
	rlwrap $(idris2) --repl order-taking-service.ipkg --codegen node

nodejs:
	$(idris2) --clean order-taking-service.ipkg
	$(idris2) --build order-taking-service.ipkg --codegen node

drop-db:
	rm -r db

init-db: init drop-db nodejs
	mkdir db
	touch db/product.db
	touch db/order.db
	rm service/order-taking-service.js
	cp build/exec/order-taking-service service/order-taking-service.js
	$(node) service/order-taking-service.js --init-db

start: init nodejs
	rm service/order-taking-service.js
	cp build/exec/order-taking-service service/order-taking-service.js
	$(node) service/order-taking-service.js

start-opt: init nodejs
	rm service/order-taking-service.js
	cp build/exec/order-taking-service service/order-taking-service.js
	npx google-closure-compiler service/order-taking-service.js \
			--language_out=ES_2020 \
			--isolation_mode=IIFE --module_resolution=NODE \
			--assume_function_wrapper > service/order-taking-service-opt.js
	$(node) service/order-taking-service-opt.js

restart:
	$(node) service/order-taking-service.js

restart-opt:
	$(node) service/order-taking-service-opt.js

```

## File: `READMAP.md`
```markdown
# Reader's map

Disclaimer: The documentation is still in the making...

You may want to read the documentation from the modules in this order if you want to learn
Idris via examples.

- [Data.Result](https://github.com/andorp/order-taking/blob/main/src/Data/Result.idr)
- [Data.Form](https://github.com/andorp/order-taking/blob/main/src/Data/Form.idr)
- [Data.Between](https://github.com/andorp/order-taking/blob/main/src/Data/Between.idr)
- [Data.StringN](https://github.com/andorp/order-taking/blob/main/src/Data/StringN.idr)
- [Language.JSON.Schema](https://github.com/andorp/order-taking/blob/main/src/Language/JSON/Schema.idr)
- [Rango.BoundedContext.Workflow](https://github.com/andorp/order-taking/blob/main/src/Rango/BoundedContext/Workflow.idr)
- [Rango.BoundedContext.BoundedContext](https://github.com/andorp/order-taking/blob/main/src/Rango/BoundedContext/BoundedContext.idr)
- [Service.NodeJS.Date](https://github.com/andorp/order-taking/blob/main/src/Service/NodeJS/Date.idr)
- [Service.NodeJS.Random](https://github.com/andorp/order-taking/blob/main/src/Service/NodeJS/Random.idr)
- [Service.NodeJS.MD5](https://github.com/andorp/order-taking/blob/main/src/Service/NodeJS/MD5.idr)
- [Service.NodeJS.Promise](https://github.com/andorp/order-taking/blob/main/src/Service/NodeJS/Promise.idr)
- ...

You may want to read the documentation from the modules in this order if you want to learn
about the DDD solution and its implementation in Idris.

- TODO
```

## File: `README.md`
```markdown
# Idris Full Stack DDD NodeJS example

## Order Taking Service

Idris version of Domain Modeling Made Functional Book.

 The [Domain Modeling Made Functional by Scott Wlaschin](https://www.amazon.co.uk/Domain-Modeling-Made-Functional-Domain-Driven/dp/1680502549)
introduces domain driven design and shows how well it fits to the world of functional programming via the lens of
the F# programming language. As Scott showed us that DDD is indeed a nice fit for functional programming,
questions arise naturally; could we push further the abstractions if we use a dependently typed programming language, like Idris?
Where are the sweet spots of depedent types in the world of everyday programming?
 Everyday programming needs to be focused on delivery, maintanability, reliability, and being correct.
The sad truth is that many applications needs to be more maintanable than correct.
Being correct is not a clear concept because its meaning changes as the software evolves.
In many cases, stakeholders only get a deeper understanding of the domain as the software solution/product evolves over time.
In this setting, depedent typed programming helps us achieve maintanability rather than being correct.
 In this repository I show a simple layered architecture and I show how to use simple dependent types
to draw explicit connections between the high level design of a service and its NodeJS deployed implementation.
Ideas and practices originated, but reshuffled from the [Type Driven Development with Idris by Edwin Brady](https://www.amazon.co.uk/Type-driven-Development-Idris-Edwin-Brady/dp/1617293024)
and the [Domain Modeling Made Functional by Scott Wlaschin](https://www.amazon.co.uk/Domain-Modeling-Made-Functional-Domain-Driven/dp/1680502549).
This architecture includes; An abstraction to talk about Bounded Context and Workflow, type safe description of a state transition system,
a free monad approach for domain implementation, and an actual implementation of the domain on NodeJS back-end.
 Because of dependent types, this architecture becomes explicit, rather than implicit, meaning that
connections between the high level design and the low level implementation are done via functions, changing
the code anywhere requires to think at the whole, as possible type errors propagates to top or to bottom.
 Idris could immensely benefit from simple FFIs for NodeJS libraries. The FFIs would grant access to thousands
of libraries from the NodeJS ecosystem almost for free. This approach would position Idris to be used even
in production settings and the Idris userbase could be bootstrapped, later the Idris version of these
libraries could be written.

Request: Please consider buying both of the books mentioned above. Boths are excellent resources for
further studying of the applied subject.

## Work In Progress parts:

- The documentation is still under development. Please come back regurarly to see what changed.
- Client needs lots of improvements.
- Better error Handling around workflow runners.
- Dependently driven testing needs to be implemented.

## Financial Support

<a href="https://www.patreon.com/AndOrP">
<img src="https://c5.patreon.com/external/logo/become_a_patron_button.png" width="150"/>
</a>

## Talk

<a href="https://youtu.be/QBj-4K-l-sg">Youtube</a>

## Notes

This project meant to be a blue-print, example for micro-services written in Idris. Its main focus is to reproduce
abstractions in dependently typed setting, that can be found in Scott Wlashin's book. The main focus is
around the dependently typed implementation of `BoundedContext`, but several other parts of the architecture
had to be worked on to be able to demostrate that Idris can host such solutions. Although during the implementation
many other problems were required to think about in the dependently typed setting. This repository can be
considered as a mine practices for dependently typed software development. Enjoy digging up those gems.

You may find the style of the explanations strange, maybe a bit chaotic, but if you follow path suggested
in the [READMAP.md](https://github.com/andorp/order-taking/blob/main/READMAP.md) you will learn many things about the Idris language. This style feels chaotic that could
be because I have a slight ADHD and I try to linarize the content here, but sometimes quickly the explanations
go deep. Although I believe a short explanation after every Idris snippet helps to view this reposity as
a hand-book for Idris development.

## High level overview

This repository contains more than just the `Idris` one to one translation of the `F#` code from the
Domain Modeling Made Functional book. I wanted to show how Idris can be used to interface with existing
`NodeJS` libraries. For that reason I added the following parts:

- FFI for NodeJS interfacing libraries
- Sketch of type-safe SQL library
- Minimal scaffolding of a NodeJS server
- Dependently typed framework for Bound-Context and Workflows
- State transition of the PlaceOrder example
- Free monadic DSL formalization of the PlaceOrder example
- One backend implementation of the operations of PlaceOrder DSL

See the [slides](https://github.com/andorp/order-taking/blob/main/SLIDES.md)

## Run

After setted up; start the microservice with `make start-opt`, start the client service `npm run dev`,
and open `localhost:5000` in a browser.

## Setup

### Server

 * Install Idris2 which version must match the one marketd the [VERSIONS](https://github.com/andorp/order-taking/blob/main/VERSIONS) file. OR
 * If you Idris2 release version installed, check out the corresponding tag from 0.4.0

For dependencies install `nodejs`, `npm` and packages:

```
npm install google-closure-compiler
npm install sqlite
npm install md5
```

To start the OrderTaking service, which will create the initial Sqlite DB and starts
the service on `127.0.0.1:3000`

```
make init-db
make start-opt
```

### Client

An example client can be found in the `client/svelte-client` directory. Follow the instructions
from its README.md

To run the client, call the following command:

```
cd client/svelte-client
npm run dev
```

Which starts the client in development mode, any changes in its code, will be picked up.

Important note, use the `g21` as product code on the client side for testing. The client
is very in pre-alpha state, best to open the developer console to see, what happens before and
after submitting the order. I will work on these details soon.

Have fun!

## ASCII ART

[ASCII ART](https://dot-to-ascii.ggerganov.com/)
```

## File: `SLIDES.md`
```markdown
# Slides

## High level overview

### Idealized view of software projects

```
┌−−−−−−−−−−−−−−−−−−−−−−−−−−−┐
╎  Software Project         ╎
╎                           ╎
╎ ┌───────────────────┐     ╎
╎ │   Requirements    │─┐   ╎
╎ └───────────────────┘ │   ╎
╎   │                   │   ╎
╎   ▼                   │   ╎
╎ ┌───────────────────┐ │   ╎
╎ │ Quality Assurance │ │   ╎
╎ └───────────────────┘ │   ╎
╎   │                   │   ╎
╎   ▼                   │   ╎
╎ ┌───────────────────┐ │   ╎
╎ │  Implementation   │◀┘   ╎
╎ └───────────────────┘     ╎
└−−−−−−−−−−−−−−−−−−−−−−−−−−−┘
```

### Semantic tower of a tipical software project

```
┌−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−┐
╎         Semantic Tower         ╎
╎                                ╎
╎ ┌────────────────────────────┐ ╎
╎ │       Design diagram       │ ╎
╎ └────────────────────────────┘ ╎
╎ ┌────────────────────────────┐ ╎
╎ │      Detailed design       │ ╎
╎ └────────────────────────────┘ ╎
╎ ┌────────────────────────────┐ ╎
╎ │ Data / Behavior definition │ ╎
╎ └────────────────────────────┘ ╎
╎ ┌────────────────────────────┐ ╎
╎ │       Implementation       │ ╎
╎ └────────────────────────────┘ ╎
╎ ┌────────────────────────────┐ ╎
╎ │         Libraries          │ ╎
╎ └────────────────────────────┘ ╎
╎ ┌────────────────────────────┐ ╎
╎ │      Tech environment      │ ╎
╎ └────────────────────────────┘ ╎
└−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−┘
```

### Realization of a software project

```
┌−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−┐
╎             Real Software Project             ╎
╎                                               ╎
╎ ┌───────────────────────────────────────────┐ ╎
╎ │       Requirement docs, JIRA items        │ ╎
╎ └───────────────────────────────────────────┘ ╎
╎ ┌───────────────────────────────────────────┐ ╎
╎ │      Implemented data and behaviour       │ ╎
╎ └───────────────────────────────────────────┘ ╎
╎ ┌───────────────────────────────────────────┐ ╎
╎ │ Some kind tests; manual, unit, end-to-end │ ╎
╎ └───────────────────────────────────────────┘ ╎
└−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−┘
```


### Realization of a software project including the semantic tower

```
┌−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−┐
╎                Real Software Project               ╎
╎                                                    ╎
╎ ┌────────────────────────────────────────────────┐ ╎
╎ │            Requirement docs, JIRA items        │ ╎
╎ │                                                │ ╎
╎ │         ┌────────────────────────────┐         │ ╎
╎ │         │        Design Diagram      │         │ ╎
╎ │         └────────────────────────────┘         │ ╎
╎ │         ┌────────────────────────────┐         │ ╎
╎ │         │        Detailed Design     │         │ ╎
╎ │         └────────────────────────────┘         │ ╎
╎ │         ┌────────────────────────────┐         │ ╎
╎ │         │ Data / Behavior definition │         │ ╎
╎ │         └────────────────────────────┘         │ ╎
╎ └────────────────────────────────────────────────┘ ╎
╎ ┌────────────────────────────────────────────────┐ ╎
╎ │         Implemented data and behaviour         │ ╎
╎ │                                                │ ╎
╎ │         ┌────────────────────────────┐         │ ╎
╎ │         │       Implementation       │         │ ╎
╎ │         └────────────────────────────┘         │ ╎
╎ │         ┌────────────────────────────┐         │ ╎
╎ │         │          Libraries         │         │ ╎
╎ │         └────────────────────────────┘         │ ╎
╎ │         ┌────────────────────────────┐         │ ╎
╎ │         │       Tech environment     │         │ ╎
╎ │         └────────────────────────────┘         │ ╎
╎ └────────────────────────────────────────────────┘ ╎
╎ ┌────────────────────────────────────────────────┐ ╎
╎ │    Some kind tests; manual, unit, end-to-end   │ ╎
╎ │                                                │ ╎
╎ │         ┌────────────────────────────┐         │ ╎
╎ │         │       Implementation       │         │ ╎
╎ │         └────────────────────────────┘         │ ╎
╎ │         ┌────────────────────────────┐         │ ╎
╎ │         │          Libraries         │         │ ╎
╎ │         └────────────────────────────┘         │ ╎
╎ │         ┌────────────────────────────┐         │ ╎
╎ │         │      Tech environment      │         │ ╎
╎ │         └────────────────────────────┘         │ ╎
╎ └────────────────────────────────────────────────┘ ╎
└−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−┘
```

### Change request of any kind

```
┌−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−┐
╎          Semantic Tower         ╎
╎                                 ╎
╎ ┌─────────────────────────────┐ ╎
╎ │        Design diagram       │ ╎ ◀─ Change should propagate down
╎ └─────────────────────────────┘ ╎
╎ ┌─────────────────────────────┐ ╎
╎ │       Detailed design       │ ╎
╎ └─────────────────────────────┘ ╎
╎ ┌─────────────────────────────┐ ╎
╎ │  Data / Behavior definition │ ╎ ◀─ Change should propagate up and down
╎ └─────────────────────────────┘ ╎
╎ ┌─────────────────────────────┐ ╎
╎ │        Implementation       │ ╎
╎ └─────────────────────────────┘ ╎
╎ ┌─────────────────────────────┐ ╎
╎ │          Libraries          │ ╎
╎ └─────────────────────────────┘ ╎
╎ ┌─────────────────────────────┐ ╎
╎ │       Tech environment      │ ╎ ◀─ Change could tear down all the project,
╎ └─────────────────────────────┘ ╎    but definetly could destroy everything up
└−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−┘    to the behavioral definition.
```

### Change request in realized software project

```
┌−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−┐
╎                Real Software Project               ╎
╎                                                    ╎
╎ ┌────────────────────────────────────────────────┐ ╎
╎ │            Requirement docs, JIRA items        │ ╎
╎ │                                                │ ╎
╎ │         ┌────────────────────────────┐         │ ╎
╎ │         │        Design Diagram      │         │ ╎ ◀─ Change here indicates ... what?
╎ │         └────────────────────────────┘         │ ╎
╎ │         ┌────────────────────────────┐         │ ╎
╎ │         │        Detailed Design     │         │ ╎
╎ │         └────────────────────────────┘         │ ╎
╎ │         ┌────────────────────────────┐         │ ╎
╎ │         │ Data / Behavior definition │         │ ╎ ◀─ Change here indicates ... what?
╎ │         └────────────────────────────┘         │ ╎
╎ └────────────────────────────────────────────────┘ ╎
╎ ┌────────────────────────────────────────────────┐ ╎
╎ │         Implemented data and behaviour         │ ╎
╎ │                                                │ ╎
╎ │         ┌────────────────────────────┐         │ ╎
╎ │         │       Implementation       │         │ ╎
╎ │         └────────────────────────────┘         │ ╎
╎ │         ┌────────────────────────────┐         │ ╎
╎ │         │          Libraries         │         │ ╎
╎ │         └────────────────────────────┘         │ ╎
╎ │         ┌────────────────────────────┐         │ ╎
╎ │         │       Tech environment     │         │ ╎ ◀─ Change here indicates ... what?
╎ │         └────────────────────────────┘         │ ╎
╎ └────────────────────────────────────────────────┘ ╎
╎ ┌────────────────────────────────────────────────┐ ╎
╎ │    Some kind tests; manual, unit, end-to-end   │ ╎
╎ │                                                │ ╎
╎ │         ┌────────────────────────────┐         │ ╎
╎ │         │       Implementation       │         │ ╎
╎ │         └────────────────────────────┘         │ ╎
╎ │         ┌────────────────────────────┐         │ ╎
╎ │         │          Libraries         │         │ ╎
╎ │         └────────────────────────────┘         │ ╎
╎ │         ┌────────────────────────────┐         │ ╎
╎ │         │      Tech environment      │         │ ╎
╎ │         └────────────────────────────┘         │ ╎
╎ └────────────────────────────────────────────────┘ ╎
└−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−┘
```

### Domain Driven Design

Focuses on the **Data / Behavioral definition**. DDD models the software a collection of
bounded contextes that interact with each other.

```
┌−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−┐
╎                    Bounded Context                    ╎
╎                                                       ╎
╎                   ┌───────────────┐                   ╎
╎   ┌────────────── │    Command    │ ──────┐           ╎
╎   │               └───────────────┘       │           ╎
╎   │                 │                     │           ╎
╎   │                 │                     │           ╎
╎   ▼                 ▼                     ▼           ╎
╎ ┌───────────┐     ┌───────────────┐     ┌───────────┐ ╎
╎ │ Workflow  │     │    Workflow   │     │ Workflow  │ ╎
╎ └───────────┘     └───────────────┘     └───────────┘ ╎
╎   │                 │                     │           ╎
╎   │                 │                     │           ╎
╎   │                 ▼                     │           ╎
╎   │               ┌───────────────┐       │           ╎
╎   └─────────────▶ │     Event     │ ◀─────┘           ╎
╎                   └───────────────┘                   ╎
└−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−┘
```

### Behaviour described in workflows

For example

```
┌−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−┐                                    
╎                                    ┌────────────────────────────┐ ╎
╎                                    │         OrderForm          │ ╎
╎                                    └────────────────────────────┘ ╎
╎                                      │                            ╎
╎                                      │ Validate Order             ╎
╎                                      ▼                            ╎
╎ ┌─────────────┐    Create valid    ┌============================┐ ╎
╎ │ ValidOrder  │   ◀─────────────── I           Order            I ╎
╎ └─────────────┘                    └============================┘ ╎
╎   │                                  │                            ╎
╎   │ Price                            │ Create invalid             ╎
╎   ▼                                  ▼                            ╎
╎ ┌─────────────┐                    ┌────────────────────────────┐ ╎
╎ │ PricedOrder │                    │        InvalidOrder        │ ╎
╎ └─────────────┘                    └────────────────────────────┘ ╎
╎   │                                  │                            ╎
╎   │                                  │ Queue                      ╎
╎   │                                  ▼                            ╎
╎   │                                ┌────────────────────────────┐ ╎
╎   │                                |     InvalidOrderQueued     │ ╎
╎   │                                └────────────────────────────┘ ╎
╎   │                                  │                            ╎
╎   │                                  │ Create invalid order info  ╎
╎   │                                  ▼                            ╎
╎   │  Create priced order info      ┌────────────────────────────┐ ╎
╎   └────────────────────────────▶   │         OrderInfo          │ ╎
╎                                    └────────────────────────────┘ ╎
└−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−┘
```

### Information flow

In a service implementation information is processed via information flow
from Request to Response. In the Bounded Context of DDD this workflow
looks like this:

```
┌−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−┐
╎      Request/Response flow in bounded context           ╎
╎                                                         ╎
╎            ┌─────────────────────┐                      ╎
╎            │       Request       │                      ╎
╎            └─────────────────────┘                      ╎
╎              ▼                                          ╎
╎            ┌─────────────────────┐                      ╎
╎            │        JSON         │                      ╎
╎            └─────────────────────┘                      ╎
╎              ▼                                          ╎
╎            ┌─────────────────────┐                      ╎
╎            │    Command Data     │                      ╎
╎            └─────────────────────┘                      ╎
╎              ▼                                          ╎
╎            ┌─────────────────────┐                      ╎
╎            │       Command       │                      ╎
╎            └─────────────────────┘                      ╎
╎              ▼                                          ╎
╎            ┌─────────────────────┐                      ╎
╎            │   Workflow Input    │                      ╎
╎            └─────────────────────┘                      ╎
╎                ▼                                        ╎
╎ ┌────┐       ┌─────────────────────┐       ┌──────────┐ ╎
╎ │ DB │ ───── │ Workflow Internals  │ ───── │ Services │ ╎
╎ └────┘       └─────────────────────┘       └──────────┘ ╎
╎              ▼                                          ╎
╎            ┌─────────────────────┐                      ╎
╎            │   Workflow Output   │                      ╎
╎            └─────────────────────┘                      ╎
╎              ▼                                          ╎
╎            ┌─────────────────────┐                      ╎
╎            │        Event        │                      ╎
╎            └─────────────────────┘                      ╎
╎              ▼                                          ╎
╎            ┌─────────────────────┐                      ╎
╎            │     Event Data      │                      ╎
╎            └─────────────────────┘                      ╎
╎              ▼                                          ╎
╎            ┌─────────────────────┐                      ╎
╎            │        JSON         │                      ╎
╎            └─────────────────────┘                      ╎
╎              ▼                                          ╎
╎            ┌─────────────────────┐                      ╎
╎            │      Response       │                      ╎
╎            └─────────────────────┘                      ╎
└−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−┘

```

### The missing link in the semantic tower

Layers may depend on each other. With dependent types we can express this connection.
If layer n of the semantic tower is a function of layer n-1 than any change in
one layer, will propagate through the semantic tower.

```
┌−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−┐
╎         Semantic Tower         ╎
╎                                ╎
╎ ┌────────────────────────────┐ ╎
╎ │       Design diagram       │ ╎
╎ └────────────────────────────┘ ╎
╎   │                            ╎
╎   ▼                            ╎
╎ ┌────────────────────────────┐ ╎
╎ │      Detailed design       │ ╎
╎ └────────────────────────────┘ ╎
╎   │                            ╎
╎   ▼                            ╎
╎ ┌────────────────────────────┐ ╎
╎ │ Data / Behavior definition │ ╎ ◀─ Change *will* propagate up and down
╎ └────────────────────────────┘ ╎
╎   │                            ╎
╎   ▼                            ╎
╎ ┌────────────────────────────┐ ╎
╎ │       Implementation       │ ╎
╎ └────────────────────────────┘ ╎
╎   │                            ╎
╎   ▼                            ╎
╎ ┌────────────────────────────┐ ╎
╎ │         Libraries          │ ╎
╎ └────────────────────────────┘ ╎
╎   │                            ╎
╎   ▼                            ╎
╎ ┌────────────────────────────┐ ╎
╎ │      Tech environment      │ ╎
╎ └────────────────────────────┘ ╎
└−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−┘
```

## Implementation details

### Focus on the most important part: Workflow

Explicit connection between high level definition of the workflow and its implementation.

- [PlaceOrder.Overview](https://github.com/andorp/order-taking/blob/main/src/BoundedContext/OrderTaking/Workflow/PlaceOrder/Overview.idr)
- [Rango.BoundedContext.Workflow DSL](https://github.com/andorp/order-taking/blob/main/src/Rango/BoundedContext/Workflow.idr)

The implementation of the workflow, is a function from the high level description of the workflow to a monadic state transition, via
the `morph` helper function:

```idris
placeOrder : Workflow Step Check OrderForm OrderInfo
placeOrder = do
  Do ValidateOrder
  Branch CheckInvalidOrder
    (do Do AddInvalidOrder
        Do SendInvalidOrder)
    (do Do PriceOrder
        Do SendAckToCustomer)
```

```idris
record Morphism (monad : Type -> Type) state (cmd : state -> state -> Type) (chk : state -> state -> state -> Type)
  where
    constructor MkMorphism
    StateType : state -> Type
    step      : cmd s e -> (StateType s) -> monad (StateType e)
    check     : chk s b1 b2 -> (StateType s) -> monad (Either (StateType b1) (StateType b2))
```

```idris
morph
  ...
  -> (r : Morphism monad state cmd chk)
  -> Workflow cmd chk start end
  -> (StateType r start) -> monad (StateType r end)
morph r w = ...
```

### Simplest architecture with workflow abstraction included

```
┌−−−−−−−−−−−−−−−−−−−−−−−−−−┐
╎       Architecture       ╎
╎                          ╎
╎ ┌──────────────────────┐ ╎
╎ │ Place Order Workflow │ ╎
╎ └──────────────────────┘ ╎
╎ ┌──────────────────────┐ ╎
╎ │  Place Order Monad   │ ╎
╎ └──────────────────────┘ ╎
╎ ┌──────────────────────┐ ╎
╎ │ NodeJS Promise Monad │ ╎
╎ └──────────────────────┘ ╎
└−−−−−−−−−−−−−−−−−−−−−−−−−−┘
```

### Full architecture

```
┌−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−┐
╎           Architecture           ╎
╎                                  ╎
╎ ┌──────────────────────────────┐ ╎
╎ │ Order Taking Bounded Context │ ╎
╎ └──────────────────────────────┘ ╎
╎ ┌──────────────────────────────┐ ╎
╎ │     Place Order Workflow     │ ╎
╎ └──────────────────────────────┘ ╎
╎ ┌──────────────────────────────┐ ╎
╎ │ Place Order DSL (Free Monad) │ ╎
╎ └──────────────────────────────┘ ╎
╎ ┌──────────────────────────────┐ ╎
╎ │  Place Order Backend Monad   │ ╎
╎ └──────────────────────────────┘ ╎
╎ ┌──────────────────────────────┐ ╎
╎ │ Place Order Database Monads  │ ╎
╎ └──────────────────────────────┘ ╎
╎ ┌──────────────────────────────┐ ╎
╎ │        Runtime Monad         │ ╎ - NodeJS Promise
╎ └──────────────────────────────┘ ╎
╎ ┌──────────────────────────────┐ ╎
╎ │          Tech stack          │ ╎ - NodeJS Runtime
╎ └──────────────────────────────┘ ╎
└−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−┘
```

### Information flow

### Bounded Context implementation

[Source](https://github.com/andorp/order-taking/blob/main/src/Rango/BoundedContext/BoundedContext.idr#L52)

```idris
record BoundedContext where
  constructor MkBoundedContext
  command     : Type
  workflow    : Type
  event       : Type
  workflowOf  : command -> workflow
  eventOf     : command -> event
```

[Source](https://github.com/andorp/order-taking/blob/main/src/Rango/BoundedContext/BoundedContext.idr#L183)

```idris
||| Execute a command with the given bounded context.
execute
  :  (Monad m)
  => (bc : BoundedContextImplementation m) -> bc.ContextCommand -> m (Either bc.ContextError bc.ContextEvent)
execute bc contextCommand = do
  (cmd ** cmdData) <- bc.createCommand contextCommand
  workflowRunner <- bc.createWorkflowEmbedding cmd
  let workflowMonadInstance = bc.WorkflowMonadInstance (bc.context.workflowOf cmd) -- For transformWorkflow
  input  <- bc.createStartState cmd cmdData
  result <- runEmbedding workflowRunner (transformWorkflow (bc.Workflow (bc.context.workflowOf cmd)) (bc.workflowMorphism cmd) input)
  case result of
    Left err => map Left (bc.createFinalError (bc.context.workflowOf cmd) err)
    Right wfVal => do
      evVal <- bc.createWorkflowEvent cmd wfVal
      map Right (bc.createFinalEvent cmd evVal)
```

- Bounded Context computation lives in its monad
- Every workflow has its own monad, which must be embeddable to the monad of the bounded context
- Note the dependent pair and its use `(cmd ** cmdData) <- bc.createCommand contextCommand`

### Full architecture, explained

- [Order Taking Bounded Context](https://github.com/andorp/order-taking/blob/main/src/BoundedContext/OrderTaking.idr#L45)  
  Simple enum like ADTs to name commands, workflows, events
- [Place Order Workflow](https://github.com/andorp/order-taking/blob/main/src/BoundedContext/OrderTaking/Workflow/PlaceOrder/Overview.idr#L95)  
  Indexed datatype to represent workflow as state transition system.
- [Place Order DSL (Free Monad)](https://github.com/andorp/order-taking/blob/main/src/BoundedContext/OrderTaking/Workflow/PlaceOrder/Domain.idr#L455)  
  Detailed information in datatypes, building blocks of behaviour,  
  implementation of workflow steps based on building blocks.
- [Place Order Backend Monad](https://github.com/andorp/order-taking/blob/main/src/BoundedContext/OrderTaking/Workflow/PlaceOrder/Backend.idr#L185)  
  Model of the Place Order DSL, real implementation of the building blocks
- [Place Order Database Monads](https://github.com/andorp/order-taking/blob/main/src/BoundedContext/OrderTaking/Workflow/PlaceOrder/Database/Order.idr#L150)  
  Connect to external sources.
- [NodeJS Promise Monad](https://github.com/andorp/order-taking/blob/main/src/Service/NodeJS/Promise.idr#L6)  
  Make run everything with event driven approach of NodeJS.
- [NodeJS Runtime](https://github.com/andorp/order-taking/tree/main/src/Service/NodeJS)  
  Use third party libraries, such as HTTP, SQLite

## Dependent types in Action

Tools of dependently typed programming and their use in software.

Examples here are in pseudo Idris; quantities, correct implicit parameters are omitted.

### Extrinsic state transitions (mapping)

```idris
data Workflow
      :  (cmd : state -> state -> Type)
      -> (chk : state -> state -> state -> Type)
      -> state
      -> state
      -> Type
  where
    Do : cmd pre post -> Workflow cmd chk pre post
    Branch : chk pre branch1 branch2
           -> Workflow cmd chk branch1 post
           -> Workflow cmd chk branch2 post
           -> Workflow cmd chk pre post
    (>>)
      :  Workflow cmd chk pre mid
      -> Workflow cmd chk mid post
      -> Workflow cmd chk pre post
```

```idris
record Morphism (monad : Type -> Type) state (cmd : state -> state -> Type) (chk : state -> state -> state -> Type)
  where
    constructor MkMorphism
    StateType : state -> Type
    command   : cmd s e -> (StateType s) -> monad (StateType e)
    check     : chk s b1 b2 -> (StateType s) -> monad (Either (StateType b1) (StateType b2))
```

```idris
morph
  ...
  -> (r : Morphism monad state cmd chk)
  -> Workflow cmd chk start end
  -> (StateType r start) -> monad (StateType r end)
morph r w = ...
```

### Example of workflow morphism

```idris
StateType : Overview.State -> Type
StateType OrderForm          = Domain.OrderForm
StateType Order              = Either Domain.InvalidOrder Domain.Order
StateType ValidOrder         = Domain.Order
StateType PricedOrder        = Domain.PricedOrder
StateType InvalidOrder       = Domain.InvalidOrder
StateType InvalidOrderQueued = List Domain.PlacedOrderEvent
StateType OrderInfo          = List Domain.PlacedOrderEvent

step : Overview.Step s e -> (StateType s) -> PlaceOrderDSL (StateType e)
step ValidateOrder     st = validateOrder st
step AddInvalidOrder   st = pure [InvalidOrderRegistered st]
step PriceOrder        st = priceOrder st
step SendAckToCustomer st = do
  ack <- acknowledgeOrder st
  placePricedOrder st
  pure $ createEvents st ack
step SendInvalidOrder  st = pure st

check : Check s b1 b2 -> (StateType s) -> PlaceOrderDSL (Either (StateType b1) (StateType b2))
check CheckInvalidOrder st = pure st

public export
PlaceOrderMorphism : Morphism PlaceOrderDSL Overview.State Overview.Step Overview.Check
PlaceOrderMorphism = MkMorphism
  { StateType = StateType
  , step      = step
  , check     = check
  }
```

### Bounded Context Implementation

Encapsulation of types in records

```idris
record BoundedContext where
  constructor MkBoundedContext
  command     : Type
  workflow    : Type
  event       : Type
  workflowOf  : command -> workflow
  eventOf     : command -> event
```

Pieces of the workflow puzzle; a type safe approach

```idris
record BoundedContextImplementation (monad : Type -> Type) where
  constructor MkBoundedContextImplementation
  context
    : BoundedContext
  Workflow
    : context.Workflow -> WorkflowEnv
  ContextCommand
    : Type
  Command
    : context.Command -> Type
  ContextEvent
    : Type
  EventData
    : context.Event -> Type
  ContextError
    : Type
  ErrorData
    : context.Workflow -> Type
  WorkflowMonad
    : context.Workflow -> (Type -> Type)
  WorkflowMonadInstance
    : (w : context.Workflow) -> Monad (WorkflowMonad w)
  workflowMorphism
    : (cmd : context.Command) ->
      let w = context.workflowOf cmd
          d = Workflow w
      in Morphism (WorkflowMonad w) (State d) (WorkflowEnv.Command d) (Branch d)
  createWorkflowEmbedding
    : (cmd : context.Command) ->
      let w = context.workflowOf cmd
      in monad (Embedding (WorkflowMonad w) (ErrorData w) monad)
  createWorkflowEvent
    : (cmd : context.Command) ->
      let m = workflowMorphism cmd
      in m.StateType (WorkflowEnv.end (Workflow (context.workflowOf cmd))) -> monad (EventData (context.eventOf cmd))
  createFinalEvent
    : (cmd : context.Command) -> EventData (context.eventOf cmd) -> monad ContextEvent
  createCommand
    : ContextCommand -> monad (cmd : context.Command ** Command cmd)
  createStartState
    : (cmd : context.Command) -> Command cmd -> 
      let m = workflowMorphism cmd
      in monad (m.StateType (WorkflowEnv.start (Workflow (context.workflowOf cmd))))
  createFinalError
    : (w : context.Workflow) -> (ErrorData w) -> monad ContextError
```

Even encapsulate Monad instances

```idris
  WorkflowMonad
    : context.Workflow -> (Type -> Type)
  WorkflowMonadInstance
    : (w : context.Workflow) -> Monad (WorkflowMonad w)
```

### Example of workflow morphism (again)

```idris
StateType : Overview.State -> Type
StateType OrderForm          = Domain.OrderForm
StateType Order              = Either Domain.InvalidOrder Domain.Order
StateType ValidOrder         = Domain.Order
StateType PricedOrder        = Domain.PricedOrder
StateType InvalidOrder       = Domain.InvalidOrder
StateType InvalidOrderQueued = List Domain.PlacedOrderEvent
StateType OrderInfo          = List Domain.PlacedOrderEvent

step : Overview.Step s e -> (StateType s) -> PlaceOrderDSL (StateType e)
step ValidateOrder     st = validateOrder st
step AddInvalidOrder   st = pure [InvalidOrderRegistered st]
step PriceOrder        st = priceOrder st
step SendAckToCustomer st = do
  ack <- acknowledgeOrder st
  placePricedOrder st
  pure $ createEvents st ack
step SendInvalidOrder  st = pure st

check : Check s b1 b2 -> (StateType s) -> PlaceOrderDSL (Either (StateType b1) (StateType b2))
check CheckInvalidOrder st = pure st

public export
PlaceOrderMorphism : Morphism PlaceOrderDSL Overview.State Overview.Step Overview.Check
PlaceOrderMorphism = MkMorphism
  { StateType = StateType
  , step      = step
  , check     = check
  }
```

### Free Monadic DSL of a workflow

The Free Monad DSL allows us to easily replace the implementation. Idris is a multi-backend
compiler, with this approach the same solution can have multiple tech environments. Imagine
the same code deployed to NodeJS, Python, JVM, linux with ChezScheme.

Write the implementation in a Domain.

```idris
data PlaceOrderDSL : Type -> Type where
  Pure : a -> PlaceOrderDSL a
  Bind : PlaceOrderDSL a -> Inf (a -> PlaceOrderDSL b) -> PlaceOrderDSL b

  ThrowError : (a : Type) -> PlaceOrderError -> PlaceOrderDSL a
  CatchError : {a : Type} -> PlaceOrderDSL a -> PlaceOrderDSL (Either PlaceOrderError a)

  NewOrderId : PlaceOrderDSL OrderId
  NewOrderLineId : PlaceOrderDSL OrderLineId

  CheckProductCodeExists : ProductCode -> PlaceOrderDSL Bool
  CheckAddressExists     : AddressForm -> PlaceOrderDSL (Either CheckedAddressValidationError CheckedAddress)

  GetProductPrice  : ProductCode -> PlaceOrderDSL Price
  PlacePricedOrder : PricedOrder -> PlaceOrderDSL ()

  CreateOrderAcknowledgementLetter : PricedOrder          -> PlaceOrderDSL HtmlString
  SendOrderAcknowledgement         : OrderAcknowledgement -> PlaceOrderDSL AckSent
```

And model it with many backends...

```idris
record Model (m : Type -> Type) where
  constructor MkModel
  throwError
    : {a : Type} -> PlaceOrderError -> m a
  catchError
    : {a : Type} -> m a -> m (Either PlaceOrderError a)
  newOrderId
    : m OrderId
  newOrderLineId
    : m OrderLineId
  checkProductCodeExists
    : ProductCode -> m Bool
  checkAddressExists
    : AddressForm -> m (Either CheckedAddressValidationError CheckedAddress)
  getProductPrice
    : ProductCode -> m Price
  placePricedOrder
    : PricedOrder -> m ()
  createOrderAcknowledgementLetter
    : PricedOrder -> m HtmlString
  sendOrderAcknowledgement
    : OrderAcknowledgement -> m AckSent
```

```idris
interpret : Monad m => Model m -> PlaceOrderDSL a -> m a
interpret model (Pure x)                             = pure x
interpret model (Bind m k)                           = interpret model m >>= (interpret model . k)
interpret model (ThrowError _ x)                     = model.throwError x
interpret model (CatchError x)                       = model.catchError (interpret model x)
interpret model NewOrderId                           = model.newOrderId
interpret model NewOrderLineId                       = model.newOrderLineId
interpret model (CheckProductCodeExists x)           = model.checkProductCodeExists x
interpret model (CheckAddressExists x)               = model.checkAddressExists x
interpret model (GetProductPrice x)                  = model.getProductPrice x
interpret model (PlacePricedOrder x)                 = model.placePricedOrder x
interpret model (CreateOrderAcknowledgementLetter x) = model.createOrderAcknowledgementLetter x
interpret model (SendOrderAcknowledgement x)         = model.sendOrderAcknowledgement x
```

NOTE: Even datatypes could be abstracted, but here that was not necesary.

### Components

Type-safe non-leaky abstraction of components; everything is closed with dependent records.

```idris
record EmailComp where
  constructor MkEmailComp
  emailError  : Type
  showError   : emailError -> String
  serviceInfo : ServiceInfo
  send        : EmailAddress -> HtmlString -> Promise (Maybe emailError)
```

```idris
record OrderDBComp where
  constructor MkOrderDBComp
  dbConnection        : Type 
  dbError             : Type
  showDBError         : dbError -> String
  initConnection      : Promise (Either dbError dbConnection)
  closeConnection     : dbConnection -> Promise (Maybe dbError)
  beginTransaction    : dbConnection -> Promise (Maybe dbError)
  commitTransaction   : dbConnection -> Promise (Maybe dbError)
  rollbackTransaction : dbConnection -> Promise (Maybe dbError)
  saveOrder           : dbConnection -> PricedOrderDTO -> Promise (Maybe dbError)
```

### Dependency injection with implicit parameters

```idris
record Dependencies where
  constructor MkDependencies
  md5Provider       : MD5
  orderDBComp       : OrderDBComp
  orderDBConn       : orderDBComp.dbConnection
  productDBComp     : ProductDBComp
  productDBConn     : productDBComp.dbConnection
  emailComp         : EmailComp
  checkAddressComp  : CheckAddressComp
```

```idris
mkRunBackend
  :  (orderDBComp       : OrderDBComp)
  => (productDBComp     : ProductDBComp)
  => (emailComp         : EmailComp)
  => (checkAddressComp  : CheckAddressComp)
  => HasIO io
  => io RunBackend
mkRunBackend = ...
```

```idris
createWorkflowEmbedding
  :  (cmd : Command)
  -> Promise (Embedding (workflowMonad (workflowOf cmd)) (errorDomainType (workflowOf cmd)) Promise)
createWorkflowEmbedding PlaceOrder = do
  let orderDBComp       = orderDBSQLite
  let productDBComp     = productDBSQlite
  let emailComp         = noEmail
  let checkAddressComp  = okCheckAddress
  rb <- mkRunBackend
  pure $ MkEmbedding (\type, x => map (the (Either PlaceOrderError type)) (runBackend rb (interpret backend x)))
```

```idris
data Embedding : (from : Type -> Type) -> (err : Type) -> (to : Type -> Type) -> Type where
  MkEmbedding : ((a : Type) -> from a -> to (Either err a)) -> Embedding from err to

runEmbedding : {a : Type} -> Embedding f e t -> f a -> t (Either e a)
runEmbedding (MkEmbedding f) y = f a y
```

### Type safe SQL commands

```idris
record Table where
  constructor MkTable
  name         : TableName
  fields       : List Field
  constraints  : List Constraint
  0 validTable : ValidTable fields constraints
```

```idris
-- Leaves out autoincrement fields
InsertValues : List Field -> List Type

data Command : Type where
  CreateTable
    :  (table : Table)
    -> Command
  Insert
    :  (table : Table)
    -> (values : HList (InsertValues table.fields))
    -> Command
```

```idris
productTable = MkTable
  "product"
  [ field "id"          SQL_Integer [PrimaryKey, AutoIncrement]
  , field "code"        SQL_Text    [NotNull]
  , field "description" SQL_Text    [NotNull]
  , field "price"       SQL_Double  [NotNull]
  ]
  [ Unique "code_unique" ["code"] ]
  YesOfCourseValid
```

```idris
Insert productTable
  [ FieldOf "code"        (SQLText productCode)
  , FieldOf "description" (SQLText description)
  , FieldOf "price"       (SQLDouble price)
  ]
```

### Type safe SQL queries

```idris
data Query : Type where
  Select
    :  (  fields    : List FieldName)
    -> (  table     : Table)
    -> (1 okFields  : SelectedFieldsDefinedInTable fields table.fields)
    => (  filters   : List (FieldName, String, String))
    -> (0 okFilters : FilteredFieldsDefinedInTable filters table.fields)
```

```idris
Select ["code", "description", "price"] productTable [("code", "=", "'\{productCode}'")]
```

### JSON Schema

```idris
data Presence = Optional | Required

data Schema
  = Null
  | Boolean
  | Number
  | Str
  | Array  (List Schema)
  | Object (String, Presence, Schema)
  | Either Schema Schema
```

```idris
data Field : (String, Presence, Schema) -> Type where
  RequiredField : {f : String} ->         JSON s -> Field (f,Required,s)
  OptionalField : {f : String} -> Maybe (JSON s) -> Field (f,Optional,s)
```

```idris
data JSON : Schema -> Type where
  JNull    :                                        JSON Null
  JBoolean : Bool                                -> JSON Boolean
  JNumber  : Double                              -> JSON Number
  JString  : String                              -> JSON Str
  JArray   : {xs : List Schema}  -> All JSON xs  -> JSON (Array xs)
  JObject  : {xs : FieldList}    -> All Field xs -> JSON (Object xs)
  JLeft    : {l  : Schema}       -> JSON l       -> JSON (Either l r)
  JRight   : {r  : Schema}       -> JSON r       -> JSON (Either l r)
```

### Postfix notation for OO feel

```idris
(.setHeader)     : Response -> String -> String -> IO ()
(.setStatusCode) : Response -> Int              -> IO ()
(.end)           : Response -> String           -> IO ()

rsp.setHeader "Content-Type" "application/json"
rsp.setHeader "Access-Control-Allow-Origin" "*"
rsp.setStatusCode 400
rsp.end "{\"message\":\"Couldn't parse incoming JSON.\"}"
```

### Dynamically typed programming

Idris as strong that it can simulate JavaScript dynamic types, with matching on Types.

```idris
renderFieldValue : {t : Type} -> t -> String
renderFieldValue {t=FieldOfTy n s} (FieldOf _ x) = renderFieldValue x
renderFieldValue {t=Maybe (SQLValue s)} (Just x) = renderFieldValue x
renderFieldValue {t=Maybe (SQLValue s)} Nothing  = "NULL"
renderFieldValue {t=SQLValue s} x = renderSQLValue x
renderFieldValue _ = "(╯°□°)╯︵ ┻━┻" -- This shouldn't happen

renderInsertNames : List Field -> List String

renderCommand (Insert table values)
  = "INSERT INTO \{table.name} (\{withCommas (renderInsertNames table.fields)}) VALUES (\{withCommas (renderInsertValues values)})"
```

Forgot this line:
```idris
renderFieldValue {t=FieldOfTy n s} (FieldOf _ x) = renderFieldValue x
```

Called this:
```idris
Insert productTable
  [ FieldOf "code"        (SQLText productCode)
  , FieldOf "description" (SQLText description)
  , FieldOf "price"       (SQLDouble price)
  ]
```

and got this in the logs:
```
INSERT INTO productTable (...) VALUES ((╯°□°)╯︵ ┻━┻, (╯°□°)╯︵ ┻━┻, (╯°□°)╯︵ ┻━┻)
```

## QED :)
```

## File: `VERSIONS`
```
Idris2: 0.5.1-f078d5f5d
NodeJS: v12.21.0
Svelte: 3.38.2
```

## File: `order-taking-service.ipkg`
```
package order-taking-service

depends = contrib, network

opts = "profile"

sourcedir = "src"

main = OrderTakingService
executable = order-taking-service
```

## File: `package.json`
```json
{
  "dependencies": {
    "google-closure-compiler": "^20210505.0.0",
    "md5": "^2.3.0",
    "sqlite": "^4.0.22",
    "sqlite3": "^5.0.2",
    "sqlite3-promisify": "^1.0.2"
  }
}
```

## File: `talks`
```
ITT 2018 - Jakub Nabrdalik - Hexagonal Architecture in practice
https://www.youtube.com/watch?v=sOaS83Ir8Ck

```

## File: `client/svelte-client/.gitignore`
```
/node_modules/
/public/build/

.DS_Store
```

## File: `client/svelte-client/README.md`
```markdown
*Looking for a shareable component template? Go here --> [sveltejs/component-template](https://github.com/sveltejs/component-template)*

---

# svelte app

This is a project template for [Svelte](https://svelte.dev) apps. It lives at https://github.com/sveltejs/template.

To create a new project based on this template using [degit](https://github.com/Rich-Harris/degit):

```bash
npx degit sveltejs/template svelte-app
cd svelte-app
```

*Note that you will need to have [Node.js](https://nodejs.org) installed.*


## Get started

Install the dependencies...

```bash
cd svelte-app
npm install
```

...then start [Rollup](https://rollupjs.org):

```bash
npm run dev
```

Navigate to [localhost:5000](http://localhost:5000). You should see your app running. Edit a component file in `src`, save it, and reload the page to see your changes.

By default, the server will only respond to requests from localhost. To allow connections from other computers, edit the `sirv` commands in package.json to include the option `--host 0.0.0.0`.

If you're using [Visual Studio Code](https://code.visualstudio.com/) we recommend installing the official extension [Svelte for VS Code](https://marketplace.visualstudio.com/items?itemName=svelte.svelte-vscode). If you are using other editors you may need to install a plugin in order to get syntax highlighting and intellisense.

## Building and running in production mode

To create an optimised version of the app:

```bash
npm run build
```

You can run the newly built app with `npm run start`. This uses [sirv](https://github.com/lukeed/sirv), which is included in your package.json's `dependencies` so that the app will work when you deploy to platforms like [Heroku](https://heroku.com).


## Single-page app mode

By default, sirv will only respond to requests that match files in `public`. This is to maximise compatibility with static fileservers, allowing you to deploy your app anywhere.

If you're building a single-page app (SPA) with multiple routes, sirv needs to be able to respond to requests for *any* path. You can make it so by editing the `"start"` command in package.json:

```js
"start": "sirv public --single"
```

## Using TypeScript

This template comes with a script to set up a TypeScript development environment, you can run it immediately after cloning the template with:

```bash
node scripts/setupTypeScript.js
```

Or remove the script via:

```bash
rm scripts/setupTypeScript.js
```

## Deploying to the web

### With [Vercel](https://vercel.com)

Install `vercel` if you haven't already:

```bash
npm install -g vercel
```

Then, from within your project folder:

```bash
cd public
vercel deploy --name my-project
```

### With [surge](https://surge.sh/)

Install `surge` if you haven't already:

```bash
npm install -g surge
```

Then, from within your project folder:

```bash
npm run build
surge public my-project.surge.sh
```
```

## File: `client/svelte-client/package.json`
```json
{
  "name": "svelte-app",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "build": "rollup -c",
    "dev": "rollup -c -w",
    "start": "sirv public --no-clear"
  },
  "devDependencies": {
    "@rollup/plugin-commonjs": "^17.0.0",
    "@rollup/plugin-node-resolve": "^11.0.0",
    "rollup": "^2.3.4",
    "rollup-plugin-css-only": "^3.1.0",
    "rollup-plugin-livereload": "^2.0.0",
    "rollup-plugin-svelte": "^7.0.0",
    "rollup-plugin-terser": "^7.0.0",
    "svelte": "^3.0.0"
  },
  "dependencies": {
    "sirv-cli": "^1.0.0"
  }
}
```

## File: `client/svelte-client/rollup.config.js`
```javascript
import svelte from 'rollup-plugin-svelte';
import commonjs from '@rollup/plugin-commonjs';
import resolve from '@rollup/plugin-node-resolve';
import livereload from 'rollup-plugin-livereload';
import { terser } from 'rollup-plugin-terser';
import css from 'rollup-plugin-css-only';

const production = !process.env.ROLLUP_WATCH;

function serve() {
	let server;

	function toExit() {
		if (server) server.kill(0);
	}

	return {
		writeBundle() {
			if (server) return;
			server = require('child_process').spawn('npm', ['run', 'start', '--', '--dev'], {
				stdio: ['ignore', 'inherit', 'inherit'],
				shell: true
			});

			process.on('SIGTERM', toExit);
			process.on('exit', toExit);
		}
	};
}

export default {
	input: 'src/main.js',
	output: {
		sourcemap: true,
		format: 'iife',
		name: 'app',
		file: 'public/build/bundle.js'
	},
	plugins: [
		svelte({
			compilerOptions: {
				// enable run-time checks when not in production
				dev: !production
			}
		}),
		// we'll extract any component CSS out into
		// a separate file - better for performance
		css({ output: 'bundle.css' }),

		// If you have external dependencies installed from
		// npm, you'll most likely need these plugins. In
		// some cases you'll need additional configuration -
		// consult the documentation for details:
		// https://github.com/rollup/plugins/tree/master/packages/commonjs
		resolve({
			browser: true,
			dedupe: ['svelte']
		}),
		commonjs(),

		// In dev mode, call `npm run start` once
		// the bundle has been generated
		!production && serve(),

		// Watch the `public` directory and refresh the
		// browser on changes when not in production
		!production && livereload('public'),

		// If we're building for production (npm run build
		// instead of npm run dev), minify
		production && terser()
	],
	watch: {
		clearScreen: false
	}
};
```

## File: `client/svelte-client/public/global.css`
```css
html, body {
	position: relative;
	width: 100%;
	height: 100%;
}

body {
	color: #333;
	margin: 0;
	padding: 8px;
	box-sizing: border-box;
	font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif;
}

a {
	color: rgb(0,100,200);
	text-decoration: none;
}

a:hover {
	text-decoration: underline;
}

a:visited {
	color: rgb(0,80,160);
}

label {
	display: block;
}

input, button, select, textarea {
	font-family: inherit;
	font-size: inherit;
	-webkit-padding: 0.4em 0;
	padding: 0.4em;
	margin: 0 0 0.5em 0;
	box-sizing: border-box;
	border: 1px solid #ccc;
	border-radius: 2px;
}

input:disabled {
	color: #ccc;
}

button {
	color: #333;
	background-color: #f4f4f4;
	outline: none;
}

button:disabled {
	color: #999;
}

button:not(:disabled):active {
	background-color: #ddd;
}

button:focus {
	border-color: #666;
}
```

## File: `client/svelte-client/public/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset='utf-8'>
	<meta name='viewport' content='width=device-width,initial-scale=1'>

	<title>Svelte app</title>

	<link rel='icon' type='image/png' href='/favicon.png'>
	<link rel='stylesheet' href='/global.css'>
	<link rel='stylesheet' href='/build/bundle.css'>

	<script defer src='/build/bundle.js'></script>
</head>

<body>
</body>
</html>
```

## File: `client/svelte-client/scripts/setupTypeScript.js`
```javascript
// @ts-check

/** This script modifies the project to support TS code in .svelte files like:

  <script lang="ts">
  	export let name: string;
  </script>
 
  As well as validating the code for CI.
  */

/**  To work on this script:
  rm -rf test-template template && git clone sveltejs/template test-template && node scripts/setupTypeScript.js test-template
*/

const fs = require("fs")
const path = require("path")
const { argv } = require("process")

const projectRoot = argv[2] || path.join(__dirname, "..")

// Add deps to pkg.json
const packageJSON = JSON.parse(fs.readFileSync(path.join(projectRoot, "package.json"), "utf8"))
packageJSON.devDependencies = Object.assign(packageJSON.devDependencies, {
  "svelte-check": "^2.0.0",
  "svelte-preprocess": "^4.0.0",
  "@rollup/plugin-typescript": "^8.0.0",
  "typescript": "^4.0.0",
  "tslib": "^2.0.0",
  "@tsconfig/svelte": "^2.0.0"
})

// Add script for checking
packageJSON.scripts = Object.assign(packageJSON.scripts, {
  "check": "svelte-check --tsconfig ./tsconfig.json"
})

// Write the package JSON
fs.writeFileSync(path.join(projectRoot, "package.json"), JSON.stringify(packageJSON, null, "  "))

// mv src/main.js to main.ts - note, we need to edit rollup.config.js for this too
const beforeMainJSPath = path.join(projectRoot, "src", "main.js")
const afterMainTSPath = path.join(projectRoot, "src", "main.ts")
fs.renameSync(beforeMainJSPath, afterMainTSPath)

// Switch the app.svelte file to use TS
const appSveltePath = path.join(projectRoot, "src", "App.svelte")
let appFile = fs.readFileSync(appSveltePath, "utf8")
appFile = appFile.replace("<script>", '<script lang="ts">')
appFile = appFile.replace("export let name;", 'export let name: string;')
fs.writeFileSync(appSveltePath, appFile)

// Edit rollup config
const rollupConfigPath = path.join(projectRoot, "rollup.config.js")
let rollupConfig = fs.readFileSync(rollupConfigPath, "utf8")

// Edit imports
rollupConfig = rollupConfig.replace(`'rollup-plugin-terser';`, `'rollup-plugin-terser';
import sveltePreprocess from 'svelte-preprocess';
import typescript from '@rollup/plugin-typescript';`)

// Replace name of entry point
rollupConfig = rollupConfig.replace(`'src/main.js'`, `'src/main.ts'`)

// Add preprocessor
rollupConfig = rollupConfig.replace(
  'compilerOptions:',
  'preprocess: sveltePreprocess({ sourceMap: !production }),\n\t\t\tcompilerOptions:'
);

// Add TypeScript
rollupConfig = rollupConfig.replace(
  'commonjs(),',
  'commonjs(),\n\t\ttypescript({\n\t\t\tsourceMap: !production,\n\t\t\tinlineSources: !production\n\t\t}),'
);
fs.writeFileSync(rollupConfigPath, rollupConfig)

// Add TSConfig
const tsconfig = `{
  "extends": "@tsconfig/svelte/tsconfig.json",

  "include": ["src/**/*"],
  "exclude": ["node_modules/*", "__sapper__/*", "public/*"]
}`
const tsconfigPath =  path.join(projectRoot, "tsconfig.json")
fs.writeFileSync(tsconfigPath, tsconfig)

// Add global.d.ts
const dtsPath =  path.join(projectRoot, "src", "global.d.ts")
fs.writeFileSync(dtsPath, `/// <reference types="svelte" />`)

// Delete this script, but not during testing
if (!argv[2]) {
  // Remove the script
  fs.unlinkSync(path.join(__filename))

  // Check for Mac's DS_store file, and if it's the only one left remove it
  const remainingFiles = fs.readdirSync(path.join(__dirname))
  if (remainingFiles.length === 1 && remainingFiles[0] === '.DS_store') {
    fs.unlinkSync(path.join(__dirname, '.DS_store'))
  }

  // Check if the scripts folder is empty
  if (fs.readdirSync(path.join(__dirname)).length === 0) {
    // Remove the scripts folder
    fs.rmdirSync(path.join(__dirname))
  }
}

// Adds the extension recommendation
fs.mkdirSync(path.join(projectRoot, ".vscode"), { recursive: true })
fs.writeFileSync(path.join(projectRoot, ".vscode", "extensions.json"), `{
  "recommendations": ["svelte.svelte-vscode"]
}
`)

console.log("Converted to TypeScript.")

if (fs.existsSync(path.join(projectRoot, "node_modules"))) {
  console.log("\nYou will need to re-run your dependency manager to get started.")
}
```

## File: `client/svelte-client/src/Address.svelte`
```
<script>
  import { createEventDispatcher } from 'svelte';
  import { getIdentifier } from './client.js';

  export let addressLine1 = "L1";
  export let addressLine2 = "";
  export let addressLine3 = "";
  export let addressLine4 = "";
  export let city = "";
  export let postCode = "";

  const dispatch = createEventDispatcher();

  async function addressChange() {
    const identifier = await getIdentifier();
    dispatch('addressChange', {
      identifier: identifier,
      addressLine1: addressLine1,
      addressLine2: addressLine2,
      addressLine3: addressLine3,
      addressLine4: addressLine4,
      city: city,
      zipCode: postCode
    });
  }
</script>

<div on:change="{addressChange}">
  <h2>Address</h2>
  <div>
    <label for="addressLine1">AddressLine 1</label>
    <input type="text" id="addressLine1" bind:value="{addressLine1}"/>
  </div>
  <div>
    <label for="addressLine2">AddressLine 2</label>
    <input type="text" id="addressLine2" bind:value="{addressLine2}"/>
  </div>
  <div>
    <label for="addressLine3">AddressLine 3</label>
    <input type="text" id="addressLine3" bind:value="{addressLine3}"/>
  </div>
  <div>
    <label for="addressLine4">AddressLine 4</label>
    <input type="text" id="addressLine4" bind:value="{addressLine4}"/>
  </div>
  <div>
    <label for="city">City</label>
    <input type="text" id="city" bind:value="{city}"/>
  </div>
  <div>
    <label for="postcode">Post code</label>
    <input type="text" id="postcode" bind:value="{postCode}"/>
  </div>
</div>
```

## File: `client/svelte-client/src/App.svelte`
```
<script>
	import OrderTaking from './OrderTaking.svelte'
</script>

<main>
	<OrderTaking/>
</main>
```

## File: `client/svelte-client/src/Button.svelte`
```
<button on:click>
  <slot/>
</button>
```

## File: `client/svelte-client/src/Customer.svelte`
```
<script>
  import { createEventDispatcher } from 'svelte';
  import { getIdentifier } from './client.js';
  export let firstName    = '';
  export let lastName     = '';
  export let emailAddress = '';

  const dispatch = createEventDispatcher();

  async function customerChange() {
    const identifier = await getIdentifier();
    dispatch('customerChange', {
      identifier: identifier,
      firstName: firstName,
      lastName: lastName,
      emailAddress: emailAddress
    });
  }
</script>

<div on:change="{customerChange}">
  <p>Customer</p>
  <label for="firstName">First Name</label>
  <input id="firstName" type="text" bind:value="{firstName}"/>
  <label for="lastName">Last Name</label>
  <input id="lastName" type="text" bind:value="{lastName}"/>
  <label for="emailAddress">Email Address</label>
  <input id="emailAddress" type="email" bind:value="{emailAddress}">
</div>
```

## File: `client/svelte-client/src/OrderLine.svelte`
```
<script>
  export let productCode = '';
  export let quantity = '';
</script>

<style>
</style>

<div>
  <p>{productCode}</p>
  <p>{quantity}</p>
</div>
```

## File: `client/svelte-client/src/OrderTaking.svelte`
```
<script>
  import { getIdentifier } from './client.js'
  import { postData } from './postdata.js'
  import OrderLine from './OrderLine.svelte'
  import Address   from './Address.svelte'
  import Customer  from './Customer.svelte'
  import Button    from './Button.svelte'

  let shippingAddressSameAsAddress = true;
  let customer = {};
  let billingAddress = {};
  let shippingAddress = {};
  let orderLines = [];
  let order = {};

  async function submitOrder() {
    let command = {
      "tag": "PlaceOrderCmdDTO",
      "value": order
    };
    let data = await postData('http://localhost:3000/order-taking', command);
    console.log('submitOrder response: ' + JSON.stringify(data));
  }

  async function updateOrder() {
    const identifier = await getIdentifier();
    order = {
      identifier: identifier,
      customer: customer,
      billingAddress: billingAddress,
      shippingAddress: shippingAddress,
      orderLines: orderLines,
    };
    console.log(JSON.stringify(order));
  }

  let productCode = '';
  let quantity = '';
  async function addOrderLine() {
    const identifier = await getIdentifier();
    const orderLine = {
      identifier: identifier,
      productCode: productCode,
      quantity: quantity
    };
    orderLines = orderLines.concat(orderLine);
    updateOrder();
  }

  function changeShippingSameAsAddress() {
    if (shippingAddressSameAsAddress === true) {
      shippingAddress = billingAddress;
    }
  }

  async function addressChange(event) {
    billingAddress = event.detail;
    changeShippingSameAsAddress();
    updateOrder();
  }

  // function shippingAddressChange(event) {
  //   shippingAddress = event.detail;
  //   console.log("shippingAddressChange " + JSON.stringify(shippingAddress));
  // }

  async function customerChange(event) {
    customer = event.detail;
    updateOrder();
  }
</script>

<div>
  <h1>Order Taking</h1>
  <Customer on:customerChange={customerChange}/>
  <Address on:addressChange={addressChange}/>
  <!-- <label for="shippingAddressSameAsAddress">Same as billingAddress.</label>
  <input id="shippingAddressSameAsAddress" type="checkbox" bind:value="{shippingAddressSameAsAddress}"/>
  {#if (shippingAddressSameAsAddress === false)}
    <h2>Shipping billingAddress</h2>
    <Address on:addressChange={shippingAddressChange}/>
  {/if} -->
  <div>
    <label for="productCode">Product code:</label>
    <input id="productCode" type="text" bind:value="{productCode}"/>
    <label for="quantity">Quantity:</label>
    <input id="quantity" type="text" bind:value="{quantity}"/>
    <Button on:click="{addOrderLine}">Add product</Button>
  </div>
  {#if orderLines.length === 0}
    <p>No orders were added yet.</p>
  {:else}
    {#each orderLines as orderLine}
      <OrderLine productCode={orderLine.productCode} quantity={orderLine.quantity}/>
    {/each}
  {/if}
  <Button on:click="{submitOrder}">Submit Order</Button>
</div>
```

## File: `client/svelte-client/src/client.js`
```javascript

export async function getIdentifier() {
  return new Promise((resolve, reject) => resolve(String(Math.random())));
}
```

## File: `client/svelte-client/src/main.js`
```javascript
import App from './App.svelte';

const app = new App({
	target: document.body
});

export default app;
```

## File: `client/svelte-client/src/postdata.js`
```javascript
export async function postData(url = '', data = {}) {
  const response = await fetch(url, {
    method: 'POST',
    cache: 'no-cache',
    body: JSON.stringify(data)
  });
  return response.json();
}
```

## File: `src/OrderTakingService.idr`
```
module OrderTakingService

import System
import Language.JSON

import Service.NodeJS.HTTP
import Service.NodeJS.Promise

import Rango.DataTransfer.JSON.Interfaces
import Rango.BoundedContext.BoundedContext

import BoundedContext.OrderTaking
import BoundedContext.OrderTaking.DTO
import BoundedContext.OrderTaking.ConvertDTO
import BoundedContext.OrderTaking.Workflow.PlaceOrder.Database.Order
import BoundedContext.OrderTaking.Workflow.PlaceOrder.Database.Product

-- Although this is the main entry for the Order Taking Service, this is module is more like scaffolding
-- for the implementation of the Bounded Context idea.
-- Scaffolding because this module either initializes the SQLlite databases for the service
-- or starts the service instanciating an HTTP server with one attached listener, but
-- no depedently typed programming was applied here. The minimum requirements are implemented
-- to be able to accept a request from a client, grab the JSON from the body, and turn that
-- JSON value to a Command of the Order Taking service. The 'handleCommand' is the real
-- entry point for the real abstraction.

handleCommand : Command.OrderTaking -> Promise (Either Error.OrderTaking Event.OrderTaking)
handleCommand = BoundedContext.execute orderTakingContext

-- Scaffolding of getting the JSON and the Command out of the request, execute the command in
-- the OrderTaking Bounded Context and render the result JSON from the Event data coming
-- from the Bounded Context.
orderTakingHandler : Request -> Response -> IO ()
orderTakingHandler req rsp =
  resolve' (\_ => pure ()) (\err => putStrLn $ "Unhandled error has happened: \{err}") $ do
    -- Extract data from request.
    rsp.setHeader "Content-Type" "application/json"
    rsp.setHeader "Access-Control-Allow-Origin" "*"
    content <- req.body
    putStrLn content
    let Just jsValue = JSON.parse content
        | Nothing => do
            putStrLn "Couldn't parse incoming JSON."
            rsp.setStatusCode 400
            rsp.end "{\"message\":\"Couldn't parse incoming JSON.\"}"
    Just cmd <- the (Promise (Maybe Command.OrderTaking))
              $ case Request.url req of
                  "/order-taking" => do
                    let Just commandDTO = the (Maybe CommandDTO) (fromJSON jsValue)
                        | Nothing => do
                            putStrLn "Couldn't parse JSValue."
                            rsp.setStatusCode 400
                            rsp.end "{\"message\":\"Couldn't parse Command DTO JSON.\"}"
                            pure Nothing
                    pure $ Just $ fromCommandDTO commandDTO
                  path  => do
                    rsp.setStatusCode 400
                    rsp.end $ "{\"message\":\"Unknown API endpoint: \{path} \"}"
                    pure Nothing
      | Nothing => pure ()
    -- Execute the learnt command.
    result <- handleCommand cmd
    -- Render the result response.
    case result of
      Left err => do
        rsp.setStatusCode 400
        rsp.end $ format 0 $ JObject
          [ ("message", JString "There was a placed order error.")
          , ("order-event-error", toJSON $ toErrorDTO err)
          ]
      Right ev => do
        rsp.setStatusCode 200
        rsp.end $ format 0 $ toJSON $ toEventDTO ev

startService : IO ()
startService = do
  putStrLn "Staring Order taking service."
  http   <- HTTP.require
  server <- http.createServer orderTakingHandler
  server.listen 3000 "127.0.0.1"

initDB : IO ()
initDB = do
  BoundedContext.OrderTaking.Workflow.PlaceOrder.Database.Order.initDB 
  BoundedContext.OrderTaking.Workflow.PlaceOrder.Database.Product.initDB

main : IO ()
main = do
  args <- getArgs
  printLn args
  if "--init-db" `elem` args
    then OrderTakingService.initDB
    else startService
```

## File: `src/BoundedContext/OrderTaking.idr`
```
module BoundedContext.OrderTaking

import public BoundedContext.OrderTaking.Error
import public BoundedContext.OrderTaking.Event
import public BoundedContext.OrderTaking.Command

import BoundedContext.OrderTaking.Workflow.PlaceOrder
import BoundedContext.OrderTaking.Workflow.PlaceOrder.Backend

import Rango.BoundedContext.BoundedContext
import Service.NodeJS.Promise


namespace Overview

  namespace C

    public export
    data Command
      = PlaceOrder

  namespace W

    public export
    data Workflow
      = PlaceOrder

  namespace E

    public export
    data Event
      = PlaceOrder

  public export
  workflowOf : Command -> Workflow
  workflowOf PlaceOrder = PlaceOrder

  public export
  eventOf : Command -> E.Event
  eventOf PlaceOrder = PlaceOrder

namespace Implementation

  public export
  orderTaking : BoundedContext
  orderTaking = MkBoundedContext
    { Command     = Command
    , Workflow    = Workflow
    , Event       = Event
    , workflowOf  = workflowOf
    , eventOf     = eventOf
    }

  WorkflowEntry : W.Workflow -> Type
  WorkflowEntry PlaceOrder = OrderForm

  EventDomainType : E.Event -> Type
  EventDomainType PlaceOrder = List PlacedOrderEvent

  workflowContexts : W.Workflow -> WorkflowEnv
  workflowContexts PlaceOrder = mkWorkflowEnv PlaceOrder.Overview.workflow

  WorkflowMonad : W.Workflow -> (Type -> Type)
  WorkflowMonad PlaceOrder = PlaceOrderDSL

  ErrorDomainType : W.Workflow -> Type
  ErrorDomainType PlaceOrder = PlaceOrderError

  createWorkflowEmbedding
    :  (cmd : Command)
    -> Promise (Embedding (WorkflowMonad (workflowOf cmd)) (ErrorDomainType (workflowOf cmd)) Promise)
  createWorkflowEmbedding PlaceOrder = do
    let orderDBComp       = orderDBSQLite
    let productDBComp     = productDBSQlite
    let emailComp         = noEmail
    let checkAddressComp  = okCheckAddress
    rb <- mkRunBackend
    pure $ MkEmbedding (\type, x => map (the (Either PlaceOrderError type)) (runBackend rb (interpret backend x)))

  workflowMorphism
    :  (cmd : Command)
    -> let w = workflowOf cmd
       in Morphism
            (WorkflowMonad w)
            (WorkflowEnv.state (workflowContexts (w)))
            (WorkflowEnv.Command (workflowContexts w))
            (WorkflowEnv.Branch (workflowContexts w))
  workflowMorphism PlaceOrder = PlaceOrderMorphism
 
  transformWorkflowResult
    :  (cmd : Command)
    -> let m = workflowMorphism cmd
       in m.StateType (WorkflowEnv.end (workflowContexts (workflowOf cmd))) -> Promise (EventDomainType (eventOf cmd))
  transformWorkflowResult PlaceOrder x = pure x

  transformEvent : (cmd : Command) -> EventDomainType (eventOf cmd) -> Promise Event.OrderTaking
  transformEvent PlaceOrder x = pure $ PlaceOrder x

  createCommand : Command.OrderTaking -> Promise (cmd : Command ** WorkflowEntry (workflowOf cmd))
  createCommand (PlaceOrder x) = pure (PlaceOrder ** x)

  transformError
    :  (wf : Workflow)
    -> ErrorDomainType wf -> Promise Error.OrderTaking
  transformError PlaceOrder x = pure (PlaceOrder x)

  createStartState
    :  (cmd : Command)
    -> WorkflowEntry (workflowOf cmd) -> Promise ((workflowMorphism cmd).StateType ((workflowContexts (workflowOf cmd)).start))
  createStartState PlaceOrder x = pure x

  WorkflowMonadInstance : (w : Workflow) -> Monad (WorkflowMonad w)
  WorkflowMonadInstance PlaceOrder = %search

  public export
  orderTakingContext : BoundedContextImplementation Promise
  orderTakingContext = MkBoundedContextImplementation
    { context                 = orderTaking
    , Workflow                = workflowContexts
    , ContextCommand          = Command.OrderTaking
    , WorkflowEntry           = WorkflowEntry
    , ContextEvent            = Event.OrderTaking
    , EventData               = EventDomainType
    , ContextError            = Error.OrderTaking
    , ErrorData               = ErrorDomainType
    , WorkflowMonad           = WorkflowMonad
    , WorkflowMonadInstance   = WorkflowMonadInstance
    , workflowMorphism        = workflowMorphism
    , createWorkflowEmbedding = createWorkflowEmbedding
    , transformWorkflowResult = transformWorkflowResult
    , transformEvent          = transformEvent
    , createCommand           = createCommand
    , createStartState        = createStartState
    , transformError          = transformError
    }
```

## File: `src/BoundedContext/OrderTaking/Command.idr`
```
module BoundedContext.OrderTaking.Command

import BoundedContext.OrderTaking.Workflow.PlaceOrder.Domain

public export
data OrderTaking
  = PlaceOrder OrderForm

```

## File: `src/BoundedContext/OrderTaking/ConvertDTO.idr`
```
module BoundedContext.OrderTaking.ConvertDTO

import BoundedContext.OrderTaking.DTO
import BoundedContext.OrderTaking.Command
import BoundedContext.OrderTaking.Error
import BoundedContext.OrderTaking.Event

import BoundedContext.OrderTaking.Workflow.PlaceOrder.Domain
import BoundedContext.OrderTaking.Workflow.PlaceOrder.DTO
import BoundedContext.OrderTaking.Workflow.PlaceOrder.ConvertDTO

export
toErrorDTO : Error.OrderTaking -> ErrorDTO
toErrorDTO (PlaceOrder x) = PlaceOrderErrorDTO $ toPlacedOrderErrorDTO x

export
toEventDTO : Event.OrderTaking -> EventDTO
toEventDTO (PlaceOrder xs) = PlaceOrderEventDTO $ map toPlaceOrderEventDTO xs

export
fromCommandDTO : CommandDTO -> Command.OrderTaking
fromCommandDTO (PlaceOrderCmdDTO x) = PlaceOrder (orderForm x)
```

## File: `src/BoundedContext/OrderTaking/DTO.idr`
```
module BoundedContext.OrderTaking.DTO

import BoundedContext.OrderTaking.Workflow.PlaceOrder.DTO

import Rango.DataTransfer.JSON.Derive

%language ElabReflection
%default total


public export
data ErrorDTO
  = PlaceOrderErrorDTO PlaceOrderErrorDTO

public export
data EventDTO
  = PlaceOrderEventDTO (List PlaceOrderEventDTO)

public export
data CommandDTO
  = PlaceOrderCmdDTO OrderFormDTO

export
ToJSON ErrorDTO where
  toJSON (PlaceOrderErrorDTO x) = constructorToJSON "PlaceOrderErrorDTO" x

export
ToJSON EventDTO where
  toJSON (PlaceOrderEventDTO x) = constructorToJSON "PlaceOrderEventDTO" x

export
FromJSON CommandDTO where
  fromJSON = constructorFromJSON "PlaceOrderCmdDTO" PlaceOrderCmdDTO
```

## File: `src/BoundedContext/OrderTaking/Error.idr`
```
module BoundedContext.OrderTaking.Error

import BoundedContext.OrderTaking.Workflow.PlaceOrder.Domain

public export
data OrderTaking
  = PlaceOrder PlaceOrderError

```

## File: `src/BoundedContext/OrderTaking/Event.idr`
```
module BoundedContext.OrderTaking.Event

import BoundedContext.OrderTaking.Workflow.PlaceOrder.Domain

public export
data OrderTaking
  = PlaceOrder (List PlacedOrderEvent)
```

## File: `src/BoundedContext/OrderTaking/Workflow/PlaceOrder.idr`
```
module BoundedContext.OrderTaking.Workflow.PlaceOrder

import public BoundedContext.OrderTaking.Workflow.PlaceOrder.Overview
import public BoundedContext.OrderTaking.Workflow.PlaceOrder.Domain
import public Rango.BoundedContext.Workflow


public export
StateType : Overview.State -> Type
StateType OrderForm          = Domain.OrderForm
StateType Order              = Either Domain.InvalidOrder Domain.Order
StateType ValidOrder         = Domain.Order
StateType PricedOrder        = Domain.PricedOrder
StateType InvalidOrder       = Domain.InvalidOrder
StateType InvalidOrderQueued = List Domain.PlacedOrderEvent
StateType OrderInfo          = List Domain.PlacedOrderEvent

step : Overview.Step s e -> (StateType s) -> PlaceOrderDSL (StateType e)
step ValidateOrder     st = validateOrder st
step AddInvalidOrder   st = pure [InvalidOrderRegistered st]
step PriceOrder        st = priceOrder st
step SendAckToCustomer st = do
  ack <- acknowledgeOrder st
  placePricedOrder st
  pure $ createEvents st ack
step SendInvalidOrder  st = pure st

check : Check s b1 b2 -> (StateType s) -> PlaceOrderDSL (Either (StateType b1) (StateType b2))
check CheckInvalidOrder st = pure st

public export
PlaceOrderMorphism : Morphism PlaceOrderDSL Overview.State Overview.Step Overview.Check
PlaceOrderMorphism = MkMorphism
  { StateType = StateType
  , step      = step
  , check     = check
  }
```

## File: `src/BoundedContext/OrderTaking/Workflow/PlaceOrder/Backend.idr`
```
module BoundedContext.OrderTaking.Workflow.PlaceOrder.Backend

import Control.Monad.Trans
import public Control.Monad.Either
import public Control.Monad.Reader

import Data.String
import Data.StringN
import System.Random

import BoundedContext.OrderTaking.Workflow.PlaceOrder.Database.DTO
import BoundedContext.OrderTaking.Workflow.PlaceOrder.Database.ConvertDTO
import BoundedContext.OrderTaking.Workflow.PlaceOrder.Database.Product
import BoundedContext.OrderTaking.Workflow.PlaceOrder.Database.Order
import BoundedContext.OrderTaking.Workflow.PlaceOrder.Domain
import BoundedContext.OrderTaking.Workflow.PlaceOrder.DTO

import Service.NodeJS.SQLite
import Service.NodeJS.MD5
import Service.NodeJS.Date
import Service.NodeJS.Promise
import Service.NodeJS.Random


record OrderDBComp where
  constructor MkOrderDBComp
  dbConnection        : Type 
  dbError             : Type
  showDBError         : dbError -> String
  initConnection      : Promise (Either dbError dbConnection)
  closeConnection     : dbConnection -> Promise (Maybe dbError)
  beginTransaction    : dbConnection -> Promise (Maybe dbError)
  commitTransaction   : dbConnection -> Promise (Maybe dbError)
  rollbackTransaction : dbConnection -> Promise (Maybe dbError)
  saveOrder           : dbConnection -> PricedOrderDTO -> Promise (Maybe dbError)

record ProductDBComp where
  constructor MkProductDBComp
  dbConnection        : Type 
  dbError             : Type
  showDBError         : dbError -> String
  initConnection      : Promise (Either dbError dbConnection)
  closeConnection     : dbConnection -> Promise (Maybe dbError)
  beginTransaction    : dbConnection -> Promise (Maybe dbError)
  commitTransaction   : dbConnection -> Promise (Maybe dbError)
  rollbackTransaction : dbConnection -> Promise (Maybe dbError)
  productPrice        : dbConnection -> ProductCodeDTO -> Promise (Either dbError Double)
  productExists       : dbConnection -> ProductCodeDTO -> Promise (Either dbError Bool)

record EmailComp where
  constructor MkEmailComp
  emailError  : Type
  showError   : emailError -> String
  serviceInfo : ServiceInfo
  send        : EmailAddress -> HtmlString -> Promise (Maybe emailError)

data CheckAddressResult
  = ValidAddress
  | NotFound String
  | InvalidAddress String

record CheckAddressComp where
  constructor MkCheckAddressComp
  addressError : Type
  showError    : addressError -> String
  serviceInfo  : ServiceInfo
  checkAddress : AddressForm -> Promise (Either addressError CheckAddressResult)

record Dependencies where
  constructor MkDependencies
  md5Provider       : MD5
  orderDBComp       : OrderDBComp
  orderDBConn       : orderDBComp.dbConnection
  productDBComp     : ProductDBComp
  productDBConn     : productDBComp.dbConnection
  emailComp         : EmailComp
  checkAddressComp  : CheckAddressComp

orderDBDep : Dependencies -> (o : OrderDBComp ** o.dbConnection)
orderDBDep d = (d.orderDBComp ** d.orderDBConn)

productDBDep : Dependencies -> (p : ProductDBComp ** p.dbConnection)
productDBDep d = (d.productDBComp ** d.productDBConn) 

||| Backend monad for the PlaceOrder workflow.
public export
data Backend : Type -> Type where
  MkBackend : EitherT PlaceOrderError (ReaderT Dependencies Promise) a -> Backend a

backend : Backend a -> EitherT PlaceOrderError (ReaderT Dependencies Promise) a
backend (MkBackend m) = m

export
Functor Backend where
  map f (MkBackend x) = MkBackend (map f x)

export
Applicative Backend where
  pure x = MkBackend (pure x)
  (MkBackend f) <*> (MkBackend x) = MkBackend (f <*> x)

export
Monad Backend where
  (MkBackend m) >>= k = MkBackend (m >>= (backend . k))

export
HasIO Backend where
  liftIO io = MkBackend (liftIO io)

export
MonadReader Dependencies Backend where
  ask = MkBackend ask
  local f (MkBackend m) = MkBackend (local f m)

export
MonadError PlaceOrderError Backend where
  catchError (MkBackend m) f = MkBackend (catchError m (backend . f))
  throwError e = MkBackend (throwError e)

export
liftPromise : Promise a -> Backend a
liftPromise p = MkBackend (lift (lift p))

export
data RunBackend : Type where
  MkRunBackend : ((a : Type) -> Backend a -> Promise (Either PlaceOrderError a)) -> RunBackend

export
runBackend : {a : Type} -> RunBackend -> Backend a -> Promise (Either PlaceOrderError a)
runBackend {a} (MkRunBackend r) = r a

export
mkRunBackend
  :  (orderDBComp       : OrderDBComp)
  => (productDBComp     : ProductDBComp)
  => (emailComp         : EmailComp)
  => (checkAddressComp  : CheckAddressComp)
  => HasIO io
  => io RunBackend
mkRunBackend = do
  md5 <- MD5.require
  pure $ MkRunBackend $ \type, script => do
    -- Open DB conenctions
    orderDBConn
      <- Promise.either
          $ mapFst (OrderDBComp.showDBError orderDBComp)
          $ !(OrderDBComp.initConnection orderDBComp)
    productDBConn
      <- Promise.either
          $ mapFst (ProductDBComp.showDBError productDBComp)
          $ !(ProductDBComp.initConnection productDBComp)
    
    -- Initialise transactions
    Nothing <- orderDBComp.beginTransaction orderDBConn
      | Just err => Promise.reject $ orderDBComp.showDBError err
    Nothing <- productDBComp.beginTransaction productDBConn
      | Just err => Promise.reject $ productDBComp.showDBError err

    -- Run the backend computation
    let dependencies =
          MkDependencies
            { md5Provider       = md5
            , orderDBComp       = orderDBComp
            , orderDBConn       = orderDBConn
            , productDBComp     = productDBComp
            , productDBConn     = productDBConn
            , emailComp         = emailComp
            , checkAddressComp  = checkAddressComp
            }
    x <- runReaderT dependencies (runEitherT (backend script))
    case x of
      Left _ => do
        ignore $ orderDBComp.rollbackTransaction orderDBConn
        ignore $ productDBComp.rollbackTransaction productDBConn
      Right _ => do
        ignore $ orderDBComp.commitTransaction orderDBConn
        ignore $ productDBComp.commitTransaction productDBConn
    
    -- Try to close the connections
    ignore $ productDBComp.closeConnection productDBConn
    ignore $ orderDBComp.closeConnection orderDBConn
    pure (the (Either PlaceOrderError type) x)

namespace Model

  generateIdentifier : HasIO io => MD5 -> io String
  generateIdentifier md5 = do
    n <- Date.now
    d <- Random.double
    idx <- md5.generate (show n ++ show d)
    putStrLn idx
    pure idx

  newOrderId : Backend OrderId
  newOrderId = MkOrderId <$> (generateIdentifier !(asks md5Provider))

  newOrderLineId : Backend OrderLineId
  newOrderLineId = MkOrderLineId <$> (generateIdentifier !(asks md5Provider))

  checkProductCodeExists : ProductCode -> Backend Bool
  checkProductCodeExists p = do
    (productDB ** productDBConn) <- asks productDBDep
    Right answer <- liftPromise $ productDB.productExists productDBConn (toProductCodeDTO p)
      | Left err => throwError $ ProductCodeError $ MkProductCodeErr $ productDB.showDBError err
    pure answer
  
  checkAddressExists : AddressForm -> Backend (Either CheckedAddressValidationError CheckedAddress)
  checkAddressExists addressForm = do
    comp <- asks checkAddressComp
    Right res <- liftPromise $ comp.checkAddress addressForm
      | Left err => throwError
                  $ RemoteServiceErr
                  $ MkRemoteServiceError comp.serviceInfo
                  $ MkRemoteServiceException
                  $ comp.showError err
    pure $ case res of
      ValidAddress        => Right (MkCheckedAddress addressForm)
      NotFound msg        => Left (AddressNotFound msg)
      InvalidAddress msg  => Left (InvalidFormat msg)

  getProductPrice : ProductCode -> Backend Price
  getProductPrice p = do
    (productDB ** productDBConn) <- asks productDBDep
    Right priceValue <- liftPromise $ productDB.productPrice productDBConn (toProductCodeDTO p)
      | Left err      => throwError $ ProductCodeError $ MkProductCodeErr $ productDB.showDBError err
    let Right price = Price.create priceValue
        | Left err    => throwError $ ProductCodeError $ MkProductCodeErr err
    pure price
  
  placePricedOrder : PricedOrder -> Backend ()
  placePricedOrder pricedOrder = do
    (orderDB ** orderDBConn) <- asks orderDBDep 
    Nothing <- liftPromise $ orderDB.saveOrder orderDBConn (toPricedOrderDTO pricedOrder)
      | Just err => throwError $ MkPlaceOrderError $ orderDB.showDBError err
    pure ()

  createOrderAcknowledgementLetter : PricedOrder -> Backend HtmlString
  createOrderAcknowledgementLetter pricedOrder = do
    -- TODO: Render some simple plain text
    pure (MkHtmlString "<HTML></HTML>")

  sendOrderAcknowledgement : OrderAcknowledgement -> Backend AckSent
  sendOrderAcknowledgement orderAcknowledgement = do
    comp <- asks emailComp
    Nothing <- liftPromise $ comp.send orderAcknowledgement.emailAddress orderAcknowledgement.letter
      | Just err => throwError
                  $ RemoteServiceErr
                  $ MkRemoteServiceError comp.serviceInfo
                  $ MkRemoteServiceException
                  $ comp.showError err
    pure Sent

  export
  backend : Model Backend
  backend = MkModel
    { throwError                       = throwError
    , catchError                       = tryError
    , newOrderId                       = newOrderId
    , newOrderLineId                   = newOrderLineId
    , checkProductCodeExists           = checkProductCodeExists
    , checkAddressExists               = checkAddressExists
    , getProductPrice                  = getProductPrice
    , placePricedOrder                 = placePricedOrder
    , createOrderAcknowledgementLetter = createOrderAcknowledgementLetter
    , sendOrderAcknowledgement         = sendOrderAcknowledgement
    }

namespace Components

  export
  productDBSQlite : ProductDBComp
  productDBSQlite = MkProductDBComp
    { dbConnection        = Database
    , dbError             = ProductDBError
    , showDBError         = show
    , initConnection      = do
        sqlite <- SQLite.require
        map (mapFst (InitializeError . show)) $ SQLite.database sqlite "./db/product.db"
    , closeConnection     = \db => Nothing <$ SQLite.Database.close db
    , beginTransaction    = \db => map (map (InitializeError . show) . toMaybe) $ SQLite.Database.run db "begin"
    , commitTransaction   = \db => map (map (InitializeError . show) . toMaybe) $ SQLite.Database.run db "commit"
    , rollbackTransaction = \db => map (map (InitializeError . show) . toMaybe) $ SQLite.Database.run db "rollback"
    , productPrice        = \db, pc => runProductDB db $ Product.productPrice  pc
    , productExists       = \db, pc => runProductDB db $ Product.productExists pc
    }

  export
  orderDBSQLite : OrderDBComp
  orderDBSQLite = MkOrderDBComp
    { dbConnection        = Database
    , dbError             = OrderDBError
    , showDBError         = show
    , initConnection      = do
        sqlite <- SQLite.require
        map (mapFst (InitializeError . show)) $ SQLite.database sqlite "./db/order.db"
    , closeConnection     = \db => Nothing <$ SQLite.Database.close db
    , beginTransaction    = \db => map (map (InitializeError . show) . toMaybe) $ SQLite.Database.run db "begin"
    , commitTransaction   = \db => map (map (InitializeError . show) . toMaybe) $ SQLite.Database.run db "commit"
    , rollbackTransaction = \db => map (map (InitializeError . show) . toMaybe) $ SQLite.Database.run db "rollback"
    , saveOrder           = \db, po => map (either Just (const Nothing)) $ runOrderDB db $ Order.saveOrder po
    }

  export
  noEmail : EmailComp
  noEmail = MkEmailComp
    { emailError  = String
    , showError   = id
    , serviceInfo = MkServiceInfo "NoOp Email" (MkUri "localhost")
    , send = \addr, html => do
        putStrLn "\{addr.value} : \{html.value}"
        pure Nothing
    }

  export
  okCheckAddress : CheckAddressComp
  okCheckAddress = MkCheckAddressComp
    { addressError = String
    , showError    = id
    , serviceInfo  = MkServiceInfo "NoOp Address Check" (MkUri "localhost")
    , checkAddress = \_ => pure $ Right ValidAddress
    }
```

## File: `src/BoundedContext/OrderTaking/Workflow/PlaceOrder/ConvertDTO.idr`
```
module BoundedContext.OrderTaking.Workflow.PlaceOrder.ConvertDTO

import BoundedContext.OrderTaking.Workflow.PlaceOrder.DTO
import BoundedContext.OrderTaking.Workflow.PlaceOrder.Domain

import Data.StringN

namespace FromUpstream

  export
  orderForm : OrderFormDTO -> OrderForm

  orderLineForm    : OrderLineFormDTO -> OrderLineForm
  addressForm      : AddressFormDTO   -> AddressForm
  customerInfoForm : CustomerFormDTO  -> CustomerInfoForm

  orderForm dto = MkOrderForm
    { customerInfo    = customerInfoForm dto.customer
    , shippingAddress = addressForm dto.shippingAddress
    , billingAddress  = addressForm dto.billingAddress
    , orderLines      = map orderLineForm dto.orderLines
    }

  customerInfoForm dto = MkCustomerInfoForm
    { firstName    = dto.firstName
    , lastName     = dto.lastName
    , emailAddress = dto.emailAddress
    }

  nonEmpty : String -> Maybe String
  nonEmpty "" = Nothing
  nonEmpty xs = Just xs

  addressForm dto = MkAddressForm
    { addressLine1 = dto.addressLine1
    , addressLine2 = nonEmpty dto.addressLine2
    , addressLine3 = nonEmpty dto.addressLine3
    , addressLine4 = nonEmpty dto.addressLine4
    , city         = dto.city
    , zipCode      = dto.zipCode
    }

  orderLineForm dto = MkOrderLineForm
    { productCode = dto.productCode
    , quantity    = dto.quantity
    }

namespace ToDownstream

  export toPlaceOrderEventDTO   : PlacedOrderEvent -> PlaceOrderEventDTO
  export toPlacedOrderErrorDTO  : PlaceOrderError -> PlaceOrderErrorDTO

  toPricedOrderDsDTO            : PricedOrder -> PricedOrderDsDTO
  toPricedOrderLineDsDTO        : PricedOrderLine -> PricedOrderLineDsDTO
  toAddressDsDTO                : Address -> AddressDsDTO
  toBillableOrderPlacedDTO      : BillableOrderPlaced -> BillableOrderPlacedDTO
  toAcknowledgementSentDTO      : OrderAcknowledgementSent -> OrderAcknowledgementSentDTO
  toAddressValidationErrorDTO   : AddressValidationError -> AddressValidationErrorDTO
  toNameValidationErrorDTO      : NameValidationError -> NameValidationErrorDTO
  toEmailValidationErrorDTO     : EmailValidationError -> EmailValidationErrorDTO
  toQuantityValidationErrorDTO  : QuantityValidationError -> QuantityValidationErrorDTO
  toValidationErrorDTO          : ValidationError -> ValidationErrorDTO
  toProductCodeErrorDTO         : ProductCodeErr -> ProductCodeErrDTO
  toInvalidOrderDTO             : InvalidOrder -> InvalidOrderDTO
  toPricingErrorDTO             : PricingError -> PricingErrorDTO
  toRemoteServiceErrorDTO       : RemoteServiceError -> RemoteServiceErrorDTO

  toPlaceOrderEventDTO (OrderPlacedEvent         x) = OrderPlacedEvent          (toPricedOrderDsDTO x)
  toPlaceOrderEventDTO (BillableOrderPlacedEvent x) = BillableOrderPlacedEvent  (toBillableOrderPlacedDTO x)
  toPlaceOrderEventDTO (AcknowledgementSentEvent x) = AcknowledgementSentEvent  (toAcknowledgementSentDTO x)
  toPlaceOrderEventDTO (InvalidOrderRegistered   x) = InvalidOrderRegistered    (toInvalidOrderDTO x)

  toPricedOrderDsDTO po = MkPricedOrderDsDTO
    { orderId       = po.orderId.value
    , orderLines    = map toPricedOrderLineDsDTO po.orderLines
    , amountToBill  = po.amountToBill.value
    }

  toPricedOrderLineDsDTO pol = MkPricedOrderLineDsDTO
    { orderLineId = pol.orderLine.orderLineId.value
    , productCode = pol.orderLine.productCode.value
    , price       = pol.price.value
    }

  toAddressDsDTO a = MkAddressDsDTO
    { addressLine1 = a.addressLine1.value
    , addressLine2 = maybe "" (.value) a.addressLine2
    , addressLine3 = maybe "" (.value) a.addressLine3
    , addressLine4 = maybe "" (.value) a.addressLine4
    , city         = a.city.value
    , zipCode      = a.zipCode.value
    }

  toBillableOrderPlacedDTO bop = MkBillableOrderPlacedDTO
    { orderId         = bop.orderId.value
    , billingAddress  = toAddressDsDTO bop.billingAddress.address
    , amountToBill    = bop.amountToBill.value
    }

  toAcknowledgementSentDTO as = MkOrderAcknowledgementSentDTO
    { orderId      = as.orderId.value
    , emailAddress = as.emailAddress.value
    }

  toCheckedAddressValidationErrorDTO : CheckedAddressValidationError -> CheckedAddressValidationErrorDTO
  toCheckedAddressValidationErrorDTO (InvalidFormat   x) = InvalidFormat x
  toCheckedAddressValidationErrorDTO (AddressNotFound x) = AddressNotFound x

  toAddressValidationErrorDTO (MkAddressLineError     x) = MkAddressLineError x
  toAddressValidationErrorDTO (MkAddressOptLineError  x) = MkAddressOptLineError x
  toAddressValidationErrorDTO (MkAddressCityError     x) = MkAddressCityError x
  toAddressValidationErrorDTO (MkAddressZipCodeError  x) = MkAddressZipCodeError x
  toAddressValidationErrorDTO (CheckedAddressError    x) = CheckedAddressError (toCheckedAddressValidationErrorDTO x)

  toNameValidationErrorDTO vne = MkNameValidationErrorDTO
    { field = vne.field
    , value = vne.value
    }
  
  toEmailValidationErrorDTO (MkEmailValidationError message)
    = MkEmailValidationErrorDTO message

  toQuantityValidationErrorDTO (MkQuantityValidationError condition message)
    = MkQuantityValidationErrorDTO condition message

  toValidationErrorDTO (AddressValidation   x) = AddressValidation  (toAddressValidationErrorDTO x)
  toValidationErrorDTO (NameValidation      x) = NameValidation     (toNameValidationErrorDTO x)
  toValidationErrorDTO (EmailValidation     x) = EmailValidation    (toEmailValidationErrorDTO x)
  toValidationErrorDTO (QuantityValidation  x) = QuantityValidation (toQuantityValidationErrorDTO x)

  toProductCodeErrorDTO (MkProductCodeErr x) = MkProductCodeErr x

  toInvalidOrderDTO io = MkInvalidOrderDTO
    { validationErrors = map toValidationErrorDTO io.validationErrors
    , productCodeErrors = map toProductCodeErrorDTO io.productCodeErrors
    }

  toPricingErrorDTO (MkPricingError message) = MkPricingError message
  
  toRemoteServiceErrorDTO (MkRemoteServiceError (MkServiceInfo name endpoint) (MkRemoteServiceException message))
    = MkRemoteServiceErrorDTO name message

  toPlacedOrderErrorDTO (MkPlaceOrderError x) = MkPlaceOrderError x
  toPlacedOrderErrorDTO (ValidationErrors xs) = ValidationErrors  $ map toValidationErrorDTO xs
  toPlacedOrderErrorDTO (ProductCodeError x)  = ProductCodeError  $ toProductCodeErrorDTO x
  toPlacedOrderErrorDTO (PriceOrderError x)   = PriceOrderError   $ toPricingErrorDTO x
  toPlacedOrderErrorDTO (RemoteServiceErr x)  = RemoteServiceErr  $ toRemoteServiceErrorDTO x
```

## File: `src/BoundedContext/OrderTaking/Workflow/PlaceOrder/DTO.idr`
```
module BoundedContext.OrderTaking.Workflow.PlaceOrder.DTO

import Rango.DataTransfer.JSON.Derive

%language ElabReflection
%default total

-- Incoming information
-- From Upstream system

namespace UpstreamDTO

  public export
  record AddressFormDTO where
    constructor MkAddressFormDTO
    addressLine1 : String
    addressLine2 : String
    addressLine3 : String
    addressLine4 : String
    city         : String
    zipCode      : String

  public export
  record OrderLineFormDTO where
    constructor MkOrderLineFormDTO
    productCode : String
    quantity    : String

  public export
  record CustomerFormDTO where
    constructor MkCustomerFormDTO
    firstName    : String
    lastName     : String
    emailAddress : String

  public export
  record OrderFormDTO where
    constructor MkOrderFormDTO
    customer        : CustomerFormDTO
    shippingAddress : AddressFormDTO
    billingAddress  : AddressFormDTO
    orderLines      : List OrderLineFormDTO

  public export
  record ProductFormDTO where
    constructor MkProductFormDTO
    productCode : String
    price       : Double
    description : String

  %runElab deriveJSON defaultOpts `{AddressFormDTO}
  %runElab deriveJSON defaultOpts `{OrderLineFormDTO}
  %runElab deriveJSON defaultOpts `{CustomerFormDTO}
  %runElab deriveJSON defaultOpts `{OrderFormDTO}
  %runElab deriveJSON defaultOpts `{ProductFormDTO}

-- Outgoing information
-- To Downstream systems

namespace DownstreamDTO

  public export
  record PricedOrderLineDsDTO where
    constructor MkPricedOrderLineDsDTO
    orderLineId : String
    productCode : String
    price       : Double

  public export
  record PricedOrderDsDTO where
    constructor MkPricedOrderDsDTO
    orderId       : String
    orderLines    : List PricedOrderLineDsDTO
    amountToBill  : Double

  --NOTE: Redefining the type doesn't raise any issues. Is this intended?
  --data BillableOrderPlacedDTO : Type

  -- NOTE: Reusing name, creates elaboration issue.
  public export
  record AddressDsDTO where
    constructor MkAddressDsDTO
    addressLine1 : String
    addressLine2 : String
    addressLine3 : String
    addressLine4 : String
    city         : String
    zipCode      : String

  public export
  record BillableOrderPlacedDTO where
    constructor MkBillableOrderPlacedDTO
    orderId        : String
    billingAddress : DownstreamDTO.AddressDsDTO
    amountToBill   : Double

  public export
  record OrderAcknowledgementSentDTO where
    constructor MkOrderAcknowledgementSentDTO
    orderId      : String
    emailAddress : String

  public export
  data CheckedAddressValidationErrorDTO
    = InvalidFormat String
    | AddressNotFound String

  public export
  data AddressValidationErrorDTO
    = MkAddressLineError    String
    | MkAddressOptLineError (Maybe String)
    | MkAddressCityError    String
    | MkAddressZipCodeError String
    | CheckedAddressError   CheckedAddressValidationErrorDTO

  public export
  record NameValidationErrorDTO where
    constructor MkNameValidationErrorDTO
    field : String
    value : String
  
  public export
  record EmailValidationErrorDTO where
    constructor MkEmailValidationErrorDTO
    message : String

  public export
  record QuantityValidationErrorDTO where
    constructor MkQuantityValidationErrorDTO
    condition : String
    message   : String

  public export
  data ValidationErrorDTO
    = AddressValidation   AddressValidationErrorDTO
    | NameValidation      NameValidationErrorDTO
    | EmailValidation     EmailValidationErrorDTO
    | QuantityValidation  QuantityValidationErrorDTO

  public export
  record ProductCodeErrDTO where
    constructor MkProductCodeErr
    message : String

  public export
  record InvalidOrderDTO where
    constructor MkInvalidOrderDTO
    validationErrors  : List ValidationErrorDTO
    productCodeErrors : List ProductCodeErrDTO

  public export
  data PlaceOrderEventDTO
    = OrderPlacedEvent          PricedOrderDsDTO
    | BillableOrderPlacedEvent  BillableOrderPlacedDTO
    | AcknowledgementSentEvent  OrderAcknowledgementSentDTO
    | InvalidOrderRegistered    InvalidOrderDTO

  public export
  record PricingErrorDTO where
    constructor MkPricingError
    message : String

  public export
  record RemoteServiceErrorDTO where
    constructor MkRemoteServiceErrorDTO
    serviceInfo : String
    exception   : String

  public export
  data PlaceOrderErrorDTO
    = MkPlaceOrderError String
    | ValidationErrors (List ValidationErrorDTO)
    | ProductCodeError ProductCodeErrDTO
    | PriceOrderError PricingErrorDTO
    | RemoteServiceErr RemoteServiceErrorDTO

  export
  constructorToJSON : {x : Type} -> (ToJSON x) => String -> x -> JSON
  constructorToJSON tag field = JObject [("tag", JString tag), ("value", toJSON field)]

  export
  constructorFromJSON : (FromJSON x) => String -> (x -> y) -> JSON -> Maybe y
  constructorFromJSON tag create (JObject [("tag", JString tag0), ("value", field)])
    = if tag == tag0
        then map create $ fromJSON field
        else Nothing
  constructorFromJSON _ _ _ = Nothing

  ToJSON CheckedAddressValidationErrorDTO where
    toJSON (InvalidFormat x)   = constructorToJSON "InvalidFormat"   x
    toJSON (AddressNotFound x) = constructorToJSON "AddressNotFound" x
  
  FromJSON CheckedAddressValidationErrorDTO where
    fromJSON x
        = constructorFromJSON "InvalidFormat"   InvalidFormat x
      <|> constructorFromJSON "AddressNotFound" AddressNotFound x

  ToJSON AddressValidationErrorDTO where
    toJSON (MkAddressLineError    x) = constructorToJSON "MkAddressLineError"    x
    toJSON (MkAddressOptLineError x) = constructorToJSON "MkAddressOptLineError" x
    toJSON (MkAddressCityError    x) = constructorToJSON "MkAddressCityError"    x
    toJSON (MkAddressZipCodeError x) = constructorToJSON "MkAddressZipCodeError" x
    toJSON (CheckedAddressError   x) = constructorToJSON "CheckedAddressError"   x
  
  FromJSON AddressValidationErrorDTO where
    fromJSON x
        = constructorFromJSON "MkAddressLineError" MkAddressLineError x
      <|> constructorFromJSON "MkAddressOptLineError" MkAddressOptLineError x
      <|> constructorFromJSON "MkAddressCityError" MkAddressCityError x
      <|> constructorFromJSON "MkAddressZipCodeError" MkAddressZipCodeError x
      <|> constructorFromJSON "CheckedAddressError" CheckedAddressError x

  %runElab deriveJSON defaultOpts `{NameValidationErrorDTO}
  %runElab deriveJSON defaultOpts `{EmailValidationErrorDTO}
  %runElab deriveJSON defaultOpts `{QuantityValidationErrorDTO}

  ToJSON ValidationErrorDTO where
    toJSON (AddressValidation   x) = constructorToJSON "AddressValidation" x
    toJSON (NameValidation      x) = constructorToJSON "NameValidation" x
    toJSON (EmailValidation     x) = constructorToJSON "EmailValidation" x
    toJSON (QuantityValidation  x) = constructorToJSON "QuantityValidation" x

  FromJSON ValidationErrorDTO where
    fromJSON x
        = constructorFromJSON "AddressValidation" AddressValidation x
      <|> constructorFromJSON "NameValidation" NameValidation x
      <|> constructorFromJSON "EmailValidation" EmailValidation x
      <|> constructorFromJSON "QuantityValidation" QuantityValidation x

  %runElab deriveJSON defaultOpts `{PricedOrderLineDsDTO}
  %runElab deriveJSON defaultOpts `{AddressDsDTO}
  %runElab deriveJSON defaultOpts `{BillableOrderPlacedDTO}
  %runElab deriveJSON defaultOpts `{OrderAcknowledgementSentDTO}
  %runElab deriveJSON defaultOpts `{ProductCodeErrDTO}
  %runElab deriveJSON defaultOpts `{InvalidOrderDTO}
  %runElab deriveJSON defaultOpts `{PricedOrderDsDTO}
  %runElab deriveJSON defaultOpts `{PricingErrorDTO}
  %runElab deriveJSON defaultOpts `{RemoteServiceErrorDTO}

  export
  ToJSON PlaceOrderEventDTO where
    toJSON (OrderPlacedEvent          x) = constructorToJSON "OrderPlacedEvent" x
    toJSON (BillableOrderPlacedEvent  x) = constructorToJSON "BillableOrderPlacedEvent" x
    toJSON (AcknowledgementSentEvent  x) = constructorToJSON "AcknowledgementSentEvent" x
    toJSON (InvalidOrderRegistered    x) = constructorToJSON "InvalidOrderRegistered" x

  export
  FromJSON PlaceOrderEventDTO where
    fromJSON x
        = constructorFromJSON "OrderPlacedEvent" OrderPlacedEvent x
      <|> constructorFromJSON "BillableOrderPlacedEvent" BillableOrderPlacedEvent x
      <|> constructorFromJSON "AcknowledgementSentEvent" AcknowledgementSentEvent x
      <|> constructorFromJSON "InvalidOrderRegistered" InvalidOrderRegistered x

  export
  ToJSON PlaceOrderErrorDTO where
    toJSON (MkPlaceOrderError x)  = constructorToJSON "MkPlaceOrderError" x
    toJSON (ValidationErrors xs)  = constructorToJSON "ValidationErrors" xs
    toJSON (ProductCodeError x)   = constructorToJSON "ProductCodeError" x
    toJSON (PriceOrderError x)    = constructorToJSON "PriceOrderError" x
    toJSON (RemoteServiceErr x)   = constructorToJSON "RemoteServiceErr" x

  export
  FromJSON PlaceOrderErrorDTO where
    fromJSON x
        = constructorFromJSON "MkPlaceOrderError" MkPlaceOrderError x
      <|> constructorFromJSON "ValidationErrors" ValidationErrors x
      <|> constructorFromJSON "ProductCodeError" ProductCodeError x
      <|> constructorFromJSON "PriceOrderError" PriceOrderError x      
      <|> constructorFromJSON "RemoteServiceErr" RemoteServiceErr x
```

## File: `src/BoundedContext/OrderTaking/Workflow/PlaceOrder/Domain.idr`
```
module BoundedContext.OrderTaking.Workflow.PlaceOrder.Domain

import Data.Between
import Data.Either
import Data.List
import Data.Result
import Data.StringN
import Data.String
import Data.Form

namespace Price

  export
  data Price = MkPrice Double

  export
  create : Double -> Either String Price
  create p = if p < 0.0 then Left "Zero or negative price." else Right (MkPrice p)

  export
  multiply : Price -> Double -> Price
  multiply (MkPrice x) d = MkPrice (x * d)

  export
  (.value) : Price -> Double
  (.value) (MkPrice x) = x

  export
  sumPrices : List Price -> Price
  sumPrices = MkPrice . sum . map (.value)

namespace EmailAddress

  export
  data EmailAddress = MkEmailAddress String

  export
  create : String -> Maybe EmailAddress
  create = Just . MkEmailAddress -- TODO

  export
  (.value) : EmailAddress -> String
  (.value) (MkEmailAddress e) = e

public export
record PersonalName where
  constructor MkPersonalName
  firstName : StringN 50
  lastName  : StringN 50

public export
record CustomerInfo where
  constructor MkCustomerInfo
  personalName : PersonalName
  emailAddress : EmailAddress

namespace ZipCode

  export
  data ZipCode = MkZipCode String

  export
  create : String -> Maybe ZipCode
  create = Just . MkZipCode -- TODO

  export
  (.value) : ZipCode -> String
  (.value) (MkZipCode z) = z

public export
record AddressForm where
  constructor MkAddressForm
  addressLine1 : String
  addressLine2 : Maybe String
  addressLine3 : Maybe String
  addressLine4 : Maybe String
  city         : String
  zipCode      : String

public export
record Address where
  constructor MkAddress
  addressLine1 : StringN 50
  addressLine2 : Maybe (StringN 50)
  addressLine3 : Maybe (StringN 50)
  addressLine4 : Maybe (StringN 50)
  city         : StringN 50
  zipCode      : ZipCode

public export
record ShippingAddress where
  constructor MkShippingAddress
  address : Address

public export
record BillingAddress where
  constructor MkBillingAddress
  address : Address

public export
data WidgetCode = MkWidgetCode String

mkWidgetCode : String -> Maybe WidgetCode
mkWidgetCode = Just . MkWidgetCode -- TODO

public export
data GizmoCode = MkGizmoCode String

mkGizmoCode : String -> Maybe GizmoCode
mkGizmoCode = Just . MkGizmoCode -- TODO

namespace ProductCode

  public export
  data ProductCode
    = WidgetProduct WidgetCode
    | GizmoProduct GizmoCode

  export
  mkProductCode : String -> Maybe ProductCode
  mkProductCode str = map WidgetProduct $ mkWidgetCode str

  export
  (.value) : ProductCode -> String
  (.value) (WidgetProduct (MkWidgetCode x)) = x
  (.value) (GizmoProduct (MkGizmoCode x)) = x

public export
record ProductForm where
  constructor MkProductForm
  productCode : String
  price       : Double
  description : String

public export
record Product where
  constructor MkProduct
  productCode : ProductCode
  price       : Price
  description : StringN 1000

public export
record OrderLineForm where
  constructor MkOrderLineForm
  productCode : String
  quantity    : String

public export
record CustomerInfoForm where
  constructor MkCustomerInfoForm
  firstName    : String
  lastName     : String
  emailAddress : String

public export
record OrderForm where
  constructor MkOrderForm
  customerInfo    : CustomerInfoForm
  shippingAddress : AddressForm
  billingAddress  : AddressForm
  orderLines      : List OrderLineForm

data UnitQuantity : Type where
  MkUnitQuantity
    : (Between Integer 1 1000)
    -> UnitQuantity

data KilogramQuantity : Type where
  MkKilogramQuantity
    :  (Between Double 0.0 100.0)
    -> KilogramQuantity

namespace OrderQuantity

  public export
  data OrderQuantity
    = OrderUnitQuantity     UnitQuantity
    | OrderKilogramQuantity KilogramQuantity

  export
  (.value) : OrderQuantity -> Double
  (.value) (OrderUnitQuantity     (MkUnitQuantity x))     = fromInteger $ x.value
  (.value) (OrderKilogramQuantity (MkKilogramQuantity x)) = the _ x.value -- See https://github.com/idris-lang/Idris2/issues/1760

namespace OrderId

  public export
  data OrderId = MkOrderId String

  export
  (.value) : OrderId -> String
  (.value) (MkOrderId x) = x

namespace OrderLineId

  public export
  data OrderLineId = MkOrderLineId String

  export
  (.value) : OrderLineId -> String
  (.value) (MkOrderLineId x) = x

public export
record OrderLine where
  constructor MkOrderLine
  orderLineId : OrderLineId
  productCode : ProductCode
  quantity    : OrderQuantity

-- Synonym to ValidatedOrder
public export
record Order where
  constructor MkOrder
  orderId         : OrderId
  customerInfo    : CustomerInfo
  shippingAddress : ShippingAddress
  billingAddress  : BillingAddress
  orderLines      : List OrderLine

public export
record PricedOrderLine where
  constructor MkPricedOrderLine
  orderLine : OrderLine
  price     : Price

public export
record PricedOrder where
  constructor MkPricedOrder
  orderId         : OrderId
  customerInfo    : CustomerInfo
  shippingAddress : ShippingAddress
  billingAddress  : BillingAddress
  orderLines      : List PricedOrderLine
  amountToBill    : Price

data AcknowledgementLetter = MkAcknowledgementLetter

record PlacedOrderAcknowledgement where
  constructor MkPlacedOrderAcknowledgement
  pricedOrder           : PricedOrder
  acknowledgementLetter : AcknowledgementLetter

public export
record BillableOrderPlaced where
  constructor MkBillableOrderPlaced
  orderId        : OrderId
  billingAddress : BillingAddress
  amountToBill   : Price

data EnvelopeContents = MkEnvelopeContents (List String)

data QuoteForm = MkQouteForm

data CategorizedMail
  = QuoteMail QuoteForm
  | OrderMail OrderForm

CategorizeInboundMail : Type
CategorizeInboundMail = EnvelopeContents -> CategorizedMail

data ProductCatalog = MkProductCatalog

CalculatePrices : Type
CalculatePrices = ProductCatalog => Order -> PricedOrder

public export
data CheckedAddressValidationError
  = InvalidFormat String
  | AddressNotFound String

Show CheckedAddressValidationError where
  showPrec d (InvalidFormat x) = showCon d "InvalidFormat" $ showArg x
  showPrec d (AddressNotFound x) = showCon d "AddressNotFound" $ showArg x

public export
data AddressValidationError
  = MkAddressLineError String
  | MkAddressOptLineError (Maybe String)
  | MkAddressCityError String
  | MkAddressZipCodeError String
  | CheckedAddressError CheckedAddressValidationError

Show AddressValidationError where
  showPrec d (MkAddressLineError x)     = showCon d "MkAddressLineError" $ showArg x
  showPrec d (MkAddressOptLineError x)  = showCon d "MkAddressOptLineError" $ showArg x
  showPrec d (MkAddressCityError x)     = showCon d "MkAddressCityError" $ showArg x
  showPrec d (MkAddressZipCodeError x)  = showCon d "MkAddressZipCodeError" $ showArg x
  showPrec d (CheckedAddressError x)    = showCon d "CheckedAddressError" $ showArg x

public export
record NameValidationError where
  constructor MkNameValidationError
  field : String
  value : String

Show NameValidationError where
  showPrec d (MkNameValidationError x y) = showCon d "MkNameValidationError" $ concatMap showArg [x, y]

public export
record EmailValidationError where
  constructor MkEmailValidationError
  message : String

Show EmailValidationError where
  showPrec d (MkEmailValidationError x) = showCon d "MkEmailValidationError" $ showArg x

public export
record QuantityValidationError where
  constructor MkQuantityValidationError
  condition : String
  message   : String

Show QuantityValidationError where
  showPrec d (MkQuantityValidationError x y) = showCon d "MkQuantityValidationError" $ concatMap showArg [x, y]

public export
data ValidationError
  = AddressValidation AddressValidationError
  | NameValidation NameValidationError
  | EmailValidation EmailValidationError
  | QuantityValidation QuantityValidationError

Show ValidationError where
  showPrec d (AddressValidation x)  = showCon d "AddressValidation"   $ showArg x
  showPrec d (NameValidation x)     = showCon d "NameValidation"      $ showArg x
  showPrec d (EmailValidation x)    = showCon d "EmailValidation"     $ showArg x
  showPrec d (QuantityValidation x) = showCon d "QuantityValidation"  $ showArg x

public export
data CheckedAddress = MkCheckedAddress AddressForm

namespace HtmlString

  public export
  data HtmlString = MkHtmlString String

  export
  (.value) : HtmlString -> String
  (.value) (MkHtmlString x) = x

public export
record OrderAcknowledgement where
  constructor MkOrderAcknowledgement
  emailAddress : EmailAddress
  letter       : HtmlString

public export
record OrderAcknowledgementSent where
  constructor MkOrderAcknowledgementSent
  orderId      : OrderId
  emailAddress : EmailAddress

public export
data ProductCodeErr = MkProductCodeErr String

Show ProductCodeErr where
  showPrec d (MkProductCodeErr x) = showCon d "MkProductCodeErr" $ showArg x

public export
record InvalidOrder where
  constructor MkInvalidOrder
  order             : OrderForm
  validationErrors  : List ValidationError
  productCodeErrors : List ProductCodeErr

Show InvalidOrder where
  showPrec d (MkInvalidOrder order validationErrors productCodeErrors)
    = showCon d "MkInvalidOrder" $ concat [showArg validationErrors, showArg productCodeErrors]

public export
data PlacedOrderEvent
  = OrderPlacedEvent         PricedOrder
  | BillableOrderPlacedEvent BillableOrderPlaced
  | AcknowledgementSentEvent OrderAcknowledgementSent
  | InvalidOrderRegistered   InvalidOrder

export
Show PlacedOrderEvent where
  show (OrderPlacedEvent         x) = "PlacedOrderEvent"
  show (BillableOrderPlacedEvent x) = "BillableOrderPlacedEvent"
  show (AcknowledgementSentEvent x) = "AcknowledgementSentEvent"
  show (InvalidOrderRegistered   x) = "InvalidOrderRegistered: " ++ show x

createBillingEvent : PricedOrder -> Maybe BillableOrderPlaced
createBillingEvent pricedOrder = do
  if pricedOrder.amountToBill.value > 0
     then Just $ MkBillableOrderPlaced
                  { orderId        = pricedOrder.orderId
                  , billingAddress = pricedOrder.billingAddress
                  , amountToBill   = pricedOrder.amountToBill
                  }
     else Nothing

public export
record PricingError where
  constructor MkPricingError
  message : String

public export
data AckSent = Sent | NotSent

public export
record Uri where
  constructor MkUri
  address : String

public export
record ServiceInfo where
  constructor MkServiceInfo
  name     : String
  endpoint : Uri

public export
record RemoteServiceException where
  constructor MkRemoteServiceException
  message : String

public export
record RemoteServiceError where
  constructor MkRemoteServiceError
  serviceInfo : ServiceInfo
  exception   : RemoteServiceException

public export
data PlaceOrderError
  = MkPlaceOrderError String
  | ValidationErrors (List ValidationError)
  | ProductCodeError ProductCodeErr
  | PriceOrderError PricingError
  | RemoteServiceErr RemoteServiceError

export
Show PlaceOrderError where
  show (MkPlaceOrderError e)  = "MkPlaceOrderError: " ++ e
  show (ValidationErrors xs)  = "ValidationErrors"
  show (ProductCodeError x)   = "ProductCodeError"
  show (PriceOrderError x)    = "PriceOrderError"
  show (RemoteServiceErr x)   = "RemoteServiceErr"

maybeValidationErrors : PlaceOrderError -> Maybe (List ValidationError)
maybeValidationErrors (ValidationErrors es) = Just es
maybeValidationErrors _ = Nothing

maybeProductCodeError : PlaceOrderError -> Maybe ProductCodeErr
maybeProductCodeError (ProductCodeError e) = Just e
maybeProductCodeError _ = Nothing

||| Place Order Monad
|||
||| PlaceOrderDSL is shorthand for PlaceOrderMonad. This is a syntactical constructs of the
||| different expressions that can be build in the PlaceOrder domain. Because
||| PlaceOrderDSL has Pure and Bind it inposes a monadic structure, but PlaceOrderDSL is purely syntactic
||| construction. Categorically it is a commands inlined free monad.
export
data PlaceOrderDSL : Type -> Type where
  -- Monad interface
  Pure : a -> PlaceOrderDSL a
  Bind : PlaceOrderDSL a -> Inf (a -> PlaceOrderDSL b) -> PlaceOrderDSL b

  -- Throwing some error
  -- Throwing error needs to help the type-checker with the expected type of the
  -- PlaceOrderDSL result.
  ThrowError : (a : Type) -> PlaceOrderError -> PlaceOrderDSL a
  CatchError : {a : Type} -> PlaceOrderDSL a -> PlaceOrderDSL (Either PlaceOrderError a)

  -- Order handling
  NewOrderId : PlaceOrderDSL OrderId
  NewOrderLineId : PlaceOrderDSL OrderLineId

  -- Validate Order Commands
  CheckProductCodeExists : ProductCode -> PlaceOrderDSL Bool
  CheckAddressExists     : AddressForm -> PlaceOrderDSL (Either CheckedAddressValidationError CheckedAddress)

  -- Price Order Commands
  GetProductPrice : ProductCode -> PlaceOrderDSL Price
  PlacePricedOrder : PricedOrder -> PlaceOrderDSL ()

  -- Acknowledgement Order Commands
  CreateOrderAcknowledgementLetter : PricedOrder -> PlaceOrderDSL HtmlString
  SendOrderAcknowledgement : OrderAcknowledgement -> PlaceOrderDSL AckSent

export
Functor PlaceOrderDSL where
  map f m = Bind m (Pure . f)

export
Applicative PlaceOrderDSL where
  pure = Pure
  f <*> x = Bind f (\f' => Bind x (\x' => Pure (f' x')))

export
Monad PlaceOrderDSL where
  join  m = Bind m id
  m >>= k = Bind m k

||| A model for the PlaceOrderDSL structure.
|||
||| As PlaceOrderDSL is purely a syntactical construct, we need to give a semantical model for such
||| a construct. Semantical models can be given for PlaceOrderDSL in any monad where we can give
||| interpretetations of the PlaceOrderDSL constructs.
||| Categorically this is a monad morphism between the PlaceOrderDSL monad an interpretation monad if it.
public export
record Model (m : Type -> Type) where
  constructor MkModel
  throwError
    : {a : Type} -> PlaceOrderError -> m a
  catchError
    : {a : Type} -> m a -> m (Either PlaceOrderError a)
  newOrderId
    : m OrderId
  newOrderLineId
    : m OrderLineId
  checkProductCodeExists
    : ProductCode -> m Bool
  checkAddressExists
    : AddressForm -> m (Either CheckedAddressValidationError CheckedAddress)
  getProductPrice
    : ProductCode -> m Price
  placePricedOrder
    : PricedOrder -> m ()
  createOrderAcknowledgementLetter
    : PricedOrder -> m HtmlString
  sendOrderAcknowledgement
    : OrderAcknowledgement -> m AckSent

||| The function that gives interpretation of a PlaceOrderDSL expression in the monad 'm' using the
||| given model.
export
interpret : Monad m => Model m -> PlaceOrderDSL a -> m a
interpret model (Pure x)                             = pure x
interpret model (Bind m k)                           = interpret model m >>= (interpret model . k)
interpret model (ThrowError _ x)                     = model.throwError x
interpret model (CatchError x)                       = model.catchError (interpret model x)
interpret model NewOrderId                           = model.newOrderId
interpret model NewOrderLineId                       = model.newOrderLineId
interpret model (CheckProductCodeExists x)           = model.checkProductCodeExists x
interpret model (CheckAddressExists x)               = model.checkAddressExists x
interpret model (GetProductPrice x)                  = model.getProductPrice x
interpret model (PlacePricedOrder x)                 = model.placePricedOrder x
interpret model (CreateOrderAcknowledgementLetter x) = model.createOrderAcknowledgementLetter x
interpret model (SendOrderAcknowledgement x)         = model.sendOrderAcknowledgement x

checkCustomerInfoForm : CustomerInfoForm -> Form ValidationError CustomerInfo
checkCustomerInfoForm customer =
  MkCustomerInfo
    <$> (MkPersonalName
          <$> field customer.firstName
                    (StringN.create 50)
                    (NameValidation (MkNameValidationError "First name" customer.firstName))
          <*> field customer.lastName
                    (StringN.create 50)
                    (NameValidation (MkNameValidationError "Last name" customer.lastName)))
    <*> field customer.emailAddress
              EmailAddress.create
              (EmailValidation (MkEmailValidationError customer.emailAddress))

createCustomerInfo : CustomerInfoForm -> PlaceOrderDSL CustomerInfo
createCustomerInfo customer = do
  let Value customerInfo = checkCustomerInfoForm customer
      | Error es => ThrowError CustomerInfo $ ValidationErrors es
  pure customerInfo

checkAddressForm : AddressForm -> Form AddressValidationError Address
checkAddressForm addr =
  MkAddress
    <$> field addr.addressLine1 (StringN.create 50) (MkAddressLineError addr.addressLine1)
    <*> optionalField addr.addressLine2 (StringN.create 50) (MkAddressOptLineError addr.addressLine2)
    <*> optionalField addr.addressLine3 (StringN.create 50) (MkAddressOptLineError addr.addressLine3)
    <*> optionalField addr.addressLine4 (StringN.create 50) (MkAddressOptLineError addr.addressLine4)
    <*> field addr.city (StringN.create 50) (MkAddressCityError addr.city)
    <*> field addr.zipCode ZipCode.create   (MkAddressZipCodeError addr.zipCode)

toAddress : AddressForm -> PlaceOrderDSL Address
toAddress addressForm = do
  Right (MkCheckedAddress checkedAddressForm) <- CheckAddressExists addressForm
    | Left e => ThrowError Address
                  $ ValidationErrors
                      [AddressValidation $ CheckedAddressError e]
  let Value addr = checkAddressForm checkedAddressForm
      | Error es => ThrowError Address $ ValidationErrors $ map AddressValidation es
  pure addr

toProductCode : String -> PlaceOrderDSL ProductCode
toProductCode productCodeStr = do
  let Just productCode = mkProductCode productCodeStr
      | _ => ThrowError ProductCode
              $ ProductCodeError
              $ MkProductCodeErr
              $ "Invalid product code " ++ productCodeStr
  True <- CheckProductCodeExists productCode
    | _ => ThrowError ProductCode
            $ ProductCodeError
            $ MkProductCodeErr
            $ "Product doesn't exist " ++ productCodeStr
  pure productCode

toOrderQuantity : ProductCode -> String -> PlaceOrderDSL OrderQuantity
toOrderQuantity (WidgetProduct wp) quantity = do
  let Just integer = the (Maybe Integer) $ parseInteger quantity
      | _ => ThrowError OrderQuantity
              $ ValidationErrors
                  [ QuantityValidation (MkQuantityValidationError "Integer" quantity) ]
  let Just between = mkBetween integer
      | _ => ThrowError OrderQuantity
              $ ValidationErrors
                  [ QuantityValidation (MkQuantityValidationError "in between" quantity) ]
  pure $ OrderUnitQuantity $ MkUnitQuantity between
toOrderQuantity (GizmoProduct gp) quantity = do
  let Just double = parseDouble quantity
      | _ => ThrowError OrderQuantity
              $ ValidationErrors
                  [ QuantityValidation (MkQuantityValidationError "Double" quantity) ]
  let Just between = mkBetween double
      | _ => ThrowError OrderQuantity
                $ ValidationErrors
                    [ QuantityValidation (MkQuantityValidationError "in between" quantity) ]
  pure $ OrderKilogramQuantity $ MkKilogramQuantity between

toValidatedOrderLine : OrderLineForm -> PlaceOrderDSL OrderLine
toValidatedOrderLine orderLineForm = do
  orderLineId <- NewOrderLineId
  productCode <- toProductCode orderLineForm.productCode
  quantity    <- toOrderQuantity productCode orderLineForm.quantity
  pure $ MkOrderLine
    { orderLineId = orderLineId
    , productCode = productCode
    , quantity    = quantity
    }

export
validateOrder : OrderForm -> PlaceOrderDSL (Either InvalidOrder Order)
validateOrder orderForm = do
  orderId      <- NewOrderId
  customerInfo <- createCustomerInfo $ orderForm.customerInfo
  address      <- toAddress $ orderForm.shippingAddress
  orderLines   <- traverse (CatchError . toValidatedOrderLine) orderForm.orderLines
  pure $ case partitionEithers orderLines of
    ([], orderLines)
      => Right $ MkOrder
          { orderId         = orderId
          , customerInfo    = customerInfo
          , shippingAddress = MkShippingAddress address
          , billingAddress  = MkBillingAddress address
          , orderLines      = orderLines
          }
    (errors, orderLines)
      => Left $ MkInvalidOrder
          { order  = orderForm
          , validationErrors = concat $ mapMaybe maybeValidationErrors errors
          , productCodeErrors = mapMaybe maybeProductCodeError errors
          }

-- The Pricing Step

toPricedOrderLine : OrderLine -> PlaceOrderDSL PricedOrderLine
toPricedOrderLine orderLine = do
  let quantity = orderLine.quantity.value
  priceVal <- GetProductPrice $ orderLine.productCode
  let price = multiply priceVal quantity
  pure $ MkPricedOrderLine
    { orderLine = orderLine
    , price     = price
    }

export
priceOrder : Order -> PlaceOrderDSL PricedOrder
priceOrder order = do
  pricedOrderLines <- traverse toPricedOrderLine order.orderLines
  let amountToBill = sumPrices $ map price pricedOrderLines
  pure $ MkPricedOrder
    { orderId         = order.orderId
    , customerInfo    = order.customerInfo
    , shippingAddress = order.shippingAddress
    , billingAddress  = order.billingAddress
    , orderLines      = pricedOrderLines
    , amountToBill    = amountToBill
    }

-- The Acknowledge Order Step

export
acknowledgeOrder : PricedOrder -> PlaceOrderDSL (Maybe OrderAcknowledgementSent)
acknowledgeOrder pricedOrder = do
  letter <- CreateOrderAcknowledgementLetter pricedOrder
  let acknowledgement
        = MkOrderAcknowledgement
        { emailAddress = pricedOrder.customerInfo.emailAddress
        , letter       = letter
        }
  case !(SendOrderAcknowledgement acknowledgement) of
    Sent =>
      pure
        $ Just
        $ MkOrderAcknowledgementSent
            { orderId      = pricedOrder.orderId
            , emailAddress = pricedOrder.customerInfo.emailAddress
            }
    NotSent =>
      pure Nothing

-- Place order step

export
placePricedOrder : PricedOrder -> PlaceOrderDSL ()
placePricedOrder = PlacePricedOrder

export
createEvents : PricedOrder -> Maybe OrderAcknowledgementSent -> List PlacedOrderEvent
createEvents pricedOrder orderAcknowledgementSent =
  catMaybes
    [ Just $ OrderPlacedEvent pricedOrder
    , map AcknowledgementSentEvent orderAcknowledgementSent
    , map BillableOrderPlacedEvent $ createBillingEvent pricedOrder
    ]
```

## File: `src/BoundedContext/OrderTaking/Workflow/PlaceOrder/Overview.idr`
```
module BoundedContext.OrderTaking.Workflow.PlaceOrder.Overview

import Rango.BoundedContext.Workflow

%default total

-- Overview of the Place Order workflow:
--
-- The incoming order form gets validated
-- - if valid it is registered
-- - if not it is rejected

-- More precisely this can be represented as the following state transition:

-- 
--                                                 ┌────────────────────────────┐
--                                                 │         OrderForm          │
--                                                 └────────────────────────────┘
--                                                   │
--                                                   │ Validate Order
--                                                   ▼
-- ┌─────────────┐    Create valid                 ┌============================┐
-- │ ValidOrder  │   ◀──────────────────────────   I           Order            I
-- └─────────────┘                                 └============================┘
--   │                                               │
--   │ Price                                         │ Create invalid
--   ▼                                               ▼
-- ┌─────────────┐                                 ┌────────────────────────────┐
-- │ PricedOrder │                                 │        InvalidOrder        │
-- └─────────────┘                                 └────────────────────────────┘
--   │                                               │
--   │                                               │ Queue
--   │                                               ▼
--   │                                             ┌────────────────────────────┐
--   │                                             │     InvalidOrderQueued     │
--   │                                             └────────────────────────────┘
--   │                                               │
--   │                                               │ Create invalid order info
--   │                                               ▼
--   │               Create priced order info      ┌────────────────────────────┐
--   └─────────────────────────────────────────▶   │         OrderInfo          │
--                                                 └────────────────────────────┘
-- 

-- Nodes represent the information we have, and edges represent the commands
-- that transforms information in this workflow.
-- Commands that have the same starting node are checks/decisions, one possible
-- path is selected during the interpretation of this process.
-- 
-- As in the order taking example, when we have an Order, it can be valid or invalid.

-- Next step is to represent this state transition in Idris as indexed datatypes.

||| States of the Order-Taking 
public export
data State
  = OrderForm
  | Order
  | ValidOrder
  | PricedOrder
  | InvalidOrder
  | InvalidOrderQueued
  | OrderInfo

-- The State is a simple ADT with some constructors.

||| Check of the OrderTaking transition;
|||
||| Decide if an order is valid or invalid.
public export
data Check : State -> State -> State -> Type where
  CheckInvalidOrder : Check Order InvalidOrder ValidOrder

-- The Check is an indexed datatype with three indices, all the three indices are type of State.

||| State transition of the OrderTaking workflow.
public export
data Step : State -> State -> Type where
  ValidateOrder     : Step OrderForm           Order
  AddInvalidOrder   : Step InvalidOrder        InvalidOrderQueued
  PriceOrder        : Step ValidOrder          PricedOrder
  SendAckToCustomer : Step PricedOrder         OrderInfo
  SendInvalidOrder  : Step InvalidOrderQueued  OrderInfo

-- The Step is another indexed datatype, with two indices of State values.

||| Workflow definiton of the state transition system.
|||
||| See the graph above. This workflow represents an order-taking
||| process, which accepts or rejects an order, if the order
||| is accepted than prices it, if the order is invalid
||| registers it as an invalid order. In both cases it sends
||| information about that state of the order to the customer
public export
workflow : Workflow Step Check OrderForm OrderInfo
workflow = do
  Do ValidateOrder
  Branch CheckInvalidOrder
    (do Do AddInvalidOrder
        Do SendInvalidOrder)
    (do Do PriceOrder
        Do SendAckToCustomer)

-- In Idris the 'do' notation is tied to the the (>>) and the (>>=) bind operatiors, any type
-- that implements those operators is able to use the 'do' notation. This is a sintactical sugar
-- and helps us to write code which can be read naturally, in sequence and in branching.
-- This approach fits well to the sequential nature of the workflows.

---------------------------------------------------------------------------------------------------

-- Graph Source:
-- 
-- digraph {
--  OrderForm          -> Order [label="Validate Order"];
--  InvalidOrder       -> InvalidOrderQueued [label="Queue"];
--  ValidOrder         -> PricedOrder [label="Price"]; 
--  PricedOrder        -> OrderInfo [label="Create priced order info"];
--  InvalidOrderQueued -> OrderInfo [label="Create invalid order info"];
--
--  Order -> ValidOrder   [label="Create valid"];
--  Order -> InvalidOrder [label="Create invalid"];
-- }
-- 
```

## File: `src/BoundedContext/OrderTaking/Workflow/PlaceOrder/Database/ConvertDTO.idr`
```
module BoundedContext.OrderTaking.Workflow.PlaceOrder.Database.ConvertDTO

import BoundedContext.OrderTaking.Workflow.PlaceOrder.Database.DTO
import BoundedContext.OrderTaking.Workflow.PlaceOrder.Domain

import Data.StringN

export toPricedOrderDTO : PricedOrder -> PricedOrderDTO
export toProductCodeDTO : ProductCode -> ProductCodeDTO
export toProductDTO : Product -> ProductDTO


orderIdentifier         : OrderId     -> Identifier
orderLineIdentifier     : OrderLineId -> Identifier
toCustomerDTO           : Identifier  -> CustomerInfo    -> CustomerDTO
toAddressDTO            : Identifier  -> Address         -> AddressDTO
fromBillingAddress      : Identifier  -> BillingAddress  -> AddressDTO
fromShippingAddress     : Identifier  -> ShippingAddress -> AddressDTO
toPricedOrderLineDTO    : Identifier  -> PricedOrderLine -> PricedOrderLineDTO

-- Order

orderIdentifier     (MkOrderId x)     = x
orderLineIdentifier (MkOrderLineId x) = x

toPricedOrderDTO p
  = let oid = orderIdentifier p.orderId
    in MkPricedOrderDTO
        { identifier      = oid
        , customer        = toCustomerDTO                  oid p.customerInfo
        , shippingAddress = fromShippingAddress            oid p.shippingAddress
        , billingAddress  = fromBillingAddress             oid p.billingAddress
        , orderLines      = map (toPricedOrderLineDTO oid) p.orderLines
        , amount          = p.amountToBill.value
        }

toCustomerDTO i c
  = MkCustomerDTO
    { identifier   = i
    , firstName    = c.personalName.firstName.value
    , lastName     = c.personalName.lastName.value
    , emailAddress = c.emailAddress.value
    }

toAddressDTO i a
  = MkAddressDTO
    { identifier   = i
    , addressLine1 = a.addressLine1.value
    , addressLine2 = map (.value) a.addressLine2
    , addressLine3 = map (.value) a.addressLine3
    , addressLine4 = map (.value) a.addressLine4
    , city         = a.city.value
    , zipCode      = a.zipCode.value
    }

fromBillingAddress  i (MkBillingAddress  ba) = toAddressDTO (i ++ "-BLN") ba
fromShippingAddress i (MkShippingAddress sa) = toAddressDTO (i ++ "-SHP") sa

toPricedOrderLineDTO i po
  = MkPricedOrderLineDTO
    { identifier  = i ++ "-PO-" ++ orderLineIdentifier po.orderLine.orderLineId
    , productCode = po.orderLine.productCode.value
    , quantity    = po.orderLine.quantity.value
    , price       = po.price.value
    }

-- Product

toProductCodeDTO (WidgetProduct (MkWidgetCode x)) = MkProductCodeDTO x
toProductCodeDTO (GizmoProduct (MkGizmoCode x))   = MkProductCodeDTO x

toProductDTO (MkProduct productCode price description)
  = MkProductDTO
    { productCode = toProductCodeDTO productCode
    , price       = price.value
    , description = description.value
    }
```

## File: `src/BoundedContext/OrderTaking/Workflow/PlaceOrder/Database/DTO.idr`
```
module BoundedContext.OrderTaking.Workflow.PlaceOrder.Database.DTO

import Rango.DataTransfer.JSON.Derive

%language ElabReflection
%default total


public export
Identifier : Type
Identifier = String

public export
record AddressDTO where
  constructor MkAddressDTO
  identifier   : Identifier
  addressLine1 : String
  addressLine2 : (Maybe String)
  addressLine3 : (Maybe String)
  addressLine4 : (Maybe String)
  city         : String
  zipCode      : String

public export
record OrderLineDTO where
  constructor MkOrderLineDTO
  identifier  : Identifier
  productCode : String
  quantity    : String

public export
record PricedOrderLineDTO where
  constructor MkPricedOrderLineDTO
  identifier  : Identifier
  productCode : String
  quantity    : Double
  price       : Double

public export
record CustomerDTO where
  constructor MkCustomerDTO
  identifier   : Identifier
  firstName    : String
  lastName     : String
  emailAddress : String

public export
record OrderDTO where
  constructor MkOrderDTO
  identifier      : Identifier
  customer        : CustomerDTO
  shippingAddress : AddressDTO
  billingAddress  : AddressDTO
  orderLines      : List OrderLineDTO

public export
record PricedOrderDTO where
  constructor MkPricedOrderDTO
  identifier      : Identifier
  customer        : CustomerDTO
  shippingAddress : AddressDTO
  billingAddress  : AddressDTO
  orderLines      : List PricedOrderLineDTO
  amount          : Double

public export
record ProductCodeDTO where
  constructor MkProductCodeDTO
  productCode : String

public export
record ProductDTO where
  constructor MkProductDTO
  productCode : ProductCodeDTO
  price       : Double
  description : String

%runElab deriveJSON defaultOpts `{AddressDTO}
%runElab deriveJSON defaultOpts `{OrderLineDTO}
%runElab deriveJSON defaultOpts `{PricedOrderLineDTO}
%runElab deriveJSON defaultOpts `{CustomerDTO}
%runElab deriveJSON defaultOpts `{OrderDTO}
%runElab deriveJSON defaultOpts `{PricedOrderDTO}
%runElab deriveJSON defaultOpts `{ProductCodeDTO}
%runElab deriveJSON defaultOpts `{ProductDTO}
```

## File: `src/BoundedContext/OrderTaking/Workflow/PlaceOrder/Database/Order.idr`
```
module BoundedContext.OrderTaking.Workflow.PlaceOrder.Database.Order

import public Control.Monad.Either

import BoundedContext.OrderTaking.Workflow.PlaceOrder.Database.DTO

import Data.String
import Control.Monad.Trans
import Control.Monad.Reader

import Rango.DataTransfer.SQL.Syntax
import Rango.Database.SQLite
import Service.NodeJS.SQLite
import Service.NodeJS.Promise


||| Value like table, meaning that it is highly redundant
addressTable : Table
addressTable = MkTable
  "address"
  [ field "id"    SQL_Text [PrimaryKey]
  , field "line1" SQL_Text [NotNull]
  , field "line2" SQL_Text []
  , field "line3" SQL_Text []
  , field "line4" SQL_Text []
  , field "city"  SQL_Text [NotNull]
  , field "zip"   SQL_Text [NotNull]
  ]
  []
  YesOfCourseValid

customerTable : Table
customerTable = MkTable
  "customer"
  [ field "id"         SQL_Text [PrimaryKey]
  , field "first_name" SQL_Text [NotNull]
  , field "last_name"  SQL_Text [NotNull]
  , field "email"      SQL_Text [NotNull]
  ]
  [ Unique "email_unqiue" ["email"] ]
  YesOfCourseValid

pricedOrderLineTable : Table
pricedOrderLineTable = MkTable
  "priced_order_line"
  [ field "id"            SQL_Text     [PrimaryKey]
  , field "product_code"  SQL_Text     [NotNull]
  , field "quantity"      SQL_Double   [NotNull]
  , field "price"         SQL_Double   [NotNull]
  ]
  []
  YesOfCourseValid

pricedOrderLinesTable : Table
pricedOrderLinesTable = MkTable
  "priced_order_lines"
  [ field "ordr"        SQL_Text [NotNull]
  , field "order_line"  SQL_Text [NotNull]
  ]
  [ ForeignKey "order_line" "priced_order_line" "id"
  , Unique "unique_key_lines" ["ordr", "order_line"]
  ]
  YesOfCourseValid

pricedOrderTable : Table
pricedOrderTable = MkTable
  "priced_order"
  [ field "id"                SQL_Text    [PrimaryKey]
  , field "customer"          SQL_Text    [NotNull]
  , field "shipping_address"  SQL_Text    [NotNull]
  , field "billing_address"   SQL_Text    [NotNull]
  , field "amount_to_bill"    SQL_Double  [NotNull]
  ]
  [ ForeignKey "customer"         "customer"    "id"
  , ForeignKey "shipping_address" "address"     "id"
  , ForeignKey "billing_address"  "address"     "id"
  ]
  YesOfCourseValid

public export
data OrderDBError
  = SaveAddressError String
  | SaveCustomerError String
  | SavePricedOrderLineError String
  | SaveOrderError String
  | InitializeError String

export
Show OrderDBError where
  showPrec d (SaveAddressError          x) = "SaveAddressError: " ++ x 
  showPrec d (SaveCustomerError         x) = "SaveCustomerError: " ++ x
  showPrec d (SavePricedOrderLineError  x) = "SavePricedOrderLineError: " ++ x
  showPrec d (SaveOrderError            x) = "SaveOrderError: " ++ x
  showPrec d (InitializeError           x) = "InitializeError: " ++ x

export
OrderDB : Type -> Type
OrderDB a = EitherT OrderDBError (ReaderT Database Promise) a

export
runOrderDB : Database -> OrderDB a -> Promise (Either OrderDBError a)
runOrderDB db m = runReaderT db (runEitherT m)

throwIfFail : (String -> OrderDBError) -> Promise SomeError -> OrderDB ()
throwIfFail mkError p = do
  NoError <- lift (lift p)
    | HasError err => throwError $ mkError !(toString err)
  pure ()

export
saveAddress : AddressDTO -> OrderDB ()
saveAddress (MkAddressDTO identifier addressLine1 addressLine2 addressLine3 addressLine4 city zipCode) = do
  db <- ask
  throwIfFail SaveAddressError $ Database.run db $ renderCommand $
    Insert addressTable
      [ FieldOf "id"     (SQLText identifier)
      , FieldOf "line1"  (SQLText addressLine1)
      , FieldOf "line2"  (SQLText <$> addressLine2)
      , FieldOf "line3"  (SQLText <$> addressLine3)
      , FieldOf "line4"  (SQLText <$> addressLine4)
      , FieldOf "city"   (SQLText city)
      , FieldOf "zip"    (SQLText zipCode)
      ]

export
saveCustomer : CustomerDTO -> OrderDB ()
saveCustomer (MkCustomerDTO identifier firstName lastName emailAddress) = do
  db <- ask
  throwIfFail SaveCustomerError $ Database.run db $ renderCommand $
    Insert customerTable
      [ FieldOf "id"          (SQLText emailAddress)
      , FieldOf "first_name"  (SQLText firstName)
      , FieldOf "last_name"   (SQLText lastName)
      , FieldOf "email"       (SQLText emailAddress)
      ]

export
savePricedOrderLine : PricedOrderLineDTO -> OrderDB ()
savePricedOrderLine (MkPricedOrderLineDTO identifier productCode quantity price) = do
  db <- ask
  throwIfFail SavePricedOrderLineError $ Database.run db $ renderCommand $
    Insert pricedOrderLineTable
      [ FieldOf "id"            (SQLText identifier)
      , FieldOf "product_code"  (SQLText productCode)
      , FieldOf "quantity"      (SQLDouble quantity)
      , FieldOf "price"         (SQLDouble price)
      ]

export
saveOrder : PricedOrderDTO -> OrderDB ()
saveOrder (MkPricedOrderDTO identifier customer shippingAddress billingAddress orderLines amount) = do
  db <- ask
  saveCustomer customer
  saveAddress shippingAddress
  saveAddress billingAddress
  traverse_ savePricedOrderLine orderLines
  throwIfFail SaveOrderError $ Database.run db $ renderCommand $
    Insert pricedOrderTable
      [ FieldOf "id"               (SQLText identifier)
      , FieldOf "customer"         (SQLText customer.identifier)
      , FieldOf "shipping_address" (SQLText shippingAddress.identifier)
      , FieldOf "billing_address"  (SQLText billingAddress.identifier)
      , FieldOf "amount_to_bill"   (SQLDouble amount)
      ]
  for_ orderLines $ \(MkPricedOrderLineDTO orderIdentifier productCode quantity price) => do
    throwIfFail SaveOrderError $ Database.run db $ renderCommand $
      Insert pricedOrderLinesTable
        [ FieldOf "ordr"        (SQLText identifier)
        , FieldOf "order_line"  (SQLText orderIdentifier)
        ]

export
initDB : IO ()
initDB = do
  sqlite <- SQLite.require
  resolve' (\_ => putStrLn "OK.") putStrLn $ do
    db <- either !(SQLite.database sqlite "./db/order.db")
    ignore $ command db $ CreateTable addressTable
    ignore $ command db $ CreateTable customerTable
    ignore $ command db $ CreateTable pricedOrderLineTable
    ignore $ command db $ CreateTable pricedOrderLinesTable
    ignore $ command db $ CreateTable pricedOrderTable
    ignore $ Database.close db
```

## File: `src/BoundedContext/OrderTaking/Workflow/PlaceOrder/Database/Product.idr`
```
module BoundedContext.OrderTaking.Workflow.PlaceOrder.Database.Product

import public Control.Monad.Either

import Data.Maybe
import Data.String
import Control.Monad.Trans
import Control.Monad.Reader
import Language.JSON.Schema

import Rango.DataTransfer.SQL.Syntax
import Rango.Database.SQLite
import Service.NodeJS.SQLite
import Service.NodeJS.Promise
import Service.NodeJS.JSON

import BoundedContext.OrderTaking.Workflow.PlaceOrder.Database.DTO


productTable : Table
productTable = MkTable
  "product"
  [ field "id"          SQL_Integer [PrimaryKey, AutoIncrement]
  , field "code"        SQL_Text    [NotNull]
  , field "description" SQL_Text    [NotNull]
  , field "price"       SQL_Double  [NotNull]
  ]
  [ Unique "code_unique" ["code"] ]
  YesOfCourseValid

public export
data ProductDBError
  = InitializeError String
  | SaveProductError String
  | ProductRetrieveError String
  | ConversionError String

export
Show ProductDBError where
  show (InitializeError       e) = "InitializeError: " ++ show e
  show (SaveProductError      e) = "SaveProductError: " ++ show e
  show (ProductRetrieveError  e) = "ProductRetrieveError: " ++ show e
  show (ConversionError       e) = "ConversionError: " ++ show e 

export
ProductDB : Type -> Type
ProductDB a = EitherT ProductDBError (ReaderT Database Promise) a

export
runProductDB : Database -> ProductDB a -> Promise (Either ProductDBError a)
runProductDB db m = runReaderT db (runEitherT m)

throwIfFail : (String -> ProductDBError) -> Promise SomeError -> ProductDB ()
throwIfFail mkError p = do
  NoError <- lift (lift p)
    | HasError err => throwError $ mkError !(toString err)
  pure ()

throwIfFailE : (String -> ProductDBError) -> Promise (Either Error a) -> ProductDB a
throwIfFailE mkError p = do
  Right result <- lift (lift p)
    | Left err => throwError $ mkError !(toString err)
  pure result

throwOnError : (String -> ProductDBError) -> Promise (Database.Safe.Result s) ->  ProductDB (Maybe (Indexed.JSON s))
throwOnError mkError p = do
  Row json <- lift (lift p)
    | EmptyRow      => pure Nothing
    | GetError  err => throwError $ mkError !(toString err)
    | JSONError err => throwError $ mkError err
  pure (Just json)

export
saveProduct : ProductDTO -> ProductDB ()
saveProduct (MkProductDTO (MkProductCodeDTO productCode) price description) = do
  db <- ask
  throwIfFail SaveProductError $ Database.run db $ renderCommand $
    Insert productTable
      [ FieldOf "code"        (SQLText productCode)
      , FieldOf "description" (SQLText description)
      , FieldOf "price"       (SQLDouble price)
      ]

export
productExists : ProductCodeDTO -> ProductDB Bool
productExists (MkProductCodeDTO productCode) = do
  db  <- ask
  res <- throwOnError ProductRetrieveError
       $ Rango.Database.SQLite.query db
       $ Select ["code", "description", "price"] productTable [("code", "=", "'\{productCode}'")]
  pure $ isJust res

export
productPrice : ProductCodeDTO -> ProductDB Double
productPrice (MkProductCodeDTO productCode) = do
  db <- ask
  Just json <- throwOnError ProductRetrieveError
             $ Rango.Database.SQLite.query db
             $ Select ["price"] productTable [("code", "=", "'\{productCode}'")]
    | Nothing => throwError $ ProductRetrieveError $ show productCode
  pure (getField json "price")

export
initDB : IO ()
initDB = do
  sqlite <- SQLite.require
  resolve' (\_ => putStrLn "OK.") putStrLn $ do
    db <- either !(SQLite.database sqlite "./db/product.db")
    ignore $ Database.run db $ renderCommand $ CreateTable productTable
    ignore $ Database.run db $ renderCommand $ Insert productTable
      [ FieldOf "code"        (SQLText "g21")
      , FieldOf "description" (SQLText "A fluffy gizmo toy")
      , FieldOf "price"       (SQLDouble 24.00)
      ]
    ignore $ Database.close db
```

## File: `src/Data/Between.idr`
```
module Data.Between

%default total

||| Simple datatype which ensures that the boxed value is in the given range, using smart
||| constructors.
export
data Between : (numType : Type) -> (l : numType) -> (h : numType) -> Type where
  MkBetween : (x : numType) -> Between numType l h

||| Smart constructor for the Between datatype.
export
mkBetween : {n : Type} -> Ord n => {l , h : n} -> (x : n) -> Maybe (Between n l h)
mkBetween x = do
  let True = l <= h
      | _ => Nothing
  let True = l <= x
      | _ => Nothing
  let True = x <= h
      | _ => Nothing
  Just $ MkBetween x

||| Value extraction.
export
(.value) : Between n l h -> n
(.value) (MkBetween v) = v
```

## File: `src/Data/Form.idr`
```
module Data.Form

%default total

||| Simple Applicative Form which collects the errors of the form.
||| 
||| During the form processing error can occur for any fields,
||| its better to collect them all, rather stopping at the first
||| one. 
|||
||| This abstraction is used in OrderTaking processing.
||| It is not a general form processing for the UI.
public export
data Form : Type -> Type -> Type where
  Error : List e -> Form e a
  Value : a      -> Form e a

-- The definition of the 'Form' is another way to introduce
-- a datatype. This datatype has two type parameters and
-- two data constructors.
-- The two type parameter come from the ': Type -> Type ->' part of
-- the definition. In a bit more technical term, the Form
-- datatype has two parameters/indices. In this case the parameters
-- refer to other types. Not only 'Type' can be an index, but
-- any other value of any type, such as values of 'Nat'. We will
-- a complex example of that.

export
Functor (Form e) where
  map f (Error es) = Error es
  map f (Value x)  = Value (f x)

-- In Idris we can define interfaces which represent a set of functions
-- associated with one or more types. The implementation of the
-- functions in the interface should differ from implementation to
-- implementation.
--
-- As technicality; the interfaces are compiled to dependent records.
--
-- One of the standard interfaces is the Functor
-- interface, which gives the ability of mapping, if the given
-- datatype is parametrized.

export
Applicative (Form e) where
  pure x = Value x
  Error es1 <*> Error es2 = Error (es1 ++ es2)
  Error es1 <*> Value x   = Error es1
  Value f   <*> Error es1 = Error es1
  Value f   <*> Value x   = Value (f x)

-- Another standard interface in Idris is the Applicative, which is
-- an extension of the function and it gives the ability of
-- apply a wrapped function to a wraped value inside the datatype.

||| A field value and its parser.
|||
||| If the parsing fails, the error is emmited.
export
field : a -> (a -> Maybe b) -> Lazy e -> Form e b
field v f e = maybe (Error [e]) Value $ f v

||| An optional field and its parser.
|||
||| If the value is present, than parsing happens, on
||| fail the error is emmited.
export
optionalField : Maybe a -> (a -> Maybe b) -> Lazy e -> Form e (Maybe b)
optionalField Nothing f e  = Value Nothing
optionalField (Just v) f e = Just <$> field v f e
```

## File: `src/Data/Result.idr`
```
module Data.Result

||| Result
|||
||| This type is mentioned during the definition of the
||| OrderTaking process. I tried to follow Scott's
||| book as closely as possible.
public export
data Result r e
  = Ok r
  | Error e

-- The 'Result' is an example of introducing an Algebraic Datatype with
-- two type parameters 'r' and 'e'. The 'Result' has two data constructors;
-- 'Ok' and 'Error', both has one argument.

-- A note on the 'public export'. Idris controls visibility with these keywords.
-- For different things the keywords have different meaning. If nothing is written
-- then the definition will be private, only accessible withing the module or the
-- namespace. Every module introduces a namespace. In this example 'Data.Result'
-- If we want to use the definition outside of the namespace we have to add the
-- 'export' or the 'public export' keyword. The 'export' means we only export
-- the datatype but we e hide its constructors. The 'public export' exposes
-- the data constructors too.
```

## File: `src/Data/StringN.idr`
```
module Data.StringN

import Data.Nat

%default total

||| A string of maximum length n.
|||
||| StringN boxes a String and a compile time proof
||| (compile time because its quantity is 0) that the string
||| is shorter then 'n'.
export
data StringN : Nat -> Type where
  MkStringN : (s : String) -> (length s `LTE` m) => StringN m

-- StringN introduces and indexed datatype, with one data constructor.
-- The 'MkStringN' data constructor has two arguments, the first one
-- is a String, which has the name 's'. The second parameter is
-- an implicit argument, which doesn't need to given when the
-- MkStringN is used for creating value of the 'StringN' datatype.
-- This second argument is implicit because the '=>' is used after
-- its declaration. This tells Idris to search this parameter
-- from some active context. More explanation will come for
-- these when simpler datatypes are introduced.

||| A simple way of proving, or calculating the proof of 'LTE n m'
|||
||| This approach is simpler than creating a DecEq as we know that
||| the negative case of the proof, when 'n' is greater then 'm',
||| is irrelevant for us, and we don't spend time developing that
||| proof. See below.
mkLTE : (n , m : Nat) -> Maybe (n `LTE` m)
mkLTE 0     0     = Just LTEZero
mkLTE 0     (S k) = Just LTEZero
mkLTE (S k) 0     = Nothing
mkLTE (S k) (S j) = do
  proofLTE <- mkLTE k j
  Just (LTESucc proofLTE)

||| Smart constructor of the StringN type.
|||
||| If the given String is longer than the given length limit
||| the value can not be created.
export
create : (n : Nat) -> String -> Maybe (StringN n)
create n s = do
  -- As creating a value of StringN requires a proof that
  -- the length is ok, we need to call the function that
  -- creates that proof object for us, which is just a value
  -- of the type 'LTE n m' If we can create that value via
  -- the 'mkLTE' function we are safe, otherwise we can't create
  -- the value for 'StringN n'. When we are unable to create the LTE n m,
  -- because we got a longer String as the parameter, then mkLTE returns
  -- Nothing, which is picked up by the Monad instance of the Maybe, so
  -- at that point the create function returns Nothing.
  proofLTE <- mkLTE (length s) n
  -- If we are able to get a proof of 'LTE n m' than we can construct
  -- the StringN, because in the context we have a value which has the
  -- right type and the '-> (length s `LTE` m) =>' part of the StringN
  -- is able to pick that type up.
  -- Check for '=>' behavior in the Idris documentation
  Just $ MkStringN s

||| Value extraction
export
(.value) : StringN x -> String
(.value) (MkStringN s) = s

-- This first seems strange, but this will be convinient when combined with
-- records in Idris.
-- This is a postfix function. With this we can write code where we can chain
-- function calls from one another. Like 'x.value.f.g'
```

## File: `src/Language/JSON/Schema.idr`
```
module Language.JSON.Schema

-- Schema aware JSON representation.

import Data.List.Quantifiers
import Decidable.Equality
import Language.JSON
import Data.List

-- JSON schema can be represented as a simple dataype, which will be in use to
-- index a JSON value. We can pattern match on the expected shape of the JSON,
-- and client codes rely on the Schema, rather than doing JSON processing
-- blindly.
namespace Schema

  mutual

    -- Here we use mutual block to define datatypes that refer to each other
    -- during their definition.

    ||| Description of a JSON schema
    public export
    data Schema
        -- The JSON value of this schema is Null
      = Null
        -- The JSON value of this schema contains a Boolean
      | Boolean
        -- The JSON value of this schema contains a Number
      | Number
        -- The JSON value of this schema contains a String
      | Str
        -- The JSON value of this schema constains an Array where
        -- the elements have the schema from the list.
      | Array  (List Schema)
        -- The JSON value of this schema contains an Object where
        -- the fields of the object have the schema from the field
        -- list.
      | Object FieldList
        -- The JSON  value of this schema contains a value which
        -- has one of the schemas.
      | Either Schema Schema

    ||| A field could be optional or required in the JSON Object.
    public export
    data Presence = Optional | Required

    ||| Declaration of type for the Field description of a JSON object.
    |||
    ||| A field in the JSON object has a name, could be required or optional
    ||| field, and should have the given schema.
    public export
    Field : Type
    Field = (String, Presence, Schema)

    ||| Field description for a JSON object.
    public export
    FieldList : Type
    FieldList = List Field

-- Schema indexed JSON data representation.
namespace Indexed

  mutual
    
    ||| Schema indexed JSON representation.
    |||
    ||| The index holds a Schema definition which can be in use of determine
    ||| the expected shape of the JSON value. Having a schema as index helps
    ||| us to create clients codes and have strong assertions on data
    ||| coming from external sources, but validated with the schema,
    ||| which is computed from a separate input.
    |||
    ||| This way we can make connections beetwen SQL queries, their result
    ||| JSON and the client code that uses the result.
    public export
    data JSON : Schema -> Type where
      JNull    :                                        JSON Null
      JBoolean : Bool                                -> JSON Boolean
      JNumber  : Double                              -> JSON Number
      JString  : String                              -> JSON Str
      JArray   : {xs : List Schema}  -> All JSON xs  -> JSON (Array xs)
      JObject  : {xs : FieldList}    -> All Field xs -> JSON (Object xs)
      JLeft    : {l  : Schema}       -> JSON l       -> JSON (Either l r)
      JRight   : {r  : Schema}       -> JSON r       -> JSON (Either l r)

    -- The 'All' type requires some explanation.
    --
    -- A proof that all elements of a list satisfy a property. It is a list of
    -- proofs, corresponding element-wise to the `List`.
    -- data All : (0 p : a -> Type) -> List a -> Type where
    --   Nil  : All p Nil
    --   (::) : {0 xs : List a} -> p x -> All p xs -> All p (x :: xs)
    --
    -- It is a list like construction, but also holds to a predicate (something that is 'a -> Type')
    -- and applies creates a list using the predice applied to the list of its index 'xs'.
    -- If the index of 'All' has type of 'List Type', and the predicate is the identity we
    -- get the HList construction, which is able to store elements of different type, because we
    -- have the information about which index has which type. Example;
    -- 
    -- hlist : HList [Int, Bool, Int]
    -- hlist = [0,False,1] -- we can use syntactical sugar for list, because we have Nil and (::)
    --
    -- Another usecase for All is to create a list where the index represents index values for
    -- a given indexed types, and we create a list of indexed values of the same indexed type.
    -- In this case the JArray; All the elements of the JArray must be a JSON which requires
    -- a schema as index, for that reason we have to have a list of indexes, and we can use
    -- All to create a well-types list. For example
    -- 
    -- jarray : JSON (Array [Number, Boolean, Number])
    -- jarray = JArray [JNumber 0, JBoolean False, JNumber 1]
    -- 
    -- Similarly as we done in the case of 'hlist' example.

    ||| Field in the JSON object.
    |||
    ||| The field must have name, its presence can optional and its value
    ||| should have the given schema.
    public export
    data Field : (String, Presence, Schema) -> Type where
      ||| Required field in the JSON object; the value must be present.
      RequiredField : {f : String} ->         JSON s -> Field (f,Required,s)
      ||| Optional field in the JSON object; the value can be absent.
      OptionalField : {f : String} -> Maybe (JSON s) -> Field (f,Optional,s)

-- Our first constuctive proof like tool.
--
-- When we write a function that extracts a field from a JSON, lets call it
-- 'getField' we have the following design choices as engineers.
--
-- - Make the function partial, meaning that when the JSON value is not an Object
--   or the field is not in the object we don't cover that case, and we get a
--   runtime error.
--   In this case we lie to the client code, the code which calls our function,
--   about the nature of our function. Type tells us 'getField : FieldName -> JSON -> JSON' works for all
--   inputs without any problem, but also Idris tells us this function is 'partial'
--   and marks the function partial, also marks any other client codes partial.
--   Writing error correction code in this case is impossible.
--
-- - Make a precondition for the 'getFieldOk : String -> JSON -> Bool' and only call the 'getField' when the
--   precondition applies; such as;
--
--   if getFieldOk f json
--     then getField f json
--     else JNull
--
--   We can use this approach within the implementation of the getField or the client code of the getField.
--   In the former case we distort information, in the later, the client code's responsibility
--   to handle the error case accordingly, but the nature of the error why the field was not ok it stays
--   hidden.
--
-- - Make the partial function total, insead of creating 'getField : FieldName -> JSON -> JSON' partial
--   construction for all the non-handled inputs we can return Nothing, for
--   the handled parts we can return 'Just x'. Something like this; ''getField : FieldName -> JSON -> Maybe JSON'.
--   This forces the client code to act on partial nature of the problem, and handle
--   wrong inputs after learning the fact that the input was not ok, for the 'getField' function, becase
--   it returns Nothing. The client code not neceserily knows the reason why the getField returned
--   Nothing. Writing error correction code is possible, but the error sitation is not recoverable
--   from the result of the function.
--
-- - Make the function total, using its own return Domain, this domain enumerates all the possible
--   good and bad cases and let the client code act on it accordingly, something like
--
--   data GetFieldResult
--     = NotAnObject
--     | FieldNotFound
--     | FieldValue JSON
--
--   'getField : FieldName -> JSON -> GetFeildResult'
--
--   The client can act on the kind of the errourneous situations accordingly.
--
-- - The one which is one option if we have dependent types:
--   Make sure that the 'getField' function can be called only with a restricted set of
--   inputs, via an indexed JSON representation and indexed HasRequiredField datatype.
--   'getField : (f : FieldName) -> (s : Schema) -> JSON s -> HasRequiredField f s -> (z : Schema ** JSON z)'
--   We can call the HasRequiredField a witness of the field is being part of the schema, or we
--   can call this witness as a constructive proof; which shows us where to find the field
--   in the Schema definition if it can be found at all. If there field is not in the Schema represented
--   JSON object, than we can not create this witness at all, meaning that we don't have a value
--   which we would invoke the getField function.
--   The getField function fits to the general pattern of 'f : (x : a) -> (P x) -> b', which explanation as
--   if you can give me an 'x' and a some information that the 'x' will be ok for the 'f',
--   f is going to be ok. 
--     More technically, if you give me an x and the proof that x is an
--   element in the co-domain of the function, the function can executed safely.
--   This is another form of defensive programming, where the assertions before the
--   function call are precise and there is an explicit connection between the precondition
--   of the function and the implementation of the function.
--     We can improve the 'getField' function with auto search implicit parameters;
--   where Idris fills out these details if it is possible.
--
--   'getField : JSON s -> (f : String) -> {auto ok : HasRequiredField f s} -> (z : Schema ** JSON z)'
--
--   In cases where the parameters of the 'getField' are constant like values Idris is easily
--   able to create the witness for the field being in the schema, but in cases if we acquire the fieldName
--   or the schema definition from runtime value, we need to be able to create such a witness, for that
--   we need to create the function which creates the witness from the given values at runtime.
--   'hasRequiredField : (f : String) -> (s : Schema) -> Maybe (HasRequiredField f s)'
--   In this case we also provide the assumption check for the 'getField' function, which can
--   be used if Idris is not able to find the witness of the condition. If the runtime witness
--   creation returns Nothing, than the client code execute its defensive code-path.
--
-- - The other option is we have dependent types, that we push the previous approach, replacing
--   the '(z : Schema ** JSON z)' return value of the function, with a return type that we compute
--   from the learn 'z : Schema' value and from the constructive proof object.
--    In short if we have a proof that the schema contains a field, we can use this information
--   to calculate a return type for the 'getField' function.
--
--   'getField : JSON s -> (f : String) -> {auto ok : HasRequiredField f s} -> FieldType ok'
--
--   'FieldType : HasRequiredField f s -> Type' which builds on the 'SimpleType : Schema -> Type'
--   function. After the getField function finds the field using the 'HasRequiredField f s'
--   to navigate through the JSON object and retrieves the value and schema of the field,
--   the 'getSimpleValue' computes the return value of the function which will fit to
--   the Type computed by the 'FieldType' function.
--
--   This is a very strong guarantee that we do type-safe programming, because we actually
--   compute the type of the return value, based on the values of the 'getField' parameter.
--   With this approach we force the client code to adopt to the expected return type.
--   When we change the schema for some reason, the client codes of the 'getField'
--   function won't compile any more.
--    This approach is useful when we work with static schemas in the code and we want to
--   have guarantees that every change in the static schema will be propagated to the
--   client code.

namespace SimpleValue

  ||| Associates a simple Idris Type with the schema.
  |||
  ||| With this mapping, interfacing with other parts of the
  ||| code is easier as no need for explicit JSON processing.
  ||| The main motivation here is the SQLite Select processing.
  public export
  SimpleType : Schema -> Type
  SimpleType Null = ()
  SimpleType Boolean = Bool
  SimpleType Number = Double
  SimpleType Str = String
  SimpleType (Array xs) = All JSON xs
  SimpleType (Object xs) = All Field xs
  SimpleType (Either x y) = Either (SimpleType x) (SimpleType y)

  ||| Convert a schema indexed JSON to its correspondence SimpleType value.
  export
  getSimpleValue : JSON s -> SimpleType s
  getSimpleValue JNull = ()
  getSimpleValue (JBoolean x) = x
  getSimpleValue (JNumber x) = x
  getSimpleValue (JString x) = x
  getSimpleValue (JArray xs) = xs
  getSimpleValue (JObject x) = x
  getSimpleValue (JLeft x) = Left (getSimpleValue x)
  getSimpleValue (JRight x) = Right (getSimpleValue x)

namespace ObjectHasField

  ||| A witness for an Object has the field, which is required.
  |||
  ||| The witness points to the element of the field list, in the structure of Here, There linked
  ||| list like construction, which helps us to traverse the Object when looking up the value.
  |||
  ||| NOTE: These constructions should be optimized to a simple integer index by the Idris compiler.
  public export
  data HasRequiredField : (0 f : String) -> (0 s : Schema) -> Type where
    Here  : (z : Schema)                    -> HasRequiredField f  (Object ((f,Required,z) :: _ ))
    There : HasRequiredField f0 (Object fs) -> HasRequiredField f0 (Object ((f1,_,_)       :: fs))

  ||| Find the HasRequiredField, which is equivalent to the index of the element in the fields of Object.
  export
  hasRequiredField : (f : String) -> (s : Schema) -> Maybe (HasRequiredField f s)
  hasRequiredField f (Object ((x, Required, z) :: xs)) = case decEq f x of
    Yes f_is_x => Just (rewrite f_is_x in (Here z))
    No contra  => map There (hasRequiredField f (Object xs))
  hasRequiredField f _ = Nothing

  public export
  FieldType : HasRequiredField f s -> Type
  FieldType (Here z)  = SimpleType z
  FieldType (There x) = FieldType x

  ||| Traverse the field of object and retrieve the JSON value of the field, alongside its Schema.
  total
  -- This function is total, because the indexes in the HasRequiredField determines that this function
  -- only be called with Object JSON, and rest of constructors don't need to be inspected.
  getFieldSafe : (s : Schema) -> JSON s -> (f : String) -> (1 ok : HasRequiredField f s) -> FieldType ok
  getFieldSafe (Object ((_, (Required, y)) ::  _)) (JObject (RequiredField x :: _)) f (Here y)  = getSimpleValue x
  getFieldSafe (Object ((f1, (_, _))       :: fs)) (JObject (_      :: x))          f (There y) = getFieldSafe (Object fs) (JObject x) f y

  ||| Traverse the field of object and retrieve the JSON value of the field, alongside its Schema.  
  export
  -- Use implicit parameters where possible.
  getField : {s : Schema} -> JSON s -> (f : String) -> {auto 1 ok : HasRequiredField f s} -> FieldType ok
  getField {s} json f {ok} = getFieldSafe s json f ok

mutual

  ||| Forget about the schema index of the JSON and convert it to the non idexed JSON representation.
  export
  toNonIndexed : Indexed.JSON s -> Data.JSON
  toNonIndexed JNull        = JNull
  toNonIndexed (JBoolean x) = JBoolean x
  toNonIndexed (JNumber x)  = JNumber x
  toNonIndexed (JString x)  = JString x
  toNonIndexed (JArray xs)  = JArray (toNonIndexedArray xs)
  toNonIndexed (JObject xs) = JObject (toNonIndexedObjectFields xs)
  toNonIndexed (JLeft x)    = toNonIndexed x
  toNonIndexed (JRight x)   = toNonIndexed x

  toNonIndexedArray : {xs : List Schema} -> All Indexed.JSON xs -> List Data.JSON
  toNonIndexedArray []        = []
  toNonIndexedArray (x :: xs) = toNonIndexed x :: toNonIndexedArray xs

  toNonIndexedObjectFields : {xs : FieldList} -> All Field xs -> List (String, Data.JSON)
  toNonIndexedObjectFields [] = []
  toNonIndexedObjectFields ((RequiredField {f} x) :: xs)        = (f, toNonIndexed x) :: toNonIndexedObjectFields xs
  toNonIndexedObjectFields ((OptionalField {f} Nothing) :: xs)  =                        toNonIndexedObjectFields xs
  toNonIndexedObjectFields ((OptionalField {f} (Just x)) :: xs) = (f, toNonIndexed x) :: toNonIndexedObjectFields xs

mutual

  ||| Parse a non-indexed JSON with the given schema.
  |||
  ||| If the given non-indexed JSON fits the schema, we can create an indexed
  ||| version of it. As schemas can be this parsing backtracks on schema
  ||| Either constructions. During the creation of the indexed object, it is
  ||| not required from the fields to have the same order as in the schema,
  ||| leading to another search when the indexed object is assembled.
  export
  toIndexed : (s : Schema) -> Data.JSON -> Maybe (Indexed.JSON s)
  toIndexed Null          JNull        = Just JNull
  toIndexed Boolean       (JBoolean b) = Just (JBoolean b)
  toIndexed Number        (JNumber n)  = Just (JNumber n)
  toIndexed Str           (JString s)  = Just (JString s)
  toIndexed (Array xs)    (JArray ys)  = do
    elems <- toIndexedArray xs ys
    Just (JArray elems)
  toIndexed (Object xs)   (JObject ys) = do
    fields <- toIndexedObject xs ys
    Just (JObject fields)
  toIndexed (Either x y)  json = (map JLeft (toIndexed x json)) <|> (map JRight (toIndexed y json))
  toIndexed _             _    = Nothing

  toIndexedArray : (xs : List Schema) -> List JSON -> Maybe (All JSON xs)
  toIndexedArray [] [] = Just []
  toIndexedArray [] (x :: xs) = Nothing
  toIndexedArray (x :: xs) [] = Nothing
  toIndexedArray (x :: xs) (y :: ys) = do
    json <- toIndexed x y
    rest <- toIndexedArray xs ys
    Just (json :: rest)

  -- Looks up the field, if a required is missing it fails, otherwise succeeds, if
  -- there are more fields in the object, that is expected, the parsing still be
  -- successful.
  toIndexedObject : (xs : FieldList) -> List (String, JSON) -> Maybe (All Field xs)
  toIndexedObject [] []
    -- Base case, no field to lookup, in an empty list, that is successful conversion
    = Just []
  toIndexedObject [] ys@(_ :: _)
    -- No field to lookup, but there are some extra left, the JSON has more information
    -- than needed, but that is not a failure.
    = Just []
  toIndexedObject ((f, Optional, s) :: xs) []
    -- Optional field, if not present it can be ignored and OptionalField needs to be used
    = do rest <- toIndexedObject xs []
         Just (OptionalField Nothing :: rest)        
  toIndexedObject ((f, Required, s) :: xs) []
    -- Required field, if not present the parsing should fail, and we have no fields given.
    = Nothing
  toIndexedObject ((f, Optional, s) :: xs) ys@(_ :: _)
    -- Optional field, if not present it can be ignored and OptionalField needs to be used
    = case lookup f ys of
        Nothing => map (OptionalField Nothing ::) (toIndexedObject xs ys)
        Just jdata => do
          field <- toIndexed s jdata -- if the field is present, but it fails to parse,
                                     -- that is an error.
          rest  <- toIndexedObject xs ys
          Just (OptionalField (Just field) :: rest)
  toIndexedObject ((f, Required, s) :: xs) ys@(_ :: _)
    -- Required field, if not present the parsing should fail, and we have no fields given.
    = do jdata <- lookup f ys
         field <- toIndexed s jdata
         rest  <- toIndexedObject xs ys
         Just (RequiredField field :: rest)
```

## File: `src/Rango/BoundedContext/BoundedContext.idr`
```
module Rango.BoundedContext.BoundedContext

import public Rango.BoundedContext.Workflow

||| Summary of a Bounded Context
|||
||| A collection of descriptive types, and their connection via
||| simple functions. The Command determines its Workflow
||| and its result.
||| 
||| Later the values of Command, Workflow, and Event will
||| be used for determining the underlying implementational
||| 'Type's as we can use the power of dependent types
||| to calculate Type from values.
--
-- Bounded Context overview in general
--
--                     ┌───────────────┐
--                     │  CommandDTO   │
--                     └───────────────┘
--                       │
--                       │
--                       ▼
-- ┌−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−┐
-- ╎                    Bounded Context                    ╎
-- ╎                                                       ╎
-- ╎                   ┌───────────────┐                   ╎
-- ╎   ┌────────────── │    Command    │ ──────┐           ╎
-- ╎   │               └───────────────┘       │           ╎
-- ╎   │                 │                     │           ╎
-- ╎   │                 │                     │           ╎
-- ╎   ▼                 ▼                     ▼           ╎
-- ╎ ┌───────────┐     ┌───────────────┐     ┌───────────┐ ╎
-- ╎ │ Workflow1 │     │    Workflow2  │     │ WorkflowN │ ╎
-- ╎ └───────────┘     └───────────────┘     └───────────┘ ╎
-- ╎   │                 │                     │           ╎
-- ╎   │                 │                     │           ╎
-- ╎   │                 ▼                     │           ╎
-- ╎   │               ┌───────────────┐       │           ╎
-- ╎   └─────────────▶ │     Event     │ ◀─────┘           ╎
-- ╎                   └───────────────┘                   ╎
-- ╎                                                       ╎
-- └−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−┘
--                       │
--                       │
--                       ▼
--                     ┌───────────────┐
--                     │   EventDTO    │
--                     └───────────────┘
--
public export
record BoundedContext where
  constructor MkBoundedContext
  ||| Description of the Command in the Bounded Context
  Command     : Type
  ||| Description of the possible workflows in the Bounded Context
  Workflow    : Type
  ||| Descriptio of the possible events in the Bounded Context
  Event       : Type
  ||| Every Command means one Workflow
  workflowOf  : Command -> Workflow
  ||| Every Command means one Event
  eventOf     : Command -> Event

||| Environment of a Workflow.
|||
||| Existential type for the Workflow; all the
||| necessary information is available that is
||| required for the Workflow. This is a connection
||| between the Workflow abstraction and its use-cases.
public export
record WorkflowEnv where
  constructor MkWorkflowEnv
  state    : Type
  Command  : state -> state -> Type
  Branch   : state -> state -> state -> Type
  start    : state
  end      : state
  Workflow : Workflow Command Branch start end

||| Smart constructor for the Workflow.
|||
||| Capture all the parameters of a Workflow
||| in a Workflow environment.
public export
mkWorkflowEnv
  :  {st : Type}
  -> {cm : st -> st -> Type}
  -> {br : st -> st -> st -> Type}
  -> {s, e : st}
  -> (w : Workflow cm br s e) -> WorkflowEnv
mkWorkflowEnv {st, cm, br, s, e} w = MkWorkflowEnv st cm br s e w

||| Transform a WorkflowEnv with a Workflow morphism.
transformWorkflow
  :  Monad monad
  => (w : WorkflowEnv)
  -> (mr : Morphism monad w.state w.Command w.Branch)
  -> (mr.StateType w.start) -> monad (mr.StateType w.end)
transformWorkflow w mr x = morph mr w.Workflow x

||| Embedding of a workflow monad into the monad of bounded context implementation.
|||
||| The embedding encapsulates a function which transforms one monad to another one.
||| This is a helper abstraction for the Workflow embedding, where workflow monads,
||| needs to be understandable in the monad of the bounded context.
public export
data Embedding : (from : Type -> Type) -> (err : Type) -> (to : Type -> Type) -> Type where
  -- An extra 'a' type parameter is needed here to support the Rank polimorphism
  -- better. This type parameter will be injected with the 'runEmbedding' function.
  -- The 'Either err' is part of the return type signature to encode the fact, that
  -- some kind of error will be expected from the run of the workflow.
  MkEmbedding : ((a : Type) -> from a -> to (Either err a)) -> Embedding from err to

||| Unwraps the embedding
|||
||| unwrapEmbedding use the implicit 'a' type parameters from the context, which
||| is determined by the clients of the 'unwrapEmbedding'.
||| Its intended use is to create the 'f a -> t (Either e a)' function.
unwrapEmbedding : {a : Type} -> Embedding f e t -> (f a -> t (Either e a))
unwrapEmbedding (MkEmbedding f) y = f a y

||| Well-typed formulazation of a Bounded Context.
public export
record BoundedContextImplementation (monad : Type -> Type) where
  constructor MkBoundedContextImplementation

  ||| The high level description of the bounded context.
  context
    : BoundedContext

  ||| Associate workflows with the values of the Workflow description.
  Workflow
    : context.Workflow -> WorkflowEnv
  
  ||| Datatype which represents an incomming command of the Bounded Context
  ContextCommand
    : Type
  
  ||| Association between the different kind of commands and the information
  ||| needed by the Workflow.
  WorkflowEntry
    : context.Workflow -> Type
  
  ||| Datatype which represents an outgoing Event of the Bounded Context
  ||| It should somehow summarize the information from the events created
  ||| by different workflows
  ContextEvent
    : Type
  
  ||| The information needed to represent the Context Event in this
  ||| implementation. Usually a datatype per Event of the context.
  EventData
    : context.Event -> Type
  
  ||| Datatype which represents an outgoing errors of the Bounded Context
  ||| It should somehow summarize the information from the events created
  ||| by different workflows
  ContextError
    : Type

  ||| The information needed to represent the Context Error in this
  ||| implementation. Usually a datatype per error of the context.
  ErrorData
    : context.Workflow -> Type

  ||| For every workflow we can define its own monad, this helps us
  ||| separate of concerns a granulated way. For example
  ||| different workflows, needs to connect to different services
  ||| or different databases. It is enough if the workflow monad
  ||| just encapsulates its very own repsonsibility.
  WorkflowMonad
    : context.Workflow -> (Type -> Type)
  
  ||| Technicality, defining the Monad type for the workflow is not
  ||| enough, we should provide its Monad interface instance. This
  ||| is needed for the embedding part, when we select the Monad
  ||| for the workflow Idris must be aware of the Monad instance
  ||| in context. The easiest way to do this is the grab the instance
  ||| in the record too.
  WorkflowMonadInstance
    : (w : context.Workflow) -> Monad (WorkflowMonad w)
  
  ||| Every command of the bounded context determines its workflow, it is
  ||| enough to associate the workflow with its morphism that implements
  ||| the worklflow in its monad.
  workflowMorphism
    : (cmd : context.Command) ->
      let w = context.workflowOf cmd
          d = Workflow w
      in Morphism (WorkflowMonad w) (state d) (WorkflowEnv.Command d) (Branch d)
  
  ||| Create an embedding from the command. This could instanciate
  ||| new embedding for the workflow every time when a new command
  ||| arrives.
  createWorkflowEmbedding
    : (cmd : context.Command) ->
      let w = context.workflowOf cmd
      in monad (Embedding (WorkflowMonad w) (ErrorData w) monad)
  
  ||| Transforms the result of a workflow into the event of the workflow.
  ||| Computation may happen during the transformation.
  transformWorkflowResult
    : (cmd : context.Command) ->
      let morphism = workflowMorphism cmd
      in morphism.StateType (WorkflowEnv.end (Workflow (context.workflowOf cmd))) -> monad (EventData (context.eventOf cmd))
  
  ||| Transforms the event information that comes from the execution of the workflow
  ||| into the Event of the bounded context.
  ||| Computation may happen during the transformation.
  transformEvent
    : (cmd : context.Command) -> EventData (context.eventOf cmd) -> monad ContextEvent
  
  ||| Creates a command from the command information.
  |||
  ||| The entry point of a bounded context is a command. We get the command
  ||| from the external world, that is the public API of the bounded context,
  ||| but that command needs to parsed, understood in terms of the internal
  ||| commands, and information which is needed by the workflow.
  createCommand
    : ContextCommand -> monad (cmd : context.Command ** WorkflowEntry (context.workflowOf cmd))
  
  ||| Creates a start state of the workflow from command, which
  ||| was extracted from the command data of the bounded context.
  ||| Creation of the start state related information of the workflow
  ||| may happen as part a computation.
  createStartState
    : (cmd : context.Command) ->
      let m = workflowMorphism cmd
      in WorkflowEntry (context.workflowOf cmd) -> monad (m.StateType (WorkflowEnv.start (Workflow (context.workflowOf cmd))))
  
  ||| Transform the error information that comes from the execution of the workflow
  ||| into the Error of the boundedContext.
  ||| Computation may happend during the transformation of this information.
  transformError
    : (w : context.Workflow) -> (ErrorData w) -> monad ContextError

||| Execute a command with the given bounded context.
|||
||| Its responsibility is to select the workflow corresponding the given command,
||| and execute the selected workflow in its monad, which is embeddeable to the
||| main monad of the bounded context handler. The result will be a bounded context
||| error or a bounded context event.
-- 
--   ┌───────────────────────────────────────────────────────────────┐
--   │                                                               │
--   │                                    ┌───────────────────────┐  │
--   │                                    │         Start         │  │
--   │                                    └───────────────────────┘  │
--   │                                      │                        │
--   │ cmd                                  │ context command        │
--   ▼                                      ▼                        │
-- ┌──────────────────┐  workflow entry   ┌────────────────────────────────────────────────────────────────────┐  cmd               ┌─────────────────────────┐
-- │ createStartState │ ◀──────────────── │                                                                    │ ─────────────────▶ │ createWorkflowEmbedding │
-- └──────────────────┘                   │                                                                    │                    └─────────────────────────┘
--   │                                    │                                                                    │                      │
--   │                                    │                           createCommand                            │                      │
--   │                                    │                                                                    │                      │
--   │                                    │                                                                    │                      │
--   │                   ┌─────────────── │                                                                    │ ─┐                   │
--   │                   │                └────────────────────────────────────────────────────────────────────┘  │                   │
--   │                   │                  │                                          │                          │                   │
--   │                   │                  │ cmd                                      │ cmd                      │                   │
--   │                   │                  ▼                                          ▼                          │                   │
--   │                   │                ┌───────────────────────┐                  ┌─────────────────────────┐  │                   │
--   │                   │                │ bc.context.workflowOf │                  │   bc.workflowMorphism   │  │                   │
--   │                   │                └───────────────────────┘                  └─────────────────────────┘  │                   │
--   │ input             │                  │                                          │                          │                   │
--   │                   │                  │ workflow                                 │                          │                   │
--   │                   │                  ▼                                          │                          │                   │
--   │                   │                ┌───────────────────────┐  morphism          │                          │                   │
--   │                   │                │   transformWorkflow   │ ◀──────────────────┘                          │                   │
--   │                   │                └───────────────────────┘                                               │                   │
--   │                   │                  │                                                                     │                   │
--   │                   │                  │ embedded workflow                                                   └───────────────────┼──────────────────────────┐
--   │                   │                  ▼                                                                                         │                          │
--   │                   │                ┌────────────────────────────────────────────────────────────────────┐  workflow runner     │                          │
--   └───────────────────┼──────────────▶ │             unwrapEmbedding: Execute embedded workflow             │ ◀────────────────────┘                          │
--                       │                └────────────────────────────────────────────────────────────────────┘                                                 │
--                       │                  │                                          │                                                                         │
--                       │ cmd              │ error                                    │ event data                                                              │
--                       │                  ▼                                          ▼                                                                         │
--                       │                ┌───────────────────────┐                  ┌─────────────────────────┐  cmd                                            │
--                       └──────────────▶ │    transformError     │                  │ transformWorkflowResult │ ◀───────────────────────────────────────────────┘
--                                        └───────────────────────┘                  └─────────────────────────┘
--                                          │                                          │
--                                          │ context error                            │
--                                          ▼                                          │
--                                        ┌───────────────────────┐  context event     │
--                                        │     contextResult     │ ◀──────────────────┘
--                                        └───────────────────────┘
--                                          │
--                                          │
--                                          ▼
--                                        ┌───────────────────────┐
--                                        │          End          │
--                                        └───────────────────────┘
--
export
execute
  :  (Monad m)
  => (bc : BoundedContextImplementation m) -> bc.ContextCommand -> m (Either bc.ContextError bc.ContextEvent)
execute bc contextCommand = do
  (cmd ** workflowEntry) <- bc.createCommand contextCommand
  workflowRunner <- bc.createWorkflowEmbedding cmd
  let workflowMonadInstance = bc.WorkflowMonadInstance (bc.context.workflowOf cmd) -- For transformWorkflow
  input  <- bc.createStartState cmd workflowEntry
  let embeddedWorkflow = transformWorkflow (bc.Workflow (bc.context.workflowOf cmd)) (bc.workflowMorphism cmd)
  result <- unwrapEmbedding workflowRunner (embeddedWorkflow input)
  case result of
    Left err => map Left (bc.transformError (bc.context.workflowOf cmd) err)
    Right eventData => do
      workflowEvent <- bc.transformWorkflowResult cmd eventData
      map Right (bc.transformEvent cmd workflowEvent)

-- NOTE: Graph definition

{-
digraph {
	Start -> createCommand [ label = "context command" ];
    createCommand -> createWorkflowEmbedding [ label = "cmd" ];
    createCommand -> createStartState [ label = "cmd" ];
    createCommand -> createStartState [ label = "workflow entry" ];
    createCommand -> bc_context_workflowOf [ label = "cmd" ];
    createCommand -> bc_workflowMorphism [ label = "cmd" ];
    bc_context_workflowOf -> transformWorkflow [ label = "workflow" ];
    bc_workflowMorphism -> transformWorkflow [ label = "morphism" ];
    createWorkflowEmbedding -> unwrapEmbedding [ label = "workflow runner" ];
    transformWorkflow -> unwrapEmbedding [ label = "embedded workflow" ];
    createStartState -> unwrapEmbedding [ label = "input" ];
    createCommand   -> transformError [ label = "cmd" ];
    unwrapEmbedding -> transformError [ label = "error" ];
    createCommand   -> transformWorkflowResult [ label = "cmd" ];
    unwrapEmbedding -> transformWorkflowResult [ label = "event data" ];
    transformError -> contextResult [ label = "context error" ];
    transformWorkflowResult -> contextResult [ label = "context event" ];
    contextResult -> End;
    
    unwrapEmbedding [ label = "unwrapEmbedding: Execute embedded workflow" ];
    bc_context_workflowOf [ label = "bc.context.workflowOf" ];
    bc_workflowMorphism [ label = "bc.workflowMorphism" ];   
}
-}
```

## File: `src/Rango/BoundedContext/DynWorkflow.idr`
```
module Rango.BoundedContext.DynWorkflow

public export
data DynWorkflow
      :  (0 t : Type)
      -> (0 cmd : state -> state -> Type)
      -> (0 obs : state -> state -> Type -> Type)
      -> (0 chk : state -> state -> state -> Type)
      -> state
      -> (t -> state)
      -> Type
  where
    Pure
      :  (r : t) -> DynWorkflow t cmd obs chk (c r) c
    Do
      :  {0 cmd : state -> state -> Type}
      -> {1 pre, post : state}
      -> cmd pre post
      -> DynWorkflow () cmd obs chk pre (const post)
    Observe
      :  {0 obs : state -> state -> Type -> Type}
      -> {1 pre, post : state} -> {t : Type}
      -> obs pre post t
      -> DynWorkflow t cmd obs chk pre (const post)
    Branch
      :  {0 chk : state -> state -> state -> Type}
      -> {1 pre, branch1, branch2, post : state}
      -> chk pre branch1 branch2
      -> DynWorkflow () cmd obs chk branch1 (const post)
      -> DynWorkflow () cmd obs chk branch2 (const post)
      -> DynWorkflow () cmd obs chk pre (const post)
    (>>=)
      :  {0 a,b : Type} -> {0 pre : state}
      -> {1 postFn1 : a -> state} -> {0 postFn2 : b -> state}
      -> DynWorkflow a cmd obs chk pre postFn1
      -> ((r : a) -> (DynWorkflow b cmd obs chk (postFn1 r) postFn2))
      -> DynWorkflow b cmd obs chk pre postFn2

export
(>>) :  {0 b : Type} -> {0 pre : state} -> {0 postFn2 : b -> state} -> {1 postFn1 : () -> state}
     -> DynWorkflow () cmd obs chk pre postFn1
     -> DynWorkflow b  cmd obs chk (postFn1 ()) postFn2
     -> DynWorkflow b  cmd obs chk pre postFn2
(>>) m k = m >>= (\() => k)

public export
record Morphism
        (0 monad : Type -> Type)
        state
        (0 cmd : state -> state -> Type)
        (0 obs : state -> state -> Type -> Type)
        (0 chk : state -> state -> state -> Type)
  where
    constructor MkRunner
    StateType
      : state -> Type
    command
      : {0 s,e : state} -> cmd s e -> (StateType s) -> monad (StateType e)
    observe
      : {0 t : Type} -> {0 s,e : state} -> obs s e t -> (StateType s) -> monad (t, StateType e)
    check
      :  {0 s,b1,b2 : state}
      -> chk s b1 b2
      -> (StateType s) -> monad (Either (StateType b1) (StateType b2))

export
morph
  :  Functor monad => Applicative monad => Monad monad
  => (r : Morphism monad state cmd obs chk)
  -> DynWorkflow t cmd obs chk start end
  -> (StateType r start)
  -> monad (x : t ** StateType r (end x))
morph r (Pure x) i = pure (x ** i)
morph r (Do cmd) i = do
  o <- command r cmd i
  pure (() ** o)
morph r (Observe obs) i = do
  (x, o) <- observe r obs i
  pure (x ** o)
morph r (Branch h b1 b2) i = do
  x <- check r h i
  case x of
    Left y => morph r b1 y
    Right y => morph r b2 y
morph r (m >>= k) i = do
  (x ** md) <- morph r m i
  morph r (k x) md
```

## File: `src/Rango/BoundedContext/Workflow.idr`
```
module Rango.BoundedContext.Workflow

||| High level description of a Workflow of a bounded context.
|||
||| State transition system which describes the state transition
||| system of a workflow, similar as flowcharts

||| The workflow starts in a state, and ends in another one.
||| The workflow describes this state transition using the
||| 'cmd' to annotate a transition from one state to another,
||| 'chk' to annotate a branching condition.
public export
data Workflow
         -- cmd - Annotate transitions from one state to another
      :  (0 cmd : state -> state -> Type)
         -- chk - Annotate checks from one state to a valid and invalid state
      -> (0 chk : state -> state -> state -> Type)
         -- initial state
      -> state
         -- end state
      -> state
      -> Type
  where
    -- Wrap a step in a Do step
    Do
      :  {0 cmd : state -> state -> Type}
      -> cmd pre post
      -> Workflow cmd chk pre post
    -- Wrap a condition is a Branch step
    Branch
      :  {0 chk : state -> state -> state -> Type}
      -> {1 branch1, branch2 : state}
      -> chk pre branch1 branch2
      -> Workflow cmd chk branch1 post
      -> Workflow cmd chk branch2 post
      -> Workflow cmd chk pre post
    -- Use Idris' do notation to sequence steps
    (>>)
      :  {1 mid : state}
      -> Workflow cmd chk pre mid
      -> Workflow cmd chk mid post
      -> Workflow cmd chk pre post

||| How to turn the pieces in the Workflow description into a computation
||| related Idris Types. This helps us to connect the high level description
||| with the actual implementation.
public export
record Morphism
        (0 monad : Type -> Type)
        state
        (0 cmd : state -> state -> Type)
        (0 chk : state -> state -> state -> Type)
  where
    constructor MkMorphism
    -- How to represent information with the associated state.
    StateType
      : state -> Type
    -- How to represent the given step as a monadic state transition,
    -- in form of 'a -> m b'
    step
      : {0 s,e : state} -> cmd s e -> (StateType s) -> monad (StateType e)
    -- How to represent branching as a monadic state transition,
    -- in form of 'a -> m (Either b c)'
    check
      :  {0 s,b1,b2 : state}
      -> chk s b1 b2
      -> (StateType s) -> monad (Either (StateType b1) (StateType b2))

||| How to turn a Workflow description into a state transition system
||| which can is represented as a Kliesli arrow of a Monad; a -> m b
||| This helps us to connect the high level description
||| with the actual implementation.
export
morph
  :  Functor monad => Applicative monad => Monad monad
  => (r : Morphism monad state cmd chk)
  -> Workflow cmd chk start end
  -> (StateType r start) -> monad (StateType r end)
morph r (Do cmd) i = step r cmd i
morph r (m1 >> m2) i = do
  x <- morph r m1 i
  morph r m2 x
morph r (Branch h b1 b2) i = do
  x <- check r h i
  case x of
    Left y  => morph r b1 y
    Right y => morph r b2 y
```

## File: `src/Rango/DataTransfer/JSON/Derive.idr`
```
||| Automatic deriviation of JSON conversion interfaces.
||| Forked from Idris2-LSP
|||
||| (C) The Idris Community, 2021
module Rango.DataTransfer.JSON.Derive

-- https://github.com/idris-community/idris2-lsp/blob/main/src/Language/LSP/Message/Derive.idr

-- NOTE: Elaborator functions are evaluated as if they are defined inside the
-- call location module, thus imported functions used inside elaborator
-- functions should be exported publicly or explicitly imported at call
-- location.
import public Data.Maybe
import public Data.SortedMap
import public Rango.DataTransfer.JSON.Interfaces
import public Language.JSON
import public Language.Reflection
import Data.String

%language ElabReflection
%default total

||| Options for automatic derivation of `ToJSON`/`FromJSON` instances.
public export
record JSONDeriveOpts where
  constructor MkOpts
  ||| If tagged, values are converted to JSON object with one field where the
  ||| key is the name of the constructor and the value is the object obtained
  ||| from converting the arguments of the constructor.
  tagged : Bool
  ||| Renaming rules for arguments where the name of the argument does not
  ||| match the correspondent key in the translated JSON object.
  renames : List (String, String)
  ||| Fields that must be present in the JSON translation but have static
  ||| values.
  staticFields : List (String, JSON)

public export
defaultOpts : JSONDeriveOpts
defaultOpts = MkOpts False [] []

stripNs : Name -> Name
stripNs (NS _ x) = x
stripNs x = x

covering
genReadableSym : String -> Elab Name
genReadableSym hint = do
  MN v i <- genSym hint
    | _ => fail "cannot generate readable argument name"
  pure $ UN $ Basic (v ++ show i)

var : Name -> TTImp
var = IVar EmptyFC

bindvar : String -> TTImp
bindvar = IBindVar EmptyFC

primStr : String -> TTImp
primStr = IPrimVal EmptyFC . Str

patClause : TTImp -> TTImp -> Clause
patClause = PatClause EmptyFC

implicit' : TTImp
implicit' = Implicit EmptyFC True

-- TODO: add support for polymorphic types and maybe use another type for
-- optional fields in place of Maybe.
||| Automatic derivation of `ToJSON` instances.
||| NOTE: all the fields in each constructor MUST be named, record already
||| comply but types declared with data must have constructors declared like
||| this:
||| ```idris example
||| data Position : Type where
|||   MkPosition : (x : Integer) -> (y : Integer) -> Position
||| ```
||| If the tagging option is enabled, types with multiple constructors are
||| translated to a JSON object with a single key-value pair where the key is
||| constructor name (without the namespace) and the value is the JSON object
||| translated as if untagged.
||| Constructor arguments that are `Maybe` instances are omitted if `Nothing`
||| and converted without the constructor if `Just`. If you need to translate a
||| mandatory field that can be nullable use the `Null` type.
|||
||| @ opts The automatic derivation options.
||| @ name The name of the type to derive for. Can be without namespace if unambigous.
public export covering
deriveToJSON : (opts : JSONDeriveOpts) -> (name : Name) -> Elab ()
deriveToJSON opts n = do
    [(name, imp)] <- getType n
      | xs => fail $ show n ++ " must be in scope and unique. Possible referred types are: " ++ show (fst <$> xs)
    -- FIXME: temporary name for debugging, should be converted to a name impossible to define from users
    -- and should not be exported, unless a specific option is enabled.
    let funName = UN $ Basic ("toJSON" ++ show (stripNs n))
    let objName = UN $ Basic ("__impl_toJSON" ++ show (stripNs n))
    conNames <- getCons name
    cons <- for conNames $ \n => do
      [(conName, conImpl)] <- getType n
        | _ => fail $ show n ++ " constructor must be in scope and unique"
      (bindNames, rhs) <- genRHS conImpl
      let rhs = if opts.tagged
                   then `(JObject $ [MkPair ~(primStr $ show $ stripNs n) (JObject $ catMaybes ~rhs)])
                   else `(JObject $ catMaybes ~rhs)
      let lhs = `(~(var funName) ~(applyBinds (var conName) (reverse bindNames)))
      pure $ patClause lhs rhs
    let funclaim = IClaim EmptyFC MW Export [Inline] (MkTy EmptyFC EmptyFC funName `(~(var name) -> JSON))
    let fundecl = IDef EmptyFC funName cons
    declare [funclaim, fundecl]
    [(ifName, _)] <- getType `{ToJSON}
      | _ => fail "ToJSON interface must be in scope and unique"
    [NS _ (DN _ ifCon)] <- getCons ifName
      | _ => fail "Interface constructor error"
    let retty = `(ToJSON ~(var name))
    let objclaim = IClaim EmptyFC MW Export [Hint True, Inline] (MkTy EmptyFC EmptyFC objName retty)
    let objrhs = `(~(var ifCon) ~(var funName))
    let objdecl = IDef EmptyFC objName [(PatClause EmptyFC (var objName) objrhs)]
    declare [objclaim, objdecl]
  where
    genRHS : TTImp -> Elab (List Name, TTImp)
    genRHS (IPi _ _ _ (Just n) `(Prelude.Types.Maybe ~argTy) retTy) = do
      (ns, rest) <- genRHS retTy
      let name = primStr $ fromMaybe (show n) $ lookup (show n) opts.renames
      pure (n :: ns, `(((MkPair ~name . toJSON) <$> ~(var n)) :: ~rest))
    genRHS (IPi _ _ _ (Just n) argTy retTy) = do
      (ns, rest) <- genRHS retTy
      let name = primStr $ fromMaybe (show n) $ lookup (show n) opts.renames
      pure (n :: ns, `(Just (MkPair ~name (toJSON ~(var n))) :: ~rest))
    genRHS (IPi _ _ _ Nothing _ _) = fail $ "All arguments must be explicitly named"
    genRHS _ = do
      -- Hack required, because if you quote directly opts.staticFields the elaborator introduces unsolved holes
      r <- traverse (\(k, v) => (k,) <$> quote v) opts.staticFields
      pure ([], foldr (\(k, v), acc => `(Just (MkPair ~(primStr k) ~v) :: ~acc)) `([]) r)

    applyBinds : TTImp -> List Name -> TTImp
    applyBinds = foldr (\n, acc => `(~acc ~(bindvar $ show n)))

||| Automatic derivation of `FromJSON` instances.
||| NOTE: all the fields in each constructor MUST be named, record already
||| comply but types declared with data must have constructors declared like
||| this:
||| ```idris example
||| data Position : Type where
|||   MkPosition : (x : Integer) -> (y : Integer) -> Position
||| ```
||| If the tagging option is enabled, types with multiple constructors are
||| translated to a JSON object with a single key-value pair where the key is
||| constructor name (without the namespace) and the value is the JSON object
||| translated as if untagged.
||| Constructor arguments that are `Maybe` instances are omitted if `Nothing`
||| and converted without the constructor if `Just`. If you need to translate a
||| mandatory field that can be nullable use the `Null` type.
|||
||| @ opts The automatic derivation options.
||| @ name The name of the type to derive for. Can be without namespace if unambigous.
public export covering
deriveFromJSON : (opts : JSONDeriveOpts) -> (name : Name) -> Elab ()
deriveFromJSON opts n = do
    [(name, imp)] <- getType n
      | xs => fail $ show n ++ " must be in scope and unique. Possible referred types are: " ++ show (fst <$> xs)
    -- FIXME: temporary name for debugging, should be converted to a name impossible to define from users
    -- and should not be exported, unless a specific option is enabled.
    let funName = UN $ Basic ("fromJSON" ++ show (stripNs n))
    let objName = UN $ Basic ("__impl_fromJSON" ++ show (stripNs n))
    conNames <- getCons name
    argName <- genReadableSym "arg"
    cons <- for conNames $ \n => do
      [(conName, conImpl)] <- getType n
        | _ => fail $ show n ++ "constructor must be in scope and unique"
      args <- getArgs conImpl
      pure (conName, args)
    clauses <- traverse (\(cn, as) => genClause funName cn argName (reverse as)) cons
    let clauses = if opts.tagged
                     then (uncurry patClause <$> clauses)
                     else [patClause `(~(var funName) (JObject ~(bindvar $ show argName)))
                                     (foldl (\acc, x => `(~x <|> ~acc)) `(Nothing) (snd <$> clauses))]
    let funClaim = IClaim EmptyFC MW Export [Inline] (MkTy EmptyFC EmptyFC funName `(JSON -> Maybe ~(var name)))
    let funDecl = IDef EmptyFC funName (clauses ++ [patClause `(~(var funName) ~implicit') `(Nothing)])
    declare [funClaim, funDecl]
    [(ifName, _)] <- getType `{FromJSON}
      | _ => fail "FromJSON interface must be in scope and unique"
    [NS _ (DN _ ifCon)] <- getCons ifName
      | _ => fail "Interface constructor error"
    let retty = `(FromJSON ~(var name))
    let objClaim = IClaim EmptyFC MW Export [Hint True, Inline] (MkTy EmptyFC EmptyFC objName retty)
    let objrhs = `(~(var ifCon) ~(var funName))
    let objDecl = IDef EmptyFC objName [(PatClause EmptyFC (var objName) objrhs)]
    declare [objClaim, objDecl]
  where
    getArgs : TTImp -> Elab (List (Name, TTImp))
    getArgs (IPi _ _ _ (Just n) argTy retTy) = ((n, argTy) ::) <$> getArgs retTy
    getArgs (IPi _ _ _ Nothing _ _) = fail $ "All arguments must be explicitly named"
    getArgs _ = pure []

    genClause : Name -> Name -> Name -> List (Name, TTImp) -> Elab (TTImp, TTImp)
    genClause funName t m xs = do
      let lhs = `(~(var funName) (JObject [MkPair ~(primStr $ show $ stripNs t) (JObject ~(bindvar $ show m))]))
      let rhs = foldr (\(n, type), acc => let name = primStr $ fromMaybe (show n) $ lookup (show n) opts.renames in
                                              case type of
                                                   `(Prelude.Types.Maybe _) => `(~acc <*> (pure $ lookup ~name ~(var m) >>= fromJSON))
                                                   _ => `(~acc <*> (lookup ~name ~(var m) >>= fromJSON)))
                      `(pure ~(var t)) xs
      r <- traverse (\(k, v) => (k,) <$> quote v) opts.staticFields
      let rhs = foldr (\(k, v), acc => `((lookup ~(primStr k) ~(var m) >>= (guard . (== ~v))) *> ~acc)) rhs r
      pure (lhs, rhs)

||| Automatic derivation of `ToJSON` and `FromJSON` instances.
||| See `deriveToJSON` and `deriveFromJSON`.
|||
||| @ opts The automatic derivation options.
||| @ name The name of the type to derive for. Can be without namespace if unambigous.
public export covering
deriveJSON : (opts : JSONDeriveOpts) -> (name : Name) -> Elab ()
deriveJSON opts name = deriveToJSON opts name *> deriveFromJSON opts name
```

## File: `src/Rango/DataTransfer/JSON/Interfaces.idr`
```
module Rango.DataTransfer.JSON.Interfaces

import Data.SortedMap
import Data.String
import Language.JSON
import Language.JSON.Lexer
import Language.JSON.Parser

%default total

-- TODO: Maybe we should be using a more expressive type than Maybe.
||| A type that can be converted to JSON.
||| An example type and implementation is:
||| ```idris example
||| record Position where
|||   constructor MkPosition
|||   x : Integer
|||   y : Integer
|||
||| ToJSON Position where
|||   toJSON pos = JObject [("x", toJSON pos.x), ("y", toJSON pos.y)]
||| ```
public export
interface ToJSON a where
  toJSON : a -> JSON

||| A type that can be possibly converted from JSON.
||| An example type and implementation is:
||| ```idris example
||| record Position where
|||   constructor MkPosition
|||   x : Integer
|||   y : Integer
|||
||| FromJSON Position where
|||   fromJSON (JObject arg) = do
|||     x <- lookup "x" arg >>= fromJSON
|||     y <- lookup "y" arg >>= fromJSON
|||     pure $ MkPosition x y
|||   fromJSON _ = neutral
||| ```
public export
interface FromJSON a where
  fromJSON : JSON -> Maybe a

export
ToJSON JSON where
  toJSON = id

export
FromJSON JSON where
  fromJSON = pure

export
ToJSON Integer where
  toJSON = JNumber . cast

-- NOTE: In JSON all numbers are `Double`, for integers we should cast or fail
-- for invalid values?
export
FromJSON Integer where
  fromJSON (JNumber x) = pure (cast x)
  fromJSON _ = neutral

export
ToJSON Int where
  toJSON = JNumber . cast

export
FromJSON Int where
  fromJSON (JNumber x) = pure (cast x)
  fromJSON _ = neutral

export
ToJSON Bits8 where
  toJSON = JNumber . cast . cast {to = Int}

export
FromJSON Bits8 where
  fromJSON (JNumber x) = pure (fromInteger $ cast x)
  fromJSON _ = neutral

export
ToJSON Bits16 where
  toJSON = JNumber . cast . cast {to = Int}

export
FromJSON Bits16 where
  fromJSON (JNumber x) = pure (fromInteger $ cast x)
  fromJSON _ = neutral

export
ToJSON Bits32 where
  toJSON = JNumber . cast . cast {to = Int}

export
FromJSON Bits32 where
  fromJSON (JNumber x) = pure (fromInteger $ cast x)
  fromJSON _ = neutral

export
ToJSON Bits64 where
  toJSON = JNumber . cast . cast {to = Int}

export
FromJSON Bits64 where
  fromJSON (JNumber x) = pure (fromInteger $ cast x)
  fromJSON _ = neutral

export
ToJSON Double where
  toJSON = JNumber

export
FromJSON Double where
  fromJSON (JNumber x) = pure x
  fromJSON _ = neutral

export
ToJSON Nat where
  toJSON = JNumber . cast

export
FromJSON Nat where
  fromJSON (JNumber x) = pure (fromInteger $ cast x)
  fromJSON _ = neutral

export
ToJSON String where
  toJSON = JString

export
FromJSON String where
  fromJSON (JString s) = pure s
  fromJSON _ = neutral

export
ToJSON Char where
  toJSON = toJSON . String.singleton

export
FromJSON Char where
  fromJSON (JString s) = case strM s of
                              StrCons c "" => pure c
                              _ => neutral
  fromJSON _ = neutral

export
ToJSON Bool where
  toJSON = JBoolean

export
FromJSON Bool where
  fromJSON (JBoolean b) = pure b
  fromJSON _ = neutral

export
ToJSON a => ToJSON (Maybe a) where
  toJSON Nothing = JNull
  toJSON (Just x) = toJSON x

export
FromJSON a => FromJSON (Maybe a) where
  fromJSON JNull = pure Nothing
  fromJSON json @{impl} = pure <$> fromJSON @{impl} json

export
ToJSON a => ToJSON (List a) where
  toJSON = JArray . map toJSON

export
FromJSON a => FromJSON (List a) where
  fromJSON (JArray xs) = traverse fromJSON xs
  fromJSON _ = neutral

export
ToJSON () where
  toJSON () = JObject empty

export
FromJSON () where
  fromJSON (JObject xs) = guard $ null xs
  fromJSON _ = neutral

export
(ToJSON a, ToJSON b) => ToJSON (a, b) where
  toJSON (x, y) = JArray [toJSON x, toJSON y]

export
(FromJSON a, FromJSON b) => FromJSON (a, b) where
  fromJSON (JArray [x, y]) = (,) <$> fromJSON x <*> fromJSON y
  fromJSON _ = neutral

export
ToJSON v => ToJSON (SortedMap String v) where
  toJSON m = JObject (toList $ toJSON <$> m)

export
FromJSON v => FromJSON (SortedMap String v) where
  fromJSON (JObject xs) = fromList <$> traverse (\(k, v) => (k,) <$> fromJSON v) xs
  fromJSON _ = neutral

export
ToJSON a => ToJSON (Inf a) where
  toJSON x = toJSON x

export
FromJSON a => FromJSON (Inf a) where
  fromJSON @{impl} x = map (\x => Delay x) (fromJSON @{impl} x)

```

## File: `src/Rango/DataTransfer/SQL/Syntax.idr`
```
module Rango.DataTransfer.SQL.Syntax

import public Data.List.Quantifiers -- for HList

import Data.String
import Data.List
import Data.Vect

public export
TableName : Type
TableName = String

public export
FieldName : Type
FieldName = String

public export
data SQLType
  = SQL_Integer
  | SQL_Text
  | SQL_Double

public export
data SQLValue : SQLType -> Type where
  SQLInteger : Int    -> SQLValue SQL_Integer
  SQLText    : String -> SQLValue SQL_Text
  SQLDouble  : Double -> SQLValue SQL_Double

public export
record Field where
  constructor MkField
  name          : FieldName
  sqlType       : SQLType
  primaryKey    : Bool
  autoIncrement : Bool
  notNull       : Bool

public export
data Modifier 
  = PrimaryKey
  | AutoIncrement
  | NotNull

fieldModifiers : Field -> List Modifier
fieldModifiers (MkField name sqlType primaryKey autoIncrement notNull) =
  if primaryKey     then [PrimaryKey]    else [] ++
  if autoIncrement  then [AutoIncrement] else [] ++
  if notNull        then [NotNull]       else []

public export
field : FieldName -> SQLType -> List Modifier -> Field
field f t ms = setModifiers ms $ MkField f t False False False
  where
    setModifiers : List Modifier -> Field -> Field
    setModifiers []                    f = f
    setModifiers (PrimaryKey    :: xs) f = setModifiers xs (record { primaryKey    = True } f)
    setModifiers (AutoIncrement :: xs) f = setModifiers xs (record { autoIncrement = True } f)
    setModifiers (NotNull       :: xs) f = setModifiers xs (record { notNull       = True } f)

public export
FieldType : Field -> Type
FieldType (MkField name sqlType False      autoIncrement False)   = Maybe (SQLValue sqlType)
FieldType (MkField name sqlType primaryKey autoIncrement notNull) = SQLValue sqlType

public export
data Constraint : Type where
  Unique
    :  (name : String)
    -> (fields : List FieldName)
    -> Constraint
  ForeignKey
    :  (field : FieldName)
    -> (foreignTable : TableName)
    -> (foreignField : FieldName)
    -> Constraint

public export
data Filter : Type

public export
data ValidTable : List Field -> List Constraint -> Type where
  YesOfCourseValid : ValidTable fields constraints
  -- TODO: Implement this check

public export
record Table where
  constructor MkTable
  name         : TableName
  fields       : List Field
  constraints  : List Constraint
  0 validTable : ValidTable fields constraints

public export
data FieldOfTy : String -> Type -> Type where
  FieldOf : (n : String) -> t -> FieldOfTy n t

||| Calculate the list of types which is required for the insert command, skipping the
||| auto incremental fields.
public export
InsertValues : List Field -> List Type
InsertValues []        = []
InsertValues (f@(MkField name sqlType primaryKey False notNull) :: fs) = FieldOfTy name (FieldType f) :: InsertValues fs
InsertValues (f@(MkField name sqlType primaryKey True  notNull) :: fs) = InsertValues fs -- Do not ask for auto fields

public export
data FieldDefinedInTable : (field : FieldName) -> (fields : List Field) -> Type where
  Here  : FieldDefinedInTable f (MkField f _ _ _ _ :: fs)
  There : FieldDefinedInTable f fs -> FieldDefinedInTable f (g :: fs)

namespace FieldsExsistenceCheck
  public export
  data SelectedFieldsDefinedInTable : (names : List FieldName) -> (fields : List Field) -> Type where
    Nil  : SelectedFieldsDefinedInTable [] fields
    (::) : FieldDefinedInTable f fields -> SelectedFieldsDefinedInTable fs fields -> SelectedFieldsDefinedInTable (f :: fs) fields

namespace FilterExsistenceCheck
  public export
  data FilteredFieldsDefinedInTable : (filters : List (FieldName, String, String)) -> (fields : List Field) -> Type where
    Nil  : FilteredFieldsDefinedInTable [] fields
    (::) : FieldDefinedInTable f fields -> FilteredFieldsDefinedInTable fs fields -> FilteredFieldsDefinedInTable ((f, _, _) :: fs) fields

public export
data Command : Type where
  CreateTable
    :  (table : Table)
    -> Command
  Insert
    :  (table : Table)
    -> (values : HList (InsertValues table.fields))
    -> Command

%name Command cmd

public export
data Query : Type where
  Select
    :  (  fields    : List FieldName)
    -> (  table     : Table)
    -> (1 okFields  : SelectedFieldsDefinedInTable fields table.fields)
    => (  filters   : List (FieldName, String, String))
    -> (0 okFilters : FilteredFieldsDefinedInTable filters table.fields)
    => Query

%name Query qry

withCommas : List String -> String
withCommas xs = concat (intersperse ", " xs)

renderSQLType : SQLType -> String
renderSQLType SQL_Integer   = "INTEGER"
renderSQLType SQL_Double    = "DOUBLE PRECISION"
renderSQLType SQL_Text      = "TEXT"

renderModifier : Modifier -> String
renderModifier PrimaryKey    = "PRIMARY KEY"
renderModifier AutoIncrement = "AUTOINCREMENT"
renderModifier NotNull       = "NOT NULL"

renderConstraint : Constraint -> String
renderConstraint (Unique name fields) =
  "CONSTRAINT \{name} UNIQUE(\{withCommas fields})"
renderConstraint (ForeignKey field foreignTable foreignField) =
  "FOREIGN KEY(\{field}) REFERENCES \{foreignTable}(\{foreignField})"

renderCreateField : Field -> String
renderCreateField f =
  show f.name ++ " " ++ renderSQLType f.sqlType ++ " " ++ unwords (map renderModifier (fieldModifiers f))

renderSQLValue : SQLValue s -> String
renderSQLValue (SQLInteger x) = show x
renderSQLValue (SQLText x)    = show x
renderSQLValue (SQLDouble x)  = show x

-- Instead of doing a lot of proof around the type safety of this construction, we use
-- type level programming in a local hack and we dispatch on the type that we expect to
-- see in these cases. Use this function with care.
renderFieldValue : {t : Type} -> t -> String
renderFieldValue {t=FieldOfTy n s} (FieldOf _ x) = renderFieldValue x
renderFieldValue {t=Maybe (SQLValue s)} (Just x) = renderFieldValue x
renderFieldValue {t=Maybe (SQLValue s)} Nothing  = "NULL"
renderFieldValue {t=SQLValue s} x = renderSQLValue x
renderFieldValue _ = "(╯°□°)╯︵ ┻━┻" -- This shouldn't happen

-- This HList should contain a list of FieldOfTy entries, but we don't
-- check type-safety here, instead we just dynamically dispatch on the
-- actual type case and render the field, or render gibberish if we got the
-- types wrong. Use this function with care.
renderInsertValues : {ts : List Type} -> HList ts -> List String
renderInsertValues []        = []
renderInsertValues (a :: as) = renderFieldValue a :: renderInsertValues as

renderInsertNames : List Field -> List String
renderInsertNames [] = []
renderInsertNames ((MkField name sqlType primaryKey False notNull) :: xs) = name :: renderInsertNames xs
renderInsertNames ((MkField name sqlType primaryKey True  notNull) :: xs) = renderInsertNames xs

export
renderCommand : Command -> String
renderCommand (CreateTable table)
  = "CREATE TABLE \{table.name} (\{withCommas (map renderCreateField table.fields ++ map renderConstraint table.constraints)})"
renderCommand (Insert table values)
  = "INSERT INTO \{table.name} (\{withCommas (renderInsertNames table.fields)}) VALUES (\{withCommas (renderInsertValues values)})"

export
renderQuery : Query -> String
renderQuery (Select fields table filters)
  = "SELECT \{withCommas fields} FROM \{table.name}" ++
    (case filters of
      [] => ""
      fs => " WHERE " ++ (withCommas $ map (\(field, op, cond) => "(\{field} \{op} \{cond})") fs)) ++
    ";"
```

## File: `src/Rango/Database/SQLite.idr`
```
module Rango.Database.SQLite

import Language.JSON.Schema
import Rango.DataTransfer.SQL.Syntax
import Service.NodeJS.SQLite
import Service.NodeJS.Promise

public export
resultSchema : Query -> Schema
resultSchema (Select fields table {okFields} filters) = Object (fieldList okFields)
  where
    jsonType : SQLType -> Schema
    jsonType SQL_Integer  = Number
    jsonType SQL_Text     = Str
    jsonType SQL_Double   = Number

    fieldInfo : SQL.Syntax.Field -> Schema.Field
    fieldInfo (MkField name sqlType primaryKey autoIncrement False) = (name, Optional, jsonType sqlType)
    fieldInfo (MkField name sqlType primaryKey autoIncrement True)  = (name, Required, jsonType sqlType)

    fieldInTable : {n : FieldName} -> {fields : List SQL.Syntax.Field} -> FieldDefinedInTable n fields -> SQL.Syntax.Field
    fieldInTable {n = n} {fields = (f@(MkField n _ _ _ _) :: fs)} Here      = f
    fieldInTable {n = n} {fields = (g :: fs)}                     (There t) = fieldInTable t

    fieldList : {ns : List FieldName} -> {fs : List SQL.Syntax.Field} -> SelectedFieldsDefinedInTable ns fs -> FieldList
    fieldList [] = []
    fieldList (x :: xs) = (fieldInfo (fieldInTable x)) :: fieldList xs

||| Execute command
export
command : Database -> Command -> Promise SomeError
command db cmd = Database.run db $ renderCommand cmd

||| Execute query
export
query : Database -> (qry : Query) -> Promise (Safe.Result (resultSchema qry))
query db qry = Database.Safe.get db (resultSchema qry) $ renderQuery qry
```

## File: `src/Rango/Example/Workflow.idr`
```
module Rango.Example.Workflow

import Rango.BoundedContext.Workflow
import System.Random

-- State is the knowledge we know about the health of the lamp, which
-- is going to be refined in every step.
public export
data State
  = DoesntWork
  | NotPluggedIn
  | PluggedIn
  | BulbBurntOut
  | BulbIsOk
  | Works

public export
data Action : State -> State -> Type where
  PlugInLamp  : Action NotPluggedIn Works
  ReplaceBulb : Action BulbBurntOut Works
  RepairLamp  : Action BulbIsOk     Works

public export
data Check : State -> State -> State -> Type where
  IsPluggedIn : Check DoesntWork PluggedIn NotPluggedIn
  IsBulbOut   : Check PluggedIn  BulbIsOk  BulbBurntOut

public export
fixLamp : Workflow Action Check DoesntWork Works
fixLamp
  = Branch IsPluggedIn
      (Branch IsBulbOut
        (Do RepairLamp)
        (Do ReplaceBulb))
      (Do PlugInLamp)

public export data LightsOff  = MkLightsOff
public export data LigthsOn   = MkLightsOn
public export data BrokenLamp = MkBrokenLamp

public export
lampStateRep : State -> Type
lampStateRep DoesntWork   = LightsOff
lampStateRep NotPluggedIn = LightsOff
lampStateRep PluggedIn    = LigthsOn
lampStateRep BulbBurntOut = LightsOff
lampStateRep BulbIsOk     = BrokenLamp
lampStateRep Works        = LigthsOn

lampAction : Action s e -> (lampStateRep s) -> IO (lampStateRep e)
lampAction PlugInLamp  MkLightsOff  = do { putStrLn "Plug in lamp"; pure MkLightsOn }
lampAction ReplaceBulb MkLightsOff  = do { putStrLn "Replace bulb and turn it on"; pure MkLightsOn }
lampAction RepairLamp  MkBrokenLamp = do { putStrLn "Fix the lamp and turn it on"; pure MkLightsOn }

yesNo : IO Bool
yesNo = map (>0.5) randomIO

lampCheck : Check p t e -> (lampStateRep p) -> IO (Either (lampStateRep t) (lampStateRep e))
lampCheck IsPluggedIn MkLightsOff = do
  putStrLn "Is it plugged in?"
  res <- yesNo
  if res
    then do
      putStrLn "Yes."
      pure (Left MkLightsOn)
    else do
      putStrLn "No."
      pure (Right MkLightsOff)
lampCheck IsBulbOut MkLightsOn = do
  putStrLn "Is the bulb out?"
  res <- yesNo
  if res
    then do
      putStrLn "Yes."
      pure (Right MkLightsOff)
    else do
      putStrLn "No."
      pure (Left MkBrokenLamp)

morphism : Morphism IO State Action Check
morphism = MkMorphism
  { StateType = lampStateRep
  , step      = lampAction
  , check     = lampCheck
  }

lampProgram : LightsOff -> IO LigthsOn
lampProgram = morph morphism fixLamp

export
testLamp : IO ()
testLamp = do { MkLightsOn <- lampProgram MkLightsOff; pure () }
```

## File: `src/Service/NodeJS/Date.idr`
```
module Service.NodeJS.Date

-- Foreign function interface for NodeJS backend.
-- After 'node:lambda:' there should be a JavaScript snippet,
-- which will be injected into the generated JavaScript.
%foreign "node:lambda: u => Number(new Date().getTime())"
ffi_now : () -> PrimIO Int

-- With HasIO interface any IO can be lifted to the Monad
-- which implements this interface.
--
-- primIO creates an IO action from PrimIO. Only PrimIO
-- can be used in foreign interface if IO like computation
-- is represented by the foreign function.
export
now : HasIO io => io Int
now = primIO (ffi_now ())
```

## File: `src/Service/NodeJS/HTTP.idr`
```
module Service.NodeJS.HTTP

import Data.String
import Service.NodeJS.Promise

namespace Request

  export
  data Request : Type where [external]

  %foreign "node:lambda: (req, f) => {let data = '';req.on('data',chunk=>{data+=chunk;});req.on('end',()=> f(data)());}"
  ffi_body : Request -> (String -> PrimIO ()) -> PrimIO ()

  export
  %foreign "node:lambda: req => req.url"
  url : Request -> String

  export
  (.body) : Request -> Promise String
  (.body) req = promisify $ \ok, err => ffi_body req $ \content => toPrim $ ok content

namespace Response

  export
  data Response : Type where [external]

  %foreign "node:lambda: (r,c) => (r.statusCode = Number(c))"
  ffi_setStatusCode : Response -> Int -> PrimIO ()

  export
  (.setStatusCode) : HasIO io => Response -> Int -> io ()
  (.setStatusCode) r c = primIO (ffi_setStatusCode r c)

  %foreign "node:lambda: (r,h,v) => {r.setHeader(h, v)}"
  ffi_setHeader : Response -> String -> String -> PrimIO ()

  export
  (.setHeader) : HasIO io => Response -> String -> String -> io ()
  (.setHeader) r h v = primIO (ffi_setHeader r h v)

  %foreign "node:lambda: (r,e) => (r.end(e))"
  ffi_end : Response -> String -> PrimIO ()

  export
  (.end) : HasIO io => Response -> String -> io ()
  (.end) r e = primIO (ffi_end r e)

namespace Server

  export
  data Server : Type where [external]

  %foreign "node:lambda: (s,p,h) => (s.listen(Number(p),h,() => {}))"
  ffi_listen : Server -> Int -> String -> PrimIO ()

  export
  (.listen) : Server -> Int -> String -> IO ()
  (.listen) server port hostname = primIO (ffi_listen server port hostname)

namespace HTTP

  export
  data HTTP : Type where [external]

  %foreign "node:lambda: u => require('http')"
  ffi_require : () -> PrimIO HTTP

  export
  require : IO HTTP
  require = primIO (ffi_require ())

  %foreign "node:lambda: (http, result) => http.createServer((req,rsp) => {return result(req)(rsp)();})"
  ffi_createServer : HTTP -> (Request -> Response -> PrimIO ()) -> PrimIO Server

  export
  (.createServer) : HTTP -> (Request -> Response -> IO ()) -> IO Server
  (.createServer) http mkResult
      = primIO (ffi_createServer http (\req , rsp => toPrim $ mkResult req rsp))
```

## File: `src/Service/NodeJS/JSON.idr`
```
module Service.NodeJS.JSON

import public Language.JSON
import Data.List


public export
data JSON : Type where [external]

%foreign "node:lambda: r => {return JSON.stringify(r);}"
ffi_stringify : NodeJS.JSON.JSON -> PrimIO String

export
stringify : HasIO io => NodeJS.JSON.JSON -> io String
stringify r = primIO (ffi_stringify r)

export
convert : HasIO io => NodeJS.JSON.JSON -> io (Maybe Data.JSON)
convert o = do
  jsonStr <- stringify o
  -- This is slow, we need a better JSON API
  pure $ JSON.parse jsonStr

infixl 9 .:

export
(.:) : Data.JSON -> Lazy String -> Maybe Data.JSON
(JObject xs) .: field = lookup field xs
o            .: _     = Nothing
```

## File: `src/Service/NodeJS/MD5.idr`
```
module Service.NodeJS.MD5

-- See: https://www.npmjs.com/package/md5

||| JavaScript MD5 object reference.
|||
||| After MD5 is created it can generate MD5 String values
||| encoding strings.
export
data MD5 : Type where [external]

||| FFI require operation for requesting an MD5 JavaScript object.
%foreign "node:lambda: u => require('md5')"
ffi_require : () -> PrimIO MD5

||| Accessing an MD5 object.
export
require : HasIO io => io MD5
require = primIO (ffi_require ())

||| FFI call to generate MD5 string from a normal string value.
%foreign "node:lambda: (m,s) => m(s)"
ffi_generate : MD5 -> String -> PrimIO String

||| Generate an MD5 string from a normal string value.
export
(.generate) : HasIO io => MD5 -> String -> io String
(.generate) m s = primIO (ffi_generate m s)
```

## File: `src/Service/NodeJS/Promise.idr`
```
module Service.NodeJS.Promise

-- Promise abstraction from NodeJS

-- NodeJS using an event driven approach to represent computations. This approach can
-- be formalized/approximated with a Monad abstraction.

-- See: https://developer.mozilla.org/en-US/brain/knowledge/docs_legacy/Web/JavaScript/Reference/Global_Objects/Promise
-- Adapted from https://raw.githubusercontent.com/idris-community/inigo/master/Inigo/Async/Promise.idr

||| Promise monad
|||
||| Encapsulates the JavaScript abstraction of promise, which consists of a continuation
||| for successful computation and a continuation for errorneous computation. The promise
||| abstraction bounds these two continuations.
export
data Promise : Type -> Type where
  MkPromise : ((a -> IO ()) -> (String -> IO ()) -> IO ()) -> Promise a

-- Promise is a functor, as we can pre-apply the 'f : a -> b' to the 'a' in the first computation.
-- Hint: This is possible as because the 'a' is in a positive position, because it got twice negated.
export
Functor Promise where
  map f (MkPromise cmd) = MkPromise (\succ => \err => cmd (\x => succ (f x)) err)

mutual

  -- The Applicative instance of the Promise uses the succ
  -- continuation with the value injected by the 'pure' function.
  -- For the '<*>' operator it piggybacks on the monad's (>>=) operator.
  export
  Applicative Promise where
    pure x = MkPromise (\succ => \err => succ x)
    x <*> y = x >>= (\f => f <$> y)

  -- Promise is like the continuation monad, we can create a new command
  -- function applying the result of the success computation in the
  -- 'f' continuation which computes another Promise that can be unwrapped.
  export
  Monad Promise where
    (MkPromise cmd) >>= f = MkPromise (\succ =>
                                        \err =>
                                                cmd (\x =>
                                                          let (MkPromise cmd_) = (f x)
                                                          in cmd_ succ err
                                                    ) err
                                      )

||| The Promise monad under the hood relies on the IO monad, for that
||| reason we can use the IO monad, execute the IO computation and
||| evaluate the success computation with the result.
export
HasIO Promise where
  liftIO x = MkPromise (\ok => \err => x >>= ok)

||| Activate the reject branch of the Promise with the given message.
export
reject : String -> Promise a
reject msg = MkPromise (\ok, err => err msg)

||| Resolve a promise compuation.
|||
||| When the final computations for successful branch and errorneous
||| branch is given, the promise computation can be resolved, and if the
||| successful branch finished then its result is passed to the success
||| 'a -> IO ()' computation. If the errorneus branch finishes, the
||| given 'String -> IO ()' evalautes with the result error String.
export
resolve : Promise a -> (a -> IO ()) -> (String -> IO ()) -> IO ()
resolve (MkPromise cmd) = cmd

||| Alternative version of the resolve function with different argument order.
export
resolve' : (a -> IO ()) -> (String -> IO ()) -> Promise a -> IO ()
resolve' ok err (MkPromise cmd) = cmd ok err

||| On Left convert it to String and reject the promise, on Right resolve it.
export
either : Show e => Either e a -> Promise a
either (Left x)  = reject $ show x
either (Right x) = pure x

||| Helper function definition which encapsulates the essence of
||| the Promise type, PrimIO is needed for the FFI parts to
||| be easily wired in.
public export
PromiseShape : Type -> Type
PromiseShape a = (a -> IO ()) -> (String -> IO ()) -> PrimIO ()

||| Turn an FFI promise like construction into a Promise.
|||
||| The name of this function comes from its JavaScript
||| counterpart, which is also called promisify and accepts
||| two closures as arguments.
export
promisify : PromiseShape a -> Promise a
promisify prim =
  MkPromise (\ok, err => primIO $ prim ok err)
```

## File: `src/Service/NodeJS/Random.idr`
```
module Service.NodeJS.Random

%foreign "node:lambda: u => (Math.random())"
ffi_random : () -> PrimIO Double

||| Generate a random Double between 0.0 and 1.0
export
double : HasIO io => io Double
double = primIO $ ffi_random ()
```

## File: `src/Service/NodeJS/SQLite.idr`
```
module Service.NodeJS.SQLite

import Language.JSON
import Language.JSON.Schema
import Service.NodeJS.JSON
import Service.NodeJS.Promise


||| SQL statement
public export
Sql : Type
Sql = String

namespace Error

  export
  data Error : Type where [external]

  public export
  data SomeError
    = NoError
    | HasError Error

  export
  toMaybe : SomeError -> Maybe Error
  toMaybe NoError      = Nothing
  toMaybe (HasError e) = Just e

  %foreign "node:lambda: e => {return String(e);}"
  ffi_toString : Error -> PrimIO String

  export
  toString : HasIO io => Error -> io String
  toString e = primIO (ffi_toString e)

  %foreign "node:lambda: e => (String(e))"
  ffi_showError : Error -> String

  export
  Show Error where
    show e = ffi_showError e

%foreign "node:lambda: e => {if(e){return 0;}else{return 1;}}"
ffi_isNull : Error -> PrimIO Bool

isNull : Error -> IO Bool
isNull e = primIO (ffi_isNull e)

||| Checks if the error really occured
occured : HasIO io => Error -> io SomeError
occured e = do
  n <- liftIO $ isNull e
  pure $ if n then NoError else HasError e

namespace Database

  public export
  data Database : Type where [external]

  %name Database db

  %foreign "node:lambda: db => (db.close())"
  ffi_close : Database -> PrimIO ()

  export
  close : HasIO io => Database -> io ()
  close db = primIO (ffi_close db)

  %foreign "node:lambda: (db,s,er) => (db.run(s, (e) => (er(e)())))"
  ffi_run : Database -> Sql -> (Error -> PrimIO ()) -> PrimIO ()

  export
  run : Database -> Sql -> Promise SomeError
  run db sql = promisify
    (\ok, err => ffi_run db sql (\e => toPrim $ do
      putStrLn sql -- TODO: Better logging
      mErr <- occured e
      ok mErr))

  export
  data RawResult : Type where [external]

  %foreign "node:lambda: r => {if(r){return 0;}else{return 1;}}"
  ffi_isEmptyResult : RawResult -> PrimIO Bool

  isEmptyRow : HasIO io => RawResult -> io Bool
  isEmptyRow r = primIO (ffi_isEmptyResult r)

  export
  nonEmpty : HasIO io => RawResult -> io (Maybe NodeJS.JSON.JSON)
  nonEmpty r = pure $ if !(isEmptyRow r)
    then Nothing
    else Just $ believe_me r

  %foreign "node:lambda: (db,s,c) => (db.get(s,(e,r) => c(e)(r)()))"
  ffi_get : Database -> String -> (Error -> RawResult -> PrimIO ()) -> PrimIO ()

  rawGet : Database -> Sql -> Promise (Either Error RawResult)
  rawGet db sql = promisify $ \ok, err => ffi_get db sql $ \e, row => toPrim $ do
    putStrLn sql
    mErr <- occured e
    case mErr of
      NoError     => ok $ Right row
      HasError e2 => ok $ Left e2

  namespace NonSafe

    public export
    data Result
      = GetError  Error
      | JSONError String
      | EmptyRow 
      | Row       Data.JSON

    export
    get : Database -> String -> Promise Result
    get db query = do
      res <- rawGet db query
      case res of
        Left err => pure $ GetError err
        Right raw => do
          json <- nonEmpty raw
          case json of
            Nothing => pure EmptyRow
            Just j0 =>
              case !(convert j0) of
                Nothing => pure $ JSONError "FFI JSON conversion"
                Just j2 => pure $ Row j2

  namespace Safe

    public export
    data Result : Schema -> Type where
      GetError  : Error  -> Result s
      JSONError : String -> Result s
      EmptyRow            : Result s
      Row       : JSON s -> Result s

    export
    get : Database -> (s : Schema) -> String -> Promise (Result s)
    get db schema query = do
      res <- rawGet db query
      case res of
        Left err => pure $ GetError err
        Right raw => do
          json <- nonEmpty raw
          case json of
            Nothing => pure EmptyRow
            Just j0 =>
              case !(convert j0) of
                Nothing => pure $ JSONError "FFI JSON conversion"
                Just j2 => case toIndexed schema j2 of
                  Nothing => pure $ JSONError "Non-schema conforming."
                  Just j3 => pure $ Row j3

namespace SQLite

  export
  data SQLite : Type where [external]

  %foreign "node:lambda: u => (require('sqlite3').verbose())"
  ffi_require : () -> PrimIO SQLite

  export
  require : HasIO io => io SQLite
  require = primIO (ffi_require ())

  %foreign "node:lambda: (s,d,err) => (new s.Database(d,(e) => (err(e)())))"
  ffi_database : SQLite -> String -> (Error -> PrimIO ()) -> PrimIO Database

  export
  database : SQLite -> String -> Promise (Either Error Database)
  database s dbStr = promisify (\ok, err => toPrim $ do
    ok $ Right !(primIO $ ffi_database s dbStr (\e => toPrim $ do
      if !(isNull e)
        then pure ()
        else (ok (Left e)))))
```

