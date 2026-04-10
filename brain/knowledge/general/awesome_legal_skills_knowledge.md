# Knowledge Dump for awesome_legal_skills

## File: DEEP_KNOWLEDGE.md
```
# Deep Matrix Profile: CIV_FETCHED_awesome-legal-skills_105805

# DEEP_KNOWLEDGE.md

## Overview

The `docx-processing-anthropic` project is designed to handle various operations on Microsoft Word documents in `.docx` format. This includes reading, modifying, and validating these documents using Python. The architecture of the project is modular, with clear separation between core functionalities such as XML parsing, document manipulation, and validation.

## Architectural Patterns

### Modularity
The project employs a modular design pattern where different components are separated into distinct modules or classes. This includes:
- **XML Parsing**: Utilizing libraries like `defusedxml` for safe XML parsing.
- **Document Manipulation**: Implementing functions to merge runs, simplify tracked changes, and more.
- **Validation**: Defining validators for schema compliance and redlining.

### Layered Architecture
The project follows a layered architecture:
1. **Data Access Layer (DAL)**: Handles file operations such as reading and writing documents.
2. **Business Logic Layer (BLL)**: Contains the core algorithms for document manipulation, including merging runs and simplifying tracked changes.
3. **Presentation Layer**: Not explicitly defined but implied through command-line interface usage.

### Dependency Injection
The project uses dependency injection to manage dependencies between components. For example, `BaseSchemaValidator` is designed to be flexible by accepting parameters like the directory path of the document and an original file for validation purposes.

## Core Algorithms

### Document Manipulation

#### Merging Runs (`merge_runs.py`)
- **Algorithm**: Traverse through runs in a paragraph or tracked change container.
- **Steps**:
  1. Identify adjacent runs with identical formatting properties.
  2. Remove `rsid` attributes and proof errors.
  3. Merge the content of adjacent runs.

#### Simplifying Tracked Changes (`simplify_redlines.py`)
- **Algorithm**: Merge adjacent tracked changes (ins or del) from the same author if they are truly adjacent.
- **Steps**:
  1. Identify all `w:ins` and `w:del` elements within paragraphs or table cells.
  2. Check for adjacency and identical authors.
  3. Merge content of adjacent tracked changes.

### Validation

#### Base Schema Validator (`base.py`)
- **Algorithm**: Provides a base class with common validation logic.
- **Steps**:
  1. Define ignored validation errors.
  2. Implement methods to parse documents using `defusedxml.minidom`.
  3. Validate against schema and report errors.

#### Redlining Validation (`validators/redlining.py`)
- **Algorithm**: Validates tracked changes by comparing with an original document.
- **Steps**:
  1. Parse the document and original file.
  2. Compare tracked changes in both documents.
  3. Report any discrepancies or missing tracked changes.

## Primary Mechanisms

### XML Parsing
The project uses `defusedxml.minidom` for safe parsing of XML files, ensuring that only valid elements are processed. This is crucial for handling potentially malicious input and maintaining document integrity.

### File Operations
- **Reading**: Uses Python's built-in file operations to read `.docx` files.
- **Writing**: Modifies the parsed XML in memory and writes it back to a new or existing file.

### Command-Line Interface (CLI)
The project provides a CLI for users to interact with the document manipulation and validation tools. This includes options like merging runs, simplifying tracked changes, and validating documents against schemas.

## Example Workflow

1. **Reading Document**:
   ```python
   from pathlib import Path
   import defusedxml.minidom

   doc_xml = Path("path/to/document.xml")
   dom = defusedxml.minidom.parse(doc_xml)
   ```

2. **Merging Runs**:
   ```python
   from helpers.merge_runs import merge_runs

   input_dir = "path/to/input"
   merge_count, message = merge_runs(input_dir)
   print(message)  # Merged 5 runs
   ```

3. **Simplifying Tracked Changes**:
   ```python
   from helpers.simplify_redlines import simplify_redlines

   input_dir = "path/to/input"
   original_file = Path("path/to/original.docx")
   merge_count, message = simplify_redlines(input_dir, original_file)
   print(message)  # Simplified 10 tracked changes
   ```

4. **Validating Document**:
   ```python
   from validators.base import BaseSchemaValidator

   input_dir = "path/to/input"
   validator = BaseSchemaValidator(input_dir)
   errors = validator.validate()
   if errors:
       print("Validation Errors:", errors)
   else:
       print("Document is valid.")
   ```

## Conclusion

The `docx-processing-anthropic` project is well-structured, with clear separation of concerns and robust validation mechanisms. The modular design ensures that each component can be developed, tested, and maintained independently. This architecture supports efficient document manipulation and validation, making it a powerful tool for handling `.docx` files in various applications.

---

This report provides an in-depth understanding of the project's architectural patterns, core algorithms, and primary mechanisms, enabling developers to effectively utilize and extend the project.
```

