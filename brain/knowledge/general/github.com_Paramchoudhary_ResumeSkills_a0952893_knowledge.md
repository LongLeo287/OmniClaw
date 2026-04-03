---
id: github.com-paramchoudhary-resumeskills-a0952893-kn
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:10.961182
---

# KNOWLEDGE EXTRACT: github.com_Paramchoudhary_ResumeSkills_a0952893
> **Extracted on:** 2026-04-01 13:59:23
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007523588/github.com_Paramchoudhary_ResumeSkills_a0952893

---

## File: `CONTRIBUTING.md`
```markdown
# Contributing to Resume Skills

Thank you for your interest in contributing to Resume Skills! This collection helps job seekers optimize their resumes and job search process with Claude Code.

## Ways to Contribute

### 1. Improve Existing Skills

- Fix typos, grammar, or unclear language
- Add more examples (before/after, industry-specific)
- Improve frameworks or methodologies
- Add edge cases or special situations
- Update for current job market trends

### 2. Create New Skills

Have an idea for a new skill? We welcome contributions for:

- Industry-specific resume optimization (healthcare, legal, nonprofit, etc.)
- Role-specific skills (sales, engineering specialties, etc.)
- International job search (different countries, visa considerations)
- Specialized documents (bios, one-pagers, networking materials)
- Career development (performance reviews, promotions, etc.)

### 3. Report Issues

- Skills not working as expected
- Outdated information
- Missing use cases
- Confusing instructions

## Skill File Format

All skills must follow this structure:

```markdown
# Skill Name

## When to Use This Skill

[Describe trigger conditions - when Claude should use this skill]
- Use when the user mentions [specific keywords]
- Use when the user wants to [specific action]
- Use when working with [specific content]

## Core Capabilities

[Brief bullet list of what this skill does]

## [Main Content Sections]

Include:
- Overview & Context
- Frameworks & Methodologies  
- Step-by-step Process
- Output Requirements/Formats
- Examples (Before/After)
- Edge Cases & Special Situations
- Implementation Checklist
```

## Guidelines for Quality

### Do:
- Include specific, actionable instructions
- Provide real-world examples
- Show before/after transformations
- Include checklists and frameworks
- Consider edge cases
- Test your skill with actual resumes

### Don't:
- Be vague or generic
- Copy content from copyrighted sources
- Include outdated practices
- Make claims without backing them up
- Ignore ATS compatibility

## How to Submit

### For Small Changes (Typos, Minor Improvements)

1. Fork the repository
2. Make your changes
3. Submit a pull request with a clear description

### For New Skills

1. Open an issue first to discuss your idea
2. Get feedback from maintainers
3. Fork and create the skill following the format
4. Test thoroughly
5. Submit pull request

### Pull Request Process

1. **Title**: Clear, descriptive (e.g., "Add healthcare-resume-optimizer skill")
2. **Description**: Explain what and why
3. **Testing**: Describe how you tested the skill
4. **Examples**: Include sample inputs/outputs if applicable

## Code of Conduct

- Be respectful and constructive
- Focus on helping job seekers
- Provide honest, accurate information
- Credit sources when applicable

## Questions?

Open an issue with the "question" label and we'll help!

---

Thank you for helping make Resume Skills better for everyone! 🎯
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2026 Resume Skills

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
# Resume Skills for Claude Code

A collection of AI agent skills focused on resume optimization, job applications, and career development. Built for job seekers, career changers, and professionals who want Claude Code to help with resume writing, ATS optimization, interview prep, and strategic job search.

## What are Skills?

Skills are markdown files that give AI agents specialized knowledge and workflows for specific tasks. When you add these to your project, Claude Code can recognize when you're working on resume and job search tasks and apply the right frameworks and best practices.

## Available Skills

| Skill | Description |
|-------|-------------|
| [resume-ats-optimizer](/skills/resume-ats-optimizer) | Optimize resumes for Applicant Tracking Systems, check ATS compatibility, analyze keyword match |
| [resume-bullet-writer](/skills/resume-bullet-writer) | Transform weak bullets into achievement-focused statements with metrics and impact |
| [job-description-analyzer](/skills/job-description-analyzer) | Analyze job postings, calculate match scores, identify gaps, create application strategy |
| [resume-tailor](/skills/resume-tailor) | Customize resume for specific job postings while maintaining truthfulness |
| [cover-letter-generator](/skills/cover-letter-generator) | Create personalized, compelling cover letters from resume + job description |
| [linkedin-profile-optimizer](/skills/linkedin-profile-optimizer) | Sync resume with LinkedIn, optimize for searchability and engagement |
| [interview-prep-generator](/skills/interview-prep-generator) | Generate STAR stories, practice questions, talking points from resume |
| [salary-negotiation-prep](/skills/salary-negotiation-prep) | Research market rates, build negotiation strategy, create counter-offer scripts |
| [tech-resume-optimizer](/skills/tech-resume-optimizer) | Optimize resumes for software engineering, PM, and technical roles |
| [executive-resume-writer](/skills/executive-resume-writer) | Create C-suite and VP level resumes emphasizing strategic leadership |
| [career-changer-translator](/skills/career-changer-translator) | Translate skills from one industry to another, identify transferable skills |
| [resume-quantifier](/skills/resume-quantifier) | Find opportunities to add metrics, estimate when numbers unknown |
| [resume-formatter](/skills/resume-formatter) | Ensure ATS-friendly formatting, create clean scannable layouts |
| [portfolio-case-study-writer](/skills/portfolio-case-study-writer) | Transform resume bullets into detailed portfolio case studies |
| [academic-cv-builder](/skills/academic-cv-builder) | Format CVs for academic positions with publications, grants, teaching |
| [reference-list-builder](/skills/reference-list-builder) | Format professional references properly and prepare reference materials |
| [offer-comparison-analyzer](/skills/offer-comparison-analyzer) | Compare multiple job offers side-by-side with total compensation analysis |
| [resume-version-manager](/skills/resume-version-manager) | Track different resume versions, maintain master resume, manage tailored versions |
| [creative-portfolio-resume](/skills/creative-portfolio-resume) | Balance visual design with ATS compatibility for creative roles |
| [resume-section-builder](/skills/resume-section-builder) | Create targeted sections optimized for different experience levels and roles |

## Installation

### Option 1: CLI Install (Recommended)

```bash
# Install all 20 skills globally (works across all projects)
npx skills add Paramchoudhary/ResumeSkills -g -y

# Install to current project only
npx skills add Paramchoudhary/ResumeSkills -y

# List installed skills
npx skills list

