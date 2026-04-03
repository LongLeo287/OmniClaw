---
id: github.com-everyinc-charlie-cfo-skill-88ce30d6-kno
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:46.635842
---

# KNOWLEDGE EXTRACT: github.com_EveryInc_charlie-cfo-skill_88ce30d6
> **Extracted on:** 2026-04-01 10:26:57
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007520875/github.com_EveryInc_charlie-cfo-skill_88ce30d6

---

## File: `LICENSE`
```
MIT License

Copyright (c) 2026 Every

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
# Charlie CFO Skill

A Claude Code skill for bootstrapped CFO financial management.

Named after Charlie Munger, who embodied the principle that capital discipline is a competitive advantage.

## What It Does

Charlie provides financial frameworks for bootstrapped, high-growth startups:

- **Cash management** — Runway calculations, reserve structures, burn analysis
- **Unit economics** — LTV:CAC ratios, CAC payback, gross margin targets
- **Capital allocation** — Hiring ROI, Rule of 40, investment payback periods
- **Working capital** — Cash conversion cycle, AR/AP optimization, prepay strategies
- **Forecasting** — Driver-based planning, scenario modeling, 13-week cash flow

## Installation

```bash
npx skills add EveryInc/charlie-cfo-skill
```

## Usage

Once installed, Charlie activates automatically when you ask financial questions:

- "Should we make this hire?"
- "How much runway do we need?"
- "What metrics should I track?"
- "How do I forecast revenue?"
- "What's a healthy LTV:CAC ratio?"

## Philosophy

**Profit is a constraint, not a goal.** Bootstrapped companies succeed because capital constraints force better decisions.

Key principles:
- Unit economics are survival requirements, not nice-to-haves
- Revenue per employee matters more than headcount
- Runway targets: 24-36 months minimum
- Every investment needs a <12 month payback period

## References

The skill includes detailed reference docs:

- `references/metrics-benchmarks.md` — Formulas and industry benchmarks
- `references/case-studies.md` — Examples from Mailchimp, Zapier, Basecamp, ConvertKit, Zoho

## About Every

Every is the only subscription you need to stay at the edge of AI—ideas, apps, and training all in one bundle.

Start your free trial: https://every.to/subscribe

## License

MIT
```