## File: README.md
```
<picture>
  <a href="https://lawvable.com/en"><img src="assets/hero-animated.svg" alt="AI Agent Skills for Legal Professionals" width="100%"></a>
</picture>

<p align="center">
  <a target="_blank" href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome" /></a>
  <a href="#contributing"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome" /></a>
  <a href="#license"><img src="https://img.shields.io/badge/License-CC_BY--NC--ND_4.0-lightgrey.svg" alt="License" /></a>
  <a href="#browse"><img src="https://img.shields.io/badge/Skills-42-yellow.svg" alt="License" /></a>
</p>
<p align="center">
  <a target="_blank" href="https://www.linkedin.com/company/lawvable/"><img src="https://img.shields.io/badge/Follow on LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Follow on LinkedIn" /></a>
</p>

## What are Agent Skills?

Agent Skills are portable instructions that teach AI agents how to perform specific tasks your way. For legal professionals, this means encoding your expertise into reusable AI workflows. Draft GDPR-compliant privacy policies. Review NDAs using your firm's methodology. Create due diligence checklists that match your standards.

<img src="assets/demo-vscode-tabular-review.gif" alt="Demo" width="100%" />

## Get Started

> [!IMPORTANT]
> **Write once, use anywhere** — Skills are an open standard for AI agents, with adoption growing across the industry. Use them with your favorite AI tool.

<div align="center">
  <br>
  <p>
    <a target="_blank" href="https://claude.com/product/overview"><img src="assets/claude-web.svg" alt="Claude.ai" height="40"></a>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <a target="_blank" href="https://claude.com/product/cowork"><img src="assets/claude-cowork.svg" alt="Claude Cowork" height="40"></a>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <a target="_blank" href="https://claude.com/product/claude-code"><img src="assets/claude-code.svg" alt="Claude Code" height="40"></a>
  </p>
  <br>
  <p>
    <a target="_blank" href="https://openai.com/codex/"><img src="assets/openai-codex.svg" alt="OpenAI Codex" height="40"></a>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <a href="https://geminicli.com/"><img src="assets/gemini-cli.svg" alt="Gemini CLI" height="40"></a>
  </p>
  <br>
  <p>
    <a target="_blank" href="https://manus.im/features/agent-skills"><img src="assets/manus.svg" alt="Manus" height="40"></a>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <a target="_blank" href="https://mistral.ai/products/vibe"><img src="assets/mistral-vibe.svg" alt="Mistral Vibe" height="40"></a>
  </p>
</div>

## Browse

<div align="center">

### ⚡ NAVIGATION ⚡

<table>
<tr>
  <td align="center">
    <a href="#commercial-law"><img src="assets/card-commercial-law.svg" alt="Commercial Law" width="200"/></a>
  </td>
  <td align="center">
    <a href="#privacy-law"><img src="assets/card-privacy-law.svg" alt="Privacy Law" width="200"/></a>
  </td>
  <td align="center">
    <a href="#compliance"><img src="assets/card-compliance.svg" alt="Compliance" width="200"/></a>
  </td>
  <td align="center">
    <a href="#employment-law"><img src="assets/card-employment-law.svg" alt="Employment Law" width="200"/></a>
  </td>
</tr>
<tr>
  <td align="center">
    <a href="#corporate-law"><img src="assets/card-corporate-law.svg" alt="Corporate Law" width="200"/></a>
  </td>
  <td align="center">
    <a href="#legal-methodology"><img src="assets/card-legal-methodology.svg" alt="Legal Methodology" width="200"/></a>
  </td>
  <td align="center">
    <a href="#legal-tooling"><img src="assets/card-tool.svg" alt="Legal Tooling" width="200"/></a>
  </td>
  <td align="center">
    <a href="#microsoft-office"><img src="assets/card-microsoft-office.svg" alt="Microsoft Office" width="200"/></a>
  </td>
</tr>
<tr>
  <td align="center">
    <a href="#adobe-acrobat"><img src="assets/card-adobe-acrobat.svg" alt="Adobe Acrobat" width="200"/></a>
  </td>
  <td align="center">
    <a href="#vibe-coding"><img src="assets/card-vibe-coding.svg" alt="Vibe-Coding" width="200"/></a>
  </td>
  <td align="center">
    <a href="#skill-authoring"><img src="assets/card-skill-authoring.svg" alt="Skill Authoring" width="200"/></a>
  </td>
</tr>
</table>
</div>

<div align="center"><img src="assets/entry-separator-light-animated.svg" alt="---"></div>

<br>
<div align="center"><img src="assets/header-domain-skills.svg" alt="DOMAIN SKILLS" height="60"></div>

### Commercial Law

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/contract-review-anthropic"><img src="assets/badge-contract-review-anthropic.svg" alt="Contract Review by Anthropic"></a>  
_Review contracts against your organization's negotiation playbook, flagging deviations and generating redline suggestions. Use when reviewing vendor contracts, customer agreements, or any commercial agreement where you need clause-by-clause analysis against standard positions._

> [OmniClaw System] Legacy non-English content redacted during Phase 16 OAP Sanitization.
> [OmniClaw System] Legacy non-English content redacted during Phase 16 OAP Sanitization.

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/nda-review-jamie-tso"><img src="assets/badge-nda-review-jamie-tso.svg" alt="NDA Review by Jamie Tso"></a>  
_Guide to review incoming one-way (unilateral) commercial NDAs in a jurisdiction-agnostic way, from either a Recipient or Discloser perspective (user-selected), producing a clause-by-clause issue log with preferred redlines, fallbacks, rationales, owners, and deadlines._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/nda-triage-anthropic"><img src="assets/badge-nda-triage-anthropic.svg" alt="NDA Triage by Anthropic"></a>  
_Screen incoming NDAs and classify them as GREEN (standard), YELLOW (needs review), or RED (significant issues). Use when a new NDA comes in from sales or business development, when assessing NDA risk level, or when deciding whether an NDA needs full counsel review._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/nil-contract-analysis-samir-patel"><img src="assets/badge-nil-contract-analysis-samir-patel.svg" alt="NIL Contract Review by Samir Patel"></a>  
_NIL (Name, Image, and Likeness) contract analysis for NCAA student-athletes. Reviews endorsement deals, social media agreements, merchandise arrangements, and collective deals from the athlete's perspective, flagging red flags and compliance issues with structured negotiation positions._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/tech-contract-negotiation-patrick-munro"><img src="assets/badge-tech-contract-negotiation-patrick-munro.svg" alt="Tech Contract Negotiation by Patrick Munro"></a>  
_Guide to negotiating technology services agreements, professional services contracts, and commercial B2B transactions. Provides three-position frameworks (provider-favorable, balanced, client-favorable), deal-size tactics, objection handling templates, and concession roadmaps._

<div align="center"><img src="assets/entry-separator-light-animated.svg" alt="---"></div>

### Privacy Law

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/politique-cookies-malik-taiar"><img src="assets/badge-politique-cookies-malik-taiar.svg" alt="Cookie Policy by Malik Taiar"></a>  
_Guide for drafting cookie policies compliant with GDPR and the ePrivacy Directive. Includes CNIL 2020 recommendations, a reference template, and best practices._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/dpia-sentinel-oliver-schmidt-prietz"><img src="assets/badge-dpia-sentinel-oliver-schmidt-prietz.svg" alt="DPIA Sentinel by Oliver Schmidt-Prietz"></a>  
_GDPR Data Protection Impact Assessment (DPIA) guidance under Article 35 GDPR, EDPB Guidelines WP 248 rev.01, and national SA blacklists/whitelists. Covers threshold assessment, multi-jurisdictional blacklist checks, 5x5 risk scoring, necessity/proportionality analysis, and mitigation mapping._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/gdpr-breach-sentinel-oliver-schmidt-prietz"><img src="assets/badge-gdpr-breach-sentinel-oliver-schmidt-prietz.svg" alt="GDPR Breach by Oliver Schmidt-Prietz"></a>  
_Incident response and legal compliance guidance for data breaches under GDPR Articles 33 & 34. Covers breach risk assessment using ENISA severity methodology, Controller vs Processor obligations, 72-hour notification clock management, EDPB case matching, and cross-border Lead SA determination._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/compliance-anthropic"><img src="assets/badge-compliance-anthropic.svg" alt="Privacy Compliance by Anthropic"></a>  
_Navigate privacy regulations (GDPR, CCPA), review DPAs, and handle data subject requests. Use when reviewing data processing agreements, responding to data subject access or deletion requests, or evaluating privacy compliance._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/gdpr-privacy-notice-eu-oliver-schmidt-prietz"><img src="assets/badge-gdpr-privacy-notice-eu-oliver-schmidt-prietz.svg" alt="Privacy Notice by Oliver Schmidt-Prietz"></a>  
_Draft GDPR-compliant privacy notices as .docx for any EU/EEA jurisdiction and audience. Supports five notice types (Website/App, Applicant, Employee, Business Partner, B2C Customer) across DE, FR, AT, IT, ES, NL, BE, IE, and UK GDPR._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/politique-confidentialite-malik-taiar"><img src="assets/badge-politique-confidentialite-malik-taiar.svg" alt="Privacy Policy by Malik Taiar"></a>  
_Guide for drafting privacy policies compliant with GDPR. Includes CNIL 2020 recommendations, a reference template, and best practices._

<div align="center"><img src="assets/entry-separator-light-animated.svg" alt="---"></div>

### Compliance

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/vendor-due-diligence-patrick-munro"><img src="assets/badge-vendor-due-diligence-patrick-munro.svg" alt="Vendor Due Diligence by Patrick Munro"></a>  
_Framework for assessing IT service providers, technology vendors, and third-party partners. Creates structured risk assessments across financial, operational, compliance, security, and reputational dimensions with regulatory checklists (GDPR, DORA, NIS2, SOX)._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/politique-lanceur-alerte-malik-taiar"><img src="assets/badge-politique-lanceur-alerte-malik-taiar.svg" alt="Whistleblower Policy by Malik Taiar"></a>  
_Guide for auditing an existing whistleblower system or drafting a compliant reporting policy. Covers EU Directive 2019/1937, the amended Sapin II law (Waserman 2022), Decree 2022-1284, CNIL guidelines, and duty of vigilance._

<div align="center"><img src="assets/entry-separator-light-animated.svg" alt="---"></div>

### Employment Law

> [OmniClaw System] Legacy non-English content redacted during Phase 16 OAP Sanitization.
_Guide for drafting petitions to the French Labor Court (Conseil de prud'hommes) to contest a dismissal for gross misconduct and request reclassification as unfair dismissal._

> [OmniClaw System] Legacy non-English content redacted during Phase 16 OAP Sanitization.
_Guide for drafting dismissal notifications compliant with French labor law. Covers serious misconduct, gross misconduct, and personal grounds with all mandatory elements under French law._

<div align="center"><img src="assets/entry-separator-light-animated.svg" alt="---"></div>

### Corporate Law

> [OmniClaw System] Legacy non-English content redacted during Phase 16 OAP Sanitization.
> [OmniClaw System] Legacy non-English content redacted during Phase 16 OAP Sanitization.

<div align="center"><img src="assets/entry-separator-light-animated.svg" alt="---"></div>

### Legal Methodology

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/legal-simulation-patrick-munro"><img src="assets/badge-legal-simulation-patrick-munro.svg" alt="Legal Simulation by Patrick Munro"></a>  
_Framework for demonstrating AI capabilities in legal contexts. Provides detailed personas across tenant law, business contracts, startup disputes, employment claims, and consumer protection with progressive complexity scenarios._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/mediation-dispute-analysis-jinzhe-tan"><img src="assets/badge-mediation-dispute-analysis-jinzhe-tan.svg" alt="Mediation Analysis by Jinzhe Tan"></a>  
_Analyze case materials for mediation preparation across civil and commercial disputes. Identifies core issues, party positions, underlying interests, BATNA/WATNA scenarios, and zones of possible agreement with multiple settlement pathways._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/red-team-verifier-patrick-munro"><img src="assets/badge-red-team-verifier-patrick-munro.svg" alt="Red Team Verifier by Patrick Munro"></a>  
_Adversarial verification for AI-generated legal content with systematic fact-checking, source validation, and quality control. Provides structured verification reports with severity-categorized errors and distribution readiness assessment._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/legal-risk-assessment-anthropic"><img src="assets/badge-legal-risk-assessment-anthropic.svg" alt="Risk Assessment by Anthropic"></a>  
_Assess and classify legal risks using a severity-by-likelihood framework with escalation criteria. Use when evaluating contract risk, assessing deal exposure, or classifying issues by severity._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/legal-risk-assessment-zacharie-laik"><img src="assets/badge-legal-risk-assessment-zacharie-laik.svg" alt="Risk Assessment by Zacharie Laïk"></a>  
_Legal research and risk evaluation for in-house teams using GoodLegal's tools. Conducts adversarial jurisprudence searches on French and EU law, identifies risk factors with inline citations, and performs temporal confidence checks on case law._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/statute-analysis-rafal-fryc"><img src="assets/badge-statute-analysis-rafal-fryc.svg" alt="Statutory Interpretation by Rafał Stanisław Fryc"></a>  
_Guide for reading, interpreting, and applying statutes, regulations, and rules in legal and compliance contexts. Covers statutory interpretation methods, canons of construction, and legislative intent._

<br>
<div align="center"><img src="assets/header-utility-skills.svg" alt="UTILITY SKILLS" height="60"></div>

### Legal Tooling

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/canned-responses-anthropic"><img src="assets/badge-canned-responses-anthropic.svg" alt="Canned Responses by Anthropic"></a>  
_Generate templated responses for common legal inquiries and identify when situations require individualized attention. Covers data subject requests, vendor inquiries, NDA requests, and discovery holds._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/meeting-briefing-anthropic"><img src="assets/badge-meeting-briefing-anthropic.svg" alt="Meeting Briefing by Anthropic"></a>  
_Prepare structured briefings for meetings with legal relevance and track resulting action items. Use when preparing for contract negotiations, board meetings, or compliance reviews._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/tabular-review-lawvable"><img src="assets/badge-tabular-review-lawvable.svg" alt="Tabular Review by Lawvable"></a>  
_Analyze multiple documents (PDF, DOCX) against user-defined columns and produce a structured Excel output with citations. Compare clauses or provisions across contracts._

<div align="center"><img src="assets/entry-separator-light-animated.svg" alt="---"></div>

### Microsoft Office

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/xlsx-processing-anthropic"><img src="assets/badge-xlsx-processing-anthropic.svg" alt="Excel by Anthropic"></a>  
_Comprehensive spreadsheet creation, editing, and analysis with support for formulas, formatting, data analysis, and visualization._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/xlsx-processing-openai"><img src="assets/badge-xlsx-processing-openai.svg" alt="Excel by OpenAI"></a>  
_Comprehensive spreadsheet reading, creation, editing, and analysis with visual quality control._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/xlsx-processing-manus"><img src="assets/badge-xlsx-processing-manus.svg" alt="Excel by Manus"></a>  
_Professional Excel spreadsheet creation with a focus on aesthetics and data analysis._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/outlook-emails-lawvable"><img src="assets/badge-outlook-emails-lawvable.svg" alt="Outlook by Lawvable"></a>  
_Read, search, and download emails and attachments from Microsoft Outlook via OAuth2._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/pptx-processing-anthropic"><img src="assets/badge-pptx-processing-anthropic.svg" alt="PowerPoint by Anthropic"></a>  
_Comprehensive presentation creation, editing, and analysis with support for layouts, comments, and speaker notes._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/docx-processing-lawvable"><img src="assets/badge-docx-processing-lawvable.svg" alt="Word by Lawvable"></a>  
_Edit Word documents with live preview and track changes via SuperDoc VS Code extension. Use when editing DOCX files, making tracked changes, or redlining contracts._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/docx-processing-superdoc"><img src="assets/badge-docx-processing-superdoc.svg" alt="Word by Superdoc"></a>  
_Search, replace, and read text in Word documents from the command line._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/docx-processing-anthropic"><img src="assets/badge-docx-processing-anthropic.svg" alt="Word by Anthropic"></a>  
_Comprehensive document creation, editing, and analysis with support for tracked changes, comments, formatting preservation, and text extraction._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/docx-processing-openai"><img src="assets/badge-docx-processing-openai.svg" alt="Word by OpenAI"></a>  
_Comprehensive document reading and creation with visual quality control for Word documents._

<div align="center"><img src="assets/entry-separator-light-animated.svg" alt="---"></div>

### Adobe Acrobat

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/pdf-processing-anthropic"><img src="assets/badge-pdf-processing-anthropic.svg" alt="PDF by Anthropic"></a>  
_Comprehensive PDF manipulation, including extracting text and tables, creating new PDFs, merging/splitting documents, and handling forms._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/pdf-processing-openai"><img src="assets/badge-pdf-processing-openai.svg" alt="PDF by OpenAI"></a>  
_Comprehensive PDF reading and creation with visual quality control._

<div align="center"><img src="assets/entry-separator-light-animated.svg" alt="---"></div>

### Vibe-coding

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/security-review-openai"><img src="assets/badge-security-review-openai.svg" alt="Security Review by OpenAI"></a>  
_Perform language and framework specific security best-practice reviews and suggest improvements. Supports Python, JavaScript/TypeScript, and Go with detailed vulnerability reports and fix suggestions._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/vscode-extension-builder-lawvable"><img src="assets/badge-vscode-extension-builder-lawvable.svg" alt="VS Code Extension by Lawvable"></a>  
_Build VS Code extensions from scratch or convert existing JS/React/Vue apps. Supports commands, webviews, custom editors, tree views, and AI agent integration._

<div align="center"><img src="assets/entry-separator-light-animated.svg" alt="---"></div>

<br>
<div align="center"><img src="assets/header-meta-skills.svg" alt="META-SKILLS" height="60"></div>
    
### Skill Authoring

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/skill-creator-anthropic"><img src="assets/badge-skill-creator-anthropic.svg" alt="Self-Creation by Anthropic"></a>  
_Guide for creating effective skills that extend the model's capabilities with specialized knowledge, workflows, or tool integrations._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/skill-creator-openai"><img src="assets/badge-skill-creator-openai.svg" alt="Self-Creation by OpenAI"></a>  
_Guide for creating effective skills that extend the model's capabilities with specialized knowledge, workflows, or tool integrations._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/skill-optimizer-lawvable"><img src="assets/badge-skill-optimizer-lawvable.svg" alt="Self-Improvement by Lawvable"></a>  
_Analyze a current work session and propose improvements to skills. Captures learnings automatically after working with a skill._

## Contributing

It's easy! Just click the link below and fill out the form. No Git knowledge required.

<h3 align="center">🚀 <a href="https://github.com/lawvable/awesome-legal-skills/issues/new?template=submit-skill.yml">Submit a new Skill here!</a></h3>

**How we evaluate submissions:** Every resource goes through a manual review before it makes it onto this list. First and foremost, best efforts are made to check for security concerns - no malware, bloatware, or other unwanted risks. Then, we assess whether the skill actually delivers real, practical value to users before it gets listed. See [CONTRIBUTING.md](/CONTRIBUTING.md) for more details.

## Support
Lawvable is the first-ever open hub dedicated to AI agent skills for law - and it's growing every day thanks to the incredible contributors sharing their work and the community showing its support. If you find this list useful, consider giving it a ⭐ - it helps others discover it too.

[![Stargazers over time](https://starchart.cc/lawvable/awesome-legal-skills.svg?variant=adaptive)](https://starchart.cc/lawvable/awesome-legal-skills)

## License

This list is licensed under the [Creative Commons CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/) license. This means you are welcome to fork, clone, copy and redistribute the list, provided you include appropriate attribution; however you are not permitted to distribute any modified versions or use it for commercial purposes. This is to prevent unlawful appropriation of the work of the authors whose resources are listed here. Please note that **all resources included in this list have their own license terms** - if you wish to incorporate those authors' works into your _own_ product, you need to do so according to the terms that _those authors_ have set out.

## Disclaimer

Although we take strong measures to uphold the quality and safety of this list, we take no responsibility or liability for anything bad that might happen as a result of these third-party resources. Make sure the skills you download are aligned with your firm's confidentiality policies and professional responsibility obligations.

## Acknowledgments

This project wouldn't exist without the Anthropic team, who developed the Skills standard and published the examples that got us all started. Huge thanks to every contributor who has shared their work here - you're the reason this list keeps growing. And to everyone who has starred, forked, or simply bookmarked this repo: your support means more than you think. Finally, a hat tip to [@hesreallyhim](https://github.com/hesreallyhim) and his [awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) repo, whose design inspired the look and feel of this one.

```