# List global skills
npx skills list --global
```

### Option 2: Manual Install

```bash
# Clone and copy to skills folder
git clone https://github.com/Paramchoudhary/ResumeSkills.git
mkdir -p ~/.cursor/skills
cp -r ResumeSkills/skills/* ~/.cursor/skills/
```

### Option 3: Direct Download

Download individual skill files from the `/skills` directory and add them to your AI agent's skills folder.

### Uninstall

```bash
# Remove individual skills by name
npx skills remove resume-ats-optimizer
npx skills remove resume-bullet-writer

# Or remove all skills from a directory
rm -rf ~/.agents/skills/resume-*
rm -rf ~/.cursor/skills/resume-*
```

## Supported AI Agents

These skills work with multiple AI coding assistants:

- **Cursor** (IDE)
- **Claude Code** (CLI)
- **Windsurf**
- **Codex**
- **Gemini CLI**
- **Amp, Antigravity, Augment** and 30+ more

## Usage

Once installed, just ask your AI assistant to help with resume tasks:

```
"Optimize my resume for ATS"
→ Uses resume-ats-optimizer skill

"Improve my resume bullets"
→ Uses resume-bullet-writer skill

"Should I apply to this job?" + paste job description
→ Uses job-description-analyzer skill

"Write me a cover letter for this role"
→ Uses cover-letter-generator skill

"Prep me for an interview at Google"
→ Uses interview-prep-generator skill
```

## Skill Categories

### Resume Optimization
- `resume-ats-optimizer` - Pass ATS systems
- `resume-bullet-writer` - Write achievement-focused bullets
- `resume-quantifier` - Add metrics and numbers
- `resume-formatter` - Clean, scannable formatting
- `resume-section-builder` - Targeted section creation

### Job Search Strategy
- `job-description-analyzer` - Match analysis and strategy
- `resume-tailor` - Customize for specific jobs
- `resume-version-manager` - Track multiple versions
- `offer-comparison-analyzer` - Compare job offers

### Supporting Documents
- `cover-letter-generator` - Personalized cover letters
- `linkedin-profile-optimizer` - LinkedIn optimization
- `portfolio-case-study-writer` - Portfolio content
- `reference-list-builder` - Professional references

### Interview & Negotiation
- `interview-prep-generator` - STAR stories and practice
- `salary-negotiation-prep` - Negotiation strategy

### Specialized Roles
- `tech-resume-optimizer` - Engineering/PM/technical
- `executive-resume-writer` - C-suite/VP
- `academic-cv-builder` - Academic positions
- `creative-portfolio-resume` - Design/creative roles
- `career-changer-translator` - Career transitions

## Why These Skills Matter

**The Problem:**
- 75% of resumes rejected by ATS before humans see them
- Average job gets 250 applications
- Most resumes have weak bullets with no metrics
- Job seekers apply to wrong jobs, waste time

**The Solution:**
- Pass ATS with optimized formatting and keywords
- Stand out with achievement-focused bullets
- Apply strategically to right-fit roles
- Get interviews faster with tailored applications

**The Results:**
- 2-3x more interviews per application
- Higher quality responses
- Faster job search (2 months saved on average)
- Better salary negotiations ($10K+ higher offers)

## Quick Start Examples

### Example 1: Full Resume Optimization

```
User: Here's my resume [paste]. I'm applying to data scientist roles. Help me optimize it.

Claude will:
1. Run ATS compatibility check
2. Analyze against common data scientist job requirements
3. Improve bullet points with metrics
4. Suggest keyword additions
5. Format for ATS compatibility
```

### Example 2: Job-Specific Tailoring

```
User: Here's a job description [paste] and my resume [paste]. Should I apply?

Claude will:
1. Calculate match score
2. Identify gaps and strengths
3. Flag any red flags in posting
4. Provide resume customization strategy
5. Generate cover letter talking points
```

### Example 3: Interview Preparation

```
User: I have an interview at [Company] for [Role]. Here's my resume. Help me prepare.

Claude will:
1. Generate STAR stories from your experience
2. Predict likely interview questions
3. Create talking points for each bullet
4. Research company-specific prep
5. Prepare questions to ask
```

## Contributing

Found a way to improve a skill? Have a new skill to suggest? PRs and issues welcome!

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Ways to Contribute
- Improve existing skill instructions
- Add industry-specific examples
- Create new skills for specialized use cases
- Fix typos or clarify language
- Add translations

## License

MIT License - Use these skills however you want.

See [LICENSE](LICENSE) for details.

## About

Resume skills for Claude Code. ATS optimization, bullet writing, job matching, interview prep, and career development.

**Keywords:** resume, CV, ATS, job search, career, interview, cover letter, LinkedIn, salary negotiation, job application

---

*Built with care for job seekers everywhere. Good luck with your search!*
```

## File: `skills/academic-cv-builder/SKILL.md`
```markdown
---
name: Academic CV Builder
description: Format CVs for academic positions with publications, grants, and teaching
---

# Academic CV Builder

## When to Use This Skill

Use this skill when the user:
- Is applying for academic positions (faculty, research, postdoc)
- Needs to create or update a curriculum vitae
- Wants to format publications, grants, and teaching experience
- Is in academia or transitioning to academic careers
- Mentions: "academic CV", "curriculum vitae", "faculty position", "research CV", "professor resume"

## Core Capabilities

- Structure CVs for academic positions
- Format publications, presentations, and grants
- Organize teaching and research experience
- Include appropriate academic sections
- Tailor for different academic roles (tenure-track, postdoc, lecturer)
- Balance research, teaching, and service

## Academic CV vs. Resume

| Resume | Academic CV |
|--------|------------|
| 1-2 pages | 2-20+ pages (length increases with career) |
| Highlights relevant experience | Comprehensive record |
| Results-focused | Scholarship-focused |
| Industry keywords | Disciplinary expertise |
| Skills section prominent | Publications prominent |
| Education minimal | Education detailed |

## Standard Academic CV Sections

### Typical Order

```
1. Contact Information
2. Education
3. Research/Academic Positions
4. Publications
5. Presentations
6. Grants & Funding
7. Teaching Experience
8. Mentoring
9. Service
10. Professional Memberships
11. Honors & Awards
12. References (or "Available upon request")
```

### Section Order Varies By:
- **Research position:** Publications, grants, research experience first
- **Teaching position:** Teaching, course development first
- **Administrative position:** Leadership, service first

## Section-by-Section Guide

### 1. Contact Information

```
FIRST MIDDLE LAST, Ph.D.
Department of [Field]
[University Name]
[Building, Room Number]
[City, State ZIP]

Email: email@university.edu
Phone: (555) 123-4567
Web: www.yoursite.edu
ORCID: 0000-0000-0000-0000
```

### 2. Education

**Format:** Degree, Field, Institution, Year

```
EDUCATION

Ph.D. in Molecular Biology, Stanford University, 2019
  Dissertation: "Title of Your Dissertation"
  Advisor: Dr. Jane Smith
  Committee: Dr. A, Dr. B, Dr. C

M.S. in Biology, UC Berkeley, 2015

B.S. in Biochemistry, UCLA, 2013
  Summa Cum Laude
```

**Include:**
- All degrees (in reverse chronological order)
- Dissertation/thesis title
- Advisor(s)
- Committee members (for PhD)
- Honors (cum laude, etc.)
- Relevant minors or certificates

### 3. Research/Academic Positions

```
ACADEMIC APPOINTMENTS

Assistant Professor of Biology, University of Michigan, 2022-Present
  Department of Molecular, Cellular, and Developmental Biology

Postdoctoral Fellow, MIT, 2019-2022
  Advisor: Dr. John Doe
  Lab: Computational Biology Lab

Graduate Research Assistant, Stanford University, 2014-2019
  Advisor: Dr. Jane Smith
```

### 4. Publications

**Most Important Section for Research Positions**

#### Formatting Options

**Option 1: Numbered List (Common in Sciences)**
```
PUBLICATIONS

Peer-Reviewed Journal Articles

15. Last, F.M., Co-Author, A.B., & Senior, C.D. (2023). Article title. Journal Name, 45(2), 123-145. doi:10.1000/xyz

14. Last, F.M., & Co-Author, A.B. (2022). Article title. Journal Name, 44(1), 10-25. doi:10.1000/abc
```

**Option 2: Categories (Useful for Multiple Types)**
```
PUBLICATIONS

Peer-Reviewed Journal Articles (15)

Book Chapters (3)

Books (1)

Under Review (2)

In Preparation (3)
```

**Formatting Details:**
- **Bold your name** in author lists
- Include DOIs when available
- Note impact factors if requested/relevant
- Indicate student co-authors with asterisk*
- Some fields expect reverse chronological; others expect chronological

**Categories to Consider:**
- Peer-reviewed journal articles
- Books and book chapters
- Conference proceedings
- Technical reports
- Non-peer-reviewed publications
- Works under review
- Works in preparation

### 5. Presentations

```
PRESENTATIONS

Invited Talks

"Talk Title," Conference Name, Location, Date.
"Talk Title," Department Seminar, University Name, Date.

Conference Presentations

"Poster/Talk Title," Conference Name, Location, Date. [Poster/Oral]
```

**Categorize By:**
- Invited talks (keynotes, seminars)
- Conference presentations
- Campus talks
- Public lectures/outreach

### 6. Grants & Funding

```
GRANTS AND FUNDING

Awarded

NIH R01 (Co-PI), "Project Title," 2023-2028, $2.5M total ($500K to my lab)

NSF CAREER Award (PI), "Project Title," 2022-2027, $650,000

Internal Grant (PI), "Project Title," 2021, $25,000

Pending

NIH R21 (PI), "Project Title," submitted January 2024

Not Funded (Optional)

[Some fields expect you to list unfunded submissions]
```

**Include:**
- Funding agency and mechanism
- Your role (PI, Co-PI, Co-I)
- Project title
- Dates
- Total amount (and amount to your lab if split)

### 7. Teaching Experience

```
TEACHING EXPERIENCE

Courses Taught

BIOL 301: Molecular Biology (Instructor of Record)
  University of Michigan, Fall 2022, Fall 2023
  Enrollment: 45 students
  Developed new course curriculum

BIOL 101: Introduction to Biology (Lab Instructor)
  Stanford University, 2015-2018
  
Guest Lectures

"Topic," Course Name, Professor's Name, University, Date
```

**Include:**
- Course number and title
- Your role (Instructor, TA, Guest Lecturer)
- Institution and dates
- Enrollment numbers
- Course development or new preparations
- Teaching evaluations summary (if strong)

### 8. Mentoring

```
MENTORING

Graduate Students
- Student Name (Ph.D. expected 2025), Dissertation: "Title"
- Student Name (Ph.D. 2023), Current position: Postdoc at MIT

Postdoctoral Fellows
- Name (2021-2023), Current position: Assistant Professor at X

Undergraduate Researchers
- Name (2022-2023), Thesis: "Title," Current: PhD program at Y
- Name (2021-2022), Thesis: "Title," Current: Industry position
```

### 9. Service

```
SERVICE

To the Profession
- Editorial Board Member, Journal Name, 2022-Present
- Grant Reviewer, NIH Study Section XYZ, 2023
- Conference Organizer, Conference Name, 2022

To the University
- Graduate Admissions Committee, 2022-Present
- Faculty Search Committee, 2023
- Curriculum Committee, 2022-2023

To the Department
- Seminar Coordinator, 2022-Present
- Undergraduate Advisor, 2022-Present
```

### 10. Professional Memberships

```
PROFESSIONAL MEMBERSHIPS

American Society for Cell Biology (ASCB), 2015-Present
Society for Neuroscience (SfN), 2018-Present
```

### 11. Honors & Awards

```
HONORS AND AWARDS

NSF CAREER Award, 2022
Best Paper Award, Conference Name, 2021
Outstanding Graduate Student Award, Stanford University, 2018
National Science Foundation Graduate Research Fellowship, 2015-2018
Phi Beta Kappa, 2013
```

## Role-Specific Emphasis

### Tenure-Track Faculty

**Emphasize:**
1. Publications (especially recent, high-impact)
2. Grants (especially independent funding)
3. Research trajectory and vision
4. Teaching experience
5. Mentoring record

### Postdoctoral Position

**Emphasize:**
1. Publications (from PhD and postdoc)
2. Research experience and skills
3. Collaboration experience
4. Future research potential
5. Any funding/fellowships

### Lecturer/Teaching Faculty

**Emphasize:**
1. Teaching experience (courses, evaluations)
2. Course development
3. Pedagogical training
4. Mentoring undergraduates
5. Teaching awards

### Research Scientist

**Emphasize:**
1. Publications
2. Technical skills
3. Grant writing experience
4. Collaboration record
5. Relevant research experience

## Discipline-Specific Conventions

### Sciences (Biology, Chemistry, Physics)
- Author order matters (first author, last author = senior)
- Impact factors sometimes included
- Numbered publication lists common
- Conference presentations less weighted than publications

### Humanities (History, Literature, Philosophy)
- Single-author publications highly valued
- Book publications crucial
- Conference presentations important
- Public scholarship valued

### Social Sciences
- Both solo and collaborative work valued
- Mix of journal articles and books
- Funded research important
- Policy impact valued

## CV Length Guidelines

| Career Stage | Expected Length |
|--------------|-----------------|
| Graduate Student | 2-4 pages |
| Postdoc | 3-6 pages |
| Early Career Faculty | 5-10 pages |
| Mid-Career Faculty | 10-20 pages |
| Senior Faculty | 15-30+ pages |

**Rule:** Your CV grows throughout your career. Don't pad, but don't artificially constrain length.

## Output Format

When creating an academic CV:

```markdown
# ACADEMIC CV STRUCTURE FOR [NAME]

## Recommended Section Order
[Based on position type and field]

1. [Section]
2. [Section]
...

## Section Content

### Education
[Formatted education section]

### Publications
[Formatted with appropriate style for field]

### [Other Sections]
[Formatted content]

---

## Formatting Notes
- [Field-specific conventions to follow]
- [Style guide recommendations]

## Things to Add/Update
- [ ] [Missing item]
- [ ] [Item needing update]
```

## Academic CV Checklist

- ✅ Contact information complete (including ORCID if applicable)
- ✅ Education includes all degrees, advisors, dissertations
- ✅ Publications properly formatted with your name highlighted
- ✅ All grants listed with amounts and your role
- ✅ Teaching experience comprehensive
- ✅ Service documented
- ✅ Consistent formatting throughout
- ✅ Reverse chronological order (usually)
- ✅ No unexplained gaps
- ✅ Updated within last 6 months
```

## File: `skills/career-changer-translator/SKILL.md`
```markdown
---
name: Career Changer Translator
description: Translate skills from one industry to another, identify transferable skills
---

# Career Changer Translator

## When to Use This Skill

Use this skill when the user:
- Is switching careers or industries
- Wants to translate their experience for a new field
- Needs help identifying transferable skills
- Mentions: "career change", "switching careers", "new industry", "transferable skills", "pivot"

## Core Capabilities

- Identify transferable skills across industries
- Translate experience into new industry language
- Reframe achievements for target roles
- Bridge skill gaps strategically
- Position career changes positively
- Create compelling change narratives

## The Career Change Challenge

**Why Career Changes Are Hard:**
- Experience doesn't directly map to new role
- Lacking industry-specific keywords
- Recruiters prefer "safe" candidates
- Need to explain "why" convincingly
- Competing against people with direct experience

**The Solution:**
- Focus on transferable skills
- Learn the new industry's language
- Leverage adjacent experiences
- Build bridge experiences
- Tell a compelling story

## Transferable Skills Framework

### Universal Transferable Skills

**Leadership & Management**
- Team leadership
- Project management
- Budget oversight
- Strategic planning
- Performance management
- Stakeholder management

**Communication**
- Presentation skills
- Written communication
- Client relations
- Cross-functional collaboration
- Negotiation
- Conflict resolution

**Analytical**
- Data analysis
- Problem-solving
- Research
- Process improvement
- Decision-making
- Strategic thinking

**Technical/Operational**
- Process design
- Systems implementation
- Quality assurance
- Training and development
- Vendor management
- Operations management

## Career Change Translation Examples

### Teacher → Corporate Trainer / L&D

**Teaching Experience:**
- "Taught 25 students in 5th grade classroom"

**Translated:**
- "Designed and delivered curriculum for 25 learners, achieving 95% proficiency on standardized assessments through differentiated instruction and data-driven intervention strategies"

**Key Translations:**
| Teaching Term | Corporate Term |
|--------------|----------------|
| Lesson plans | Training curriculum |
| Students | Learners |
| Classroom management | Group facilitation |
| Parent conferences | Stakeholder communication |
| Assessments | Learning evaluations |
| IEPs | Individual development plans |

### Military → Corporate

**Military Experience:**
- "Commanded platoon of 30 soldiers in combat operations"

**Translated:**
- "Led cross-functional team of 30 through high-stakes operations in ambiguous environments, managing $2M in equipment and achieving 100% mission completion rate"

**Key Translations:**
| Military Term | Corporate Term |
|--------------|----------------|
| Platoon/Unit | Team/Department |
| Mission | Project/Initiative |
| Operations | Programs |
| Intel | Data/Analytics |
| Briefing | Presentation |
| Command | Leadership |
| Deployment | Implementation |

### Retail → Sales/Account Management

**Retail Experience:**
- "Sold products to customers and met sales targets"

**Translated:**
- "Consistently exceeded sales targets by 125%, generating $500K annual revenue through consultative selling and relationship building with 50+ repeat customers"

**Key Translations:**
| Retail Term | Corporate Term |
|------------|----------------|
| Customers | Clients/Accounts |
| Store sales | Revenue generation |
| Customer service | Account management |
| Upselling | Cross-selling |
| Returns | Issue resolution |
| Visual merchandising | Brand presentation |

### Hospitality → Customer Success

**Hospitality Experience:**
- "Managed front desk and handled guest complaints"

**Translated:**
- "Served as primary customer contact for 100+ daily guests, resolving escalated issues with 95% satisfaction rate and implementing feedback processes that improved NPS by 15 points"

**Key Translations:**
| Hospitality Term | Corporate Term |
|-----------------|----------------|
| Guests | Customers/Clients |
| Reservations | Account management |
| Guest satisfaction | Customer success |
| Complaints | Escalations |
| Concierge services | Customer support |
| Event planning | Project management |

### Healthcare → Tech/Pharma

**Healthcare Experience:**
- "Provided patient care and maintained medical records"

**Translated:**
- "Delivered patient-centered care to 20+ daily cases, maintaining 100% compliance with HIPAA protocols and utilizing EMR systems (Epic) for accurate documentation and care coordination"

**Key Translations:**
| Healthcare Term | Corporate Term |
|----------------|----------------|
| Patient care | Client service |
| EMR/EHR | CRM/Database systems |
| Care coordination | Project coordination |
| Clinical protocols | Standard operating procedures |
| Patient outcomes | Performance metrics |
| Rounds | Status meetings |

## The Career Change Resume Strategy

### 1. Lead with Transferable Summary

**Format:**
"[Target Role] professional with [X] years of [transferable skill] experience. Background in [previous field] provides unique perspective on [relevant aspect]. Skilled in [transferable skill 1], [transferable skill 2], and [transferable skill 3]."

**Example (Teacher → L&D):**
"Learning & Development professional with 8 years designing and delivering curriculum for diverse audiences. Background in education provides deep expertise in learning science, assessment design, and adult learning principles. Skilled in instructional design, facilitation, and measuring learning outcomes."

### 2. Use a Functional/Hybrid Resume Format

**Structure:**
```
Professional Summary (targeted)
Core Competencies (transferable skills)
Relevant Experience (grouped by skill)
Additional Experience (chronological)
Education & Certifications
```

**Group by Transferable Function:**
```
PROJECT MANAGEMENT EXPERIENCE
[Bullet from Job 1]
[Bullet from Job 2]
[Bullet from Job 3]

LEADERSHIP & TEAM DEVELOPMENT
[Bullet from Job 1]
[Bullet from Job 2]

CLIENT RELATIONSHIP MANAGEMENT
[Bullet from Job 1]
[Bullet from Job 2]
```

### 3. Build Bridge Experiences

**Ways to Add Relevant Experience:**
- Volunteer work in target field
- Freelance/consulting projects
- Relevant certifications
- Side projects
- Professional organizations
- Coursework

**Example:**
```
BRIDGE EXPERIENCE

Volunteer Marketing Lead | Nonprofit XYZ | 2023-Present
- Designed social media strategy increasing engagement by 150%
- Created content calendar and managed 3 volunteer content creators

Google Digital Marketing Certificate | 2023
- Completed 200+ hour program covering SEO, SEM, Analytics, and Social Media
```

## Addressing the "Why" Question

**You will be asked:** "Why are you making this change?"

**Good Reasons:**
- Natural evolution of interests
- Discovered passion through exposure
- Specific experience that sparked interest
- Skills naturally translate
- Industry changes made you reconsider
- Seeking growth not available in current path

**Bad Reasons (Don't Say):**
- "I'm burned out"
- "I hate my current job"
- "I want more money"
- "It seems easier"

### Story Framework

```
[DISCOVERY]: "Through [experience], I discovered my passion for [new field]..."

[CONNECTION]: "I realized that my experience in [old field] gave me a unique perspective on [new field] because..."

[ACTION]: "To prepare for this transition, I've [certifications, projects, volunteering]..."

[VISION]: "I'm excited to bring my [transferable skill] expertise to [target company/industry] because..."
```

## Industry-Specific Career Change Paths

### Into Tech

**Best Entry Points:**
- Customer Success (from any client-facing role)
- Technical Project Manager (from any PM role)
- Sales/Account Executive (from any sales role)
- Product Management (from domain expertise)
- Technical Writing (from any writing role)

**Bridge Activities:**
- Learn SQL, basic coding, or relevant tools
- Get certifications (Google, Salesforce, AWS)
- Build personal projects
- Attend tech meetups
- Volunteer for tech nonprofits

### Into Finance

**Best Entry Points:**
- Operations (from any process-oriented role)
- Compliance (from any regulated industry)
- Client Services (from relationship roles)
- Analysis (from any analytical role)

**Bridge Activities:**
- Excel/financial modeling certifications
- CFA or CFP study
- Financial analysis courses
- Industry networking

### Into Healthcare

**Best Entry Points:**
- Healthcare Administration (from any admin role)
- Medical Sales (from any sales role)
- Health IT (from any tech role)
- Patient Advocacy (from customer service)

**Bridge Activities:**
- Healthcare certifications
- HIPAA training
- Healthcare industry knowledge
- Volunteer at hospitals

## Output Format

When helping a career changer:

```markdown
# CAREER CHANGE TRANSLATION

## Current Background
**Field:** [Current industry]
**Role:** [Current function]
**Years:** [Experience]

## Target
**Field:** [Target industry]
**Role:** [Target function]

## Transferable Skills Identified
1. [Skill] → Relevant because: [explanation]
2. [Skill] → Relevant because: [explanation]
3. [Skill] → Relevant because: [explanation]

## Translation Guide

### Experience Reframes

**Original:** "[Their current bullet]"
**Translated:** "[Reframed for target industry]"
**Key changes:** [What was changed and why]

[Repeat for key bullets]

### Language Translations
| Your Current Language | Target Industry Language |
|----------------------|--------------------------|
| [Term] | [Translated term] |
| [Term] | [Translated term] |

## Gap Analysis

**Skills to Develop:**
- [Gap] → Suggestion: [How to bridge]
- [Gap] → Suggestion: [How to bridge]

**Bridge Experiences to Consider:**
- [Suggestion]
- [Suggestion]

## Your Career Change Story

[Draft of their "why" narrative]

## Recommended Resume Structure
[Guidance on format and organization]
```

## Key Reminders

1. **Lead with transferable skills**, not job titles
2. **Use target industry language** - translate everything
3. **Build bridges** - get any experience in target field
4. **Tell a compelling story** - make the change make sense
5. **Focus on value you bring** - your unique perspective is an asset
6. **Address concerns proactively** - don't let them wonder "why"
7. **Network in target field** - referrals help career changers most
```

## File: `skills/cover-letter-generator/SKILL.md`
```markdown
---
name: Cover Letter Generator
description: Create personalized, compelling cover letters from resume and job description
---

# Cover Letter Generator

## When to Use This Skill

Use this skill when the user wants to:
- Write a cover letter for a job application
- Create a personalized application letter
- Address specific job requirements in letter format
- Mentions: "cover letter", "application letter", "write cover letter", "letter for job"

Use AFTER analyzing job description to have clear talking points.

## Core Capabilities

- Generate personalized cover letters from resume + job description
- Match tone to company culture
- Address qualification gaps strategically
- Create compelling opening hooks
- Structure persuasive arguments for candidacy
- Maintain authenticity while selling effectively

## Cover Letter Philosophy

**The Problem:** Most cover letters are generic, boring, and add no value beyond the resume.

**The Solution:** A great cover letter should:
1. Show you've researched the company
2. Connect YOUR specific experience to THEIR specific needs
3. Address the "why you, why now, why here" questions
4. Add personality and context a resume can't convey

## The Perfect Cover Letter Structure

### Length & Format
- **Length:** 250-400 words (3-4 paragraphs)
- **Format:** Professional business letter style
- **Tone:** Confident but not arrogant, personalized but professional

### Structure Overview
```
[Your Contact Info]
[Date]
[Recipient Info]

Opening Paragraph: Hook + Position + Why This Company (2-3 sentences)

Body Paragraph 1: Your strongest qualification match (3-4 sentences)

Body Paragraph 2: Additional qualifications + address any gaps (3-4 sentences)

Closing Paragraph: Call to action + enthusiasm (2-3 sentences)

[Professional Sign-off]
```

## Opening Paragraph Strategies

The opening is critical - you have 5 seconds to grab attention.

### Hook Types (Choose One)

**1. Specific Company Knowledge**
```
"I was excited to see TechCorp's recent launch of your API marketplace - as a Product Manager who's spent 3 years building developer tools, I immediately saw how my experience could accelerate your platform growth."
```

**2. Mutual Connection**
```
"Sarah Chen on your engineering team mentioned you're looking for a PM to lead the payments initiative. Having worked with Sarah at [Previous Company] and led payment integrations at [Current Company], I'd love to discuss how I could contribute."
```

**3. Problem-Solver**
```
"Your job description mentions the challenge of aligning technical and business stakeholders - I've navigated this exact challenge, successfully launching 8 products by building shared roadmap visibility across engineering, sales, and executive teams."
```

**4. Impressive Achievement**
```
"Last year, I led a product that grew from 0 to 100K users in 6 months. I'm excited about the opportunity to bring that growth mindset to [Company]'s expanding product line."
```

**5. Industry Insight**
```
"The B2B payments space is at an inflection point, and [Company]'s approach to embedded finance positions you perfectly for the next wave. As someone who's been building in fintech for 5 years, I'd love to contribute to that growth."
```

### Opening Don'ts
- ❌ "I am writing to apply for..." (boring, obvious)
- ❌ "I am the perfect candidate..." (let them decide)
- ❌ "I saw your job posting on LinkedIn..." (generic)
- ❌ Starting with "I" (start with them or a hook)

## Body Paragraph Frameworks

### Body Paragraph 1: Direct Match

Connect your strongest experience to their top requirement.

**Formula:** [Their Need] + [Your Exact Experience] + [Specific Result]

```
Your focus on data-driven product decisions aligns perfectly with my approach. At [Company], I implemented a product analytics framework that increased feature adoption by 40% by identifying and prioritizing high-impact opportunities through A/B testing and user behavior analysis.
```

### Body Paragraph 2: Broader Value + Gap Handling

Show additional value and proactively address concerns.

**If you have gaps, address them:**
```
While my SQL experience is developing (currently completing DataCamp's SQL track), I bring strong analytical skills demonstrated through building Tableau dashboards that informed $2M in strategic decisions. I've consistently collaborated effectively with data teams and have a track record of quickly ramping on new tools.
```

**If no gaps, add more value:**
```
Beyond product management, I bring [relevant additional skill]. At [Company], this enabled me to [specific achievement]. I'm particularly drawn to [Company] because [specific reason showing research].
```

## Closing Paragraph

End with confidence and a clear call to action.

**Strong Closing Example:**
```
I'm excited about the opportunity to bring my [specific skill] experience to [Company]'s [specific initiative or product]. I'd welcome the chance to discuss how my background in [key area] could contribute to your team's goals. Thank you for considering my application.
```

**Elements of a Good Close:**
- Express genuine enthusiasm (for something specific)
- Reference a specific contribution you'd make
- Clear call to action (discuss, meet, etc.)
- Thank them

**Closing Don'ts:**
- ❌ "I look forward to hearing from you" (passive)
- ❌ "Please find my resume attached" (obvious)
- ❌ "I am available for an interview at your convenience" (desperate)

## Complete Cover Letter Template

```
[Your Name]
[Your Email] | [Your Phone] | [LinkedIn URL]
[City, State]

[Date]

[Hiring Manager Name, if known]
[Title]
[Company Name]
[Company Address]

Dear [Mr./Ms. Last Name / Hiring Manager],

[OPENING HOOK - 1-2 sentences grabbing attention with company knowledge, mutual connection, or impressive achievement]

[BRIDGE TO POSITION - 1 sentence stating the role and your interest]

[BODY 1 - 3-4 sentences connecting your strongest relevant experience to their primary requirement. Include specific metrics and results.]

[BODY 2 - 3-4 sentences adding additional value, addressing any gaps if needed, and demonstrating company research/culture fit]

[CLOSING - 2-3 sentences expressing enthusiasm, suggesting next steps, and thanking them]

Sincerely,
[Your Name]
```

## Industry-Specific Considerations

### Tech/Engineering
- Mention specific technologies
- Reference GitHub, portfolio, or technical projects
- Show you understand their tech stack

### Marketing/Creative
- Show creativity in the letter itself (within reason)
- Reference their campaigns or brand voice
- Include relevant metrics (engagement, conversion, etc.)

### Finance/Consulting
- More formal tone
- Lead with credentials/certifications
- Emphasize analytical rigor and results

### Startup vs. Enterprise
**Startup:** More casual, show scrappiness, emphasize growth mindset
**Enterprise:** More formal, emphasize process and scale experience

## Handling Common Scenarios

### When You Don't Know the Hiring Manager
```
Dear Hiring Manager,
OR
Dear [Department] Team,
OR
Dear [Company Name] Recruiting Team,
```
Avoid "To Whom It May Concern" (too impersonal)

### When You Have a Referral
Lead with it:
```
"[Name] on your [team] team suggested I reach out about the [Position] role. Having [connection to referrer], I was excited to learn about [Company]'s work in [area]."
```

### When You're Underqualified
Don't apologize. Instead, emphasize:
- Transferable skills
- Quick learning ability
- Genuine enthusiasm
- Related experience that compensates

### When You're Overqualified
Explain your motivation:
```
"After 10 years leading large teams, I'm energized by the opportunity to return to hands-on [function] work at a company where I can make direct impact on [specific area]."
```

### When Addressing Career Change
```
"While my background is in [Previous Field], I've been actively building [New Field] skills through [courses, projects, etc.]. My experience in [transferable skill] translates directly to [new role] through [specific connection]."
```

## Output Format

When generating a cover letter, provide:

```markdown
# COVER LETTER FOR [POSITION] AT [COMPANY]

## Analysis Summary
- Match Score: [From JD Analyzer]
- Key Strengths to Highlight: [List]
- Gaps to Address: [List or "None"]
- Company Research Notes: [Key facts to reference]

## Generated Cover Letter

[Full cover letter text]

---

## Alternative Openings

**Option 1 (Company Knowledge):**
[Alternative opening hook]

**Option 2 (Achievement-Led):**
[Alternative opening hook]

## Key Talking Points for Interview
- [Point 1 from the letter to expand on]
- [Point 2]
- [Point 3]
```

## Quality Checklist

Before delivering any cover letter:

1. ✅ Opens with a hook (not "I am writing to apply")
2. ✅ Mentions specific company knowledge
3. ✅ Connects experience directly to job requirements
4. ✅ Includes at least one specific metric/achievement
5. ✅ Addresses any obvious gaps (if applicable)
6. ✅ Has confident but not arrogant tone
7. ✅ Ends with clear call to action
8. ✅ Is 250-400 words (3-4 paragraphs)
9. ✅ Contains no typos or grammatical errors
10. ✅ Would make you want to interview this person
```

## File: `skills/creative-portfolio-resume/SKILL.md`
```markdown
---
name: Creative Portfolio Resume
description: Balance visual design with ATS compatibility for creative roles
---

# Creative Portfolio Resume

## When to Use This Skill

Use this skill when the user:
- Works in a creative field (design, marketing, writing)
- Needs to balance visual design with ATS compatibility
- Wants to showcase creative skills through resume design
- Is building a portfolio resume for creative roles
- Mentions: "creative resume", "designer resume", "visual resume", "portfolio resume", "creative field"

## Core Capabilities

- Balance visual appeal with ATS compatibility
- Design resumes for creative roles
- Integrate portfolio elements with resume content
- Advise on when to use creative vs. traditional formats
- Guide visual hierarchy and design choices
- Connect resume to portfolio effectively

## The Creative Resume Dilemma

**The Problem:**
- Creative professionals want to show design skills through their resume
- But most applications go through ATS systems
- Overly designed resumes often fail ATS parsing

**The Solution:**
Two-version approach:
1. **ATS-compatible version** for online applications
2. **Designed version** for portfolio, networking, direct submissions

## When to Use Each Version

### Use ATS-Compatible Version When:
- Applying through online portals
- Submitting to job boards
- Resume will be parsed by software
- You're unsure how it will be processed

### Use Designed Version When:
- Networking events
- Direct email to hiring manager
- Portfolio website
- In-person interviews
- Creative agencies that expect visual resumes
- When specifically told ATS isn't used

## ATS-Compatible Creative Resume

Even the ATS version can show creativity through:

### Subtle Design Elements
- Strategic use of white space
- Clean typography hierarchy
- Thoughtful content organization
- Strong copywriting
- Polished, professional appearance

### Safe Creative Touches
- ✅ Custom professional font (ATS-safe ones)
- ✅ Strategic bold and italic
- ✅ Clean section dividers (simple lines)
- ✅ Consistent, intentional spacing
- ✅ Color in your name/headers (sparing)
- ✅ Hyperlinks to portfolio

### Still Avoid
- ❌ Multiple columns
- ❌ Text boxes
- ❌ Images or icons
- ❌ Tables for layout
- ❌ Unusual fonts
- ❌ Graphics or skill bars

## Designed Portfolio Resume

### Design Principles

**1. Show, Don't Just Tell**
- Your resume IS a design sample
- Typography choices matter
- Layout demonstrates design thinking
- Details show attention to craft

**2. Clarity Over Cleverness**
- Information must still be findable
- Prioritize readability
- Save experimental design for portfolio pieces

**3. Brand Consistency**
- Match your portfolio website
- Consistent color palette
- Unified visual identity

### Visual Elements to Consider

**Typography:**
- Headline font (display, personality)
- Body font (readable, professional)
- Size hierarchy (name > sections > body)
- Line height and letter spacing

**Color:**
- Brand color for accents
- High contrast for readability
- Limited palette (2-3 colors max)
- Consider print-friendly colors

**Layout:**
- Consider two-column (for designed version only)
- Strategic white space
- Clear visual hierarchy
- Consistent margins and gutters

**Visual Accents:**
- Icons (if used, consistently)
- Dividers and rules
- Subtle background elements
- Your logo/personal brand mark

## Creative Field-Specific Guidance

### Graphic Designers

**Must Show:**
- Typography skills
- Layout and composition
- Visual hierarchy
- Attention to detail

**Resume Approach:**
- Your resume IS a portfolio piece
- Clean, sophisticated design
- Show range through subtle choices
- Link to portfolio for variety

### UX/Product Designers

**Must Show:**
- Information architecture skills
- User-centered thinking
- Clear visual hierarchy
- Systematic approach

**Resume Approach:**
- Scannable, organized structure
- Clear content hierarchy
- User (recruiter) focused organization
- Link to case studies

### Marketing/Brand

**Must Show:**
- Brand thinking
- Storytelling ability
- Strategic communication
- Attention to audience

**Resume Approach:**
- On-brand visual identity
- Compelling narrative flow
- Strategic content choices
- Proof points for claims

### Writers/Content

**Must Show:**
- Writing quality
- Editing precision
- Clear communication
- Voice and style

**Resume Approach:**
- Impeccable copy
- Strong bullets
- Zero errors
- Personality through writing

### Photographers/Video

**Must Show:**
- Visual eye
- Production quality
- Technical skill
- Aesthetic sensibility

**Resume Approach:**
- Clean, uncluttered design
- Strong portfolio link
- Quality over quantity
- Let portfolio speak

## Portfolio Integration

### On the Resume

**Link to Portfolio:**
```
Portfolio: yourname.com
```

**Link to Specific Work:**
```
• Redesigned checkout flow, increasing conversion by 40%
  Case Study: yourname.com/checkout
```

### Portfolio Website Resume Page

**Options:**
1. PDF download (designed version)
2. HTML resume page
3. Interactive resume experience
4. All of the above

**Best Practice:**
- Offer PDF download for convenience
- Ensure web version is responsive
- Keep updated with main resume

## Design Execution Tips

### Typography Checklist
- [ ] Name is largest element
- [ ] Clear hierarchy (3-4 levels max)
- [ ] Body text is 10-12pt minimum
- [ ] Line height allows breathing room
- [ ] No more than 2 font families
- [ ] Fonts complement each other

### Layout Checklist
- [ ] Clear sections and flow
- [ ] Consistent margins throughout
- [ ] Adequate white space
- [ ] Elements align to grid
- [ ] Visual balance achieved
- [ ] Scannable in 6 seconds

### Color Checklist
- [ ] Limited palette (2-3 colors)
- [ ] High contrast for text
- [ ] Accessible color choices
- [ ] Prints well in B&W
- [ ] Consistent with personal brand
- [ ] Professional appearance

## Tools for Designed Resumes

**Design Software:**
- Adobe InDesign (best for layout)
- Figma (good for web-native)
- Adobe Illustrator (vector-based)
- Sketch (Mac option)

**Simpler Options:**
- Canva (templates available)
- Google Docs (limited but ATS-safe)
- Microsoft Word (surprisingly capable)

**Avoid:**
- PowerPoint/Keynote (not designed for this)
- Random online resume builders
- Heavy templates that obscure content

## Output Format

When creating a creative resume:

```markdown
# CREATIVE RESUME STRATEGY

## Role Type: [Design/Marketing/Creative]
## Industry: [Agency/In-house/Freelance]

## Version Strategy

### Version 1: ATS-Compatible
**Use for:** Online applications, job boards
**Format:** .docx and .pdf
**Design level:** Clean and professional, minimal embellishment

### Version 2: Designed
**Use for:** Portfolio, networking, direct outreach
**Format:** .pdf (print-quality)
**Design level:** Full creative treatment

## Design Specifications

### Typography
- Headline: [Font name, weight, size]
- Body: [Font name, weight, size]
- Accent: [Font name, use case]

### Colors
- Primary: [Hex code] - [Use case]
- Secondary: [Hex code] - [Use case]  
- Text: [Hex code]

### Layout
- Format: [Single column / Two column]
- Margins: [Specifications]
- Grid: [If applicable]

## Portfolio Integration
- Main portfolio link: [URL]
- Case studies to highlight: [List]
- Resume page on portfolio: [Y/N]

## Content Adjustments for Creative Field
- [Specific content recommendation]
- [Specific content recommendation]
```

## Creative Resume Checklist

- ✅ Have both ATS and designed versions
- ✅ Design demonstrates relevant skills
- ✅ Content is still clear and scannable
- ✅ Portfolio is prominently linked
- ✅ Visual identity is consistent
- ✅ Typography is professional
- ✅ Colors are accessible and print-friendly
- ✅ File is optimized for sharing (reasonable size)
- ✅ Content quality matches design quality
- ✅ Resume is a worthy portfolio piece
```

## File: `skills/executive-resume-writer/SKILL.md`
```markdown
---
name: Executive Resume Writer
description: Create C-suite and VP level resumes emphasizing strategic leadership
---

# Executive Resume Writer

## When to Use This Skill

Use this skill when the user:
- Is applying for C-suite, VP, or Director roles
- Has 15+ years of experience in senior leadership
- Needs to emphasize strategic leadership over tactical skills
- Mentions: "executive resume", "C-suite", "VP resume", "senior leadership", "board", "executive search"

## Core Capabilities

- Write resumes for C-suite and VP-level positions
- Emphasize strategic leadership and business transformation
- Showcase P&L responsibility and organizational impact
- Balance achievements with leadership philosophy
- Format for executive recruiters and board presentations
- Include board experience and industry recognition

## Executive Resume Philosophy

**Key Differences from Standard Resumes:**

| Standard Resume | Executive Resume |
|-----------------|------------------|
| Lists skills | Demonstrates leadership brand |
| Shows tasks | Shows strategic impact |
| Focuses on "what" | Focuses on "so what" |
| 1-2 pages | 2-3 pages acceptable |
| Keywords for ATS | Story for decision-makers |
| Individual contributions | Organizational transformation |

## Executive Resume Structure

### Recommended Sections

```
1. Executive Profile/Summary
2. Core Competencies (Leadership Themes)
3. Career Highlights / Key Achievements
4. Professional Experience
5. Board & Advisory Roles
6. Education & Executive Development
7. Industry Recognition (optional)
```

### Length Guidelines
- VP/SVP: 2 pages
- C-Suite: 2-3 pages
- Board CV: Can be longer

## Executive Profile Section

This replaces the standard professional summary. Should communicate your **leadership brand**.

### Format
```
[TITLE/FUNCTION] EXECUTIVE

[Leadership brand statement - who you are as a leader]

[2-3 sentences on your track record with scope/scale]

[What you're known for / unique value proposition]
```

### Example

```
CHIEF OPERATING OFFICER | P&L LEADERSHIP | OPERATIONAL TRANSFORMATION

Growth-focused operations executive with 20+ years scaling B2B technology companies from $50M to $500M+ in revenue. Known for building high-performance teams, operational excellence, and creating scalable infrastructure that enables rapid growth.

Track record includes 3 successful exits, 2 IPO preparations, and leading organizations of 500+ employees across 6 countries. Expertise in operational strategy, M&A integration, and digital transformation in SaaS and enterprise software environments.

Core philosophy: Build repeatable processes that scale while maintaining the agility that drives innovation.
```

## Core Competencies Section

Frame as leadership themes rather than skills lists.

### Example
```
LEADERSHIP COMPETENCIES

Strategic Growth        | M&A Integration          | Digital Transformation
P&L Management ($500M+) | Global Team Leadership   | Board Relations
Operational Excellence  | Change Management        | Investor Relations
```

## Career Highlights Section

Place your biggest achievements upfront before chronological experience.

### Format
```
CAREER HIGHLIGHTS

• [Achievement 1 with metrics]
• [Achievement 2 with metrics]
• [Achievement 3 with metrics]
• [Achievement 4 with metrics]
```

### Example
```
CAREER HIGHLIGHTS

• Led operational transformation at TechCorp, improving EBITDA margins from 12% to 28% while growing revenue from $150M to $400M
• Executed 5 acquisitions totaling $200M+ and successfully integrated 3 companies with 95% employee retention
• Built global operations team from 50 to 500+ employees across US, EMEA, and APAC regions
• Prepared company for successful IPO, implementing SOX compliance and investor-ready reporting
```

## Experience Section for Executives

### The Executive Bullet Formula

**[Leadership Action] + [Strategic Initiative] + [Business Outcome at Scale]**

### Example Role

```
CHIEF OPERATING OFFICER
TechCorp Inc. | San Francisco, CA | 2019 - Present
$400M B2B SaaS company | 1,200 employees | Series D - IPO track

Recruited by CEO to transform operations and prepare company for IPO. Direct reports include VP Engineering, VP Customer Success, VP Operations, and CIO. Full P&L ownership for services business ($150M).

Strategic Initiatives & Results:

• Operational Transformation: Redesigned end-to-end operations, improving gross margins from 62% to 78% and reducing customer onboarding time from 90 to 30 days

• Scale & Growth: Built infrastructure to support growth from $150M to $400M revenue, including implementation of ERP, expansion to 3 new geographies, and establishment of 24/7 global support

• M&A Leadership: Served as operational lead for 3 acquisitions totaling $75M, achieving full integration within 6 months and 95% talent retention

• Team Development: Expanded operations organization from 200 to 600 employees, established leadership development program that promoted 15 internal candidates to VP/Director roles

• IPO Preparation: Led SOX compliance implementation, established audit committee reporting, and built investor-ready operational metrics and forecasting capabilities
```

### Key Elements for Executive Experience

**Always Include:**
- Company context (revenue, employees, stage)
- Reporting structure / span of control
- P&L or budget responsibility
- Strategic scope

**Metrics to Emphasize:**
- Revenue growth ($ and %)
- Profitability improvement (margins, EBITDA)
- Cost reduction
- Team size and development
- Geographic expansion
- M&A activity
- Exit outcomes

## Board & Advisory Section

```
BOARD & ADVISORY POSITIONS

Board of Directors | TechStartup Inc. | 2022 - Present
$50M ARR B2B SaaS company. Chair of Compensation Committee.

Advisory Board | VentureStudio | 2020 - Present
Supporting portfolio companies with operational strategy and GTM execution.

Board Observer | AcquiredCo (acquired by BigTech, 2023) | 2021 - 2023
Provided operational guidance through $200M acquisition process.
```

## Executive-Specific Considerations

### Emphasize Transformation

Executives are hired to **transform**, not maintain. Show:
- What changed because of you
- Before/after states
- Scale of impact

**Transformation Story Formula:**
"Inherited [situation]. Implemented [strategic change]. Achieved [outcome]."

### Show Leadership Philosophy

Unlike individual contributor resumes, executive resumes should hint at **how** you lead.

**Examples:**
- "Known for building consensus across diverse stakeholder groups"
- "Leads with data-driven decision making while maintaining strategic flexibility"
- "Champions innovation while maintaining operational discipline"

### Handle Tenure Carefully

**Short Tenures:** Frame around specific missions
- "Brought in to lead post-merger integration"
- "Recruited for turnaround; completed in 18 months"
- "Joined to prepare company for acquisition"

**Long Tenures:** Show progression and reinvention
- "Promoted through 4 roles over 12 years"
- "Led multiple transformations as company grew from $50M to $500M"

### Confidential Information

**Do:**
- Use percentage improvements when absolutes are confidential
- Use ranges for revenue/headcount
- Speak to relative impact

**Don't:**
- Share proprietary strategies
- Name confidential acquisition targets
- Reveal undisclosed financial information

## Executive Resume Tone

### Power Language for Executives

**Strategic Action Verbs:**
- Spearheaded, Orchestrated, Championed, Steered
- Transformed, Revolutionized, Pioneered
- Architected, Engineered (strategically)
- Drove, Accelerated, Catalyzed

**Leadership Language:**
- "Led organization through..."
- "Built and scaled..."
- "Established vision for..."
- "Negotiated and secured..."
- "Championed transformation..."

### What to Avoid

- ❌ Tactical/operational language (managed, handled, assisted)
- ❌ First person pronouns (I, my, me)
- ❌ Jargon without context
- ❌ Generic statements without proof
- ❌ Too much humility (take credit appropriately)

## Output Format

When writing an executive resume:

```markdown
# EXECUTIVE RESUME

## Executive Profile
[Full executive profile section]

## Core Competencies
[Formatted competency grid]

## Career Highlights
[4-6 top achievements with metrics]

## Professional Experience

### [Most Recent Role]
[Full executive role writeup]

### [Previous Role]
[Full executive role writeup]

## Board & Advisory
[Board positions]

## Education & Development
[Degrees and executive education]

---

## Positioning Notes
- Key narrative theme: [The story your resume tells]
- Leadership brand: [What you're known for]
- Differentiator: [What sets you apart]
```

## Executive Search Considerations

**Your resume may be seen by:**
- Executive recruiters
- Board members
- PE/VC partners
- CEOs and CHROs

**Optimize for:**
- Quick scanning by busy executives
- Clear narrative of career progression
- Obvious leadership brand
- Credible, verifiable achievements

**Remember:**
- Executive searches often involve references before interviews
- Your resume will be fact-checked
- Relationships and reputation matter
- The resume opens doors; relationships close deals
```

## File: `skills/interview-prep-generator/SKILL.md`
```markdown
---
name: Interview Prep Generator
description: Generate STAR stories, practice questions, and talking points from resume
---

# Interview Prep Generator

## When to Use This Skill

Use this skill when the user wants to:
- Prepare for a job interview
- Practice answering interview questions
- Create STAR stories from their experience
- Anticipate questions for a specific role
- Mentions: "interview prep", "prepare for interview", "STAR stories", "interview questions", "behavioral questions"

## Core Capabilities

- Generate role-specific interview questions
- Create STAR stories from resume bullets
- Predict questions based on job description
- Prepare answers for common questions
- Create talking points for each experience
- Identify potential concerns and prepare responses

## Interview Preparation Framework

### Phase 1: Role Analysis
- Extract likely questions from job description
- Identify skills that will be tested
- Research company interview style

### Phase 2: Story Banking
- Convert resume bullets into STAR stories
- Create stories for common competencies
- Practice concise delivery

### Phase 3: Mock Preparation
- Practice common questions
- Prepare questions to ask
- Research company-specific topics

## The STAR Method Detailed

### Structure
- **S**ituation: Set the context (1-2 sentences)
- **T**ask: Describe your responsibility (1 sentence)
- **A**ction: Explain what YOU did (2-3 sentences)
- **R**esult: Share the outcome with metrics (1-2 sentences)

### STAR Story Template

```
SITUATION: "At [Company], we faced [specific challenge/context]..."

TASK: "I was responsible for [specific ownership]..."

ACTION: "I [specific action 1], [specific action 2], and [specific action 3]..."

RESULT: "As a result, [quantified outcome]. This led to [business impact]."
```

### Example STAR Story

**Question:** "Tell me about a time you led a team through a difficult project."

**Answer:**
```
SITUATION: "At TechCorp, our main product was losing customers to a competitor who had launched a better mobile experience. We were seeing 5% monthly churn, up from our normal 2%."

TASK: "As the product manager, I was responsible for turning around our mobile product to stop the bleeding and win back customers."

ACTION: "I started by interviewing 30 churned customers to understand exactly why they left. Based on that research, I prioritized 5 critical features that would achieve parity with competitors. I then worked with engineering to restructure our roadmap, negotiated with leadership to add 2 contract developers, and implemented weekly sprint reviews to keep the project on track. I also started a beta program with 50 of our best customers to get feedback before full launch."

RESULT: "We launched the improved mobile app in 3 months, reducing churn from 5% back to 2% within 60 days. We recovered 35% of churned customers and the NPS for our mobile app increased from 32 to 58. This project was recognized in our company all-hands as a turnaround success."
```

**Time:** 90 seconds to 2 minutes

## Story Banking Process

### Step 1: Identify Core Competencies

**Leadership Stories Needed:**
- Led a team through challenge
- Managed conflict
- Made a difficult decision
- Delegated effectively
- Developed/mentored someone

**Problem-Solving Stories Needed:**
- Solved complex technical problem
- Fixed a process that was broken
- Handled unexpected obstacle
- Made decision with incomplete information
- Improved something proactively

**Collaboration Stories Needed:**
- Worked with difficult colleague
- Aligned cross-functional stakeholders
- Built consensus
- Partnered with other teams
- Influenced without authority

**Achievement Stories Needed:**
- Exceeded goals/expectations
- Delivered under pressure
- Went above and beyond
- Took initiative
- Accomplished something proud of

**Failure/Growth Stories Needed:**
- Made a mistake and learned
- Received critical feedback
- Failed and recovered
- Changed approach based on learning

### Step 2: Map Resume to Stories

For each resume bullet, create a full STAR story:

```
RESUME BULLET: "Led cross-functional team of 12 to deliver $2M product launch"

STAR EXPANSION:

SITUATION: Our company was losing market share to a competitor, and leadership decided we needed to launch a new product line within 6 months.

TASK: As Product Manager, I was tasked with leading the product from concept to launch, coordinating across engineering, design, marketing, and sales teams (12 people total).

ACTION: 
- I established weekly cross-functional syncs and a shared Notion workspace
- Created a detailed project plan with milestones and dependencies
- Implemented a rapid prototyping process with 2-week design sprints
- Personally resolved 3 major conflicts between engineering and marketing
- Presented monthly updates to leadership to maintain alignment

RESULT: 
- Launched on time and under budget
- Generated $2M revenue in first year
- Acquired 50 new enterprise customers
- Team received company innovation award
```

### Step 3: Create Multiple Versions

Each story should have:
- **Full version:** 2 minutes (for "tell me about a time...")
- **Short version:** 60 seconds (for follow-ups)
- **One-liner:** 15 seconds (for "give me an example")

## Common Interview Questions by Category

### Behavioral Questions

**Leadership:**
- "Tell me about a time you led a team."
- "Describe a situation where you had to make an unpopular decision."
- "How have you developed team members?"
- "Tell me about a time you dealt with a difficult team member."

**Problem-Solving:**
- "Describe a complex problem you solved."
- "Tell me about a time something didn't go as planned."
- "How do you approach problems with incomplete information?"
- "Give an example of an innovative solution you developed."

**Collaboration:**
- "Tell me about working with someone difficult."
- "Describe a time you had to influence someone without authority."
- "How do you handle disagreements with colleagues?"
- "Tell me about a successful cross-functional project."

**Achievement:**
- "What's your proudest professional accomplishment?"
- "Tell me about a time you exceeded expectations."
- "Describe a goal you achieved against the odds."
- "What's the biggest impact you've had in your career?"

**Failure/Growth:**
- "Tell me about a time you failed."
- "What's the biggest mistake you've made at work?"
- "How do you handle criticism?"
- "What would you do differently in your career?"

### Role-Specific Questions

**Product Management:**
- "How do you prioritize features?"
- "Walk me through how you'd approach [product problem]."
- "How do you measure product success?"
- "Tell me about a product you shipped from 0 to 1."

**Engineering:**
- "Describe your experience with [specific technology]."
- "How do you approach code reviews?"
- "Tell me about a technical challenge you solved."
- "How do you balance technical debt vs. features?"

**Marketing:**
- "How do you measure campaign success?"
- "Tell me about a campaign that didn't work."
- "How do you allocate budget across channels?"
- "Describe your approach to brand building."

**Sales:**
- "Walk me through your sales process."
- "Tell me about a deal you lost and why."
- "How do you handle objections?"
- "Describe your largest closed deal."

### Standard Questions

**About You:**
- "Tell me about yourself." (2 min pitch)
- "Walk me through your resume."
- "Why are you looking for a new role?"
- "Where do you see yourself in 5 years?"

**About the Role:**
- "Why this role?"
- "What interests you about this position?"
- "What do you think this role entails?"
- "What would you do in your first 90 days?"

**About the Company:**
- "Why this company?"
- "What do you know about us?"
- "Why do you want to work here?"
- "What excites you about our mission?"

## Questions to Ask Interviewers

### For Hiring Manager
- "What does success look like in this role at 30/60/90 days?"
- "What are the biggest challenges facing the team?"
- "How is performance measured?"
- "What's the team structure?"

### For Team Members
- "What's a typical day/week like?"
- "What do you enjoy most about working here?"
- "How do teams collaborate?"
- "What would you want a new hire to know?"

### For Executives
- "What's the company's strategy for the next year?"
- "How does this team contribute to company goals?"
- "What keeps you excited about the company?"

### To Avoid
- ❌ Questions about salary/benefits (save for HR)
- ❌ Questions you could easily Google
- ❌ Negative questions about company problems
- ❌ Yes/no questions (ask open-ended)

## Handling Difficult Questions

### "What's your greatest weakness?"

**Formula:** Real weakness + Self-awareness + Improvement steps

```
"I tend to be overly detail-oriented, which can sometimes slow me down. I've recognized this and now set time limits for tasks and ask for feedback on when good enough is good enough. In my current role, I've also learned to delegate detailed work when appropriate."
```

### "Why are you leaving your current job?"

**Keep it:**
- Positive (growth-focused)
- Forward-looking (not complaint-based)
- Brief (don't over-explain)

```
"I've learned a lot at [Company], but I'm looking for [specific opportunity] that I don't see available in my current path. This role at [Company] offers exactly that - the chance to [specific thing]."
```

### "Tell me about a time you failed"

**Must include:**
- Real failure (not humble brag)
- What you learned
- How you applied the learning

```
"In my first year as a PM, I launched a feature without sufficient user research. The feature was technically sound but users found it confusing. Only 10% adopted it. I learned the hard way that building the right thing matters more than building the thing right. Since then, I never skip user research - I now always do at least 10 user interviews before major feature decisions."
```

### Salary Questions

**Deflect until you have to answer:**

```
"I'm flexible on compensation and more focused on finding the right role. Can you share the range budgeted for this position?"
```

**If pressed:**
```
"Based on my research and experience, I'm looking for something in the range of $X-$Y, but I'm open to discussing the full compensation package."
```

## Output Format

When generating interview prep:

```markdown
# INTERVIEW PREP: [POSITION] AT [COMPANY]

## Role Analysis
**Key competencies they'll test:**
1. [Competency] - Evidence: [From JD]
2. [Competency] - Evidence: [From JD]
3. [Competency] - Evidence: [From JD]

## Predicted Questions

### High Probability (prepare thoroughly)
1. [Question] → Use story: [Story name]
2. [Question] → Use story: [Story name]
3. [Question] → Use story: [Story name]

### Medium Probability
1. [Question]
2. [Question]

## Your STAR Story Bank

### Story 1: [Name - e.g., "Product Launch Success"]
**Use for:** Leadership, Achievement, Cross-functional
**STAR:**
- S: [Situation]
- T: [Task]
- A: [Action]
- R: [Result with metrics]
**Short version:** [60 second version]

### Story 2: [Name]
[Same structure]

## "Tell Me About Yourself" Script
[2-minute pitch tailored to this role]

## Questions to Ask
**For Hiring Manager:**
1. [Question]
2. [Question]

**For Team:**
1. [Question]
2. [Question]

## Company Research Notes
- Recent news: [Item]
- Key facts to reference: [Facts]
- Potential concerns: [Items to be ready for]

## Red Flag Answers to Avoid
- Don't mention: [Topics]
- Don't criticize: [Past employer aspects]
- Watch out for: [Potential trap questions]
```

## Implementation Checklist

For complete interview prep:
1. ✅ Analyze job description for competencies
2. ✅ Create 8-10 STAR stories covering all competencies
3. ✅ Write "tell me about yourself" pitch
4. ✅ Prepare answers for likely questions
5. ✅ Research company thoroughly
6. ✅ Prepare thoughtful questions to ask
7. ✅ Practice out loud (time yourself)
8. ✅ Prepare logistics (outfit, route, tech check)
9. ✅ Review the day before interview
10. ✅ Send thank you notes after
```

## File: `skills/job-description-analyzer/SKILL.md`
```markdown
---
name: Job Description Analyzer
description: Analyze job postings, calculate match scores, identify gaps, and create application strategy
---

# Job Description Analyzer

## When to Use This Skill

Use this skill when the user:
- Wants to analyze a job posting
- Asks "should I apply to this job?"
- Wants to know their match percentage for a role
- Needs help understanding job requirements
- Wants to tailor their resume for a specific position
- Mentions: "analyze this job", "am I qualified", "match score", "should I apply"

Use this BEFORE resume tailoring to ensure effort is worth it.

## Core Capabilities

- Extract and categorize job requirements (must-have vs nice-to-have)
- Calculate match score between user's experience and job requirements
- Identify skill gaps and strengths
- Detect red flags in job postings
- Prioritize which experiences to highlight
- Generate resume tailoring strategy
- Create cover letter talking points
- Assess company culture fit indicators

## The Strategic Problem

Most job seekers waste time on:
- Jobs they're under-qualified for (<60% match)
- Jobs they're over-qualified for (flight risk)
- Jobs with red flags (high turnover, toxic culture)
- Applying to 50+ jobs blindly hoping something sticks

Better approach:
- Apply to 10-15 jobs strategically
- Target 70-90% match jobs
- Customize deeply for each
- Higher response rate, less burnout

## Analysis Process

### Step 1: Extract Requirements

Break job description into categories:

**Required (Must-Have)**
- Education requirements
- Years of experience
- Specific technical skills
- Certifications/licenses
- Industry experience

**Preferred (Nice-to-Have)**
- "Bonus" skills
- Advanced certifications
- Domain expertise
- Specific tool experience

**Soft Skills/Culture**
- Communication style
- Work environment
- Team structure
- Company values

### Step 2: Keyword Extraction

Identify three types:

**Hard Skills** (Technical abilities)
- Tools: Salesforce, Python, AWS, Excel
- Methodologies: Agile, Six Sigma, SDLC
- Certifications: PMP, CPA, AWS Certified

**Soft Skills** (Interpersonal)
- Leadership, collaboration, communication
- Problem-solving, critical thinking
- Adaptability, initiative

**Industry/Domain Knowledge**
- B2B SaaS, healthcare, fintech
- Enterprise vs SMB
- Regulatory knowledge (HIPAA, SOX, GDPR)

### Step 3: Calculate Match Score

```
MATCH CALCULATION:

Required Skills:
- User has 8 out of 10 required = 80%

Preferred Skills:
- User has 3 out of 5 preferred = 60%

Overall Match:
- Weight required 70%, preferred 30%
- (80% × 0.7) + (60% × 0.3) = 74%

INTERPRETATION:
90-100% = Overqualified (may be flight risk)
75-89% = Excellent fit (apply immediately)
60-74% = Good fit (apply with strong cover letter)
50-59% = Stretch role (apply if passionate)
<50% = Under-qualified (skip unless dream job)
```

### Step 4: Gap Analysis

For each missing requirement:
- **Critical gap**: Deal-breaker (don't apply)
- **Major gap**: Significant but addressable (mention in cover letter)
- **Minor gap**: Easy to learn (downplay or emphasize related skills)

### Step 5: Red Flag Detection

Scan for warning signs:

**Workload Red Flags:**
- "Wear many hats"
- "Fast-paced environment"
- "Hit the ground running"
- "Self-starter in ambiguous situations"

**Culture Red Flags:**
- "Rockstar/Ninja/Guru"
- "We work hard, play hard"
- "Unlimited vacation"
- "Like a family"

**Compensation Red Flags:**
- "Competitive salary" (won't tell you range)
- "Equity-heavy" (low cash compensation)
- "Commission-based" (no base salary)
- "DOE" with no range

## Match Score Output Format

```markdown
# JOB ANALYSIS REPORT

**Position:** Senior Product Manager
**Company:** TechCorp Inc.
**Location:** San Francisco, CA (Hybrid)
**Salary Range:** $140K-$180K + equity

═══════════════════════════════════════════

## OVERALL MATCH SCORE: 78% ✅

**Recommendation:** STRONG FIT - Apply within 48 hours

**Application Priority:** HIGH
**Estimated Competition:** Medium (Posted 2 days ago)
**Time to Tailor Resume:** 30-45 minutes

═══════════════════════════════════════════

## REQUIREMENTS BREAKDOWN

### Required Skills - 8/10 ✅

✅ 5+ years product management (You have: 6 years)
✅ B2B SaaS experience (You have: 4 years)
✅ Agile/Scrum (You have: 5 years)
✅ Cross-functional leadership (You have: Strong experience)
✅ Data-driven decision making (You have: 3 years analytics)
✅ API products (You have: 2 years)
✅ Roadmap planning (You have: Extensive)
✅ User research (You have: 2 years)
❌ SQL/data analysis (You have: Basic Excel only) ⚠️
❌ Mobile product experience (You don't have) ⚠️

### Preferred Skills - 4/6 ✅

✅ MBA or equivalent (You have: MBA from UC Berkeley)
✅ Developer tools experience (You have: 2 years)
✅ Payment systems (You have: 1 year)
✅ International markets (You have: Worked with EU teams)
❌ E-commerce background (You don't have)
❌ Machine learning products (You don't have)

### Soft Skills - 5/5 ✅

✅ Stakeholder management (Strong mentions in your resume)
✅ Communication (You present regularly)
✅ Strategic thinking (MBA + senior experience)
✅ Influence without authority (You've done this)
✅ Customer empathy (User research experience)

═══════════════════════════════════════════

## STRENGTHS TO EMPHASIZE

**Your Top 3 Selling Points:**

1. **B2B SaaS PM Experience**
   - 4 years in SaaS, exactly what they want
   - Lead with this in resume summary

2. **API Product Background**
   - Your developer tools experience is highly relevant
   - This differentiates you from other candidates

3. **Data-Driven Approach**
   - Your analytics background addresses their need
   - Emphasize metrics and data in every bullet

═══════════════════════════════════════════

## GAPS TO ADDRESS

**Critical Gaps:** None ✅

**Major Gaps:**
⚠️ **SQL/Data Analysis**
- They mention this 5x in job description
- They want PM who can query data independently

**Strategy:**
- Don't avoid this gap
- Address in cover letter: "While my primary analytics work has been in Excel and BI tools, I'm actively learning SQL through DataCamp and can currently write basic queries"
- Emphasize your data-driven mindset and collaboration with data team

**Minor Gaps:**
- Mobile product experience (mentioned 2x)
- Not a dealbreaker - they want "any product," mobile just a plus

**Strategy:**
- Don't mention this gap
- If asked in interview, pivot to "transferable product skills"

═══════════════════════════════════════════

## RESUME CUSTOMIZATION STRATEGY

### Priority 1: Lead with Most Relevant Experience

**Current Resume Order:**
1. Company ABC - General PM work
2. Company XYZ - Your developer tools role
3. Company 123 - Early career

**Recommended Order:**
1. Company XYZ - Developer tools role (MOST RELEVANT)
2. Company ABC - B2B SaaS work
3. Company 123 - Only if space allows

### Priority 2: Keyword Integration

**Add These Exact Phrases:**
- "SQL and data analysis" (mentioned 5x in JD)
- "API product management" (mentioned 4x)
- "Developer-focused products" (mentioned 3x)
- "Stakeholder alignment" (mentioned 3x)

**Where to Add:**
- Professional Summary: Mention "API products" and "data-driven"
- Skills Section: Add "SQL (basic), Data Analysis, API Design"
- Experience: Weave into existing bullets

### Priority 3: Quantify Everything

They mention "metrics" and "KPIs" 7 times total.

**Enhance These Bullets:**

Current: "Led product roadmap"
Better: "Defined product roadmap based on analysis of 50+ customer interviews and usage data from 100K+ users"

Current: "Launched new features"
Better: "Launched 8 features in 12 months, increasing user engagement by 35% and reducing churn by 20%"

═══════════════════════════════════════════

## COVER LETTER TALKING POINTS

### Opening Hook (Choose One):

**Option 1 - Specific Company Knowledge:**
"I noticed TechCorp recently launched your API marketplace - I've spent the last 2 years as PM for a developer tools platform, and I'm excited about the opportunity to bring that experience to your growing API ecosystem."

**Option 2 - Mutual Connection:**
"[Name] on your product team mentioned you're looking for a PM to lead the API product line - my 2 years in developer tools and B2B SaaS background would be a strong fit."

**Option 3 - Problem-Solver:**
"Your JD mentions challenges in stakeholder alignment across technical teams - I've navigated this exact challenge at my current role, aligning engineering, design, and sales teams across 6 concurrent product initiatives."

### Body - Address the Match:
- "Your requirement for B2B SaaS experience: I have 4 years with..." 
- "Your focus on data-driven decisions: In my current role, I..."
- "Your need for API product expertise: At [Company], I..."

### Addressing SQL Gap (Optional):
"While my data analysis has primarily been in Excel and Tableau, I'm expanding my SQL skills and can currently write basic queries. More importantly, I've built strong partnerships with data teams and consistently use data to inform product decisions."

═══════════════════════════════════════════

## RED FLAGS ANALYSIS

### Potential Concerns: ⚠️ MINOR

**Flag 1:** "Fast-paced environment"
- Appears 2x in description
- Interpretation: Likely startup or high-growth
- May mean: Long hours, ambiguity, rapid changes

**Flag 2:** Salary range is wide ($140K-$180K)
- 29% spread
- May indicate: Experience range is flexible, or negotiation room

### Positive Signals: ✅

**Signal 1:** Detailed job description
- Shows company knows what they want
- Well-organized role

**Signal 2:** Mentions specific tools (JIRA, Amplitude)
- Shows operational maturity

**Signal 3:** Hybrid flexibility mentioned
- Modern workplace practices

### Company Research Needed:

Before applying, check:
- Glassdoor reviews (look for patterns in 1-2 star reviews)
- Recent funding/news (layoffs? growth?)
- LinkedIn: Check how long people stay (high turnover?)
- Levels.fyi: Verify salary range is accurate

═══════════════════════════════════════════

## APPLICATION TIMELINE

**✅ Day 1 (Today):**
- Customize resume (30-45 minutes)
- Write cover letter (30 minutes)

**✅ Day 1-2:**
- Submit application
- Connect with 2-3 current employees on LinkedIn
- Research company more deeply

**✅ Week 1:**
- Follow up if no response after 7 days

**📊 Expected Response Time:** 1-2 weeks

**📊 Interview Process (from job posting):**
1. Recruiter screen (30 min)
2. Hiring manager (1 hour)
3. Product case study (take-home)
4. Team interviews (3-4 hours)
5. Executive interview (1 hour)

═══════════════════════════════════════════

## DECISION FACTORS

### Reasons to Apply ✅

1. Strong match (78%) - You meet most requirements
2. Role aligns with career goals
3. Salary range is appropriate for your experience
4. Company stage fits your preferences
5. You have unique relevant experience (developer tools)

### Reasons to Hesitate ⚠️

1. SQL gap is real - prepare to address this
2. "Fast-paced" may mean high pressure
3. Need to research company culture more

### Overall Recommendation:

**APPLY - This is a strong opportunity**

You meet 80% of required skills and 67% of preferred skills. Your developer tools and B2B SaaS experience makes you a differentiated candidate. The SQL gap is addressable with honesty and emphasis on your analytical skills. Apply within 48 hours while posting is fresh.
```

## Requirement Classification Guide

### Identifying "Must Have" vs "Nice to Have"

**Language indicating REQUIRED:**
- "Must have..."
- "Required: X years of..."
- "You have..."
- "Essential qualifications"
- Listed under "Requirements"
- Mentioned 3+ times in description

**Language indicating PREFERRED:**
- "Nice to have..."
- "Bonus if you have..."
- "Preferred qualifications"
- "Ideally, you'd have..."
- "A plus if..."
- Mentioned only 1-2 times

### Dealbreaker Detection

**Absolute dealbreakers (don't apply):**
- Required license you don't have (medical, legal, CPA)
- Required clearance you can't get
- Years of experience 50%+ below requirement
- Required degree you don't have (when stated as "required")
- Location requirement you can't meet

**Not dealbreakers (apply anyway):**
- Years of experience slightly below (e.g., 3 years when they want 5)
- "Preferred" degree you don't have
- Nice-to-have tools/skills you can learn
- Industry experience when you have transferable skills

## Implementation Checklist

When analyzing a job:

1. ✅ Extract all requirements (required vs preferred)
2. ✅ Identify all keywords (hard skills, soft skills, industry terms)
3. ✅ Calculate match score
4. ✅ Identify strengths to emphasize
5. ✅ Identify gaps and strategies to address
6. ✅ Detect red flags
7. ✅ Create resume customization plan
8. ✅ Generate cover letter talking points
9. ✅ Research company
10. ✅ Provide application recommendation and timeline

## Edge Cases

### Vague Job Descriptions
- Flag as potential red flag
- Extract what keywords you can
- Recommend reaching out for clarity before applying
- Use industry standard requirements as baseline

### Multiple Roles in One JD
- Identify the core role vs "other duties"
- Focus match score on primary responsibilities
- Flag scope creep concerns

### Internal Postings (Already Working There)
- Different strategy - emphasize internal knowledge
- Highlight cross-team relationships
- Reference specific company initiatives

### Reposted Jobs
- May indicate: Previous hire didn't work out, role expanded, or first search failed
- Worth applying, but research why it was reposted
- Check if requirements changed from original posting
```

## File: `skills/linkedin-profile-optimizer/SKILL.md`
```markdown
---
name: LinkedIn Profile Optimizer
description: Optimize LinkedIn profile for searchability, recruiter visibility, and engagement
---

# LinkedIn Profile Optimizer

## When to Use This Skill

Use this skill when the user wants to:
- Optimize their LinkedIn profile for job searching
- Improve LinkedIn visibility and searchability
- Sync their resume with their LinkedIn profile
- Attract recruiters and job opportunities
- Mentions: "LinkedIn", "LinkedIn profile", "optimize LinkedIn", "LinkedIn headline", "recruiter"

## Core Capabilities

- Optimize headline for searchability
- Write compelling About/Summary sections
- Structure Experience section for impact
- Improve profile completeness score
- Add relevant keywords for recruiter searches
- Align LinkedIn with resume while leveraging platform differences

## LinkedIn vs. Resume: Key Differences

| Aspect | Resume | LinkedIn |
|--------|--------|----------|
| Length | 1-2 pages | Unlimited |
| Tone | Formal | More conversational |
| Keywords | Job-specific | Industry-wide |
| Audience | One specific employer | All recruiters |
| Updates | Per application | Always current |
| Personality | Minimal | Show more |

## Profile Section Optimization

### 1. Profile Photo

**Requirements:**
- Professional headshot (not casual photo)
- Face takes up 60% of frame
- Neutral or branded background
- Good lighting, high resolution
- Appropriate attire for your industry
- Friendly expression (slight smile)

**Impact:** Profiles with photos get 21x more views

### 2. Background Banner

**Best Practices:**
- Use a professional design or industry-related image
- Can include personal branding elements
- Size: 1584 x 396 pixels
- Avoid busy patterns that distract from your photo

**Options:**
- Company brand (if appropriate)
- Industry-related imagery
- Professional abstract design
- Personal brand statement

### 3. Headline (Most Important for Searchability)

**Character Limit:** 220 characters

**Formula:** [Role] | [Key Expertise] | [Value Proposition]

**Examples:**

❌ **Weak Headlines:**
- "Looking for opportunities"
- "Unemployed Product Manager"
- "Student at University"
- "Open to work"

✅ **Strong Headlines:**
```
Senior Product Manager | B2B SaaS | Driving 0→1 Products from Concept to $10M ARR

Data Scientist | Machine Learning & Analytics | Turning Data into Business Decisions

Software Engineer | Python, AWS, Kubernetes | Building Scalable Systems at Fortune 500

Marketing Director | Growth & Brand Strategy | 3x Revenue Growth at Series B Startups
```

**Keyword Strategy:**
Include terms recruiters search for:
- Your job title (and variations)
- Key skills (languages, tools, methodologies)
- Industry terms
- Certifications

### 4. About Section (Summary)

**Character Limit:** 2,600 characters
**Recommended Length:** 1,500-2,000 characters (3-5 paragraphs)

**Structure:**

```
[HOOK - Compelling first line that shows up in preview]

[PARAGRAPH 1: Who you are and what you do]

[PARAGRAPH 2: Your key achievements and specialties]

[PARAGRAPH 3: What you're looking for or passionate about]

[SKILLS LIST: Core competencies, searchable keywords]

[CALL TO ACTION: How to reach you]
```

**Example:**

```
I help SaaS companies turn product ideas into revenue.

For the past 8 years, I've been building products that people actually want to use. From a payments platform that processed $50M monthly to a developer tool used by 100K+ engineers, I've led cross-functional teams from idea to launch and beyond.

What I do best:
→ Transform ambiguous customer problems into clear product roadmaps
→ Build and lead high-performing product teams
→ Drive growth through data-informed decision making
→ Bridge technical and business stakeholders

Currently, I'm a Senior Product Manager at [Company], where I lead our API platform serving 500+ enterprise customers. Previously, I led product at [Previous Company] through their Series B and 10x growth.

Key skills: Product Strategy, Roadmap Planning, Agile/Scrum, User Research, A/B Testing, SQL, Data Analysis, Stakeholder Management, B2B SaaS, API Products

Let's connect! I'm always happy to chat about product, SaaS, or career advice for aspiring PMs. Reach me at [email].
```

**First Line is Crucial:**
Only ~300 characters show before "see more" - make them count!

### 5. Experience Section

**Key Differences from Resume:**
- Can be longer and more detailed
- Should include media (presentations, links)
- Can show personality
- Update regularly (not just when job hunting)

**For Each Role Include:**
- Clear job title
- Company (with logo linked)
- Date range
- Location
- Description (2-3 sentences about the role)
- 4-6 bullet points with achievements
- Media attachments if available

**Example:**

```
Senior Product Manager
TechCorp Inc. · Full-time
Jan 2021 - Present · 3 yrs 1 mo
San Francisco, CA · Hybrid

Leading product strategy for TechCorp's API Platform, serving 500+ enterprise customers and generating $20M ARR.

• Grew platform revenue from $5M to $20M ARR by launching 3 new product lines and expanding into enterprise segment
• Led cross-functional team of 15 (engineering, design, data) to deliver 25+ features with 95% on-time delivery rate  
• Improved customer retention from 82% to 94% through proactive feature development based on usage analytics
• Established product analytics framework using Amplitude, increasing feature adoption by 40%
• Collaborated with sales team to close 50+ enterprise deals worth $10M+ by participating in technical sales calls

Skills: Product Management · B2B SaaS · API Design · Agile Methodology · Stakeholder Management
```

### 6. Skills Section

**Strategy:**
- List up to 50 skills (use all 50!)
- Order by relevance and endorsements
- Get endorsements for top skills
- Include both technical and soft skills

**Categories to Include:**
- Job-specific skills (Product Management, Data Analysis)
- Tools (JIRA, Salesforce, Python)
- Methodologies (Agile, Six Sigma)
- Soft skills (Leadership, Communication)
- Industry terms (B2B, SaaS, Enterprise)

**Top 3 Featured Skills:**
Choose your three most important, most endorsed skills

### 7. Featured Section

**Use For:**
- Portfolio pieces
- Published articles
- Presentations
- Media coverage
- Important posts
- Project highlights

**Why It Matters:**
Appears prominently on profile - showcase your best work

### 8. Recommendations

**Target:** 5-10 quality recommendations

**Best Sources:**
- Former managers
- Direct reports
- Cross-functional partners
- Clients/customers

**How to Get Them:**
1. Give recommendations first
2. Ask specific people directly
3. Make it easy - suggest talking points
4. Time it right (after successful project)

## Keyword Optimization

### Finding Keywords
1. Search job descriptions for your target role
2. Look at profiles of people in roles you want
3. Use LinkedIn's Skills section suggestions
4. Check industry publications for terminology

### Keyword Placement
Place keywords in:
- Headline (highest weight)
- About section (multiple times naturally)
- Experience descriptions
- Skills section
- Recommendations (ask recommenders to use)

### Search Algorithm Tips
- Exact matches matter (use exact phrases)
- Keyword density helps (repeat important terms)
- Recent activity boosts visibility
- Complete profiles rank higher
- Engagement increases reach

## Profile Completeness Checklist

**All-Star Profile Requirements:**
- ✅ Professional photo
- ✅ Custom headline (not just job title)
- ✅ Current position with description
- ✅ Two past positions
- ✅ Education
- ✅ At least 5 skills
- ✅ Industry and postal code
- ✅ 50+ connections

**Beyond All-Star:**
- ✅ Custom background banner
- ✅ Featured section populated
- ✅ About section (1500+ characters)
- ✅ Rich media in Experience
- ✅ 500+ connections
- ✅ Recommendations (5+)
- ✅ All 50 skills listed
- ✅ Volunteer experience
- ✅ Certifications

## Recruiter Visibility Settings

### Open to Work Feature
**Settings to configure:**
- Job titles you're interested in
- Location preferences
- Start date
- Job types (full-time, contract, etc.)

**Visibility Options:**
- All LinkedIn members (shows green badge)
- Recruiters only (hidden, more discreet)

### Profile Visibility
Ensure these are ON:
- Profile viewing options: Show full profile
- Sharing profile edits: Your choice
- Represent in LinkedIn Services: ON (if relevant)

## Content Strategy

### Why Post Content?
- Increases profile visibility
- Demonstrates expertise
- Builds personal brand
- Attracts opportunities

### Content Types:
1. Industry insights/opinions
2. Professional lessons learned
3. Career milestones
4. Helpful resources
5. Engagement with others' content

### Posting Frequency:
- Minimum: 1x per week
- Optimal: 3-5x per week
- Comment/engage: Daily

## Output Format

When optimizing a LinkedIn profile:

```markdown
# LINKEDIN PROFILE OPTIMIZATION

## Current Profile Assessment
**Completeness:** X%
**Searchability Score:** X/10
**Key Issues:** [List]

## Optimized Sections

### Headline
**Current:** [Their current headline]
**Optimized:** [New headline with keywords]

### About Section
[Full optimized About section text]

### Experience Improvements
**[Company Name]**
- Add: [Suggested additions]
- Modify: [Suggested changes]
- Media to add: [Suggestions]

### Skills to Add
[List of skills to add based on target roles]

### Keywords Integrated
[List of keywords added throughout profile]

## Action Items
1. [ ] Update headline
2. [ ] Rewrite About section
3. [ ] Update current role description
4. [ ] Add X skills
5. [ ] Request X recommendations
6. [ ] Add featured content
7. [ ] Upload professional photo
```

## Resume-to-LinkedIn Sync

### What to Keep the Same:
- Core achievements and metrics
- Job titles and dates
- Key skills and qualifications
- Overall career narrative

### What to Expand:
- More detail in descriptions
- Additional context
- More bullets per role
- Personality and voice

### What to Adjust:
- Tone (more conversational)
- Length (can be longer)
- Keywords (broader than job-specific)
- Call to action (add contact info)
```

## File: `skills/offer-comparison-analyzer/SKILL.md`
```markdown
---
name: Offer Comparison Analyzer
description: Compare multiple job offers side-by-side with total compensation analysis
---

# Offer Comparison Analyzer

## When to Use This Skill

Use this skill when the user:
- Has multiple job offers to compare
- Needs to evaluate total compensation
- Wants to make a data-driven job decision
- Is weighing different opportunities
- Mentions: "compare offers", "multiple offers", "which job", "offer comparison", "deciding between jobs"

## Core Capabilities

- Compare total compensation across offers
- Evaluate non-monetary factors
- Create weighted decision frameworks
- Calculate true offer value
- Identify hidden costs and benefits
- Guide the decision-making process

## The Comparison Challenge

**The Problem:** 
Comparing offers is hard because:
- Different compensation structures
- Non-monetary factors matter
- Hidden benefits and costs
- Emotional factors cloud judgment
- Information asymmetry

**The Solution:**
Systematic comparison framework that considers:
- Total compensation (not just salary)
- Career growth potential
- Work-life factors
- Risk assessment
- Personal values alignment

## Total Compensation Calculator

### Components to Include

**Cash Compensation:**
- Base salary
- Signing bonus (one-time)
- Annual bonus (target %)
- Commission (for sales roles)
- Relocation assistance

**Equity Compensation:**
- Stock options (value = current price - strike price)
- RSUs (value = current price × shares)
- Vesting schedule
- Refresh grant expectations

**Benefits Value:**
- Health insurance (employer contribution)
- 401(k) match
- HSA/FSA contributions
- Life/disability insurance
- Other insurance benefits

**Perks Value:**
- Vacation days (can assign $ value)
- Remote work (saves commute costs)
- Professional development budget
- Equipment/office stipend
- Meals, gym, etc.

### Calculation Template

```
OFFER A - TOTAL COMPENSATION

CASH
Base Salary:                    $150,000
Signing Bonus (year 1 only):     $25,000
Target Bonus (15%):              $22,500
--------------------------------
Cash Compensation:              $197,500 (year 1)
                               $172,500 (ongoing)

EQUITY
RSU Grant: $200,000 over 4 years
Annual Value:                    $50,000
--------------------------------
Equity Compensation:             $50,000/year

BENEFITS
401(k) Match (4%):               $6,000
Health Insurance:                $15,000 (employer portion)
HSA Contribution:                 $1,000
--------------------------------
Benefits Value:                  $22,000/year

PERKS
Vacation: 20 days (vs 10 standard)
  Extra 10 days × ~$575/day:      $5,750 value
Remote Work Savings:              $3,000 (commute, lunch)
Professional Dev:                 $2,000 budget
--------------------------------
Perks Value:                     $10,750/year

TOTAL YEAR 1:        $280,250
TOTAL ONGOING:       $255,250/year
```

## Side-by-Side Comparison Template

```markdown
# OFFER COMPARISON

|                          | Company A | Company B | Notes |
|--------------------------|-----------|-----------|-------|
| **CASH**                 |           |           |       |
| Base Salary              | $150,000  | $160,000  | B +$10K |
| Signing Bonus            | $25,000   | $10,000   | A +$15K |
| Target Bonus             | 15%       | 10%       | A +$6.5K |
| **Cash Total (Yr 1)**    | $197,500  | $186,000  | A +$11.5K |
|                          |           |           |       |
| **EQUITY**               |           |           |       |
| Grant Value (4yr)        | $200,000  | $300,000  | B +$100K |
| Annual Equity            | $50,000   | $75,000   | B +$25K |
|                          |           |           |       |
| **BENEFITS**             |           |           |       |
| 401(k) Match             | 4%        | 6%        | B +$3.2K |
| Health Insurance         | Good      | Premium   | B better |
| PTO                      | 20 days   | Unlimited | Varies |
|                          |           |           |       |
| **TOTAL COMP (Yr 1)**    | $280,250  | $285,000  | B +$4.7K |
| **TOTAL COMP (Ongoing)** | $255,250  | $275,000  | B +$19.7K |
```

## Non-Monetary Factor Framework

### Career Growth (Weight: High)

**Questions to Consider:**
- Which role offers more learning?
- Which company/brand helps future job search?
- Which has better promotion track?
- Which offers more scope/responsibility?
- Which manager will develop you more?

**Scoring:**
```
Company A: Growth Score
- Learning opportunity: 8/10
- Brand/resume value: 7/10
- Promotion potential: 6/10
- Scope: 8/10
Average: 7.25/10

Company B: Growth Score
- Learning opportunity: 7/10
- Brand/resume value: 9/10
- Promotion potential: 8/10
- Scope: 7/10
Average: 7.75/10
```

### Work-Life Balance (Weight: Personal)

**Factors:**
- Expected hours
- Remote/hybrid flexibility
- Vacation usage culture
- On-call requirements
- Travel requirements
- Commute time

### Team & Culture (Weight: High)

**Factors:**
- Manager quality (crucial!)
- Team health/dynamics
- Company culture fit
- DEI considerations
- Company stability/growth
- Values alignment

### Risk Assessment (Weight: Medium)

**Startup vs. Established:**
- Funding runway
- Market position
- Company trajectory
- Equity risk (could be worth $0)

**Questions:**
- What happens if company struggles?
- How stable is this role?
- What's the severance policy?

## Weighted Decision Matrix

### Step 1: Define Your Priorities

```
Factor                  Weight
------------------------------------
Total Compensation       25%
Career Growth            25%
Work-Life Balance        20%
Team & Culture           20%
Location/Commute         10%
------------------------------------
Total:                   100%
```

### Step 2: Score Each Factor

```
                    Company A   Company B
Factor              Score (1-10)
------------------------------------
Compensation        7           8
Career Growth       7           8
Work-Life           8           6
Team & Culture      9           7
Location            8           5
```

### Step 3: Calculate Weighted Score

```
Company A:
(7 × 0.25) + (7 × 0.25) + (8 × 0.20) + (9 × 0.20) + (8 × 0.10)
= 1.75 + 1.75 + 1.60 + 1.80 + 0.80
= 7.70

Company B:
(8 × 0.25) + (8 × 0.25) + (6 × 0.20) + (7 × 0.20) + (5 × 0.10)
= 2.00 + 2.00 + 1.20 + 1.40 + 0.50
= 7.10

Result: Company A scores higher (7.70 vs 7.10)
```

## Red Flags to Watch

### In the Offer

- ❌ Vague bonus language ("up to 20%")
- ❌ Equity with no liquidity path
- ❌ High base but no equity (at startup)
- ❌ Cliff longer than 1 year
- ❌ Vesting acceleration absent
- ❌ Non-compete restrictions
- ❌ Verbal promises not in writing

### About the Company

- ❌ High turnover (check LinkedIn)
- ❌ Recent layoffs or reorgs
- ❌ Manager seems checked out
- ❌ Glassdoor patterns in bad reviews
- ❌ Funding concerns
- ❌ Unclear path to profitability

### About the Role

- ❌ Vague responsibilities
- ❌ Role seems to change during interviews
- ❌ Red flags in why position is open
- ❌ No growth path discussed
- ❌ Unrealistic expectations set

## Questions to Ask Yourself

### The Gut Check
- Which offer excites me more?
- Which would I regret not taking?
- Which aligns with my 5-year goals?
- Which would I brag about to friends?

### The Monday Morning Test
- Which job do I want to wake up for?
- Which team do I want to work with?
- Which problems do I want to solve?

### The Learning Test
- Where will I grow more?
- Which skills will I develop?
- Which looks better on my resume in 3 years?

### The Risk Test
- What's the downside of each?
- Which failure would I regret more?
- What's my backup plan for each?

## Output Format

When comparing offers:

```markdown
# JOB OFFER COMPARISON

## Offers Being Compared
- **Offer A:** [Role] at [Company]
- **Offer B:** [Role] at [Company]

## Total Compensation Comparison

| Component | Offer A | Offer B | Difference |
|-----------|---------|---------|------------|
| Base | $X | $X | |
| Bonus | $X | $X | |
| Equity (annual) | $X | $X | |
| Benefits | $X | $X | |
| **Year 1 Total** | $X | $X | |
| **Ongoing Total** | $X | $X | |

## Non-Monetary Comparison

| Factor | Offer A | Offer B | Notes |
|--------|---------|---------|-------|
| Career Growth | X/10 | X/10 | |
| Work-Life | X/10 | X/10 | |
| Team/Culture | X/10 | X/10 | |
| Risk Level | X/10 | X/10 | |

## Weighted Analysis

Using your priorities:
- Offer A Score: X.XX
- Offer B Score: X.XX

## Key Differences
1. [Key difference 1]
2. [Key difference 2]
3. [Key difference 3]

## Recommendation

Based on your stated priorities of [X, Y, Z], **Offer [A/B]** appears to be the stronger choice because:
- [Reason 1]
- [Reason 2]
- [Reason 3]

## Things to Clarify Before Deciding
- [ ] [Question for Company A]
- [ ] [Question for Company B]

## Negotiation Opportunities
- [Opportunity 1]
- [Opportunity 2]
```

## Comparison Checklist

- ✅ Calculated total comp (not just base)
- ✅ Included equity with realistic valuation
- ✅ Factored in benefits value
- ✅ Considered tax implications
- ✅ Weighted non-monetary factors
- ✅ Assessed career growth potential
- ✅ Evaluated team and manager quality
- ✅ Checked company stability/risk
- ✅ Aligned with personal priorities
- ✅ Gut-checked the decision
```

## File: `skills/portfolio-case-study-writer/SKILL.md`
```markdown
---
name: Portfolio Case Study Writer
description: Transform resume bullets into detailed portfolio case studies
---

# Portfolio Case Study Writer

## When to Use This Skill

Use this skill when the user:
- Wants to create portfolio case studies
- Needs to expand resume bullets into detailed writeups
- Is building a portfolio website
- Wants to showcase project work in depth
- Mentions: "case study", "portfolio", "project writeup", "work samples", "portfolio piece"

## Core Capabilities

- Transform resume bullets into detailed case studies
- Structure case studies for maximum impact
- Create compelling project narratives
- Balance technical detail with business context
- Format for portfolio websites
- Tailor depth to audience

## Case Study Purpose

**Why Case Studies Matter:**
- Resumes show WHAT you did; case studies show HOW and WHY
- Demonstrate thinking process, not just outcomes
- Allow deeper showcase of skills
- Differentiate you from other candidates
- Required for many PM, UX, and creative roles

## The Case Study Structure

### Standard Structure

```
1. Overview (Project summary)
2. Problem (What needed to be solved)
3. Process (How you approached it)
4. Solution (What you created/delivered)
5. Results (The impact)
6. Learnings (What you'd do differently)
```

### Time to Read
- **Quick Read:** 3-5 minutes (essential for portfolio)
- **Deep Dive:** 10-15 minutes (for interested readers)

## Section-by-Section Guide

### 1. Overview Section

**Purpose:** Hook the reader, provide context

**Include:**
- Project name and company
- Your role
- Timeline
- Team size
- One-sentence summary of impact

**Example:**
```
# Redesigning the Checkout Flow

**Company:** E-Commerce Inc.
**Role:** Lead Product Designer
**Timeline:** 6 weeks
**Team:** 2 designers, 3 engineers, 1 PM

**Summary:** Reduced cart abandonment by 35% through a streamlined 3-step checkout process, generating $2M in recovered revenue.
```

### 2. Problem Section

**Purpose:** Set up why this work mattered

**Include:**
- Business context
- User pain points
- Key metrics or goals
- Constraints

**Example:**
```
## The Problem

E-Commerce Inc. was experiencing 68% cart abandonment—significantly higher than the industry average of 55%. Exit surveys and user research revealed several issues:

- **Too many steps:** Our checkout had 7 screens
- **Forced account creation:** Users had to register before purchasing
- **Hidden costs:** Shipping wasn't shown until step 5
- **Mobile friction:** Forms weren't optimized for mobile

**Goal:** Reduce cart abandonment to below 50% within 3 months.

**Constraints:**
- No changes to existing payment integrations
- Had to maintain PCI compliance
- 6-week timeline before holiday season
```

### 3. Process Section

**Purpose:** Show your thinking and methodology

**Include:**
- Research conducted
- Stakeholders involved
- Hypotheses formed
- Options considered
- Decisions made (and why)

**Example:**
```
## Process

### Research
I started by understanding the problem deeply:
- Analyzed Mixpanel funnel data for drop-off points
- Conducted 10 user interviews with recent abandoners
- Reviewed heatmaps and session recordings
- Benchmarked against 5 competitor checkout flows

**Key Insight:** 73% of drop-offs occurred at the account creation screen. Users wanted to purchase, not commit to a relationship.

### Ideation
I explored several approaches:
1. Guest checkout only (simplest)
2. Social login options (lower friction)
3. Progressive profiling (collect info over time)
4. One-page checkout (Amazon-style)

After weighing feasibility, timeline, and impact, we chose a hybrid approach...

### Decisions Made
- **Guest checkout first:** Made registration optional and post-purchase
- **Transparent pricing:** Showed shipping on the first screen
- **Mobile-first design:** Designed for mobile, then adapted for desktop
- **Progress indicator:** Added clear "Step 1 of 3" indicator
```

### 4. Solution Section

**Purpose:** Show what you actually created

**Include:**
- Visual artifacts (mockups, screenshots, diagrams)
- Key features/changes
- Technical implementation (if relevant)
- How it addressed the problems

**Example:**
```
## Solution

### The New Checkout Flow

**Before:** 7 screens with mandatory registration
**After:** 3 screens with optional guest checkout

[IMAGE: Before/After comparison]

### Key Changes

**1. Transparent Pricing Widget**
[IMAGE: Pricing widget mockup]
Showed order total, shipping, and taxes from the start. No surprises.

**2. Guest Checkout Option**
[IMAGE: Guest checkout screen]
Made account creation optional with clear value proposition for why to register.

**3. Smart Form Design**
[IMAGE: Form design]
- Single-column layout on mobile
- Auto-format for phone/card numbers
- Address autocomplete integration
- Clear error messaging

**4. Trust Signals**
Added security badges, money-back guarantee, and customer service contact throughout the flow.
```

### 5. Results Section

**Purpose:** Prove impact with data

**Include:**
- Quantitative results (with timeframe)
- Comparison to goals
- Secondary metrics affected
- Business impact

**Example:**
```
## Results

### Primary Metrics (90 days post-launch)

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Cart Abandonment | 68% | 44% | -35% |
| Checkout Completion | 32% | 56% | +75% |
| Mobile Conversion | 18% | 41% | +128% |
| Revenue per Visitor | $2.40 | $3.85 | +60% |

### Business Impact
- **$2M additional revenue** in first quarter
- **15% increase in mobile orders**
- **Customer support tickets about checkout** dropped by 45%

### Secondary Effects
- Account creation actually increased 20% (post-purchase)
- Average order value stayed stable
- Return customer rate improved
```

### 6. Learnings Section

**Purpose:** Show growth mindset and self-awareness

**Include:**
- What worked well
- What you'd do differently
- Unexpected challenges
- Skills developed

**Example:**
```
## Learnings

### What Worked
- **Early user research** prevented us from building the wrong solution
- **Cross-functional alignment** meetings kept everyone on the same page
- **Launching with analytics** let us measure impact immediately

### What I'd Do Differently
- **More A/B testing:** We launched the full redesign at once. Would have preferred to test individual changes to understand what drove results.
- **Earlier mobile focus:** We designed desktop-first then adapted. Starting mobile-first would have been more efficient.
- **Stakeholder education:** Spent too long convincing leadership. Would start stakeholder alignment earlier next time.

### Skills Developed
- Advanced Figma prototyping
- Working with A/B testing frameworks
- Presenting data-driven design decisions to executives
```

## Case Study Types by Role

### Product Manager Case Study
**Focus on:**
- Strategy and prioritization
- Stakeholder management
- Metrics and outcomes
- Technical trade-offs

### UX/Product Designer Case Study
**Focus on:**
- User research
- Design process
- Visual artifacts
- Usability improvements

### Software Engineer Case Study
**Focus on:**
- Technical architecture
- Problem-solving approach
- System design
- Code quality/performance

### Marketing Case Study
**Focus on:**
- Strategy and targeting
- Creative execution
- Channel performance
- ROI and attribution

## Visual Elements

### Must-Have Visuals
- Before/after comparisons
- Key screens or deliverables
- Process diagrams
- Results charts

### Nice-to-Have Visuals
- User journey maps
- Wireframes evolution
- Research artifacts
- Team photos

### Visual Tips
- Use consistent image sizing
- Add captions explaining each image
- Blur sensitive data if needed
- Ensure mobile-friendly image sizes

## Output Format

When creating a case study:

```markdown
# CASE STUDY: [PROJECT NAME]

## Quick Facts
- **Role:** [Your role]
- **Company:** [Company]
- **Timeline:** [Duration]
- **Team:** [Team composition]
- **Impact:** [One-line result]

---

## Overview
[2-3 sentence summary of the project]

## Problem
[Context and challenges - what needed to be solved]

## Process
### Research
[What you learned]

### Approach
[How you tackled it]

### Key Decisions
[Important choices and rationale]

## Solution
[What you built/created - include visual descriptions]

### Feature 1
[Description]

### Feature 2
[Description]

## Results
[Quantified impact]

| Metric | Before | After | Change |
|--------|--------|-------|--------|

## Learnings
[Reflections and growth]

---

## Visual Asset List
[List of images/screenshots needed]
```

## Case Study Quality Checklist

- ✅ Clear problem statement
- ✅ Evidence of user/customer focus
- ✅ Process clearly explained
- ✅ Your specific contributions are clear
- ✅ Quantified results
- ✅ Visual artifacts included
- ✅ Honest about challenges/learnings
- ✅ Appropriate length (3-10 min read)
- ✅ Proofread and polished
- ✅ Can discuss in detail in interview
```

## File: `skills/reference-list-builder/SKILL.md`
```markdown
---
name: Reference List Builder
description: Format professional references properly and prepare reference materials
---

# Reference List Builder

## When to Use This Skill

Use this skill when the user:
- Needs to create a professional reference list
- Wants help choosing the right references
- Needs to format references properly
- Is preparing references for job applications
- Mentions: "references", "reference list", "professional references", "reference check"

## Core Capabilities

- Format professional reference lists
- Guide reference selection strategy
- Prepare reference briefing materials
- Anticipate reference check questions
- Handle difficult reference situations
- Coordinate reference outreach

## Reference Strategy

### Who Makes a Good Reference?

**Ideal References:**
- Former direct managers (most important)
- Senior colleagues who observed your work
- Cross-functional partners
- Clients or customers
- Direct reports (for leadership roles)
- Professors or advisors (for recent graduates)

**Reference Hierarchy:**
1. **Most Valuable:** Recent direct supervisor
2. **Very Valuable:** Senior leaders who know your work
3. **Valuable:** Peers and cross-functional partners
4. **Acceptable:** Clients, vendors, professors
5. **Avoid:** Friends, family, HR contacts only

### Who to Avoid

- ❌ Current employer (without permission)
- ❌ People who barely know you
- ❌ References from 10+ years ago only
- ❌ Personal friends (unless specified)
- ❌ People who might give lukewarm feedback
- ❌ Anyone you haven't contacted in advance

## Reference List Format

### Standard Format

```
PROFESSIONAL REFERENCES

Jane Smith
Senior Director of Product
TechCorp Inc.
Phone: (555) 123-4567
Email: jane.smith@techcorp.com
Relationship: Direct supervisor for 3 years (2020-2023)

John Doe
VP of Engineering
Previous Company
Phone: (555) 234-5678
Email: john.doe@previous.com
Relationship: Cross-functional partner on 5 major projects
```

### Information to Include

**Required:**
- Full name
- Current job title
- Current company
- Phone number
- Professional email
- Your relationship to them

**Optional:**
- LinkedIn URL
- Best time to reach
- Preferred contact method

### Formatting Guidelines

- Match the style of your resume (fonts, formatting)
- 3-5 references (more only if requested)
- Separate page from resume
- Header should match resume header
- Include "References" or "Professional References" as title

## Reference Preparation

### Step 1: Ask Permission

**Before listing anyone:**
- Call or email to ask permission
- Confirm their contact information
- Explain the role you're applying for
- Gauge their willingness and enthusiasm

**Script:**
```
"Hi [Name], I hope you're doing well! I'm applying for a [Role] position at [Company] and was wondering if you'd be comfortable serving as a reference for me. The role involves [brief description], and I think your perspective on [specific project/skill] would be particularly valuable. Would you be willing to speak with them if they reach out?"
```

### Step 2: Brief Your References

**Send them:**
- Copy of your resume
- Job description
- Key points you want highlighted
- Specific projects to mention
- Timeline for when they might be contacted

**Briefing Email Template:**
```
Subject: Reference Preparation - [Role] at [Company]

Hi [Name],

Thank you so much for agreeing to be a reference! Here's some context to help:

**The Role:** [Job title] at [Company]
**What they're looking for:** [Key requirements]

**Points I'm emphasizing:**
- [Achievement 1]
- [Achievement 2]
- [Skill they should mention]

**Our work together they might ask about:**
- [Project 1]
- [Project 2]

I've attached my resume and the job description for reference. They may reach out in the next [timeframe].

Please let me know if you have any questions, and thank you again!

Best,
[Your name]
```

### Step 3: Follow Up

After references are checked:
- Thank your references regardless of outcome
- Let them know the result
- Offer to reciprocate

## Handling Special Situations

### Current Employer Doesn't Know

**Options:**
- Ask if reference check can wait until later stage
- Use colleagues who've left the company
- Be upfront: "My current employer doesn't know I'm looking"
- Use other professional references

### Manager Left the Company

**Options:**
- Track them down on LinkedIn
- Use their personal email/phone
- Include their new company in reference list
- Explain "Former manager, now at [New Company]"

### Bad Relationship with Past Manager

**Options:**
- Use another supervisor from that role
- Use senior colleagues instead
- Choose references from different roles
- Be prepared to explain if asked

### Limited Professional Experience

**Options:**
- Professors or academic advisors
- Internship supervisors
- Volunteer organization leaders
- Coaches or mentors
- Client contacts

### Reference Won't Give Positive Review

**Don't use them.** It's better to have fewer references than a lukewarm or negative one.

## What Reference Checkers Ask

### Common Questions

**Performance:**
- "How would you describe [name]'s work?"
- "What were their primary responsibilities?"
- "How did they perform against expectations?"

**Skills:**
- "What are their greatest strengths?"
- "What areas could they improve?"
- "How would you rate their [specific skill]?"

**Work Style:**
- "How did they handle pressure/deadlines?"
- "How did they work with the team?"
- "How did they handle conflict?"

**Character:**
- "Would you rehire them?"
- "Is there anything else I should know?"
- "How do they compare to peers?"

### The "Would You Rehire?" Question

**Most important question.** Brief your references that this may be asked and ensure they can answer enthusiastically.

## Reference List Template

```
[YOUR NAME]
[Your Email] | [Your Phone]

PROFESSIONAL REFERENCES

[REFERENCE 1 - MOST SENIOR/RELEVANT]
[Name]
[Title]
[Company]
Phone: [Number]
Email: [Email]
Relationship: [How you worked together, dates]

[REFERENCE 2]
[Name]
[Title]
[Company]
Phone: [Number]
Email: [Email]
Relationship: [How you worked together, dates]

[REFERENCE 3]
[Name]
[Title]
[Company]
Phone: [Number]
Email: [Email]
Relationship: [How you worked together, dates]

---
References available upon request for additional contacts.
```

## Reference Timing

### When to Provide References

- **Don't include with initial application** (unless requested)
- **Bring to interview** (have them ready)
- **Provide when asked** (usually after final interview)
- **Always ask before sharing** (confirm permission each time)

### Common Timeline

1. **Application:** "References available upon request" (optional on resume)
2. **First Interview:** Have list ready but don't offer
3. **Final Rounds:** "Can you provide references?" → Share list
4. **Reference Check:** Company contacts your references
5. **Offer:** Follow up with references, thank them

## Output Format

When building a reference list:

```markdown
# REFERENCE LIST

## Reference Strategy
**Target Role:** [Position]
**Company:** [Company]

## Recommended References

### Primary References (Use These)

**Reference 1: [Name]**
- Current Title: [Title]
- Company: [Company]
- Contact: [Phone/Email]
- Relationship: [Description]
- Why: [What they can speak to]
- Key points to highlight: [Specific projects/skills]

**Reference 2: [Name]**
[Same format]

**Reference 3: [Name]**
[Same format]

### Backup References (If Needed)

**Reference 4: [Name]**
[Same format]

## Briefing Notes

### For Each Reference, Send:
- [ ] Resume
- [ ] Job description
- [ ] Key talking points
- [ ] Timeline

### Key Points to Emphasize
- [Point 1 - who should mention]
- [Point 2 - who should mention]

## Reference Outreach

### Permission Request Script
[Customized script]

### Briefing Email
[Draft briefing email]

### Thank You Template
[Post-check thank you message]
```

## Reference Checklist

- ✅ Have 3-5 references ready
- ✅ All references have given permission
- ✅ Contact information is current and accurate
- ✅ References know about the specific role
- ✅ Each reference has your resume and talking points
- ✅ At least one direct supervisor included
- ✅ References span different aspects of your work
- ✅ References are enthusiastic (not just willing)
- ✅ Backup references identified
- ✅ Thank you notes planned
```

## File: `skills/resume-ats-optimizer/SKILL.md`
```markdown
---
name: Resume ATS Optimizer
description: Optimize resumes for Applicant Tracking Systems, check ATS compatibility, and analyze keyword match
---

# Resume ATS Optimizer

## When to Use This Skill

Use this skill when the user wants to:
- Optimize their resume for Applicant Tracking Systems (ATS)
- Check if their resume will pass automated screening
- Understand why their applications aren't getting responses
- Mentions keywords like: "ATS", "not getting interviews", "resume not working", "optimize resume", "keyword optimization"

Also use when the user provides a resume file and mentions they're applying to jobs.

## Core Capabilities

- Parse resume and test ATS compatibility
- Extract and analyze keywords against job descriptions
- Identify formatting issues that break ATS parsers
- Calculate match scores between resume and job postings
- Suggest keyword additions and placements
- Generate ATS-friendly formatting recommendations

## The ATS Problem

75% of resumes are rejected by Applicant Tracking Systems before a human ever sees them. Companies use ATS to:
- Filter out unqualified candidates automatically
- Search for specific keywords from job requirements
- Parse resumes into structured data
- Rank candidates by keyword match percentage

Common reasons resumes fail ATS:
1. Poor formatting (tables, columns, headers/footers)
2. Missing keywords from job description
3. Inconsistent section headers
4. Non-standard fonts or special characters
5. Text embedded in images
6. Incorrect file format

## ATS Compatibility Checklist

### File Format
- ✅ Use .docx or .pdf (not .pages, .odt)
- ✅ PDF must be text-based, not scanned image
- ✅ File name: "FirstName_LastName_Resume.pdf"

### Font & Formatting
- ✅ Standard fonts: Arial, Calibri, Georgia, Times New Roman
- ✅ Font size: 10-12pt for body, 14-16pt for headers
- ✅ No text boxes, tables, or columns
- ✅ No headers/footers (put contact info in body)
- ✅ No images, graphics, or charts
- ✅ Consistent date formats (MM/YYYY)
- ✅ Standard bullet points (•, -, *)

### Section Headers
Use standard, recognizable headers:
- ✅ "Professional Experience" or "Work Experience" (not "Where I've Been")
- ✅ "Education" (not "Academic Background")
- ✅ "Skills" (not "Core Competencies")
- ✅ "Summary" or "Professional Summary"

### Contact Information
```
John Smith
email@example.com | (555) 123-4567 | LinkedIn: linkedin.com/in/johnsmith
San Francisco, CA
```

NOT in header/footer, and avoid:
- ❌ Tables for contact info
- ❌ Special characters in email
- ❌ Multiple phone numbers
- ❌ Full mailing address (city/state is enough)

## Keyword Optimization Process

### Step 1: Extract Job Description Keywords

Identify three types of keywords:

**Hard Skills (Technical)**
- Programming languages (Python, Java, SQL)
- Tools and platforms (Salesforce, AWS, Excel)
- Certifications (PMP, CPA, CFA)
- Methodologies (Agile, Six Sigma, SDLC)

**Soft Skills**
- Leadership, collaboration, communication
- Problem-solving, analytical thinking
- Project management, stakeholder management

**Industry Terms**
- B2B, SaaS, e-commerce
- Enterprise, SMB, mid-market
- ARR, MRR, churn rate

### Step 2: Match Analysis

For each keyword in job description:
1. Check if exact phrase appears in resume
2. Check for synonyms or variations
3. Count frequency of mention
4. Note location (summary, experience, skills)

### Step 3: Calculate Match Score

```
Match Score = (Keywords Matched / Total Required Keywords) × 100

Example:
Job has 20 required keywords
Your resume has 15 of them
Match Score = 75%

Target: 80%+ for strong match
```

### Step 4: Keyword Placement Strategy

**Priority 1: Professional Summary (Top of Resume)**
- Include 5-8 most important keywords
- Use naturally in 3-4 sentence paragraph
- Example: "Data Scientist with 5+ years using Python, SQL, and machine learning to drive business insights..."

**Priority 2: Skills Section**
- List keywords explicitly
- Group by category if needed
- Use exact phrasing from job description

**Priority 3: Experience Bullets**
- Incorporate keywords into achievement statements
- Don't force keywords unnaturally
- Use variations throughout

**Keyword Density Guidelines:**
- Critical keywords: Appear 2-4 times throughout resume
- Important keywords: Appear 1-2 times
- Don't keyword stuff - keep it natural
- Vary phrasing (e.g., "led team" and "team leadership")

## Analysis Output Format

When analyzing a resume, provide this structured report:

```markdown
# ATS COMPATIBILITY REPORT

## Overall Score: [X]/100

### File Format Check ✅/❌
- Format: [DOCX/PDF]
- Text extraction: [Success/Failed]
- File size: [X KB/MB]

### Formatting Issues
✅ No tables or columns detected
❌ Contact info in header (move to body)
⚠️  Two different font sizes in skills section

### Keyword Analysis

JOB REQUIREMENTS vs YOUR RESUME:

**Critical Keywords (Must Have):**
✅ Project Management - Found 3x
✅ Agile/Scrum - Found 2x
❌ Stakeholder Management - MISSING (mentioned 5x in JD)
❌ Budget Management - MISSING (mentioned 3x in JD)

**Important Keywords:**
✅ Cross-functional teams - Found 1x
⚠️  "Risk management" - You have "risk mitigation" (close but not exact match)
✅ Process improvement - Found 2x

**Match Score: 65%**
Target: 80%+ recommended

### Recommended Changes

**1. Add Missing Keywords:**

In Professional Summary, change:
"Experienced project manager with proven track record..."

To:
"Experienced project manager with proven track record in stakeholder management and budget oversight..."

In Experience section, add bullet:
"Managed stakeholder communication across 3 departments and executive leadership team"
"Directed budget management for $2.5M project portfolio"

**2. Fix Formatting:**
- Move contact information from header to body of resume
- Make all skill section items same font size (currently 10pt and 11pt mixed)

**3. Strengthen Existing Keywords:**
Change "risk mitigation" to "risk management" for exact match

### Estimated New Match Score: 85%
```

## Common ATS Failure Patterns

### Pattern 1: Creative Formatting
```
❌ PROBLEM:
[Two-column layout with graphics]
[Skill bars and proficiency charts]
[Text in colored boxes]

✅ SOLUTION:
- Single column layout
- Text-only skills list
- Simple bullet points
```

### Pattern 2: Unconventional Section Names
```
❌ PROBLEM:
"My Journey" (instead of Experience)
"What I Bring to the Table" (instead of Skills)
"Academic Pursuits" (instead of Education)

✅ SOLUTION:
Use standard headers ATS recognizes
```

### Pattern 3: Missing Keywords
```
❌ PROBLEM:
Job requires: "Python, SQL, Data Visualization"
Resume says: "Programming, databases, making charts"

✅ SOLUTION:
Use exact terminology from job description
```

### Pattern 4: Keyword Stuffing
```
❌ PROBLEM:
Skills: Python, Python programming, Python developer, Python expert, Python specialist, Advanced Python...

✅ SOLUTION:
Skills: Python, SQL, JavaScript, React, Node.js
(Then incorporate naturally in bullets)
```

## Industry-Specific Considerations

### Tech Resumes
- Emphasize programming languages and frameworks
- Include GitHub, portfolio links in Skills section (not header)
- Certifications and courses matter highly

### Business/Finance
- Focus on software proficiency (Excel, SAP, Salesforce)
- Certifications critical (CPA, CFA, PMP)
- Industry keywords (P&L, ROI, KPI)

### Healthcare
- Licenses and certifications required
- Specific systems (Epic, Cerner, MEDITECH)
- Compliance keywords (HIPAA, Joint Commission)

### Marketing
- Platform expertise (HubSpot, Salesforce, Google Analytics)
- Channel keywords (SEO, PPC, email marketing)
- Metrics and results-driven language

## Edge Cases & Special Situations

### Career Changers
- Focus on transferable skills
- Use keywords from TARGET industry, not just current
- May need two resume versions for ATS

### Recent Graduates
- Education section becomes priority for keywords
- Include relevant coursework, projects
- Internships count as experience - use those keywords

### Executive Level
- ATS still matters for senior roles
- Focus on strategic keywords
- Include board experience, P&L size, team size

### Gaps in Employment
- Use years only (not months) if it helps
- Include freelance/consulting with keywords
- Volunteer work can include relevant keywords

## Implementation Checklist

When helping user optimize for ATS:

1. ✅ Scan current resume for ATS compatibility issues
2. ✅ Analyze job description for required keywords
3. ✅ Calculate current match score
4. ✅ Identify specific missing keywords
5. ✅ Suggest exact placements for new keywords
6. ✅ Flag formatting problems
7. ✅ Provide before/after examples
8. ✅ Re-score after suggested changes
9. ✅ Verify file format and naming
10. ✅ Test with ATS simulator if possible

## Success Metrics

After optimization, the resume should:
- Score 80%+ match for target job descriptions
- Pass ATS parsing test (all sections recognized)
- Have zero formatting errors
- Include all critical keywords 2-4x each
- Read naturally (not keyword-stuffed)
- Be ready to submit immediately
```

## File: `skills/resume-bullet-writer/SKILL.md`
```markdown
---
name: Resume Bullet Writer
description: Transform weak resume bullets into achievement-focused statements with metrics and impact
---

# Resume Bullet Writer

## When to Use This Skill

Use this skill when the user wants to:
- Write or improve resume bullet points
- Transform weak descriptions into strong achievements
- Add metrics and quantifiable results
- Make their experience more compelling
- Mentions: "improve my bullets", "make my resume stronger", "quantify my achievements", "results-driven"

Also use when you see weak bullets that need improvement (passive language, no metrics, vague descriptions).

## Core Capabilities

- Transform weak bullet points into achievement-focused statements
- Apply STAR method and X-Y-Z formula
- Add quantifiable metrics and results
- Use strong action verbs
- Tailor bullets to specific roles/industries
- Ensure every bullet shows impact, not just duties

## The Bullet Point Problem

Most resumes have weak bullets that list job duties instead of achievements:

❌ **Weak Bullets (What NOT to do):**
- "Responsible for managing team"
- "Helped with customer service"
- "Worked on improving processes"
- "Assisted with projects"

These are passive, vague, and don't show impact or results.

✅ **Strong Bullets (What TO do):**
- "Led cross-functional team of 12 to deliver $2M product, increasing revenue by 35%"
- "Resolved 50+ customer issues daily, improving satisfaction scores from 3.2 to 4.8/5"
- "Streamlined approval process, reducing cycle time by 40% (from 10 to 6 days)"
- "Managed portfolio of 8 concurrent projects with 100% on-time delivery rate"

These are active, specific, and quantify the impact.

## Core Frameworks

### 1. The X-Y-Z Formula (Google Method)

**Structure:** "Accomplished [X] as measured by [Y] by doing [Z]"

- X = What you achieved
- Y = How you measured it
- Z = What actions you took

**Examples:**

```
❌ BEFORE: "Managed social media accounts"

✅ AFTER: "Grew Instagram following by 250% (5K to 17.5K) by implementing daily content calendar and influencer partnerships"

X = Grew Instagram following by 250%
Y = 5K to 17.5K followers
Z = Daily content calendar + influencer partnerships
```

```
❌ BEFORE: "Improved customer service"

✅ AFTER: "Increased customer satisfaction scores by 40% (3.2 to 4.5/5) by redesigning support ticketing system and training 15 agents"

X = Increased customer satisfaction by 40%
Y = 3.2 to 4.5 out of 5
Z = Redesigned ticketing system + trained agents
```

### 2. STAR Method

**Structure:**
- **S**ituation: What was the context?
- **T**ask: What needed to be done?
- **A**ction: What did YOU specifically do?
- **R**esult: What was the measurable outcome?

**Example:**

Full STAR story:
"Inherited underperforming sales team (S) with 65% quota attainment. Tasked with improving performance within Q1 (T). Implemented new training program and revised commission structure (A). Achieved 92% quota attainment by Q2, generating $1.8M additional revenue (R)."

For resume bullet (condensed STAR):
"Revitalized underperforming sales team through training program and commission restructure, improving quota attainment from 65% to 92% and generating $1.8M additional revenue"

### 3. CAR Method (Alternative to STAR)

**Structure:**
- **C**hallenge: What problem existed?
- **A**ction: What did you do about it?
- **R**esult: What happened?

**Example:**

"Reduced customer churn (C) by implementing proactive outreach program (A), retaining 85% of at-risk accounts worth $500K ARR (R)"

## Power Verbs by Category

### Leadership & Management
- Led, Directed, Managed, Supervised, Coordinated
- Spearheaded, Orchestrated, Oversaw, Championed, Mentored

### Achievement & Success
- Achieved, Delivered, Exceeded, Surpassed, Attained
- Secured, Won, Earned, Captured, Clinched

### Growth & Improvement
- Grew, Increased, Boosted, Expanded, Scaled
- Elevated, Amplified, Maximized, Accelerated, Doubled

### Creation & Innovation
- Created, Developed, Designed, Built, Launched
- Pioneered, Established, Founded, Introduced, Originated

### Optimization & Efficiency
- Streamlined, Optimized, Enhanced, Improved, Revitalized
- Transformed, Restructured, Modernized, Automated, Simplified

### Analysis & Strategy
- Analyzed, Assessed, Evaluated, Identified, Diagnosed
- Researched, Investigated, Examined, Audited, Forecasted

### Collaboration & Communication
- Collaborated, Partnered, Facilitated, Coordinated, United
- Presented, Communicated, Negotiated, Influenced, Persuaded

### Problem-Solving
- Resolved, Solved, Troubleshot, Rectified, Debugged
- Eliminated, Reduced, Mitigated, Prevented, Corrected

## Quantification Strategies

Every bullet should have at least ONE number. Here's how to find metrics:

### Types of Metrics to Include

**1. Money**
- Revenue generated: "$2M in new revenue"
- Money saved: "Reduced costs by $50K annually"
- Budget managed: "Managed $5M project budget"
- Deal size: "Closed 3 enterprise deals worth $500K"

**2. Percentages**
- Growth: "Increased conversion rate by 45%"
- Improvement: "Reduced error rate by 60%"
- Efficiency: "Decreased processing time by 30%"
- Quality: "Improved accuracy from 85% to 98%"

**3. Time**
- Speed: "Reduced load time from 8s to 2s"
- Frequency: "Delivered weekly reports to 50+ stakeholders"
- Duration: "Completed 6-month project in 4 months"
- Saved time: "Automated process, saving team 10 hours/week"

**4. Scale/Volume**
- People: "Led team of 15", "Trained 50+ employees"
- Projects: "Managed 8 concurrent initiatives"
- Customers: "Served 500+ enterprise clients"
- Users: "Built product used by 100K+ daily active users"

**5. Comparison/Before-After**
- "Increased from X to Y"
- "Reduced from X to Y"
- "Grew from X to Y"

### When You Don't Have Exact Numbers

Use estimation strategies:

**Approximate with ~**
"Improved performance by ~40%"

**Use ranges**
"Managed team of 8-12 people"
"Generated $50K-$75K in monthly revenue"

**Use conservative estimates**
If you think it was 60%, say 50%
If you saved 100 hours, say 75 hours

**Quantify inputs if outputs unknown**
Can't measure revenue? Quantify activities:
- "Conducted 30+ customer interviews"
- "Analyzed 500+ data points"
- "Created 20+ marketing campaigns"

**Find related metrics**
Can't measure conversion? Measure traffic, engagement, or other funnel metrics

## Industry-Specific Bullet Examples

### Software Engineering

❌ WEAK:
- Wrote code for new features
- Fixed bugs in production
- Worked with product team

✅ STRONG:
- Architected authentication microservice serving 500K+ daily active users, reducing login latency by 60% (from 5s to 2s)
- Resolved 50+ critical production bugs over 6 months, improving system uptime from 97.2% to 99.8%
- Collaborated with product team to deliver 12 features ahead of schedule, resulting in 25% increase in user engagement

### Product Management

❌ WEAK:
- Managed product roadmap
- Worked with stakeholders
- Launched new features

✅ STRONG:
- Defined and executed product roadmap for $10M ARR product, prioritizing 50+ feature requests from 200+ customers
- Facilitated weekly stakeholder meetings with engineering, design, and executive teams to align on strategic priorities
- Launched 8 major features in 12 months, driving 40% increase in customer retention and $2M additional revenue

### Sales

❌ WEAK:
- Met with clients
- Closed deals
- Exceeded quota

✅ STRONG:
- Generated $3.2M in new business revenue by closing 15 enterprise deals, achieving 142% of annual quota
- Managed sales cycle for 50+ prospects simultaneously, maintaining 35% close rate (company average: 22%)
- Exceeded quarterly quota 8 consecutive quarters, ranking #2 out of 45 sales reps nationwide

### Marketing

❌ WEAK:
- Created marketing campaigns
- Managed social media
- Analyzed campaign performance

✅ STRONG:
- Launched 12 multi-channel campaigns generating $500K in attributed revenue and 2,500+ qualified leads
- Grew LinkedIn audience by 400% (3K to 15K followers) through thought leadership content strategy, resulting in 200+ inbound demo requests
- Analyzed campaign performance across 8 channels using Google Analytics, identifying 3 top-performing channels responsible for 75% of conversions

### Customer Success

❌ WEAK:
- Helped customers with problems
- Managed customer accounts
- Conducted onboarding sessions

✅ STRONG:
- Maintained 95% customer retention rate across portfolio of 50 enterprise accounts representing $4M ARR
- Resolved 40+ customer issues weekly with average response time of 2 hours, achieving 4.9/5 CSAT score
- Delivered 25+ onboarding sessions for new customers, achieving 90% product adoption rate within first 30 days

### Data Analysis

❌ WEAK:
- Analyzed data
- Created reports
- Made recommendations

✅ STRONG:
- Analyzed 500K+ transaction records to identify $2M revenue opportunity, presented findings to C-suite resulting in new product line
- Built automated reporting dashboard in Tableau reducing manual reporting time by 15 hours/week for team of 8
- Developed predictive model with 85% accuracy for customer churn, enabling proactive retention campaigns that saved $500K ARR

### Operations/Project Management

❌ WEAK:
- Managed projects
- Coordinated with teams
- Tracked progress

✅ STRONG:
- Led 8 cross-functional projects simultaneously with 100% on-time delivery rate and zero budget overruns across $5M portfolio
- Coordinated efforts across engineering, design, and marketing teams (30+ people) to launch product ahead of schedule
- Implemented project tracking system reducing status meeting time by 50% and improving visibility for 15+ stakeholders

## Common Bullet Writing Mistakes

### Mistake 1: Passive Language
❌ "Was responsible for..."
❌ "Helped with..."
❌ "Assisted in..."
❌ "Participated in..."

✅ Use active verbs: Led, Created, Delivered, Achieved

### Mistake 2: No Metrics
❌ "Improved website performance"
✅ "Improved website load time by 60% (8s to 3.2s)"

❌ "Managed large team"
✅ "Led cross-functional team of 25 across 4 departments"

### Mistake 3: Job Duties Instead of Achievements
❌ "Responsible for customer support"
✅ "Resolved 50+ tickets daily with 98% customer satisfaction score"

❌ "Managed social media accounts"
✅ "Grew social media following by 300% (10K to 40K) in 8 months"

### Mistake 4: Too Vague
❌ "Worked with stakeholders"
✅ "Facilitated weekly meetings with 15+ stakeholders across engineering, product, and executive teams"

❌ "Improved processes"
✅ "Streamlined approval workflow, reducing cycle time from 10 to 4 days (60% improvement)"

### Mistake 5: Too Long
❌ "Was responsible for managing and overseeing all aspects of the customer success function including onboarding, training, support, and retention for a portfolio of enterprise clients..."

✅ "Led customer success for 50 enterprise clients ($3M ARR), achieving 95% retention rate"

**Rule: Keep bullets to 1-2 lines maximum**

## Bullet Writing Process

### Step 1: Start with the Weak Bullet
```
Original: "Managed social media"
```

### Step 2: Ask Clarifying Questions
- What platforms?
- How many followers?
- What growth did you achieve?
- What specific actions did you take?
- What business impact resulted?

### Step 3: Gather Information
- Platforms: Instagram, LinkedIn
- Started: 5K followers
- Ended: 18K followers  
- Actions: Daily content calendar, influencer partnerships
- Impact: 200 leads generated

### Step 4: Apply Formula
Using X-Y-Z:
"Grew Instagram and LinkedIn following by 260% (5K to 18K) by implementing daily content calendar and 15 influencer partnerships, generating 200+ qualified leads"

### Step 5: Optimize Length
If too long, prioritize most impressive metrics:
"Grew social media audience by 260% (5K to 18K followers) through content strategy and influencer partnerships, generating 200+ leads"

## Bullet Strength Checklist

Every bullet should have:
- ✅ Strong action verb (avoid "responsible for", "helped")
- ✅ At least one number/metric
- ✅ Specific outcome or result
- ✅ Context of scale (team size, budget, users, etc.)
- ✅ 1-2 lines maximum
- ✅ Reads as an achievement, not a duty
- ✅ Relevant to target role

## Output Format

When rewriting bullets, provide:

```markdown
## BULLET IMPROVEMENTS

### Original Bullet #1:
"Managed customer accounts"

### Issues:
- Passive language ("managed")
- No metrics
- Vague (what does "managed" mean?)
- No results shown

### Improved Version:
"Grew portfolio of 40 enterprise accounts from $2M to $3.5M ARR (75% growth) through quarterly business reviews and proactive upselling strategy"

### What Changed:
- Added scale (40 accounts)
- Added growth metric (75%, $2M to $3.5M)
- Specified actions (QBRs, upselling)
- Shows business impact (revenue growth)

---

### Original Bullet #2:
[Continue for each bullet...]
```

## Special Situations

### For Entry-Level/Recent Graduates
Focus on:
- Academic projects with real impact
- Internship achievements
- Relevant coursework projects
- Volunteer work with quantifiable results
- Club leadership with metrics

Example:
"Led university marketing club of 50 members, organizing 8 events attended by 300+ students and securing $10K in corporate sponsorships"

### For Career Changers
Focus on:
- Transferable skills
- Reframe old experience for new industry
- Highlight relevant projects/side work
- Emphasize learning and adaptation

Example:
"Managed cross-functional teams of 15 (traditional retail) → can become:
"Led cross-functional teams of 15 across operations, merchandising, and customer experience, coordinating workflows and achieving 100% project completion rate"

### For Gaps in Employment
Focus on:
- Freelance/consulting work
- Volunteer achievements
- Side projects
- Professional development

Don't draw attention to gaps, just fill space with relevant achievements.

## Implementation Checklist

For each resume bullet:
1. ✅ Identify weak verb → Replace with power verb
2. ✅ Check for metrics → Add at least one number
3. ✅ Verify it shows result → Add outcome/impact
4. ✅ Confirm specificity → Remove vague language
5. ✅ Test length → Keep to 1-2 lines
6. ✅ Read aloud → Ensure it sounds natural
7. ✅ Verify relevance → Aligns with target role
```

## File: `skills/resume-formatter/SKILL.md`
```markdown
---
name: Resume Formatter
description: Ensure ATS-friendly formatting and create clean scannable layouts
---

# Resume Formatter

## When to Use This Skill

Use this skill when the user:
- Needs help with resume layout and formatting
- Has a messy or hard-to-read resume
- Wants to ensure ATS compatibility through formatting
- Needs a clean, professional design
- Mentions: "format resume", "resume layout", "resume design", "clean resume", "professional format"

## Core Capabilities

- Structure resumes for optimal readability
- Ensure ATS compatibility through formatting
- Create visual hierarchy
- Optimize white space and margins
- Select appropriate fonts and sizes
- Balance aesthetic appeal with functionality

## Formatting Fundamentals

### The Dual Audience Challenge

Your resume must work for:
1. **ATS (Applicant Tracking Systems)** - Robots that parse text
2. **Human Readers** - Recruiters who scan quickly

**The Solution:** Clean, simple formatting that satisfies both.

## Document Setup

### Page Length
- **Entry Level (0-5 years):** 1 page
- **Mid-Level (5-15 years):** 1-2 pages
- **Senior/Executive (15+ years):** 2 pages (max 3 for executives)

### Margins
- **Recommended:** 0.5" - 1" all sides
- **Minimum:** 0.5" (don't go smaller)
- **Maximum:** 1" (don't waste space)

### Font Selection

**Safe, ATS-Friendly Fonts:**
- **Sans-serif:** Arial, Calibri, Helvetica, Verdana
- **Serif:** Times New Roman, Georgia, Garamond

**Font Sizes:**
- **Name:** 16-20pt
- **Section Headers:** 12-14pt
- **Body Text:** 10-12pt
- **Minimum readable:** 10pt

### Spacing
- **Line spacing:** 1.0 to 1.15
- **Space after paragraphs:** 6-12pt
- **Section spacing:** 12-16pt between sections

## ATS-Safe Formatting Rules

### DO:
- ✅ Use standard fonts
- ✅ Use simple bullet points (•, -, *)
- ✅ Use bold and italic sparingly
- ✅ Use standard section headers
- ✅ Save as .docx or text-based .pdf
- ✅ Put contact info in body (not header)
- ✅ Use single column layout
- ✅ Use consistent formatting throughout

### DON'T:
- ❌ Use tables (except simple ones for contact info)
- ❌ Use text boxes
- ❌ Use columns (multi-column layouts)
- ❌ Use headers/footers for important info
- ❌ Use images or graphics
- ❌ Use unusual fonts
- ❌ Use skill bars or progress indicators
- ❌ Use special characters or emojis
- ❌ Use color for essential information

## Section Organization

### Standard Section Order

```
1. Contact Information
2. Professional Summary (optional)
3. Skills/Technical Skills
4. Professional Experience
5. Education
6. Certifications (if relevant)
7. Additional (volunteer, languages, etc.)
```

### Section Header Formatting

**ATS-Recognized Headers:**
- PROFESSIONAL EXPERIENCE or WORK EXPERIENCE
- EDUCATION
- SKILLS or TECHNICAL SKILLS
- PROFESSIONAL SUMMARY or SUMMARY
- CERTIFICATIONS
- PROJECTS

**Format Options:**
```
PROFESSIONAL EXPERIENCE
━━━━━━━━━━━━━━━━━━━━━━

or

Professional Experience
_______________________

or

PROFESSIONAL EXPERIENCE
```

## Contact Information Layout

### Recommended Format
```
JOHN SMITH
john.smith@email.com | (555) 123-4567 | linkedin.com/in/johnsmith
San Francisco, CA
```

### Alternative Format
```
JOHN SMITH
San Francisco, CA
john.smith@email.com | (555) 123-4567
LinkedIn: linkedin.com/in/johnsmith | GitHub: github.com/johnsmith
```

### What to Include
- ✅ Full name
- ✅ Professional email
- ✅ Phone number
- ✅ City, State (no full address needed)
- ✅ LinkedIn URL
- ✅ Portfolio/GitHub (if relevant)

### What to Exclude
- ❌ Full street address
- ❌ Photo
- ❌ Date of birth
- ❌ Marital status
- ❌ Multiple phone numbers
- ❌ Personal social media

## Experience Section Formatting

### Standard Format
```
COMPANY NAME | City, ST
Job Title | Month Year - Month Year

• Achievement bullet with metrics and results
• Achievement bullet with metrics and results
• Achievement bullet with metrics and results
```

### Alternative Format
```
Job Title
COMPANY NAME, City, ST                    Month Year - Month Year

• Achievement bullet with metrics and results
• Achievement bullet with metrics and results
```

### Date Formatting
- **Consistent format:** Use same format throughout
- **Recommended:** Month Year (Jan 2020 - Present)
- **Also acceptable:** MM/YYYY (01/2020 - Present)
- **Avoid:** Full dates (January 15, 2020)

### Bullet Point Guidelines
- **Length:** 1-2 lines each
- **Format:** Start with action verb, end with result
- **Quantity:** 3-6 bullets per role (more for recent, fewer for old)
- **Symbol:** Use standard bullets (•, -, *)

## Skills Section Formatting

### Option 1: Simple List
```
SKILLS
Python, JavaScript, SQL, React, Node.js, AWS, Docker, Git, Agile, JIRA
```

### Option 2: Categorized
```
TECHNICAL SKILLS
Languages: Python, JavaScript, TypeScript, SQL
Frameworks: React, Node.js, Django, Flask
Tools: AWS, Docker, Kubernetes, Git, Jenkins
```

### Option 3: Columns (Careful with ATS)
```
SKILLS
Languages        Frameworks       Tools
Python           React            AWS
JavaScript       Node.js          Docker
SQL              Django           Git
```

**Note:** Multi-column layouts may cause ATS issues. Test before using.

## Education Section Formatting

### Standard Format
```
EDUCATION
Bachelor of Science in Computer Science
University of California, Berkeley | 2018
GPA: 3.8/4.0 (include if 3.5+)
```

### With Honors/Details
```
EDUCATION
MBA, Finance & Strategy | Stanford Graduate School of Business | 2020
• Graduated with Distinction
• Relevant Coursework: Corporate Finance, M&A Strategy
```

## Visual Hierarchy Principles

### Hierarchy Order
1. **Name** - Largest, most prominent
2. **Section Headers** - Clear divisions
3. **Job Titles/Company Names** - Easy to scan
4. **Bullet Points** - The details

### Creating Hierarchy
- Use font SIZE to create levels
- Use **BOLD** for emphasis (names, titles, headers)
- Use CAPS for section headers
- Use consistent spacing to separate sections

## White Space Management

### Good White Space:
- Between sections (clear separation)
- After headings (visual breathing room)
- Between bullets (don't cram)
- Around margins (frame the content)

### Bad White Space:
- Huge gaps between sections
- Inconsistent spacing
- Half-empty pages
- Excessive margins eating space

## Common Formatting Mistakes

### Mistake 1: Wall of Text
**Problem:** Dense paragraphs with no bullets
**Solution:** Use bullet points, keep paragraphs short

### Mistake 2: Inconsistent Formatting
**Problem:** Different fonts, sizes, or styles throughout
**Solution:** Pick one format and stick to it

### Mistake 3: Trying to Be Creative
**Problem:** Fancy designs that break ATS
**Solution:** Save creativity for portfolio, not resume

### Mistake 4: Too Much Information
**Problem:** Cramming everything onto one page
**Solution:** Edit ruthlessly, prioritize relevance

### Mistake 5: Not Enough Information
**Problem:** Half-page resume with massive margins
**Solution:** Add detail, reduce margins (to 0.5")

## File Format Guidelines

### For Online Applications
- **.docx** - Best for ATS parsing
- **.pdf** - Good if created from Word (not scanned)

### For Email/Direct Send
- **.pdf** - Preserves formatting

### File Naming
```
FirstName_LastName_Resume.pdf
JohnSmith_Resume_ProductManager.pdf
```

**Avoid:**
- resume_final_v2_updated_FINAL.docx
- resume (1).pdf
- Untitled document.docx

## Output Format

When formatting a resume:

```markdown
# RESUME FORMATTING REVIEW

## Current Issues
- [ ] [Issue 1]
- [ ] [Issue 2]
- [ ] [Issue 3]

## Recommended Changes

### Document Setup
- Margins: [Current] → [Recommended]
- Font: [Current] → [Recommended]
- Font sizes: [Current] → [Recommended]

### Section Order
**Current:** [Current order]
**Recommended:** [New order and why]

### Visual Improvements
- [Specific change 1]
- [Specific change 2]

### ATS Compatibility Fixes
- [Fix 1]
- [Fix 2]

## Before/After Preview

### Before:
[Description or example of current formatting]

### After:
[Description or example of improved formatting]
```

## Quick Formatting Checklist

Before submitting any resume:
- ✅ One page (or two if warranted)
- ✅ Standard font (10-12pt body)
- ✅ Consistent formatting throughout
- ✅ Clear section headers
- ✅ Appropriate white space
- ✅ No tables, text boxes, or columns
- ✅ Contact info in body (not header)
- ✅ Saved as .docx or .pdf
- ✅ Proper file name
- ✅ Proofread for consistency
```

## File: `skills/resume-quantifier/SKILL.md`
```markdown
---
name: Resume Quantifier
description: Find opportunities to add metrics and estimate numbers when exact data unavailable
---

# Resume Quantifier

## When to Use This Skill

Use this skill when the user:
- Needs to add metrics and numbers to their resume
- Has bullets without quantifiable results
- Doesn't know what numbers to include
- Says they "don't have metrics" or "can't measure impact"
- Mentions: "add metrics", "quantify", "add numbers", "measure impact", "no data"

## Core Capabilities

- Find hidden metrics in any experience
- Estimate numbers when exact data unavailable
- Create before/after comparisons
- Identify measurable impact points
- Transform vague statements into quantified achievements
- Guide users to discover their metrics

## Why Quantification Matters

**The Problem:**
- "Managed projects" vs "Managed 12 projects worth $2M"
- "Improved processes" vs "Reduced cycle time by 40%"
- "Helped customers" vs "Resolved 50+ tickets daily with 98% satisfaction"

**Studies Show:**
- Resumes with numbers get 30% more attention
- Quantified bullets are 40% more memorable
- Numbers provide credibility and scale

## The Quantification Framework

### Categories of Metrics

**1. Money**
- Revenue generated
- Costs reduced/saved
- Budget managed
- Deal sizes closed
- Profit margins improved

**2. Time**
- Hours saved
- Cycle time reduced
- Project duration
- Response times
- Time to market

**3. Percentages**
- Growth rates
- Improvement percentages
- Efficiency gains
- Error reduction
- Conversion rates

**4. Volume/Scale**
- Number of customers/users
- Projects managed
- Team size
- Transactions processed
- Items produced

**5. Quality**
- Satisfaction scores
- Error rates
- Accuracy rates
- Compliance rates
- SLA adherence

**6. Frequency**
- Per day/week/month
- Annual totals
- Meeting cadences
- Report cycles

## Finding Hidden Metrics

### The Discovery Questions

For any experience, ask:

**Scale Questions:**
- How many people/projects/customers?
- What was the budget/revenue involved?
- How large was the team?
- How many locations/regions?

**Impact Questions:**
- What changed because of your work?
- What would have happened without you?
- What problems did you solve?
- What got better/faster/cheaper?

**Comparison Questions:**
- How was it before vs. after?
- How did you compare to others/previous results?
- What was the baseline you improved?

### Role-Specific Metric Discovery

**Sales:**
- Quota attainment percentage
- Revenue generated
- Number of deals closed
- Average deal size
- Pipeline generated
- New accounts acquired
- Retention rate

**Marketing:**
- Leads generated
- Campaign ROI
- Engagement rates
- Follower growth
- Website traffic increase
- Conversion rates
- Brand awareness metrics

**Customer Service:**
- Tickets resolved per day
- Customer satisfaction score
- Average response time
- First call resolution rate
- NPS score contribution

**Operations:**
- Efficiency improvements
- Cost reductions
- Process cycle times
- Error rate reductions
- Throughput increases

**Engineering:**
- System uptime
- Performance improvements
- Bug resolution rate
- Deployment frequency
- Code coverage

**Project Management:**
- Number of projects
- Budget sizes
- Team sizes
- On-time delivery rate
- Stakeholders managed

**HR/Admin:**
- Hiring numbers
- Time to fill
- Employee satisfaction scores
- Training completion rates
- Onboarding efficiency

## Estimation Techniques

When you don't have exact numbers:

### Conservative Estimation

**Principle:** Estimate low to maintain credibility

**Example:**
- You think you saved 100 hours/month → say "75+ hours"
- You think growth was 50% → say "~40%"
- You think you served 500 customers → say "400+"

### Range Estimation

**Format:** "X-Y" or "X to Y"

**Examples:**
- "Managed team of 8-12"
- "Generated $100K-$150K in revenue"
- "Saved 20-30 hours weekly"

### Minimum Bound

**Format:** "X+" or "at least X"

**Examples:**
- "Served 100+ customers daily"
- "Managed at least 15 concurrent projects"
- "Generated $500K+ in annual revenue"

### Percentage of Activity

**Format:** Calculate from known totals

**Example:**
- Company had 1000 customers → You managed 20% → "Managed 200 customer accounts"
- Team had 10 people → You supervised 4 → "Supervised 40% of team"

### Time-Based Calculation

**Format:** Work backwards from frequency

**Example:**
- Met with 5 clients/week × 50 weeks = "Consulted with 250+ clients annually"
- Processed 30 invoices/day × 250 days = "Processed 7,500+ invoices annually"

## Quantification Templates

### Before and After Template
```
"Improved [X] from [before number] to [after number], resulting in [Y]% improvement"

Example:
"Improved page load time from 8 seconds to 2 seconds, resulting in 75% reduction and 20% increase in user engagement"
```

### Scale Template
```
"[Verb] [number] [things], resulting in [impact]"

Example:
"Managed 25 concurrent projects worth $3M, delivering 95% on-time with zero budget overruns"
```

### Volume + Impact Template
```
"Processed [number] [items] per [time period], achieving [quality metric]"

Example:
"Resolved 50+ customer tickets daily, maintaining 98% satisfaction rating and 4-hour average response time"
```

### Comparison Template
```
"Ranked #[X] out of [Y] in [metric], [context]"

Example:
"Ranked #2 out of 45 sales representatives nationally, generating $3.2M in annual revenue"
```

## Common "I Have No Numbers" Situations

### Situation 1: "I was just one person on a team"

**Solution:** Focus on YOUR contribution

**Example:**
- "Part of team that launched product" →
- "Contributed 40% of front-end code for product launch reaching 100K users"

### Situation 2: "I don't have access to business metrics"

**Solution:** Quantify activities and inputs

**Example:**
- "Supported sales team" →
- "Created 50+ sales presentations and managed pipeline of 200+ prospects in Salesforce"

### Situation 3: "My job didn't produce measurable outcomes"

**Solution:** Measure the work itself

**Example:**
- "Wrote documentation" →
- "Produced 75-page technical documentation reducing new hire onboarding time by 2 weeks"

### Situation 4: "Results were confidential"

**Solution:** Use percentages or ranges

**Example:**
- "Increased revenue" →
- "Grew revenue by 40%+ year-over-year" or "Contributed to $X-$Y million growth"

### Situation 5: "I was entry-level with limited impact"

**Solution:** Quantify learning, throughput, accuracy

**Example:**
- "Entered data" →
- "Processed 200+ records daily with 99.5% accuracy rate, exceeding team average by 15%"

## Output Format

When quantifying a resume:

```markdown
# RESUME QUANTIFICATION

## Analysis Summary
**Bullets without numbers:** X
**Bullets with numbers:** Y
**Target:** 100% of bullets should have at least one metric

## Quantified Bullets

### Original Bullet #1:
"Managed customer accounts"

### Questions to Find Metrics:
- How many accounts? → [User answer: ~40]
- What was the revenue? → [User answer: ~$2M]
- What results did you achieve? → [User answer: retained most]

### Quantified Version:
"Managed portfolio of 40 enterprise accounts representing $2M ARR, achieving 95% retention rate"

### Metrics Added:
- Account count: 40
- Revenue: $2M ARR
- Retention: 95%

---

### Original Bullet #2:
[Continue for each bullet]

## Estimation Notes
- [Metric]: Estimated based on [reasoning]
- [Metric]: Conservative estimate using [method]

## Remaining Questions
- [Questions to ask user for missing information]
```

## Quantification Quality Checklist

For each bullet:
- ✅ Has at least ONE number
- ✅ Number is relevant (not just any number)
- ✅ Scale is clear (what does the number mean?)
- ✅ Estimation is conservative and defensible
- ✅ Number adds credibility, not confusion
- ✅ You can explain the number in an interview

## Numbers to Avoid

- ❌ Numbers that make you look bad
- ❌ Numbers you can't explain or defend
- ❌ Numbers that reveal confidential information
- ❌ Exaggerated or inflated numbers
- ❌ Numbers without context (e.g., "increased by 300%" without baseline)
- ❌ Too many numbers in one bullet (2-3 max)

## Key Principle

**Every bullet can be quantified.** If you think your work can't be measured, you haven't asked the right questions yet.

The goal isn't to have impressive numbers—it's to have SPECIFIC numbers that show the scope and impact of your work.
```

## File: `skills/resume-section-builder/SKILL.md`
```markdown
---
name: Resume Section Builder
description: Create targeted resume sections optimized for different experience levels and roles
---

# Resume Section Builder

## When to Use This Skill

Use this skill when the user:
- Needs help with specific resume sections
- Wants to optimize a particular part of their resume
- Is unsure what to include in a section
- Needs section-specific guidance
- Mentions: "resume sections", "skills section", "summary section", "experience section", "what to include"

## Core Capabilities

- Build targeted professional summaries
- Structure skills sections effectively
- Optimize experience sections
- Create education sections appropriately
- Add supplementary sections strategically
- Tailor sections for different career stages

## Professional Summary Section

### When to Include

**Include Summary If:**
- Career changers (need to explain transition)
- Senior professionals (distill long career)
- Returning to workforce (address gaps)
- Highly specialized role (emphasize fit)

**Skip Summary If:**
- Entry level with limited experience
- Straightforward career progression
- Space is at a premium

### Summary Framework

**Formula:** [Title/Identity] + [Years/Experience] + [Key Skills] + [Value Proposition]

### By Career Stage

**Entry Level:**
```
Recent Computer Science graduate from UC Berkeley with internship experience in full-stack development. Skilled in Python, React, and AWS. Seeking to leverage academic projects in machine learning and user-facing application development in a software engineering role.
```

**Mid-Career:**
```
Product Manager with 6 years driving B2B SaaS products from concept to scale. Track record of launching products that generated $10M+ ARR through data-driven roadmap prioritization and cross-functional leadership. Expert in API products, developer tools, and enterprise sales motions.
```

**Senior/Executive:**
```
Technology executive with 15+ years building and scaling engineering organizations from 50 to 500+ across global markets. Proven success leading digital transformation initiatives, M&A integration, and platform modernization. P&L ownership of $100M+ with track record of 40%+ efficiency improvements.
```

**Career Changer:**
```
Sales professional transitioning to Customer Success, bringing 5 years of consultative selling experience and proven ability to build lasting client relationships. Skilled in needs assessment, solution design, and stakeholder management. Seeking to apply relationship-building expertise to drive customer retention and expansion.
```

### Summary Don'ts

- ❌ "Seeking a challenging position..."
- ❌ "Hard-working team player..."
- ❌ "Results-oriented professional..."
- ❌ Third person ("John is a...")
- ❌ Objectives (what you want vs. what you offer)

## Skills Section

### Organization Options

**Option 1: Simple List**
```
SKILLS
Python, JavaScript, SQL, React, Node.js, AWS, Docker, Git, Agile, JIRA
```
Best for: ATS optimization, space constraints

**Option 2: Categorized**
```
TECHNICAL SKILLS
Languages: Python, JavaScript, TypeScript, SQL
Frameworks: React, Node.js, Django, FastAPI
Cloud: AWS (EC2, S3, Lambda), GCP, Docker, Kubernetes
Tools: Git, JIRA, Confluence, Datadog
```
Best for: Technical roles, extensive skill sets

**Option 3: Proficiency Levels** (use carefully)
```
SKILLS
Expert: Python, SQL, Product Management
Advanced: AWS, Data Analysis, Stakeholder Management
Proficient: Machine Learning, Figma, Financial Modeling
```
Best for: Roles requiring specific proficiency, honest representation

### What to Include

**Technical/Hard Skills:**
- Programming languages
- Software and tools
- Methodologies (Agile, Lean)
- Platforms (Salesforce, SAP)
- Certifications

**Functional Skills:**
- Project management
- Financial analysis
- Data analysis
- Market research

**Industry Knowledge:**
- Domain expertise
- Regulatory knowledge
- Industry certifications

### What to Exclude

- ❌ Microsoft Office (assumed)
- ❌ "Basic" skills
- ❌ Skills you can't discuss in interview
- ❌ Soft skills (show, don't list)
- ❌ Outdated technologies

## Experience Section

### Standard Format

```
COMPANY NAME | City, State
Job Title | Start Date - End Date

• Achievement bullet with metric and impact
• Achievement bullet with metric and impact
• Achievement bullet with metric and impact
```

### Bullet Guidelines by Career Stage

**Entry Level (0-2 years):**
- 3-5 bullets per role
- Include relevant projects
- Quantify where possible
- Show initiative and learning

**Mid-Career (3-10 years):**
- 4-6 bullets for recent roles
- 2-3 bullets for older roles
- Focus on achievements over duties
- Strong metrics throughout

**Senior (10+ years):**
- 5-6 bullets for recent roles
- 2-3 bullets for older roles
- Emphasize leadership and strategy
- Show increasing scope

### Handling Different Situations

**Multiple Roles at Same Company:**
```
COMPANY NAME | City, State
Senior Manager | 2021 - Present
• [Bullets for current role]

Manager | 2019 - 2021
• [Bullets for previous role]

Analyst | 2017 - 2019
• [Bullets for earliest role]
```

**Short Tenure:**
- Include if relevant experience
- Frame around project or achievement
- Don't apologize or explain in resume

**Contract/Freelance:**
```
Freelance Product Consultant | 2022 - Present
Clients include: Company A, Company B, Company C
• [Achievement with Client A]
• [Achievement with Client B]
```

## Education Section

### Standard Format

```
EDUCATION

Bachelor of Science in Computer Science
University of California, Berkeley | 2020
GPA: 3.8/4.0 | Honors: Magna Cum Laude
```

### What to Include by Career Stage

**Entry Level:**
- Degree, major, school, year
- GPA (if 3.5+)
- Honors and awards
- Relevant coursework
- Academic projects
- Study abroad

**Mid-Career:**
- Degree, major, school, year
- GPA only if exceptional
- Skip coursework (replaced by experience)

**Senior:**
- Degree, school
- May skip year (age discrimination)
- Professional development more relevant

### Advanced Degrees

```
MBA, Finance & Strategy
Harvard Business School | 2022
• Leadership Fellow
• Relevant coursework: Corporate Finance, M&A Strategy

M.S. in Computer Science
Stanford University | 2018
• Specialization: Artificial Intelligence
• Thesis: "Title of Thesis"
```

### Certifications

```
CERTIFICATIONS
AWS Solutions Architect Associate | Amazon Web Services | 2023
PMP (Project Management Professional) | PMI | 2022
Google Analytics Certified | Google | 2023
```

## Additional Sections

### When to Include Each

**Projects Section:**
- Entry level with limited work experience
- Career changers showing new skills
- Technical roles with personal projects

**Volunteer Section:**
- Relevant volunteer experience
- Leadership roles
- Fills employment gaps meaningfully

**Languages:**
- If relevant to role/company
- List proficiency levels accurately
- Only if beyond basic conversational

**Publications/Patents:**
- Academic positions
- Research roles
- Technical thought leadership

**Awards/Recognition:**
- Significant industry awards
- Company-wide recognition
- Relevant honors

### Format Examples

**Projects:**
```
PROJECTS
E-commerce Platform | React, Node.js, PostgreSQL | github.com/user/project
• Built full-stack marketplace with 500+ active users
• Implemented payment processing with Stripe integration
```

**Volunteer:**
```
VOLUNTEER EXPERIENCE
Board Member | Local Nonprofit | 2021 - Present
• Led fundraising committee, increasing annual donations by 40%
```

**Languages:**
```
LANGUAGES
English (Native) | Spanish (Professional) | Mandarin (Conversational)
```

## Section Order by Role Type

### Standard Order
1. Contact
2. Summary (optional)
3. Skills
4. Experience
5. Education
6. Additional

### Technical Roles
1. Contact
2. Skills (prioritized)
3. Experience
4. Projects
5. Education
6. Certifications

### Recent Graduate
1. Contact
2. Education (prioritized)
3. Skills
4. Experience/Internships
5. Projects
6. Activities

### Executive
1. Contact
2. Executive Summary
3. Career Highlights
4. Experience
5. Board Roles
6. Education

### Career Changer
1. Contact
2. Summary (explaining transition)
3. Skills (transferable)
4. Experience (reframed)
5. Bridge Experience
6. Education

## Output Format

When building resume sections:

```markdown
# RESUME SECTION RECOMMENDATIONS

## For: [User's situation/role]

### Recommended Section Order
1. [Section] - [Why]
2. [Section] - [Why]
...

### Section Details

#### Professional Summary
**Recommendation:** [Include/Skip]
**Draft:**
[Written summary if recommended]

#### Skills Section
**Format:** [Simple/Categorized/Proficiency]
**Content:**
[Organized skills list]

#### Experience Section
**Format:** [Standard/Functional/Hybrid]
**Bullets per Role:**
- Recent: [X] bullets
- Older: [X] bullets

#### Education Section
**Include:**
- [Items to include]
**Exclude:**
- [Items to exclude]

#### Additional Sections
**Recommended:** [Section name] because [reason]
**Skip:** [Section name] because [reason]
```

## Section-Building Checklist

- ✅ Section order optimized for role
- ✅ Summary is concise and targeted (if included)
- ✅ Skills are relevant and organized
- ✅ Experience bullets are achievement-focused
- ✅ Education appropriate for career stage
- ✅ Additional sections add value (not filler)
- ✅ Consistent formatting throughout
- ✅ All sections support the target role
- ✅ Nothing irrelevant or outdated included
- ✅ Total length appropriate (1-2 pages)
```

## File: `skills/resume-tailor/SKILL.md`
```markdown
---
name: Resume Tailor
description: Customize resume for specific job postings while maintaining truthfulness
---

# Resume Tailor

## When to Use This Skill

Use this skill when the user wants to:
- Customize their resume for a specific job posting
- Adjust their resume to match job requirements
- Create a targeted version of their resume
- Mentions: "tailor resume", "customize resume", "target role", "specific job", "match job description"

Use AFTER job-description-analyzer to know what to emphasize.

## Core Capabilities

- Reorder experience sections by relevance to target role
- Adjust professional summary for specific position
- Add missing keywords from job description
- Modify bullet points to match job requirements
- Maintain authenticity while optimizing match
- Create multiple targeted resume versions

## The Tailoring Philosophy

**Key Principle:** You're not lying or fabricating - you're HIGHLIGHTING the most relevant parts of your true experience.

Think of your full experience as a library of achievements. Tailoring means selecting the books that best fit what each employer is looking for.

## Tailoring Process

### Step 1: Analyze the Job (Use Job Description Analyzer First)
- Identify required skills and keywords
- Note the company's priorities
- Understand the role's primary responsibilities

### Step 2: Audit Your Resume
For each section, ask:
- Does this support my candidacy for THIS specific role?
- Is there a better way to phrase this for THIS job?
- Should this be higher or lower in priority?

### Step 3: Make Strategic Adjustments

**Professional Summary:** Rewrite to mirror the job's key requirements

**Skills Section:** Reorder to put most relevant skills first, add missing keywords

**Experience:** 
- Reorder jobs if a less recent role is more relevant
- Swap bullet points to lead with most relevant achievements
- Add keywords naturally into existing bullets

**Education:** Highlight relevant coursework, certifications

## Section-by-Section Tailoring Guide

### Professional Summary

This is your "elevator pitch" - customize for each application.

**Generic Summary (AVOID):**
```
Results-driven professional with 5 years of experience in business operations. Strong analytical and communication skills. Looking for a challenging opportunity to grow.
```

**Tailored for Operations Manager Role:**
```
Operations Manager with 5 years optimizing supply chain processes and reducing costs by 25%. Expertise in Lean Six Sigma, vendor management, and cross-functional team leadership. Track record of improving operational efficiency while maintaining quality standards.
```

**Tailored for Project Manager Role (Same Person):**
```
Project Manager with 5 years leading cross-functional initiatives from concept to delivery. PMP-certified with expertise in Agile methodology, stakeholder management, and budget oversight. Track record of on-time, under-budget project delivery across $10M+ portfolios.
```

### Skills Section Reordering

**Job Description Emphasizes:** Data analysis, SQL, Python, stakeholder communication

**Before (Generic Order):**
```
Skills: Microsoft Office, Communication, Project Management, Python, SQL, Data Visualization, Leadership
```

**After (Tailored Order):**
```
Skills: SQL, Python, Data Analysis, Data Visualization, Stakeholder Communication, Project Management, Microsoft Office
```

### Experience Section

**Strategy 1: Reorder Jobs**

If your most recent job is less relevant than a previous role:

**Before:**
1. Marketing Coordinator (current, but applying for data role)
2. Data Analyst (previous, highly relevant)

**After:**
1. Data Analyst (labeled with dates, moved up)
2. Marketing Coordinator (still included, but secondary)

**Strategy 2: Swap Bullet Order**

Lead with bullets most relevant to the target role.

**Applying for Management Role - Lead with:**
- "Led team of 12..."
- "Managed budget of $2M..."

**Applying for Technical Role - Lead with:**
- "Developed automated system..."
- "Analyzed 500K+ data points..."

**Strategy 3: Adjust Bullet Language**

Incorporate job description keywords while staying truthful.

**Job Description Says:** "stakeholder management"
**Your Bullet Says:** "Worked with various teams"
**Tailored Version:** "Managed stakeholder relationships across 5 departments, ensuring alignment on project priorities"

## Tailoring Templates

### For Each Job Application, Create:

```markdown
## RESUME TAILORING PLAN

**Target Position:** [Job Title]
**Company:** [Company Name]
**Match Score:** [From JD Analyzer]

### Summary Customization
**Current:** [Your current summary]
**Tailored:** [Rewritten for this role]

### Skills Reordering
**Current Order:** [List]
**New Order:** [Reordered list with added keywords]
**Keywords Added:** [New skills from JD]

### Experience Adjustments

**Job 1: [Title]**
- Bullet to emphasize: [Which bullet to lead with]
- Keyword to add: [What phrase to incorporate]
- Bullet to de-emphasize: [Move down or remove if space needed]

**Job 2: [Title]**
[Same structure]

### Other Adjustments
- Education: [Any relevant coursework to add]
- Certifications: [Any to highlight]
- Projects: [Relevant projects to include]
```

## Common Tailoring Scenarios

### Scenario 1: Technical Role at Non-Tech Company

**Challenge:** They want technical skills but also business acumen

**Strategy:**
- Lead with technical achievements
- Include business impact in every technical bullet
- Add "translated technical concepts for business stakeholders"

### Scenario 2: Management Role (But You've Done Both IC and Management)

**Challenge:** Show leadership without abandoning technical credibility

**Strategy:**
- Summary: Emphasize leadership
- Experience: Lead with team management bullets
- Keep some technical bullets to show you understand the work

### Scenario 3: Startup (But You've Worked at Big Companies)

**Challenge:** Show you can thrive in ambiguity and wear many hats

**Strategy:**
- Highlight cross-functional work
- Emphasize initiative and self-starting
- Show scrappy, creative problem-solving
- De-emphasize rigid processes and large team structures

### Scenario 4: Big Company (But You've Worked at Startups)

**Challenge:** Show you can work within structure and at scale

**Strategy:**
- Emphasize process improvement
- Highlight work that scaled
- Show collaboration across teams
- Add metrics that show impact at scale

## Keyword Integration Rules

### DO:
- Add keywords that truthfully describe your work
- Use exact phrasing from job description when accurate
- Place keywords naturally in context
- Include keywords in multiple locations (summary, skills, experience)

### DON'T:
- Add skills you don't actually have
- Keyword stuff (repeating same term 10x)
- Create a different meaning than your actual experience
- Sacrifice readability for keyword density

## Truth vs. Tailoring Line

**Acceptable Tailoring:**
- Reordering true information
- Emphasizing relevant experience
- Using industry-standard terminology
- Adding context to vague statements
- Matching language style to job description

**Unacceptable (Lying):**
- Adding skills you don't have
- Changing numbers or metrics
- Creating fake experiences
- Claiming titles you didn't hold
- Stating certifications you don't have

## Version Management

### Maintain a Master Resume
- Keep ONE complete document with ALL experiences
- Include every bullet you've ever written
- This is your "source of truth"

### Create Targeted Versions
- Name files clearly: "JohnSmith_Resume_ProductManager_TechCorp.pdf"
- Track which version went to which company
- Save tailoring notes for interview prep

### Version Naming Convention
```
[LastName]_Resume_[TargetRole]_[Company]_[Date].pdf

Examples:
- Smith_Resume_PM_Google_Jan2024.pdf
- Smith_Resume_DataAnalyst_Meta_Jan2024.pdf
- Smith_Resume_General_Master.docx (your master file)
```

## Quick Tailoring Checklist

Before submitting any resume:

1. ✅ Summary mentions the exact job title/function
2. ✅ Top 5 skills match job description's top 5 requirements
3. ✅ Most relevant experience is positioned first
4. ✅ Each job's top bullet addresses job's key requirement
5. ✅ Keywords from JD appear naturally throughout
6. ✅ Company/industry terminology is used correctly
7. ✅ All claims are truthful
8. ✅ File is named appropriately
9. ✅ ATS formatting maintained
10. ✅ Saved for interview prep reference

## Output Format

When tailoring a resume, provide:

```markdown
# TAILORED RESUME CHANGES

## Target: [Job Title] at [Company]

### Professional Summary
**Before:** [Original]
**After:** [Tailored version]
**Keywords Added:** [List]

### Skills Section
**New Order:** [Reordered list]
**Added:** [New keywords]
**Removed:** [If any, for space]

### Experience Changes

**[Company Name] - [Title]**
- Move bullet X to position 1
- Modify bullet Y: [Before → After]
- Add keyword "[phrase]" to bullet Z

[Repeat for each relevant job]

### Overall Changes Summary
- Keywords added: X
- Bullets modified: Y
- Sections reordered: Yes/No
- Estimated new match score: Z%
```

## Implementation Notes

- Always start with the job description analyzer
- Keep tailoring changes documented for interview prep
- Maintain master resume as source of truth
- Never sacrifice ATS compatibility for tailoring
- Test keyword match after tailoring
```

## File: `skills/resume-version-manager/SKILL.md`
```markdown
---
name: Resume Version Manager
description: Track different resume versions, maintain master resume, manage tailored versions
---

# Resume Version Manager

## When to Use This Skill

Use this skill when the user:
- Has multiple resume versions to manage
- Needs to track tailored resumes
- Wants to maintain a master resume
- Is applying to many different roles
- Mentions: "resume versions", "master resume", "different versions", "track resumes", "which resume"

## Core Capabilities

- Create and maintain master resume document
- Track tailored resume versions
- Organize resume versions by role/industry
- Maintain consistent source of truth
- Streamline resume updates
- Prevent version confusion

## The Version Management Problem

**Common Pain Points:**
- "Which version did I send to Company X?"
- "Where's my most recent resume?"
- "I have 15 resume files and don't know which is best"
- "I forgot to update my resume after that project"
- "I keep tailoring from different base versions"

**The Solution:**
A systematic approach with:
1. One master resume (source of truth)
2. Organized tailored versions
3. Clear naming conventions
4. Update workflow

## Master Resume Concept

### What is a Master Resume?

A comprehensive document containing:
- ALL your experiences (not just recent)
- ALL bullet points you've ever written
- Every achievement, project, skill
- Full details (even if they won't fit on one page)

**Purpose:** Source of truth to pull from when tailoring

### Master Resume Structure

```markdown
# MASTER RESUME - [YOUR NAME]
Last Updated: [Date]

## CONTACT INFORMATION
[Full contact details]

## PROFESSIONAL SUMMARY VERSIONS
[Summary for Role Type A]
[Summary for Role Type B]
[Summary for Role Type C]

## ALL SKILLS
### Technical Skills
[Complete list by category]

### Soft Skills
[Complete list]

### Industry Knowledge
[All domains]

## PROFESSIONAL EXPERIENCE

### Company Name | Title | Dates

**All Bullets (choose best for each application):**
• Bullet 1 (leadership focused)
• Bullet 2 (technical focused)
• Bullet 3 (results focused)
• Bullet 4 (collaboration focused)
• Bullet 5 (additional achievement)
• Bullet 6 (additional achievement)

**Keywords this experience covers:**
[List of keywords this job demonstrates]

### Previous Company | Title | Dates
[Same format...]

## EDUCATION
[Complete education history]

## CERTIFICATIONS
[All certifications ever earned]

## PROJECTS
[All notable projects]

## VOLUNTEER / ADDITIONAL
[All other relevant experience]
```

## File Organization System

### Folder Structure

```
Resume/
├── Master/
│   └── LastName_Master_Resume.docx
├── Tailored/
│   ├── ProductManagement/
│   │   ├── LastName_PM_Google_Jan2024.pdf
│   │   └── LastName_PM_Meta_Jan2024.pdf
│   ├── Engineering/
│   │   ├── LastName_SWE_Startup_Feb2024.pdf
│   │   └── LastName_SWE_Enterprise_Feb2024.pdf
│   └── General/
│       └── LastName_General_Resume.pdf
├── CoverLetters/
│   ├── Google_PM_CoverLetter.docx
│   └── Meta_PM_CoverLetter.docx
└── Applications/
    └── ApplicationTracker.xlsx
```

### File Naming Convention

**Pattern:**
`[LastName]_[Role/Type]_[Company]_[Date].pdf`

**Examples:**
- `Smith_ProductManager_Google_Jan2024.pdf`
- `Smith_SWE_Stripe_Feb2024.pdf`
- `Smith_DataScience_General_2024.pdf`
- `Smith_Master_Resume_v3.docx`

## Version Categories

### By Target Role

**Product Management:**
- Emphasizes: Strategy, roadmap, metrics, stakeholders
- Skills highlight: Product tools, analytics, user research

**Software Engineering:**
- Emphasizes: Technical projects, systems, code
- Skills highlight: Languages, frameworks, tools

**Data Science:**
- Emphasizes: Analysis, ML, statistical methods
- Skills highlight: Python, SQL, ML libraries

### By Industry

**Tech/Startup:**
- Emphasizes: Innovation, growth, scrappiness
- Tone: Modern, direct, achievement-focused

**Enterprise/Corporate:**
- Emphasizes: Scale, process, collaboration
- Tone: Professional, structured, comprehensive

**Finance:**
- Emphasizes: Analysis, compliance, accuracy
- Tone: Conservative, precise, credentialed

### By Seniority Level

**Individual Contributor:**
- Focus on execution and technical skills
- Detailed project descriptions
- Technical accomplishments

**Manager:**
- Team leadership and development
- Cross-functional collaboration
- Business impact metrics

**Executive:**
- Strategic leadership
- P&L responsibility
- Organizational transformation

## Application Tracking

### Simple Tracker Spreadsheet

```
| Company | Role | Version Used | Date Applied | Status | Notes |
|---------|------|--------------|--------------|--------|-------|
| Google | PM | PM_Google_Jan | 1/15/24 | Interview | 2nd round 2/1 |
| Meta | PM | PM_Meta_Jan | 1/18/24 | Applied | Referral from John |
| Startup | PM | PM_General | 1/20/24 | Rejected | Too senior |
```

### Information to Track

- Company name
- Job title
- Resume version used
- Cover letter version used
- Application date
- Application method (portal, referral, direct)
- Current status
- Follow-up dates
- Notes and contacts

## Update Workflow

### When to Update Master Resume

**Immediately Update For:**
- New job or promotion
- Completed major project
- New skills or certifications
- Significant achievements
- Awards or recognition

**Quarterly Review:**
- Add recent accomplishments
- Update metrics with new data
- Refresh skills section
- Remove outdated information

### Master to Tailored Workflow

```
1. Start with Master Resume
   ↓
2. Copy to new file (don't edit master)
   ↓
3. Analyze job description
   ↓
4. Select relevant bullets from master
   ↓
5. Choose appropriate summary version
   ↓
6. Reorder skills for relevance
   ↓
7. Add job-specific keywords
   ↓
8. Trim to appropriate length
   ↓
9. Save with proper naming convention
   ↓
10. Update application tracker
```

## Common Scenarios

### Scenario 1: Applying to Similar Roles

**Strategy:**
- Create one well-tailored version for the role type
- Make minor adjustments for each company
- Track which slight variation went where

### Scenario 2: Applying to Different Role Types

**Strategy:**
- Create separate base versions for each role type
- Maintain clear folder organization
- Each version pulls from same master

### Scenario 3: Rapid Application Volume

**Strategy:**
- Create 2-3 strong category versions
- Use "general" versions for quick applications
- Reserve deep tailoring for top choices

### Scenario 4: Career Transition

**Strategy:**
- Create transition-focused version
- Emphasize transferable skills
- Maintain original industry version as backup

## Version Control Best Practices

### DO:
- ✅ Always work from master as source
- ✅ Use consistent naming conventions
- ✅ Track which version went where
- ✅ Keep master updated
- ✅ Date your files
- ✅ Backup to cloud storage

### DON'T:
- ❌ Edit master directly for applications
- ❌ Use vague names like "resume_final_v2"
- ❌ Forget which version you sent
- ❌ Let master get out of date
- ❌ Have multiple "master" files
- ❌ Delete old versions (archive instead)

## Output Format

When managing resume versions:

```markdown
# RESUME VERSION MANAGEMENT

## Master Resume Status
**Last Updated:** [Date]
**Location:** [File path]
**Total Experience Entries:** [X]
**Total Bullet Points Available:** [X]

## Active Versions

### Role Type: Product Management
**Base Version:** PM_General_2024.docx
**Tailored Versions:**
| Company | File Name | Date Created | Status |
|---------|-----------|--------------|--------|
| Google | PM_Google_Jan24 | 1/15/24 | Submitted |
| Meta | PM_Meta_Jan24 | 1/18/24 | Submitted |

### Role Type: Engineering
[Same structure]

## Update Queue
- [ ] Add Q4 project results to master
- [ ] Update skills with new certification
- [ ] Archive versions older than 6 months

## Recommended Actions
1. [Action 1]
2. [Action 2]
```

## Version Management Checklist

- ✅ Master resume exists and is current
- ✅ Folder structure is organized
- ✅ Naming convention is consistent
- ✅ Application tracker is maintained
- ✅ Know which version sent to each company
- ✅ All versions pull from same master
- ✅ Backup system in place
- ✅ Old versions archived (not deleted)
- ✅ Update workflow is established
- ✅ Regular master resume reviews scheduled
```

## File: `skills/salary-negotiation-prep/SKILL.md`
```markdown
---
name: Salary Negotiation Prep
description: Research market rates, build negotiation strategy, and create counter-offer scripts
---

# Salary Negotiation Prep

## When to Use This Skill

Use this skill when the user wants to:
- Negotiate a job offer or salary
- Research market rates for their role
- Create a counter-offer strategy
- Understand total compensation packages
- Mentions: "salary negotiation", "negotiate offer", "counter offer", "compensation", "how much should I ask for"

## Core Capabilities

- Research and validate market compensation
- Build negotiation strategy and scripts
- Calculate total compensation (not just base salary)
- Prepare counter-offer responses
- Identify negotiation leverage points
- Navigate difficult salary conversations

## The Negotiation Mindset

**Key Principles:**
1. Negotiation is expected - companies budget for it
2. 84% of employers expect candidates to negotiate
3. Not negotiating leaves $500K-$1M on the table over a career
4. The goal is win-win, not adversarial

**What You're Really Negotiating:**
- Base salary
- Signing bonus
- Annual bonus/commission
- Equity (stock options, RSUs)
- Benefits (401k match, insurance)
- Perks (vacation, remote work, professional development)
- Start date
- Title

## Research Phase

### Step 1: Determine Market Rate

**Sources to Check:**
- Levels.fyi (best for tech)
- Glassdoor (general, take with grain of salt)
- LinkedIn Salary
- Blind (anonymous reports)
- PayScale
- Salary.com
- H1B salary data (publicly available)

**Build a Range:**
```
Low (25th percentile): $XXX,XXX
Target (50th percentile): $XXX,XXX  
High (75th percentile): $XXX,XXX
Stretch (90th percentile): $XXX,XXX
```

### Step 2: Know Your Value

**Factors That Increase Your Worth:**
- Years of relevant experience
- Specialized/rare skills
- Track record of results
- In-demand certifications
- Current competing offers
- Referral from employee
- Market demand in your field

**Factors That May Limit:**
- Entry level or career change
- Less experience than ideal candidate
- Gaps in required skills
- Location arbitrage (lower cost of living)

### Step 3: Calculate Total Compensation

**Total Comp = Base + Bonus + Equity + Benefits**

```
EXAMPLE:
Base Salary: $150,000
Target Bonus (15%): $22,500
RSU Grant (4-year): $200,000 ($50,000/year)
401k Match (4%): $6,000
Benefits Value: ~$15,000

Total Annual Comp: $243,500
```

**Common Equity Terms:**
- **RSUs:** Restricted Stock Units (real shares, taxed when vesting)
- **Options:** Right to buy at strike price (value = current price - strike price)
- **Vesting:** Typically 4-year with 1-year cliff
- **Refresh grants:** Annual additional equity grants

## Negotiation Strategy

### When to Negotiate

**Best Time:** After you have a written offer, before you sign

**Timeline:**
1. Receive verbal offer → Express enthusiasm, ask for written offer
2. Receive written offer → Thank them, ask for time to review
3. Research and prepare → 24-48 hours
4. Counter with ask → Email or call
5. Discussion/back and forth → May take several rounds
6. Final agreement → Get in writing

### The Counter-Offer Framework

**Structure:**
1. Express enthusiasm
2. Reinforce your value
3. Make specific ask
4. Provide justification
5. Open discussion

### Counter-Offer Email Template

```
Subject: [Your Name] - Offer Discussion

Hi [Recruiter/Hiring Manager],

Thank you so much for the offer to join [Company] as [Title]. I'm very excited about the opportunity to [specific thing about the role]. After speaking with the team and learning more about [something specific], I'm confident this is the right fit.

I've had time to review the offer details and wanted to discuss the compensation. Based on my research of the market and my [X years of experience / specific valuable skill / competing offer], I was hoping we could discuss a base salary of $[Your Ask] rather than $[Their Offer].

[Optional: Add specific justification - e.g., "I've seen similar roles at [comparable companies] in this range" or "Given the scope of the role and my track record of [specific achievement], I believe this reflects my value."]

I'm flexible and open to discussing other elements of the package as well. Would you have time for a quick call to discuss?

Thank you again for this opportunity. I'm looking forward to finding a package that works for both of us.

Best,
[Your Name]
```

### Counter-Offer Call Script

```
"Hi [Name], thanks for making time. I'm really excited about this opportunity - [genuine specific reason].

I've reviewed the offer and want to discuss compensation. Based on my market research and [X years experience / key accomplishment / competing offer], I was hoping for a base salary closer to $[Amount].

Is there flexibility there?"

[LISTEN - Let them respond]

[If they push back:]
"I understand there are constraints. I'm flexible - could we look at other elements like signing bonus, equity, or [other element] to bridge the gap?"

[If they say they'll need to check:]
"That's totally fair. When would be a good time to reconnect?"
```

## Common Negotiation Scenarios

### Scenario 1: First Offer Is Low

**Approach:**
- Don't accept immediately
- Express enthusiasm for role
- Counter with research-backed number
- Be prepared to justify

**Script:**
```
"I'm thrilled about the opportunity. The base salary is lower than I expected based on my research. For this role and market, I was expecting something in the $X-$Y range. Is there room to move closer to $X?"
```

### Scenario 2: They Ask Your Salary Expectations First

**Deflection Strategy:**
```
"I'm flexible and focused on finding the right fit. What's the range you've budgeted for this role?"
```

**If Pressed:**
```
"Based on my research for this role and market, I'm looking at $X-$Y, but I'm open to discussing the full compensation picture."
```

### Scenario 3: They Won't Budge on Base

**Alternatives to Negotiate:**
- Signing bonus (one-time, easier to approve)
- Additional equity
- Earlier performance review (sooner raise)
- More vacation days
- Remote work flexibility
- Professional development budget
- Title upgrade
- Relocation assistance
- Start date

**Script:**
```
"I understand the base salary is firm. Could we discuss a signing bonus to help bridge the gap? Something in the range of $X would make this work."
```

### Scenario 4: You Have Competing Offers

**Use Carefully:**
- Only mention if true
- Don't make it a threat
- Frame as problem-solving

**Script:**
```
"I want to be transparent - I'm also in discussions with [another company/a few other companies]. They're offering $X. [Your Company] is my first choice because [genuine reason], but I want to make sure the compensation is competitive."
```

### Scenario 5: They Ask About Current Salary

**In Many States, This Question Is Illegal**

**If Asked (and legal):**
```
"I'd prefer to focus on the value I'd bring to this role and what the market rate is. What's the range you've budgeted?"
```

**Or Redirect:**
```
"My current compensation isn't really comparable since [different location/role/structure]. Based on my research for this role, I'm targeting $X-$Y."
```

## Negotiation Tactics

### Do's:
- ✅ Always negotiate (respectfully)
- ✅ Get the offer in writing before negotiating
- ✅ Research thoroughly
- ✅ Be specific with numbers
- ✅ Express genuine enthusiasm
- ✅ Give them a way to say yes
- ✅ Consider total compensation
- ✅ Be patient - process takes time
- ✅ Get final agreement in writing

### Don'ts:
- ❌ Accept on the spot
- ❌ Give a salary history (if not required by law)
- ❌ Make ultimatums
- ❌ Lie about competing offers
- ❌ Be rude or aggressive
- ❌ Negotiate just for the sake of it
- ❌ Accept verbal promises without writing
- ❌ Burn bridges if it doesn't work out

## Total Compensation Comparison

### Side-by-Side Analysis

```markdown
## OFFER COMPARISON

| Component | Company A | Company B | Notes |
|-----------|-----------|-----------|-------|
| Base Salary | $150,000 | $140,000 | A wins |
| Target Bonus | 15% ($22,500) | 20% ($28,000) | B wins |
| Signing Bonus | $20,000 | $10,000 | A wins |
| Equity (annual) | $50,000 | $75,000 | B wins |
| 401k Match | 4% ($6,000) | 6% ($8,400) | B wins |
| Benefits | Standard | Premium | B wins |
| WFH | Hybrid (3 days) | Full remote | B wins |
| Vacation | 3 weeks | Unlimited | Depends |

**Year 1 Total Comp:**
Company A: $248,500
Company B: $261,400

**Analysis:** Company B is higher total comp, but Company A has higher base which affects future raises and mortgage qualification.
```

## Negotiation Timeline Template

```
Day 1: Receive offer
- Thank them, express enthusiasm
- Ask for offer in writing
- Ask deadline for response

Day 1-3: Research
- Verify market rate
- Calculate total comp
- Identify priorities
- Prepare counter-offer

Day 3-5: Counter
- Send counter-offer email or schedule call
- Be specific about ask

Day 5-10: Discussion
- May require several rounds
- Be patient but responsive
- Stay professional and positive

Day 10+: Resolution
- Agree on terms
- Get everything in writing
- Sign and celebrate!
```

## Output Format

When preparing salary negotiation:

```markdown
# SALARY NEGOTIATION STRATEGY

## Market Research Summary
**Role:** [Title]
**Location:** [City/Remote]
**Experience Level:** [Years]

**Market Range:**
- 25th percentile: $XXX,XXX
- 50th percentile: $XXX,XXX (target)
- 75th percentile: $XXX,XXX
- 90th percentile: $XXX,XXX (stretch)

**Sources:** [List sources used]

## Their Offer
| Component | Amount |
|-----------|--------|
| Base | $XXX,XXX |
| Bonus | X% |
| Equity | $XXX,XXX |
| Signing | $XXX |
| Total Year 1 | $XXX,XXX |

## Your Counter
| Component | Ask | Justification |
|-----------|-----|---------------|
| Base | $XXX,XXX | [Why] |
| Signing | $XXX | [Why] |
| [Other] | | |

## Counter-Offer Script
[Email template or call script customized for this situation]

## If They Push Back
**Plan B:** [Alternative elements to negotiate]
**Walk-away Point:** [Your minimum]

## Key Talking Points
1. [Your experience/value point]
2. [Market data point]
3. [Specific achievement]

## Questions to Clarify
- [Equity vesting schedule?]
- [Bonus guaranteed?]
- [Review cycle timeline?]
```

## Implementation Checklist

1. ✅ Research market rate from 3+ sources
2. ✅ Calculate total compensation (not just base)
3. ✅ Identify your priorities
4. ✅ Determine walk-away point
5. ✅ Prepare counter-offer with justification
6. ✅ Write or practice negotiation script
7. ✅ Plan for pushback scenarios
8. ✅ Get agreement in writing
9. ✅ Review final offer letter carefully
10. ✅ Sign and celebrate!
```

## File: `skills/tech-resume-optimizer/SKILL.md`
```markdown
---
name: Tech Resume Optimizer
description: Optimize resumes for software engineering, PM, and technical roles
---

# Tech Resume Optimizer

## When to Use This Skill

Use this skill when the user:
- Is applying for software engineering roles
- Wants to optimize a technical resume
- Needs help with developer/PM/technical job applications
- Mentions: "tech resume", "software engineer resume", "developer resume", "technical resume", "SWE resume", "PM resume"

## Core Capabilities

- Optimize resumes for technical roles (SWE, PM, Data, DevOps)
- Structure technical skills sections effectively
- Highlight projects and technical achievements
- Balance technical depth with business impact
- Format for both ATS and technical recruiters
- Include GitHub, portfolio, and technical links

## Tech Resume Philosophy

**What Tech Recruiters Look For:**
1. Relevant technical skills (languages, frameworks, tools)
2. Scale and impact (users, transactions, data size)
3. Problem-solving abilities
4. System design understanding
5. Collaborative abilities
6. Growth trajectory

## Tech Resume Structure

### Recommended Order

```
1. Contact Information (including GitHub, Portfolio)
2. Professional Summary (optional but helpful)
3. Technical Skills (critical for ATS)
4. Work Experience (with technical achievements)
5. Projects (especially for early career)
6. Education
7. Certifications (if relevant)
```

### Contact Section for Tech

```
John Developer
San Francisco, CA
john@email.com | (555) 123-4567
LinkedIn: linkedin.com/in/johndev
GitHub: github.com/johndev
Portfolio: johndev.io
```

**Include:**
- GitHub (required for SWE roles)
- Portfolio/personal website
- LinkedIn
- Tech blog (if you have one)

**Don't Include:**
- Address (city/state is enough)
- Photo
- Social media (unless relevant)

## Technical Skills Section

### Organization Strategies

**Option 1: By Category**
```
Languages: Python, JavaScript, TypeScript, Go, SQL
Frameworks: React, Node.js, Django, FastAPI
Databases: PostgreSQL, MongoDB, Redis, Elasticsearch
Cloud/Infrastructure: AWS (EC2, S3, Lambda, RDS), Docker, Kubernetes, Terraform
Tools: Git, JIRA, CI/CD, Datadog, Grafana
```

**Option 2: By Proficiency** (use carefully)
```
Expert: Python, React, PostgreSQL, AWS
Proficient: Go, TypeScript, MongoDB, Docker
Familiar: Rust, GraphQL, Kubernetes
```

**Option 3: Flat List** (ATS-friendly)
```
Skills: Python, JavaScript, TypeScript, React, Node.js, Django, PostgreSQL, MongoDB, AWS, Docker, Kubernetes, Git
```

### What to Include

**Languages:**
- List languages you can code in confidently
- Order by relevance to target role
- Include query languages (SQL, GraphQL)

**Frameworks/Libraries:**
- Web: React, Vue, Angular, Django, Flask, Express
- Data: Pandas, NumPy, TensorFlow, PyTorch
- Testing: Jest, Pytest, Selenium

**Databases:**
- Relational: PostgreSQL, MySQL, SQL Server
- NoSQL: MongoDB, DynamoDB, Cassandra
- Caching: Redis, Memcached

**Cloud/DevOps:**
- Cloud: AWS, GCP, Azure (specific services)
- Containers: Docker, Kubernetes
- CI/CD: Jenkins, GitHub Actions, CircleCI
- IaC: Terraform, CloudFormation

### What NOT to Include
- ❌ Microsoft Office (assumed)
- ❌ Operating systems (unless DevOps role)
- ❌ Outdated tech (unless specifically required)
- ❌ Skill bars or ratings (subjective and break ATS)
- ❌ Every technology you've touched once

## Experience Section for Tech Roles

### The Technical Bullet Formula

**[Action Verb] + [Technical What] + [Scale/Impact] + [Technology Used]**

**Examples:**

❌ **Weak Technical Bullet:**
```
- Worked on backend services
- Helped improve system performance
- Built features for the product
```

✅ **Strong Technical Bullet:**
```
- Architected microservices migration from monolith, reducing deployment time from 2 hours to 15 minutes and enabling independent team deployments
- Optimized PostgreSQL queries and implemented Redis caching, reducing API latency by 60% (from 500ms to 200ms) for 100K daily active users
- Built real-time notification system using WebSockets and AWS SNS, handling 1M+ messages daily with 99.9% delivery rate
```

### Technical Metrics to Include

**Scale:**
- Users: "serving 500K DAU"
- Requests: "handling 10K requests/second"
- Data: "processing 50TB daily"
- Uptime: "maintaining 99.99% availability"

**Performance:**
- Latency: "reduced from Xms to Yms"
- Speed: "improved by X%"
- Load time: "decreased by X seconds"

**Efficiency:**
- Cost: "reduced AWS costs by 40%"
- Time: "cut deployment time from X to Y"
- Resources: "reduced memory usage by X%"

**Business:**
- Revenue: "features drove $XM revenue"
- Conversion: "improved checkout by X%"
- Engagement: "increased DAU by X%"

### Role-Specific Bullet Examples

**Software Engineer:**
```
• Designed and implemented authentication service using OAuth 2.0 and JWT, securing 2M+ user accounts with zero security incidents
• Led migration to Kubernetes, achieving 99.99% uptime and reducing infrastructure costs by 35% ($200K annually)
• Mentored 3 junior engineers through code reviews and pair programming, improving team velocity by 25%
```

**Data Engineer:**
```
• Built data pipeline processing 100M+ events daily using Apache Kafka and Spark, reducing data latency from hours to minutes
• Designed data warehouse schema in Snowflake, enabling self-service analytics for 50+ business users
• Implemented data quality monitoring with Great Expectations, catching 95% of data issues before impacting downstream systems
```

**DevOps/SRE:**
```
• Implemented infrastructure as code using Terraform, reducing provisioning time from 2 days to 30 minutes
• Built monitoring and alerting system with Prometheus and Grafana, reducing MTTR from 4 hours to 30 minutes
• Automated deployment pipeline with GitHub Actions, enabling 50+ daily deployments with zero-downtime releases
```

**Product Manager (Technical):**
```
• Led API platform roadmap for developer tools used by 10K+ developers, driving 40% increase in API adoption
• Defined technical requirements for ML recommendation engine, resulting in 25% increase in user engagement
• Partnered with engineering to reduce technical debt by 30%, improving release velocity from bi-weekly to weekly
```

## Projects Section

**Critical for:**
- Junior engineers
- Career changers
- Bootcamp graduates
- Anyone with gaps

### Project Format

```
Project Name | Technologies | Link
• Description of what it does
• Technical highlights and challenges solved
• Scale or usage metrics if available
```

### Example Projects Section

```
PROJECTS

Distributed Task Queue | Python, Redis, Docker | github.com/user/taskqueue
• Built distributed task queue handling 10K+ jobs/hour with automatic retries and dead letter queue
• Implemented priority queuing and rate limiting for multi-tenant support

Real-time Chat App | React, Node.js, WebSocket, MongoDB | chatapp.demo.com
• Full-stack chat application supporting 100+ concurrent users with real-time messaging
• Implemented end-to-end encryption and message persistence

ML Price Predictor | Python, TensorFlow, FastAPI | github.com/user/predictor
• Trained regression model on 1M+ data points achieving 92% accuracy for price prediction
• Deployed as REST API with automatic model retraining pipeline
```

### What Makes a Good Project

**Do Include:**
- Projects with real users
- Open source contributions
- Technical blog posts
- Hackathon projects (especially winners)
- Complex personal projects

**Don't Include:**
- Tutorial follow-alongs
- Trivial to-do apps
- Incomplete projects
- Coursework (unless exceptional)

## Education Section for Tech

### Standard Format
```
B.S. Computer Science | Stanford University | 2020
GPA: 3.8/4.0 (include if above 3.5)
Relevant Coursework: Distributed Systems, Machine Learning, Database Systems
```

### For Bootcamp Graduates
```
Software Engineering Certificate | App Academy | 2023
- 1000+ hour immersive program
- Full-stack JavaScript, React, Node.js, PostgreSQL

B.A. Economics | UCLA | 2020
```

### For Self-Taught Engineers
```
Professional Certifications:
- AWS Solutions Architect Associate | 2023
- MongoDB Certified Developer | 2023

Relevant Education:
- MIT OpenCourseWare: Algorithms, Data Structures
- Coursera: Machine Learning Specialization (Stanford)
```

## Tech-Specific Tips

### GitHub Profile Optimization

**Make sure your GitHub shows:**
- Pinned repositories (your best 6)
- Green contribution graph (activity)
- README for profile
- Complete project READMEs

**Project READMEs should include:**
- What the project does
- Technologies used
- How to run it
- Screenshots/demos
- Your contributions (for collaborative projects)

### Dealing with Tech Stacks

**If you match their stack:**
- Lead with those technologies
- Quantify your experience with them

**If you don't match exactly:**
- Emphasize transferable skills
- Show learning ability
- Highlight similar technologies
- Example: "Django" → "Extensive Python web framework experience (Django); quick to ramp on new frameworks"

### Technical Interviews Prep Note

Tech resumes should support your interview:
- Only claim technologies you can discuss deeply
- Be ready to explain every project listed
- Know the architecture of systems you've built
- Have stories ready for each bullet

## Output Format

When optimizing a tech resume:

```markdown
# TECH RESUME OPTIMIZATION

## Technical Skills Restructure
**Current:** [Their current skills section]
**Optimized:**
Languages: [Ordered list]
Frameworks: [Ordered list]
Databases: [Ordered list]
Cloud/Tools: [Ordered list]

## Experience Improvements

### [Company/Role]

**Current Bullet 1:**
"Worked on backend services"

**Improved:**
"Designed and deployed 5 Node.js microservices handling 50K requests/minute, reducing system coupling and enabling independent team deployments"

**Current Bullet 2:**
[Continue for each bullet]

## Projects to Highlight
[Suggestions based on their background]

## GitHub Recommendations
- [ ] Add READMEs to pinned repos
- [ ] Pin X project (most relevant)
- [ ] Add profile README

## Technical Gaps to Address
- [Missing skill] → [How to address in resume/cover letter]
```

## ATS + Tech Recruiter Balance

Remember: Your resume must pass ATS AND impress technical recruiters.

**For ATS:**
- Include exact skill keywords
- Use standard section headers
- Avoid tables and graphics

**For Tech Recruiters:**
- Show technical depth
- Include metrics and scale
- Demonstrate problem-solving
- Show you understand systems
```