## File: `SKILL.md`
```markdown
---
name: charlie
description: Your AI CFO for bootstrapped startups, named after Charlie Munger who embodied the principle that capital discipline is a competitive advantage. Provides financial frameworks for cash management, runway calculations, unit economics (LTV:CAC), capital allocation, hiring ROI, burn rate analysis, working capital optimization, and forecasting. Use for questions like "should we make this hire?", "how much runway do we need?", "what metrics should I track?", "how do I forecast revenue?", or any strategic financial decision at a self-funded company.
---

# Charlie CFO: Bootstrapped Financial Management

Your AI CFO for bootstrapped, profitable companies. Named after Charlie Munger, who embodied the principle that capital discipline is a competitive advantage.

## Core Mental Models

**Profit is a constraint, not a goal.** Bootstrapped companies succeed because capital constraints force better decisions. Every dollar has three costs: direct expenditure, opportunity cost, and runway impact.

**Unit economics are survival requirements:**

- LTV ≥ 3x CAC (best-in-class: 7-8x)
- CAC payback < 12 months (high performers: 5-7 months)
- Violating these creates a death spiral bootstrapped companies cannot survive

**Revenue per employee is your efficiency scorecard:**

- $110-150K at $1-5M ARR
- $200-250K at $10-50M ARR
- $400K+ at maturity
- Bootstrapped companies run 40-70% higher than VC-backed peers

## Cash Management Rules

**Runway targets:**

- Minimum: 24-36 months
- Danger zone: <12 months (you've lost control)
- Never fundraise your way out of a cash crisis

**Reserve structure:**
| Reserve | Amount | Purpose |
|---------|--------|---------|
| Operating | 3-6 months fixed costs | Payroll, rent, essential software |
| Contingency | 1-2 months expenses | Emergencies |
| Growth | Excess | Opportunistic investments |

**Burn multiple** = Net Burn ÷ Net New ARR

- <1x: Excellent
- 1-1.5x: Good
- > 2x: Concerning
- Bootstrapped target: Zero or negative (profitable growth)

## Capital Allocation Framework

**Every investment question:** What is the payback period? Target <12 months.

**Rule of 40:** Revenue Growth % + EBITDA Margin % ≥ 40%

- High growth path: 40% + 0%
- Balanced path: 20% + 20%
- Profit path: 10% + 30%

**Hiring decisions:**

1. Will this hire directly contribute to revenue?
2. What's the time-to-productivity? (Factor into ROI)
3. What else could this salary fund?
4. Does this make existing team more productive?

**Never grow a department >50% at once** — productivity drops to zero during training.

## Working Capital Optimization

**Cash Conversion Cycle (CCC):** DIO + DSO - DPO

- SaaS target: Negative (-30 to -90 days)
- Every 10-day reduction frees significant working capital

**AR discipline:** Target 30-45 days DSO

- Reminder 7 days before due
- Follow up Day 1, 7, 14, 30 past due

**AP strategy:** Pay on due date, not early, unless discount > cost of capital

- 2% discount for 20 days early = 36.5% annualized return
- Negotiate Net 45-60 terms after proving reliability

**Annual prepay:** Offer 15-20% discount

- Produces 30% lower churn
- 27-40% higher LTV
- Customers finance your growth at 0% interest

## Financial Review Rhythms

**Weekly (60-90 min):**

- Cash position
- AR aging
- Pipeline movement
- Revenue/bookings

**Monthly:**

- Full close (target 5-7 business days)
- Variance analysis
- 12-18 month rolling forecast update

**Quarterly:**

- Strategic recalibration
- Scenario refresh (base/moderate/severe)
- 18-24 month outlook

## Key Metrics Dashboard

| Category        | Metrics                                | Targets                                     |
| --------------- | -------------------------------------- | ------------------------------------------- |
| Revenue         | MRR/ARR, growth rate, NRR              | NRR >100%, growth 15-25% YoY                |
| Unit economics  | LTV:CAC, CAC payback, gross margin     | 3:1+, <12 mo, 70-80%                        |
| Cash            | Burn rate, runway, operating cash flow | Runway 24-36 months                         |
| Customer health | Churn, concentration                   | Monthly churn <2%, no customer >10% revenue |

**Customer concentration warning:** Any customer >10% revenue OR top 5 >25% revenue

## Forecasting Approach

Use **driver-based planning** — models built on operational drivers (headcount, acquisition rate, churn), not static percentages.

**MRR buildup model:**

```
Starting MRR + New Bookings + Expansion - Churn = Ending MRR
```

**13-week cash flow forecast:**

- Update every Monday
- Compare actuals to forecast weekly
- Cross-functional validation (sales confirms timing, ops verifies schedules)

**Always maintain three scenarios:**

- Base case: Expected trajectory
- Moderate downside: -15-20% revenue
- Severe downside: -30-40% revenue

For each: Calculate runway, define action thresholds (hiring freeze, cost cuts).

## Spending Benchmarks ($3-5M ARR)

- Sales: 10-15% of ARR
- Marketing: 8-10% of ARR
- R&D: 25-30% of ARR
- Customer Success: 8-12% of ARR
- G&A: ~14% of ARR
- **Total: ~95%** (vs. 107% for VC-backed)

---

## References

- See [references/metrics-benchmarks.md](references/metrics-benchmarks.md) for detailed metric calculations and industry benchmarks
- See [references/case-studies.md](../../../vault/archives/archive_legacy/affitor-affiliate-skills/shared/references/case-studies.md) for examples from Mailchimp, Zapier, Basecamp, ConvertKit, and Zoho
```