## File: schema.json
```
{
    "name": "Awesome Legal Skills",
    "description": "Assimilated OmniClaw Skill for awesome_legal_skills.",
    "domain": "core",
    "tier": 3,
    "type": "assimilated_repo_skill",
    "parameters": {}
}
```

## File: SKILL.md
```
---
id: awesome_legal_skills
name: Awesome Legal Skills
version: 1.0.0
tier: 3
status: active
author: OmniClaw Assimilation Daemon
updated: 2026-04-09
domain: core
---

# Awesome Legal Skills

This skill was assimilated from an external raw repository.
Reference README.md or DEEP_KNOWLEDGE.md for specific technical payload.

```

## File: _DIR_IDENTITY.md
```
---
id: awesome_legal_skills
type: skill
owner: OA
registered_at: 2026-04-08T13:33:46.287323
tags: ["auto-cloned", "AI", "Legal", "Skills", "oa-assimilated", "premium-repo"]
---

# CIV_FETCHED_awesome_legal_skills

## Assimilation Report
The repository appears to be related to AI Agent Skills for legal professionals, focusing on creating portable instructions for AI agents to perform specific tasks. It includes badges and links to support community engagement and open adoption of the standard.

## Application for OmniClaw
EMERGENCY FALLBACK: LLM failed to analyze. However, because this is a CIV-Approved Repo, OA forces assimilation. Please manually review and integrate.

```

## File: payload\config.json
```
{"database":"sqlite","host":"localhost","port":3306,"username":"root","password":"password","table":"skills"}
```

## File: payload\contributing.md
```
# Contributing

Welcome! We're excited that you want to contribute to Lawvable. This guide will walk you through our streamlined contribution process.

**Important:** We take security seriously. All submissions are carefully reviewed to ensure they don't expose users to data risks or malicious code. Advanced tools may take additional time to review.

> [!IMPORTANT] 
> Due to resource limitations, you may experience some delays in getting a review from a maintainer. We appreciate your patience.

## How to Submit a Skill

It's easy! Just click the link below and fill out the form. No Git knowledge required.

<a href="https://github.com/lawvable/awesome-legal-skills/issues/new?template=submit-skill.yml">
  <h3 align="center">🚀 Submit a new Skill here!</h1>
</a>

## Before You Start

- Ensure your skill is based on a **real use case**, not a hypothetical scenario
- Search existing skills to avoid duplicates
- Verify your skill works on at least one platform (Claude.ai, Claude Code, etc.)
- If inspired by someone's workflow, prepare to give attribution

## Skill Authoring

Every skill lives in a folder with a lowercase, hyphen-separated name:

```
skill-name/
├── SKILL.md          # Required: instructions with YAML frontmatter
├── scripts/          # Optional: helper scripts
├── templates/        # Optional: document templates
└── resources/        # Optional: reference materials
```

We strongly recommend using the [**skill-creator**](https://github.com/anthropics/skill-creator) meta-skill, which comes pre-installed with many agents, to guide you through the process from start to finish. It enforces good practices around structure, progressive disclosure, and SKILL.md quality - so you don't have to remember all the rules yourself. Just ask your agent to create a new skill and it will take it from there.

Once you've gone through a few rounds of iteration, do a **final review pass**: ask the AI agent to verify that the finished skill satisfies all the guidelines set out in the skill-creator skill. This catches things like missing frontmatter fields, overly long SKILL.md files, or resources that should have been split into separate reference files.

For an extensive and well-written guide on what makes a great skill, have a look at Anthropic's official [Best Practices for Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices).

## Questions?

Open an [issue](https://github.com/lawvable/awesome-legal-skills/issues) for help. Please be respectful and credit original sources.

```

