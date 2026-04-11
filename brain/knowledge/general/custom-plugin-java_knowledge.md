# Knowledge Dump for custom-plugin-java

## File: changelog.md
```
# Changelog

## [3.0.0] - 2025-12-30

### 🎯 Production-Grade Upgrade

Complete upgrade to production-grade EQHM-compliant agent-skill architecture.

### Changed

#### Agents (8) - Production-Grade
All agents upgraded with:
- Input/Output JSON schemas
- ReAct pattern workflow
- Error handling strategies with fallbacks
- Token/cost optimization settings
- Comprehensive troubleshooting guides
- Debug checklists and log interpretation

| Agent | Role |
|-------|------|
| `01-java-fundamentals` | Java syntax, OOP, collections, streams |
| `02-java-advanced` | Concurrency, JVM internals, performance |
| `03-java-spring` | Spring Boot, MVC, Security, Cloud |
| `04-java-testing` | JUnit 5, Mockito, integration testing |
| `05-java-build-tools` | Maven, Gradle, CI/CD pipelines |
| `06-java-persistence` | JPA, Hibernate, query optimization |
| `07-java-microservices` | Spring Cloud, distributed systems |
| `08-java-devops` | Docker, Kubernetes, monitoring |

#### Skills (12) - SASMP v1.3.0 Compliant
All skills upgraded with:
- Parameter validation schemas
- Primary/Secondary bond types
- Quick reference code examples
- Troubleshooting tables
- Debug checklists

| Skill | Bonded Agent | Bond Type |
|-------|--------------|-----------|
| `java-fundamentals` | 01-java-fundamentals | PRIMARY |
| `java-concurrency` | 02-java-advanced | PRIMARY |
| `java-spring-boot` | 03-java-spring | PRIMARY |
| `java-testing` | 04-java-testing | PRIMARY |
| `java-maven-gradle` | 05-java-build-tools | PRIMARY |
| `java-jpa-hibernate` | 06-java-persistence | PRIMARY |
| `java-microservices` | 07-java-microservices | PRIMARY |
| `java-docker` | 08-java-devops | PRIMARY |
| `java-maven` | 05-java-build-tools | SECONDARY |
| `java-gradle` | 05-java-build-tools | SECONDARY |
| `java-performance` | 02-java-advanced | SECONDARY |
| `java-testing-advanced` | 04-java-testing | SECONDARY |

#### Commands (4) - v3.0.0
All commands upgraded with:
- Parameter validation in frontmatter
- Exit codes documentation
- Troubleshooting tables

### Fixed
- java-testing-advanced bonded_agent corrected to 04-java-testing
- All agent↔skill references verified
- Version consistency across all components

---

## [2.0.0] - 2025-12-29

### 🚀 Complete Rewrite

Complete rewrite with Java-specific content based on roadmap.sh structure.

### Added

#### Agents (8)
- `java-fundamentals` - Syntax, data types, control flow
- `java-oop` - Classes, inheritance, polymorphism
- `java-collections` - List, Set, Map, Queue
- `java-concurrency` - Threads, executors, CompletableFuture
- `java-build-tools` - Maven, Gradle
- `java-spring` - Spring Boot, Spring MVC
- `java-testing` - JUnit 5, Mockito
- `java-jvm` - Memory, GC, profiling

#### Skills (12) - Golden Format
- All skills with SKILL.md + assets/ + scripts/ + references/

#### Commands (4)
- `/java-check` - Environment verification
- `/java-new` - Project creation
- `/java-build` - Build automation
- `/java-debug` - Troubleshooting

### Changed
- Renamed to "java-development-assistant"
- SASMP v1.3.0 compliance

### Removed
- Generic developer roadmap content

## [1.0.0] - 2025-12-28

### Initial Release (Incorrect Content)
- Generic content (WRONG)

```

## File: contributing.md
```
# Contributing to Java Plugin

Thank you for your interest in contributing to this Claude Code plugin!

## 📋 How to Contribute

1. **Fork** the repository
2. **Create** your feature branch (`git checkout -b feature/amazing-feature`)
3. **Follow** the Golden Format for new skills
4. **Test** your changes thoroughly
5. **Commit** your changes (`git commit -m 'feat: Add amazing feature'`)
6. **Push** to the branch (`git push origin feature/amazing-feature`)
7. **Open** a Pull Request

## 📐 Guidelines

### SASMP v1.3.0 Compliance

All contributions must follow SASMP (Standardized Agent/Skill Metadata Protocol) v1.3.0:

- Agents must include `sasmp_version: "1.3.0"` and `eqhm_enabled: true`
- Skills must include `bonded_agent` and `bond_type` fields
- Commands must have YAML frontmatter

### Agent Development

```yaml
---
name: agent-name
description: Agent description
model: sonnet
tools: Read, Write, Bash
sasmp_version: "1.3.0"
eqhm_enabled: true
---
```

### Skill Development (Golden Format)

```
skills/skill-name/
├── SKILL.md          # Main skill definition
├── assets/           # Templates, configs, schemas
├── scripts/          # Automation scripts
└── references/       # Documentation, guides
```

SKILL.md frontmatter:
```yaml
---
name: skill-name
description: Skill description
sasmp_version: "1.3.0"
bonded_agent: agent-name
bond_type: PRIMARY_BOND
---
```

### Command Development

```yaml
---
name: command-name
description: Command description
allowed-tools: Read, Glob
---
```

## ✅ Testing Requirements

- Test all new features locally
- Verify agent/skill bonding
- Run `/plugin validate` before submitting
- Ensure no E-code errors

## 🔒 Code of Conduct

- Be respectful and constructive
- Follow existing code style
- Document your changes
- Test before submitting

## ❓ Questions?

Open an issue for any questions or suggestions.

---

© 2025 Dr. Umit Kacar & Muhsin Elcicek. All Rights Reserved.

```

## File: master_guide.md
```
# 🌟 DEVELOPER ROADMAP NAVIGATOR PLUGIN - MASTER GUIDE

**Version**: 1.0.0 Production Ready
**Status**: ✅ Ultra-Premium, Marketplace-Ready
**Quality**: Professional, Enterprise-Grade
**Community**: 2.1M+ developers on roadmap.sh

---

## 🎯 Executive Overview

Transform your development career with **Developer Roadmap Navigator** - an intelligent Claude Code plugin providing:

✨ **7 Specialized Agents** - Expert guidance across all development disciplines
📚 **69 Roadmaps** - Complete coverage of modern development paths
🎓 **Structured Learning** - Progressive levels from beginner to architect
🚀 **Career Advancement** - Clear paths to senior engineer and leadership roles
💼 **Interview Mastery** - Technical, system design, and behavioral prep
📊 **Real-World Workflows** - Practical step-by-step guides for common scenarios

---

##  🤖 The 7 Specialized Agents

### 1️⃣ **Web Development Specialist** 🌐
**Expertise**: Frontend, React, Vue, Angular, TypeScript, Next.js, modern web
**Perfect For**: Web developers, full-stack engineers, frontend specialists
**Career Path**: Junior Frontend → Senior Frontend → Staff Engineer → Architect
**Key Skills**: HTML5, CSS3, JavaScript, React/Vue/Angular, TypeScript, web performance
**Salary Range**: $60-90k (Junior) → $130-300k (Principal)
**Time to First Job**: 6-9 months from zero

**What You'll Learn**
- Complete HTML5, CSS3, JavaScript mastery
- Choose and master a framework (React is 70% of jobs)
- TypeScript for type safety
- Performance optimization and accessibility
- Testing strategies and build tools
- Career progression paths with salary expectations

**Quick Links**
- `/explore frontend` - Start with fundamentals
- `/explore react` - Most in-demand framework
- `/learn` - Personalized path based on your level

---

### 2️⃣ **Backend & Systems Architect** 🔧
**Expertise**: Node.js, Python, Java, Go, databases, APIs, system design
**Perfect For**: Backend engineers, full-stack developers, architects
**Career Path**: Junior Backend → Senior Backend → Staff Engineer → Architect
**Key Skills**: Node.js/Python/Java, SQL, REST/GraphQL APIs, database optimization
**Salary Range**: $60-90k (Junior) → $180-300k (Principal)
**Time to First Job**: 6-12 months from zero

**What You'll Learn**
- Backend language fundamentals (pick: Node.js, Python, Java, Go)
- REST API design and GraphQL basics
- Database design (SQL, NoSQL, caching strategies)
- System design for scale (caching, queuing, databases)
- Authentication and authorization patterns
- Production deployment and monitoring

**Quick Links**
- `/explore backend` - Start here
- `/explore nodejs` - JavaScript backend (easiest entry)
- `/explore system-design` - For senior+ roles

---

### 3️⃣ **Mobile & Data Expert** 📱
**Expertise**: iOS, Android, React Native, Flutter, Data Science, ML, AI
**Perfect For**: Mobile developers, data scientists, ML engineers
**Career Path**: Junior Mobile/Data → Senior → Staff Engineer
**Key Skills**: Swift/Kotlin, Python, ML algorithms, deep learning
**Salary Range**: $70-100k (Junior) → $170-300k+ (Principal/AI)
**Time to First Job**: 9-12 months from zero

**What You'll Learn**
- Choose mobile platform (iOS with Swift, Android with Kotlin, or cross-platform)
- Build production-quality mobile apps
- Data science fundamentals and ML algorithms
- Deep learning and LLM/AI integration
- Production ML deployment and monitoring
- Real-time features and backend integration

**Quick Links**
- `/explore ios` or `/explore android` - Native development
- `/explore flutter` or `/explore react-native` - Cross-platform
- `/explore data-scientist` - Data science path

---

### 4️⃣ **DevOps & Cloud Engineer** ☁️
**Expertise**: Docker, Kubernetes, Terraform, AWS, GCP, Azure, CI/CD
**Perfect For**: DevOps engineers, SRE, infrastructure engineers
**Career Path**: Junior DevOps → Senior DevOps → Staff → Platform Engineer
**Key Skills**: Docker, Kubernetes, Terraform, AWS, Linux, CI/CD
**Salary Range**: $80-110k (Junior) → $180-260k (Staff)
**Time to First Job**: 10-14 months from zero

**What You'll Learn**
- Linux fundamentals and system administration
- Docker containerization and best practices
- Kubernetes orchestration (production-ready)
- Infrastructure as Code (Terraform)
- Cloud platforms (AWS, GCP, or Azure)
- CI/CD pipelines and automation
- Monitoring, logging, and observability

**Quick Links**
- `/explore linux` - Start with OS fundamentals
- `/explore docker` - Containerization foundation
- `/explore kubernetes` - Container orchestration

---

### 5️⃣ **Architecture & Security Specialist** 🏗️
**Expertise**: System Design, Software Architecture, Cybersecurity, Blockchain
**Perfect For**: Architects, security engineers, senior engineers
**Career Path**: Senior Engineer → Architect → Principal Engineer
**Key Skills**: System design, security hardening, compliance, blockchain basics
**Salary Range**: $130-180k (Senior) → $200-300k+ (Principal)
**Time to Entry**: 5-8 years of solid engineering experience

**What You'll Learn**
- System design for scale (Instagram-like systems, Uber-like services)
- Distributed systems and microservices architecture
- Database scaling and optimization strategies
- Security hardening (OWASP Top 10, compliance)
- Blockchain and Web3 technologies
- Cryptography fundamentals
- Architecture decision making

**Quick Links**
- `/explore system-design` - For senior+ interview prep
- `/explore cyber-security` - Security engineering path
- `/explore blockchain` - Web3 development

---

### 6️⃣ **Leadership & Specializations** 👥
**Expertise**: Product Management, Engineering Leadership, Technical Writing, DevRel, QA, UX
**Perfect For**: Tech leads, managers, career transitioners
**Career Path**: Senior IC → Tech Lead → Manager → Director
**Key Skills**: Leadership, communication, strategic thinking, domain expertise
**Salary Range**: $130-180k (Tech Lead/Senior) → $250-400k+ (Director/VP)
**Time to Transition**: 1-2 years from senior IC role

**What You'll Learn**
- Product management fundamentals and strategy
- Engineering management and team leadership
- Technical writing and documentation excellence
- Developer relations and community building
- QA strategies and test automation
- UX/design fundamentals
- Career transitions and progression

**Quick Links**
- `/explore product-manager` - Product strategy
- `/explore engineering-manager` - Tech leadership
- `/explore technical-writer` - Documentation expertise

---

### 7️⃣ **Universal Navigator** 🗺️
**Expertise**: All 69 roadmaps, comparison, filtering, discovery
**Perfect For**: Those unsure which path to take, comparison seekers
**Special Abilities**:
- Search and filter all 69 roadmaps
- Compare technologies side-by-side
- Job market insights and salary data
- Resource curation and recommendations
- Career path planning and transitions

**Quick Links**
- `/learn` - Personalized path assessment
- `/explore react vs vue vs angular` - Framework comparison
- `/resources python --difficulty=beginner` - Curated resources

---

## 📋 The 4 Power Commands

### 1. `/learn` - Personalized Learning Path
```
Usage: /learn

What it does:
├─ Assesses your current experience level
├─ Asks about your goals and timeline
├─ Provides personalized roadmap recommendation
├─ Estimates time to job-readiness
├─ Connects you with the right agent
└─ Suggests first projects and resources

Example:
/learn
→ Level: Beginner
→ Goal: Get first web developer job
→ Recommendation: Frontend Beginner → React → Next.js (10-12 months)
→ Agent: Web Development Specialist
→ First project: Portfolio website (3 weeks)
```

### 2. `/explore` - Deep Dive Into Roadmaps
```
Usage: /explore [roadmap-name]

What it does:
├─ Detailed breakdown of any roadmap
├─ Learning phases with time estimates
├─ Key projects and milestones
├─ Tools and technologies involved
├─ Common mistakes to avoid
├─ Interview preparation tips
└─ Comparison with related paths

Examples:
/explore react
/explore kubernetes
/explore system-design
/explore react vs vue vs angular
```

### 3. `/progress` - Track Your Journey
```
Usage: /progress [optional: roadmap-name]

What it does:
├─ Visual progress on current roadmap
├─ Topics completed vs pending
├─ Time spent and learning velocity
├─ Estimated completion date
├─ Streak counting and motivation
├─ Next recommended topic
├─ Job readiness assessment
└─ Skills gap analysis

Example:
/progress react
→ 45% complete (Components & Hooks)
→ 12/25 topics done
→ Estimated finish: 4 months
→ Streak: 15 days 🔥
→ Next: Advanced state management
→ Job ready in: 3-4 months
```

### 4. `/resources` - Find Best Learning Materials
```
Usage: /resources [topic] --filters

What it does:
├─ Official documentation links
├─ Curated course recommendations
├─ Book suggestions
├─ YouTube channels and playlists
├─ Community forums and communities
├─ Practice platforms (LeetCode, HackerRank, etc)
├─ Portfolio project ideas
└─ Interview preparation resources

Examples:
/resources react --difficulty=beginner --format=video
/resources kubernetes --goal=certification
/resources system-design --goal=interview
/resources python --format=book
```

---

## 🎯 Quick Start Paths

###  Scenario 1: Complete Beginner → First Tech Job (6-12 months)
```
Month 1-2: Choose specialization
├─ Run: /learn
├─ Choose: Web, Backend, Mobile, or Data
└─ Agent: [Corresponding specialist]

Month 2-4: Fundamentals
├─ Command: /explore [roadmap-beginner]
├─ Time: 40-50 hours learning
├─ Projects: 2-3 small projects
└─ Skill check: Success checklist

Month 4-6: Intermediate
├─ Command: /explore [main-roadmap]
├─ Time: 60-80 hours learning
├─ Projects: 2-3 medium projects
└─ Skill check: Can build real-world features

Month 6-8: Advanced & Portfolio
├─ Command: /progress [roadmap]
├─ Time: 50-60 hours learning
├─ Projects: 2-3 portfolio projects
└─ Skill check: Production-ready code

Month 8-12: Job Search
├─ Interview preparation (coding + system design)
├─ Mock interviews
├─ Networking and applications
├─ Resume and portfolio polish
└─ Negotiate offers

Timeline: 6-12 months at 20 hours/week
Target Salary: $60-90k
Probability: 70% get hired within 12 months
```

### Scenario 2: Transition Between Specializations (6-9 months)
```
Example: Frontend Engineer → Backend Engineer

Month 1-2: Language Fundamentals
├─ Choose: Node.js (easiest), Python, Java, or Go
├─ Time: 30-40 hours (faster, already know CS)
└─ Projects: 2 simple projects

Month 2-4: Framework & Databases
├─ Master chosen framework
├─ Learn SQL and database design
├─ Time: 60-80 hours
└─ Projects: 2 database-backed APIs

Month 4-6: Advanced & System Design
├─ System design fundamentals
├─ Performance optimization
├─ Production deployment
├─ Time: 50-60 hours
└─ Projects: 1 full-featured backend project

Month 6-9: Job Transition
├─ Update resume and portfolio
├─ Interview preparation
├─ Target backend roles
└─ Negotiate offers

Timeline: 6-9 months at 20-30 hours/week
Current: Mid-level Frontend ($100-140k)
Target: Mid-level Backend ($100-140k or higher)
```

### Scenario 3: Senior Engineer → Architect (1-2 years)
```
Current: 5+ years solid engineering experience

Quarter 1: Deepen Technical Knowledge
├─ Master chosen specialization deeply
├─ Explore: /explore system-design
├─ Time: 20-30 hours/month
└─ Focus: Scale and optimization

Quarter 2: Learn Architecture Patterns
├─ Microservices design
├─ Distributed systems
├─ System design interviews
├─ Time: 20-30 hours/month
└─ Practice: Design real-world systems

Quarter 3: Leadership & Influence
├─ Mentor junior engineers
├─ Lead technical decisions
├─ Influence architecture
├─ Document design decisions
├─ Time: Ongoing practice
└─ Build: Thought leadership

Quarter 4: Organizational Impact
├─ Cross-team initiatives
├─ Technical strategy setting
├─ Speaking and writing
└─ Career transition to Staff/Principal

Timeline: 1-2 years
Current Salary: $130-180k
Target Salary: $180-300k+
Title Progression: Senior → Staff → Principal
```

---

## 💼 Career Advancement Blueprint

### Engineering Career Progression
```
Entry Level (0-2 years)
├─ Junior Engineer ($60-90k)
├─ Task: Learn fundamentals, assigned work
├─ Skills: Core language, basic frameworks
├─ Time: 2 years
└─ Assessment: Can complete assigned tasks well

Mid-Level (2-5 years)
├─ Mid-Level Engineer ($100-140k)
├─ Task: Own features, mentor juniors
├─ Skills: Framework mastery, system understanding
├─ Time: 3 years
└─ Assessment: Can design and deliver features

Senior Level (5-8 years)
├─ Senior Engineer ($130-180k)
├─ Task: Architecture decisions, tech strategy
├─ Skills: System design, expertise, mentoring
├─ Time: 3 years
└─ Assessment: Can design scalable systems

Staff Level (8-10 years)
├─ Staff Engineer ($150-220k)
├─ Task: Technical vision, org initiatives
├─ Skills: Deep expertise, influence
├─ Time: 2+ years
└─ Assessment: Can drive company initiatives

Principal Level (10+ years)
├─ Principal Engineer ($180-300k+)
├─ Task: Strategic decisions, mentoring leaders
├─ Skills: Visionary expertise, business alignment
└─ Assessment: Can shape company technical future
```

### Management Track
```
Senior Engineer (5-8 years, $130-180k)
    ↓
Engineering Manager (1-3 teams, $140-200k)
    ↓
Senior Manager / Director (3-10 teams, $180-280k)
    ↓
VP Engineering / CTO ($250-400k+)
    ↓
C-Level / EVP ($400k+)
```

### Specialist Track
```
Senior Engineer (5-8 years)
    ↓
Specialist (Performance / Security / Accessibility / etc)
    ↓
Principal Specialist / Expert ($180-300k+)
    ↓
Organization Leader / Thought Leader
```

---

## 📊 Salary & Job Market Insights

### By Specialization (Mid-Level Engineer, 2-5 years)
```
Frontend (React dominant): $100-140k
├─ React: $120-160k (70% jobs)
├─ Vue: $110-150k (15% jobs)
└─ Angular: $115-170k (10% jobs)

Backend (Node.js/Python dominant): $100-140k
├─ Node.js: $120-160k (70% jobs)
├─ Python: $110-150k (60% jobs)
├─ Java: $130-180k (50% jobs)
└─ Go: $120-170k (30% jobs)

Mobile (iOS/Android): $110-160k
├─ iOS: $120-180k (higher pay)
├─ Android: $110-160k
└─ Cross-platform: $100-140k

Data/ML: $110-150k
├─ Data Scientist: $110-150k
├─ ML Engineer: $120-160k
└─ AI Engineer: $130-180k

DevOps/Cloud: $120-170k
├─ DevOps: $120-160k
├─ SRE: $130-170k
└─ Cloud Architect: $140-190k
```

### By Experience Level (All specializations averaged)
```
Intern/Junior (0-2 years): $60-90k
Mid-Level (2-5 years): $100-140k
Senior (5-8 years): $130-180k
Staff (8-10 years): $150-220k
Principal (10+ years): $180-300k+
C-Level (15+ years): $250-500k+ (+ equity)
```

### Job Market Demand & Growth
```
High Demand (Easy to find jobs)
├─ React Frontend: 70% of frontend jobs
├─ Node.js Backend: 70% of JS backend jobs
├─ Python: 60% growth year-over-year
├─ Java: Stable demand, enterprise
├─ AWS: Dominant cloud platform
├─ Kubernetes: Industry standard for scale
└─ Data Engineer / ML Engineer: Rapid growth

Growing Demand (Good opportunities)
├─ Go: Microservices and DevOps
├─ Rust: Systems and performance
├─ Flutter: Cross-platform mobile
├─ AI Engineer: Emerging, high pay
├─ GCP: Growing, strong fundamentals
└─ Azure: Enterprise, Microsoft ecosystem

Stable Demand (Still opportunities)
├─ Vue: Niche but dedicated community
├─ Angular: Enterprise systems
├─ Android: Large market but competitive
├─ iOS: Premium segment
└─ Blockchain: Niche, speculative

Declining/Niche
├─ PHP (legacy)
├─ jQuery (modern frameworks replacing)
└─ CoffeeScript (ES6+ replaced it)
```

---

## 🎓 Interview Preparation Guide

### Technical Interview Structure (2-3 hours typical)

**Round 1: Coding Problem (45-60 minutes)**
```
Difficulty: Medium LeetCode level
Focus: Algorithms, data structures, problem-solving
Tools: Write code in shared editor or whiteboard
Evaluation: Correctness, code quality, communication

Topics by specialization:
Frontend: DOM manipulation, async JavaScript, algorithm basics
Backend: Algorithms, SQL, database design
Mobile: Algorithms, platform-specific APIs
Data/ML: Data manipulation, statistics, model training
DevOps: System design, infrastructure scaling
```

**Round 2: Live Coding Project (45-90 minutes)**
```
Format: Build a mini-application in real-time
Frontend example: Build a task management app with React
Backend example: Build a simple e-commerce API
Time: 45-60 minutes, partial completion is OK
Focus: Architecture, code organization, decision-making

What they're looking for:
├─ Can you think out loud?
├─ Do you ask clarifying questions?
├─ Is your code organized?
├─ Can you debug and iterate?
└─ Do you test as you go?
```

**Round 3: System Design (45-90 minutes)**
```
For Senior+ positions only

Format: Design a large-scale system
Examples: Design Instagram, Design Uber, Design Netflix
Time: 45-90 minutes with discussion
Focus: Scalability, trade-offs, technology choices

Structure:
1. Clarifying Questions (5-10 min)
2. High-Level Design (15-20 min)
3. Deep Dive (20-30 min)
4. Trade-offs Discussion (10-15 min)
5. Questions (remaining time)
```

**Round 4: Behavioral Interview (30-60 minutes)**
```
Common Questions:
1. "Tell me about a project you're proud of"
   Focus: Problem, solution, learning, impact

2. "How do you handle technical disagreements?"
   Focus: Communication, collaboration, outcomes

3. "Describe a time you failed"
   Focus: Learning, resilience, growth

4. "What interests you about this role?"
   Focus: Genuine interest, alignment, vision

STAR Method: Situation → Task → Action → Result
```

### Interview Preparation Timeline

**1 Week Before**
- Practice 5-10 LeetCode problems at target difficulty
- Review system design fundamentals
- Prepare stories for behavioral questions
- Review company and role description

**3 Days Before**
- Practice 3-5 more LeetCode problems
- Mock system design interview with friend
- Prepare questions for interview (always ask!)
- Get good sleep

**Day Before**
- Light review (don't cram)
- Prepare logistics (Zoom link, environment setup)
- Get 8+ hours sleep

**Day Of**
- 30 min before: Do quick warm-up problem
- 10 min before: Deep breathing, calm environment
- 5 min before: Tech check (camera, mic, internet)
- Interview: Think out loud, ask questions, show your best self

---

## 🚀 Success Metrics & Milestones

### Learning Success Indicators
✅ Can build projects without tutorials
✅ Can read and understand production code
✅ Can debug problems independently
✅ Can explain concepts to others
✅ Can make architectural decisions

### Job Readiness Checklist
✅ 3+ portfolio projects on GitHub
✅ Well-documented code and READMEs
✅ Can solve LeetCode medium problems
✅ Can explain system design trade-offs
✅ Can discuss technical decisions clearly
✅ Can handle rejection and iterate

### Career Growth Indicators
✅ Promotions on track (every 2-3 years)
✅ Salary in market range for role
✅ Technical leadership opportunities
✅ Speaking or writing contributions
✅ Mentoring junior engineers
✅ Influencing technical decisions

---

## 🤝 Plugin Integration Examples

### Example 1: Complete Beginner to First Job
```bash
# Week 1: Discovery
/learn
→ Assessment → Web Development Path Recommended
→ Agent: Web Development Specialist

# Week 2-4: Fundamentals
/explore frontend
/progress frontend
→ Learning HTML5, CSS3, JavaScript basics
→ Building portfolio website

# Month 2-3: Framework Selection
/explore react vs vue vs angular
→ Choose React (70% of jobs)
→ Agent recommends React roadmap

/explore react
→ Detailed React learning path
→ 4-week plan for React fundamentals

# Month 3-6: Deep Dive
/progress react
→ 25% complete, on track
→ Next: Learn hooks and state management
→ Practice: Build TODO list app

# Month 6-9: Production Skills
/explore react-interview-prep
→ Interview questions and solutions
→ Mock interview setup
/resources react --goal=interview
→ Curated resources for interview prep

# Month 9-12: Job Search
/progress react
→ 90% complete, job-ready confirmed
→ Portfolio projects polished
→ Interview prepared
→ Ready to apply!
```

### Example 2: Backend Engineer Learning System Design
```bash
# Current: Mid-level backend engineer
/learn
→ Level: Intermediate
→ Goal: Senior engineer + system design
→ Agent: Backend Systems Architect + Architecture Specialist

# Phase 1: Deep Fundamentals
/explore system-design
→ Understand scalability fundamentals
→ Learn about CAP theorem, consistency models
→ Database scaling strategies

# Phase 2: Real-World Problems
/progress system-design
→ Design Instagram (feed generation)
→ Design Uber (real-time location)
→ Design Netflix (streaming at scale)

# Phase 3: Interview Preparation
/resources system-design --goal=interview
→ Mock interview practice
→ Top 50 system design questions
→ Company-specific design questions

# Result: 6-12 months → Ready for senior roles
```

### Example 3: Transitioning to Product Management
```bash
# Current: Senior backend engineer
/learn
→ Goal: Transition to product management
→ Current experience: 6 years backend

# Phase 1: Product Fundamentals
/explore product-manager
→ Understand product strategy
→ Learn about roadmapping and OKRs
→ Understand customer-first thinking

# Phase 2: Practical Skills
/progress product-manager
→ Write 3 sample PRDs
→ Conduct 5 user interviews
→ Build simple dashboard with metrics
→ Learn pricing strategy

# Phase 3: Transition Positioning
/resources product-manager --goal=transition
→ How to position technical background
→ PM interview preparation
→ Companies hiring ex-engineers as PMs

# Result: 1-2 years → Product Manager role
```

---

## 🌟 Why This Plugin Is Different

### 1. **Comprehensive Coverage**
- No gaps or missing paths
- Every major tech is covered

### 2. **Practical & Action-Oriented**
- Real projects to build
- Workflow diagrams
- Timeline estimates
- Success checkpoints

### 3. **Career-Focused**
- Salary data by role and experience
- Job market insights
- Career progression paths
- Interview preparation

### 4. **AI-Powered Guidance**
- 7 specialized agents
- Intelligent routing
- Personalized recommendations
- Context-aware help

### 5. **Community-Driven**
- Based on 2.1M developers' input
- Real-world feedback
- Continuously updated
- Battle-tested paths

---

## 📞 Getting Started

### First Time?
1. **Run** `/learn` - Get assessed and personalized path
2. **Choose** your specialization from 7 agents
3. **Follow** recommended roadmaps
4. **Use** `/explore` for deep dives
5. **Track** `/progress` as you learn

### Already Coding?
1. **Run** `/learn` - Validate your level
2. **Explore** `/explore system-design` for advancement
3. **Track** your skill development with `/progress`
4. **Get** `/resources` for interview prep

### Switching Specializations?
1. **Run** `/learn` with transition goal
2. **Get** custom bridge path
3. **Focus** on key differences
4. **Build** transition portfolio
5. **Interview** with both backgrounds

---

## ❓ FAQ

**Q: How long until I can get a job?**
A: 6-12 months at 20 hours/week for complete beginners. 3-6 months for career switchers. 1-2 years for major transitions (e.g., IC → Manager).

**Q: Which path makes the most money?**
A: AI/ML Engineer ($130-180k+), Cloud Architect ($140-190k+), Principal Engineers ($180-300k+). But software engineering overall has good salaries across specializations.

**Q: Can I learn multiple paths simultaneously?**
A: Focus on ONE core path first (6-12 months), then add complementary skills. Learning too much at once leads to burnout.

**Q: How accurate are the time estimates?**
A: Based on 2.1M developers' experiences. Actual times vary by: learning speed, prior experience, time invested, learning efficiency. These are realistic averages.

**Q: What if I fail or need to switch paths?**
A: Completely normal. Use `/learn` to reassess and find a better path. Many successful developers changed direction multiple times.

**Q: How do I stay motivated?**
A: Use `/progress` to track streaks and celebrate milestones. Build real projects. Join communities. Find accountability partners.

---

## 🎓 Your Success Story Starts Here

Welcome to Developer Roadmap Navigator - your guide to a thriving development career.

Whether you're:
- 🌱 Just starting your coding journey
- 🔄 Switching specializations
- 📈 Advancing to senior/leadership roles
- 🚀 Building intelligent applications
- 💼 Making career transitions

...this plugin is your partner every step of the way.

**Ready to transform your career?**

```bash
/learn
```

Start now. Your future self will thank you! 🚀

---

## 📝 Document Version History

**v1.0.0** (January 2025) - Initial Release
- 7 comprehensive agents
- 69 roadmaps coverage
- 4 power commands
- Complete learning paths
- Career guidance
- Interview preparation
- Real-world workflows

---

**Made with ❤️ for developers, by developers**

*Part of Developer Roadmap Navigator - Powered by Claude*

```

## File: README.md
```
<div align="center">

<!-- Animated Typing Banner -->
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=28&duration=3000&pause=1000&color=2E9EF7&center=true&vCenter=true&multiline=true&repeat=true&width=600&height=100&lines=Java+Assistant;8+Agents+%7C+12+Skills;Claude+Code+Plugin" alt="Java Assistant" />

<br/>

<!-- Badge Row 1: Status Badges -->
[![Version](https://img.shields.io/badge/Version-3.0.0-blue?style=for-the-badge)](https://github.com/pluginagentmarketplace/custom-plugin-java/releases)
[![License](https://img.shields.io/badge/License-Custom-yellow?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production-brightgreen?style=for-the-badge)](#)
[![SASMP](https://img.shields.io/badge/SASMP-v1.3.0-blueviolet?style=for-the-badge)](#)
[![EQHM](https://img.shields.io/badge/EQHM-Enabled-green?style=for-the-badge)](#)

<!-- Badge Row 2: Content Badges -->
[![Agents](https://img.shields.io/badge/Agents-8-orange?style=flat-square&logo=robot)](#-agents)
[![Skills](https://img.shields.io/badge/Skills-12-purple?style=flat-square&logo=lightning)](#-skills)
[![Commands](https://img.shields.io/badge/Commands-4-green?style=flat-square&logo=terminal)](#-commands)

<br/>

<!-- Quick CTA Row -->
[📦 **Install Now**](#-quick-start) · [🤖 **Explore Agents**](#-agents) · [📖 **Documentation**](#-documentation) · [⭐ **Star this repo**](https://github.com/pluginagentmarketplace/custom-plugin-java)

---

### What is this?

> **Java Assistant** is a Claude Code plugin with **8 agents** and **12 skills** for java development.

</div>

---

## 📑 Table of Contents

<details>
<summary>Click to expand</summary>

- [Quick Start](#-quick-start)
- [Features](#-features)
- [Agents](#-agents)
- [Skills](#-skills)
- [Commands](#-commands)
- [Documentation](#-documentation)
- [Contributing](#-contributing)
- [License](#-license)

</details>

---

## 🚀 Quick Start

### Prerequisites

- Claude Code CLI v2.0.27+
- Active Claude subscription

### Installation (Choose One)

<details open>
<summary><strong>Option 1: From Marketplace (Recommended)</strong></summary>

```bash
# Step 1️⃣ Add the marketplace
/plugin marketplace add pluginagentmarketplace/custom-plugin-java

# Step 2️⃣ Install the plugin
/plugin install java-development-assistant@pluginagentmarketplace-java

# Step 3️⃣ Restart Claude Code
# Close and reopen your terminal/IDE
```

</details>

<details>
<summary><strong>Option 2: Local Installation</strong></summary>

```bash
# Clone the repository
git clone https://github.com/pluginagentmarketplace/custom-plugin-java.git
cd custom-plugin-java

# Load locally
/plugin load .

# Restart Claude Code
```

</details>

### ✅ Verify Installation

After restart, you should see these agents:

```
java-development-assistant:01-java-fundamentals
java-development-assistant:02-java-advanced
java-development-assistant:03-java-spring
java-development-assistant:04-java-testing
java-development-assistant:05-java-build-tools
java-development-assistant:06-java-persistence
java-development-assistant:07-java-microservices
java-development-assistant:08-java-devops
```

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🤖 **8 Agents** | Production-grade AI agents with ReAct pattern |
| 🛠️ **12 Skills** | SASMP-compliant skills with Golden Format |
| ⌨️ **4 Commands** | Quick slash commands with validation |
| 🔄 **SASMP v1.3.0** | Full protocol compliance |
| ✅ **EQHM** | Error handling, quality, and monitoring enabled |

---

## 🤖 Agents

### 8 Production-Grade Agents

| # | Agent | Purpose | Primary Skill |
|---|-------|---------|---------------|
| 1 | **01-java-fundamentals** | Java syntax, OOP, collections, streams | `java-fundamentals` |
| 2 | **02-java-advanced** | Concurrency, JVM internals, performance | `java-concurrency` |
| 3 | **03-java-spring** | Spring Boot, MVC, Security, Cloud | `java-spring-boot` |
| 4 | **04-java-testing** | JUnit 5, Mockito, integration testing | `java-testing` |
| 5 | **05-java-build-tools** | Maven, Gradle, CI/CD pipelines | `java-maven-gradle` |
| 6 | **06-java-persistence** | JPA, Hibernate, query optimization | `java-jpa-hibernate` |
| 7 | **07-java-microservices** | Spring Cloud, distributed systems | `java-microservices` |
| 8 | **08-java-devops** | Docker, Kubernetes, monitoring | `java-docker` |

---

## 🛠️ Skills

### 12 SASMP-Compliant Skills

| Skill | Description | Bond Type |
|-------|-------------|-----------|
| `java-fundamentals` | Core Java syntax, OOP, collections, streams | PRIMARY |
| `java-concurrency` | Threads, executors, CompletableFuture, virtual threads | PRIMARY |
| `java-spring-boot` | Spring Boot REST APIs, Security, Data, Actuator | PRIMARY |
| `java-testing` | JUnit 5, Mockito, integration testing, TDD | PRIMARY |
| `java-maven-gradle` | Build configuration, dependencies, CI/CD | PRIMARY |
| `java-jpa-hibernate` | Entity design, queries, transactions, caching | PRIMARY |
| `java-microservices` | Spring Cloud, service mesh, event-driven patterns | PRIMARY |
| `java-docker` | Dockerfile optimization, JVM settings, security | PRIMARY |
| `java-maven` | Maven POM, lifecycle, plugins | SECONDARY |
| `java-gradle` | Gradle Kotlin DSL, build optimization | SECONDARY |
| `java-performance` | JVM tuning, GC, profiling, benchmarking | SECONDARY |
| `java-testing-advanced` | Testcontainers, contract testing, mutation testing | SECONDARY |

---

## ⌨️ Commands

| Command | Description |
|---------|-------------|
| `/java-build` | Build Java project with Maven or Gradle |
| `/java-new` | Create a new Java project with Maven or Gradle |
| `/java-check` | Check Java and build tool installation and configuration |
| `/java-debug` | Debug Java applications and troubleshoot common issues |

---

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [LICENSE](LICENSE) | License information |

---

## 📁 Project Structure

<details>
<summary>Click to expand</summary>

```
custom-plugin-java/
├── 📁 .claude-plugin/
│   ├── plugin.json
│   └── marketplace.json
├── 📁 agents/              # 8 agents
├── 📁 skills/              # 12 skills (Golden Format)
├── 📁 commands/            # 4 commands
├── 📁 hooks/
├── 📄 README.md
├── 📄 CHANGELOG.md
└── 📄 LICENSE
```

</details>

---

## 📅 Metadata

| Field | Value |
|-------|-------|
| **Version** | 3.0.0 |
| **Last Updated** | 2025-12-30 |
| **Status** | Production Ready |
| **SASMP** | v1.3.0 |
| **EQHM** | Enabled |
| **Agents** | 8 |
| **Skills** | 12 |
| **Commands** | 4 |

---

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md).

1. Fork the repository
2. Create your feature branch
3. Follow the Golden Format for new skills
4. Submit a pull request

---

## ⚠️ Security

> **Important:** This repository contains third-party code and dependencies.
>
> - ✅ Always review code before using in production
> - ✅ Check dependencies for known vulnerabilities
> - ✅ Follow security best practices
> - ✅ Report security issues privately via [Issues](../../issues)

---

## 📝 License

Copyright © 2025 **Dr. Umit Kacar** & **Muhsin Elcicek**

Custom License - See [LICENSE](LICENSE) for details.

---

## 👥 Contributors

<table>
<tr>
<td align="center">
<strong>Dr. Umit Kacar</strong><br/>
Senior AI Researcher & Engineer
</td>
<td align="center">
<strong>Muhsin Elcicek</strong><br/>
Senior Software Architect
</td>
</tr>
</table>

---

<div align="center">

**Made with ❤️ for the Claude Code Community**

[![GitHub](https://img.shields.io/badge/GitHub-pluginagentmarketplace-black?style=for-the-badge&logo=github)](https://github.com/pluginagentmarketplace)

</div>

```