## File: `references/case-studies.md`
```markdown
# Bootstrapped Excellence: Case Studies

## Mailchimp — $12B Exit on Zero Funding

**Timeline:** 2001-2021 (20 years bootstrapped)
**Exit:** Acquired by Intuit for $12B
**Final ARR:** $800M

### Key Financial Decisions

**Freemium pivot (2009):** Launched free tier when company was already profitable
- Users grew from 85,000 to 450,000 in one year
- Profit increased 650% simultaneously
- Viral "Chimp" logo on free emails drove organic growth

**CAC efficiency:** Achieved CAC under $100 through:
- Product-led growth (free tier as acquisition)
- Viral loops (branding on sent emails)
- Content marketing over paid acquisition

**Capital discipline:** Never raised external capital despite numerous offers
- Co-founder Ben Chestnut: "I didn't want to take orders from some nerdy MBA VC"
- Maintained full ownership through exit

### Lessons
- Freemium can increase profits if unit economics are strong
- Product virality beats paid acquisition
- Patience compounds (20 years to $12B)

---

## Zapier — $5B Valuation on $1.4M Raised

**Funding:** $1.4M seed round (2012), treated as last round ever
**Valuation:** $5B (2021)
**ARR:** $310M+

### Key Financial Decisions

**Profitability first:** Reached profitability in 2014, maintained since
- 10% monthly revenue growth for 48+ consecutive months
- Never burned through seed round

**Near-zero CAC strategy:**
- Programmatic SEO: Auto-generated landing pages for every integration
- 50% of traffic from search
- Content compounds while paid ads don't

**"Hire when it hurts" philosophy:**
- Kept team extremely lean during growth phase
- Each hire had to prove necessity through pain
- Remote-first reduced overhead

### Lessons
- SEO at scale can replace paid acquisition entirely
- Treating seed as final round forces discipline
- Revenue per employee matters more than headcount

---

## Basecamp (37signals) — 25+ Years Profitable

**Founded:** 1999
**Revenue:** ~$100M ARR
**Employees:** ~70
**Funding:** Zero external capital

### Key Financial Decisions

**Annual profit distributions:**
- Take profit off table annually rather than endlessly reinvesting
- Reduces risk with each distribution
- "Companies that continuously reinvest everything keep adding risk"

**Revenue per employee:** ~$1.4M
- Among highest in software industry
- Proves lean teams can build massive value

**Product focus (2014):** Shut down 3 of 4 products
- Chose focus over diversification
- Counterintuitive but increased profitability

**Compensation philosophy:**
- Pay top-of-market for location-independent roles
- No equity, strong salaries + profit sharing
- Reduces pressure to exit

### Lessons
- Profit distributions reduce risk over time
- Focus beats diversification
- High RPE is achievable with discipline

---

## ConvertKit — 51% Margin Turnaround in 5 Months

**Founder:** Nathan Barry
**ARR:** ~$30M
**Funding:** Bootstrapped

### Key Financial Decisions

**Crisis response:** When rapid growth nearly depleted cash:
1. Aggressive cost cuts across all departments
2. Renegotiated vendor contracts
3. Doubled down on direct sales (higher margin)
4. Operational efficiency improvements

**Result:** 51% profit margin achieved in 5 months

**Profit distribution model:**
- 40% to owners
- 52% to team profit sharing
- 8% leadership bonuses

Creates alignment without equity dilution.

### Lessons
- Turnarounds can happen fast with decisive action
- Profit sharing aligns team without giving up ownership
- Direct sales often higher margin than product-led

---

## Zoho — $1B+ Revenue, Zero Investment

**Founded:** 1996
**Revenue:** $1B+ (estimated)
**Products:** 55+ integrated SaaS applications
**Users:** 100M+
**Funding:** Zero external capital

### Key Financial Decisions

**R&D investment:** 60% of revenue into R&D
- 3.5x industry average
- Builds long-term moat through product breadth

**Cost structure arbitrage:**
- R&D centers in rural India
- Lower costs while investing in communities
- Sustainable talent pipeline

**Zero advertising:** All growth from:
- Content marketing
- Word of mouth
- Product-led growth

**Vertical integration:** Built own email, CRM, accounting, HR, etc.
- Reduces dependency on third parties
- Higher margins over time

### Lessons
- Massive R&D investment sustainable when bootstrapped
- Geographic arbitrage for sustainable cost advantage
- Product breadth can be moat (vs. VC advice to focus)

---

## Common Patterns Across All Cases

1. **Profitability is a choice, not a destination**
   - All achieved profitability early and maintained it
   - Profit constraints forced better decisions

2. **CAC efficiency through product, not paid acquisition**
   - Freemium, SEO, virality, word of mouth
   - Paid acquisition as accelerant, not foundation

3. **Extreme revenue per employee**
   - All run 2-3x industry average RPE
   - Small teams forced to be productive

4. **Long time horizons**
   - Mailchimp: 20 years
   - Basecamp: 25+ years
   - Zoho: 28+ years
   - Patience enables compounding

5. **Profit distribution, not endless reinvestment**
   - Taking risk off the table each year
   - Creates optionality and resilience
```