## File: payload\DEEP_KNOWLEDGE.md
```
# Deep Matrix Profile: CIV_FETCHED_awesome-legal-skills_105805

# DEEP_KNOWLEDGE.md

## Overview

The `docx-processing-anthropic` project is designed to handle various operations on Microsoft Word documents in `.docx` format. This includes reading, modifying, and validating these documents using Python. The architecture of the project is modular, with clear separation between core functionalities such as XML parsing, document manipulation, and validation.

## Architectural Patterns

### Modularity
The project employs a modular design pattern where different components are separated into distinct modules or classes. This includes:
- **XML Parsing**: Utilizing libraries like `defusedxml` for safe XML parsing.
- **Document Manipulation**: Implementing functions to merge runs, simplify tracked changes, and more.
- **Validation**: Defining validators for schema compliance and redlining.

### Layered Architecture
The project follows a layered architecture:
1. **Data Access Layer (DAL)**: Handles file operations such as reading and writing documents.
2. **Business Logic Layer (BLL)**: Contains the core algorithms for document manipulation, including merging runs and simplifying tracked changes.
3. **Presentation Layer**: Not explicitly defined but implied through command-line interface usage.

### Dependency Injection
The project uses dependency injection to manage dependencies between components. For example, `BaseSchemaValidator` is designed to be flexible by accepting parameters like the directory path of the document and an original file for validation purposes.

## Core Algorithms

### Document Manipulation

#### Merging Runs (`merge_runs.py`)
- **Algorithm**: Traverse through runs in a paragraph or tracked change container.
- **Steps**:
  1. Identify adjacent runs with identical formatting properties.
  2. Remove `rsid` attributes and proof errors.
  3. Merge the content of adjacent runs.

#### Simplifying Tracked Changes (`simplify_redlines.py`)
- **Algorithm**: Merge adjacent tracked changes (ins or del) from the same author if they are truly adjacent.
- **Steps**:
  1. Identify all `w:ins` and `w:del` elements within paragraphs or table cells.
  2. Check for adjacency and identical authors.
  3. Merge content of adjacent tracked changes.

### Validation

#### Base Schema Validator (`base.py`)
- **Algorithm**: Provides a base class with common validation logic.
- **Steps**:
  1. Define ignored validation errors.
  2. Implement methods to parse documents using `defusedxml.minidom`.
  3. Validate against schema and report errors.

#### Redlining Validation (`validators/redlining.py`)
- **Algorithm**: Validates tracked changes by comparing with an original document.
- **Steps**:
  1. Parse the document and original file.
  2. Compare tracked changes in both documents.
  3. Report any discrepancies or missing tracked changes.

## Primary Mechanisms

### XML Parsing
The project uses `defusedxml.minidom` for safe parsing of XML files, ensuring that only valid elements are processed. This is crucial for handling potentially malicious input and maintaining document integrity.

### File Operations
- **Reading**: Uses Python's built-in file operations to read `.docx` files.
- **Writing**: Modifies the parsed XML in memory and writes it back to a new or existing file.

### Command-Line Interface (CLI)
The project provides a CLI for users to interact with the document manipulation and validation tools. This includes options like merging runs, simplifying tracked changes, and validating documents against schemas.

## Example Workflow

1. **Reading Document**:
   ```python
   from pathlib import Path
   import defusedxml.minidom

   doc_xml = Path("path/to/document.xml")
   dom = defusedxml.minidom.parse(doc_xml)
   ```

2. **Merging Runs**:
   ```python
   from helpers.merge_runs import merge_runs

   input_dir = "path/to/input"
   merge_count, message = merge_runs(input_dir)
   print(message)  # Merged 5 runs
   ```

3. **Simplifying Tracked Changes**:
   ```python
   from helpers.simplify_redlines import simplify_redlines

   input_dir = "path/to/input"
   original_file = Path("path/to/original.docx")
   merge_count, message = simplify_redlines(input_dir, original_file)
   print(message)  # Simplified 10 tracked changes
   ```

4. **Validating Document**:
   ```python
   from validators.base import BaseSchemaValidator

   input_dir = "path/to/input"
   validator = BaseSchemaValidator(input_dir)
   errors = validator.validate()
   if errors:
       print("Validation Errors:", errors)
   else:
       print("Document is valid.")
   ```

## Conclusion

The `docx-processing-anthropic` project is well-structured, with clear separation of concerns and robust validation mechanisms. The modular design ensures that each component can be developed, tested, and maintained independently. This architecture supports efficient document manipulation and validation, making it a powerful tool for handling `.docx` files in various applications.

---

This report provides an in-depth understanding of the project's architectural patterns, core algorithms, and primary mechanisms, enabling developers to effectively utilize and extend the project.
```

## File: payload\models.py
```
from app import db
class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
```