## File: _GIT_INGEST.md
```
# OmniClaw Repo Plow: CIV_FETCHED_custom-plugin-java_194736



================================================
FILE: CHANGELOG.md
================================================
# Changelog

## [3.0.0] - 2025-12-30

### 🎯 Production-Grade Upgrade

Complete upgrade to production-grade EQHM-compliant agent-skill architecture.

### Changed

#### Agents (8) - Production-Grade
All agents upgraded with:
- Input/Output JSON schemas
- ReAct pattern workflow
- Error handling strategies with fallbacks
- Token/cost optimization settings
- Comprehensive troubleshooting guides
- Debug checklists and log interpretation

| Agent | Role |
|-------|------|
| `01-java-fundamentals` | Java syntax, OOP, collections, streams |
| `02-java-advanced` | Concurrency, JVM internals, performance |
| `03-java-spring` | Spring Boot, MVC, Security, Cloud |
| `04-java-testing` | JUnit 5, Mockito, integration testing |
| `05-java-build-tools` | Maven, Gradle, CI/CD pipelines |
| `06-java-persistence` | JPA, Hibernate, query optimization |
| `07-java-microservices` | Spring Cloud, distributed systems |
| `08-java-devops` | Docker, Kubernetes, monitoring |

#### Skills (12) - SASMP v1.3.0 Compliant
All skills upgraded with:
- Parameter validation schemas
- Primary/Secondary bond types
- Quick reference code examples
- Troubleshooting tables
- Debug checklists

| Skill | Bonded Agent | Bond Type |
|-------|--------------|-----------|
| `java-fundamentals` | 01-java-fundamentals | PRIMARY |
| `java-concurrency` | 02-java-advanced | PRIMARY |
| `java-spring-boot` | 03-java-spring | PRIMARY |
| `java-testing` | 04-java-testing | PRIMARY |
| `java-maven-gradle` | 05-java-build-tools | PRIMARY |
| `java-jpa-hibernate` | 06-java-persistence | PRIMARY |
| `java-microservices` | 07-java-microservices | PRIMARY |
| `java-docker` | 08-java-devops | PRIMARY |
| `java-maven` | 05-java-build-tools | SECONDARY |
| `java-gradle` | 05-java-build-tools | SECONDARY |
| `java-performance` | 02-java-advanced | SECONDARY |
| `java-testing-advanced` | 04-java-testing | SECONDARY |

#### Commands (4) - v3.0.0
All commands upgraded with:
- Parameter validation in frontmatter
- Exit codes documentation
- Troubleshooting tables

### Fixed
- java-testing-advanced bonded_agent corrected to 04-java-testing
- All agent↔skill references verified
- Version consistency across all components

---

## [2.0.0] - 2025-12-29

### 🚀 Complete Rewrite

Complete rewrite with Java-specific content based on roadmap.sh structure.

### Added

#### Agents (8)
- `java-fundamentals` - Syntax, data types, control flow
- `java-oop` - Classes, inheritance, polymorphism
- `java-collections` - List, Set, Map, Queue
- `java-concurrency` - Threads, executors, CompletableFuture
- `java-build-tools` - Maven, Gradle
- `java-spring` - Spring Boot, Spring MVC
- `java-testing` - JUnit 5, Mockito
- `java-jvm` - Memory, GC, profiling

#### Skills (12) - Golden Format
- All skills with SKILL.md + assets/ + scripts/ + references/

#### Commands (4)
- `/java-check` - Environment verification
- `/java-new` - Project creation
- `/java-build` - Build automation
- `/java-debug` - Troubleshooting

### Changed
- Renamed to "java-development-assistant"
- SASMP v1.3.0 compliance

### Removed
- Generic developer roadmap content

## [1.0.0] - 2025-12-28

### Initial Release (Incorrect Content)
- Generic content (WRONG)


================================================
FILE: CONTRIBUTING.md
================================================
# Contributing to Java Plugin

Thank you for your interest in contributing to this Claude Code plugin!

## 📋 How to Contribute

1. **Fork** the repository
2. **Create** your feature branch (`git checkout -b feature/amazing-feature`)
3. **Follow** the Golden Format for new skills
4. **Test** your changes thoroughly
5. **Commit** your changes (`git commit -m 'feat: Add amazing feature'`)
6. **Push** to the branch (`git push origin feature/amazing-feature`)
7. **Open** a Pull Request

## 📐 Guidelines

### SASMP v1.3.0 Compliance

All contributions must follow SASMP (Standardized Agent/Skill Metadata Protocol) v1.3.0:

- Agents must include `sasmp_version: "1.3.0"` and `eqhm_enabled: true`
- Skills must include `bonded_agent` and `bond_type` fields
- Commands must have YAML frontmatter

### Agent Development

```yaml
---
name: agent-name
description: Agent description
model: sonnet
tools: Read, Write, Bash
sasmp_version: "1.3.0"
eqhm_enabled: true
---
```

### Skill Development (Golden Format)

```
skills/skill-name/
├── SKILL.md          # Main skill definition
├── assets/           # Templates, configs, schemas
├── scripts/          # Automation scripts
└── references/       # Documentation, guides
```

SKILL.md frontmatter:
```yaml
---
name: skill-name
description: Skill description
sasmp_version: "1.3.0"
bonded_agent: agent-name
bond_type: PRIMARY_BOND
---
```

### Command Development

```yaml
---
name: command-name
description: Command description
allowed-tools: Read, Glob
---
```

## ✅ Testing Requirements

- Test all new features locally
- Verify agent/skill bonding
- Run `/plugin validate` before submitting
- Ensure no E-code errors

## 🔒 Code of Conduct

- Be respectful and constructive
- Follow existing code style
- Document your changes
- Test before submitting

## ❓ Questions?

Open an issue for any questions or suggestions.

---

© 2025 Dr. Umit Kacar & Muhsin Elcicek. All Rights Reserved.


================================================
FILE: MASTER-GUIDE.md
================================================
# 🌟 DEVELOPER ROADMAP NAVIGATOR PLUGIN - MASTER GUIDE

**Version**: 1.0.0 Production Ready
**Status**: ✅ Ultra-Premium, Marketplace-Ready
**Quality**: Professional, Enterprise-Grade
**Community**: 2.1M+ developers on roadmap.sh

---

## 🎯 Executive Overview

Transform your development career with **Developer Roadmap Navigator** - an intelligent Claude Code plugin providing:

✨ **7 Specialized Agents** - Expert guidance across all development disciplines
📚 **69 Roadmaps** - Complete coverage of modern development paths
🎓 **Structured Learning** - Progressive levels from beginner to architect
🚀 **Career Advancement** - Clear paths to senior engineer and leadership roles
💼 **Interview Mastery** - Technical, system design, and behavioral prep
📊 **Real-World Workflows** - Practical step-by-step guides for common scenarios

---

##  🤖 The 7 Specialized Agents

### 1️⃣ **Web Development Specialist** 🌐
**Expertise**: Frontend, React, Vue, Angular, TypeScript, Next.js, modern web
**Perfect For**: Web developers, full-stack engineers, frontend specialists
**Career Path**: Junior Frontend → Senior Frontend → Staff Engineer → Architect
**Key Skills**: HTML5, CSS3, JavaScript, React/Vue/Angular, TypeScript, web performance
**Salary Range**: $60-90k (Junior) → $130-300k (Principal)
**Time to First Job**: 6-9 months from zero

**What You'll Learn**
- Complete HTML5, CSS3, JavaScript mastery
- Choose and master a framework (React is 70% of jobs)
- TypeScript for type safety
- Performance optimization and accessibility
- Testing strategies and build tools
- Career progression paths with salary expectations

**Quick Links**
- `/explore frontend` - Start with fundamentals
- `/explore react` - Most in-demand framework
- `/learn` - Personalized path based on your level

---

### 2️⃣ **Backend & Systems Architect** 🔧
**Expertise**: Node.js, Python, Java, Go, databases, APIs, system design
**Perfect For**: Backend engineers, full-stack developers, architects
**Career Path**: Junior Backend → Senior Backend → Staff Engineer → Architect
**Key Skills**: Node.js/Python/Java, SQL, REST/GraphQL APIs, database optimization
**Salary Range**: $60-90k (Junior) → $180-300k (Principal)
**Time to First Job**: 6-12 months from zero

**What You'll Learn**
- Backend language fundamentals (pick: Node.js, Python, Java, Go)
- REST API design and GraphQL basics
- Database design (SQL, NoSQL, caching strategies)
- System design for scale (caching, queuing, databases)
- Authentication and authorization patterns
- Production deployment and monitoring

**Quick Links**
- `/explore backend` - Start here
- `/explore nodejs` - JavaScript backend (easiest entry)
- `/explore system-design` - For senior+ roles

---

### 3️⃣ **Mobile & Data Expert** 📱
**Expertise**: iOS, Android, React Native, Flutter, Data Science, ML, AI
**Perfect For**: Mobile developers, data scientists, ML engineers
**Career Path**: Junior Mobile/Data → Senior → Staff Engineer
**Key Skills**: Swift/Kotlin, Python, ML algorithms, deep learning
**Salary Range**: $70-100k (Junior) → $170-300k+ (Principal/AI)
**Time to First Job**: 9-12 months from zero

**What You'll Learn**
- Choose mobile platform (iOS with Swift, Android with Kotlin, or cross-platform)
- Build production-quality mobile apps
- Data science fundamentals and ML algorithms
- Deep learning and LLM/AI integration
- Production ML deployment and monitoring
- Real-time features and backend integration

**Quick Links**
- `/explore ios` or `/explore android` - Native development
- `/explore flutter` or `/explore react-native` - Cross-platform
- `/explore data-scientist` - Data science path

---

### 4️⃣ **DevOps & Cloud Engineer** ☁️
**Expertise**: Docker, Kubernetes, Terraform, AWS, GCP, Azure, CI/CD
**Perfect For**: DevOps engineers, SRE, infrastructure engineers
**Career Path**: Junior DevOps → Senior DevOps → Staff → Platform Engineer
**Key Skills**: Docker, Kubernetes, Terraform, AWS, Linux, CI/CD
**Salary Range**: $80-110k (Junior) → $180-260k (Staff)
**Time to First Job**: 10-14 months from zero

**What You'll Learn**
- Linux fundamentals and system administration
- Docker containerization and best practices
- Kubernetes orchestration (production-ready)
- Infrastructure as Code (Terraform)
- Cloud platforms (AWS, GCP, or Azure)
- CI/CD pipelines and automation
- Monitoring, logging, and observability

**Quick Links**
- `/explore linux` - Start with OS fundamentals
- `/explore docker` - Containerization foundation
- `/explore kubernetes` - Container orchestration

---

### 5️⃣ **Architecture & Security Specialist** 🏗️
**Expertise**: System Design, Software Architecture, Cybersecurity, Blockchain
**Perfect For**: Architects, security engineers, senior engineers
**Career Path**: Senior Engineer → Architect → Principal Engineer
**Key Skills**: System design, security hardening, compliance, blockchain basics
**Salary Range**: $130-180k (Senior) → $200-300k+ (Principal)
**Time to Entry**: 5-8 years of solid engineering experience

*

================================================
FILE: README.md
================================================
<div align="center">

<!-- Animated Typing Banner -->
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=28&duration=3000&pause=1000&color=2E9EF7&center=true&vCenter=true&multiline=true&repeat=true&width=600&height=100&lines=Java+Assistant;8+Agents+%7C+12+Skills;Claude+Code+Plugin" alt="Java Assistant" />

<br/>

<!-- Badge Row 1: Status Badges -->
[![Version](https://img.shields.io/badge/Version-3.0.0-blue?style=for-the-badge)](https://github.com/pluginagentmarketplace/custom-plugin-java/releases)
[![License](https://img.shields.io/badge/License-Custom-yellow?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production-brightgreen?style=for-the-badge)](#)
[![SASMP](https://img.shields.io/badge/SASMP-v1.3.0-blueviolet?style=for-the-badge)](#)
[![EQHM](https://img.shields.io/badge/EQHM-Enabled-green?style=for-the-badge)](#)

<!-- Badge Row 2: Content Badges -->
[![Agents](https://img.shields.io/badge/Agents-8-orange?style=flat-square&logo=robot)](#-agents)
[![Skills](https://img.shields.io/badge/Skills-12-purple?style=flat-square&logo=lightning)](#-skills)
[![Commands](https://img.shields.io/badge/Commands-4-green?style=flat-square&logo=terminal)](#-commands)

<br/>

<!-- Quick CTA Row -->
[📦 **Install Now**](#-quick-start) · [🤖 **Explore Agents**](#-agents) · [📖 **Documentation**](#-documentation) · [⭐ **Star this repo**](https://github.com/pluginagentmarketplace/custom-plugin-java)

---

### What is this?

> **Java Assistant** is a Claude Code plugin with **8 agents** and **12 skills** for java development.

</div>

---

## 📑 Table of Contents

<details>
<summary>Click to expand</summary>

- [Quick Start](#-quick-start)
- [Features](#-features)
- [Agents](#-agents)
- [Skills](#-skills)
- [Commands](#-commands)
- [Documentation](#-documentation)
- [Contributing](#-contributing)
- [License](#-license)

</details>

---

## 🚀 Quick Start

### Prerequisites

- Claude Code CLI v2.0.27+
- Active Claude subscription

### Installation (Choose One)

<details open>
<summary><strong>Option 1: From Marketplace (Recommended)</strong></summary>

```bash
# Step 1️⃣ Add the marketplace
/plugin marketplace add pluginagentmarketplace/custom-plugin-java

# Step 2️⃣ Install the plugin
/plugin install java-development-assistant@pluginagentmarketplace-java

# Step 3️⃣ Restart Claude Code
# Close and reopen your terminal/IDE
```

</details>

<details>
<summary><strong>Option 2: Local Installation</strong></summary>

```bash
# Clone the repository
git clone https://github.com/pluginagentmarketplace/custom-plugin-java.git
cd custom-plugin-java

# Load locally
/plugin load .

# Restart Claude Code
```

</details>

### ✅ Verify Installation

After restart, you should see these agents:

```
java-development-assistant:01-java-fundamentals
java-development-assistant:02-java-advanced
java-development-assistant:03-java-spring
java-development-assistant:04-java-testing
java-development-assistant:05-java-build-tools
java-development-assistant:06-java-persistence
java-development-assistant:07-java-microservices
java-development-assistant:08-java-devops
```

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🤖 **8 Agents** | Production-grade AI agents with ReAct pattern |
| 🛠️ **12 Skills** | SASMP-compliant skills with Golden Format |
| ⌨️ **4 Commands** | Quick slash commands with validation |
| 🔄 **SASMP v1.3.0** | Full protocol compliance |
| ✅ **EQHM** | Error handling, quality, and monitoring enabled |

---

## 🤖 Agents

### 8 Production-Grade Agents

| # | Agent | Purpose | Primary Skill |
|---|-------|---------|---------------|
| 1 | **01-java-fundamentals** | Java syntax, OOP, collections, streams | `java-fundamentals` |
| 2 | **02-java-advanced** | Concurrency, JVM internals, performance | `java-concurrency` |
| 3 | **03-java-spring** | Spring Boot, MVC, Security, Cloud | `java-spring-boot` |
| 4 | **04-java-testing** | JUnit 5, Mockito, integration testing | `java-testing` |
| 5 | **05-java-build-tools** | Maven, Gradle, CI/CD pipelines | `java-maven-gradle` |
| 6 | **06-java-persistence** | JPA, Hibernate, query optimization | `java-jpa-hibernate` |
| 7 | **07-java-microservices** | Spring Cloud, distributed systems | `java-microservices` |
| 8 | **08-java-devops** | Docker, Kubernetes, monitoring | `java-docker` |

---

## 🛠️ Skills

### 12 SASMP-Compliant Skills

| Skill | Description | Bond Type |
|-------|-------------|-----------|
| `java-fundamentals` | Core Java syntax, OOP, collections, streams | PRIMARY |
| `java-concurrency` | Threads, executors, CompletableFuture, virtual threads | PRIMARY |
| `java-spring-boot` | Spring Boot REST APIs, Security, Data, Actuator | PRIMARY |
| `java-testing` | JUnit 5, Mockito, integration testing, TDD | PRIMARY |
| `java-maven-gradle` | Build configuration, dependencies, CI/CD | PRIMARY |
| `java-jpa-hibernate` | Entity design, queries, transactions, caching | PRIMARY |
| `java-microservices` | Spring Cloud, s

================================================
FILE: .claude-plugin\marketplace.json
================================================
{
  "marketplace_id": "java-development-assistant",
  "display_name": "Java Development Assistant",
  "category": "Programming Languages",
  "tags": ["java", "spring-boot", "jvm", "maven", "gradle"],
  "visibility": "public",
  "featured": true,
  "downloads": 0,
  "rating": 0,
  "created_at": "2025-12-29",
  "updated_at": "2025-12-29",
  "source": "./",
  "sasmp_version": "1.3.0",
  "eqhm_enabled": true
}


================================================
FILE: .claude-plugin\plugin.json
================================================
{
  "schema_version": "1.0.0",
  "name": "java-development-assistant",
  "version": "3.0.0",
  "description": "Production-grade Java development plugin with 8 specialized agents, 12 SASMP-compliant skills, and 4 commands for core Java, Spring, testing, DevOps, and enterprise development",
  "author": {
    "name": "Dr. Umit Kacar & Muhsin Elcicek",
    "email": "kacarumit.phd@gmail.com"
  },
  "repository": "https://github.com/pluginagentmarketplace/custom-plugin-java",
  "license": "SEE LICENSE IN LICENSE",
  "keywords": [
    "java",
    "spring-boot",
    "maven",
    "gradle",
    "jvm",
    "collections",
    "concurrency",
    "junit",
    "testing",
    "microservices",
    "docker",
    "performance"
  ],
  "agents": [
    "./agents/01-java-fundamentals.md",
    "./agents/02-java-advanced.md",
    "./agents/03-java-spring.md",
    "./agents/04-java-testing.md",
    "./agents/05-java-build-tools.md",
    "./agents/06-java-persistence.md",
    "./agents/07-java-microservices.md",
    "./agents/08-java-devops.md"
  ],
  "skills": [
    "./skills/java-fundamentals/SKILL.md",
    "./skills/java-spring-boot/SKILL.md",
    "./skills/java-testing/SKILL.md",
    "./skills/java-concurrency/SKILL.md",
    "./skills/java-jpa-hibernate/SKILL.md",
    "./skills/java-maven-gradle/SKILL.md",
    "./skills/java-microservices/SKILL.md",
    "./skills/java-maven/SKILL.md",
    "./skills/java-gradle/SKILL.md",
    "./skills/java-docker/SKILL.md",
    "./skills/java-testing-advanced/SKILL.md",
    "./skills/java-performance/SKILL.md"
  ],
  "commands": [
    "./commands/java-check.md",
    "./commands/java-new.md",
    "./commands/java-build.md",
    "./commands/java-debug.md"
  ]
}


================================================
FILE: agents\01-java-fundamentals.md
================================================
---
name: 01-java-fundamentals
description: Java fundamentals expert - syntax, OOP, collections, streams, exception handling
model: sonnet
tools: Read, Write, Bash, Glob, Grep
sasmp_version: "1.3.0"
eqhm_enabled: true
skills:
  - java-fundamentals
  - java-concurrency
  - java-microservices
  - java-spring-boot
  - java-docker
  - java-performance
  - java-testing
  - java-maven-gradle
  - java-testing-advanced
  - java-jpa-hibernate
  - java-maven
  - java-gradle
triggers:
  - "java java"
  - "java"
  - "spring"
  - "java fundamentals"
version: "3.0.0"

# Input/Output Schema
input_schema:
  type: object
  properties:
    task_type:
      type: string
      enum: [code_review, implementation, refactoring, debugging, explanation]
    code_context:
      type: string
      description: Existing code or project context
    requirements:
      type: string
      description: What needs to be accomplished
  required: [task_type, requirements]

output_schema:
  type: object
  properties:
    solution:
      type: string
      description: Implemented code or explanation
    explanation:
      type: string
      description: Reasoning behind the solution
    best_practices:
      type: array
      items:
        type: string
    warnings:
      type: array
      items:
        type: string

# Cost Optimization
token_budget: 8000
max_iterations: 5
prefer_streaming: true
---

# 01 Java Fundamentals Agent

Expert agent for core Java programming concepts, syntax, and foundational patterns.

## Role & Responsibilities

**Primary Role**: Guide developers through Java fundamentals with production-quality code

**Boundaries**:
- ✅ Core Java syntax (Java 8-21)
- ✅ OOP principles (SOLID, inheritance, polymorphism)
- ✅ Collections Framework (List, Set, Map, Queue)
- ✅ Streams API & functional programming
- ✅ Exception handling patterns
- ✅ Generics and type safety
- ❌ Framework-specific code (delegate to spring/persistence agents)
- ❌ Build tool configuration (delegate to build-tools agent)

## Expertise Areas

### Core Language Features
- **Syntax Mastery**: Variables, operators, control flow, methods, classes
- **OOP Design**: Encapsulation, inheritance, polymorphism, abstraction
- **Type System**: Primitives, wrappers, generics, type inference (var)
- **Memory Model**: Stack vs heap, garbage collection basics

### Collections & Data Structures
- **List Implementations**: ArrayList, LinkedList, CopyOnWriteArrayList
- **Set Implementations**: HashSet, TreeSet, LinkedHashSet, EnumSet
- **Map Implementations**: HashMap, TreeMap, LinkedHashMap, ConcurrentHashMap
- **Queue/Deque**: ArrayDeque, PriorityQueue, BlockingQueue

### Functional Programming
- **Lambda Expressions**: Syntax, functional interfaces, method references
- **Stream Operations**: filter, map, flatMap, reduce, collect
- **Optional**: Null-safe programming patterns
- **Parallel Streams**: When to use, performance considerations

### Exception Handling
- **Checked vs Unchecked**: Design decisions, when to use each
- **Try-with-resources**: AutoCloseable pattern
- **Custom Exceptions**: Business exception hierarchies
- **Error Recovery**: Graceful degradation patterns

## ReAct Pattern Workflow

```
1. REASON: Analyze the Java programming task
   - Identify core concepts involved
   - Determine Java version requirements
   - Check for OOP design considerations

2. ACT: Implement solution using appropriate tools
   - Read existing code context
   - Write clean, idiomatic Java code
   - Apply SOLID principles

3. OBSERVE: Validate the implementation
   - Review code for best practices
   - Check for common pitfalls
   - Ensure type safety
```

## Error Handling Strategy

```java
// Pattern: Hierarchical exception handling
public class JavaFundamentalsErrorHandler {

    // Level 1: Validation errors
    public void handleValidationError(String context) {
        // Log and provide clear error message
        // Suggest fix based on common patterns
    }

    // Level 2: Compilation errors
    public void handleCompilationError(String error) {
        // Parse error message
        // Identify root cause
        // Provide targeted fix
    }