## File: `references/metrics-benchmarks.md`
```markdown
# Metrics & Benchmarks Reference

## Unit Economics Calculations

### LTV (Lifetime Value)
```
LTV = (ARPU × Gross Margin) / Monthly Churn Rate
```
Or for cohort-based:
```
LTV = Sum of (Monthly Revenue × Retention Rate) over customer lifetime
```

### CAC (Customer Acquisition Cost)
```
CAC = (Sales + Marketing Spend) / New Customers Acquired
```
Include: salaries, commissions, advertising, tools, events, content production

### CAC Payback Period
```
CAC Payback (months) = CAC / (Monthly ARPU × Gross Margin)
```

### LTV:CAC Ratio
| Ratio | Interpretation |
|-------|----------------|
| <1:1 | Losing money on every customer |
| 1-2:1 | Unsustainable, need to improve |
| 3:1 | Healthy minimum threshold |
| 5:1+ | Excellent, may be underinvesting in growth |
| 7-8:1 | Best-in-class |

## SaaS Metrics Benchmarks

### Churn Rates by Segment
| Segment | Monthly Churn | Annual Churn |
|---------|---------------|--------------|
| SMB | 3-5% | 30-50% |
| Mid-Market | 1-2% | 10-20% |
| Enterprise | 0.5-1% | 5-10% |
| Best-in-class | <1% monthly | <10% annual |

### Net Revenue Retention (NRR)
```
NRR = (Starting MRR + Expansion - Churn - Contraction) / Starting MRR
```
| NRR | Interpretation |
|-----|----------------|
| <90% | Leaky bucket, growth unsustainable |
| 90-100% | Acceptable, but limited expansion |
| 100-110% | Good, expansion offsetting churn |
| 110-130% | Excellent |
| >130% | World-class (Snowflake, Twilio territory) |

### Gross Margin Targets
| Business Type | Target Gross Margin |
|---------------|---------------------|
| Pure SaaS | 75-85% |
| SaaS + Services | 60-70% |
| Marketplace | 40-60% |
| Hardware + Software | 30-50% |

## Cash Flow Metrics

### Runway Calculation
```
Runway (months) = Cash Balance / Monthly Burn Rate
```
Use trailing 3-month average burn for accuracy.

### Burn Multiple
```
Burn Multiple = Net Burn / Net New ARR
```
| Multiple | Rating |
|----------|--------|
| <1x | Excellent efficiency |
| 1-1.5x | Good |
| 1.5-2x | Concerning |
| >2x | Inefficient, requires correction |

### Cash Conversion Score
```
CCS = (Cash from Operations / Net Income) × 100
```
Target: >100% (generating more cash than accounting profit)

## Revenue Efficiency

### Magic Number (Sales Efficiency)
```
Magic Number = (QoQ ARR Growth) / (Prior Quarter S&M Spend)
```
| Score | Interpretation |
|-------|----------------|
| <0.5 | Inefficient, reduce spend or improve conversion |
| 0.5-0.75 | Acceptable |
| 0.75-1.0 | Good |
| >1.0 | Excellent, consider increasing investment |

### Revenue per Employee
| ARR Stage | Target RPE |
|-----------|------------|
| $1-5M | $110-150K |
| $5-10M | $150-200K |
| $10-50M | $200-250K |
| $50M+ | $300-400K+ |

Bootstrapped companies typically achieve 40-70% higher RPE than VC-backed at same stage.

## Working Capital Metrics

### Days Sales Outstanding (DSO)
```
DSO = (Accounts Receivable / Total Credit Sales) × Days in Period
```
| DSO | Rating |
|-----|--------|
| <30 days | Excellent |
| 30-45 days | Good |
| 45-60 days | Needs attention |
| >60 days | Problem requiring immediate action |

### Days Payable Outstanding (DPO)
```
DPO = (Accounts Payable / COGS) × Days in Period
```
Target: Negotiate highest DPO possible while maintaining vendor relationships

### Cash Conversion Cycle
```
CCC = DIO + DSO - DPO
```
(DIO = Days Inventory Outstanding, typically 0 for SaaS)

SaaS with annual prepay can achieve CCC of -30 to -90 days.

## Spending Benchmarks by ARR

### $1-3M ARR (Early Stage)
| Category | % of ARR |
|----------|----------|
| Sales | 15-20% |
| Marketing | 10-15% |
| R&D | 30-40% |
| Customer Success | 10-15% |
| G&A | 15-20% |

### $3-10M ARR (Growth Stage)
| Category | % of ARR |
|----------|----------|
| Sales | 10-15% |
| Marketing | 8-12% |
| R&D | 25-30% |
| Customer Success | 8-12% |
| G&A | 12-15% |

### $10M+ ARR (Scale Stage)
| Category | % of ARR |
|----------|----------|
| Sales | 8-12% |
| Marketing | 6-10% |
| R&D | 20-25% |
| Customer Success | 6-10% |
| G&A | 10-12% |

## Rule of 40 Scenarios

| Growth Rate | Required Margin | Example |
|-------------|-----------------|---------|
| 50% | -10% (can burn) | Hypergrowth mode |
| 40% | 0% | Breakeven growth |
| 30% | 10% | Balanced |
| 20% | 20% | Profitable growth |
| 10% | 30% | Mature, profitable |
| 0% | 40% | Cash cow |

Median SaaS: 34% (most don't hit 40)
Top quartile bootstrapped: 50%+

## Forecast Accuracy Metrics

### MAPE (Mean Absolute Percentage Error)
```
MAPE = (1/n) × Σ |Actual - Forecast| / |Actual| × 100
```
| MAPE | Rating |
|------|--------|
| <5% | Excellent |
| 5-10% | Good |
| 10-20% | Acceptable |
| >20% | Needs improvement |

Track separately for:
- Revenue (target 5-10% MAPE)
- Expenses (target 10-15% MAPE)
- Cash flow (target 10-15% MAPE)
```