## File: payload\README.md
```
<picture>
  <a href="https://lawvable.com/en"><img src="assets/hero-animated.svg" alt="AI Agent Skills for Legal Professionals" width="100%"></a>
</picture>

<p align="center">
  <a target="_blank" href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome" /></a>
  <a href="#contributing"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome" /></a>
  <a href="#license"><img src="https://img.shields.io/badge/License-CC_BY--NC--ND_4.0-lightgrey.svg" alt="License" /></a>
  <a href="#browse"><img src="https://img.shields.io/badge/Skills-42-yellow.svg" alt="License" /></a>
</p>
<p align="center">
  <a target="_blank" href="https://www.linkedin.com/company/lawvable/"><img src="https://img.shields.io/badge/Follow on LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Follow on LinkedIn" /></a>
</p>

## What are Agent Skills?

Agent Skills are portable instructions that teach AI agents how to perform specific tasks your way. For legal professionals, this means encoding your expertise into reusable AI workflows. Draft GDPR-compliant privacy policies. Review NDAs using your firm's methodology. Create due diligence checklists that match your standards.

<img src="assets/demo-vscode-tabular-review.gif" alt="Demo" width="100%" />

## Get Started

> [!IMPORTANT]
> **Write once, use anywhere** — Skills are an open standard for AI agents, with adoption growing across the industry. Use them with your favorite AI tool.

<div align="center">
  <br>
  <p>
    <a target="_blank" href="https://claude.com/product/overview"><img src="assets/claude-web.svg" alt="Claude.ai" height="40"></a>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <a target="_blank" href="https://claude.com/product/cowork"><img src="assets/claude-cowork.svg" alt="Claude Cowork" height="40"></a>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <a target="_blank" href="https://claude.com/product/claude-code"><img src="assets/claude-code.svg" alt="Claude Code" height="40"></a>
  </p>
  <br>
  <p>
    <a target="_blank" href="https://openai.com/codex/"><img src="assets/openai-codex.svg" alt="OpenAI Codex" height="40"></a>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <a href="https://geminicli.com/"><img src="assets/gemini-cli.svg" alt="Gemini CLI" height="40"></a>
  </p>
  <br>
  <p>
    <a target="_blank" href="https://manus.im/features/agent-skills"><img src="assets/manus.svg" alt="Manus" height="40"></a>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <a target="_blank" href="https://mistral.ai/products/vibe"><img src="assets/mistral-vibe.svg" alt="Mistral Vibe" height="40"></a>
  </p>
</div>

## Browse

<div align="center">

### ⚡ NAVIGATION ⚡

<table>
<tr>
  <td align="center">
    <a href="#commercial-law"><img src="assets/card-commercial-law.svg" alt="Commercial Law" width="200"/></a>
  </td>
  <td align="center">
    <a href="#privacy-law"><img src="assets/card-privacy-law.svg" alt="Privacy Law" width="200"/></a>
  </td>
  <td align="center">
    <a href="#compliance"><img src="assets/card-compliance.svg" alt="Compliance" width="200"/></a>
  </td>
  <td align="center">
    <a href="#employment-law"><img src="assets/card-employment-law.svg" alt="Employment Law" width="200"/></a>
  </td>
</tr>
<tr>
  <td align="center">
    <a href="#corporate-law"><img src="assets/card-corporate-law.svg" alt="Corporate Law" width="200"/></a>
  </td>
  <td align="center">
    <a href="#legal-methodology"><img src="assets/card-legal-methodology.svg" alt="Legal Methodology" width="200"/></a>
  </td>
  <td align="center">
    <a href="#legal-tooling"><img src="assets/card-tool.svg" alt="Legal Tooling" width="200"/></a>
  </td>
  <td align="center">
    <a href="#microsoft-office"><img src="assets/card-microsoft-office.svg" alt="Microsoft Office" width="200"/></a>
  </td>
</tr>
<tr>
  <td align="center">
    <a href="#adobe-acrobat"><img src="assets/card-adobe-acrobat.svg" alt="Adobe Acrobat" width="200"/></a>
  </td>
  <td align="center">
    <a href="#vibe-coding"><img src="assets/card-vibe-coding.svg" alt="Vibe-Coding" width="200"/></a>
  </td>
  <td align="center">
    <a href="#skill-authoring"><img src="assets/card-skill-authoring.svg" alt="Skill Authoring" width="200"/></a>
  </td>
</tr>
</table>
</div>

<div align="center"><img src="assets/entry-separator-light-animated.svg" alt="---"></div>

<br>
<div align="center"><img src="assets/header-domain-skills.svg" alt="DOMAIN SKILLS" height="60"></div>

### Commercial Law

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/contract-review-anthropic"><img src="assets/badge-contract-review-anthropic.svg" alt="Contract Review by Anthropic"></a>  
_Review contracts against your organization's negotiation playbook, flagging deviations and generating redline suggestions. Use when reviewing vendor contracts, customer agreements, or any commercial agreement where you need clause-by-clause analysis against standard positions._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/assignation-refere-recouvrement-creance-selim-brihi"><img src="assets/badge-assignation-refere-recouvrement-creance-selim-brihi.svg" alt="Debt Recovery by Sélim Brihi"></a>  
_Guide for drafting emergency court filings (assignation en référé) before the Commercial Court to recover unpaid commercial debts. Use when a creditor needs to obtain a fast-track court order for payment of undisputed invoices._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/nda-review-jamie-tso"><img src="assets/badge-nda-review-jamie-tso.svg" alt="NDA Review by Jamie Tso"></a>  
_Guide to review incoming one-way (unilateral) commercial NDAs in a jurisdiction-agnostic way, from either a Recipient or Discloser perspective (user-selected), producing a clause-by-clause issue log with preferred redlines, fallbacks, rationales, owners, and deadlines._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/nda-triage-anthropic"><img src="assets/badge-nda-triage-anthropic.svg" alt="NDA Triage by Anthropic"></a>  
_Screen incoming NDAs and classify them as GREEN (standard), YELLOW (needs review), or RED (significant issues). Use when a new NDA comes in from sales or business development, when assessing NDA risk level, or when deciding whether an NDA needs full counsel review._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/nil-contract-analysis-samir-patel"><img src="assets/badge-nil-contract-analysis-samir-patel.svg" alt="NIL Contract Review by Samir Patel"></a>  
_NIL (Name, Image, and Likeness) contract analysis for NCAA student-athletes. Reviews endorsement deals, social media agreements, merchandise arrangements, and collective deals from the athlete's perspective, flagging red flags and compliance issues with structured negotiation positions._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/tech-contract-negotiation-patrick-munro"><img src="assets/badge-tech-contract-negotiation-patrick-munro.svg" alt="Tech Contract Negotiation by Patrick Munro"></a>  
_Guide to negotiating technology services agreements, professional services contracts, and commercial B2B transactions. Provides three-position frameworks (provider-favorable, balanced, client-favorable), deal-size tactics, objection handling templates, and concession roadmaps._

<div align="center"><img src="assets/entry-separator-light-animated.svg" alt="---"></div>

### Privacy Law

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/politique-cookies-malik-taiar"><img src="assets/badge-politique-cookies-malik-taiar.svg" alt="Cookie Policy by Malik Taiar"></a>  
_Guide for drafting cookie policies compliant with GDPR and the ePrivacy Directive. Includes CNIL 2020 recommendations, a reference template, and best practices._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/dpia-sentinel-oliver-schmidt-prietz"><img src="assets/badge-dpia-sentinel-oliver-schmidt-prietz.svg" alt="DPIA Sentinel by Oliver Schmidt-Prietz"></a>  
_GDPR Data Protection Impact Assessment (DPIA) guidance under Article 35 GDPR, EDPB Guidelines WP 248 rev.01, and national SA blacklists/whitelists. Covers threshold assessment, multi-jurisdictional blacklist checks, 5x5 risk scoring, necessity/proportionality analysis, and mitigation mapping._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/gdpr-breach-sentinel-oliver-schmidt-prietz"><img src="assets/badge-gdpr-breach-sentinel-oliver-schmidt-prietz.svg" alt="GDPR Breach by Oliver Schmidt-Prietz"></a>  
_Incident response and legal compliance guidance for data breaches under GDPR Articles 33 & 34. Covers breach risk assessment using ENISA severity methodology, Controller vs Processor obligations, 72-hour notification clock management, EDPB case matching, and cross-border Lead SA determination._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/compliance-anthropic"><img src="assets/badge-compliance-anthropic.svg" alt="Privacy Compliance by Anthropic"></a>  
_Navigate privacy regulations (GDPR, CCPA), review DPAs, and handle data subject requests. Use when reviewing data processing agreements, responding to data subject access or deletion requests, or evaluating privacy compliance._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/gdpr-privacy-notice-eu-oliver-schmidt-prietz"><img src="assets/badge-gdpr-privacy-notice-eu-oliver-schmidt-prietz.svg" alt="Privacy Notice by Oliver Schmidt-Prietz"></a>  
_Draft GDPR-compliant privacy notices as .docx for any EU/EEA jurisdiction and audience. Supports five notice types (Website/App, Applicant, Employee, Business Partner, B2C Customer) across DE, FR, AT, IT, ES, NL, BE, IE, and UK GDPR._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/politique-confidentialite-malik-taiar"><img src="assets/badge-politique-confidentialite-malik-taiar.svg" alt="Privacy Policy by Malik Taiar"></a>  
_Guide for drafting privacy policies compliant with GDPR. Includes CNIL 2020 recommendations, a reference template, and best practices._

<div align="center"><img src="assets/entry-separator-light-animated.svg" alt="---"></div>

### Compliance

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/vendor-due-diligence-patrick-munro"><img src="assets/badge-vendor-due-diligence-patrick-munro.svg" alt="Vendor Due Diligence by Patrick Munro"></a>  
_Framework for assessing IT service providers, technology vendors, and third-party partners. Creates structured risk assessments across financial, operational, compliance, security, and reputational dimensions with regulatory checklists (GDPR, DORA, NIS2, SOX)._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/politique-lanceur-alerte-malik-taiar"><img src="assets/badge-politique-lanceur-alerte-malik-taiar.svg" alt="Whistleblower Policy by Malik Taiar"></a>  
_Guide for auditing an existing whistleblower system or drafting a compliant reporting policy. Covers EU Directive 2019/1937, the amended Sapin II law (Waserman 2022), Decree 2022-1284, CNIL guidelines, and duty of vigilance._

<div align="center"><img src="assets/entry-separator-light-animated.svg" alt="---"></div>

### Employment Law

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/requete-cph-licenciement-faute-grave-selim-brihi"><img src="assets/badge-requete-cph-licenciement-faute-grave-selim-brihi.svg" alt="Dismissal Challenge by Sélim Brihi"></a>  
_Guide for drafting petitions to the French Labor Court (Conseil de prud'hommes) to contest a dismissal for gross misconduct and request reclassification as unfair dismissal._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/notification-licenciement-selim-brihi"><img src="assets/badge-notification-licenciement-selim-brihi.svg" alt="Dismissal Notification by Sélim Brihi"></a>  
_Guide for drafting dismissal notifications compliant with French labor law. Covers serious misconduct, gross misconduct, and personal grounds with all mandatory elements under French law._

<div align="center"><img src="assets/entry-separator-light-animated.svg" alt="---"></div>

### Corporate Law

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/assignation-refere-communication-associe-selim-brihi"><img src="assets/badge-assignation-refere-communication-associe-selim-brihi.svg" alt="Shareholder Disclosure by Sélim Brihi"></a>  
_Guide for drafting emergency court filings (assignation en référé) to force disclosure of corporate documents to a shareholder under Article L. 238-1 of the French Commercial Code._

<div align="center"><img src="assets/entry-separator-light-animated.svg" alt="---"></div>

### Legal Methodology

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/legal-simulation-patrick-munro"><img src="assets/badge-legal-simulation-patrick-munro.svg" alt="Legal Simulation by Patrick Munro"></a>  
_Framework for demonstrating AI capabilities in legal contexts. Provides detailed personas across tenant law, business contracts, startup disputes, employment claims, and consumer protection with progressive complexity scenarios._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/mediation-dispute-analysis-jinzhe-tan"><img src="assets/badge-mediation-dispute-analysis-jinzhe-tan.svg" alt="Mediation Analysis by Jinzhe Tan"></a>  
_Analyze case materials for mediation preparation across civil and commercial disputes. Identifies core issues, party positions, underlying interests, BATNA/WATNA scenarios, and zones of possible agreement with multiple settlement pathways._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/red-team-verifier-patrick-munro"><img src="assets/badge-red-team-verifier-patrick-munro.svg" alt="Red Team Verifier by Patrick Munro"></a>  
_Adversarial verification for AI-generated legal content with systematic fact-checking, source validation, and quality control. Provides structured verification reports with severity-categorized errors and distribution readiness assessment._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/legal-risk-assessment-anthropic"><img src="assets/badge-legal-risk-assessment-anthropic.svg" alt="Risk Assessment by Anthropic"></a>  
_Assess and classify legal risks using a severity-by-likelihood framework with escalation criteria. Use when evaluating contract risk, assessing deal exposure, or classifying issues by severity._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/legal-risk-assessment-zacharie-laik"><img src="assets/badge-legal-risk-assessment-zacharie-laik.svg" alt="Risk Assessment by Zacharie Laïk"></a>  
_Legal research and risk evaluation for in-house teams using GoodLegal's tools. Conducts adversarial jurisprudence searches on French and EU law, identifies risk factors with inline citations, and performs temporal confidence checks on case law._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/statute-analysis-rafal-fryc"><img src="assets/badge-statute-analysis-rafal-fryc.svg" alt="Statutory Interpretation by Rafał Stanisław Fryc"></a>  
_Guide for reading, interpreting, and applying statutes, regulations, and rules in legal and compliance contexts. Covers statutory interpretation methods, canons of construction, and legislative intent._

<br>
<div align="center"><img src="assets/header-utility-skills.svg" alt="UTILITY SKILLS" height="60"></div>

### Legal Tooling

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/canned-responses-anthropic"><img src="assets/badge-canned-responses-anthropic.svg" alt="Canned Responses by Anthropic"></a>  
_Generate templated responses for common legal inquiries and identify when situations require individualized attention. Covers data subject requests, vendor inquiries, NDA requests, and discovery holds._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/meeting-briefing-anthropic"><img src="assets/badge-meeting-briefing-anthropic.svg" alt="Meeting Briefing by Anthropic"></a>  
_Prepare structured briefings for meetings with legal relevance and track resulting action items. Use when preparing for contract negotiations, board meetings, or compliance reviews._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/tabular-review-lawvable"><img src="assets/badge-tabular-review-lawvable.svg" alt="Tabular Review by Lawvable"></a>  
_Analyze multiple documents (PDF, DOCX) against user-defined columns and produce a structured Excel output with citations. Compare clauses or provisions across contracts._

<div align="center"><img src="assets/entry-separator-light-animated.svg" alt="---"></div>

### Microsoft Office

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/xlsx-processing-anthropic"><img src="assets/badge-xlsx-processing-anthropic.svg" alt="Excel by Anthropic"></a>  
_Comprehensive spreadsheet creation, editing, and analysis with support for formulas, formatting, data analysis, and visualization._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/xlsx-processing-openai"><img src="assets/badge-xlsx-processing-openai.svg" alt="Excel by OpenAI"></a>  
_Comprehensive spreadsheet reading, creation, editing, and analysis with visual quality control._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/xlsx-processing-manus"><img src="assets/badge-xlsx-processing-manus.svg" alt="Excel by Manus"></a>  
_Professional Excel spreadsheet creation with a focus on aesthetics and data analysis._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/outlook-emails-lawvable"><img src="assets/badge-outlook-emails-lawvable.svg" alt="Outlook by Lawvable"></a>  
_Read, search, and download emails and attachments from Microsoft Outlook via OAuth2._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/pptx-processing-anthropic"><img src="assets/badge-pptx-processing-anthropic.svg" alt="PowerPoint by Anthropic"></a>  
_Comprehensive presentation creation, editing, and analysis with support for layouts, comments, and speaker notes._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/docx-processing-lawvable"><img src="assets/badge-docx-processing-lawvable.svg" alt="Word by Lawvable"></a>  
_Edit Word documents with live preview and track changes via SuperDoc VS Code extension. Use when editing DOCX files, making tracked changes, or redlining contracts._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/docx-processing-superdoc"><img src="assets/badge-docx-processing-superdoc.svg" alt="Word by Superdoc"></a>  
_Search, replace, and read text in Word documents from the command line._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/docx-processing-anthropic"><img src="assets/badge-docx-processing-anthropic.svg" alt="Word by Anthropic"></a>  
_Comprehensive document creation, editing, and analysis with support for tracked changes, comments, formatting preservation, and text extraction._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/docx-processing-openai"><img src="assets/badge-docx-processing-openai.svg" alt="Word by OpenAI"></a>  
_Comprehensive document reading and creation with visual quality control for Word documents._

<div align="center"><img src="assets/entry-separator-light-animated.svg" alt="---"></div>

### Adobe Acrobat

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/pdf-processing-anthropic"><img src="assets/badge-pdf-processing-anthropic.svg" alt="PDF by Anthropic"></a>  
_Comprehensive PDF manipulation, including extracting text and tables, creating new PDFs, merging/splitting documents, and handling forms._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/pdf-processing-openai"><img src="assets/badge-pdf-processing-openai.svg" alt="PDF by OpenAI"></a>  
_Comprehensive PDF reading and creation with visual quality control._

<div align="center"><img src="assets/entry-separator-light-animated.svg" alt="---"></div>

### Vibe-coding

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/security-review-openai"><img src="assets/badge-security-review-openai.svg" alt="Security Review by OpenAI"></a>  
_Perform language and framework specific security best-practice reviews and suggest improvements. Supports Python, JavaScript/TypeScript, and Go with detailed vulnerability reports and fix suggestions._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/vscode-extension-builder-lawvable"><img src="assets/badge-vscode-extension-builder-lawvable.svg" alt="VS Code Extension by Lawvable"></a>  
_Build VS Code extensions from scratch or convert existing JS/React/Vue apps. Supports commands, webviews, custom editors, tree views, and AI agent integration._

<div align="center"><img src="assets/entry-separator-light-animated.svg" alt="---"></div>

<br>
<div align="center"><img src="assets/header-meta-skills.svg" alt="META-SKILLS" height="60"></div>
    
### Skill Authoring

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/skill-creator-anthropic"><img src="assets/badge-skill-creator-anthropic.svg" alt="Self-Creation by Anthropic"></a>  
_Guide for creating effective skills that extend the model's capabilities with specialized knowledge, workflows, or tool integrations._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/skill-creator-openai"><img src="assets/badge-skill-creator-openai.svg" alt="Self-Creation by OpenAI"></a>  
_Guide for creating effective skills that extend the model's capabilities with specialized knowledge, workflows, or tool integrations._

<a href="https://github.com/lawvable/awesome-legal-skills/tree/main/skills/skill-optimizer-lawvable"><img src="assets/badge-skill-optimizer-lawvable.svg" alt="Self-Improvement by Lawvable"></a>  
_Analyze a current work session and propose improvements to skills. Captures learnings automatically after working with a skill._

## Contributing

It's easy! Just click the link below and fill out the form. No Git knowledge required.

<h3 align="center">🚀 <a href="https://github.com/lawvable/awesome-legal-skills/issues/new?template=submit-skill.yml">Submit a new Skill here!</a></h3>

**How we evaluate submissions:** Every resource goes through a manual review before it makes it onto this list. First and foremost, best efforts are made to check for security concerns - no malware, bloatware, or other unwanted risks. Then, we assess whether the skill actually delivers real, practical value to users before it gets listed. See [CONTRIBUTING.md](/CONTRIBUTING.md) for more details.

## Support
Lawvable is the first-ever open hub dedicated to AI agent skills for law - and it's growing every day thanks to the incredible contributors sharing their work and the community showing its support. If you find this list useful, consider giving it a ⭐ - it helps others discover it too.

[![Stargazers over time](https://starchart.cc/lawvable/awesome-legal-skills.svg?variant=adaptive)](https://starchart.cc/lawvable/awesome-legal-skills)

## License

This list is licensed under the [Creative Commons CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/) license. This means you are welcome to fork, clone, copy and redistribute the list, provided you include appropriate attribution; however you are not permitted to distribute any modified versions or use it for commercial purposes. This is to prevent unlawful appropriation of the work of the authors whose resources are listed here. Please note that **all resources included in this list have their own license terms** - if you wish to incorporate those authors' works into your _own_ product, you need to do so according to the terms that _those authors_ have set out.

## Disclaimer

Although we take strong measures to uphold the quality and safety of this list, we take no responsibility or liability for anything bad that might happen as a result of these third-party resources. Make sure the skills you download are aligned with your firm's confidentiality policies and professional responsibility obligations.

## Acknowledgments

This project wouldn't exist without the Anthropic team, who developed the Skills standard and published the examples that got us all started. Huge thanks to every contributor who has shared their work here - you're the reason this list keeps growing. And to everyone who has starred, forked, or simply bookmarked this repo: your support means more than you think. Finally, a hat tip to [@hesreallyhim](https://github.com/hesreallyhim) and his [awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) repo, whose design inspired the look and feel of this one.

```

