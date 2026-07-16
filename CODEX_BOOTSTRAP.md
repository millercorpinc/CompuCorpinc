# Codex Bootstrap Instructions

You are working inside the canonical operating repository for a substantially designed founder-led technology advisory, implementation, security, automation, and managed-governance company.

## Critical framing

This is **not** a blank business-design exercise.

The Startup project has already substantially established:

- The company category and value proposition
- The advisory-led operating model
- Microsoft specialization with vendor-flexible integration
- The core customer range and customer condition
- The service families
- The project-to-recurring revenue architecture
- The delivery lifecycle
- The founder functional responsibilities
- The partner and indirect-distributor model
- The founder-led go-to-market motion
- The structured knowledge strategy

Treat those as the presumptive operating design.

Do not reopen them from first principles unless you find a material contradiction, execution risk, or explicit founder instruction.

Your role is to formalize, operationalize, validate, price, document, and execute the business that has already been designed.

## Required reading

Read in this order:

1. `AGENTS.md`
2. `docs/START-HERE.md`
3. `knowledge/PROJECT-CONTEXT-EXPANDED.md`
4. `knowledge/MASTER-CONTEXT.md`
5. `knowledge/DECISION-STATUS.md`
6. `knowledge/OPEN-QUESTIONS.md`
7. `docs/business/01-BUSINESS-DEFINITION.md`
8. `docs/business/03-SERVICE-ARCHITECTURE.md`
9. `docs/business/05-PARTNERSHIPS-AND-DISTRIBUTION.md`
10. `docs/business/09-OPERATING-MODEL.md`
11. `docs/business/10-PRICING-AND-UNIT-ECONOMICS.md`
12. `docs/architecture/00-ARCHITECTURE-OVERVIEW.md`
13. `docs/launch/00-LAUNCH-PROGRAM.md`
14. `docs/operations/01-90-DAY-LAUNCH-PLAN.md`
15. `ops/launch-backlog.yaml`

Then inspect the relevant service and operations documents.

## Verification

Run:

```bash
python scripts/verify_repository.py
```

Report errors before editing.

Inspect available skills with `/skills`. If upstream Superpowers skills are not present, follow `docs/setup/02-INSTALL-SUPERPOWERS.md`.

## First assignment

Produce a concise operating-readiness assessment that:

1. Confirms the established business baseline without re-brainstorming it.
2. Identifies actual contradictions, missing implementation details, or stale documents.
3. Converts the established baseline into a dependency-aware execution sequence.
4. Identifies only the genuine founder, professional, pricing, partner-selection, and product-selection decisions that remain.
5. Recommends the next three executable work packages.

The default first work packages should be selected from:

- Founder and legal formalization
- Launch-service productization and pricing
- Internal security and operating-stack setup
- Partner/distributor evaluation
- Sales and pilot readiness

## Working method

Use Superpowers brainstorming when a new design decision is genuinely required. Do not use brainstorming merely to reopen settled project context.

For established directions:

1. Confirm the canonical source.
2. Build the operational artifact.
3. Record any material new decision.
4. Update the backlog.
5. Verify the repository.

For genuinely unresolved design work:

1. Use brainstorming.
2. Present alternatives and tradeoffs.
3. Obtain approval.
4. Write the design spec.
5. Use writing-plans.
6. Implement after approval.

## Guardrails

Do not choose or invent:

- Final company name
- Ownership percentages
- Vesting
- Legal or tax structure
- Final pricing
- Final distributor or partner
- Contract language presented as legal advice
- Insurance coverage presented as professional advice
- Support hours or service levels without approval

Do not build a website, application, CRM, or complex knowledge platform before the related business requirement and operating process are approved.

Keep `[COMPANY_NAME]` until the name is approved.

## Session completion

Before claiming completion:

- Run repository verification.
- Update canonical documents.
- Update decision status and open questions when applicable.
- Update `knowledge/WORKING-LOG.md`.
- State what changed, what evidence was used, and what remains unresolved.
