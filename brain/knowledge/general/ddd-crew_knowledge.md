---
id: ddd-crew-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:16.844709
---

# KNOWLEDGE EXTRACT: ddd-crew
> **Extracted on:** 2026-03-30 17:35:50
> **Source:** ddd-crew

---

## File: `context-mapping.md`
```markdown
# 📦 ddd-crew/context-mapping [🔖 PENDING/APPROVE]
🔗 https://github.com/ddd-crew/context-mapping


## Meta
- **Stars:** ⭐ 1778 | **Forks:** 🍴 151
- **Language:** N/A | **License:** CC-BY-SA-4.0
- **Last updated:** 2026-03-21
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
(No description)

## README (trích đầu)
```
# Context Mapping

Context Maps describe the contact between bounded contexts and teams with a collection of patterns. There are nine context map patterns and three different team relationships. The context map patterns describe a variety of perspectives like service provisioning, model propagation or governance aspects. This diversity of perspectives enables you to get a holistic overview of team and bounded context relationships.

Context Maps can be used to analyze existing systems or application landscapes, but they are also suitable for upfront design considerations. However, we have realized that many folks struggle to get started with the context mapping patterns based on the definitions in the existing DDD books. This GitHub repository aims to give you some help with context maps with a cheat sheet and a starter kit for Miro.

## Overview of the context map team relationships and patterns

### Team Relationships

#### Mutually Dependent

<img src="resources/mutual-dependent.jpg" alt="Mutually Dependent" width=300/>

Two teams or bounded contexts are mutually dependent when their software artifacts or systems need to be delivered together to be successful and work. You will often see a close, reciprocal link between data, functionality and capabilities of these teams. Those teams also need a lot of communication between each other in order to coordinate their efforts (see Partnership pattern).

#### Upstream Downstream

<img src="resources/upstream-downstream.jpg" alt="Upstream / Downstream" width=300/>

Actions of an upstream team will have an effect on the downstream team, but actions of the downstream do not have a significant impact on the upstream team. "The upstream team may succeed independently of the fate of the downstream team" (Quote from the [DDD Reference by Eric Evans](https://www.domainlanguage.com/ddd/reference/)).

#### Free

<img src="resources/free.jpg" alt="Free" width=300/>

A Bounded Context or a team that works in it is free if changes in other Bounded Contexts do not influence its success or failure. There is, therefore, no organizational or technical link of any kind between these teams.

### Context Map Patterns

Most publications in the Domain-Driven Design community currently describe nine context mapping patterns. 

#### Open-host Service

<img src="resources/ohs.jpg" alt="Open-host Service" height=150/>

"A protocol that gives access to your subsystem as a set of services. Open the protocol so that all who need to integrate with you can use it. Enhance and expand the protocol to handle new integration requirements, except when a single team has idiosyncratic needs. Then, use a one-off translator to augment the protocol for that special case so that the shared protocol can stay simple and coherent." ([Source: DDD Reference by Eric Evans](https://www.domainlanguage.com/ddd/reference/))

The team providing an Open-host Service is usually in an upstream position whereas the clients using it are downstream teams. T
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `eventstorming-glossary-cheat-sheet.md`
```markdown
# 📦 ddd-crew/eventstorming-glossary-cheat-sheet [🔖 PENDING/APPROVE]
🔗 https://github.com/ddd-crew/eventstorming-glossary-cheat-sheet


## Meta
- **Stars:** ⭐ 953 | **Forks:** 🍴 87
- **Language:** N/A | **License:** CC-BY-SA-4.0
- **Last updated:** 2026-03-20
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
(No description)

## README (trích đầu)
```
# EventStorming Glossary & Cheat sheet



EventStorming is the smartest approach to collaborate beyond silo boundaries. The power of EventStorming comes from a diverse multi-disciplined group of people who, together, have a lot of wisdom and knowledge. While it originally was invented for a workshop to model domain-driven design aggregates, it now has a broader spectrum. From gaining a big-picture problem space of the whole domain to gaining insight into the entire software delivery flow and creating a long term planning. Every one of these workshops has the same basic requirements and needs. 



Here you will find a combination of a glossary of terms on EventStorming core concepts written down in a consistent and comprehensive glossary. Just be sure to try and avoid jargon as much as possible, as it sets up the unnecessary insider-outsider distinction. And a Cheat sheet that you can use facilitating your own EventStorming.



## Glossary



### Core Concepts



**Domain Event**

A Domain Event is the main concept of EventStorming. It is an event that is relevant for the domain experts and contextual for the domain that is being explored. A Domain Event is a verb at the past tense. The official EventStorming colour is orange.



**HotSpot**

Hotspots are used to visualise and capture hot conflicts. Conflicts caused by, and not exclusive to, inconsistencies (in language), frictions, questions, dissent, objections, issues or procrastinating going deep to explore for later. The official EventStorming colour is neon pink and we also slightly pivot a hotspot when we use it.



**Timeline**

EventStorming is a powerful tool when we have a story to tell, when we have a timeline. The paper roll on the wall represents time from left to right. We can have parallel streams from top to bottom on the paper roll.



![Core Concepts](/_resources/core-concepts.jpg)



**Chaotic Exploration**  

Chaotic exploration can be used at the start of EventStorming. Each person writes Domain Events by themselves that they can think off. They will put these Domain Events in order they think they happen on the paper roll.



**Enforce the Timeline**  

A phase happening after chaotic exploration, meaning we try to make the timeline consistent and remove duplicate stickies.



### Big Picture EventStorming



The goal of Big Picture EventStorming is to assess the health of an existing line of business or explore the viability of a new startup business model. It helps the group create a shared state of mind of the vision of that domain of the company. We can use the output as input for Conway’s law alignment, organising business flow around teams and software with emergent bounded contexts. You can do these workshop with 10-30+ people on one paper roll.



![Example big picture](/_resources/big-picture.jpg)



**Opportunity**  

Because a Hotspot can have a negative association we also give people the chance to add opportunities. We use green because of the association it has
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