## File: payload\upgrade_proposal.md
```
# System Upgrade Proposal: CIV_FETCHED_awesome-legal-skills_105805

> [!TIP]
> This actionable proposal was automatically drafted by OA Academy because this repository scored 9/10.

## Application Vision for OmniClaw
EMERGENCY FALLBACK: LLM failed to analyze. However, because this is a CIV-Approved Repo, OA forces assimilation. Please manually review and integrate.

## Next Action Items
1. Review the `DEEP_KNOWLEDGE.md` to understand the architecture.
2. Isolate the target modules identified in the vision.
3. Wrap the modules into an OmniClaw Skill or Agent in `ecosystem/`.

```

## File: payload\_DIR_IDENTITY.md
```
---
id: repo-civ-fetched-awesome-legal-skills-105805
type: skill
owner: OA
registered_at: 2026-04-08T13:33:46.287323
tags: ["auto-cloned", "AI", "Legal", "Skills", "oa-assimilated", "premium-repo"]
---

# CIV_FETCHED_awesome-legal-skills_105805

## Assimilation Report
The repository appears to be related to AI Agent Skills for legal professionals, focusing on creating portable instructions for AI agents to perform specific tasks. It includes badges and links to support community engagement and open adoption of the standard.

## Application for OmniClaw
EMERGENCY FALLBACK: LLM failed to analyze. However, because this is a CIV-Approved Repo, OA forces assimilation. Please manually review and integrate.

```