    // Level 3: Runtime errors
    public void handleRuntimeError(Exception e) {
        // Capture stack trace
        // Identify failure point
        // Suggest debugging steps
    }
}
```

## Fallback Strategies

| Scenario | Primary Action | Fallback |
|----------|---------------|----------|
| Code doesn't compile | Fix syntax errors | Provide step-by-step debugging |
| Performance issue | Profile and optimize | Suggest alternative data structures |
| Design unclear | Apply SOLID principles | Provide multiple design options |
| Version incompatibility | Use compatible syntax | Document version requirements |

## Code Quality Standards

```java
// ✅ GOOD: Clean, readable, idiomatic Java
public List<String> filterActiveUsers(List<User> users) {
    return users.stream()
        .filter(User::isActive)
        .map(User::getN

================================================
FILE: agents\02-java-advanced.md
================================================
---
name: 02-java-advanced
description: Java advanced expert - concurrency, JVM internals, performance optimization
model: sonnet
tools: Read, Write, Bash, Glob, Grep
sasmp_version: "1.3.0"
eqhm_enabled: true
skills:
  - java-fundamentals
  - java-concurrency
  - java-microservices
  - java-spring-boot
  - java-docker
  - java-performance
  - java-testing
  - java-maven-gradle
  - java-testing-advanced
  - java-jpa-hibernate
  - java-maven
  - java-gradle
triggers:
  - "java java"
  - "java"
  - "spring"
  - "java advanced"
version: "3.0.0"

# Input/Output Schema
input_schema:
  type: object
  properties:
    task_type:
      type: string
      enum: [concurrency, jvm_tuning, profiling, optimization, memory_analysis]
    performance_context:
      type: string
      description: Current performance metrics or issues
    requirements:
      type: string
      description: Performance goals or concurrency needs
  required: [task_type, requirements]

output_schema:
  type: object
  properties:
    solution:
      type: string
      description: Optimized implementation
    metrics:
      type: object
      description: Expected performance improvements
    jvm_flags:
      type: array
      items:
        type: string
    warnings:
      type: array
      items:
        type: string

# Cost Optimization
token_budget: 10000
max_iterations: 7
prefer_streaming: true
---

# 02 Java Advanced Agent

Expert agent for advanced Java topics including concurrency, JVM internals, and performance optimization.

## Role & Responsibilities

**Primary Role**: Solve complex Java performance and concurrency challenges

**Boundaries**:
- ✅ Concurrency (threads, executors, locks, atomic operations)
- ✅ JVM internals (memory model, GC, class loading)
- ✅ Performance profiling and optimization
- ✅ Memory management and leak detection
- ✅ Virtual Threads (Java 21+)
- ❌ Application framework issues (delegate to spring agent)
- ❌ Database performance (delegate to persistence agent)

## Expertise Areas

### Concurrency & Multithreading
- **Thread Management**: Thread lifecycle, daemon threads, thread pools
- **Synchronization**: synchronized, volatile, locks (ReentrantLock, ReadWriteLock)
- **Concurrent Collections**: ConcurrentHashMap, CopyOnWriteArrayList, BlockingQueue
- **Executors**: ThreadPoolExecutor, ScheduledExecutor, ForkJoinPool
- **CompletableFuture**: Async programming, composition, error handling
- **Virtual Threads**: Project Loom, structured concurrency (Java 21+)

### JVM Internals
- **Memory Model**: Heap, stack, metaspace, direct memory
- **Garbage Collection**: G1, ZGC, Shenandoah, tuning strategies
- **Class Loading**: Bootstrap, extension, application classloaders
- **JIT Compilation**: Tiered compilation, hot spot optimization
- **Native Memory**: Off-heap storage, ByteBuffer, Unsafe

### Performance Optimization
- **Profiling Tools**: JFR, async-profiler, VisualVM, JMC
- **Benchmarking**: JMH microbenchmarks, load testing
- **Memory Analysis**: Heap dumps, MAT, leak detection
- **CPU Optimization**: Hot path analysis, cache optimization
- **I/O Optimization**: NIO, async I/O, buffer pooling

## ReAct Pattern Workflow

```
1. REASON: Analyze performance/concurrency issue
   - Profile current behavior
   - Identify bottlenecks or race conditions
   - Determine JVM resource usage

2. ACT: Implement optimizations
   - Apply appropriate concurrency patterns
   - Tune JVM settings
   - Optimize hot paths

3. OBSERVE: Measure improvements
   - Benchmark before/after
   - Validate thread safety
   - Monitor resource usage
```

## Error Handling Strategy

```java
// Pattern: Robust concurrency error handling
public class ConcurrencyErrorHandler {

    private static final Logger log = LoggerFactory.getLogger(ConcurrencyErrorHandler.class);

    // Deadlock detection
    public void detectDeadlock() {
        ThreadMXBean bean = ManagementFactory.getThreadMXBean();
        long[] deadlockedThreads = bean.findDeadlockedThreads();
        if (deadlockedThreads != null) {
            ThreadInfo[] infos = bean.getThreadInfo(deadlockedThreads, true, true);
            log.error("Deadlock detected: {}", Arrays.toString(infos));
        }
    }

    // Thread pool rejection handling
    public RejectedExecutionHandler createRejectionHandler() {
        return (r, executor) -> {
            log.warn("Task rejected, queue full. Applying backpressure...");
            try {
                executor.getQueue().put(r);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                throw new RejectedExecutionException("Interrupted while waiting", e);
            }
        };
    }
}
```

## Fallback Strategies

| Scenario | Primary Action | Fallback |
|----------|---------------|----------|
| Deadlock detected | Thread dump analysis | Timeout-based recovery |
| Memory leak | Heap dump analysis | Force GC + monitoring |
| Thread pool exhaustion | Increase pool size | Implement backpre

================================================
FILE: agents\03-java-spring.md
================================================
---
name: 03-java-spring
description: Spring Framework expert - Spring Boot, MVC, Security, Data, Cloud
model: sonnet
tools: Read, Write, Bash, Glob, Grep
sasmp_version: "1.3.0"
eqhm_enabled: true
skills:
  - java-fundamentals
  - java-concurrency
  - java-microservices
  - java-spring-boot
  - java-docker
  - java-performance
  - java-testing
  - java-maven-gradle
  - java-testing-advanced
  - java-jpa-hibernate
  - java-maven
  - java-gradle
triggers:
  - "java java"
  - "java"
  - "spring"
version: "3.0.0"

# Input/Output Schema
input_schema:
  type: object
  properties:
    task_type:
      type: string
      enum: [api_development, security, configuration, integration, migration]
    spring_version:
      type: string
      description: Target Spring Boot version (e.g., 3.2.x)
    requirements:
      type: string
      description: Feature or issue to address
  required: [task_type, requirements]

output_schema:
  type: object
  properties:
    solution:
      type: string
      description: Spring implementation
    configuration:
      type: object
      description: Required application properties
    dependencies:
      type: array
      items:
        type: string
    security_notes:
      type: array
      items:
        type: string

# Cost Optimization
token_budget: 10000
max_iterations: 6
prefer_streaming: true
---

# 03 Java Spring Agent

Expert agent for Spring Framework ecosystem including Spring Boot, MVC, Security, and Cloud.

## Role & Responsibilities

**Primary Role**: Build production-ready Spring Boot applications

**Boundaries**:
- ✅ Spring Boot application architecture
- ✅ Spring MVC / WebFlux REST APIs
- ✅ Spring Security (authentication, authorization)
- ✅ Spring Data (JPA, MongoDB, Redis)
- ✅ Spring Cloud (Config, Gateway, Eureka)
- ✅ Spring Native / GraalVM compilation
- ❌ Raw JDBC/SQL optimization (delegate to persistence agent)
- ❌ Container orchestration (delegate to devops agent)

## Expertise Areas

### Spring Boot Core
- **Auto-configuration**: Understanding and customizing
- **Starters**: Selecting appropriate dependencies
- **Profiles**: Environment-specific configuration
- **Actuator**: Health checks, metrics, monitoring
- **DevTools**: Hot reload, live reload configuration

### Spring MVC & WebFlux
- **Controllers**: REST, HATEOAS, content negotiation
- **Validation**: Bean Validation, custom validators
- **Exception Handling**: @ControllerAdvice, ProblemDetail
- **WebFlux**: Reactive programming, Mono/Flux
- **WebClient**: Non-blocking HTTP client

### Spring Security
- **Authentication**: Form, Basic, OAuth2, JWT, SAML
- **Authorization**: Method security, URL patterns, RBAC
- **CSRF/CORS**: Protection configuration
- **Password Encoding**: BCrypt, Argon2, SCrypt
- **Security Filters**: Custom filter chains

### Spring Data
- **JPA**: Repositories, specifications, projections
- **Query Methods**: Derived queries, @Query, native
- **Transactions**: @Transactional, propagation, isolation
- **Auditing**: @CreatedDate, @LastModifiedBy
- **Pagination**: Page, Slice, Sort

### Spring Cloud
- **Config Server**: Centralized configuration
- **Service Discovery**: Eureka, Consul
- **API Gateway**: Spring Cloud Gateway, routing
- **Circuit Breaker**: Resilience4j integration
- **Distributed Tracing**: Micrometer, Zipkin

## ReAct Pattern Workflow

```
1. REASON: Analyze Spring application requirements
   - Identify required Spring modules
   - Determine security requirements
   - Plan API structure and data flow

2. ACT: Implement Spring components
   - Create configurations and beans
   - Implement controllers and services
   - Configure security and data access

3. OBSERVE: Validate Spring application
   - Test with Actuator endpoints
   - Verify security configuration
   - Check auto-configuration reports
```

## Error Handling Strategy

```java
// Pattern: Global exception handling with ProblemDetail (RFC 7807)
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(EntityNotFoundException.class)
    public ProblemDetail handleNotFound(EntityNotFoundException ex) {
        ProblemDetail problem = ProblemDetail.forStatusAndDetail(
            HttpStatus.NOT_FOUND, ex.getMessage());
        problem.setTitle("Resource Not Found");
        problem.setProperty("timestamp", Instant.now());
        return problem;
    }

    @ExceptionHandler(ConstraintViolationException.class)
    public ProblemDetail handleValidation(ConstraintViolationException ex) {
        ProblemDetail problem = ProblemDetail.forStatusAndDetail(
            HttpStatus.BAD_REQUEST, "Validation failed");
        problem.setProperty("violations", ex.getConstraintViolations().stream()
            .map(v -> Map.of("field", v.getPropertyPath().toString(),
                            "message", v.getMessage()))
            .toList());
        return problem;
    }

    @ExceptionHandler(Exception.class)
    public ProblemDetail handleGeneric(Exception ex) {
        log.error("Unexpected 

================================================
FILE: agents\04-java-testing.md
================================================
---
name: 04-java-testing
description: Java testing expert - JUnit 5, Mockito, integration testing, TDD/BDD
model: sonnet
tools: Read, Write, Bash, Glob, Grep
sasmp_version: "1.3.0"
eqhm_enabled: true
skills:
  - java-fundamentals
  - java-concurrency
  - java-microservices
  - java-spring-boot
  - java-docker
  - java-performance
  - java-testing
  - java-maven-gradle
  - java-testing-advanced
  - java-jpa-hibernate
  - java-maven
  - java-gradle
triggers:
  - "java java"
  - "java"
  - "spring"
  - "java testing"
version: "3.0.0"

# Input/Output Schema
input_schema:
  type: object
  properties:
    task_type:
      type: string
      enum: [unit_test, integration_test, e2e_test, test_refactor, coverage_improvement]
    code_to_test:
      type: string
      description: Source code or class reference to test
    coverage_target:
      type: number
      description: Target code coverage percentage
  required: [task_type]

output_schema:
  type: object
  properties:
    test_code:
      type: string
      description: Generated test implementation
    test_strategy:
      type: string
      description: Explanation of testing approach
    coverage_estimate:
      type: number
    recommendations:
      type: array
      items:
        type: string

# Cost Optimization
token_budget: 8000
max_iterations: 5
prefer_streaming: true
---

# 04 Java Testing Agent

Expert agent for comprehensive Java testing with JUnit 5, Mockito, and modern testing practices.

## Role & Responsibilities

**Primary Role**: Ensure code quality through comprehensive testing strategies

**Boundaries**:
- ✅ Unit testing with JUnit 5
- ✅ Mocking with Mockito, MockK (Kotlin)
- ✅ Integration testing (Spring, Testcontainers)
- ✅ API testing (RestAssured, MockMvc)
- ✅ TDD/BDD practices
- ✅ Test coverage analysis
- ❌ Load testing infrastructure (delegate to devops)
- ❌ Security penetration testing

## Expertise Areas

### Unit Testing
- **JUnit 5**: @Test, @ParameterizedTest, @Nested, @DisplayName
- **Assertions**: AssertJ fluent assertions, custom matchers
- **Lifecycle**: @BeforeEach, @AfterAll, @TestInstance
- **Extensions**: Custom extensions, conditional execution

### Mocking
- **Mockito**: @Mock, @InjectMocks, @Spy, @Captor
- **Stubbing**: when/thenReturn, doThrow, argument matchers
- **Verification**: verify, times, never, inOrder
- **BDD Style**: given/willReturn, then/should

### Integration Testing
- **Spring Boot Test**: @SpringBootTest, @WebMvcTest, @DataJpaTest
- **Testcontainers**: Docker-based integration tests
- **Database**: @Sql, @Transactional, H2/embedded
- **API Testing**: MockMvc, RestAssured, WebTestClient

## ReAct Pattern Workflow

```
1. REASON: Analyze code to be tested
   - Identify testable units and boundaries
   - Determine test types needed
   - Plan mocking strategy

2. ACT: Implement tests
   - Write unit tests with proper isolation
   - Create integration tests for critical paths
   - Set up test fixtures and data

3. OBSERVE: Validate test quality
   - Run tests and verify passing
   - Check coverage metrics
   - Review mutation test results
```

## Testing Patterns

```java
// Pattern 1: Parameterized Testing
@ParameterizedTest
@CsvSource({
    "valid@email.com, true",
    "invalid-email, false",
    "'', false"
})
@DisplayName("Should validate email format correctly")
void shouldValidateEmailFormat(String email, boolean expected) {
    assertThat(validator.isValidEmail(email)).isEqualTo(expected);
}

// Pattern 2: Builder for Test Data
public class UserTestBuilder {
    private String name = "John Doe";
    private String email = "john@example.com";
    private Role role = Role.USER;

    public static UserTestBuilder aUser() { return new UserTestBuilder(); }
    public UserTestBuilder withName(String n) { this.name = n; return this; }
    public UserTestBuilder asAdmin() { this.role = Role.ADMIN; return this; }
    public User build() { return new User(name, email, role); }
}

// Pattern 3: Mockito BDD Style
@Test
void shouldCalculateDiscountForPremiumUsers() {
    given(userRepository.findById(1L)).willReturn(Optional.of(premiumUser));
    given(discountService.getPremiumDiscount()).willReturn(0.2);

    var price = orderService.calculateFinalPrice(1L, 100.0);

    then(discountService).should().getPremiumDiscount();
    assertThat(price).isEqualTo(80.0);
}

// Pattern 4: Testcontainers Integration
@Testcontainers
@SpringBootTest
class OrderRepositoryIntegrationTest {

    @Container
    static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>("postgres:15");

    @DynamicPropertySource
    static void configureProperties(DynamicPropertyRegistry registry) {
        registry.add("spring.datasource.url", postgres::getJdbcUrl);
        registry.add("spring.datasource.username", postgres::getUsername);
        registry.add("spring.datasource.password", postgres::getPassword);
    }

    @Test
    void shouldPersistOrderWithItems() {
        var order = new Order(List.of(new Item("Product", 10.0)

================================================
FILE: agents\05-java-build-tools.md
================================================
---
name: 05-java-build-tools
description: Build tools expert - Maven, Gradle, dependency management, CI/CD pipelines
model: sonnet
tools: Read, Write, Bash, Glob, Grep
sasmp_version: "1.3.0"
eqhm_enabled: true
skills:
  - java-fundamentals
  - java-concurrency
  - java-microservices
  - java-spring-boot
  - java-docker
  - java-performance
  - java-testing
  - java-maven-gradle
  - java-testing-advanced
  - java-jpa-hibernate
  - java-maven
  - java-gradle
triggers:
  - "java java"
  - "java"
  - "spring"
version: "3.0.0"

# Input/Output Schema
input_schema:
  type: object
  properties:
    task_type:
      type: string
      enum: [project_setup, dependency_management, build_optimization, ci_cd, migration]
    build_tool:
      type: string
      enum: [maven, gradle]
    project_type:
      type: string
      enum: [single_module, multi_module, library, spring_boot]
  required: [task_type, build_tool]

output_schema:
  type: object
  properties:
    build_files:
      type: array
      description: Generated or modified build files
    commands:
      type: array
      description: Build/run commands
    ci_config:
      type: string
    dependencies:
      type: array

# Cost Optimization
token_budget: 8000
max_iterations: 5
prefer_streaming: true
---

# 05 Java Build Tools Agent

Expert agent for Maven, Gradle, and build automation with CI/CD integration.

## Role & Responsibilities

**Primary Role**: Configure and optimize Java build systems

**Boundaries**:
- ✅ Maven configuration and plugins
- ✅ Gradle (Groovy & Kotlin DSL)
- ✅ Dependency management (BOM, versions)
- ✅ Multi-module project structures
- ✅ Build optimization (caching, parallel)
- ✅ CI/CD pipeline configuration
- ❌ Container orchestration (delegate to devops)
- ❌ Infrastructure as code

## Expertise Areas

### Maven
- **Project Structure**: POM hierarchy, modules, parent POMs
- **Lifecycle**: clean, compile, test, package, install, deploy
- **Plugins**: compiler, surefire, failsafe, shade, assembly
- **Dependency Management**: BOMs, exclusions, scopes
- **Profiles**: Environment-specific builds

### Gradle
- **Kotlin DSL**: build.gradle.kts best practices
- **Build Logic**: Precompiled script plugins
- **Dependency Management**: Catalogs, constraints, platforms
- **Task Configuration**: Lazy configuration
- **Build Cache**: Local and remote caching

### CI/CD Integration
- **GitHub Actions**: Java workflows, caching, matrix builds
- **GitLab CI**: Pipelines, artifacts, environments
- **Jenkins**: Declarative pipelines

## ReAct Pattern Workflow

```
1. REASON: Analyze build requirements
   - Identify project structure needs
   - Determine dependency requirements
   - Plan CI/CD integration

2. ACT: Configure build system
   - Create/modify build files
   - Set up plugins and tasks
   - Configure CI/CD pipelines

3. OBSERVE: Validate build
   - Run build and tests
   - Check for dependency issues
   - Verify CI/CD execution
```

## Maven Best Practices

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>my-app</artifactId>
    <version>1.0.0-SNAPSHOT</version>

    <properties>
        <java.version>21</java.version>
        <maven.compiler.source>${java.version}</maven.compiler.source>
        <maven.compiler.target>${java.version}</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <spring-boot.version>3.2.1</spring-boot.version>
    </properties>

    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-dependencies</artifactId>
                <version>${spring-boot.version}</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-enforcer-plugin</artifactId>
                <version>3.4.1</version>
                <executions>
                    <execution>
                        <id>enforce-versions</id>
                        <goals><goal>enforce</goal></goals>
                        <configuration>
                            <rules>
                                <requireMavenVersion>
                                    <version>3.8.0</version>
                                </requireMavenVersion>
                            </rules>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
</project>
```

## Gradle Best Practices

```kotlin
// build.gradle.kts
plugins {
    java
    id("org.springframework.boot") version "3.2.1"
    id("io.spring.dependency-management") vers

================================================
FILE: agents\06-java-persistence.md
================================================
---
name: 06-java-persistence
description: Persistence expert - JPA, Hibernate, database design, query optimization
model: sonnet
tools: Read, Write, Bash, Glob, Grep
sasmp_version: "1.3.0"
eqhm_enabled: true
skills:
  - java-fundamentals
  - java-concurrency
  - java-microservices
  - java-spring-boot
  - java-docker
  - java-performance
  - java-testing
  - java-maven-gradle
  - java-testing-advanced
  - java-jpa-hibernate
  - java-maven
  - java-gradle
triggers:
  - "java java"
  - "java"
  - "spring"
version: "3.0.0"

# Input/Output Schema
input_schema:
  type: object
  properties:
    task_type:
      type: string
      enum: [entity_design, query_optimization, migration, transaction_management, caching]
    database_type:
      type: string
      enum: [postgresql, mysql, oracle, h2, mongodb]
    requirements:
      type: string
  required: [task_type, requirements]

output_schema:
  type: object
  properties:
    entities:
      type: array
    repositories:
      type: array
    queries:
      type: array
    migrations:
      type: array
    performance_notes:
      type: array

# Cost Optimization
token_budget: 10000
max_iterations: 6
prefer_streaming: true
---

# 06 Java Persistence Agent

Expert agent for JPA, Hibernate, and database access patterns with performance optimization.

## Role & Responsibilities

**Primary Role**: Design and optimize data persistence layer

**Boundaries**:
- ✅ JPA entity design and mapping
- ✅ Hibernate configuration and tuning
- ✅ Repository pattern (Spring Data JPA)
- ✅ Query optimization (JPQL, Criteria, native SQL)
- ✅ Transaction management
- ✅ Database migration (Flyway, Liquibase)
- ✅ Caching strategies (L1, L2, query cache)
- ❌ Database administration/DBA tasks
- ❌ NoSQL specialized patterns

## Expertise Areas

### JPA Entity Design
- **Entity Mapping**: @Entity, @Table, @Column
- **Relationships**: @OneToMany, @ManyToOne, @ManyToMany
- **Inheritance**: SINGLE_TABLE, JOINED, TABLE_PER_CLASS
- **Lifecycle Callbacks**: @PrePersist, @PostLoad, @EntityListeners

### Hibernate Optimization
- **Fetching Strategies**: LAZY vs EAGER, @BatchSize, @Fetch
- **N+1 Prevention**: JOIN FETCH, EntityGraph, batch fetching
- **Batch Operations**: hibernate.jdbc.batch_size
- **Connection Pooling**: HikariCP configuration

### Query Strategies
- **JPQL**: Object-oriented queries
- **Criteria API**: Type-safe dynamic queries
- **Specifications**: Composable predicates
- **Projections**: DTOs, interfaces

## ReAct Pattern Workflow

```
1. REASON: Analyze data access requirements
   - Understand domain model
   - Identify query patterns
   - Plan caching strategy

2. ACT: Implement persistence layer
   - Design entities and relationships
   - Create repositories with optimized queries
   - Configure caching and transactions

3. OBSERVE: Validate performance
   - Enable SQL logging
   - Identify N+1 issues
   - Verify transaction boundaries
```

## Entity Design Patterns

```java
// Pattern: Proper bidirectional relationship
@Entity
@Table(name = "orders")
public class Order {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @OneToMany(mappedBy = "order", cascade = CascadeType.ALL, orphanRemoval = true)
    @BatchSize(size = 20)
    private List<OrderItem> items = new ArrayList<>();

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "customer_id", nullable = false)
    private Customer customer;

    @Version
    private Long version;  // Optimistic locking

    public void addItem(OrderItem item) {
        items.add(item);
        item.setOrder(this);
    }

    public void removeItem(OrderItem item) {
        items.remove(item);
        item.setOrder(null);
    }
}

// Pattern: Auditing
@MappedSuperclass
@EntityListeners(AuditingEntityListener.class)
public abstract class Auditable {

    @CreatedDate
    @Column(updatable = false)
    private Instant createdAt;

    @LastModifiedDate
    private Instant updatedAt;

    @CreatedBy
    @Column(updatable = false)
    private String createdBy;
}
```

## Query Optimization

```java
// ❌ N+1 Problem
@Query("SELECT o FROM Order o")
List<Order> findAllOrders();  // Each order.getItems() causes extra query

// ✅ Solution 1: JOIN FETCH
@Query("SELECT DISTINCT o FROM Order o JOIN FETCH o.items WHERE o.status = :status")
List<Order> findByStatusWithItems(@Param("status") Status status);

// ✅ Solution 2: EntityGraph
@EntityGraph(attributePaths = {"items", "customer"})
@Query("SELECT o FROM Order o WHERE o.id = :id")
Optional<Order> findByIdWithDetails(@Param("id") Long id);

// ✅ Solution 3: DTO Projection
public interface OrderSummary {
    Long getId();
    String getStatus();
    @Value("#{target.customer.name}")
    String getCustomerName();
}
```

## Configuration

```yaml
spring:
  jpa:
    open-in-view: false  # Critical for production
    properties:
      hibernate:
        jdbc.batch_size: 50
        order_inserts: true
        order_updates: true
        default_batch_fetch_si

================================================
FILE: agents\07-java-microservices.md
================================================
---
name: 07-java-microservices
description: Microservices expert - Spring Cloud, distributed systems, service mesh, event-driven
model: sonnet
tools: Read, Write, Bash, Glob, Grep
sasmp_version: "1.3.0"
eqhm_enabled: true
skills:
  - java-fundamentals
  - java-concurrency
  - java-microservices
  - java-spring-boot
  - java-docker
  - java-performance
  - java-testing
  - java-maven-gradle
  - java-testing-advanced
  - java-jpa-hibernate
  - java-maven
  - java-gradle
triggers:
  - "java java"
  - "java"
  - "spring"
version: "3.0.0"

# Input/Output Schema
input_schema:
  type: object
  properties:
    task_type:
      type: string
      enum: [service_design, api_gateway, service_discovery, messaging, resilience, observability]
    architecture_pattern:
      type: string
      enum: [saga, cqrs, event_sourcing, choreography, orchestration]
    requirements:
      type: string
  required: [task_type, requirements]

output_schema:
  type: object
  properties:
    services:
      type: array
    api_contracts:
      type: array
    infrastructure:
      type: object
    diagrams:
      type: array

# Cost Optimization
token_budget: 12000
max_iterations: 8
prefer_streaming: true
---

# 07 Java Microservices Agent

Expert agent for distributed systems with Spring Cloud, messaging, and resilience patterns.

## Role & Responsibilities

**Primary Role**: Design and implement production microservices architectures

**Boundaries**:
- ✅ Spring Cloud ecosystem (Gateway, Config, Eureka)
- ✅ Service communication (REST, gRPC, messaging)
- ✅ Event-driven architecture (Kafka, RabbitMQ)
- ✅ Resilience patterns (Circuit Breaker, Retry)
- ✅ Distributed tracing and observability
- ✅ API Gateway and routing
- ❌ Kubernetes administration (delegate to devops)
- ❌ Database sharding strategies

## Expertise Areas

### Service Architecture
- **Domain-Driven Design**: Bounded contexts, aggregates
- **Service Decomposition**: Strangler fig pattern
- **API Design**: REST maturity levels, HATEOAS
- **Contract First**: OpenAPI, AsyncAPI

### Spring Cloud
- **Config Server**: Centralized configuration
- **Service Discovery**: Eureka, Consul
- **API Gateway**: Spring Cloud Gateway, filters
- **Load Balancing**: Spring Cloud LoadBalancer
- **Distributed Tracing**: Micrometer, Zipkin

### Messaging & Events
- **Apache Kafka**: Producers, consumers, streams
- **RabbitMQ**: Queues, exchanges, dead letter
- **Spring Cloud Stream**: Binder abstraction
- **Saga Pattern**: Choreography vs orchestration

### Resilience
- **Circuit Breaker**: Resilience4j configuration
- **Retry**: Exponential backoff, jitter
- **Bulkhead**: Thread pool isolation
- **Rate Limiting**: Request throttling

## ReAct Pattern Workflow

```
1. REASON: Analyze distributed system requirements
   - Identify service boundaries
   - Determine communication patterns
   - Plan failure modes and recovery

2. ACT: Implement microservices
   - Create service components
   - Configure resilience patterns
   - Set up messaging infrastructure

3. OBSERVE: Validate distributed behavior
   - Trace requests across services
   - Test failure scenarios
   - Monitor service health
```

## Distributed Patterns

```java
// Pattern 1: Saga with Choreography
@Component
public class OrderSagaListener {

    @KafkaListener(topics = "order.created")
    public void handleOrderCreated(OrderCreatedEvent event) {
        inventoryService.reserve(event.getItems());
    }

    @KafkaListener(topics = "inventory.reserved")
    public void handleInventoryReserved(InventoryReservedEvent event) {
        paymentService.charge(event.getOrderId(), event.getAmount());
    }

    @KafkaListener(topics = "payment.failed")
    public void handlePaymentFailed(PaymentFailedEvent event) {
        // Compensating transaction
        inventoryService.release(event.getOrderId());
        orderService.cancel(event.getOrderId());
    }
}

// Pattern 2: Circuit Breaker
@Configuration
public class ResilienceConfig {

    @Bean
    public Customizer<Resilience4JCircuitBreakerFactory> circuitBreakerCustomizer() {
        return factory -> factory.configureDefault(id ->
            new Resilience4JConfigBuilder(id)
                .circuitBreakerConfig(CircuitBreakerConfig.custom()
                    .failureRateThreshold(50)
                    .waitDurationInOpenState(Duration.ofSeconds(30))
                    .slidingWindowSize(10)
                    .build())
                .build());
    }
}

// Pattern 3: API Gateway
@Configuration
public class GatewayConfig {

    @Bean
    public RouteLocator customRouteLocator(RouteLocatorBuilder builder) {
        return builder.routes()
            .route("order-service", r -> r
                .path("/api/orders/**")
                .filters(f -> f
                    .stripPrefix(1)
                    .circuitBreaker(c -> c.setName("order-cb"))
                    .retry(retryConfig -> retryConfig.setRetries(3)))
                .uri("lb://order-service"))
            .bu

================================================
FILE: agents\08-java-devops.md
================================================
---
name: 08-java-devops
description: DevOps expert - Docker, Kubernetes, CI/CD, deployment, monitoring
model: sonnet
tools: Read, Write, Bash, Glob, Grep
sasmp_version: "1.3.0"
eqhm_enabled: true
skills:
  - java-fundamentals
  - java-concurrency
  - java-microservices
  - java-spring-boot
  - java-docker
  - java-performance
  - java-testing
  - java-maven-gradle
  - java-testing-advanced
  - java-jpa-hibernate
  - java-maven
  - java-gradle
triggers:
  - "java java"
  - "java"
  - "spring"
  - "java devops"
version: "3.0.0"

# Input/Output Schema
input_schema:
  type: object
  properties:
    task_type:
      type: string
      enum: [containerization, orchestration, ci_cd, monitoring, deployment]
    environment:
      type: string
      enum: [development, staging, production]
    platform:
      type: string
      enum: [kubernetes, docker_compose, ecs, cloud_run]
  required: [task_type]

output_schema:
  type: object
  properties:
    dockerfiles:
      type: array
    k8s_manifests:
      type: array
    pipelines:
      type: array
    monitoring_config:
      type: object

# Cost Optimization
token_budget: 10000
max_iterations: 6
prefer_streaming: true
---

# 08 Java DevOps Agent

Expert agent for containerization, deployment, CI/CD, and production operations.

## Role & Responsibilities

**Primary Role**: Deploy and operate Java applications in production

**Boundaries**:
- ✅ Docker containerization for Java
- ✅ Kubernetes deployment and operations
- ✅ CI/CD pipeline design
- ✅ Monitoring and alerting (Prometheus, Grafana)
- ✅ Log aggregation
- ✅ JVM tuning for containers
- ❌ Database administration
- ❌ Network security/firewall rules

## Expertise Areas

### Containerization
- **Dockerfile Optimization**: Multi-stage builds, layer caching
- **JVM in Containers**: Memory settings, CPU limits
- **Base Images**: Eclipse Temurin, Distroless, Alpine
- **Security**: Non-root users, vulnerability scanning

### Kubernetes
- **Workloads**: Deployments, StatefulSets, Jobs
- **Configuration**: ConfigMaps, Secrets, Kustomize
- **Networking**: Services, Ingress, NetworkPolicies
- **Scaling**: HPA, VPA, KEDA
- **Observability**: Probes, metrics, logging

### CI/CD
- **GitHub Actions**: Workflows, caching, matrix builds
- **GitLab CI**: Pipelines, environments
- **ArgoCD**: GitOps deployment
- **Security Scanning**: Trivy, Snyk

### Monitoring
- **Metrics**: Prometheus, Micrometer
- **Dashboards**: Grafana, key JVM metrics
- **Alerting**: AlertManager
- **Logging**: Structured logging, ELK

## ReAct Pattern Workflow

```
1. REASON: Analyze deployment requirements
   - Understand application architecture
   - Determine scaling needs
   - Plan monitoring strategy

2. ACT: Implement DevOps artifacts
   - Create optimized Dockerfiles
   - Configure Kubernetes resources
   - Set up CI/CD pipelines

3. OBSERVE: Validate deployment
   - Verify container health
   - Check metrics and logs
   - Test scaling behavior
```

## Docker Best Practices

```dockerfile
# Multi-stage optimized Dockerfile
FROM eclipse-temurin:21-jdk-alpine AS builder

WORKDIR /app

COPY pom.xml .
COPY .mvn .mvn
RUN mvn dependency:go-offline -B

COPY src ./src
RUN mvn package -DskipTests && \
    java -Djarmode=layertools -jar target/*.jar extract

# Runtime stage
FROM eclipse-temurin:21-jre-alpine

RUN addgroup -S app && adduser -S app -G app
USER app

WORKDIR /app

COPY --from=builder /app/dependencies/ ./
COPY --from=builder /app/spring-boot-loader/ ./
COPY --from=builder /app/snapshot-dependencies/ ./
COPY --from=builder /app/application/ ./

ENV JAVA_OPTS="-XX:+UseContainerSupport \
    -XX:MaxRAMPercentage=75.0 \
    -XX:+ExitOnOutOfMemoryError"

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=3s --start-period=30s \
    CMD wget -qO- http://localhost:8080/actuator/health/liveness || exit 1

ENTRYPOINT ["sh", "-c", "java $JAVA_OPTS org.springframework.boot.loader.launch.JarLauncher"]
```

## Kubernetes Manifests

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: order-service
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 1
      maxSurge: 1
  template:
    spec:
      securityContext:
        runAsNonRoot: true
        runAsUser: 1000
      containers:
      - name: order-service
        image: order-service:v1.0.0
        ports:
        - containerPort: 8080
        resources:
          requests:
            memory: "512Mi"
            cpu: "250m"
          limits:
            memory: "1Gi"
            cpu: "1000m"
        startupProbe:
          httpGet:
            path: /actuator/health/liveness
            port: 8080
          initialDelaySeconds: 15
          failureThreshold: 30
        livenessProbe:
          httpGet:
            path: /actuator/health/liveness
            port: 8080
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /actuator/health/readiness
            port: 8080
          periodSeconds: 5
        lifecycle:
  

================================================
FILE: commands\java-build.md
================================================
---
name: java-build
description: Build Java project with Maven or Gradle - compile, test, package
allowed-tools: Bash, Read
version: "3.0.0"

# Input Validation
parameters:
  skip_tests:
    type: boolean
    default: false
    description: Skip test execution
  goal:
    type: string
    enum: [compile, test, package, install, deploy]
    default: package
  profile:
    type: string
    description: Build profile to activate
---

# Java Build Command

Build the Java project and run tests.

## What This Command Does

1. **Detect Build Tool** - Find Maven or Gradle wrapper
2. **Clean Build** - Remove previous artifacts
3. **Compile** - Compile source code
4. **Test** - Run unit tests
5. **Package** - Create JAR/WAR
6. **Report** - Show build summary

## Usage

```bash
/java-build                    # Build and test
/java-build --skip-tests       # Build without tests
/java-build --package          # Create JAR/WAR
/java-build --install          # Install to local repo
/java-build --profile prod     # Use production profile
```

## Build Goals

| Goal | Maven | Gradle | Description |
|------|-------|--------|-------------|
| compile | compile | classes | Compile sources |
| test | test | test | Run tests |
| package | package | jar | Create artifact |
| install | install | publishToMavenLocal | Install locally |

## Options

| Option | Description |
|--------|-------------|
| `--skip-tests` | Build without tests |
| `--package` | Create JAR/WAR |
| `--install` | Install to local repository |
| `--profile <name>` | Activate build profile |
| `--debug` | Enable debug output |

## Output Example

```
=== Java Build ===

[INFO] Building my-app 1.0.0-SNAPSHOT
[INFO] Compiling 42 source files
[INFO] Running 28 tests

Tests:
  ✓ 28 tests passed
  ✗ 0 tests failed
  ⊘ 2 tests skipped

[INFO] Building jar: target/my-app-1.0.0-SNAPSHOT.jar

BUILD SUCCESS (32s)
```

## Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| Compilation error | Syntax error | Check error line |
| Test failure | Assertion failed | Review test output |
| Dependency not found | Missing repo | Check repositories |
| Out of memory | Heap too small | Set MAVEN_OPTS |

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Build success |
| 1 | Compilation failed |
| 2 | Tests failed |

## Related Commands

- `/java-check` - Verify environment
- `/java-debug` - Debug issues


================================================
FILE: commands\java-check.md
================================================
---
name: java-check
description: Check Java environment - JDK, Maven, Gradle versions and configuration
allowed-tools: Bash, Read
version: "3.0.0"

# Input Validation
parameters:
  verbose:
    type: boolean
    default: false
    description: Show detailed output
---

# Java Check Command

Verify Java development environment is properly configured.

## What This Command Does

1. **JDK Check** - Verify Java version (recommend 17 or 21)
2. **JAVA_HOME** - Validate environment variable
3. **Maven Check** - Verify installation and version
4. **Gradle Check** - Verify installation and version
5. **Environment Summary** - Display configuration status

## Usage

```bash
/java-check            # Quick check
/java-check --verbose  # Detailed output
```

## Expected Output

```
=== Java Environment Check ===

JDK:
  ✓ Version: 21.0.1
  ✓ JAVA_HOME: /usr/lib/jvm/java-21
  ✓ javac available

Build Tools:
  ✓ Maven: 3.9.6
  ✓ Gradle: 8.5

Status: Environment Ready
```

## Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| java not found | Not in PATH | Add JAVA_HOME/bin to PATH |
| JAVA_HOME not set | Missing variable | Export JAVA_HOME |
| Maven not found | Not installed | Install via sdkman or apt |
| Wrong Java version | Multiple JDKs | Use update-alternatives |

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Environment OK |
| 1 | Java not found |
| 2 | Build tools missing |

## Related Commands

- `/java-new` - Create new project
- `/java-build` - Build project


================================================
FILE: commands\java-debug.md
================================================
---
name: java-debug
description: Debug Java applications - analyze errors, memory issues, performance
allowed-tools: Bash, Read, WebSearch
version: "3.0.0"

# Input Validation
parameters:
  error_type:
    type: string
    enum: [OutOfMemoryError, ClassNotFoundException, NoSuchMethodError, StackOverflowError, NullPointerException, all]
    description: Specific error type to debug
  pid:
    type: integer
    description: Process ID for live debugging
---

# Java Debug Command

Diagnose and troubleshoot Java application issues.

## What This Command Does

1. **Error Analysis** - Parse and explain stack traces
2. **Common Errors** - Identify known issue patterns
3. **JVM Diagnostics** - Check memory, threads, GC
4. **Solutions** - Provide targeted fixes
5. **Prevention** - Best practices to avoid issues

## Usage

```bash
/java-debug                       # Analyze current error
/java-debug OutOfMemoryError      # Debug OOM specifically
/java-debug --pid 12345           # Debug running process
/java-debug ClassNotFoundException # Debug classpath issues
```

## Common Issues

### OutOfMemoryError

**Causes:**
- Heap too small
- Memory leak
- Large objects

**Diagnosis:**
```bash
# Heap dump
jmap -dump:format=b,file=heap.hprof <pid>

# GC logs
-Xlog:gc*:file=gc.log

# Heap settings
java -Xms512m -Xmx2g -XX:+HeapDumpOnOutOfMemoryError
```

### ClassNotFoundException

**Causes:**
- Missing dependency
- Wrong classpath
- Shading issues

**Diagnosis:**
```bash
# Check classpath
java -cp . -verbose:class MyApp

# Dependency tree
mvn dependency:tree
gradle dependencies
```

### NoSuchMethodError

**Causes:**
- Version conflict
- Incompatible dependency
- Classpath order

**Diagnosis:**
```bash
# Find duplicates
mvn dependency:tree -Dincludes=groupId:artifactId
gradle dependencyInsight --dependency name
```

### StackOverflowError

**Causes:**
- Infinite recursion
- Deep call stack
- Circular references

**Fix:**
- Add base case to recursion
- Use iteration instead
- Increase stack size: `-Xss2m`

### NullPointerException

**Causes:**
- Null reference access
- Missing initialization
- Bad API return

**Fix:**
- Use Optional
- Add null checks
- Use @NonNull annotations

## JVM Diagnostic Commands

```bash
# Thread dump
jstack -l <pid>

# Heap info
jmap -heap <pid>

# GC stats
jstat -gcutil <pid> 1000

# Flight recording
jcmd <pid> JFR.start duration=60s filename=recording.jfr

# Full diagnostics
jcmd <pid> VM.info
```

## Troubleshooting Decision Tree

```
Error occurred?
├── OutOfMemoryError
│   ├── Heap? → Increase -Xmx, check leaks
│   └── Metaspace? → Increase -XX:MaxMetaspaceSize
├── ClassNotFoundException
│   ├── At runtime? → Check classpath
│   └── At startup? → Missing dependency
├── NoSuchMethodError
│   └── Check for version conflicts
└── Performance issue
    ├── High CPU? → Profile with async-profiler
    └── Slow response? → Check GC pauses
```

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Diagnosis complete |
| 1 | Process not found |
| 2 | Insufficient permissions |

## Related Commands

- `/java-build` - Build project
- `/java-check` - Check environment


================================================
FILE: commands\java-new.md
================================================
---
name: java-new
description: Create a new Java project with Maven or Gradle
allowed-tools: Bash, Read, Write
version: "3.0.0"

# Input Validation
parameters:
  project_name:
    type: string
    required: true
    pattern: "^[a-z][a-z0-9-]*$"
    description: Project name (lowercase, hyphens allowed)
  build_tool:
    type: string
    enum: [maven, gradle]
    default: maven
  framework:
    type: string
    enum: [plain, spring-boot, quarkus, library]
    default: plain
  java_version:
    type: string
    default: "21"
    enum: ["17", "21"]
---

# Java New Command

Create a new Java project with proper structure and dependencies.

## What This Command Does

1. **Project Type Selection** - Choose Maven or Gradle
2. **Framework Selection** - Spring Boot, Quarkus, or plain Java
3. **Directory Structure** - Create standard Java layout
4. **Build Configuration** - Generate pom.xml or build.gradle.kts
5. **Git Init** - Initialize git repository with .gitignore

## Usage

```bash
/java-new my-app                        # Plain Maven project
/java-new my-app --spring-boot          # Spring Boot with Maven
/java-new my-app --gradle --spring-boot # Spring Boot with Gradle
/java-new my-lib --library              # Library project
```

## Project Types

### Plain Java
- Basic Maven/Gradle project
- JUnit 5 for testing
- No framework dependencies

### Spring Boot
- Spring Boot 3.x starter
- Web, actuator included
- Application class generated

### Library
- No main class
- Configured for publishing
- Test dependencies only

### Multi-module (advanced)
- Parent POM with modules
- Shared dependencies
- Separate subprojects

## Generated Structure

```
my-app/
├── pom.xml (or build.gradle.kts)
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/example/myapp/
│   │   │       └── Application.java
│   │   └── resources/
│   │       └── application.yml
│   └── test/
│       └── java/
│           └── com/example/myapp/
│               └── ApplicationTest.java
├── .gitignore
└── README.md
```

## Options

| Option | Description |
|--------|-------------|
| `--maven` | Use Maven (default) |
| `--gradle` | Use Gradle with Kotlin DSL |
| `--spring-boot` | Include Spring Boot starter |
| `--library` | Create library project |
| `--java 17` | Specify Java version |

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Project created |
| 1 | Invalid project name |
| 2 | Directory exists |

## Related Commands

- `/java-check` - Verify environment
- `/java-build` - Build project


================================================
FILE: hooks\hooks.json
================================================
{
  "hooks": {}
}


================================================
FILE: skills\java-concurrency\SKILL.md
================================================
---
name: java-concurrency
description: Master Java concurrency - threads, executors, locks, CompletableFuture, virtual threads
sasmp_version: "1.3.0"
version: "3.0.0"
bonded_agent: 02-java-advanced
bond_type: PRIMARY_BOND
allowed-tools: Read, Write, Bash, Glob, Grep

# Parameter Validation
parameters:
  concurrency_model:
    type: string
    enum: [threads, executors, virtual_threads, reactive]
  java_version:
    type: string
    default: "21"
---

# Java Concurrency Skill

Master Java concurrency patterns for thread-safe applications.

## Overview

This skill covers concurrency from basic threads to virtual threads (Java 21+), including thread pools, synchronization, and CompletableFuture.

## When to Use This Skill

Use when you need to:
- Write thread-safe code
- Implement parallel processing
- Use async programming patterns
- Tune thread pools
- Debug concurrency issues

## Topics Covered

### Thread Management
- Thread lifecycle and states
- Daemon vs user threads
- Interrupt handling

### Synchronization
- synchronized, volatile
- Lock interfaces (ReentrantLock)
- Atomic operations

### Executors
- ThreadPoolExecutor configuration
- ForkJoinPool
- Virtual Threads (Java 21+)

### CompletableFuture
- Async execution
- Chaining and composition
- Exception handling

## Quick Reference

```java
// Virtual Threads (Java 21+)
try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
    IntStream.range(0, 10_000).forEach(i ->
        executor.submit(() -> processRequest(i)));
}

// CompletableFuture composition
CompletableFuture<Result> result = fetchUser(id)
    .thenCompose(user -> fetchOrders(user.id()))
    .thenApply(orders -> processOrders(orders))
    .exceptionally(ex -> handleError(ex))
    .orTimeout(5, TimeUnit.SECONDS);

// Thread pool configuration
ThreadPoolExecutor executor = new ThreadPoolExecutor(
    10, 50, 60L, TimeUnit.SECONDS,
    new ArrayBlockingQueue<>(1000),
    new ThreadPoolExecutor.CallerRunsPolicy()
);

// Lock with timeout
ReentrantLock lock = new ReentrantLock();
if (lock.tryLock(1, TimeUnit.SECONDS)) {
    try {
        // critical section
    } finally {
        lock.unlock();
    }
}
```

## Thread Pool Sizing

| Workload | Formula | Example |
|----------|---------|---------|
| CPU-bound | cores | 8 threads |
| I/O-bound | cores * (1 + wait/compute) | 80 threads |

## Troubleshooting

| Problem | Cause | Solution |
|---------|-------|----------|
| Deadlock | Circular lock | Lock ordering, tryLock |
| Race condition | Missing sync | Add locks/atomics |
| Thread starvation | Unfair scheduling | Fair locks |

### Debug Commands
```bash
jstack -l <pid> > threaddump.txt
jcmd <pid> Thread.print
```

## Usage

```
Skill("java-concurrency")
```


================================================
FILE: skills\java-concurrency\assets\schema.json
================================================
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "java-concurrency Configuration Schema",
  "type": "object",
  "properties": {
    "skill": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "version": {
          "type": "string",
          "pattern": "^\\d+\\.\\d+\\.\\d+$"
        },
        "category": {
          "type": "string",
          "enum": [
            "api",
            "testing",
            "devops",
            "security",
            "database",
            "frontend",
            "algorithms",
            "machine-learning",
            "cloud",
            "containers",
            "general"
          ]
        }
      },
      "required": [
        "name",
        "version"
      ]
    },
    "settings": {
      "type": "object",
      "properties": {
        "enabled": {
          "type": "boolean",
          "default": true
        },
        "log_level": {
          "type": "string",
          "enum": [
            "debug",
            "info",
            "warn",
            "error"
          ]
        }
      }
    }
  },
  "required": [
    "skill"
  ]
}

================================================
FILE: skills\java-concurrency\references\GUIDE.md
================================================
# Java Concurrency Guide

## Overview

This guide provides comprehensive documentation for the **java-concurrency** skill in the custom-plugin-java plugin.

## Category: General

## Quick Start

### Prerequisites

- Familiarity with general concepts
- Development environment set up
- Plugin installed and configured

### Basic Usage

```bash
# Invoke the skill
claude "java-concurrency - [your task description]"

# Example
claude "java-concurrency - analyze the current implementation"
```

## Core Concepts

### Key Principles

1. **Consistency** - Follow established patterns
2. **Clarity** - Write readable, maintainable code
3. **Quality** - Validate before deployment

### Best Practices

- Always validate input data
- Handle edge cases explicitly
- Document your decisions
- Write tests for critical paths

## Common Tasks

### Task 1: Basic Implementation

```python
# Example implementation pattern
def implement_java_concurrency(input_data):
    """
    Implement java-concurrency functionality.

    Args:
        input_data: Input to process

    Returns:
        Processed result
    """
    # Validate input
    if not input_data:
        raise ValueError("Input required")

    # Process
    result = process(input_data)

    # Return
    return result
```

### Task 2: Advanced Usage

For advanced scenarios, consider:

- Configuration customization via `assets/config.yaml`
- Validation using `scripts/validate.py`
- Integration with other skills

## Troubleshooting

### Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Skill not found | Not installed | Run plugin sync |
| Validation fails | Invalid config | Check config.yaml |
| Unexpected output | Missing context | Provide more details |

## Related Resources

- SKILL.md - Skill specification
- config.yaml - Configuration options
- validate.py - Validation script

---

*Last updated: 2025-12-30*


================================================
FILE: skills\java-concurrency\references\PATTERNS.md
================================================
# Java Concurrency Patterns

## Design Patterns

### Pattern 1: Input Validation

Always validate input before processing:

```python
def validate_input(data):
    if data is None:
        raise ValueError("Data cannot be None")
    if not isinstance(data, dict):
        raise TypeError("Data must be a dictionary")
    return True
```

### Pattern 2: Error Handling

Use consistent error handling:

```python
try:
    result = risky_operation()
except SpecificError as e:
    logger.error(f"Operation failed: {e}")
    handle_error(e)
except Exception as e:
    logger.exception("Unexpected error")
    raise
```

### Pattern 3: Configuration Loading

Load and validate configuration:

```python
import yaml

def load_config(config_path):
    with open(config_path) as f:
        config = yaml.safe_load(f)
    validate_config(config)
    return config
```

## Anti-Patterns to Avoid

### ❌ Don't: Swallow Exceptions

```python
# BAD
try:
    do_something()
except:
    pass
```

### ✅ Do: Handle Explicitly

```python
# GOOD
try:
    do_something()
except SpecificError as e:
    logger.warning(f"Expected error: {e}")
    return default_value
```

## Category-Specific Patterns: General

### Recommended Approach

1. Start with the simplest implementation
2. Add complexity only when needed
3. Test each addition
4. Document decisions

### Common Integration Points

- Configuration: `assets/config.yaml`
- Validation: `scripts/validate.py`
- Documentation: `references/GUIDE.md`

---

*Pattern library for java-concurrency skill*


================================================
FILE: skills\java-concurrency\scripts\validate.py
================================================
#!/usr/bin/env python3
"""
Validation script for java-concurrency skill.
Category: general
"""

import os
import sys
import yaml
import json
from pathlib import Path


def validate_config(config_path: str) -> dict:
    """
    Validate skill configuration file.

    Args:
        config_path: Path to config.yaml

    Returns:
        dict: Validation result with 'valid' and 'errors' keys
    """
    errors = []

    if not os.path.exists(config_path):
        return {"valid": False, "errors": ["Config file not found"]}

    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
    except yaml.YAMLError as e:
        return {"valid": False, "errors": [f"YAML parse error: {e}"]}

    # Validate required fields
    if 'skill' not in config:
        errors.append("Missing 'skill' section")
    else:
        if 'name' not in config['skill']:
            errors.append("Missing skill.name")
        if 'version' not in config['skill']:
            errors.append("Missing skill.version")

    # Validate settings
    if 'settings' in config:
        settings = config['settings']
        if 'log_level' in settings:
            valid_levels = ['debug', 'info', 'warn', 'error']
            if settings['log_level'] not in valid_levels:
                errors.append(f"Invalid log_level: {settings['log_level']}")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "config": config if not errors else None
    }


def validate_skill_structure(skill_path: str) -> dict:
    """
    Validate skill directory structure.

    Args:
        skill_path: Path to skill directory

    Returns:
        dict: Structure validation result
    """
    required_dirs = ['assets', 'scripts', 'references']
    required_files = ['SKILL.md']

    errors = []

    # Check required files
    for file in required_files:
        if not os.path.exists(os.path.join(skill_path, file)):
            errors.append(f"Missing required file: {file}")

    # Check required directories
    for dir in required_dirs:
        dir_path = os.path.join(skill_path, dir)
        if not os.path.isdir(dir_path):
            errors.append(f"Missing required directory: {dir}/")
        else:
            # Check for real content (not just .gitkeep)
            files = [f for f in os.listdir(dir_path) if f != '.gitkeep']
            if not files:
                errors.append(f"Directory {dir}/ has no real content")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "skill_name": os.path.basename(skill_path)
    }


def main():
    """Main validation entry point."""
    skill_path = Path(__file__).parent.parent

    print(f"Validating java-concurrency skill...")
    print(f"Path: {skill_path}")

    # Validate structure
    structure_result = validate_skill_structure(str(skill_path))
    print(f"\nStructure validation: {'PASS' if structure_result['valid'] else 'FAIL'}")
    if structure_result['errors']:
        for error in structure_result['errors']:
            print(f"  - {error}")

    # Validate config
    config_path = skill_path / 'assets' / 'config.yaml'
    if config_path.exists():
        config_result = validate_config(str(config_path))
        print(f"\nConfig validation: {'PASS' if config_result['valid'] else 'FAIL'}")
        if config_result['errors']:
            for error in config_result['errors']:
                print(f"  - {error}")
    else:
        print("\nConfig validation: SKIPPED (no config.yaml)")

    # Summary
    all_valid = structure_result['valid']
    print(f"\n==================================================")
    print(f"Overall: {'VALID' if all_valid else 'INVALID'}")

    return 0 if all_valid else 1


if __name__ == "__main__":
    sys.exit(main())


================================================
FILE: skills\java-docker\SKILL.md
================================================
---
name: java-docker
description: Containerize Java applications - Dockerfile optimization, JVM settings, security
sasmp_version: "1.3.0"
version: "3.0.0"
bonded_agent: 08-java-devops
bond_type: PRIMARY_BOND
allowed-tools: Read, Write, Bash, Glob, Grep

# Parameter Validation
parameters:
  base_image:
    type: string
    enum: [temurin, distroless, alpine]
    description: Base image type
  java_version:
    type: string
    default: "21"
    description: Java version
---

# Java Docker Skill

Containerize Java applications with optimized Dockerfiles and JVM settings.

## Overview

This skill covers Docker best practices for Java including multi-stage builds, JVM container settings, security hardening, and layer optimization.

## When to Use This Skill

Use when you need to:
- Create optimized Java Dockerfiles
- Configure JVM for containers
- Implement security best practices
- Reduce image size
- Set up health checks

## Topics Covered

### Dockerfile Optimization
- Multi-stage builds
- Layer caching strategy
- Spring Boot layered JARs
- Dependency caching

### JVM Container Settings
- UseContainerSupport
- MaxRAMPercentage
- GC selection
- Exit on OOM

### Security
- Non-root users
- Read-only filesystem
- Vulnerability scanning
- Secrets handling

## Quick Reference

```dockerfile
# Multi-stage optimized Dockerfile
FROM eclipse-temurin:21-jdk-alpine AS builder

WORKDIR /app

# Cache dependencies
COPY pom.xml .
COPY .mvn .mvn
RUN mvn dependency:go-offline -B

# Build and extract layers
COPY src ./src
RUN mvn package -DskipTests && \
    java -Djarmode=layertools -jar target/*.jar extract

# Runtime stage
FROM eclipse-temurin:21-jre-alpine

# Security: non-root user
RUN addgroup -S app && adduser -S app -G app
USER app

WORKDIR /app

# Copy layers in order of change frequency
COPY --from=builder /app/dependencies/ ./
COPY --from=builder /app/spring-boot-loader/ ./
COPY --from=builder /app/snapshot-dependencies/ ./
COPY --from=builder /app/application/ ./

# JVM container settings
ENV JAVA_OPTS="-XX:+UseContainerSupport \
    -XX:MaxRAMPercentage=75.0 \
    -XX:+ExitOnOutOfMemoryError \
    -XX:+UseG1GC"

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=3s --start-period=30s \
    CMD wget -qO- http://localhost:8080/actuator/health/liveness || exit 1

ENTRYPOINT ["sh", "-c", "java $JAVA_OPTS org.springframework.boot.loader.launch.JarLauncher"]
```

## JVM Container Flags

```bash
# Recommended production settings
JAVA_OPTS="
  -XX:+UseContainerSupport
  -XX:MaxRAMPercentage=75.0
  -XX:InitialRAMPercentage=50.0
  -XX:+ExitOnOutOfMemoryError
  -XX:+HeapDumpOnOutOfMemoryError
  -XX:HeapDumpPath=/tmp/heapdump.hprof
  -XX:+UseG1GC
  -Djava.security.egd=file:/dev/./urandom
"
```

## Base Image Comparison

| Image | Size | Security | Use Case |
|-------|------|----------|----------|
| temurin:21-jre | ~200MB | Good | General use |
| temurin:21-jre-alpine | ~100MB | Good | Size-optimized |
| distroless/java21 | ~80MB | Best | Production |

## Security Best Practices

```dockerfile
# Non-root user
RUN addgroup -S app && adduser -S app -G app
USER app

# Read-only filesystem
# (Configure at runtime with --read-only)

# No shell access with distroless
FROM gcr.io/distroless/java21-debian12

# Health check
HEALTHCHECK --interval=30s --timeout=3s \
    CMD wget -qO- localhost:8080/actuator/health || exit 1
```

## Troubleshooting

### Common Issues

| Problem | Cause | Solution |
|---------|-------|----------|
| OOMKilled | Heap > limit | Set MaxRAMPercentage |
| Slow startup | Large image | Multi-stage build |
| Permission denied | Root required | Fix file permissions |
| No memory info | Old JVM | Update to Java 11+ |

### Debug Checklist
```
□ Check container memory limits
□ Verify JVM sees container limits
□ Review health check configuration
□ Scan image for vulnerabilities
□ Test with resource constraints
```

## Usage

```
Skill("java-docker")
```

## Related Skills
- `java-maven-gradle` - Build integration
- `java-microservices` - K8s deployment


================================================
FILE: skills\java-docker\assets\Dockerfile.java
================================================
FROM eclipse-temurin:21-jdk AS builder
WORKDIR /app
COPY . .
RUN ./mvnw package -DskipTests

FROM eclipse-temurin:21-jre
COPY --from=builder /app/target/*.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]


================================================
FILE: skills\java-docker\assets\schema.json
================================================
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "java-docker Configuration Schema",
  "type": "object",
  "properties": {
    "skill": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "version": {
          "type": "string",
          "pattern": "^\\d+\\.\\d+\\.\\d+$"
        },
        "category": {
          "type": "string",
          "enum": [
            "api",
            "testing",
            "devops",
            "security",
            "database",
            "frontend",
            "algorithms",
            "machine-learning",
            "cloud",
            "containers",
            "general"
          ]
        }
      },
      "required": [
        "name",
        "version"
      ]
    },
    "settings": {
      "type": "object",
      "properties": {
        "enabled": {
          "type": "boolean",
          "default": true
        },
        "log_level": {
          "type": "string",
          "enum": [
            "debug",
            "info",
            "warn",
            "error"
          ]
        }
      }
    }
  },
  "required": [
    "skill"
  ]
}

================================================
FILE: skills\java-docker\references\GUIDE.md
================================================
# Java Docker Guide

## Overview

This guide provides comprehensive documentation for the **java-docker** skill in the custom-plugin-java plugin.

## Category: Containers

## Quick Start

### Prerequisites

- Familiarity with containers concepts
- Development environment set up
- Plugin installed and configured

### Basic Usage

```bash
# Invoke the skill
claude "java-docker - [your task description]"

# Example
claude "java-docker - analyze the current implementation"
```

## Core Concepts

### Key Principles

1. **Consistency** - Follow established patterns
2. **Clarity** - Write readable, maintainable code
3. **Quality** - Validate before deployment

### Best Practices

- Always validate input data
- Handle edge cases explicitly
- Document your decisions
- Write tests for critical paths

## Common Tasks

### Task 1: Basic Implementation

```python
# Example implementation pattern
def implement_java_docker(input_data):
    """
    Implement java-docker functionality.

    Args:
        input_data: Input to process

    Returns:
        Processed result
    """
    # Validate input
    if not input_data:
        raise ValueError("Input required")

    # Process
    result = process(input_data)

    # Return
    return result
```

### Task 2: Advanced Usage

For advanced scenarios, consider:

- Configuration customization via `assets/config.yaml`
- Validation using `scripts/validate.py`
- Integration with other skills

## Troubleshooting

### Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Skill not found | Not installed | Run plugin sync |
| Validation fails | Invalid config | Check config.yaml |
| Unexpected output | Missing context | Provide more details |

## Related Resources

- SKILL.md - Skill specification
- config.yaml - Configuration options
- validate.py - Validation script

---

*Last updated: 2025-12-30*


================================================
FILE: skills\java-docker\references\PATTERNS.md
================================================
# Java Docker Patterns

## Design Patterns

### Pattern 1: Input Validation

Always validate input before processing:

```python
def validate_input(data):
    if data is None:
        raise ValueError("Data cannot be None")
    if not isinstance(data, dict):
        raise TypeError("Data must be a dictionary")
    return True
```

### Pattern 2: Error Handling

Use consistent error handling:

```python
try:
    result = risky_operation()
except SpecificError as e:
    logger.error(f"Operation failed: {e}")
    handle_error(e)
except Exception as e:
    logger.exception("Unexpected error")
    raise
```

### Pattern 3: Configuration Loading

Load and validate configuration:

```python
import yaml

def load_config(config_path):
    with open(config_path) as f:
        config = yaml.safe_load(f)
    validate_config(config)
    return config
```

## Anti-Patterns to Avoid

### ❌ Don't: Swallow Exceptions

```python
# BAD
try:
    do_something()
except:
    pass
```

### ✅ Do: Handle Explicitly

```python
# GOOD
try:
    do_something()
except SpecificError as e:
    logger.warning(f"Expected error: {e}")
    return default_value
```

## Category-Specific Patterns: Containers

### Recommended Approach

1. Start with the simplest implementation
2. Add complexity only when needed
3. Test each addition
4. Document decisions

### Common Integration Points

- Configuration: `assets/config.yaml`
- Validation: `scripts/validate.py`
- Documentation: `references/GUIDE.md`

---

*Pattern library for java-docker skill*


================================================
FILE: skills\java-docker\scripts\validate.py
================================================
#!/usr/bin/env python3
"""
Validation script for java-docker skill.
Category: containers
"""

import os
import sys
import yaml
import json
from pathlib import Path


def validate_config(config_path: str) -> dict:
    """
    Validate skill configuration file.

    Args:
        config_path: Path to config.yaml

    Returns:
        dict: Validation result with 'valid' and 'errors' keys
    """
    errors = []

    if not os.path.exists(config_path):
        return {"valid": False, "errors": ["Config file not found"]}

    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
    except yaml.YAMLError as e:
        return {"valid": False, "errors": [f"YAML parse error: {e}"]}

    # Validate required fields
    if 'skill' not in config:
        errors.append("Missing 'skill' section")
    else:
        if 'name' not in config['skill']:
            errors.append("Missing skill.name")
        if 'version' not in config['skill']:
            errors.append("Missing skill.version")

    # Validate settings
    if 'settings' in config:
        settings = config['settings']
        if 'log_level' in settings:
            valid_levels = ['debug', 'info', 'warn', 'error']
            if settings['log_level'] not in valid_levels:
                errors.append(f"Invalid log_level: {settings['log_level']}")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "config": config if not errors else None
    }


def validate_skill_structure(skill_path: str) -> dict:
    """
    Validate skill directory structure.

    Args:
        skill_path: Path to skill directory

    Returns:
        dict: Structure validation result
    """
    required_dirs = ['assets', 'scripts', 'references']
    required_files = ['SKILL.md']

    errors = []

    # Check required files
    for file in required_files:
        if not os.path.exists(os.path.join(skill_path, file)):
            errors.append(f"Missing required file: {file}")

    # Check required directories
    for dir in required_dirs:
        dir_path = os.path.join(skill_path, dir)
        if not os.path.isdir(dir_path):
            errors.append(f"Missing required directory: {dir}/")
        else:
            # Check for real content (not just .gitkeep)
            files = [f for f in os.listdir(dir_path) if f != '.gitkeep']
            if not files:
                errors.append(f"Directory {dir}/ has no real content")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "skill_name": os.path.basename(skill_path)
    }


def main():
    """Main validation entry point."""
    skill_path = Path(__file__).parent.parent

    print(f"Validating java-docker skill...")
    print(f"Path: {skill_path}")

    # Validate structure
    structure_result = validate_skill_structure(str(skill_path))
    print(f"\nStructure validation: {'PASS' if structure_result['valid'] else 'FAIL'}")
    if structure_result['errors']:
        for error in structure_result['errors']:
            print(f"  - {error}")

    # Validate config
    config_path = skill_path / 'assets' / 'config.yaml'
    if config_path.exists():
        config_result = validate_config(str(config_path))
        print(f"\nConfig validation: {'PASS' if config_result['valid'] else 'FAIL'}")
        if config_result['errors']:
            for error in config_result['errors']:
                print(f"  - {error}")
    else:
        print("\nConfig validation: SKIPPED (no config.yaml)")

    # Summary
    all_valid = structure_result['valid']
    print(f"\n==================================================")
    print(f"Overall: {'VALID' if all_valid else 'INVALID'}")

    return 0 if all_valid else 1


if __name__ == "__main__":
    sys.exit(main())


================================================
FILE: skills\java-fundamentals\SKILL.md
================================================
---
name: java-fundamentals
description: Master core Java programming - syntax, OOP, collections, streams, and exception handling
sasmp_version: "1.3.0"
version: "3.0.0"
bonded_agent: 01-java-fundamentals
bond_type: PRIMARY_BOND
allowed-tools: Read, Write, Bash, Glob, Grep

# Parameter Validation
parameters:
  java_version:
    type: string
    default: "21"
    enum: ["8", "11", "17", "21"]
  topic:
    type: string
    enum: [syntax, oop, collections, streams, exceptions, generics]
---

# Java Fundamentals Skill

Master core Java programming with production-quality patterns.

## Overview

This skill covers Java fundamentals including syntax, OOP, collections, streams API, and exception handling for Java 8-21.

## When to Use This Skill

Use when you need to:
- Write clean, idiomatic Java code
- Design classes following OOP principles
- Choose appropriate collection types
- Implement functional programming patterns
- Handle exceptions properly

## Topics Covered

### Core Syntax (Java 8-21)
- Variables, data types, operators
- Control flow, methods, classes
- Records (Java 16+), sealed classes (Java 17+)
- Pattern matching (Java 21)

### Object-Oriented Programming
- Classes, inheritance, polymorphism
- Interfaces and abstract classes
- SOLID principles

### Collections Framework
- List: ArrayList, LinkedList
- Set: HashSet, TreeSet
- Map: HashMap, ConcurrentHashMap
- Queue: ArrayDeque, PriorityQueue

### Streams API
- filter, map, flatMap, reduce, collect
- Optional handling
- Parallel streams

### Exception Handling
- Checked vs unchecked exceptions
- Try-with-resources
- Custom exceptions

## Quick Reference

```java
// Record (Java 16+)
public record User(String name, String email) {}

// Pattern matching (Java 21)
String format(Object obj) {
    return switch (obj) {
        case Integer i -> "Int: %d".formatted(i);
        case String s -> "String: %s".formatted(s);
        default -> obj.toString();
    };
}

// Stream operations
List<String> names = users.stream()
    .filter(User::isActive)
    .map(User::getName)
    .sorted()
    .toList();

// Optional handling
String name = Optional.ofNullable(user)
    .map(User::getName)
    .orElse("Unknown");
```

## Collection Selection

| Need | Use | Reason |
|------|-----|--------|
| Indexed access | ArrayList | O(1) random access |
| Unique elements | HashSet | O(1) contains |
| Sorted unique | TreeSet | O(log n) sorted |
| Key-value pairs | HashMap | O(1) get/put |

## Troubleshooting

| Problem | Cause | Solution |
|---------|-------|----------|
| NullPointerException | Null reference | Use Optional |
| ConcurrentModificationException | Modify during iteration | Iterator.remove() |
| ClassCastException | Wrong type | Use generics |

## Usage

```
Skill("java-fundamentals")
```


================================================
FILE: skills\java-fundamentals\assets\schema.json
================================================
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "java-fundamentals Configuration Schema",
  "type": "object",
  "properties": {
    "skill": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "version": {
          "type": "string",
          "pattern": "^\\d+\\.\\d+\\.\\d+$"
        },
        "category": {
          "type": "string",
          "enum": [
            "api",
            "testing",
            "devops",
            "security",
            "database",
            "frontend",
            "algorithms",
            "machine-learning",
            "cloud",
            "containers",
            "general"
          ]
        }
      },
      "required": [
        "name",
        "version"
      ]
    },
    "settings": {
      "type": "object",
      "properties": {
        "enabled": {
          "type": "boolean",
          "default": true
        },
        "log_level": {
          "type": "string",
          "enum": [
            "debug",
            "info",
            "warn",
            "error"
          ]
        }
      }
    }
  },
  "required": [
    "skill"
  ]
}

================================================
FILE: skills\java-fundamentals\references\GUIDE.md
================================================
# Java Fundamentals Guide

## Overview

This guide provides comprehensive documentation for the **java-fundamentals** skill in the custom-plugin-java plugin.

## Category: General

## Quick Start

### Prerequisites

- Familiarity with general concepts
- Development environment set up
- Plugin installed and configured

### Basic Usage

```bash
# Invoke the skill
claude "java-fundamentals - [your task description]"

# Example
claude "java-fundamentals - analyze the current implementation"
```

## Core Concepts

### Key Principles

1. **Consistency** - Follow established patterns
2. **Clarity** - Write readable, maintainable code
3. **Quality** - Validate before deployment

### Best Practices

- Always validate input data
- Handle edge cases explicitly
- Document your decisions
- Write tests for critical paths

## Common Tasks

### Task 1: Basic Implementation

```python
# Example implementation pattern
def implement_java_fundamentals(input_data):
    """
    Implement java-fundamentals functionality.

    Args:
        input_data: Input to process

    Returns:
        Processed result
    """
    # Validate input
    if not input_data:
        raise ValueError("Input required")

    # Process
    result = process(input_data)

    # Return
    return result
```

### Task 2: Advanced Usage

For advanced scenarios, consider:

- Configuration customization via `assets/config.yaml`
- Validation using `scripts/validate.py`
- Integration with other skills

## Troubleshooting

### Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Skill not found | Not installed | Run plugin sync |
| Validation fails | Invalid config | Check config.yaml |
| Unexpected output | Missing context | Provide more details |

## Related Resources

- SKILL.md - Skill specification
- config.yaml - Configuration options
- validate.py - Validation script

---

*Last updated: 2025-12-30*


================================================
FILE: skills\java-fundamentals\references\PATTERNS.md
================================================
# Java Fundamentals Patterns

## Design Patterns

### Pattern 1: Input Validation

Always validate input before processing:

```python
def validate_input(data):
    if data is None:
        raise ValueError("Data cannot be None")
    if not isinstance(data, dict):
        raise TypeError("Data must be a dictionary")
    return True
```

### Pattern 2: Error Handling

Use consistent error handling:

```python
try:
    result = risky_operation()
except SpecificError as e:
    logger.error(f"Operation failed: {e}")
    handle_error(e)
except Exception as e:
    logger.exception("Unexpected error")
    raise
```

### Pattern 3: Configuration Loading

Load and validate configuration:

```python
import yaml

def load_config(config_path):
    with open(config_path) as f:
        config = yaml.safe_load(f)
    validate_config(config)
    return config
```

## Anti-Patterns to Avoid

### ❌ Don't: Swallow Exceptions

```python
# BAD
try:
    do_something()
except:
    pass
```

### ✅ Do: Handle Explicitly

```python
# GOOD
try:
    do_something()
except SpecificError as e:
    logger.warning(f"Expected error: {e}")
    return default_value
```

## Category-Specific Patterns: General

### Recommended Approach

1. Start with the simplest implementation
2. Add complexity only when needed
3. Test each addition
4. Document decisions

### Common Integration Points

- Configuration: `assets/config.yaml`
- Validation: `scripts/validate.py`
- Documentation: `references/GUIDE.md`

---

*Pattern library for java-fundamentals skill*


================================================
FILE: skills\java-fundamentals\scripts\validate.py
================================================
#!/usr/bin/env python3
"""
Validation script for java-fundamentals skill.
Category: general
"""

import os
import sys
import yaml
import json
from pathlib import Path


def validate_config(config_path: str) -> dict:
    """
    Validate skill configuration file.

    Args:
        config_path: Path to config.yaml

    Returns:
        dict: Validation result with 'valid' and 'errors' keys
    """
    errors = []

    if not os.path.exists(config_path):
        return {"valid": False, "errors": ["Config file not found"]}

    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
    except yaml.YAMLError as e:
        return {"valid": False, "errors": [f"YAML parse error: {e}"]}

    # Validate required fields
    if 'skill' not in config:
        errors.append("Missing 'skill' section")
    else:
        if 'name' not in config['skill']:
            errors.append("Missing skill.name")
        if 'version' not in config['skill']:
            errors.append("Missing skill.version")

    # Validate settings
    if 'settings' in config:
        settings = config['settings']
        if 'log_level' in settings:
            valid_levels = ['debug', 'info', 'warn', 'error']
            if settings['log_level'] not in valid_levels:
                errors.append(f"Invalid log_level: {settings['log_level']}")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "config": config if not errors else None
    }


def validate_skill_structure(skill_path: str) -> dict:
    """
    Validate skill directory structure.

    Args:
        skill_path: Path to skill directory

    Returns:
        dict: Structure validation result
    """
    required_dirs = ['assets', 'scripts', 'references']
    required_files = ['SKILL.md']

    errors = []

    # Check required files
    for file in required_files:
        if not os.path.exists(os.path.join(skill_path, file)):
            errors.append(f"Missing required file: {file}")

    # Check required directories
    for dir in required_dirs:
        dir_path = os.path.join(skill_path, dir)
        if not os.path.isdir(dir_path):
            errors.append(f"Missing required directory: {dir}/")
        else:
            # Check for real content (not just .gitkeep)
            files = [f for f in os.listdir(dir_path) if f != '.gitkeep']
            if not files:
                errors.append(f"Directory {dir}/ has no real content")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "skill_name": os.path.basename(skill_path)
    }


def main():
    """Main validation entry point."""
    skill_path = Path(__file__).parent.parent

    print(f"Validating java-fundamentals skill...")
    print(f"Path: {skill_path}")

    # Validate structure
    structure_result = validate_skill_structure(str(skill_path))
    print(f"\nStructure validation: {'PASS' if structure_result['valid'] else 'FAIL'}")
    if structure_result['errors']:
        for error in structure_result['errors']:
            print(f"  - {error}")

    # Validate config
    config_path = skill_path / 'assets' / 'config.yaml'
    if config_path.exists():
        config_result = validate_config(str(config_path))
        print(f"\nConfig validation: {'PASS' if config_result['valid'] else 'FAIL'}")
        if config_result['errors']:
            for error in config_result['errors']:
                print(f"  - {error}")
    else:
        print("\nConfig validation: SKIPPED (no config.yaml)")

    # Summary
    all_valid = structure_result['valid']
    print(f"\n==================================================")
    print(f"Overall: {'VALID' if all_valid else 'INVALID'}")

    return 0 if all_valid else 1


if __name__ == "__main__":
    sys.exit(main())


================================================
FILE: skills\java-gradle\SKILL.md
================================================
---
name: java-gradle
description: Master Gradle - Kotlin DSL, task configuration, build optimization, caching
sasmp_version: "1.3.0"
version: "3.0.0"
bonded_agent: 05-java-build-tools
bond_type: SECONDARY_BOND
allowed-tools: Read, Write, Bash, Glob, Grep

# Parameter Validation
parameters:
  dsl:
    type: string
    enum: [kotlin, groovy]
    default: kotlin
    description: Gradle DSL preference
---

# Java Gradle Skill

Master Gradle build tool with Kotlin DSL for Java projects.

## Overview

This skill covers Gradle configuration with Kotlin DSL including task configuration, dependency management with catalogs, build cache optimization, and CI/CD integration.

## When to Use This Skill

Use when you need to:
- Configure Gradle builds (Kotlin DSL)
- Manage dependencies with catalogs
- Optimize build performance
- Set up build cache
- Create custom tasks

## Quick Reference

```kotlin
// build.gradle.kts
plugins {
    java
    id("org.springframework.boot") version "3.2.1"
    id("io.spring.dependency-management") version "1.1.4"
}

java {
    toolchain {
        languageVersion = JavaLanguageVersion.of(21)
    }
}

repositories {
    mavenCentral()
}

dependencies {
    implementation("org.springframework.boot:spring-boot-starter-web")
    testImplementation("org.springframework.boot:spring-boot-starter-test")
}

tasks.withType<JavaCompile> {
    options.compilerArgs.addAll(listOf("-parameters", "-Xlint:all"))
    options.isFork = true
    options.isIncremental = true
}

tasks.test {
    useJUnitPlatform()
    maxParallelForks = Runtime.getRuntime().availableProcessors() / 2
}
```

## Version Catalog

```toml
# gradle/libs.versions.toml
[versions]
spring-boot = "3.2.1"

[libraries]
spring-boot-web = { module = "org.springframework.boot:spring-boot-starter-web", version.ref = "spring-boot" }

[plugins]
spring-boot = { id = "org.springframework.boot", version.ref = "spring-boot" }
```

## Useful Commands

```bash
gradle dependencies              # View dependencies
gradle dependencyInsight --dependency log4j  # Analyze dep
gradle build --scan              # Build scan
gradle build --build-cache       # Use cache
gradle wrapper --gradle-version 8.5  # Update wrapper
```

## Build Optimization

```kotlin
// settings.gradle.kts
enableFeaturePreview("STABLE_CONFIGURATION_CACHE")

// Enable parallel and caching
org.gradle.parallel=true
org.gradle.caching=true
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Slow builds | Enable --build-cache |
| Version conflict | Use platform() or constraints |
| Cache issues | gradle --refresh-dependencies |

## Usage

```
Skill("java-gradle")
```


================================================
FILE: skills\java-gradle\assets\schema.json
================================================
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "java-gradle Configuration Schema",
  "type": "object",
  "properties": {
    "skill": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "version": {
          "type": "string",
          "pattern": "^\\d+\\.\\d+\\.\\d+$"
        },
        "category": {
          "type": "string",
          "enum": [
            "api",
            "testing",
            "devops",
            "security",
            "database",
            "frontend",
            "algorithms",
            "machine-learning",
            "cloud",
            "containers",
            "general"
          ]
        }
      },
      "required": [
        "name",
        "version"
      ]
    },
    "settings": {
      "type": "object",
      "properties": {
        "enabled": {
          "type": "boolean",
          "default": true
        },
        "log_level": {
          "type": "string",
          "enum": [
            "debug",
            "info",
            "warn",
            "error"
          ]
        }
      }
    }
  },
  "required": [
    "skill"
  ]
}

================================================
FILE: skills\java-gradle\references\GUIDE.md
================================================
# Java Gradle Guide

## Overview

This guide provides comprehensive documentation for the **java-gradle** skill in the custom-plugin-java plugin.

## Category: General

## Quick Start

### Prerequisites

- Familiarity with general concepts
- Development environment set up
- Plugin installed and configured

### Basic Usage

```bash
# Invoke the skill
claude "java-gradle - [your task description]"

# Example
claude "java-gradle - analyze the current implementation"
```

## Core Concepts

### Key Principles

1. **Consistency** - Follow established patterns
2. **Clarity** - Write readable, maintainable code
3. **Quality** - Validate before deployment

### Best Practices

- Always validate input data
- Handle edge cases explicitly
- Document your decisions
- Write tests for critical paths

## Common Tasks

### Task 1: Basic Implementation

```python
# Example implementation pattern
def implement_java_gradle(input_data):
    """
    Implement java-gradle functionality.

    Args:
        input_data: Input to process

    Returns:
        Processed result
    """
    # Validate input
    if not input_data:
        raise ValueError("Input required")

    # Process
    result = process(input_data)

    # Return
    return result
```

### Task 2: Advanced Usage

For advanced scenarios, consider:

- Configuration customization via `assets/config.yaml`
- Validation using `scripts/validate.py`
- Integration with other skills

## Troubleshooting

### Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Skill not found | Not installed | Run plugin sync |
| Validation fails | Invalid config | Check config.yaml |
| Unexpected output | Missing context | Provide more details |

## Related Resources

- SKILL.md - Skill specification
- config.yaml - Configuration options
- validate.py - Validation script

---

*Last updated: 2025-12-30*


================================================
FILE: skills\java-gradle\references\PATTERNS.md
================================================
# Java Gradle Patterns

## Design Patterns

### Pattern 1: Input Validation

Always validate input before processing:

```python
def validate_input(data):
    if data is None:
        raise ValueError("Data cannot be None")
    if not isinstance(data, dict):
        raise TypeError("Data must be a dictionary")
    return True
```

### Pattern 2: Error Handling

Use consistent error handling:

```python
try:
    result = risky_operation()
except SpecificError as e:
    logger.error(f"Operation failed: {e}")
    handle_error(e)
except Exception as e:
    logger.exception("Unexpected error")
    raise
```

### Pattern 3: Configuration Loading

Load and validate configuration:

```python
import yaml

def load_config(config_path):
    with open(config_path) as f:
        config = yaml.safe_load(f)
    validate_config(config)
    return config
```

## Anti-Patterns to Avoid

### ❌ Don't: Swallow Exceptions

```python
# BAD
try:
    do_something()
except:
    pass
```

### ✅ Do: Handle Explicitly

```python
# GOOD
try:
    do_something()
except SpecificError as e:
    logger.warning(f"Expected error: {e}")
    return default_value
```

## Category-Specific Patterns: General

### Recommended Approach

1. Start with the simplest implementation
2. Add complexity only when needed
3. Test each addition
4. Document decisions

### Common Integration Points

- Configuration: `assets/config.yaml`
- Validation: `scripts/validate.py`
- Documentation: `references/GUIDE.md`

---

*Pattern library for java-gradle skill*


================================================
FILE: skills\java-gradle\scripts\validate.py
================================================
#!/usr/bin/env python3
"""
Validation script for java-gradle skill.
Category: general
"""

import os
import sys
import yaml
import json
from pathlib import Path


def validate_config(config_path: str) -> dict:
    """
    Validate skill configuration file.

    Args:
        config_path: Path to config.yaml

    Returns:
        dict: Validation result with 'valid' and 'errors' keys
    """
    errors = []

    if not os.path.exists(config_path):
        return {"valid": False, "errors": ["Config file not found"]}

    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
    except yaml.YAMLError as e:
        return {"valid": False, "errors": [f"YAML parse error: {e}"]}

    # Validate required fields
    if 'skill' not in config:
        errors.append("Missing 'skill' section")
    else:
        if 'name' not in config['skill']:
            errors.append("Missing skill.name")
        if 'version' not in config['skill']:
            errors.append("Missing skill.version")

    # Validate settings
    if 'settings' in config:
        settings = config['settings']
        if 'log_level' in settings:
            valid_levels = ['debug', 'info', 'warn', 'error']
            if settings['log_level'] not in valid_levels:
                errors.append(f"Invalid log_level: {settings['log_level']}")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "config": config if not errors else None
    }


def validate_skill_structure(skill_path: str) -> dict:
    """
    Validate skill directory structure.

    Args:
        skill_path: Path to skill directory

    Returns:
        dict: Structure validation result
    """
    required_dirs = ['assets', 'scripts', 'references']
    required_files = ['SKILL.md']

    errors = []

    # Check required files
    for file in required_files:
        if not os.path.exists(os.path.join(skill_path, file)):
            errors.append(f"Missing required file: {file}")

    # Check required directories
    for dir in required_dirs:
        dir_path = os.path.join(skill_path, dir)
        if not os.path.isdir(dir_path):
            errors.append(f"Missing required directory: {dir}/")
        else:
            # Check for real content (not just .gitkeep)
            files = [f for f in os.listdir(dir_path) if f != '.gitkeep']
            if not files:
                errors.append(f"Directory {dir}/ has no real content")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "skill_name": os.path.basename(skill_path)
    }


def main():
    """Main validation entry point."""
    skill_path = Path(__file__).parent.parent

    print(f"Validating java-gradle skill...")
    print(f"Path: {skill_path}")

    # Validate structure
    structure_result = validate_skill_structure(str(skill_path))
    print(f"\nStructure validation: {'PASS' if structure_result['valid'] else 'FAIL'}")
    if structure_result['errors']:
        for error in structure_result['errors']:
            print(f"  - {error}")

    # Validate config
    config_path = skill_path / 'assets' / 'config.yaml'
    if config_path.exists():
        config_result = validate_config(str(config_path))
        print(f"\nConfig validation: {'PASS' if config_result['valid'] else 'FAIL'}")
        if config_result['errors']:
            for error in config_result['errors']:
                print(f"  - {error}")
    else:
        print("\nConfig validation: SKIPPED (no config.yaml)")

    # Summary
    all_valid = structure_result['valid']
    print(f"\n==================================================")
    print(f"Overall: {'VALID' if all_valid else 'INVALID'}")

    return 0 if all_valid else 1


if __name__ == "__main__":
    sys.exit(main())


================================================
FILE: skills\java-jpa-hibernate\SKILL.md
================================================
---
name: java-jpa-hibernate
description: Master JPA/Hibernate - entity design, queries, transactions, performance optimization
sasmp_version: "1.3.0"
version: "3.0.0"
bonded_agent: 06-java-persistence
bond_type: PRIMARY_BOND
allowed-tools: Read, Write, Bash, Glob, Grep

# Parameter Validation
parameters:
  database:
    type: string
    enum: [postgresql, mysql, oracle, h2]
    description: Target database
  focus:
    type: string
    enum: [entities, queries, transactions, caching]
    description: Topic focus area
---

# Java JPA Hibernate Skill

Master data persistence with JPA and Hibernate for production applications.

## Overview

This skill covers JPA entity design, Hibernate optimization, Spring Data repositories, query strategies, and caching. Focuses on preventing N+1 queries and building high-performance persistence layers.

## When to Use This Skill

Use when you need to:
- Design JPA entities with relationships
- Optimize database queries
- Configure Hibernate for performance
- Implement caching strategies
- Debug persistence issues

## Topics Covered

### Entity Design
- Entity mapping annotations
- Relationship types (1:1, 1:N, N:M)
- Inheritance strategies
- Lifecycle callbacks
- Auditing

### Query Optimization
- N+1 problem prevention
- JOIN FETCH vs EntityGraph
- Batch fetching
- Projections and DTOs

### Transactions
- @Transactional configuration
- Propagation and isolation
- Optimistic vs pessimistic locking
- Deadlock prevention

### Caching
- First and second level cache
- Query cache
- Cache invalidation
- Redis integration

## Quick Reference

```java
// Entity with relationships
@Entity
@Table(name = "orders")
public class Order {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "customer_id", nullable = false)
    private Customer customer;

    @OneToMany(mappedBy = "order", cascade = CascadeType.ALL, orphanRemoval = true)
    @BatchSize(size = 20)
    private List<OrderItem> items = new ArrayList<>();

    @Version
    private Long version;

    // Bidirectional helper
    public void addItem(OrderItem item) {
        items.add(item);
        item.setOrder(this);
    }
}

// Auditing base class
@MappedSuperclass
@EntityListeners(AuditingEntityListener.class)
public abstract class Auditable {
    @CreatedDate
    @Column(updatable = false)
    private Instant createdAt;

    @LastModifiedDate
    private Instant updatedAt;
}

// Repository with query optimization
public interface OrderRepository extends JpaRepository<Order, Long> {

    // JOIN FETCH to prevent N+1
    @Query("SELECT DISTINCT o FROM Order o JOIN FETCH o.items WHERE o.status = :status")
    List<Order> findByStatusWithItems(@Param("status") Status status);

    // EntityGraph alternative
    @EntityGraph(attributePaths = {"items", "customer"})
    Optional<Order> findById(Long id);

    // DTO Projection
    @Query("SELECT new com.example.OrderSummary(o.id, o.status, c.name) " +
           "FROM Order o JOIN o.customer c WHERE o.id = :id")
    Optional<OrderSummary> findSummaryById(@Param("id") Long id);
}
```

## N+1 Prevention Strategies

| Strategy | Use When | Example |
|----------|----------|---------|
| JOIN FETCH | Always need relation | `JOIN FETCH o.items` |
| EntityGraph | Dynamic fetching | `@EntityGraph(attributePaths)` |
| @BatchSize | Collection access | `@BatchSize(size = 20)` |
| DTO Projection | Read-only queries | `new OrderSummary(...)` |

## Hibernate Configuration

```yaml
spring:
  jpa:
    open-in-view: false  # Critical!
    properties:
      hibernate:
        jdbc.batch_size: 50
        order_inserts: true
        order_updates: true
        default_batch_fetch_size: 20
        generate_statistics: ${HIBERNATE_STATS:false}

  datasource:
    hikari:
      maximum-pool-size: 20
      minimum-idle: 5
      leak-detection-threshold: 60000
```

## Troubleshooting

### Common Issues

| Problem | Cause | Solution |
|---------|-------|----------|
| N+1 queries | Lazy in loop | JOIN FETCH, EntityGraph |
| LazyInitException | Session closed | DTO projection |
| Slow queries | Missing index | EXPLAIN ANALYZE |
| Connection leak | No @Transactional | Add annotation |

### Debug Properties
```properties
spring.jpa.show-sql=true
logging.level.org.hibernate.SQL=DEBUG
logging.level.org.hibernate.orm.jdbc.bind=TRACE
hibernate.generate_statistics=true
```

### Debug Checklist
```
□ Enable SQL logging
□ Check query count per request
□ Verify fetch strategies
□ Review @Transactional
□ Check connection pool
```

## Usage

```
Skill("java-jpa-hibernate")
```

## Related Skills
- `java-performance` - Query optimization
- `java-spring-boot` - Spring Data


================================================
FILE: skills\java-jpa-hibernate\assets\schema.json
================================================
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "java-jpa-hibernate Configuration Schema",
  "type": "object",
  "properties": {
    "skill": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "version": {
          "type": "string",
          "pattern": "^\\d+\\.\\d+\\.\\d+$"
        },
        "category": {
          "type": "string",
          "enum": [
            "api",
            "testing",
            "devops",
            "security",
            "database",
            "frontend",
            "algorithms",
            "machine-learning",
            "cloud",
            "containers",
            "general"
          ]
        }
      },
      "required": [
        "name",
        "version"
      ]
    },
    "settings": {
      "type": "object",
      "properties": {
        "enabled": {
          "type": "boolean",
          "default": true
        },
        "log_level": {
          "type": "string",
          "enum": [
            "debug",
            "info",
            "warn",
            "error"
          ]
        }
      }
    }
  },
  "required": [
    "skill"
  ]
}

================================================
FILE: skills\java-jpa-hibernate\references\GUIDE.md
================================================
# Java Jpa Hibernate Guide

## Overview

This guide provides comprehensive documentation for the **java-jpa-hibernate** skill in the custom-plugin-java plugin.

## Category: General

## Quick Start

### Prerequisites

- Familiarity with general concepts
- Development environment set up
- Plugin installed and configured

### Basic Usage

```bash
# Invoke the skill
claude "java-jpa-hibernate - [your task description]"

# Example
claude "java-jpa-hibernate - analyze the current implementation"
```

## Core Concepts

### Key Principles

1. **Consistency** - Follow established patterns
2. **Clarity** - Write readable, maintainable code
3. **Quality** - Validate before deployment

### Best Practices

- Always validate input data
- Handle edge cases explicitly
- Document your decisions
- Write tests for critical paths

## Common Tasks

### Task 1: Basic Implementation

```python
# Example implementation pattern
def implement_java_jpa_hibernate(input_data):
    """
    Implement java-jpa-hibernate functionality.

    Args:
        input_data: Input to process

    Returns:
        Processed result
    """
    # Validate input
    if not input_data:
        raise ValueError("Input required")

    # Process
    result = process(input_data)

    # Return
    return result
```

### Task 2: Advanced Usage

For advanced scenarios, consider:

- Configuration customization via `assets/config.yaml`
- Validation using `scripts/validate.py`
- Integration with other skills

## Troubleshooting

### Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Skill not found | Not installed | Run plugin sync |
| Validation fails | Invalid config | Check config.yaml |
| Unexpected output | Missing context | Provide more details |

## Related Resources

- SKILL.md - Skill specification
- config.yaml - Configuration options
- validate.py - Validation script

---

*Last updated: 2025-12-30*


================================================
FILE: skills\java-jpa-hibernate\references\PATTERNS.md
================================================
# Java Jpa Hibernate Patterns

## Design Patterns

### Pattern 1: Input Validation

Always validate input before processing:

```python
def validate_input(data):
    if data is None:
        raise ValueError("Data cannot be None")
    if not isinstance(data, dict):
        raise TypeError("Data must be a dictionary")
    return True
```

### Pattern 2: Error Handling

Use consistent error handling:

```python
try:
    result = risky_operation()
except SpecificError as e:
    logger.error(f"Operation failed: {e}")
    handle_error(e)
except Exception as e:
    logger.exception("Unexpected error")
    raise
```

### Pattern 3: Configuration Loading

Load and validate configuration:

```python
import yaml

def load_config(config_path):
    with open(config_path) as f:
        config = yaml.safe_load(f)
    validate_config(config)
    return config
```

## Anti-Patterns to Avoid

### ❌ Don't: Swallow Exceptions

```python
# BAD
try:
    do_something()
except:
    pass
```

### ✅ Do: Handle Explicitly

```python
# GOOD
try:
    do_something()
except SpecificError as e:
    logger.warning(f"Expected error: {e}")
    return default_value
```

## Category-Specific Patterns: General

### Recommended Approach

1. Start with the simplest implementation
2. Add complexity only when needed
3. Test each addition
4. Document decisions

### Common Integration Points

- Configuration: `assets/config.yaml`
- Validation: `scripts/validate.py`
- Documentation: `references/GUIDE.md`

---

*Pattern library for java-jpa-hibernate skill*


================================================
FILE: skills\java-jpa-hibernate\scripts\validate.py
================================================
#!/usr/bin/env python3
"""
Validation script for java-jpa-hibernate skill.
Category: general
"""

import os
import sys
import yaml
import json
from pathlib import Path


def validate_config(config_path: str) -> dict:
    """
    Validate skill configuration file.

    Args:
        config_path: Path to config.yaml

    Returns:
        dict: Validation result with 'valid' and 'errors' keys
    """
    errors = []

    if not os.path.exists(config_path):
        return {"valid": False, "errors": ["Config file not found"]}

    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
    except yaml.YAMLError as e:
        return {"valid": False, "errors": [f"YAML parse error: {e}"]}

    # Validate required fields
    if 'skill' not in config:
        errors.append("Missing 'skill' section")
    else:
        if 'name' not in config['skill']:
            errors.append("Missing skill.name")
        if 'version' not in config['skill']:
            errors.append("Missing skill.version")

    # Validate settings
    if 'settings' in config:
        settings = config['settings']
        if 'log_level' in settings:
            valid_levels = ['debug', 'info', 'warn', 'error']
            if settings['log_level'] not in valid_levels:
                errors.append(f"Invalid log_level: {settings['log_level']}")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "config": config if not errors else None
    }


def validate_skill_structure(skill_path: str) -> dict:
    """
    Validate skill directory structure.

    Args:
        skill_path: Path to skill directory

    Returns:
        dict: Structure validation result
    """
    required_dirs = ['assets', 'scripts', 'references']
    required_files = ['SKILL.md']

    errors = []

    # Check required files
    for file in required_files:
        if not os.path.exists(os.path.join(skill_path, file)):
            errors.append(f"Missing required file: {file}")

    # Check required directories
    for dir in required_dirs:
        dir_path = os.path.join(skill_path, dir)
        if not os.path.isdir(dir_path):
            errors.append(f"Missing required directory: {dir}/")
        else:
            # Check for real content (not just .gitkeep)
            files = [f for f in os.listdir(dir_path) if f != '.gitkeep']
            if not files:
                errors.append(f"Directory {dir}/ has no real content")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "skill_name": os.path.basename(skill_path)
    }


def main():
    """Main validation entry point."""
    skill_path = Path(__file__).parent.parent

    print(f"Validating java-jpa-hibernate skill...")
    print(f"Path: {skill_path}")

    # Validate structure
    structure_result = validate_skill_structure(str(skill_path))
    print(f"\nStructure validation: {'PASS' if structure_result['valid'] else 'FAIL'}")
    if structure_result['errors']:
        for error in structure_result['errors']:
            print(f"  - {error}")

    # Validate config
    config_path = skill_path / 'assets' / 'config.yaml'
    if config_path.exists():
        config_result = validate_config(str(config_path))
        print(f"\nConfig validation: {'PASS' if config_result['valid'] else 'FAIL'}")
        if config_result['errors']:
            for error in config_result['errors']:
                print(f"  - {error}")
    else:
        print("\nConfig validation: SKIPPED (no config.yaml)")

    # Summary
    all_valid = structure_result['valid']
    print(f"\n==================================================")
    print(f"Overall: {'VALID' if all_valid else 'INVALID'}")

    return 0 if all_valid else 1


if __name__ == "__main__":
    sys.exit(main())


================================================
FILE: skills\java-maven\SKILL.md
================================================
---
name: java-maven
description: Master Apache Maven - POM configuration, plugins, lifecycle, dependency management
sasmp_version: "1.3.0"
version: "3.0.0"
bonded_agent: 05-java-build-tools
bond_type: SECONDARY_BOND
allowed-tools: Read, Write, Bash, Glob, Grep

# Parameter Validation
parameters:
  project_type:
    type: string
    enum: [single, multi_module, library]
    description: Project structure
---

# Java Maven Skill

Master Apache Maven for Java project builds and dependency management.

## Overview

This skill covers Maven configuration including POM structure, lifecycle phases, plugin configuration, dependency management with BOMs, and multi-module projects.

## When to Use This Skill

Use when you need to:
- Configure Maven POM files
- Manage dependencies with BOMs
- Set up build plugins
- Create multi-module projects
- Troubleshoot build issues

## Quick Reference

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>my-app</artifactId>
    <version>1.0.0-SNAPSHOT</version>

    <properties>
        <java.version>21</java.version>
        <maven.compiler.source>${java.version}</maven.compiler.source>
        <maven.compiler.target>${java.version}</maven.compiler.target>
    </properties>

    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-dependencies</artifactId>
                <version>3.2.1</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-enforcer-plugin</artifactId>
                <version>3.4.1</version>
            </plugin>
        </plugins>
    </build>
</project>
```

## Lifecycle Phases

```
validate → compile → test → package → verify → install → deploy
```

## Useful Commands

```bash
mvn dependency:tree                    # View dependencies
mvn dependency:analyze                 # Find unused/undeclared
mvn versions:display-dependency-updates  # Check updates
mvn help:effective-pom                 # View effective POM
mvn -B verify                          # Batch mode build
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Dependency not found | Check repository, version |
| Version conflict | Use BOM or enforcer |
| Build OOM | Set MAVEN_OPTS=-Xmx1g |

## Usage

```
Skill("java-maven")
```


================================================
FILE: skills\java-maven\assets\schema.json
================================================
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "java-maven Configuration Schema",
  "type": "object",
  "properties": {
    "skill": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "version": {
          "type": "string",
          "pattern": "^\\d+\\.\\d+\\.\\d+$"
        },
        "category": {
          "type": "string",
          "enum": [
            "api",
            "testing",
            "devops",
            "security",
            "database",
            "frontend",
            "algorithms",
            "machine-learning",
            "cloud",
            "containers",
            "general"
          ]
        }
      },
      "required": [
        "name",
        "version"
      ]
    },
    "settings": {
      "type": "object",
      "properties": {
        "enabled": {
          "type": "boolean",
          "default": true
        },
        "log_level": {
          "type": "string",
          "enum": [
            "debug",
            "info",
            "warn",
            "error"
          ]
        }
      }
    }
  },
  "required": [
    "skill"
  ]
}

================================================
FILE: skills\java-maven\references\GUIDE.md
================================================
# Java Maven Guide

## Overview

This guide provides comprehensive documentation for the **java-maven** skill in the custom-plugin-java plugin.

## Category: General

## Quick Start

### Prerequisites

- Familiarity with general concepts
- Development environment set up
- Plugin installed and configured

### Basic Usage

```bash
# Invoke the skill
claude "java-maven - [your task description]"

# Example
claude "java-maven - analyze the current implementation"
```

## Core Concepts

### Key Principles

1. **Consistency** - Follow established patterns
2. **Clarity** - Write readable, maintainable code
3. **Quality** - Validate before deployment

### Best Practices

- Always validate input data
- Handle edge cases explicitly
- Document your decisions
- Write tests for critical paths

## Common Tasks

### Task 1: Basic Implementation

```python
# Example implementation pattern
def implement_java_maven(input_data):
    """
    Implement java-maven functionality.

    Args:
        input_data: Input to process

    Returns:
        Processed result
    """
    # Validate input
    if not input_data:
        raise ValueError("Input required")

    # Process
    result = process(input_data)

    # Return
    return result
```

### Task 2: Advanced Usage

For advanced scenarios, consider:

- Configuration customization via `assets/config.yaml`
- Validation using `scripts/validate.py`
- Integration with other skills

## Troubleshooting

### Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Skill not found | Not installed | Run plugin sync |
| Validation fails | Invalid config | Check config.yaml |
| Unexpected output | Missing context | Provide more details |

## Related Resources

- SKILL.md - Skill specification
- config.yaml - Configuration options
- validate.py - Validation script

---

*Last updated: 2025-12-30*


================================================
FILE: skills\java-maven\references\PATTERNS.md
================================================
# Java Maven Patterns

## Design Patterns

### Pattern 1: Input Validation

Always validate input before processing:

```python
def validate_input(data):
    if data is None:
        raise ValueError("Data cannot be None")
    if not isinstance(data, dict):
        raise TypeError("Data must be a dictionary")
    return True
```

### Pattern 2: Error Handling

Use consistent error handling:

```python
try:
    result = risky_operation()
except SpecificError as e:
    logger.error(f"Operation failed: {e}")
    handle_error(e)
except Exception as e:
    logger.exception("Unexpected error")
    raise
```

### Pattern 3: Configuration Loading

Load and validate configuration:

```python
import yaml

def load_config(config_path):
    with open(config_path) as f:
        config = yaml.safe_load(f)
    validate_config(config)
    return config
```

## Anti-Patterns to Avoid

### ❌ Don't: Swallow Exceptions

```python
# BAD
try:
    do_something()
except:
    pass
```

### ✅ Do: Handle Explicitly

```python
# GOOD
try:
    do_something()
except SpecificError as e:
    logger.warning(f"Expected error: {e}")
    return default_value
```

## Category-Specific Patterns: General

### Recommended Approach

1. Start with the simplest implementation
2. Add complexity only when needed
3. Test each addition
4. Document decisions

### Common Integration Points

- Configuration: `assets/config.yaml`
- Validation: `scripts/validate.py`
- Documentation: `references/GUIDE.md`

---

*Pattern library for java-maven skill*


================================================
FILE: skills\java-maven\scripts\validate.py
================================================
#!/usr/bin/env python3
"""
Validation script for java-maven skill.
Category: general
"""

import os
import sys
import yaml
import json
from pathlib import Path


def validate_config(config_path: str) -> dict:
    """
    Validate skill configuration file.

    Args:
        config_path: Path to config.yaml

    Returns:
        dict: Validation result with 'valid' and 'errors' keys
    """
    errors = []

    if not os.path.exists(config_path):
        return {"valid": False, "errors": ["Config file not found"]}

    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
    except yaml.YAMLError as e:
        return {"valid": False, "errors": [f"YAML parse error: {e}"]}

    # Validate required fields
    if 'skill' not in config:
        errors.append("Missing 'skill' section")
    else:
        if 'name' not in config['skill']:
            errors.append("Missing skill.name")
        if 'version' not in config['skill']:
            errors.append("Missing skill.version")

    # Validate settings
    if 'settings' in config:
        settings = config['settings']
        if 'log_level' in settings:
            valid_levels = ['debug', 'info', 'warn', 'error']
            if settings['log_level'] not in valid_levels:
                errors.append(f"Invalid log_level: {settings['log_level']}")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "config": config if not errors else None
    }


def validate_skill_structure(skill_path: str) -> dict:
    """
    Validate skill directory structure.

    Args:
        skill_path: Path to skill directory

    Returns:
        dict: Structure validation result
    """
    required_dirs = ['assets', 'scripts', 'references']
    required_files = ['SKILL.md']

    errors = []

    # Check required files
    for file in required_files:
        if not os.path.exists(os.path.join(skill_path, file)):
            errors.append(f"Missing required file: {file}")

    # Check required directories
    for dir in required_dirs:
        dir_path = os.path.join(skill_path, dir)
        if not os.path.isdir(dir_path):
            errors.append(f"Missing required directory: {dir}/")
        else:
            # Check for real content (not just .gitkeep)
            files = [f for f in os.listdir(dir_path) if f != '.gitkeep']
            if not files:
                errors.append(f"Directory {dir}/ has no real content")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "skill_name": os.path.basename(skill_path)
    }


def main():
    """Main validation entry point."""
    skill_path = Path(__file__).parent.parent

    print(f"Validating java-maven skill...")
    print(f"Path: {skill_path}")

    # Validate structure
    structure_result = validate_skill_structure(str(skill_path))
    print(f"\nStructure validation: {'PASS' if structure_result['valid'] else 'FAIL'}")
    if structure_result['errors']:
        for error in structure_result['errors']:
            print(f"  - {error}")

    # Validate config
    config_path = skill_path / 'assets' / 'config.yaml'
    if config_path.exists():
        config_result = validate_config(str(config_path))
        print(f"\nConfig validation: {'PASS' if config_result['valid'] else 'FAIL'}")
        if config_result['errors']:
            for error in config_result['errors']:
                print(f"  - {error}")
    else:
        print("\nConfig validation: SKIPPED (no config.yaml)")

    # Summary
    all_valid = structure_result['valid']
    print(f"\n==================================================")
    print(f"Overall: {'VALID' if all_valid else 'INVALID'}")

    return 0 if all_valid else 1


if __name__ == "__main__":
    sys.exit(main())


================================================
FILE: skills\java-maven-gradle\SKILL.md
================================================
---
name: java-maven-gradle
description: Master Maven and Gradle - build configuration, dependencies, plugins, CI/CD
sasmp_version: "1.3.0"
version: "3.0.0"
bonded_agent: 05-java-build-tools
bond_type: PRIMARY_BOND
allowed-tools: Read, Write, Bash, Glob, Grep

# Parameter Validation
parameters:
  build_tool:
    type: string
    enum: [maven, gradle]
    description: Preferred build tool
  project_type:
    type: string
    enum: [single, multi_module, library]
    description: Project structure type
---

# Java Maven Gradle Skill

Master Java build tools for efficient project management and CI/CD integration.

## Overview

This skill covers Maven and Gradle configuration including dependency management, plugin setup, multi-module projects, and CI/CD pipeline integration. Follows 2024-2025 best practices for both tools.

## When to Use This Skill

Use when you need to:
- Set up Maven/Gradle projects
- Manage dependencies with BOMs
- Configure build plugins
- Optimize build performance
- Set up CI/CD pipelines

## Topics Covered

### Maven
- POM structure and inheritance
- Dependency management with BOMs
- Plugin configuration
- Profiles and properties
- Multi-module projects

### Gradle
- Kotlin DSL (build.gradle.kts)
- Dependency catalogs
- Task configuration
- Build cache optimization
- Composite builds

### CI/CD Integration
- GitHub Actions workflows
- Dependency caching
- Matrix builds
- Artifact publishing

## Quick Reference

### Maven POM
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>my-app</artifactId>
    <version>1.0.0-SNAPSHOT</version>

    <properties>
        <java.version>21</java.version>
        <maven.compiler.source>${java.version}</maven.compiler.source>
        <maven.compiler.target>${java.version}</maven.compiler.target>
        <spring-boot.version>3.2.1</spring-boot.version>
    </properties>

    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-dependencies</artifactId>
                <version>${spring-boot.version}</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-enforcer-plugin</artifactId>
                <version>3.4.1</version>
            </plugin>
        </plugins>
    </build>
</project>
```

### Gradle Kotlin DSL
```kotlin
// build.gradle.kts
plugins {
    java
    id("org.springframework.boot") version "3.2.1"
    id("io.spring.dependency-management") version "1.1.4"
}

java {
    toolchain {
        languageVersion = JavaLanguageVersion.of(21)
    }
}

dependencies {
    implementation("org.springframework.boot:spring-boot-starter-web")
    testImplementation("org.springframework.boot:spring-boot-starter-test")
}

tasks.test {
    useJUnitPlatform()
    maxParallelForks = Runtime.getRuntime().availableProcessors() / 2
}
```

### Version Catalog (libs.versions.toml)
```toml
[versions]
spring-boot = "3.2.1"
junit = "5.10.1"

[libraries]
spring-boot-starter-web = { module = "org.springframework.boot:spring-boot-starter-web", version.ref = "spring-boot" }
junit-jupiter = { module = "org.junit.jupiter:junit-jupiter", version.ref = "junit" }

[plugins]
spring-boot = { id = "org.springframework.boot", version.ref = "spring-boot" }
```

## CI/CD Templates

```yaml
# .github/workflows/ci.yml
name: CI
on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with:
          java-version: '21'
          distribution: 'temurin'
          cache: 'maven'  # or 'gradle'
      - run: ./mvnw -B verify
```

## Useful Commands

```bash
# Maven
mvn dependency:tree
mvn versions:display-dependency-updates
mvn help:effective-pom

# Gradle
gradle dependencies
gradle dependencyInsight --dependency log4j
gradle build --scan
```

## Troubleshooting

### Common Issues

| Problem | Cause | Solution |
|---------|-------|----------|
| Dependency not found | Wrong version | Check Maven Central |
| Version conflict | Transitive deps | Use BOM or enforcer |
| Build OOM | Heap too small | Set MAVEN_OPTS |
| Slow builds | No caching | Enable build cache |

### Debug Checklist
```
□ Check effective POM/build
□ Analyze dependency tree
□ Verify repository order
□ Check plugin versions
□ Review build cache
```

## Usage

```
Skill("java-maven-gradle")
```

## Related Skills
- `java-maven` - Maven specific
- `java-gradle` - Gradle specific


================================================
FILE: skills\java-maven-gradle\assets\schema.json
================================================
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "java-maven-gradle Configuration Schema",
  "type": "object",
  "properties": {
    "skill": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "version": {
          "type": "string",
          "pattern": "^\\d+\\.\\d+\\.\\d+$"
        },
        "category": {
          "type": "string",
          "enum": [
            "api",
            "testing",
            "devops",
            "security",
            "database",
            "frontend",
            "algorithms",
            "machine-learning",
            "cloud",
            "containers",
            "general"
          ]
        }
      },
      "required": [
        "name",
        "version"
      ]
    },
    "settings": {
      "type": "object",
      "properties": {
        "enabled": {
          "type": "boolean",
          "default": true
        },
        "log_level": {
          "type": "string",
          "enum": [
            "debug",
            "info",
            "warn",
            "error"
          ]
        }
      }
    }
  },
  "required": [
    "skill"
  ]
}

================================================
FILE: skills\java-maven-gradle\references\GUIDE.md
================================================
# Java Maven Gradle Guide

## Overview

This guide provides comprehensive documentation for the **java-maven-gradle** skill in the custom-plugin-java plugin.

## Category: General

## Quick Start

### Prerequisites

- Familiarity with general concepts
- Development environment set up
- Plugin installed and configured

### Basic Usage

```bash
# Invoke the skill
claude "java-maven-gradle - [your task description]"

# Example
claude "java-maven-gradle - analyze the current implementation"
```

## Core Concepts

### Key Principles

1. **Consistency** - Follow established patterns
2. **Clarity** - Write readable, maintainable code
3. **Quality** - Validate before deployment

### Best Practices

- Always validate input data
- Handle edge cases explicitly
- Document your decisions
- Write tests for critical paths

## Common Tasks

### Task 1: Basic Implementation

```python
# Example implementation pattern
def implement_java_maven_gradle(input_data):
    """
    Implement java-maven-gradle functionality.

    Args:
        input_data: Input to process

    Returns:
        Processed result
    """
    # Validate input
    if not input_data:
        raise ValueError("Input required")

    # Process
    result = process(input_data)

    # Return
    return result
```

### Task 2: Advanced Usage

For advanced scenarios, consider:

- Configuration customization via `assets/config.yaml`
- Validation using `scripts/validate.py`
- Integration with other skills

## Troubleshooting

### Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Skill not found | Not installed | Run plugin sync |
| Validation fails | Invalid config | Check config.yaml |
| Unexpected output | Missing context | Provide more details |

## Related Resources

- SKILL.md - Skill specification
- config.yaml - Configuration options
- validate.py - Validation script

---

*Last updated: 2025-12-30*


================================================
FILE: skills\java-maven-gradle\references\PATTERNS.md
================================================
# Java Maven Gradle Patterns

## Design Patterns

### Pattern 1: Input Validation

Always validate input before processing:

```python
def validate_input(data):
    if data is None:
        raise ValueError("Data cannot be None")
    if not isinstance(data, dict):
        raise TypeError("Data must be a dictionary")
    return True
```

### Pattern 2: Error Handling

Use consistent error handling:

```python
try:
    result = risky_operation()
except SpecificError as e:
    logger.error(f"Operation failed: {e}")
    handle_error(e)
except Exception as e:
    logger.exception("Unexpected error")
    raise
```

### Pattern 3: Configuration Loading

Load and validate configuration:

```python
import yaml

def load_config(config_path):
    with open(config_path) as f:
        config = yaml.safe_load(f)
    validate_config(config)
    return config
```

## Anti-Patterns to Avoid

### ❌ Don't: Swallow Exceptions

```python
# BAD
try:
    do_something()
except:
    pass
```

### ✅ Do: Handle Explicitly

```python
# GOOD
try:
    do_something()
except SpecificError as e:
    logger.warning(f"Expected error: {e}")
    return default_value
```

## Category-Specific Patterns: General

### Recommended Approach

1. Start with the simplest implementation
2. Add complexity only when needed
3. Test each addition
4. Document decisions

### Common Integration Points

- Configuration: `assets/config.yaml`
- Validation: `scripts/validate.py`
- Documentation: `references/GUIDE.md`

---

*Pattern library for java-maven-gradle skill*


================================================
FILE: skills\java-maven-gradle\scripts\validate.py
================================================
#!/usr/bin/env python3
"""
Validation script for java-maven-gradle skill.
Category: general
"""

import os
import sys
import yaml
import json
from pathlib import Path


def validate_config(config_path: str) -> dict:
    """
    Validate skill configuration file.

    Args:
        config_path: Path to config.yaml

    Returns:
        dict: Validation result with 'valid' and 'errors' keys
    """
    errors = []

    if not os.path.exists(config_path):
        return {"valid": False, "errors": ["Config file not found"]}

    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
    except yaml.YAMLError as e:
        return {"valid": False, "errors": [f"YAML parse error: {e}"]}

    # Validate required fields
    if 'skill' not in config:
        errors.append("Missing 'skill' section")
    else:
        if 'name' not in config['skill']:
            errors.append("Missing skill.name")
        if 'version' not in config['skill']:
            errors.append("Missing skill.version")

    # Validate settings
    if 'settings' in config:
        settings = config['settings']
        if 'log_level' in settings:
            valid_levels = ['debug', 'info', 'warn', 'error']
            if settings['log_level'] not in valid_levels:
                errors.append(f"Invalid log_level: {settings['log_level']}")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "config": config if not errors else None
    }


def validate_skill_structure(skill_path: str) -> dict:
    """
    Validate skill directory structure.

    Args:
        skill_path: Path to skill directory

    Returns:
        dict: Structure validation result
    """
    required_dirs = ['assets', 'scripts', 'references']
    required_files = ['SKILL.md']

    errors = []

    # Check required files
    for file in required_files:
        if not os.path.exists(os.path.join(skill_path, file)):
            errors.append(f"Missing required file: {file}")

    # Check required directories
    for dir in required_dirs:
        dir_path = os.path.join(skill_path, dir)
        if not os.path.isdir(dir_path):
            errors.append(f"Missing required directory: {dir}/")
        else:
            # Check for real content (not just .gitkeep)
            files = [f for f in os.listdir(dir_path) if f != '.gitkeep']
            if not files:
                errors.append(f"Directory {dir}/ has no real content")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "skill_name": os.path.basename(skill_path)
    }


def main():
    """Main validation entry point."""
    skill_path = Path(__file__).parent.parent

    print(f"Validating java-maven-gradle skill...")
    print(f"Path: {skill_path}")

    # Validate structure
    structure_result = validate_skill_structure(str(skill_path))
    print(f"\nStructure validation: {'PASS' if structure_result['valid'] else 'FAIL'}")
    if structure_result['errors']:
        for error in structure_result['errors']:
            print(f"  - {error}")

    # Validate config
    config_path = skill_path / 'assets' / 'config.yaml'
    if config_path.exists():
        config_result = validate_config(str(config_path))
        print(f"\nConfig validation: {'PASS' if config_result['valid'] else 'FAIL'}")
        if config_result['errors']:
            for error in config_result['errors']:
                print(f"  - {error}")
    else:
        print("\nConfig validation: SKIPPED (no config.yaml)")

    # Summary
    all_valid = structure_result['valid']
    print(f"\n==================================================")
    print(f"Overall: {'VALID' if all_valid else 'INVALID'}")

    return 0 if all_valid else 1


if __name__ == "__main__":
    sys.exit(main())


================================================
FILE: skills\java-microservices\SKILL.md
================================================
---
name: java-microservices
description: Build microservices - Spring Cloud, service mesh, event-driven, resilience patterns
sasmp_version: "1.3.0"
version: "3.0.0"
bonded_agent: 07-java-microservices
bond_type: PRIMARY_BOND
allowed-tools: Read, Write, Bash, Glob, Grep

# Parameter Validation
parameters:
  pattern:
    type: string
    enum: [saga, cqrs, event_sourcing, api_gateway]
    description: Architecture pattern
  messaging:
    type: string
    enum: [kafka, rabbitmq, redis]
    description: Messaging platform
---

# Java Microservices Skill

Build production microservices with Spring Cloud and distributed system patterns.

## Overview

This skill covers microservices architecture with Spring Cloud including service discovery, API gateway, circuit breakers, event-driven communication, and distributed tracing.

## When to Use This Skill

Use when you need to:
- Design microservices architecture
- Implement service-to-service communication
- Configure resilience patterns
- Set up event-driven messaging
- Add distributed tracing

## Topics Covered

### Spring Cloud Components
- Config Server (centralized config)
- Service Discovery (Eureka, Consul)
- API Gateway (Spring Cloud Gateway)
- Load Balancing (Spring Cloud LoadBalancer)

### Resilience Patterns
- Circuit Breaker (Resilience4j)
- Retry with backoff
- Bulkhead isolation
- Rate limiting

### Event-Driven Architecture
- Apache Kafka integration
- Spring Cloud Stream
- Saga pattern
- Event sourcing basics

### Observability
- Distributed tracing (Micrometer)
- Metrics (Prometheus)
- Log correlation

## Quick Reference

```java
// Saga with Choreography
@Component
public class OrderSagaListener {

    @KafkaListener(topics = "order.created")
    public void handleOrderCreated(OrderCreatedEvent event) {
        inventoryService.reserve(event.getItems());
    }

    @KafkaListener(topics = "payment.failed")
    public void handlePaymentFailed(PaymentFailedEvent event) {
        // Compensating transaction
        inventoryService.release(event.getOrderId());
        orderService.cancel(event.getOrderId());
    }
}

// Circuit Breaker Configuration
@Configuration
public class ResilienceConfig {

    @Bean
    public Customizer<Resilience4JCircuitBreakerFactory> cbCustomizer() {
        return factory -> factory.configureDefault(id ->
            new Resilience4JConfigBuilder(id)
                .circuitBreakerConfig(CircuitBreakerConfig.custom()
                    .failureRateThreshold(50)
                    .waitDurationInOpenState(Duration.ofSeconds(30))
                    .slidingWindowSize(10)
                    .build())
                .build());
    }
}

// API Gateway Routes
@Configuration
public class GatewayConfig {

    @Bean
    public RouteLocator routes(RouteLocatorBuilder builder) {
        return builder.routes()
            .route("orders", r -> r
                .path("/api/orders/**")
                .filters(f -> f
                    .stripPrefix(1)
                    .circuitBreaker(c -> c.setName("order-cb"))
                    .retry(retry -> retry.setRetries(3)))
                .uri("lb://order-service"))
            .build();
    }
}
```

## Observability Configuration

```yaml
management:
  tracing:
    sampling:
      probability: 1.0
  endpoints:
    web:
      exposure:
        include: health,info,metrics,prometheus

logging:
  pattern:
    level: "%5p [${spring.application.name:},%X{traceId:-},%X{spanId:-}]"
```

## Common Patterns

### Saga Pattern
```
Order → Inventory → Payment → (Success | Compensate)
```

### Circuit Breaker States
```
CLOSED → (failures exceed threshold) → OPEN
OPEN → (wait duration) → HALF_OPEN
HALF_OPEN → (success) → CLOSED
HALF_OPEN → (failure) → OPEN
```

## Troubleshooting

### Common Issues

| Problem | Cause | Solution |
|---------|-------|----------|
| Cascade failure | No circuit breaker | Add Resilience4j |
| Message lost | No ack | Enable manual ack |
| Inconsistent data | No compensation | Implement saga |
| Service not found | Discovery delay | Tune heartbeat |

### Debug Checklist
```
□ Trace request (traceId)
□ Check circuit breaker state
□ Verify Kafka consumer lag
□ Review gateway routes
□ Monitor retry counts
```

## Usage

```
Skill("java-microservices")
```

## Related Skills
- `java-spring-boot` - Spring Cloud
- `java-docker` - Containerization


================================================
FILE: skills\java-microservices\assets\schema.json
================================================
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "java-microservices Configuration Schema",
  "type": "object",
  "properties": {
    "skill": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "version": {
          "type": "string",
          "pattern": "^\\d+\\.\\d+\\.\\d+$"
        },
        "category": {
          "type": "string",
          "enum": [
            "api",
            "testing",
            "devops",
            "security",
            "database",
            "frontend",
            "algorithms",
            "machine-learning",
            "cloud",
            "containers",
            "general"
          ]
        }
      },
      "required": [
        "name",
        "version"
      ]
    },
    "settings": {
      "type": "object",
      "properties": {
        "enabled": {
          "type": "boolean",
          "default": true
        },
        "log_level": {
          "type": "string",
          "enum": [
            "debug",
            "info",
            "warn",
            "error"
          ]
        }
      }
    }
  },
  "required": [
    "skill"
  ]
}

================================================
FILE: skills\java-microservices\references\GUIDE.md
================================================
# Java Microservices Guide

## Overview

This guide provides comprehensive documentation for the **java-microservices** skill in the custom-plugin-java plugin.

## Category: General

## Quick Start

### Prerequisites

- Familiarity with general concepts
- Development environment set up
- Plugin installed and configured

### Basic Usage

```bash
# Invoke the skill
claude "java-microservices - [your task description]"

# Example
claude "java-microservices - analyze the current implementation"
```

## Core Concepts

### Key Principles

1. **Consistency** - Follow established patterns
2. **Clarity** - Write readable, maintainable code
3. **Quality** - Validate before deployment

### Best Practices

- Always validate input data
- Handle edge cases explicitly
- Document your decisions
- Write tests for critical paths

## Common Tasks

### Task 1: Basic Implementation

```python
# Example implementation pattern
def implement_java_microservices(input_data):
    """
    Implement java-microservices functionality.

    Args:
        input_data: Input to process

    Returns:
        Processed result
    """
    # Validate input
    if not input_data:
        raise ValueError("Input required")

    # Process
    result = process(input_data)

    # Return
    return result
```

### Task 2: Advanced Usage

For advanced scenarios, consider:

- Configuration customization via `assets/config.yaml`
- Validation using `scripts/validate.py`
- Integration with other skills

## Troubleshooting

### Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Skill not found | Not installed | Run plugin sync |
| Validation fails | Invalid config | Check config.yaml |
| Unexpected output | Missing context | Provide more details |

## Related Resources

- SKILL.md - Skill specification
- config.yaml - Configuration options
- validate.py - Validation script

---

*Last updated: 2025-12-30*


================================================
FILE: skills\java-microservices\references\PATTERNS.md
================================================
# Java Microservices Patterns

## Design Patterns

### Pattern 1: Input Validation

Always validate input before processing:

```python
def validate_input(data):
    if data is None:
        raise ValueError("Data cannot be None")
    if not isinstance(data, dict):
        raise TypeError("Data must be a dictionary")
    return True
```

### Pattern 2: Error Handling

Use consistent error handling:

```python
try:
    result = risky_operation()
except SpecificError as e:
    logger.error(f"Operation failed: {e}")
    handle_error(e)
except Exception as e:
    logger.exception("Unexpected error")
    raise
```

### Pattern 3: Configuration Loading

Load and validate configuration:

```python
import yaml

def load_config(config_path):
    with open(config_path) as f:
        config = yaml.safe_load(f)
    validate_config(config)
    return config
```

## Anti-Patterns to Avoid

### ❌ Don't: Swallow Exceptions

```python
# BAD
try:
    do_something()
except:
    pass
```

### ✅ Do: Handle Explicitly

```python
# GOOD
try:
    do_something()
except SpecificError as e:
    logger.warning(f"Expected error: {e}")
    return default_value
```

## Category-Specific Patterns: General

### Recommended Approach

1. Start with the simplest implementation
2. Add complexity only when needed
3. Test each addition
4. Document decisions

### Common Integration Points

- Configuration: `assets/config.yaml`
- Validation: `scripts/validate.py`
- Documentation: `references/GUIDE.md`

---

*Pattern library for java-microservices skill*


================================================
FILE: skills\java-microservices\scripts\validate.py
================================================
#!/usr/bin/env python3
"""
Validation script for java-microservices skill.
Category: general
"""

import os
import sys
import yaml
import json
from pathlib import Path


def validate_config(config_path: str) -> dict:
    """
    Validate skill configuration file.

    Args:
        config_path: Path to config.yaml

    Returns:
        dict: Validation result with 'valid' and 'errors' keys
    """
    errors = []

    if not os.path.exists(config_path):
        return {"valid": False, "errors": ["Config file not found"]}

    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
    except yaml.YAMLError as e:
        return {"valid": False, "errors": [f"YAML parse error: {e}"]}

    # Validate required fields
    if 'skill' not in config:
        errors.append("Missing 'skill' section")
    else:
        if 'name' not in config['skill']:
            errors.append("Missing skill.name")
        if 'version' not in config['skill']:
            errors.append("Missing skill.version")

    # Validate settings
    if 'settings' in config:
        settings = config['settings']
        if 'log_level' in settings:
            valid_levels = ['debug', 'info', 'warn', 'error']
            if settings['log_level'] not in valid_levels:
                errors.append(f"Invalid log_level: {settings['log_level']}")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "config": config if not errors else None
    }


def validate_skill_structure(skill_path: str) -> dict:
    """
    Validate skill directory structure.

    Args:
        skill_path: Path to skill directory

    Returns:
        dict: Structure validation result
    """
    required_dirs = ['assets', 'scripts', 'references']
    required_files = ['SKILL.md']

    errors = []

    # Check required files
    for file in required_files:
        if not os.path.exists(os.path.join(skill_path, file)):
            errors.append(f"Missing required file: {file}")

    # Check required directories
    for dir in required_dirs:
        dir_path = os.path.join(skill_path, dir)
        if not os.path.isdir(dir_path):
            errors.append(f"Missing required directory: {dir}/")
        else:
            # Check for real content (not just .gitkeep)
            files = [f for f in os.listdir(dir_path) if f != '.gitkeep']
            if not files:
                errors.append(f"Directory {dir}/ has no real content")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "skill_name": os.path.basename(skill_path)
    }


def main():
    """Main validation entry point."""
    skill_path = Path(__file__).parent.parent

    print(f"Validating java-microservices skill...")
    print(f"Path: {skill_path}")

    # Validate structure
    structure_result = validate_skill_structure(str(skill_path))
    print(f"\nStructure validation: {'PASS' if structure_result['valid'] else 'FAIL'}")
    if structure_result['errors']:
        for error in structure_result['errors']:
            print(f"  - {error}")

    # Validate config
    config_path = skill_path / 'assets' / 'config.yaml'
    if config_path.exists():
        config_result = validate_config(str(config_path))
        print(f"\nConfig validation: {'PASS' if config_result['valid'] else 'FAIL'}")
        if config_result['errors']:
            for error in config_result['errors']:
                print(f"  - {error}")
    else:
        print("\nConfig validation: SKIPPED (no config.yaml)")

    # Summary
    all_valid = structure_result['valid']
    print(f"\n==================================================")
    print(f"Overall: {'VALID' if all_valid else 'INVALID'}")

    return 0 if all_valid else 1


if __name__ == "__main__":
    sys.exit(main())


================================================
FILE: skills\java-performance\SKILL.md
================================================
---
name: java-performance
description: JVM performance tuning - GC optimization, profiling, memory analysis, benchmarking
sasmp_version: "1.3.0"
version: "3.0.0"
bonded_agent: 02-java-advanced
bond_type: SECONDARY_BOND
allowed-tools: Read, Write, Bash, Glob, Grep

# Parameter Validation
parameters:
  focus:
    type: string
    enum: [gc, memory, cpu, profiling]
    description: Performance focus area
---

# Java Performance Skill

Optimize JVM performance through profiling, GC tuning, and memory analysis.

## Overview

This skill covers JVM performance optimization including garbage collection tuning, memory analysis, CPU profiling, and benchmarking with JMH.

## When to Use This Skill

Use when you need to:
- Tune GC for low latency or throughput
- Profile CPU hotspots
- Analyze memory leaks
- Benchmark code performance
- Optimize container settings

## Quick Reference

### GC Presets

```bash
# High-throughput
-XX:+UseG1GC
-XX:MaxGCPauseMillis=200
-Xms4g -Xmx4g
-XX:+AlwaysPreTouch

# Low-latency
-XX:+UseZGC
-XX:+ZGenerational
-Xms8g -Xmx8g

# Memory-constrained
-XX:+UseSerialGC
-Xms512m -Xmx512m
-XX:+UseCompressedOops

# Container-optimized
-XX:+UseContainerSupport
-XX:MaxRAMPercentage=75.0
-XX:+ExitOnOutOfMemoryError
```

### Profiling Commands

```bash
# Thread dump
jstack -l <pid> > threaddump.txt

# Heap dump
jmap -dump:format=b,file=heap.hprof <pid>

# GC analysis
jstat -gcutil <pid> 1000 10

# Flight recording
jcmd <pid> JFR.start duration=60s filename=app.jfr

# Async profiler
./profiler.sh -d 30 -f profile.html <pid>
```

### JMH Benchmark

```java
@BenchmarkMode(Mode.Throughput)
@Warmup(iterations = 3, time = 1)
@Measurement(iterations = 5, time = 1)
@State(Scope.Benchmark)
public class MyBenchmark {

    @Benchmark
    public void testMethod(Blackhole bh) {
        bh.consume(compute());
    }
}
```

## GC Comparison

| GC | Latency | Throughput | Heap Size |
|----|---------|------------|-----------|
| G1 | Medium | High | 4-32GB |
| ZGC | Very Low | Medium | 8GB-16TB |
| Shenandoah | Very Low | Medium | 8GB+ |
| Parallel | High | Very High | Any |

## Troubleshooting

| Problem | Cause | Solution |
|---------|-------|----------|
| GC thrashing | Heap too small | Increase heap |
| High latency | GC pauses | Switch to ZGC |
| Memory leak | Object retention | Heap dump + MAT |
| CPU spikes | Hot loops | Profile + optimize |

## Usage

```
Skill("java-performance")
```


================================================
FILE: skills\java-performance\assets\schema.json
================================================
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "java-performance Configuration Schema",
  "type": "object",
  "properties": {
    "skill": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "version": {
          "type": "string",
          "pattern": "^\\d+\\.\\d+\\.\\d+$"
        },
        "category": {
          "type": "string",
          "enum": [
            "api",
            "testing",
            "devops",
            "security",
            "database",
            "frontend",
            "algorithms",
            "machine-learning",
            "cloud",
            "containers",
            "general"
          ]
        }
      },
      "required": [
        "name",
        "version"
      ]
    },
    "settings": {
      "type": "object",
      "properties": {
        "enabled": {
          "type": "boolean",
          "default": true
        },
        "log_level": {
          "type": "string",
          "enum": [
            "debug",
            "info",
            "warn",
            "error"
          ]
        }
      }
    }
  },
  "required": [
    "skill"
  ]
}

================================================
FILE: skills\java-performance\references\GUIDE.md
================================================
# Java Performance Guide

## Overview

This guide provides comprehensive documentation for the **java-performance** skill in the custom-plugin-java plugin.

## Category: Database

## Quick Start

### Prerequisites

- Familiarity with database concepts
- Development environment set up
- Plugin installed and configured

### Basic Usage

```bash
# Invoke the skill
claude "java-performance - [your task description]"

# Example
claude "java-performance - analyze the current implementation"
```

## Core Concepts

### Key Principles

1. **Consistency** - Follow established patterns
2. **Clarity** - Write readable, maintainable code
3. **Quality** - Validate before deployment

### Best Practices

- Always validate input data
- Handle edge cases explicitly
- Document your decisions
- Write tests for critical paths

## Common Tasks

### Task 1: Basic Implementation

```python
# Example implementation pattern
def implement_java_performance(input_data):
    """
    Implement java-performance functionality.

    Args:
        input_data: Input to process

    Returns:
        Processed result
    """
    # Validate input
    if not input_data:
        raise ValueError("Input required")

    # Process
    result = process(input_data)

    # Return
    return result
```

### Task 2: Advanced Usage

For advanced scenarios, consider:

- Configuration customization via `assets/config.yaml`
- Validation using `scripts/validate.py`
- Integration with other skills

## Troubleshooting

### Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Skill not found | Not installed | Run plugin sync |
| Validation fails | Invalid config | Check config.yaml |
| Unexpected output | Missing context | Provide more details |

## Related Resources

- SKILL.md - Skill specification
- config.yaml - Configuration options
- validate.py - Validation script

---

*Last updated: 2025-12-30*


================================================
FILE: skills\java-performance\references\PATTERNS.md
================================================
# Java Performance Patterns

## Design Patterns

### Pattern 1: Input Validation

Always validate input before processing:

```python
def validate_input(data):
    if data is None:
        raise ValueError("Data cannot be None")
    if not isinstance(data, dict):
        raise TypeError("Data must be a dictionary")
    return True
```

### Pattern 2: Error Handling

Use consistent error handling:

```python
try:
    result = risky_operation()
except SpecificError as e:
    logger.error(f"Operation failed: {e}")
    handle_error(e)
except Exception as e:
    logger.exception("Unexpected error")
    raise
```

### Pattern 3: Configuration Loading

Load and validate configuration:

```python
import yaml

def load_config(config_path):
    with open(config_path) as f:
        config = yaml.safe_load(f)
    validate_config(config)
    return config
```

## Anti-Patterns to Avoid

### ❌ Don't: Swallow Exceptions

```python
# BAD
try:
    do_something()
except:
    pass
```

### ✅ Do: Handle Explicitly

```python
# GOOD
try:
    do_something()
except SpecificError as e:
    logger.warning(f"Expected error: {e}")
    return default_value
```

## Category-Specific Patterns: Database

### Recommended Approach

1. Start with the simplest implementation
2. Add complexity only when needed
3. Test each addition
4. Document decisions

### Common Integration Points

- Configuration: `assets/config.yaml`
- Validation: `scripts/validate.py`
- Documentation: `references/GUIDE.md`

---

*Pattern library for java-performance skill*


================================================
FILE: skills\java-performance\scripts\validate.py
================================================
#!/usr/bin/env python3
"""
Validation script for java-performance skill.
Category: database
"""

import os
import sys
import yaml
import json
from pathlib import Path


def validate_config(config_path: str) -> dict:
    """
    Validate skill configuration file.

    Args:
        config_path: Path to config.yaml

    Returns:
        dict: Validation result with 'valid' and 'errors' keys
    """
    errors = []

    if not os.path.exists(config_path):
        return {"valid": False, "errors": ["Config file not found"]}

    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
    except yaml.YAMLError as e:
        return {"valid": False, "errors": [f"YAML parse error: {e}"]}

    # Validate required fields
    if 'skill' not in config:
        errors.append("Missing 'skill' section")
    else:
        if 'name' not in config['skill']:
            errors.append("Missing skill.name")
        if 'version' not in config['skill']:
            errors.append("Missing skill.version")

    # Validate settings
    if 'settings' in config:
        settings = config['settings']
        if 'log_level' in settings:
            valid_levels = ['debug', 'info', 'warn', 'error']
            if settings['log_level'] not in valid_levels:
                errors.append(f"Invalid log_level: {settings['log_level']}")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "config": config if not errors else None
    }


def validate_skill_structure(skill_path: str) -> dict:
    """
    Validate skill directory structure.

    Args:
        skill_path: Path to skill directory

    Returns:
        dict: Structure validation result
    """
    required_dirs = ['assets', 'scripts', 'references']
    required_files = ['SKILL.md']

    errors = []

    # Check required files
    for file in required_files:
        if not os.path.exists(os.path.join(skill_path, file)):
            errors.append(f"Missing required file: {file}")

    # Check required directories
    for dir in required_dirs:
        dir_path = os.path.join(skill_path, dir)
        if not os.path.isdir(dir_path):
            errors.append(f"Missing required directory: {dir}/")
        else:
            # Check for real content (not just .gitkeep)
            files = [f for f in os.listdir(dir_path) if f != '.gitkeep']
            if not files:
                errors.append(f"Directory {dir}/ has no real content")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "skill_name": os.path.basename(skill_path)
    }


def main():
    """Main validation entry point."""
    skill_path = Path(__file__).parent.parent

    print(f"Validating java-performance skill...")
    print(f"Path: {skill_path}")

    # Validate structure
    structure_result = validate_skill_structure(str(skill_path))
    print(f"\nStructure validation: {'PASS' if structure_result['valid'] else 'FAIL'}")
    if structure_result['errors']:
        for error in structure_result['errors']:
            print(f"  - {error}")

    # Validate config
    config_path = skill_path / 'assets' / 'config.yaml'
    if config_path.exists():
        config_result = validate_config(str(config_path))
        print(f"\nConfig validation: {'PASS' if config_result['valid'] else 'FAIL'}")
        if config_result['errors']:
            for error in config_result['errors']:
                print(f"  - {error}")
    else:
        print("\nConfig validation: SKIPPED (no config.yaml)")

    # Summary
    all_valid = structure_result['valid']
    print(f"\n==================================================")
    print(f"Overall: {'VALID' if all_valid else 'INVALID'}")

    return 0 if all_valid else 1


if __name__ == "__main__":
    sys.exit(main())


================================================
FILE: skills\java-spring-boot\SKILL.md
================================================
---
name: java-spring-boot
description: Build production Spring Boot applications - REST APIs, Security, Data, Actuator
sasmp_version: "1.3.0"
version: "3.0.0"
bonded_agent: 03-java-spring
bond_type: PRIMARY_BOND
allowed-tools: Read, Write, Bash, Glob, Grep

# Parameter Validation
parameters:
  spring_version:
    type: string
    default: "3.2"
    description: Spring Boot version
  module:
    type: string
    enum: [web, security, data, actuator, cloud]
    description: Spring module focus
---

# Java Spring Boot Skill

Build production-ready Spring Boot applications with modern best practices.

## Overview

This skill covers Spring Boot development including REST APIs, security configuration, data access, actuator monitoring, and cloud integration. Follows Spring Boot 3.x patterns with emphasis on production readiness.

## When to Use This Skill

Use when you need to:
- Create REST APIs with Spring MVC/WebFlux
- Configure Spring Security (OAuth2, JWT)
- Set up database access with Spring Data
- Enable monitoring with Actuator
- Integrate with Spring Cloud

## Topics Covered

### Spring Boot Core
- Auto-configuration and starters
- Application properties and profiles
- Bean lifecycle and configuration
- DevTools and hot reload

### REST API Development
- @RestController and @RequestMapping
- Request/response handling
- Validation with Bean Validation
- Exception handling with @ControllerAdvice

### Spring Security
- SecurityFilterChain configuration
- OAuth2 and JWT authentication
- Method security (@PreAuthorize)
- CORS and CSRF configuration

### Spring Data JPA
- Repository pattern
- Query methods and @Query
- Pagination and sorting
- Auditing and transactions

### Actuator & Monitoring
- Health checks and probes
- Metrics with Micrometer
- Custom endpoints
- Prometheus integration

## Quick Reference

```java
// REST Controller
@RestController
@RequestMapping("/api/users")
@Validated
public class UserController {

    @GetMapping("/{id}")
    public ResponseEntity<User> getUser(@PathVariable Long id) {
        return userService.findById(id)
            .map(ResponseEntity::ok)
            .orElse(ResponseEntity.notFound().build());
    }

    @PostMapping
    public ResponseEntity<User> createUser(@Valid @RequestBody UserRequest request) {
        User user = userService.create(request);
        URI location = URI.create("/api/users/" + user.getId());
        return ResponseEntity.created(location).body(user);
    }
}

// Security Configuration
@Configuration
@EnableWebSecurity
public class SecurityConfig {

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        return http
            .csrf(csrf -> csrf.disable())
            .sessionManagement(s -> s.sessionCreationPolicy(STATELESS))
            .authorizeHttpRequests(auth -> auth
                .requestMatchers("/actuator/health/**").permitAll()
                .requestMatchers("/api/public/**").permitAll()
                .anyRequest().authenticated())
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(Customizer.withDefaults()))
            .build();
    }
}

// Exception Handler
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(EntityNotFoundException.class)
    public ProblemDetail handleNotFound(EntityNotFoundException ex) {
        return ProblemDetail.forStatusAndDetail(NOT_FOUND, ex.getMessage());
    }
}
```

## Configuration Templates

```yaml
# application.yml
spring:
  application:
    name: ${APP_NAME:my-service}
  profiles:
    active: ${SPRING_PROFILES_ACTIVE:local}
  jpa:
    open-in-view: false
    properties:
      hibernate:
        jdbc.batch_size: 50

management:
  endpoints:
    web:
      exposure:
        include: health,info,metrics,prometheus
  endpoint:
    health:
      probes:
        enabled: true

server:
  error:
    include-stacktrace: never
```

## Common Patterns

### Layer Architecture
```
Controller → Service → Repository → Database
     ↓           ↓          ↓
   DTOs      Entities    Entities
```

### Validation Patterns
```java
public record CreateUserRequest(
    @NotBlank @Size(max = 100) String name,
    @Email @NotBlank String email,
    @NotNull @Min(18) Integer age
) {}
```

## Troubleshooting

### Common Issues

| Problem | Cause | Solution |
|---------|-------|----------|
| Bean not found | Missing @Component | Add annotation or @Bean |
| Circular dependency | Constructor injection | Use @Lazy or refactor |
| 401 Unauthorized | Security config | Check permitAll paths |
| Slow startup | Heavy auto-config | Exclude unused starters |

### Debug Properties
```properties
debug=true
logging.level.org.springframework.security=DEBUG
spring.jpa.show-sql=true
```

### Debug Checklist
```
□ Check /actuator/conditions
□ Verify active profiles
□ Review security filter chain
□ Check bean definitions
□ Test health endpoints
```

## Usage

```
Skill("java-spring-boot")
```

## Related Skills
- `java-testing` - Spring test patterns
- 

================================================
FILE: skills\java-spring-boot\assets\schema.json
================================================
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "java-spring-boot Configuration Schema",
  "type": "object",
  "properties": {
    "skill": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "version": {
          "type": "string",
          "pattern": "^\\d+\\.\\d+\\.\\d+$"
        },
        "category": {
          "type": "string",
          "enum": [
            "api",
            "testing",
            "devops",
            "security",
            "database",
            "frontend",
            "algorithms",
            "machine-learning",
            "cloud",
            "containers",
            "general"
          ]
        }
      },
      "required": [
        "name",
        "version"
      ]
    },
    "settings": {
      "type": "object",
      "properties": {
        "enabled": {
          "type": "boolean",
          "default": true
        },
        "log_level": {
          "type": "string",
          "enum": [
            "debug",
            "info",
            "warn",
            "error"
          ]
        }
      }
    }
  },
  "required": [
    "skill"
  ]
}

================================================
FILE: skills\java-spring-boot\references\GUIDE.md
================================================
# Java Spring Boot Guide

## Overview

This guide provides comprehensive documentation for the **java-spring-boot** skill in the custom-plugin-java plugin.

## Category: General

## Quick Start

### Prerequisites

- Familiarity with general concepts
- Development environment set up
- Plugin installed and configured

### Basic Usage

```bash
# Invoke the skill
claude "java-spring-boot - [your task description]"

# Example
claude "java-spring-boot - analyze the current implementation"
```

## Core Concepts

### Key Principles

1. **Consistency** - Follow established patterns
2. **Clarity** - Write readable, maintainable code
3. **Quality** - Validate before deployment

### Best Practices

- Always validate input data
- Handle edge cases explicitly
- Document your decisions
- Write tests for critical paths

## Common Tasks

### Task 1: Basic Implementation

```python
# Example implementation pattern
def implement_java_spring_boot(input_data):
    """
    Implement java-spring-boot functionality.

    Args:
        input_data: Input to process

    Returns:
        Processed result
    """
    # Validate input
    if not input_data:
        raise ValueError("Input required")

    # Process
    result = process(input_data)

    # Return
    return result
```

### Task 2: Advanced Usage

For advanced scenarios, consider:

- Configuration customization via `assets/config.yaml`
- Validation using `scripts/validate.py`
- Integration with other skills

## Troubleshooting

### Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Skill not found | Not installed | Run plugin sync |
| Validation fails | Invalid config | Check config.yaml |
| Unexpected output | Missing context | Provide more details |

## Related Resources

- SKILL.md - Skill specification
- config.yaml - Configuration options
- validate.py - Validation script

---

*Last updated: 2025-12-30*


================================================
FILE: skills\java-spring-boot\references\PATTERNS.md
================================================
# Java Spring Boot Patterns

## Design Patterns

### Pattern 1: Input Validation

Always validate input before processing:

```python
def validate_input(data):
    if data is None:
        raise ValueError("Data cannot be None")
    if not isinstance(data, dict):
        raise TypeError("Data must be a dictionary")
    return True
```

### Pattern 2: Error Handling

Use consistent error handling:

```python
try:
    result = risky_operation()
except SpecificError as e:
    logger.error(f"Operation failed: {e}")
    handle_error(e)
except Exception as e:
    logger.exception("Unexpected error")
    raise
```

### Pattern 3: Configuration Loading

Load and validate configuration:

```python
import yaml

def load_config(config_path):
    with open(config_path) as f:
        config = yaml.safe_load(f)
    validate_config(config)
    return config
```

## Anti-Patterns to Avoid

### ❌ Don't: Swallow Exceptions

```python
# BAD
try:
    do_something()
except:
    pass
```

### ✅ Do: Handle Explicitly

```python
# GOOD
try:
    do_something()
except SpecificError as e:
    logger.warning(f"Expected error: {e}")
    return default_value
```

## Category-Specific Patterns: General

### Recommended Approach

1. Start with the simplest implementation
2. Add complexity only when needed
3. Test each addition
4. Document decisions

### Common Integration Points

- Configuration: `assets/config.yaml`
- Validation: `scripts/validate.py`
- Documentation: `references/GUIDE.md`

---

*Pattern library for java-spring-boot skill*


================================================
FILE: skills\java-spring-boot\scripts\validate.py
================================================
#!/usr/bin/env python3
"""
Validation script for java-spring-boot skill.
Category: general
"""

import os
import sys
import yaml
import json
from pathlib import Path


def validate_config(config_path: str) -> dict:
    """
    Validate skill configuration file.

    Args:
        config_path: Path to config.yaml

    Returns:
        dict: Validation result with 'valid' and 'errors' keys
    """
    errors = []

    if not os.path.exists(config_path):
        return {"valid": False, "errors": ["Config file not found"]}

    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
    except yaml.YAMLError as e:
        return {"valid": False, "errors": [f"YAML parse error: {e}"]}

    # Validate required fields
    if 'skill' not in config:
        errors.append("Missing 'skill' section")
    else:
        if 'name' not in config['skill']:
            errors.append("Missing skill.name")
        if 'version' not in config['skill']:
            errors.append("Missing skill.version")

    # Validate settings
    if 'settings' in config:
        settings = config['settings']
        if 'log_level' in settings:
            valid_levels = ['debug', 'info', 'warn', 'error']
            if settings['log_level'] not in valid_levels:
                errors.append(f"Invalid log_level: {settings['log_level']}")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "config": config if not errors else None
    }


def validate_skill_structure(skill_path: str) -> dict:
    """
    Validate skill directory structure.

    Args:
        skill_path: Path to skill directory

    Returns:
        dict: Structure validation result
    """
    required_dirs = ['assets', 'scripts', 'references']
    required_files = ['SKILL.md']

    errors = []

    # Check required files
    for file in required_files:
        if not os.path.exists(os.path.join(skill_path, file)):
            errors.append(f"Missing required file: {file}")

    # Check required directories
    for dir in required_dirs:
        dir_path = os.path.join(skill_path, dir)
        if not os.path.isdir(dir_path):
            errors.append(f"Missing required directory: {dir}/")
        else:
            # Check for real content (not just .gitkeep)
            files = [f for f in os.listdir(dir_path) if f != '.gitkeep']
            if not files:
                errors.append(f"Directory {dir}/ has no real content")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "skill_name": os.path.basename(skill_path)
    }


def main():
    """Main validation entry point."""
    skill_path = Path(__file__).parent.parent

    print(f"Validating java-spring-boot skill...")
    print(f"Path: {skill_path}")

    # Validate structure
    structure_result = validate_skill_structure(str(skill_path))
    print(f"\nStructure validation: {'PASS' if structure_result['valid'] else 'FAIL'}")
    if structure_result['errors']:
        for error in structure_result['errors']:
            print(f"  - {error}")

    # Validate config
    config_path = skill_path / 'assets' / 'config.yaml'
    if config_path.exists():
        config_result = validate_config(str(config_path))
        print(f"\nConfig validation: {'PASS' if config_result['valid'] else 'FAIL'}")
        if config_result['errors']:
            for error in config_result['errors']:
                print(f"  - {error}")
    else:
        print("\nConfig validation: SKIPPED (no config.yaml)")

    # Summary
    all_valid = structure_result['valid']
    print(f"\n==================================================")
    print(f"Overall: {'VALID' if all_valid else 'INVALID'}")

    return 0 if all_valid else 1


if __name__ == "__main__":
    sys.exit(main())


================================================
FILE: skills\java-testing\SKILL.md
================================================
---
name: java-testing
description: Test Java applications - JUnit 5, Mockito, integration testing, TDD patterns
sasmp_version: "1.3.0"
version: "3.0.0"
bonded_agent: 04-java-testing
bond_type: PRIMARY_BOND
allowed-tools: Read, Write, Bash, Glob, Grep

# Parameter Validation
parameters:
  test_type:
    type: string
    enum: [unit, integration, e2e, contract]
    description: Type of test to create
  framework:
    type: string
    default: junit5
    enum: [junit5, testng]
    description: Testing framework
---

# Java Testing Skill

Write comprehensive tests for Java applications with modern testing practices.

## Overview

This skill covers Java testing with JUnit 5, Mockito, AssertJ, and integration testing with Spring Boot Test and Testcontainers. Includes TDD patterns and test coverage strategies.

## When to Use This Skill

Use when you need to:
- Write unit tests with JUnit 5
- Create mocks with Mockito
- Build integration tests with Testcontainers
- Implement TDD/BDD practices
- Improve test coverage

## Topics Covered

### JUnit 5
- @Test, @Nested, @DisplayName
- @ParameterizedTest with sources
- Lifecycle annotations
- Extensions and custom annotations

### Mockito
- @Mock, @InjectMocks, @Spy
- Stubbing (when/thenReturn)
- Verification (verify, times)
- BDD style (given/willReturn)

### AssertJ
- Fluent assertions
- Collection assertions
- Exception assertions
- Custom assertions

### Integration Testing
- @SpringBootTest slices
- Testcontainers setup
- MockMvc for APIs
- Database testing

## Quick Reference

```java
// Unit Test with Mockito
@ExtendWith(MockitoExtension.class)
class UserServiceTest {

    @Mock
    private UserRepository userRepository;

    @InjectMocks
    private UserService userService;

    @Test
    @DisplayName("Should find user by ID")
    void shouldFindUserById() {
        // Given
        User user = new User(1L, "John");
        given(userRepository.findById(1L)).willReturn(Optional.of(user));

        // When
        Optional<User> result = userService.findById(1L);

        // Then
        assertThat(result)
            .isPresent()
            .hasValueSatisfying(u ->
                assertThat(u.getName()).isEqualTo("John"));
        then(userRepository).should().findById(1L);
    }
}

// Parameterized Test
@ParameterizedTest
@CsvSource({
    "valid@email.com, true",
    "invalid-email, false",
    "'', false"
})
void shouldValidateEmail(String email, boolean expected) {
    assertThat(validator.isValid(email)).isEqualTo(expected);
}

// Integration Test with Testcontainers
@Testcontainers
@SpringBootTest
class OrderRepositoryIT {

    @Container
    static PostgreSQLContainer<?> postgres =
        new PostgreSQLContainer<>("postgres:15");

    @DynamicPropertySource
    static void configure(DynamicPropertyRegistry registry) {
        registry.add("spring.datasource.url", postgres::getJdbcUrl);
        registry.add("spring.datasource.username", postgres::getUsername);
        registry.add("spring.datasource.password", postgres::getPassword);
    }

    @Autowired
    private OrderRepository repository;

    @Test
    void shouldPersistOrder() {
        Order saved = repository.save(new Order("item", 100.0));
        assertThat(saved.getId()).isNotNull();
    }
}

// API Test with MockMvc
@WebMvcTest(UserController.class)
class UserControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @MockBean
    private UserService userService;

    @Test
    void shouldReturnUser() throws Exception {
        given(userService.findById(1L))
            .willReturn(Optional.of(new User(1L, "John")));

        mockMvc.perform(get("/api/users/1"))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.name").value("John"));
    }
}
```

## Test Data Builders

```java
public class UserTestBuilder {
    private Long id = 1L;
    private String name = "John Doe";
    private String email = "john@example.com";
    private boolean active = true;

    public static UserTestBuilder aUser() {
        return new UserTestBuilder();
    }

    public UserTestBuilder withName(String name) {
        this.name = name;
        return this;
    }

    public UserTestBuilder inactive() {
        this.active = false;
        return this;
    }

    public User build() {
        return new User(id, name, email, active);
    }
}

// Usage
User user = aUser().withName("Jane").inactive().build();
```

## Coverage Goals

```xml
<!-- JaCoCo configuration -->
<configuration>
    <rules>
        <rule>
            <element>BUNDLE</element>
            <limits>
                <limit>
                    <counter>LINE</counter>
                    <value>COVEREDRATIO</value>
                    <minimum>0.80</minimum>
                </limit>
            </limits>
        </rule>
    </rules>
</configuration>
```

## Troubleshooting

### Common Issues

| Problem | Cause | Solution |
|---------|-------|----------|
| Mock not working | Missing @ExtendWith | Add MockitoExtens

================================================
FILE: skills\java-testing\assets\schema.json
================================================
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "java-testing Configuration Schema",
  "type": "object",
  "properties": {
    "skill": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "version": {
          "type": "string",
          "pattern": "^\\d+\\.\\d+\\.\\d+$"
        },
        "category": {
          "type": "string",
          "enum": [
            "api",
            "testing",
            "devops",
            "security",
            "database",
            "frontend",
            "algorithms",
            "machine-learning",
            "cloud",
            "containers",
            "general"
          ]
        }
      },
      "required": [
        "name",
        "version"
      ]
    },
    "settings": {
      "type": "object",
      "properties": {
        "enabled": {
          "type": "boolean",
          "default": true
        },
        "log_level": {
          "type": "string",
          "enum": [
            "debug",
            "info",
            "warn",
            "error"
          ]
        }
      }
    }
  },
  "required": [
    "skill"
  ]
}

================================================
FILE: skills\java-testing\references\GUIDE.md
================================================
# Java Testing Guide

## Overview

This guide provides comprehensive documentation for the **java-testing** skill in the custom-plugin-java plugin.

## Category: Testing

## Quick Start

### Prerequisites

- Familiarity with testing concepts
- Development environment set up
- Plugin installed and configured

### Basic Usage

```bash
# Invoke the skill
claude "java-testing - [your task description]"

# Example
claude "java-testing - analyze the current implementation"
```

## Core Concepts

### Key Principles

1. **Consistency** - Follow established patterns
2. **Clarity** - Write readable, maintainable code
3. **Quality** - Validate before deployment

### Best Practices

- Always validate input data
- Handle edge cases explicitly
- Document your decisions
- Write tests for critical paths

## Common Tasks

### Task 1: Basic Implementation

```python
# Example implementation pattern
def implement_java_testing(input_data):
    """
    Implement java-testing functionality.

    Args:
        input_data: Input to process

    Returns:
        Processed result
    """
    # Validate input
    if not input_data:
        raise ValueError("Input required")

    # Process
    result = process(input_data)

    # Return
    return result
```

### Task 2: Advanced Usage

For advanced scenarios, consider:

- Configuration customization via `assets/config.yaml`
- Validation using `scripts/validate.py`
- Integration with other skills

## Troubleshooting

### Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Skill not found | Not installed | Run plugin sync |
| Validation fails | Invalid config | Check config.yaml |
| Unexpected output | Missing context | Provide more details |

## Related Resources

- SKILL.md - Skill specification
- config.yaml - Configuration options
- validate.py - Validation script

---

*Last updated: 2025-12-30*


================================================
FILE: skills\java-testing\references\PATTERNS.md
================================================
# Java Testing Patterns

## Design Patterns

### Pattern 1: Input Validation

Always validate input before processing:

```python
def validate_input(data):
    if data is None:
        raise ValueError("Data cannot be None")
    if not isinstance(data, dict):
        raise TypeError("Data must be a dictionary")
    return True
```

### Pattern 2: Error Handling

Use consistent error handling:

```python
try:
    result = risky_operation()
except SpecificError as e:
    logger.error(f"Operation failed: {e}")
    handle_error(e)
except Exception as e:
    logger.exception("Unexpected error")
    raise
```

### Pattern 3: Configuration Loading

Load and validate configuration:

```python
import yaml

def load_config(config_path):
    with open(config_path) as f:
        config = yaml.safe_load(f)
    validate_config(config)
    return config
```

## Anti-Patterns to Avoid

### ❌ Don't: Swallow Exceptions

```python
# BAD
try:
    do_something()
except:
    pass
```

### ✅ Do: Handle Explicitly

```python
# GOOD
try:
    do_something()
except SpecificError as e:
    logger.warning(f"Expected error: {e}")
    return default_value
```

## Category-Specific Patterns: Testing

### Recommended Approach

1. Start with the simplest implementation
2. Add complexity only when needed
3. Test each addition
4. Document decisions

### Common Integration Points

- Configuration: `assets/config.yaml`
- Validation: `scripts/validate.py`
- Documentation: `references/GUIDE.md`

---

*Pattern library for java-testing skill*


================================================
FILE: skills\java-testing\scripts\validate.py
================================================
#!/usr/bin/env python3
"""
Validation script for java-testing skill.
Category: testing
"""

import os
import sys
import yaml
import json
from pathlib import Path


def validate_config(config_path: str) -> dict:
    """
    Validate skill configuration file.

    Args:
        config_path: Path to config.yaml

    Returns:
        dict: Validation result with 'valid' and 'errors' keys
    """
    errors = []

    if not os.path.exists(config_path):
        return {"valid": False, "errors": ["Config file not found"]}

    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
    except yaml.YAMLError as e:
        return {"valid": False, "errors": [f"YAML parse error: {e}"]}

    # Validate required fields
    if 'skill' not in config:
        errors.append("Missing 'skill' section")
    else:
        if 'name' not in config['skill']:
            errors.append("Missing skill.name")
        if 'version' not in config['skill']:
            errors.append("Missing skill.version")

    # Validate settings
    if 'settings' in config:
        settings = config['settings']
        if 'log_level' in settings:
            valid_levels = ['debug', 'info', 'warn', 'error']
            if settings['log_level'] not in valid_levels:
                errors.append(f"Invalid log_level: {settings['log_level']}")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "config": config if not errors else None
    }


def validate_skill_structure(skill_path: str) -> dict:
    """
    Validate skill directory structure.

    Args:
        skill_path: Path to skill directory

    Returns:
        dict: Structure validation result
    """
    required_dirs = ['assets', 'scripts', 'references']
    required_files = ['SKILL.md']

    errors = []

    # Check required files
    for file in required_files:
        if not os.path.exists(os.path.join(skill_path, file)):
            errors.append(f"Missing required file: {file}")

    # Check required directories
    for dir in required_dirs:
        dir_path = os.path.join(skill_path, dir)
        if not os.path.isdir(dir_path):
            errors.append(f"Missing required directory: {dir}/")
        else:
            # Check for real content (not just .gitkeep)
            files = [f for f in os.listdir(dir_path) if f != '.gitkeep']
            if not files:
                errors.append(f"Directory {dir}/ has no real content")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "skill_name": os.path.basename(skill_path)
    }


def main():
    """Main validation entry point."""
    skill_path = Path(__file__).parent.parent

    print(f"Validating java-testing skill...")
    print(f"Path: {skill_path}")

    # Validate structure
    structure_result = validate_skill_structure(str(skill_path))
    print(f"\nStructure validation: {'PASS' if structure_result['valid'] else 'FAIL'}")
    if structure_result['errors']:
        for error in structure_result['errors']:
            print(f"  - {error}")

    # Validate config
    config_path = skill_path / 'assets' / 'config.yaml'
    if config_path.exists():
        config_result = validate_config(str(config_path))
        print(f"\nConfig validation: {'PASS' if config_result['valid'] else 'FAIL'}")
        if config_result['errors']:
            for error in config_result['errors']:
                print(f"  - {error}")
    else:
        print("\nConfig validation: SKIPPED (no config.yaml)")

    # Summary
    all_valid = structure_result['valid']
    print(f"\n==================================================")
    print(f"Overall: {'VALID' if all_valid else 'INVALID'}")

    return 0 if all_valid else 1


if __name__ == "__main__":
    sys.exit(main())


================================================
FILE: skills\java-testing-advanced\SKILL.md
================================================
---
name: java-testing-advanced
description: Advanced testing - Testcontainers, contract testing, mutation testing, property-based
sasmp_version: "1.3.0"
version: "3.0.0"
bonded_agent: 04-java-testing
bond_type: SECONDARY_BOND
allowed-tools: Read, Write, Bash, Glob, Grep

# Parameter Validation
parameters:
  technique:
    type: string
    enum: [testcontainers, contract, mutation, property_based]
    description: Advanced testing technique
---

# Java Testing Advanced Skill

Advanced testing techniques for comprehensive test coverage.

## Overview

This skill covers advanced testing patterns including Testcontainers for integration testing, contract testing with Pact, mutation testing with PIT, and property-based testing.

## When to Use This Skill

Use when you need to:
- Test with real databases (Testcontainers)
- Verify API contracts
- Find gaps with mutation testing
- Generate test cases automatically

## Quick Reference

### Testcontainers

```java
@Testcontainers
@SpringBootTest
class OrderRepositoryIT {

    @Container
    static PostgreSQLContainer<?> postgres =
        new PostgreSQLContainer<>("postgres:15")
            .withDatabaseName("test")
            .withUsername("test")
            .withPassword("test");

    @Container
    static KafkaContainer kafka =
        new KafkaContainer(DockerImageName.parse("confluentinc/cp-kafka:7.4.0"));

    @DynamicPropertySource
    static void configure(DynamicPropertyRegistry registry) {
        registry.add("spring.datasource.url", postgres::getJdbcUrl);
        registry.add("spring.kafka.bootstrap-servers", kafka::getBootstrapServers);
    }

    @Test
    void shouldPersistOrder() {
        Order saved = repository.save(new Order("item", 100.0));
        assertThat(saved.getId()).isNotNull();
    }
}
```

### Contract Testing (Pact)

```java
@ExtendWith(PactConsumerTestExt.class)
class UserServiceContractTest {

    @Pact(consumer = "order-service", provider = "user-service")
    public RequestResponsePact createPact(PactDslWithProvider builder) {
        return builder
            .given("user exists")
            .uponReceiving("get user request")
                .path("/users/1")
                .method("GET")
            .willRespondWith()
                .status(200)
                .body(new PactDslJsonBody()
                    .integerType("id", 1)
                    .stringType("name", "John"))
            .toPact();
    }

    @Test
    @PactTestFor(pactMethod = "createPact")
    void testGetUser(MockServer mockServer) {
        User user = client.getUser(mockServer.getUrl(), 1L);
        assertThat(user.getName()).isEqualTo("John");
    }
}
```

### Mutation Testing (PIT)

```xml
<plugin>
    <groupId>org.pitest</groupId>
    <artifactId>pitest-maven</artifactId>
    <version>1.15.0</version>
    <configuration>
        <targetClasses>
            <param>com.example.service.*</param>
        </targetClasses>
        <mutationThreshold>80</mutationThreshold>
    </configuration>
</plugin>
```

### Property-Based Testing

```java
@Property
void shouldReverseListTwiceReturnsOriginal(@ForAll List<Integer> list) {
    Collections.reverse(list);
    Collections.reverse(list);
    // Original order restored
}
```

## Testing Pyramid

```
     /\        E2E Tests (few)
    /  \       Contract Tests
   /----\      Integration Tests
  /------\     Unit Tests (many)
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Container slow | Reuse containers |
| Port conflicts | Random ports |
| Flaky tests | Wait strategies |

## Usage

```
Skill("java-testing-advanced")
```


================================================
FILE: skills\java-testing-advanced\assets\schema.json
================================================
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "java-testing-advanced Configuration Schema",
  "type": "object",
  "properties": {
    "skill": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "version": {
          "type": "string",
          "pattern": "^\\d+\\.\\d+\\.\\d+$"
        },
        "category": {
          "type": "string",
          "enum": [
            "api",
            "testing",
            "devops",
            "security",
            "database",
            "frontend",
            "algorithms",
            "machine-learning",
            "cloud",
            "containers",
            "general"
          ]
        }
      },
      "required": [
        "name",
        "version"
      ]
    },
    "settings": {
      "type": "object",
      "properties": {
        "enabled": {
          "type": "boolean",
          "default": true
        },
        "log_level": {
          "type": "string",
          "enum": [
            "debug",
            "info",
            "warn",
            "error"
          ]
        }
      }
    }
  },
  "required": [
    "skill"
  ]
}

================================================
FILE: skills\java-testing-advanced\references\GUIDE.md
================================================
# Java Testing Advanced Guide

## Overview

This guide provides comprehensive documentation for the **java-testing-advanced** skill in the custom-plugin-java plugin.

## Category: Testing

## Quick Start

### Prerequisites

- Familiarity with testing concepts
- Development environment set up
- Plugin installed and configured

### Basic Usage

```bash
# Invoke the skill
claude "java-testing-advanced - [your task description]"

# Example
claude "java-testing-advanced - analyze the current implementation"
```

## Core Concepts

### Key Principles

1. **Consistency** - Follow established patterns
2. **Clarity** - Write readable, maintainable code
3. **Quality** - Validate before deployment

### Best Practices

- Always validate input data
- Handle edge cases explicitly
- Document your decisions
- Write tests for critical paths

## Common Tasks

### Task 1: Basic Implementation

```python
# Example implementation pattern
def implement_java_testing_advanced(input_data):
    """
    Implement java-testing-advanced functionality.

    Args:
        input_data: Input to process

    Returns:
        Processed result
    """
    # Validate input
    if not input_data:
        raise ValueError("Input required")

    # Process
    result = process(input_data)

    # Return
    return result
```

### Task 2: Advanced Usage

For advanced scenarios, consider:

- Configuration customization via `assets/config.yaml`
- Validation using `scripts/validate.py`
- Integration with other skills

## Troubleshooting

### Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Skill not found | Not installed | Run plugin sync |
| Validation fails | Invalid config | Check config.yaml |
| Unexpected output | Missing context | Provide more details |

## Related Resources

- SKILL.md - Skill specification
- config.yaml - Configuration options
- validate.py - Validation script

---

*Last updated: 2025-12-30*


================================================
FILE: skills\java-testing-advanced\references\PATTERNS.md
================================================
# Java Testing Advanced Patterns

## Design Patterns

### Pattern 1: Input Validation

Always validate input before processing:

```python
def validate_input(data):
    if data is None:
        raise ValueError("Data cannot be None")
    if not isinstance(data, dict):
        raise TypeError("Data must be a dictionary")
    return True
```

### Pattern 2: Error Handling

Use consistent error handling:

```python
try:
    result = risky_operation()
except SpecificError as e:
    logger.error(f"Operation failed: {e}")
    handle_error(e)
except Exception as e:
    logger.exception("Unexpected error")
    raise
```

### Pattern 3: Configuration Loading

Load and validate configuration:

```python
import yaml

def load_config(config_path):
    with open(config_path) as f:
        config = yaml.safe_load(f)
    validate_config(config)
    return config
```

## Anti-Patterns to Avoid

### ❌ Don't: Swallow Exceptions

```python
# BAD
try:
    do_something()
except:
    pass
```

### ✅ Do: Handle Explicitly

```python
# GOOD
try:
    do_something()
except SpecificError as e:
    logger.warning(f"Expected error: {e}")
    return default_value
```

## Category-Specific Patterns: Testing

### Recommended Approach

1. Start with the simplest implementation
2. Add complexity only when needed
3. Test each addition
4. Document decisions

### Common Integration Points

- Configuration: `assets/config.yaml`
- Validation: `scripts/validate.py`
- Documentation: `references/GUIDE.md`

---

*Pattern library for java-testing-advanced skill*


================================================
FILE: skills\java-testing-advanced\scripts\validate.py
================================================
#!/usr/bin/env python3
"""
Validation script for java-testing-advanced skill.
Category: testing
"""

import os
import sys
import yaml
import json
from pathlib import Path


def validate_config(config_path: str) -> dict:
    """
    Validate skill configuration file.

    Args:
        config_path: Path to config.yaml

    Returns:
        dict: Validation result with 'valid' and 'errors' keys
    """
    errors = []

    if not os.path.exists(config_path):
        return {"valid": False, "errors": ["Config file not found"]}

    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
    except yaml.YAMLError as e:
        return {"valid": False, "errors": [f"YAML parse error: {e}"]}

    # Validate required fields
    if 'skill' not in config:
        errors.append("Missing 'skill' section")
    else:
        if 'name' not in config['skill']:
            errors.append("Missing skill.name")
        if 'version' not in config['skill']:
            errors.append("Missing skill.version")

    # Validate settings
    if 'settings' in config:
        settings = config['settings']
        if 'log_level' in settings:
            valid_levels = ['debug', 'info', 'warn', 'error']
            if settings['log_level'] not in valid_levels:
                errors.append(f"Invalid log_level: {settings['log_level']}")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "config": config if not errors else None
    }


def validate_skill_structure(skill_path: str) -> dict:
    """
    Validate skill directory structure.

    Args:
        skill_path: Path to skill directory

    Returns:
        dict: Structure validation result
    """
    required_dirs = ['assets', 'scripts', 'references']
    required_files = ['SKILL.md']

    errors = []

    # Check required files
    for file in required_files:
        if not os.path.exists(os.path.join(skill_path, file)):
            errors.append(f"Missing required file: {file}")

    # Check required directories
    for dir in required_dirs:
        dir_path = os.path.join(skill_path, dir)
        if not os.path.isdir(dir_path):
            errors.append(f"Missing required directory: {dir}/")
        else:
            # Check for real content (not just .gitkeep)
            files = [f for f in os.listdir(dir_path) if f != '.gitkeep']
            if not files:
                errors.append(f"Directory {dir}/ has no real content")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "skill_name": os.path.basename(skill_path)
    }


def main():
    """Main validation entry point."""
    skill_path = Path(__file__).parent.parent

    print(f"Validating java-testing-advanced skill...")
    print(f"Path: {skill_path}")

    # Validate structure
    structure_result = validate_skill_structure(str(skill_path))
    print(f"\nStructure validation: {'PASS' if structure_result['valid'] else 'FAIL'}")
    if structure_result['errors']:
        for error in structure_result['errors']:
            print(f"  - {error}")

    # Validate config
    config_path = skill_path / 'assets' / 'config.yaml'
    if config_path.exists():
        config_result = validate_config(str(config_path))
        print(f"\nConfig validation: {'PASS' if config_result['valid'] else 'FAIL'}")
        if config_result['errors']:
            for error in config_result['errors']:
                print(f"  - {error}")
    else:
        print("\nConfig validation: SKIPPED (no config.yaml)")

    # Summary
    all_valid = structure_result['valid']
    print(f"\n==================================================")
    print(f"Overall: {'VALID' if all_valid else 'INVALID'}")

    return 0 if all_valid else 1


if __name__ == "__main__":
    sys.exit(main())

```

## File: .claude-plugin\marketplace.json
```
{
  "marketplace_id": "java-development-assistant",
  "display_name": "Java Development Assistant",
  "category": "Programming Languages",
  "tags": ["java", "spring-boot", "jvm", "maven", "gradle"],
  "visibility": "public",
  "featured": true,
  "downloads": 0,
  "rating": 0,
  "created_at": "2025-12-29",
  "updated_at": "2025-12-29",
  "source": "./",
  "sasmp_version": "1.3.0",
  "eqhm_enabled": true
}

```

## File: .claude-plugin\plugin.json
```
{
  "schema_version": "1.0.0",
  "name": "java-development-assistant",
  "version": "3.0.0",
  "description": "Production-grade Java development plugin with 8 specialized agents, 12 SASMP-compliant skills, and 4 commands for core Java, Spring, testing, DevOps, and enterprise development",
  "author": {
    "name": "Dr. Umit Kacar & Muhsin Elcicek",
    "email": "kacarumit.phd@gmail.com"
  },
  "repository": "https://github.com/pluginagentmarketplace/custom-plugin-java",
  "license": "SEE LICENSE IN LICENSE",
  "keywords": [
    "java",
    "spring-boot",
    "maven",
    "gradle",
    "jvm",
    "collections",
    "concurrency",
    "junit",
    "testing",
    "microservices",
    "docker",
    "performance"
  ],
  "agents": [
    "./agents/01-java-fundamentals.md",
    "./agents/02-java-advanced.md",
    "./agents/03-java-spring.md",
    "./agents/04-java-testing.md",
    "./agents/05-java-build-tools.md",
    "./agents/06-java-persistence.md",
    "./agents/07-java-microservices.md",
    "./agents/08-java-devops.md"
  ],
  "skills": [
    "./skills/java-fundamentals/SKILL.md",
    "./skills/java-spring-boot/SKILL.md",
    "./skills/java-testing/SKILL.md",
    "./skills/java-concurrency/SKILL.md",
    "./skills/java-jpa-hibernate/SKILL.md",
    "./skills/java-maven-gradle/SKILL.md",
    "./skills/java-microservices/SKILL.md",
    "./skills/java-maven/SKILL.md",
    "./skills/java-gradle/SKILL.md",
    "./skills/java-docker/SKILL.md",
    "./skills/java-testing-advanced/SKILL.md",
    "./skills/java-performance/SKILL.md"
  ],
  "commands": [
    "./commands/java-check.md",
    "./commands/java-new.md",
    "./commands/java-build.md",
    "./commands/java-debug.md"
  ]
}

```

## File: agents\01_java_fundamentals.md
```
---
name: 01-java-fundamentals
description: Java fundamentals expert - syntax, OOP, collections, streams, exception handling
model: sonnet
tools: Read, Write, Bash, Glob, Grep
sasmp_version: "1.3.0"
eqhm_enabled: true
skills:
  - java-fundamentals
  - java-concurrency
  - java-microservices
  - java-spring-boot
  - java-docker
  - java-performance
  - java-testing
  - java-maven-gradle
  - java-testing-advanced
  - java-jpa-hibernate
  - java-maven
  - java-gradle
triggers:
  - "java java"
  - "java"
  - "spring"
  - "java fundamentals"
version: "3.0.0"

# Input/Output Schema
input_schema:
  type: object
  properties:
    task_type:
      type: string
      enum: [code_review, implementation, refactoring, debugging, explanation]
    code_context:
      type: string
      description: Existing code or project context
    requirements:
      type: string
      description: What needs to be accomplished
  required: [task_type, requirements]

output_schema:
  type: object
  properties:
    solution:
      type: string
      description: Implemented code or explanation
    explanation:
      type: string
      description: Reasoning behind the solution
    best_practices:
      type: array
      items:
        type: string
    warnings:
      type: array
      items:
        type: string

# Cost Optimization
token_budget: 8000
max_iterations: 5
prefer_streaming: true
---

# 01 Java Fundamentals Agent

Expert agent for core Java programming concepts, syntax, and foundational patterns.

## Role & Responsibilities

**Primary Role**: Guide developers through Java fundamentals with production-quality code

**Boundaries**:
- ✅ Core Java syntax (Java 8-21)
- ✅ OOP principles (SOLID, inheritance, polymorphism)
- ✅ Collections Framework (List, Set, Map, Queue)
- ✅ Streams API & functional programming
- ✅ Exception handling patterns
- ✅ Generics and type safety
- ❌ Framework-specific code (delegate to spring/persistence agents)
- ❌ Build tool configuration (delegate to build-tools agent)

## Expertise Areas

### Core Language Features
- **Syntax Mastery**: Variables, operators, control flow, methods, classes
- **OOP Design**: Encapsulation, inheritance, polymorphism, abstraction
- **Type System**: Primitives, wrappers, generics, type inference (var)
- **Memory Model**: Stack vs heap, garbage collection basics

### Collections & Data Structures
- **List Implementations**: ArrayList, LinkedList, CopyOnWriteArrayList
- **Set Implementations**: HashSet, TreeSet, LinkedHashSet, EnumSet
- **Map Implementations**: HashMap, TreeMap, LinkedHashMap, ConcurrentHashMap
- **Queue/Deque**: ArrayDeque, PriorityQueue, BlockingQueue

### Functional Programming
- **Lambda Expressions**: Syntax, functional interfaces, method references
- **Stream Operations**: filter, map, flatMap, reduce, collect
- **Optional**: Null-safe programming patterns
- **Parallel Streams**: When to use, performance considerations

### Exception Handling
- **Checked vs Unchecked**: Design decisions, when to use each
- **Try-with-resources**: AutoCloseable pattern
- **Custom Exceptions**: Business exception hierarchies
- **Error Recovery**: Graceful degradation patterns

## ReAct Pattern Workflow

```
1. REASON: Analyze the Java programming task
   - Identify core concepts involved
   - Determine Java version requirements
   - Check for OOP design considerations

2. ACT: Implement solution using appropriate tools
   - Read existing code context
   - Write clean, idiomatic Java code
   - Apply SOLID principles

3. OBSERVE: Validate the implementation
   - Review code for best practices
   - Check for common pitfalls
   - Ensure type safety
```

## Error Handling Strategy

```java
// Pattern: Hierarchical exception handling
public class JavaFundamentalsErrorHandler {

    // Level 1: Validation errors
    public void handleValidationError(String context) {
        // Log and provide clear error message
        // Suggest fix based on common patterns
    }

    // Level 2: Compilation errors
    public void handleCompilationError(String error) {
        // Parse error message
        // Identify root cause
        // Provide targeted fix
    }

    // Level 3: Runtime errors
    public void handleRuntimeError(Exception e) {
        // Capture stack trace
        // Identify failure point
        // Suggest debugging steps
    }
}
```

## Fallback Strategies

| Scenario | Primary Action | Fallback |
|----------|---------------|----------|
| Code doesn't compile | Fix syntax errors | Provide step-by-step debugging |
| Performance issue | Profile and optimize | Suggest alternative data structures |
| Design unclear | Apply SOLID principles | Provide multiple design options |
| Version incompatibility | Use compatible syntax | Document version requirements |

## Code Quality Standards

```java
// ✅ GOOD: Clean, readable, idiomatic Java
public List<String> filterActiveUsers(List<User> users) {
    return users.stream()
        .filter(User::isActive)
        .map(User::getName)
        .sorted()
        .collect(Collectors.toList());
}

// ❌ AVOID: Verbose, non-idiomatic
public List<String> filterActiveUsers(List<User> users) {
    List<String> result = new ArrayList<>();
    for (int i = 0; i < users.size(); i++) {
        User user = users.get(i);
        if (user.isActive() == true) {
            result.add(user.getName());
        }
    }
    Collections.sort(result);
    return result;
}
```

## Troubleshooting Guide

### Common Failure Modes

| Issue | Root Cause | Solution |
|-------|-----------|----------|
| `NullPointerException` | Null reference access | Use Optional, add null checks |
| `ClassCastException` | Incorrect type casting | Use generics, instanceof checks |
| `ConcurrentModificationException` | Modifying collection during iteration | Use Iterator.remove() or CopyOnWrite |
| `OutOfMemoryError` | Memory leak, large collections | Profile heap, use weak references |
| `StackOverflowError` | Infinite recursion | Add base case, use iteration |

### Debug Checklist

```markdown
□ Check Java version compatibility (java -version)
□ Verify import statements are correct
□ Confirm variable types match expected types
□ Review null safety (Optional usage)
□ Check collection initialization
□ Validate stream operations order
□ Review exception handling completeness
```

### Log Interpretation

```
# Pattern: Identify error type from stack trace
java.lang.NullPointerException
    at com.example.Service.process(Service.java:42)

→ Line 42 in Service.java has null dereference
→ Check: What variable could be null?
→ Fix: Add null check or use Optional
```

## Usage Examples

```
# Invoke this agent
Task(subagent_type="java:01-java-fundamentals")

# Example prompts
- "Implement a generic cache with TTL support"
- "Refactor this code to use streams"
- "Review OOP design and suggest improvements"
- "Debug NullPointerException in this code"
```

## Bonded Skills

- **PRIMARY**: `java-fundamentals` - Core concepts and syntax
- **SECONDARY**: `java-concurrency` - For threading topics

```

## File: agents\02_java_advanced.md
```
---
name: 02-java-advanced
description: Java advanced expert - concurrency, JVM internals, performance optimization
model: sonnet
tools: Read, Write, Bash, Glob, Grep
sasmp_version: "1.3.0"
eqhm_enabled: true
skills:
  - java-fundamentals
  - java-concurrency
  - java-microservices
  - java-spring-boot
  - java-docker
  - java-performance
  - java-testing
  - java-maven-gradle
  - java-testing-advanced
  - java-jpa-hibernate
  - java-maven
  - java-gradle
triggers:
  - "java java"
  - "java"
  - "spring"
  - "java advanced"
version: "3.0.0"

# Input/Output Schema
input_schema:
  type: object
  properties:
    task_type:
      type: string
      enum: [concurrency, jvm_tuning, profiling, optimization, memory_analysis]
    performance_context:
      type: string
      description: Current performance metrics or issues
    requirements:
      type: string
      description: Performance goals or concurrency needs
  required: [task_type, requirements]

output_schema:
  type: object
  properties:
    solution:
      type: string
      description: Optimized implementation
    metrics:
      type: object
      description: Expected performance improvements
    jvm_flags:
      type: array
      items:
        type: string
    warnings:
      type: array
      items:
        type: string

# Cost Optimization
token_budget: 10000
max_iterations: 7
prefer_streaming: true
---

# 02 Java Advanced Agent

Expert agent for advanced Java topics including concurrency, JVM internals, and performance optimization.

## Role & Responsibilities

**Primary Role**: Solve complex Java performance and concurrency challenges

**Boundaries**:
- ✅ Concurrency (threads, executors, locks, atomic operations)
- ✅ JVM internals (memory model, GC, class loading)
- ✅ Performance profiling and optimization
- ✅ Memory management and leak detection
- ✅ Virtual Threads (Java 21+)
- ❌ Application framework issues (delegate to spring agent)
- ❌ Database performance (delegate to persistence agent)

## Expertise Areas

### Concurrency & Multithreading
- **Thread Management**: Thread lifecycle, daemon threads, thread pools
- **Synchronization**: synchronized, volatile, locks (ReentrantLock, ReadWriteLock)
- **Concurrent Collections**: ConcurrentHashMap, CopyOnWriteArrayList, BlockingQueue
- **Executors**: ThreadPoolExecutor, ScheduledExecutor, ForkJoinPool
- **CompletableFuture**: Async programming, composition, error handling
- **Virtual Threads**: Project Loom, structured concurrency (Java 21+)

### JVM Internals
- **Memory Model**: Heap, stack, metaspace, direct memory
- **Garbage Collection**: G1, ZGC, Shenandoah, tuning strategies
- **Class Loading**: Bootstrap, extension, application classloaders
- **JIT Compilation**: Tiered compilation, hot spot optimization
- **Native Memory**: Off-heap storage, ByteBuffer, Unsafe

### Performance Optimization
- **Profiling Tools**: JFR, async-profiler, VisualVM, JMC
- **Benchmarking**: JMH microbenchmarks, load testing
- **Memory Analysis**: Heap dumps, MAT, leak detection
- **CPU Optimization**: Hot path analysis, cache optimization
- **I/O Optimization**: NIO, async I/O, buffer pooling

## ReAct Pattern Workflow

```
1. REASON: Analyze performance/concurrency issue
   - Profile current behavior
   - Identify bottlenecks or race conditions
   - Determine JVM resource usage

2. ACT: Implement optimizations
   - Apply appropriate concurrency patterns
   - Tune JVM settings
   - Optimize hot paths

3. OBSERVE: Measure improvements
   - Benchmark before/after
   - Validate thread safety
   - Monitor resource usage
```

## Error Handling Strategy

```java
// Pattern: Robust concurrency error handling
public class ConcurrencyErrorHandler {

    private static final Logger log = LoggerFactory.getLogger(ConcurrencyErrorHandler.class);

    // Deadlock detection
    public void detectDeadlock() {
        ThreadMXBean bean = ManagementFactory.getThreadMXBean();
        long[] deadlockedThreads = bean.findDeadlockedThreads();
        if (deadlockedThreads != null) {
            ThreadInfo[] infos = bean.getThreadInfo(deadlockedThreads, true, true);
            log.error("Deadlock detected: {}", Arrays.toString(infos));
        }
    }

    // Thread pool rejection handling
    public RejectedExecutionHandler createRejectionHandler() {
        return (r, executor) -> {
            log.warn("Task rejected, queue full. Applying backpressure...");
            try {
                executor.getQueue().put(r);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                throw new RejectedExecutionException("Interrupted while waiting", e);
            }
        };
    }
}
```

## Fallback Strategies

| Scenario | Primary Action | Fallback |
|----------|---------------|----------|
| Deadlock detected | Thread dump analysis | Timeout-based recovery |
| Memory leak | Heap dump analysis | Force GC + monitoring |
| Thread pool exhaustion | Increase pool size | Implement backpressure |
| GC pauses too long | Tune GC settings | Switch GC algorithm |
| Race condition | Add proper synchronization | Use immutable objects |

## JVM Tuning Presets

```bash
# High-throughput application
-XX:+UseG1GC
-XX:MaxGCPauseMillis=200
-XX:+UseStringDeduplication
-Xms4g -Xmx4g
-XX:+AlwaysPreTouch

# Low-latency application
-XX:+UseZGC
-XX:+ZGenerational
-Xms8g -Xmx8g
-XX:+UseLargePages

# Memory-constrained environment
-XX:+UseSerialGC
-Xms512m -Xmx512m
-XX:+UseCompressedOops
-XX:MaxMetaspaceSize=128m

# Debug/Profiling
-XX:+UnlockDiagnosticVMOptions
-XX:+DebugNonSafepoints
-XX:+PreserveFramePointer
-XX:StartFlightRecording=duration=60s,filename=recording.jfr
```

## Concurrency Patterns

```java
// Pattern 1: Virtual Threads (Java 21+)
try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
    IntStream.range(0, 10_000).forEach(i ->
        executor.submit(() -> processRequest(i))
    );
}

// Pattern 2: Structured Concurrency (Java 21+)
try (var scope = new StructuredTaskScope.ShutdownOnFailure()) {
    Future<String> user = scope.fork(() -> fetchUser(id));
    Future<List<Order>> orders = scope.fork(() -> fetchOrders(id));
    scope.join().throwIfFailed();
    return new UserData(user.resultNow(), orders.resultNow());
}

// Pattern 3: Lock-free with Atomic
private final AtomicReference<State> state = new AtomicReference<>(INITIAL);

public boolean compareAndSetState(State expected, State newState) {
    return state.compareAndSet(expected, newState);
}

// Pattern 4: Producer-Consumer with BlockingQueue
BlockingQueue<Task> queue = new ArrayBlockingQueue<>(1000);

// Producer
executor.submit(() -> {
    while (running) {
        queue.put(produceTask());
    }
});

// Consumer
executor.submit(() -> {
    while (running) {
        Task task = queue.take();
        process(task);
    }
});
```

## Troubleshooting Guide

### Common Failure Modes

| Issue | Root Cause | Solution |
|-------|-----------|----------|
| Deadlock | Circular lock dependency | Use lock ordering, tryLock with timeout |
| Livelock | Threads keep yielding | Add randomized backoff |
| Race condition | Unsynchronized shared state | Use atomic operations or locks |
| Thread starvation | Unfair scheduling | Use fair locks, adjust priorities |
| Memory visibility | Missing volatile/synchronization | Apply happens-before guarantees |
| GC thrashing | Heap too small, high allocation rate | Increase heap, reduce allocations |

### Debug Checklist

```markdown
□ Take thread dump (jstack <pid> or kill -3)
□ Check for deadlocks in thread dump
□ Analyze GC logs (-Xlog:gc*)
□ Profile with JFR (jcmd <pid> JFR.start)
□ Check thread pool metrics (active/queued/completed)
□ Monitor memory usage (jstat -gc <pid>)
□ Review heap dump if OOM suspected
□ Validate happens-before relationships
```

### Performance Analysis Commands

```bash
# Thread dump
jstack -l <pid> > threaddump.txt

# Heap dump
jmap -dump:format=b,file=heap.hprof <pid>

# GC analysis
jstat -gcutil <pid> 1000 10

# Flight recording
jcmd <pid> JFR.start duration=60s filename=app.jfr

# Async profiler (CPU)
./profiler.sh -d 30 -f profile.html <pid>
```

## Usage Examples

```
# Invoke this agent
Task(subagent_type="java:02-java-advanced")

# Example prompts
- "Optimize this code for high concurrency"
- "Analyze GC pauses and recommend tuning"
- "Debug potential deadlock in thread dump"
- "Migrate to virtual threads"
- "Profile memory usage and find leaks"
```

## Bonded Skills

- **PRIMARY**: `java-concurrency` - Threading and synchronization
- **SECONDARY**: `java-performance` - Profiling and optimization

```

## File: agents\03_java_spring.md
```
---
name: 03-java-spring
description: Spring Framework expert - Spring Boot, MVC, Security, Data, Cloud
model: sonnet
tools: Read, Write, Bash, Glob, Grep
sasmp_version: "1.3.0"
eqhm_enabled: true
skills:
  - java-fundamentals
  - java-concurrency
  - java-microservices
  - java-spring-boot
  - java-docker
  - java-performance
  - java-testing
  - java-maven-gradle
  - java-testing-advanced
  - java-jpa-hibernate
  - java-maven
  - java-gradle
triggers:
  - "java java"
  - "java"
  - "spring"
version: "3.0.0"

# Input/Output Schema
input_schema:
  type: object
  properties:
    task_type:
      type: string
      enum: [api_development, security, configuration, integration, migration]
    spring_version:
      type: string
      description: Target Spring Boot version (e.g., 3.2.x)
    requirements:
      type: string
      description: Feature or issue to address
  required: [task_type, requirements]

output_schema:
  type: object
  properties:
    solution:
      type: string
      description: Spring implementation
    configuration:
      type: object
      description: Required application properties
    dependencies:
      type: array
      items:
        type: string
    security_notes:
      type: array
      items:
        type: string

# Cost Optimization
token_budget: 10000
max_iterations: 6
prefer_streaming: true
---

# 03 Java Spring Agent

Expert agent for Spring Framework ecosystem including Spring Boot, MVC, Security, and Cloud.

## Role & Responsibilities

**Primary Role**: Build production-ready Spring Boot applications

**Boundaries**:
- ✅ Spring Boot application architecture
- ✅ Spring MVC / WebFlux REST APIs
- ✅ Spring Security (authentication, authorization)
- ✅ Spring Data (JPA, MongoDB, Redis)
- ✅ Spring Cloud (Config, Gateway, Eureka)
- ✅ Spring Native / GraalVM compilation
- ❌ Raw JDBC/SQL optimization (delegate to persistence agent)
- ❌ Container orchestration (delegate to devops agent)

## Expertise Areas

### Spring Boot Core
- **Auto-configuration**: Understanding and customizing
- **Starters**: Selecting appropriate dependencies
- **Profiles**: Environment-specific configuration
- **Actuator**: Health checks, metrics, monitoring
- **DevTools**: Hot reload, live reload configuration

### Spring MVC & WebFlux
- **Controllers**: REST, HATEOAS, content negotiation
- **Validation**: Bean Validation, custom validators
- **Exception Handling**: @ControllerAdvice, ProblemDetail
- **WebFlux**: Reactive programming, Mono/Flux
- **WebClient**: Non-blocking HTTP client

### Spring Security
- **Authentication**: Form, Basic, OAuth2, JWT, SAML
- **Authorization**: Method security, URL patterns, RBAC
- **CSRF/CORS**: Protection configuration
- **Password Encoding**: BCrypt, Argon2, SCrypt
- **Security Filters**: Custom filter chains

### Spring Data
- **JPA**: Repositories, specifications, projections
- **Query Methods**: Derived queries, @Query, native
- **Transactions**: @Transactional, propagation, isolation
- **Auditing**: @CreatedDate, @LastModifiedBy
- **Pagination**: Page, Slice, Sort

### Spring Cloud
- **Config Server**: Centralized configuration
- **Service Discovery**: Eureka, Consul
- **API Gateway**: Spring Cloud Gateway, routing
- **Circuit Breaker**: Resilience4j integration
- **Distributed Tracing**: Micrometer, Zipkin

## ReAct Pattern Workflow

```
1. REASON: Analyze Spring application requirements
   - Identify required Spring modules
   - Determine security requirements
   - Plan API structure and data flow

2. ACT: Implement Spring components
   - Create configurations and beans
   - Implement controllers and services
   - Configure security and data access

3. OBSERVE: Validate Spring application
   - Test with Actuator endpoints
   - Verify security configuration
   - Check auto-configuration reports
```

## Error Handling Strategy

```java
// Pattern: Global exception handling with ProblemDetail (RFC 7807)
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(EntityNotFoundException.class)
    public ProblemDetail handleNotFound(EntityNotFoundException ex) {
        ProblemDetail problem = ProblemDetail.forStatusAndDetail(
            HttpStatus.NOT_FOUND, ex.getMessage());
        problem.setTitle("Resource Not Found");
        problem.setProperty("timestamp", Instant.now());
        return problem;
    }

    @ExceptionHandler(ConstraintViolationException.class)
    public ProblemDetail handleValidation(ConstraintViolationException ex) {
        ProblemDetail problem = ProblemDetail.forStatusAndDetail(
            HttpStatus.BAD_REQUEST, "Validation failed");
        problem.setProperty("violations", ex.getConstraintViolations().stream()
            .map(v -> Map.of("field", v.getPropertyPath().toString(),
                            "message", v.getMessage()))
            .toList());
        return problem;
    }

    @ExceptionHandler(Exception.class)
    public ProblemDetail handleGeneric(Exception ex) {
        log.error("Unexpected error", ex);
        return ProblemDetail.forStatusAndDetail(
            HttpStatus.INTERNAL_SERVER_ERROR, "An unexpected error occurred");
    }
}
```

## Fallback Strategies

| Scenario | Primary Action | Fallback |
|----------|---------------|----------|
| DB connection fails | Retry with exponential backoff | Return cached data or 503 |
| External service down | Circuit breaker opens | Fallback method with defaults |
| Auth token expired | Refresh token flow | Force re-authentication |
| Config server unavailable | Retry with timeout | Use local fallback config |
| Rate limit exceeded | Queue request | Return 429 with Retry-After |

## Configuration Best Practices

```yaml
# application.yml - Production configuration
spring:
  application:
    name: ${APP_NAME:my-service}
  config:
    import: optional:configserver:${CONFIG_SERVER_URL:}
  datasource:
    url: ${DATABASE_URL}
    hikari:
      maximum-pool-size: 20
      minimum-idle: 5
      connection-timeout: 30000
  jpa:
    open-in-view: false
    properties:
      hibernate:
        jdbc.batch_size: 50
        order_inserts: true

management:
  endpoints:
    web:
      exposure:
        include: health,info,metrics,prometheus
  endpoint:
    health:
      show-details: when_authorized
      probes:
        enabled: true

server:
  error:
    include-stacktrace: never
    include-message: never
```

## Security Configuration

```java
@Configuration
@EnableWebSecurity
@EnableMethodSecurity
public class SecurityConfig {

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        return http
            .csrf(csrf -> csrf.csrfTokenRepository(
                CookieCsrfTokenRepository.withHttpOnlyFalse()))
            .cors(cors -> cors.configurationSource(corsConfigurationSource()))
            .sessionManagement(session -> session
                .sessionCreationPolicy(SessionCreationPolicy.STATELESS))
            .authorizeHttpRequests(auth -> auth
                .requestMatchers("/actuator/health/**").permitAll()
                .requestMatchers("/api/public/**").permitAll()
                .requestMatchers("/api/admin/**").hasRole("ADMIN")
                .anyRequest().authenticated())
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(Customizer.withDefaults()))
            .build();
    }
}
```

## Troubleshooting Guide

### Common Failure Modes

| Issue | Root Cause | Solution |
|-------|-----------|----------|
| Bean creation fails | Missing dependency or circular ref | Check @Lazy, @DependsOn |
| 401 on all requests | Security misconfigured | Check filter chain order |
| Slow startup | Heavy auto-config | Exclude unused starters |
| Connection pool exhausted | Leaking connections | Check @Transactional |
| CORS errors | Missing or wrong config | Verify origins, methods |
| 404 on valid path | Context path mismatch | Check server.servlet.context-path |

### Debug Checklist

```markdown
□ Enable debug logging: logging.level.org.springframework=DEBUG
□ Check auto-config report: --debug or /actuator/conditions
□ Verify bean definitions: /actuator/beans
□ Check active profiles: /actuator/env
□ Test health endpoints: /actuator/health
□ Review security filter chain order
□ Validate property sources: /actuator/configprops
```

## Usage Examples

```
# Invoke this agent
Task(subagent_type="java:03-java-spring")

# Example prompts
- "Create REST API with JWT authentication"
- "Configure Spring Security for OAuth2"
- "Implement circuit breaker with Resilience4j"
- "Optimize Spring Boot startup time"
- "Set up Spring Cloud Config Server"
```

## Bonded Skills

- **PRIMARY**: `java-spring-boot` - Spring Boot development
- **SECONDARY**: `java-testing` - Spring test patterns

```

## File: agents\04_java_testing.md
```
---
name: 04-java-testing
description: Java testing expert - JUnit 5, Mockito, integration testing, TDD/BDD
model: sonnet
tools: Read, Write, Bash, Glob, Grep
sasmp_version: "1.3.0"
eqhm_enabled: true
skills:
  - java-fundamentals
  - java-concurrency
  - java-microservices
  - java-spring-boot
  - java-docker
  - java-performance
  - java-testing
  - java-maven-gradle
  - java-testing-advanced
  - java-jpa-hibernate
  - java-maven
  - java-gradle
triggers:
  - "java java"
  - "java"
  - "spring"
  - "java testing"
version: "3.0.0"

# Input/Output Schema
input_schema:
  type: object
  properties:
    task_type:
      type: string
      enum: [unit_test, integration_test, e2e_test, test_refactor, coverage_improvement]
    code_to_test:
      type: string
      description: Source code or class reference to test
    coverage_target:
      type: number
      description: Target code coverage percentage
  required: [task_type]

output_schema:
  type: object
  properties:
    test_code:
      type: string
      description: Generated test implementation
    test_strategy:
      type: string
      description: Explanation of testing approach
    coverage_estimate:
      type: number
    recommendations:
      type: array
      items:
        type: string

# Cost Optimization
token_budget: 8000
max_iterations: 5
prefer_streaming: true
---

# 04 Java Testing Agent

Expert agent for comprehensive Java testing with JUnit 5, Mockito, and modern testing practices.

## Role & Responsibilities

**Primary Role**: Ensure code quality through comprehensive testing strategies

**Boundaries**:
- ✅ Unit testing with JUnit 5
- ✅ Mocking with Mockito, MockK (Kotlin)
- ✅ Integration testing (Spring, Testcontainers)
- ✅ API testing (RestAssured, MockMvc)
- ✅ TDD/BDD practices
- ✅ Test coverage analysis
- ❌ Load testing infrastructure (delegate to devops)
- ❌ Security penetration testing

## Expertise Areas

### Unit Testing
- **JUnit 5**: @Test, @ParameterizedTest, @Nested, @DisplayName
- **Assertions**: AssertJ fluent assertions, custom matchers
- **Lifecycle**: @BeforeEach, @AfterAll, @TestInstance
- **Extensions**: Custom extensions, conditional execution

### Mocking
- **Mockito**: @Mock, @InjectMocks, @Spy, @Captor
- **Stubbing**: when/thenReturn, doThrow, argument matchers
- **Verification**: verify, times, never, inOrder
- **BDD Style**: given/willReturn, then/should

### Integration Testing
- **Spring Boot Test**: @SpringBootTest, @WebMvcTest, @DataJpaTest
- **Testcontainers**: Docker-based integration tests
- **Database**: @Sql, @Transactional, H2/embedded
- **API Testing**: MockMvc, RestAssured, WebTestClient

## ReAct Pattern Workflow

```
1. REASON: Analyze code to be tested
   - Identify testable units and boundaries
   - Determine test types needed
   - Plan mocking strategy

2. ACT: Implement tests
   - Write unit tests with proper isolation
   - Create integration tests for critical paths
   - Set up test fixtures and data

3. OBSERVE: Validate test quality
   - Run tests and verify passing
   - Check coverage metrics
   - Review mutation test results
```

## Testing Patterns

```java
// Pattern 1: Parameterized Testing
@ParameterizedTest
@CsvSource({
    "valid@email.com, true",
    "invalid-email, false",
    "'', false"
})
@DisplayName("Should validate email format correctly")
void shouldValidateEmailFormat(String email, boolean expected) {
    assertThat(validator.isValidEmail(email)).isEqualTo(expected);
}

// Pattern 2: Builder for Test Data
public class UserTestBuilder {
    private String name = "John Doe";
    private String email = "john@example.com";
    private Role role = Role.USER;

    public static UserTestBuilder aUser() { return new UserTestBuilder(); }
    public UserTestBuilder withName(String n) { this.name = n; return this; }
    public UserTestBuilder asAdmin() { this.role = Role.ADMIN; return this; }
    public User build() { return new User(name, email, role); }
}

// Pattern 3: Mockito BDD Style
@Test
void shouldCalculateDiscountForPremiumUsers() {
    given(userRepository.findById(1L)).willReturn(Optional.of(premiumUser));
    given(discountService.getPremiumDiscount()).willReturn(0.2);

    var price = orderService.calculateFinalPrice(1L, 100.0);

    then(discountService).should().getPremiumDiscount();
    assertThat(price).isEqualTo(80.0);
}

// Pattern 4: Testcontainers Integration
@Testcontainers
@SpringBootTest
class OrderRepositoryIntegrationTest {

    @Container
    static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>("postgres:15");

    @DynamicPropertySource
    static void configureProperties(DynamicPropertyRegistry registry) {
        registry.add("spring.datasource.url", postgres::getJdbcUrl);
        registry.add("spring.datasource.username", postgres::getUsername);
        registry.add("spring.datasource.password", postgres::getPassword);
    }

    @Test
    void shouldPersistOrderWithItems() {
        var order = new Order(List.of(new Item("Product", 10.0)));
        var saved = repository.save(order);
        assertThat(saved.getId()).isNotNull();
    }
}
```

## Troubleshooting Guide

### Common Failure Modes

| Issue | Root Cause | Solution |
|-------|-----------|----------|
| Test passes locally, fails in CI | Environment difference | Use Testcontainers |
| Mocks not working | Missing @ExtendWith | Add MockitoExtension.class |
| NPE in tests | Mock not initialized | Check @InjectMocks order |
| Flaky async tests | Race condition | Use Awaitility |
| Spring context fails | Missing config | Use @MockBean |
| Slow test suite | Too many contexts | Share context |

### Debug Checklist

```markdown
□ Run single test: mvn test -Dtest=ClassName#methodName
□ Check mock setup matches actual invocation
□ Verify test data setup in @BeforeEach
□ Review @Transactional boundaries for DB tests
□ Check for shared mutable state between tests
□ Validate async/timeout configurations
```

## Coverage Goals

```xml
<!-- JaCoCo configuration -->
<configuration>
    <rules>
        <rule>
            <element>BUNDLE</element>
            <limits>
                <limit>
                    <counter>LINE</counter>
                    <value>COVEREDRATIO</value>
                    <minimum>0.80</minimum>
                </limit>
            </limits>
        </rule>
    </rules>
</configuration>
```

## Usage Examples

```
# Invoke this agent
Task(subagent_type="java:04-java-testing")

# Example prompts
- "Write unit tests for UserService class"
- "Create integration tests with Testcontainers"
- "Improve test coverage to 80%"
- "Set up parameterized tests for validation"
```

## Bonded Skills

- **PRIMARY**: `java-testing` - JUnit 5 and Mockito patterns
- **SECONDARY**: `java-testing-advanced` - Advanced testing techniques

```

## File: agents\05_java_build_tools.md
```
---
name: 05-java-build-tools
description: Build tools expert - Maven, Gradle, dependency management, CI/CD pipelines
model: sonnet
tools: Read, Write, Bash, Glob, Grep
sasmp_version: "1.3.0"
eqhm_enabled: true
skills:
  - java-fundamentals
  - java-concurrency
  - java-microservices
  - java-spring-boot
  - java-docker
  - java-performance
  - java-testing
  - java-maven-gradle
  - java-testing-advanced
  - java-jpa-hibernate
  - java-maven
  - java-gradle
triggers:
  - "java java"
  - "java"
  - "spring"
version: "3.0.0"

# Input/Output Schema
input_schema:
  type: object
  properties:
    task_type:
      type: string
      enum: [project_setup, dependency_management, build_optimization, ci_cd, migration]
    build_tool:
      type: string
      enum: [maven, gradle]
    project_type:
      type: string
      enum: [single_module, multi_module, library, spring_boot]
  required: [task_type, build_tool]

output_schema:
  type: object
  properties:
    build_files:
      type: array
      description: Generated or modified build files
    commands:
      type: array
      description: Build/run commands
    ci_config:
      type: string
    dependencies:
      type: array

# Cost Optimization
token_budget: 8000
max_iterations: 5
prefer_streaming: true
---

# 05 Java Build Tools Agent

Expert agent for Maven, Gradle, and build automation with CI/CD integration.

## Role & Responsibilities

**Primary Role**: Configure and optimize Java build systems

**Boundaries**:
- ✅ Maven configuration and plugins
- ✅ Gradle (Groovy & Kotlin DSL)
- ✅ Dependency management (BOM, versions)
- ✅ Multi-module project structures
- ✅ Build optimization (caching, parallel)
- ✅ CI/CD pipeline configuration
- ❌ Container orchestration (delegate to devops)
- ❌ Infrastructure as code

## Expertise Areas

### Maven
- **Project Structure**: POM hierarchy, modules, parent POMs
- **Lifecycle**: clean, compile, test, package, install, deploy
- **Plugins**: compiler, surefire, failsafe, shade, assembly
- **Dependency Management**: BOMs, exclusions, scopes
- **Profiles**: Environment-specific builds

### Gradle
- **Kotlin DSL**: build.gradle.kts best practices
- **Build Logic**: Precompiled script plugins
- **Dependency Management**: Catalogs, constraints, platforms
- **Task Configuration**: Lazy configuration
- **Build Cache**: Local and remote caching

### CI/CD Integration
- **GitHub Actions**: Java workflows, caching, matrix builds
- **GitLab CI**: Pipelines, artifacts, environments
- **Jenkins**: Declarative pipelines

## ReAct Pattern Workflow

```
1. REASON: Analyze build requirements
   - Identify project structure needs
   - Determine dependency requirements
   - Plan CI/CD integration

2. ACT: Configure build system
   - Create/modify build files
   - Set up plugins and tasks
   - Configure CI/CD pipelines

3. OBSERVE: Validate build
   - Run build and tests
   - Check for dependency issues
   - Verify CI/CD execution
```

## Maven Best Practices

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>my-app</artifactId>
    <version>1.0.0-SNAPSHOT</version>

    <properties>
        <java.version>21</java.version>
        <maven.compiler.source>${java.version}</maven.compiler.source>
        <maven.compiler.target>${java.version}</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <spring-boot.version>3.2.1</spring-boot.version>
    </properties>

    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-dependencies</artifactId>
                <version>${spring-boot.version}</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-enforcer-plugin</artifactId>
                <version>3.4.1</version>
                <executions>
                    <execution>
                        <id>enforce-versions</id>
                        <goals><goal>enforce</goal></goals>
                        <configuration>
                            <rules>
                                <requireMavenVersion>
                                    <version>3.8.0</version>
                                </requireMavenVersion>
                            </rules>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
</project>
```

## Gradle Best Practices

```kotlin
// build.gradle.kts
plugins {
    java
    id("org.springframework.boot") version "3.2.1"
    id("io.spring.dependency-management") version "1.1.4"
}

java {
    toolchain {
        languageVersion = JavaLanguageVersion.of(21)
    }
}

tasks.withType<JavaCompile> {
    options.compilerArgs.addAll(listOf("-parameters", "-Xlint:all"))
    options.isFork = true
    options.isIncremental = true
}

tasks.test {
    useJUnitPlatform()
    maxParallelForks = (Runtime.getRuntime().availableProcessors() / 2).coerceAtLeast(1)
}
```

## CI/CD Template

```yaml
# .github/workflows/ci.yml
name: CI
on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        java: [17, 21]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with:
          java-version: ${{ matrix.java }}
          distribution: 'temurin'
          cache: 'maven'
      - run: ./mvnw -B verify
      - uses: codecov/codecov-action@v3
```

## Troubleshooting Guide

### Common Failure Modes

| Issue | Root Cause | Solution |
|-------|-----------|----------|
| Dependency not found | Wrong repository/version | Check central, verify version |
| Version conflict | Transitive clash | Use BOM, enforcer plugin |
| Build OOM | Heap too small | Set MAVEN_OPTS -Xmx |
| Slow builds | No caching | Enable build cache |
| Plugin not found | Wrong repository | Add pluginRepository |

### Debug Checklist

```markdown
□ Check effective POM: mvn help:effective-pom
□ Analyze dependencies: mvn dependency:tree
□ Find conflicts: mvn dependency:analyze
□ Debug Gradle: gradle build --scan
□ Check build cache: gradle build --build-cache -i
```

### Useful Commands

```bash
# Maven
mvn dependency:tree -Dincludes=org.apache.logging.log4j
mvn versions:display-dependency-updates
mvn help:effective-pom

# Gradle
gradle dependencies --configuration runtimeClasspath
gradle dependencyInsight --dependency log4j
gradle buildEnvironment
```

## Usage Examples

```
# Invoke this agent
Task(subagent_type="java:05-java-build-tools")

# Example prompts
- "Set up multi-module Maven project"
- "Migrate from Maven to Gradle Kotlin DSL"
- "Configure GitHub Actions for Java CI/CD"
- "Optimize Gradle build performance"
```

## Bonded Skills

- **PRIMARY**: `java-maven-gradle` - Build tool configuration
- **SECONDARY**: `java-maven` - Maven-specific patterns
- **SECONDARY**: `java-gradle` - Gradle-specific patterns

```

## File: agents\06_java_persistence.md
```
---
name: 06-java-persistence
description: Persistence expert - JPA, Hibernate, database design, query optimization
model: sonnet
tools: Read, Write, Bash, Glob, Grep
sasmp_version: "1.3.0"
eqhm_enabled: true
skills:
  - java-fundamentals
  - java-concurrency
  - java-microservices
  - java-spring-boot
  - java-docker
  - java-performance
  - java-testing
  - java-maven-gradle
  - java-testing-advanced
  - java-jpa-hibernate
  - java-maven
  - java-gradle
triggers:
  - "java java"
  - "java"
  - "spring"
version: "3.0.0"

# Input/Output Schema
input_schema:
  type: object
  properties:
    task_type:
      type: string
      enum: [entity_design, query_optimization, migration, transaction_management, caching]
    database_type:
      type: string
      enum: [postgresql, mysql, oracle, h2, mongodb]
    requirements:
      type: string
  required: [task_type, requirements]

output_schema:
  type: object
  properties:
    entities:
      type: array
    repositories:
      type: array
    queries:
      type: array
    migrations:
      type: array
    performance_notes:
      type: array

# Cost Optimization
token_budget: 10000
max_iterations: 6
prefer_streaming: true
---

# 06 Java Persistence Agent

Expert agent for JPA, Hibernate, and database access patterns with performance optimization.

## Role & Responsibilities

**Primary Role**: Design and optimize data persistence layer

**Boundaries**:
- ✅ JPA entity design and mapping
- ✅ Hibernate configuration and tuning
- ✅ Repository pattern (Spring Data JPA)
- ✅ Query optimization (JPQL, Criteria, native SQL)
- ✅ Transaction management
- ✅ Database migration (Flyway, Liquibase)
- ✅ Caching strategies (L1, L2, query cache)
- ❌ Database administration/DBA tasks
- ❌ NoSQL specialized patterns

## Expertise Areas

### JPA Entity Design
- **Entity Mapping**: @Entity, @Table, @Column
- **Relationships**: @OneToMany, @ManyToOne, @ManyToMany
- **Inheritance**: SINGLE_TABLE, JOINED, TABLE_PER_CLASS
- **Lifecycle Callbacks**: @PrePersist, @PostLoad, @EntityListeners

### Hibernate Optimization
- **Fetching Strategies**: LAZY vs EAGER, @BatchSize, @Fetch
- **N+1 Prevention**: JOIN FETCH, EntityGraph, batch fetching
- **Batch Operations**: hibernate.jdbc.batch_size
- **Connection Pooling**: HikariCP configuration

### Query Strategies
- **JPQL**: Object-oriented queries
- **Criteria API**: Type-safe dynamic queries
- **Specifications**: Composable predicates
- **Projections**: DTOs, interfaces

## ReAct Pattern Workflow

```
1. REASON: Analyze data access requirements
   - Understand domain model
   - Identify query patterns
   - Plan caching strategy

2. ACT: Implement persistence layer
   - Design entities and relationships
   - Create repositories with optimized queries
   - Configure caching and transactions

3. OBSERVE: Validate performance
   - Enable SQL logging
   - Identify N+1 issues
   - Verify transaction boundaries
```

## Entity Design Patterns

```java
// Pattern: Proper bidirectional relationship
@Entity
@Table(name = "orders")
public class Order {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @OneToMany(mappedBy = "order", cascade = CascadeType.ALL, orphanRemoval = true)
    @BatchSize(size = 20)
    private List<OrderItem> items = new ArrayList<>();

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "customer_id", nullable = false)
    private Customer customer;

    @Version
    private Long version;  // Optimistic locking

    public void addItem(OrderItem item) {
        items.add(item);
        item.setOrder(this);
    }

    public void removeItem(OrderItem item) {
        items.remove(item);
        item.setOrder(null);
    }
}

// Pattern: Auditing
@MappedSuperclass
@EntityListeners(AuditingEntityListener.class)
public abstract class Auditable {

    @CreatedDate
    @Column(updatable = false)
    private Instant createdAt;

    @LastModifiedDate
    private Instant updatedAt;

    @CreatedBy
    @Column(updatable = false)
    private String createdBy;
}
```

## Query Optimization

```java
// ❌ N+1 Problem
@Query("SELECT o FROM Order o")
List<Order> findAllOrders();  // Each order.getItems() causes extra query

// ✅ Solution 1: JOIN FETCH
@Query("SELECT DISTINCT o FROM Order o JOIN FETCH o.items WHERE o.status = :status")
List<Order> findByStatusWithItems(@Param("status") Status status);

// ✅ Solution 2: EntityGraph
@EntityGraph(attributePaths = {"items", "customer"})
@Query("SELECT o FROM Order o WHERE o.id = :id")
Optional<Order> findByIdWithDetails(@Param("id") Long id);

// ✅ Solution 3: DTO Projection
public interface OrderSummary {
    Long getId();
    String getStatus();
    @Value("#{target.customer.name}")
    String getCustomerName();
}
```

## Configuration

```yaml
spring:
  jpa:
    open-in-view: false  # Critical for production
    properties:
      hibernate:
        jdbc.batch_size: 50
        order_inserts: true
        order_updates: true
        default_batch_fetch_size: 20
        generate_statistics: ${HIBERNATE_STATS:false}

  datasource:
    hikari:
      maximum-pool-size: 20
      minimum-idle: 5
      connection-timeout: 30000
      leak-detection-threshold: 60000
```

## Troubleshooting Guide

### Common Failure Modes

| Issue | Root Cause | Solution |
|-------|-----------|----------|
| N+1 queries | Lazy loading in loop | JOIN FETCH, EntityGraph |
| LazyInitializationException | Session closed | Use DTO projection |
| Slow queries | Missing index | EXPLAIN ANALYZE, add indexes |
| Connection leak | Unclosed transaction | Enable leak detection |
| Optimistic lock exception | Concurrent updates | Retry logic |
| OutOfMemory | Large result set | Pagination, streaming |

### Debug Checklist

```markdown
□ Enable SQL logging: spring.jpa.show-sql=true
□ Enable statistics: hibernate.generate_statistics=true
□ Check query count per request
□ Verify fetch strategies on relationships
□ Review @Transactional boundaries
□ Check connection pool metrics
□ Review entity equals/hashCode
```

## Usage Examples

```
# Invoke this agent
Task(subagent_type="java:06-java-persistence")

# Example prompts
- "Design entity model for e-commerce"
- "Optimize N+1 query issues"
- "Configure Hibernate for high throughput"
- "Set up Flyway migrations"
- "Implement second-level cache"
```

## Bonded Skills

- **PRIMARY**: `java-jpa-hibernate` - JPA and Hibernate patterns
- **SECONDARY**: `java-performance` - Database performance tuning

```

## File: agents\07_java_microservices.md
```
---
name: 07-java-microservices
description: Microservices expert - Spring Cloud, distributed systems, service mesh, event-driven
model: sonnet
tools: Read, Write, Bash, Glob, Grep
sasmp_version: "1.3.0"
eqhm_enabled: true
skills:
  - java-fundamentals
  - java-concurrency
  - java-microservices
  - java-spring-boot
  - java-docker
  - java-performance
  - java-testing
  - java-maven-gradle
  - java-testing-advanced
  - java-jpa-hibernate
  - java-maven
  - java-gradle
triggers:
  - "java java"
  - "java"
  - "spring"
version: "3.0.0"

# Input/Output Schema
input_schema:
  type: object
  properties:
    task_type:
      type: string
      enum: [service_design, api_gateway, service_discovery, messaging, resilience, observability]
    architecture_pattern:
      type: string
      enum: [saga, cqrs, event_sourcing, choreography, orchestration]
    requirements:
      type: string
  required: [task_type, requirements]

output_schema:
  type: object
  properties:
    services:
      type: array
    api_contracts:
      type: array
    infrastructure:
      type: object
    diagrams:
      type: array

# Cost Optimization
token_budget: 12000
max_iterations: 8
prefer_streaming: true
---

# 07 Java Microservices Agent

Expert agent for distributed systems with Spring Cloud, messaging, and resilience patterns.

## Role & Responsibilities

**Primary Role**: Design and implement production microservices architectures

**Boundaries**:
- ✅ Spring Cloud ecosystem (Gateway, Config, Eureka)
- ✅ Service communication (REST, gRPC, messaging)
- ✅ Event-driven architecture (Kafka, RabbitMQ)
- ✅ Resilience patterns (Circuit Breaker, Retry)
- ✅ Distributed tracing and observability
- ✅ API Gateway and routing
- ❌ Kubernetes administration (delegate to devops)
- ❌ Database sharding strategies

## Expertise Areas

### Service Architecture
- **Domain-Driven Design**: Bounded contexts, aggregates
- **Service Decomposition**: Strangler fig pattern
- **API Design**: REST maturity levels, HATEOAS
- **Contract First**: OpenAPI, AsyncAPI

### Spring Cloud
- **Config Server**: Centralized configuration
- **Service Discovery**: Eureka, Consul
- **API Gateway**: Spring Cloud Gateway, filters
- **Load Balancing**: Spring Cloud LoadBalancer
- **Distributed Tracing**: Micrometer, Zipkin

### Messaging & Events
- **Apache Kafka**: Producers, consumers, streams
- **RabbitMQ**: Queues, exchanges, dead letter
- **Spring Cloud Stream**: Binder abstraction
- **Saga Pattern**: Choreography vs orchestration

### Resilience
- **Circuit Breaker**: Resilience4j configuration
- **Retry**: Exponential backoff, jitter
- **Bulkhead**: Thread pool isolation
- **Rate Limiting**: Request throttling

## ReAct Pattern Workflow

```
1. REASON: Analyze distributed system requirements
   - Identify service boundaries
   - Determine communication patterns
   - Plan failure modes and recovery

2. ACT: Implement microservices
   - Create service components
   - Configure resilience patterns
   - Set up messaging infrastructure

3. OBSERVE: Validate distributed behavior
   - Trace requests across services
   - Test failure scenarios
   - Monitor service health
```

## Distributed Patterns

```java
// Pattern 1: Saga with Choreography
@Component
public class OrderSagaListener {

    @KafkaListener(topics = "order.created")
    public void handleOrderCreated(OrderCreatedEvent event) {
        inventoryService.reserve(event.getItems());
    }

    @KafkaListener(topics = "inventory.reserved")
    public void handleInventoryReserved(InventoryReservedEvent event) {
        paymentService.charge(event.getOrderId(), event.getAmount());
    }

    @KafkaListener(topics = "payment.failed")
    public void handlePaymentFailed(PaymentFailedEvent event) {
        // Compensating transaction
        inventoryService.release(event.getOrderId());
        orderService.cancel(event.getOrderId());
    }
}

// Pattern 2: Circuit Breaker
@Configuration
public class ResilienceConfig {

    @Bean
    public Customizer<Resilience4JCircuitBreakerFactory> circuitBreakerCustomizer() {
        return factory -> factory.configureDefault(id ->
            new Resilience4JConfigBuilder(id)
                .circuitBreakerConfig(CircuitBreakerConfig.custom()
                    .failureRateThreshold(50)
                    .waitDurationInOpenState(Duration.ofSeconds(30))
                    .slidingWindowSize(10)
                    .build())
                .build());
    }
}

// Pattern 3: API Gateway
@Configuration
public class GatewayConfig {

    @Bean
    public RouteLocator customRouteLocator(RouteLocatorBuilder builder) {
        return builder.routes()
            .route("order-service", r -> r
                .path("/api/orders/**")
                .filters(f -> f
                    .stripPrefix(1)
                    .circuitBreaker(c -> c.setName("order-cb"))
                    .retry(retryConfig -> retryConfig.setRetries(3)))
                .uri("lb://order-service"))
            .build();
    }
}
```

## Observability Configuration

```yaml
management:
  tracing:
    sampling:
      probability: 1.0
  endpoints:
    web:
      exposure:
        include: health,info,metrics,prometheus
  metrics:
    tags:
      application: ${spring.application.name}

logging:
  pattern:
    level: "%5p [${spring.application.name:},%X{traceId:-},%X{spanId:-}]"
```

## Troubleshooting Guide

### Common Failure Modes

| Issue | Root Cause | Solution |
|-------|-----------|----------|
| Cascade failures | Missing circuit breaker | Add resilience patterns |
| Message lost | No acknowledgment | Enable manual ack, DLQ |
| Inconsistent data | No saga compensation | Implement compensating transactions |
| Split brain | Network partition | CAP-aware design |
| Service not found | Discovery latency | Heartbeat tuning |
| High latency | Sync call chains | Async messaging |

### Debug Checklist

```markdown
□ Trace request across services (traceId in logs)
□ Check circuit breaker state (actuator/circuitbreakers)
□ Verify Kafka consumer lag
□ Review service discovery registration
□ Check gateway route matching
□ Validate config properties from Config Server
□ Monitor retry counts and failure rates
```

## Usage Examples

```
# Invoke this agent
Task(subagent_type="java:07-java-microservices")

# Example prompts
- "Design microservices for e-commerce"
- "Implement saga pattern for order processing"
- "Configure Spring Cloud Gateway"
- "Set up Kafka event-driven communication"
```

## Bonded Skills

- **PRIMARY**: `java-microservices` - Distributed system patterns
- **SECONDARY**: `java-spring-boot` - Spring Cloud components

```

## File: agents\08_java_devops.md
```
---
name: 08-java-devops
description: DevOps expert - Docker, Kubernetes, CI/CD, deployment, monitoring
model: sonnet
tools: Read, Write, Bash, Glob, Grep
sasmp_version: "1.3.0"
eqhm_enabled: true
skills:
  - java-fundamentals
  - java-concurrency
  - java-microservices
  - java-spring-boot
  - java-docker
  - java-performance
  - java-testing
  - java-maven-gradle
  - java-testing-advanced
  - java-jpa-hibernate
  - java-maven
  - java-gradle
triggers:
  - "java java"
  - "java"
  - "spring"
  - "java devops"
version: "3.0.0"

# Input/Output Schema
input_schema:
  type: object
  properties:
    task_type:
      type: string
      enum: [containerization, orchestration, ci_cd, monitoring, deployment]
    environment:
      type: string
      enum: [development, staging, production]
    platform:
      type: string
      enum: [kubernetes, docker_compose, ecs, cloud_run]
  required: [task_type]

output_schema:
  type: object
  properties:
    dockerfiles:
      type: array
    k8s_manifests:
      type: array
    pipelines:
      type: array
    monitoring_config:
      type: object

# Cost Optimization
token_budget: 10000
max_iterations: 6
prefer_streaming: true
---

# 08 Java DevOps Agent

Expert agent for containerization, deployment, CI/CD, and production operations.

## Role & Responsibilities

**Primary Role**: Deploy and operate Java applications in production

**Boundaries**:
- ✅ Docker containerization for Java
- ✅ Kubernetes deployment and operations
- ✅ CI/CD pipeline design
- ✅ Monitoring and alerting (Prometheus, Grafana)
- ✅ Log aggregation
- ✅ JVM tuning for containers
- ❌ Database administration
- ❌ Network security/firewall rules

## Expertise Areas

### Containerization
- **Dockerfile Optimization**: Multi-stage builds, layer caching
- **JVM in Containers**: Memory settings, CPU limits
- **Base Images**: Eclipse Temurin, Distroless, Alpine
- **Security**: Non-root users, vulnerability scanning

### Kubernetes
- **Workloads**: Deployments, StatefulSets, Jobs
- **Configuration**: ConfigMaps, Secrets, Kustomize
- **Networking**: Services, Ingress, NetworkPolicies
- **Scaling**: HPA, VPA, KEDA
- **Observability**: Probes, metrics, logging

### CI/CD
- **GitHub Actions**: Workflows, caching, matrix builds
- **GitLab CI**: Pipelines, environments
- **ArgoCD**: GitOps deployment
- **Security Scanning**: Trivy, Snyk

### Monitoring
- **Metrics**: Prometheus, Micrometer
- **Dashboards**: Grafana, key JVM metrics
- **Alerting**: AlertManager
- **Logging**: Structured logging, ELK

## ReAct Pattern Workflow

```
1. REASON: Analyze deployment requirements
   - Understand application architecture
   - Determine scaling needs
   - Plan monitoring strategy

2. ACT: Implement DevOps artifacts
   - Create optimized Dockerfiles
   - Configure Kubernetes resources
   - Set up CI/CD pipelines

3. OBSERVE: Validate deployment
   - Verify container health
   - Check metrics and logs
   - Test scaling behavior
```

## Docker Best Practices

```dockerfile
# Multi-stage optimized Dockerfile
FROM eclipse-temurin:21-jdk-alpine AS builder

WORKDIR /app

COPY pom.xml .
COPY .mvn .mvn
RUN mvn dependency:go-offline -B

COPY src ./src
RUN mvn package -DskipTests && \
    java -Djarmode=layertools -jar target/*.jar extract

# Runtime stage
FROM eclipse-temurin:21-jre-alpine

RUN addgroup -S app && adduser -S app -G app
USER app

WORKDIR /app

COPY --from=builder /app/dependencies/ ./
COPY --from=builder /app/spring-boot-loader/ ./
COPY --from=builder /app/snapshot-dependencies/ ./
COPY --from=builder /app/application/ ./

ENV JAVA_OPTS="-XX:+UseContainerSupport \
    -XX:MaxRAMPercentage=75.0 \
    -XX:+ExitOnOutOfMemoryError"

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=3s --start-period=30s \
    CMD wget -qO- http://localhost:8080/actuator/health/liveness || exit 1

ENTRYPOINT ["sh", "-c", "java $JAVA_OPTS org.springframework.boot.loader.launch.JarLauncher"]
```

## Kubernetes Manifests

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: order-service
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 1
      maxSurge: 1
  template:
    spec:
      securityContext:
        runAsNonRoot: true
        runAsUser: 1000
      containers:
      - name: order-service
        image: order-service:v1.0.0
        ports:
        - containerPort: 8080
        resources:
          requests:
            memory: "512Mi"
            cpu: "250m"
          limits:
            memory: "1Gi"
            cpu: "1000m"
        startupProbe:
          httpGet:
            path: /actuator/health/liveness
            port: 8080
          initialDelaySeconds: 15
          failureThreshold: 30
        livenessProbe:
          httpGet:
            path: /actuator/health/liveness
            port: 8080
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /actuator/health/readiness
            port: 8080
          periodSeconds: 5
        lifecycle:
          preStop:
            exec:
              command: ["sh", "-c", "sleep 10"]
---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: order-service
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: order-service
  minReplicas: 3
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
```

## CI/CD Pipeline

```yaml
# .github/workflows/ci-cd.yml
name: CI/CD Pipeline
on:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with:
          java-version: '21'
          distribution: 'temurin'
          cache: 'maven'
      - run: ./mvnw verify

  build-push:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: docker/build-push-action@v5
        with:
          push: true
          tags: ghcr.io/${{ github.repository }}:${{ github.sha }}

  deploy:
    needs: build-push
    runs-on: ubuntu-latest
    environment: production
    steps:
      - uses: azure/k8s-deploy@v4
        with:
          manifests: k8s/
          images: ghcr.io/${{ github.repository }}:${{ github.sha }}
```

## Troubleshooting Guide

### Common Failure Modes

| Issue | Root Cause | Solution |
|-------|-----------|----------|
| OOMKilled | Heap > container limit | Set -XX:MaxRAMPercentage |
| CrashLoopBackOff | App fails startup | Check logs, increase startup probe |
| ImagePullBackOff | Registry auth issue | Verify credentials |
| Pending pods | Insufficient resources | Check node capacity |
| Slow startup | Heavy initialization | Lazy loading |
| CPU throttling | CPU limit too low | Increase limit |

### Debug Checklist

```markdown
□ Check pod status: kubectl get pods -o wide
□ View pod logs: kubectl logs <pod> --previous
□ Describe pod: kubectl describe pod <pod>
□ Exec into pod: kubectl exec -it <pod> -- sh
□ Check events: kubectl get events --sort-by='.lastTimestamp'
□ View metrics: kubectl top pods
□ Check HPA status: kubectl get hpa
```

### JVM Container Settings

```bash
JAVA_OPTS="
  -XX:+UseContainerSupport
  -XX:MaxRAMPercentage=75.0
  -XX:+ExitOnOutOfMemoryError
  -XX:+HeapDumpOnOutOfMemoryError
  -XX:+UseG1GC
"
```

## Usage Examples

```
# Invoke this agent
Task(subagent_type="java:08-java-devops")

# Example prompts
- "Create optimized Dockerfile for Spring Boot"
- "Set up Kubernetes deployment with HPA"
- "Configure GitHub Actions CI/CD"
- "Add Prometheus monitoring"
- "Debug OOMKilled pod"
```

## Bonded Skills

- **PRIMARY**: `java-docker` - Container optimization
- **SECONDARY**: `java-maven` - Build integration
- **SECONDARY**: `java-gradle` - Build integration

```

## File: commands\java_build.md
```
---
name: java-build
description: Build Java project with Maven or Gradle - compile, test, package
allowed-tools: Bash, Read
version: "3.0.0"

# Input Validation
parameters:
  skip_tests:
    type: boolean
    default: false
    description: Skip test execution
  goal:
    type: string
    enum: [compile, test, package, install, deploy]
    default: package
  profile:
    type: string
    description: Build profile to activate
---

# Java Build Command

Build the Java project and run tests.

## What This Command Does

1. **Detect Build Tool** - Find Maven or Gradle wrapper
2. **Clean Build** - Remove previous artifacts
3. **Compile** - Compile source code
4. **Test** - Run unit tests
5. **Package** - Create JAR/WAR
6. **Report** - Show build summary

## Usage

```bash
/java-build                    # Build and test
/java-build --skip-tests       # Build without tests
/java-build --package          # Create JAR/WAR
/java-build --install          # Install to local repo
/java-build --profile prod     # Use production profile
```

## Build Goals

| Goal | Maven | Gradle | Description |
|------|-------|--------|-------------|
| compile | compile | classes | Compile sources |
| test | test | test | Run tests |
| package | package | jar | Create artifact |
| install | install | publishToMavenLocal | Install locally |

## Options

| Option | Description |
|--------|-------------|
| `--skip-tests` | Build without tests |
| `--package` | Create JAR/WAR |
| `--install` | Install to local repository |
| `--profile <name>` | Activate build profile |
| `--debug` | Enable debug output |

## Output Example

```
=== Java Build ===

[INFO] Building my-app 1.0.0-SNAPSHOT
[INFO] Compiling 42 source files
[INFO] Running 28 tests

Tests:
  ✓ 28 tests passed
  ✗ 0 tests failed
  ⊘ 2 tests skipped

[INFO] Building jar: target/my-app-1.0.0-SNAPSHOT.jar

BUILD SUCCESS (32s)
```

## Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| Compilation error | Syntax error | Check error line |
| Test failure | Assertion failed | Review test output |
| Dependency not found | Missing repo | Check repositories |
| Out of memory | Heap too small | Set MAVEN_OPTS |

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Build success |
| 1 | Compilation failed |
| 2 | Tests failed |

## Related Commands

- `/java-check` - Verify environment
- `/java-debug` - Debug issues

```

## File: commands\java_check.md
```
---
name: java-check
description: Check Java environment - JDK, Maven, Gradle versions and configuration
allowed-tools: Bash, Read
version: "3.0.0"

# Input Validation
parameters:
  verbose:
    type: boolean
    default: false
    description: Show detailed output
---

# Java Check Command

Verify Java development environment is properly configured.

## What This Command Does

1. **JDK Check** - Verify Java version (recommend 17 or 21)
2. **JAVA_HOME** - Validate environment variable
3. **Maven Check** - Verify installation and version
4. **Gradle Check** - Verify installation and version
5. **Environment Summary** - Display configuration status

## Usage

```bash
/java-check            # Quick check
/java-check --verbose  # Detailed output
```

## Expected Output

```
=== Java Environment Check ===

JDK:
  ✓ Version: 21.0.1
  ✓ JAVA_HOME: /usr/lib/jvm/java-21
  ✓ javac available

Build Tools:
  ✓ Maven: 3.9.6
  ✓ Gradle: 8.5

Status: Environment Ready
```

## Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| java not found | Not in PATH | Add JAVA_HOME/bin to PATH |
| JAVA_HOME not set | Missing variable | Export JAVA_HOME |
| Maven not found | Not installed | Install via sdkman or apt |
| Wrong Java version | Multiple JDKs | Use update-alternatives |

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Environment OK |
| 1 | Java not found |
| 2 | Build tools missing |

## Related Commands

- `/java-new` - Create new project
- `/java-build` - Build project

```

## File: commands\java_debug.md
```
---
name: java-debug
description: Debug Java applications - analyze errors, memory issues, performance
allowed-tools: Bash, Read, WebSearch
version: "3.0.0"

# Input Validation
parameters:
  error_type:
    type: string
    enum: [OutOfMemoryError, ClassNotFoundException, NoSuchMethodError, StackOverflowError, NullPointerException, all]
    description: Specific error type to debug
  pid:
    type: integer
    description: Process ID for live debugging
---

# Java Debug Command

Diagnose and troubleshoot Java application issues.

## What This Command Does

1. **Error Analysis** - Parse and explain stack traces
2. **Common Errors** - Identify known issue patterns
3. **JVM Diagnostics** - Check memory, threads, GC
4. **Solutions** - Provide targeted fixes
5. **Prevention** - Best practices to avoid issues

## Usage

```bash
/java-debug                       # Analyze current error
/java-debug OutOfMemoryError      # Debug OOM specifically
/java-debug --pid 12345           # Debug running process
/java-debug ClassNotFoundException # Debug classpath issues
```

## Common Issues

### OutOfMemoryError

**Causes:**
- Heap too small
- Memory leak
- Large objects

**Diagnosis:**
```bash
# Heap dump
jmap -dump:format=b,file=heap.hprof <pid>

# GC logs
-Xlog:gc*:file=gc.log

# Heap settings
java -Xms512m -Xmx2g -XX:+HeapDumpOnOutOfMemoryError
```

### ClassNotFoundException

**Causes:**
- Missing dependency
- Wrong classpath
- Shading issues

**Diagnosis:**
```bash
# Check classpath
java -cp . -verbose:class MyApp

# Dependency tree
mvn dependency:tree
gradle dependencies
```

### NoSuchMethodError

**Causes:**
- Version conflict
- Incompatible dependency
- Classpath order

**Diagnosis:**
```bash
# Find duplicates
mvn dependency:tree -Dincludes=groupId:artifactId
gradle dependencyInsight --dependency name
```

### StackOverflowError

**Causes:**
- Infinite recursion
- Deep call stack
- Circular references

**Fix:**
- Add base case to recursion
- Use iteration instead
- Increase stack size: `-Xss2m`

### NullPointerException

**Causes:**
- Null reference access
- Missing initialization
- Bad API return

**Fix:**
- Use Optional
- Add null checks
- Use @NonNull annotations

## JVM Diagnostic Commands

```bash
# Thread dump
jstack -l <pid>

# Heap info
jmap -heap <pid>

# GC stats
jstat -gcutil <pid> 1000

# Flight recording
jcmd <pid> JFR.start duration=60s filename=recording.jfr

# Full diagnostics
jcmd <pid> VM.info
```

## Troubleshooting Decision Tree

```
Error occurred?
├── OutOfMemoryError
│   ├── Heap? → Increase -Xmx, check leaks
│   └── Metaspace? → Increase -XX:MaxMetaspaceSize
├── ClassNotFoundException
│   ├── At runtime? → Check classpath
│   └── At startup? → Missing dependency
├── NoSuchMethodError
│   └── Check for version conflicts
└── Performance issue
    ├── High CPU? → Profile with async-profiler
    └── Slow response? → Check GC pauses
```

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Diagnosis complete |
| 1 | Process not found |
| 2 | Insufficient permissions |

## Related Commands

- `/java-build` - Build project
- `/java-check` - Check environment

```

## File: commands\java_new.md
```
---
name: java-new
description: Create a new Java project with Maven or Gradle
allowed-tools: Bash, Read, Write
version: "3.0.0"

# Input Validation
parameters:
  project_name:
    type: string
    required: true
    pattern: "^[a-z][a-z0-9-]*$"
    description: Project name (lowercase, hyphens allowed)
  build_tool:
    type: string
    enum: [maven, gradle]
    default: maven
  framework:
    type: string
    enum: [plain, spring-boot, quarkus, library]
    default: plain
  java_version:
    type: string
    default: "21"
    enum: ["17", "21"]
---

# Java New Command

Create a new Java project with proper structure and dependencies.

## What This Command Does

1. **Project Type Selection** - Choose Maven or Gradle
2. **Framework Selection** - Spring Boot, Quarkus, or plain Java
3. **Directory Structure** - Create standard Java layout
4. **Build Configuration** - Generate pom.xml or build.gradle.kts
5. **Git Init** - Initialize git repository with .gitignore

## Usage

```bash
/java-new my-app                        # Plain Maven project
/java-new my-app --spring-boot          # Spring Boot with Maven
/java-new my-app --gradle --spring-boot # Spring Boot with Gradle
/java-new my-lib --library              # Library project
```

## Project Types

### Plain Java
- Basic Maven/Gradle project
- JUnit 5 for testing
- No framework dependencies

### Spring Boot
- Spring Boot 3.x starter
- Web, actuator included
- Application class generated

### Library
- No main class
- Configured for publishing
- Test dependencies only

### Multi-module (advanced)
- Parent POM with modules
- Shared dependencies
- Separate subprojects

## Generated Structure

```
my-app/
├── pom.xml (or build.gradle.kts)
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/example/myapp/
│   │   │       └── Application.java
│   │   └── resources/
│   │       └── application.yml
│   └── test/
│       └── java/
│           └── com/example/myapp/
│               └── ApplicationTest.java
├── .gitignore
└── README.md
```

## Options

| Option | Description |
|--------|-------------|
| `--maven` | Use Maven (default) |
| `--gradle` | Use Gradle with Kotlin DSL |
| `--spring-boot` | Include Spring Boot starter |
| `--library` | Create library project |
| `--java 17` | Specify Java version |

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Project created |
| 1 | Invalid project name |
| 2 | Directory exists |

## Related Commands

- `/java-check` - Verify environment
- `/java-build` - Build project

```

## File: hooks\hooks.json
```
{
  "hooks": {}
}

```

