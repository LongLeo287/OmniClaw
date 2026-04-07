# Using PM Skills with n8n

n8n is best when you want repeatable PM workflows (not manual copy/paste each time).

If this is your first time here, read [`Using PM Skills 101.md`](Using%20PM%20Skills%20101.md) first.

## Best For

- Weekly recurring PM workflows
- Intake pipelines (requests -> prioritization -> summary)
- Standardizing artifact quality across teams

## 10-Minute Setup

1. Ensure this repo is accessible where n8n runs.
2. Create a simple workflow:
   - Trigger (`Manual Trigger` or `Schedule Trigger`)
   - `Execute Command` node
   - `Slack`/`Email`/`Notion` output node (optional)
3. In `Execute Command`, run:

```bash
./scripts/run-pm.sh skill prioritization-advisor "We have 12 requests and one sprint"
```

4. Confirm output and then switch trigger to schedule.

## Typical PM Automations

- Weekly roadmap triage summary
- Monthly business-health diagnostic
- New feature request intake scoring
- Discovery interview prep checklist generation

## How To Keep Output Quality High

- Keep one workflow for one business job.
- Log inputs and outputs for auditability.
- Add a human approval gate before publishing to stakeholders.

## Common Pitfalls

- One giant workflow that tries to do everything.
- No clear metric for workflow success.
- Shipping AI-generated output directly without review.

## Learn More (Official)

- n8n docs home: [https://docs.n8n.io/](https://docs.n8n.io/)
- n8n quickstart: [https://docs.n8n.io/try-it-out/quickstart/](https://docs.n8n.io/try-it-out/quickstart/)
- Build an AI workflow in n8n: [https://docs.n8n.io/advanced-ai/intro-tutorial/](https://docs.n8n.io/advanced-ai/intro-tutorial/)
- n8n source control and environments: [https://docs.n8n.io/source-control-environments/](https://docs.n8n.io/source-control-environments/)

## PM Skills Links

- Tooling charter context: [`PM Tooling Operations Charter.md`](PM%20Tooling%20Operations%20Charter.md)
- One-page onboarding: [`../START_HERE.md`](../START_HERE.md)