## File: payload\.claude-plugin\marketplace.json
```
{
  "name": "lawvable",
  "version": "1.0.0",
  "description": "Bundled agent skills for legal work",
  "owner": {
    "name": "Antoine Louis (Lawvable)",
    "email": "antoiloui@gmail.com"
  },
  "plugins": [
    {
      "name": "nda-review-jamie-tso",
      "description": "Guide for reviewing incoming commercial NDAs, producing a clause-by-clause issue log with redlines and rationales",
      "version": "2025.12.30",
      "author": {
        "name": "Jamie Tso"
      },
      "license": "AGPL-3.0",
      "source": "./skills/nda-review-jamie-tso"
    },
    {
      "name": "legal-simulation-patrick-munro",
      "description": "Framework for demonstrating AI capabilities in legal contexts with detailed personas and progressive complexity scenarios",
      "version": "2026.01.12",
      "author": {
        "name": "Patrick Munro"
      },
      "license": "AGPL-3.0",
      "source": "./skills/legal-simulation-patrick-munro"
    },
    {
      "name": "tech-contract-negotiation-patrick-munro",
      "description": "Guide to negotiating technology services agreements with three-position frameworks and concession roadmaps",
      "version": "2026.01.12",
      "author": {
        "name": "Patrick Munro"
      },
      "license": "AGPL-3.0",
      "source": "./skills/tech-contract-negotiation-patrick-munro"
    },
    {
      "name": "vendor-due-diligence-patrick-munro",
      "description": "Framework for assessing IT vendors with structured risk assessments and regulatory checklists (GDPR, DORA, NIS2, SOX)",
      "version": "2026.01.12",
      "author": {
        "name": "Patrick Munro"
      },
      "license": "AGPL-3.0",
      "source": "./skills/vendor-due-diligence-patrick-munro"
    },
    {
      "name": "contract-review-anthropic",
      "description": "Review contracts against your organization's negotiation playbook, flagging deviations and generating redline suggestions",
      "version": "2026.01.30",
      "author": {
        "name": "Anthropic"
      },
      "license": "Apache-2.0",
      "source": "./skills/contract-review-anthropic"
    },
    {
      "name": "compliance-anthropic",
      "description": "Navigate privacy regulations (GDPR, CCPA), review DPAs, and handle data subject requests",
      "version": "2026.01.30",
      "author": {
        "name": "Anthropic"
      },
      "license": "Apache-2.0",
      "source": "./skills/compliance-anthropic"
    },
    {
      "name": "canned-responses-anthropic",
      "description": "Generate templated responses for common legal inquiries and identify when situations require individualized attention",
      "version": "2026.01.30",
      "author": {
        "name": "Anthropic"
      },
      "license": "Apache-2.0",
      "source": "./skills/canned-responses-anthropic"
    },
    {
      "name": "legal-risk-assessment-anthropic",
      "description": "Assess and classify legal risks using a severity-by-likelihood framework with escalation criteria",
      "version": "2026.01.30",
      "author": {
        "name": "Anthropic"
      },
      "license": "Apache-2.0",
      "source": "./skills/legal-risk-assessment-anthropic"
    },
    {
      "name": "meeting-briefing-anthropic",
      "description": "Prepare structured briefings for meetings with legal relevance and track resulting action items",
      "version": "2026.01.30",
      "author": {
        "name": "Anthropic"
      },
      "license": "Apache-2.0",
      "source": "./skills/meeting-briefing-anthropic"
    },
    {
      "name": "nda-triage-anthropic",
      "description": "Screen incoming NDAs and classify them as GREEN, YELLOW, or RED based on risk level",
      "version": "2026.01.30",
      "author": {
        "name": "Anthropic"
      },
      "license": "Apache-2.0",
      "source": "./skills/nda-triage-anthropic"
    },
    {
      "name": "statute-analysis-rafal-fryc",
      "description": "Guide for reading, interpreting, and applying US statutes, regulations, and rules with canons of construction",
      "version": "2026.01.14",
      "author": {
        "name": "Rafał Stanisław Fryc"
      },
      "license": "AGPL-3.0",
      "source": "./skills/statute-analysis-rafal-fryc"
    },
    {
      "name": "gdpr-breach-sentinel-oliver-schmidt-prietz",
      "description": "Incident response and legal compliance guidance for data breaches under GDPR Articles 33 & 34",
      "version": "2026.02.09",
      "author": {
        "name": "Oliver Schmidt-Prietz"
      },
      "license": "AGPL-3.0",
      "source": "./skills/gdpr-breach-sentinel-oliver-schmidt-prietz"
    },
    {
      "name": "dpia-sentinel-oliver-schmidt-prietz",
      "description": "GDPR Data Protection Impact Assessment (DPIA) guidance under Article 35 with multi-jurisdictional blacklist checks",
      "version": "2026.02.10",
      "author": {
        "name": "Oliver Schmidt-Prietz"
      },
      "license": "AGPL-3.0",
      "source": "./skills/dpia-sentinel-oliver-schmidt-prietz"
    },
    {
      "name": "gdpr-privacy-notice-eu-oliver-schmidt-prietz",
      "description": "Draft GDPR-compliant privacy notices as .docx for any EU/EEA jurisdiction and audience",
      "version": "2026.02.09",
      "author": {
        "name": "Oliver Schmidt-Prietz"
      },
      "license": "AGPL-3.0",
      "source": "./skills/gdpr-privacy-notice-eu-oliver-schmidt-prietz"
    },
    {
      "name": "politique-confidentialite-malik-taiar",
      "description": "Guide pour la rédaction de politiques de confidentialité conformes au RGPD avec recommandations CNIL",
      "version": "2025.12.24",
      "author": {
        "name": "Malik Taiar"
      },
      "license": "AGPL-3.0",
      "source": "./skills/politique-confidentialite-malik-taiar"
    },
    {
      "name": "politique-cookies-malik-taiar",
      "description": "Guide pour la rédaction de politiques cookies conformes au RGPD et à la directive ePrivacy",
      "version": "2025.12.24",
      "author": {
        "name": "Malik Taiar"
      },
      "license": "AGPL-3.0",
      "source": "./skills/politique-cookies-malik-taiar"
    },
    {
      "name": "politique-lanceur-alerte-malik-taiar",
      "description": "Guide pour l'évaluation ou la rédaction de politiques lanceur d'alerte conformes à la loi Sapin II",
      "version": "2025.12.31",
      "author": {
        "name": "Malik Taiar"
      },
      "license": "AGPL-3.0",
      "source": "./skills/politique-lanceur-alerte-malik-taiar"
    },
    {
      "name": "notification-licenciement-selim-brihi",
      "description": "Guide pour la rédaction de notifications de licenciement conformes au droit du travail français",
      "version": "2026.01.16",
      "author": {
        "name": "Sélim Brihi"
      },
      "license": "AGPL-3.0",
      "source": "./skills/notification-licenciement-selim-brihi"
    },
    {
      "name": "requete-cph-licenciement-faute-grave-selim-brihi",
      "description": "Guide pour la rédaction de requêtes CPH contestant un licenciement pour faute grave",
      "version": "2026.01.23",
      "author": {
        "name": "Sélim Brihi"
      },
      "license": "AGPL-3.0",
      "source": "./skills/requete-cph-licenciement-faute-grave-selim-brihi"
    },
    {
      "name": "assignation-refere-recouvrement-creance-selim-brihi",
      "description": "Guide pour la rédaction d'assignations en référé pour le recouvrement de créances commerciales",
      "version": "2026.01.23",
      "author": {
        "name": "Sélim Brihi"
      },
      "license": "AGPL-3.0",
      "source": "./skills/assignation-refere-recouvrement-creance-selim-brihi"
    },
    {
      "name": "assignation-refere-communication-associe-selim-brihi",
      "description": "Guide pour la rédaction d'assignations en référé pour la communication de documents sociaux (art. L. 238-1)",
      "version": "2026.01.23",
      "author": {
        "name": "Sélim Brihi"
      },
      "license": "AGPL-3.0",
      "source": "./skills/assignation-refere-communication-associe-selim-brihi"
    },
    {
      "name": "docx-processing-anthropic",
      "description": "Document creation, editing, and analysis with tracked changes and comments support",
      "version": "2025.12.01",
      "author": {
        "name": "Anthropic"
      },
      "source": "./skills/docx-processing-anthropic"
    },
    {
      "name": "docx-processing-openai",
      "description": "Document reading and creation with visual quality control for Word files",
      "version": "2026.01.30",
      "author": {
        "name": "OpenAI"
      },
      "license": "Apache-2.0",
      "source": "./skills/docx-processing-openai"
    },
    {
      "name": "docx-processing-superdoc",
      "description": "Search, replace, and read text in Word documents from the command line",
      "version": "2026.02.02",
      "author": {
        "name": "Superdoc"
      },
      "license": "AGPL-3.0",
      "source": "./skills/docx-processing-superdoc"
    },
    {
      "name": "docx-processing-lawvable",
      "description": "Edit Word documents with live preview and track changes via SuperDoc VS Code extension",
      "version": "2026.02.04",
      "author": {
        "name": "Antoine Louis (Lawvable)"
      },
      "license": "AGPL-3.0",
      "source": "./skills/docx-processing-lawvable"
    },
    {
      "name": "pdf-processing-anthropic",
      "description": "PDF manipulation toolkit for text extraction, creation, merging, and form handling",
      "version": "2025.12.01",
      "author": {
        "name": "Anthropic"
      },
      "source": "./skills/pdf-processing-anthropic"
    },
    {
      "name": "pdf-processing-openai",
      "description": "PDF reading and creation with visual quality control",
      "version": "2026.01.30",
      "author": {
        "name": "OpenAI"
      },
      "license": "Apache-2.0",
      "source": "./skills/pdf-processing-openai"
    },
    {
      "name": "xlsx-processing-anthropic",
      "description": "Spreadsheet creation, editing, and analysis with formulas and data visualization",
      "version": "2025.12.01",
      "author": {
        "name": "Anthropic"
      },
      "source": "./skills/xlsx-processing-anthropic"
    },
    {
      "name": "xlsx-processing-openai",
      "description": "Spreadsheet reading, creation, editing, and analysis with visual quality control",
      "version": "2026.01.30",
      "author": {
        "name": "OpenAI"
      },
      "license": "Apache-2.0",
      "source": "./skills/xlsx-processing-openai"
    },
    {
      "name": "xlsx-processing-manus",
      "description": "Professional Excel spreadsheet creation with a focus on aesthetics and data analysis",
      "version": "2025.12.01",
      "author": {
        "name": "Manus"
      },
      "source": "./skills/xlsx-processing-manus"
    },
    {
      "name": "pptx-processing-anthropic",
      "description": "Presentation creation, editing, and analysis with layouts and speaker notes",
      "version": "2025.12.01",
      "author": {
        "name": "Anthropic"
      },
      "source": "./skills/pptx-processing-anthropic"
    },
    {
      "name": "outlook-emails-lawvable",
      "description": "Read, search, and download emails and attachments from Microsoft Outlook via OAuth2",
      "version": "2026.02.02",
      "author": {
        "name": "Malik Taiar (Lawvable)"
      },
      "license": "AGPL-3.0",
      "source": "./skills/outlook-emails-lawvable"
    },
    {
      "name": "tabular-review-lawvable",
      "description": "Analyze multiple documents against user-defined columns and produce structured Excel output with citations",
      "version": "2026.01.14",
      "author": {
        "name": "Antoine Louis (Lawvable)"
      },
      "license": "AGPL-3.0",
      "source": "./skills/tabular-review-lawvable"
    },
    {
      "name": "vscode-extension-builder-lawvable",
      "description": "Build VS Code extensions from scratch or convert existing JS/React/Vue apps",
      "version": "2026.02.05",
      "author": {
        "name": "Antoine Louis (Lawvable)"
      },
      "license": "AGPL-3.0",
      "source": "./skills/vscode-extension-builder-lawvable"
    },
    {
      "name": "skill-creator-anthropic",
      "description": "Guide for creating effective Agent Skills with specialized knowledge and workflows",
      "version": "2025.12.01",
      "author": {
        "name": "Anthropic"
      },
      "source": "./skills/skill-creator-anthropic"
    },
    {
      "name": "skill-creator-openai",
      "description": "Guide for creating effective Agent Skills with specialized knowledge and workflows",
      "version": "2025.12.18",
      "author": {
        "name": "OpenAI"
      },
      "license": "Apache-2.0",
      "source": "./skills/skill-creator-openai"
    },
    {
      "name": "skill-optimizer-lawvable",
      "description": "Analyze work sessions and propose improvements to skills based on corrections and edge cases",
      "version": "2026.01.07",
      "author": {
        "name": "Malik Taiar (Lawvable)"
      },
      "license": "AGPL-3.0",
      "source": "./skills/skill-optimizer-lawvable"
    },
    {
      "name": "security-review-openai",
      "description": "Perform language and framework specific security best-practice reviews and suggest improvements",
      "version": "2026.02.02",
      "author": {
        "name": "OpenAI"
      },
      "license": "Apache-2.0",
      "source": "./skills/security-review-openai"
    },
    {
      "name": "red-team-verifier-patrick-munro",
      "description": "Adversarial verification for AI-generated legal content with systematic fact-checking, source validation, and quality control",
      "version": "2026.02.17",
      "author": {
        "name": "Patrick Munro"
      },
      "license": "AGPL-3.0",
      "source": "./skills/red-team-verifier-patrick-munro"
    },
    {
      "name": "legal-risk-assessment-zacharie-laik",
      "description": "Legal research and risk evaluation on French and EU law using GoodLegal's tools with adversarial jurisprudence search",
      "version": "2026.02.25",
      "author": {
        "name": "Zacharie Laïk"
      },
      "license": "AGPL-3.0",
      "source": "./skills/legal-risk-assessment-zacharie-laik"
    },
    {
      "name": "mediation-dispute-analysis-jinzhe-tan",
      "description": "Analyze case materials for mediation preparation with BATNA/WATNA analysis and settlement pathways",
      "version": "2026.02.27",
      "author": {
        "name": "Jinzhe Tan"
      },
      "license": "AGPL-3.0",
      "source": "./skills/mediation-dispute-analysis-jinzhe-tan"
    },
    {
      "name": "nil-contract-analysis-samir-patel",
      "description": "NIL contract analysis for NCAA student-athletes with red flag detection and compliance review",
      "version": "2026.03.02",
      "author": {
        "name": "Samir Patel"
      },
      "license": "AGPL-3.0",
      "source": "./skills/nil-contract-analysis-samir-patel"
    }
  ]
}

```

## File: payload\.github\FUNDING.yml
```
# These are supported funding model platforms

github: lawvable
patreon: # Replace with a single Patreon username
open_collective: # Replace with a single Open Collective username
ko_fi: # unsloth
tidelift: # Replace with a single Tidelift platform-name/package-name e.g., npm/babel
community_bridge: # Replace with a single Community Bridge project-name e.g., cloud-foundry
liberapay: # Replace with a single Liberapay username
issuehunt: # Replace with a single IssueHunt username
otechie: # Replace with a single Otechie username
lfx_crowdfunding: # Replace with a single LFX Crowdfunding project-name e.g., cloud-foundry
custom: # Replace with up to 4 custom sponsorship URLs e.g., ['link1', 'link2']

```

## File: payload\.github\ISSUE_TEMPLATE\submit-skill.yml
```
name: 🚀 Submit New Skill
description: Submit a new skill to be featured in the curated list of Lawvable
title: "[Skill]: "
labels: ["skill-submission", "pending-validation"]

body:
  - type: markdown
    attributes:
      value: |
        ## Welcome! 👋

        Thank you for submitting a skill! This form will guide you through the recommendation process.

        **Resource Guidelines:**
        - Ensure that your skill is unique and provides genuine value to users.
        - Only the original author of a skill may submit it - this helps us verify authenticity and ensure proper attribution.
        - Submissions will be closely scrutinized for security and potential risk.

  - type: input
    id: author_name
    attributes:
      label: Author Name
      description: "The author's name, alias, or GitHub username"
      placeholder: "Jane Doe or janedoe"
    validations:
      required: true

  - type: input
    id: author_link
    attributes:
      label: Author Link
      description: "Link to author's GitHub, LinkedIn, or personal website"
      placeholder: "https://github.com/janedoe"
    validations:
      required: true

  - type: input
    id: skill_name
    attributes:
      label: Skill Name
      description: The name of the skill as it will appear in the list
      placeholder: "e.g., nda-review-jane-doe"
    validations:
      required: true

  - type: textarea
    id: skill_file
    attributes:
      label: Skill File
      description: "Drag and drop your .skill file here (or a .zip of the skill folder)"
      placeholder: "Drag your file here..."
    validations:
      required: true

  - type: textarea
    id: skill_description
    attributes:
      label: Description
      description: "A brief description of your skill (1-3 sentences maximum, no emojis) - follow the list's style - be descriptive, not promotional"
      placeholder: "Describe what your skill does and its key features..."
    validations:
      required: true

  - type: dropdown
    id: category
    attributes:
      label: Category
      description: "What type of skill is this?"
      options:
        - Domain (Tackles a specific legal task or workflow)
        - Utility (Powers the tools and formats legal professionals rely on)
        - Meta (Builds, optimizes, or orchestrates other skills)
    validations:
      required: true

  - type: input
    id: jurisdiction
    attributes:
      label: Jurisdiction
      description: "If you selected 'Domain' above, which jurisdiction does this skill target?"
      placeholder: "e.g., France, United States, EU, International"
    validations:
      required: false

  - type: dropdown
    id: license
    attributes:
      label: License
      description: Select the license for your resource (or choose 'Other' to specify)
      options:
        - MIT
        - Apache-2.0
        - GPL-3.0
        - LGPL-3.0
        - AGPL-3.0
        - BSD-2-Clause
        - BSD-3-Clause
        - ISC
        - MPL-2.0
        - Unlicense
        - CC0-1.0
        - CC-BY-4.0
        - CC-BY-SA-4.0
        - CC-BY-NC-4.0
        - CC-BY-NC-ND-4.0
        - All Rights Reserved
        - No License / Not Specified
        - Other (specify below)
    validations:
      required: true

  - type: input
    id: license_other
    attributes:
      label: Other License
      description: If you selected "Other" above, please specify the license
      placeholder: "e.g., BSD-2-Clause, Proprietary"
    validations:
      required: false

  - type: textarea
    id: additional_comments
    attributes:
      label: Additional Comments
      description: "Optional - Any additional information you'd like to share about your skill (not processed during validation)"
      placeholder: "e.g., context about why you created this, special features, acknowledgments, etc."
    validations:
      required: false

  - type: checkboxes
    id: checklist
    attributes:
      label: Recommendation Checklist
      description: Please confirm the following
      options:
        - label: "I have checked that this skill hasn't already been submitted"
          required: true
        - label: My skill provides genuine value to users, and any risks are clearly stated
          required: true
        - label: All provided links are working and publicly accessible
          required: true
        - label: I am submitting only ONE skill in this form
          required: true
        - label: I understand that low-quality or duplicate submissions may be rejected
          required: true

  - type: markdown
    attributes:
      value: |
        ## What happens next?

        1. **Review**: A maintainer will review your submission as soon as possible
        2. **Result**: If approved, your skill will be added to the curated list. Either way, we'll let you know the outcome in the comments of this issue.

        Thank you for contributing to Lawvable! 🎉

```

