# Codex Bootstrap Instructions

Use this prompt after opening the repository in Codex.

---

You are helping establish the canonical operating repository for a new technology consulting and managed-governance company.

First, read and follow `AGENTS.md`. Then read:

1. `docs/START-HERE.md`
2. `knowledge/MASTER-CONTEXT.md`
3. `knowledge/DECISION-STATUS.md`
4. `docs/launch/00-LAUNCH-PROGRAM.md`
5. `docs/architecture/00-ARCHITECTURE-OVERVIEW.md`

Before editing anything:

- Confirm that the upstream Superpowers skills are available with `/skills`.
- If they are not available, follow `docs/setup/02-INSTALL-SUPERPOWERS.md`.
- Run `python scripts/verify_repository.py`.
- Summarize the current business model, repository structure, confirmed decisions, and the five most important open decisions.
- Do not choose a company name.
- Do not assume ownership percentages, legal structure, final pricing, or a final distributor.
- Treat all professional legal, tax, audit, and insurance requirements as items for qualified review.

Then use the brainstorming skill to design the first execution phase. The initial phase should make the repository operational before producing a website or application. It should prioritize:

1. Founder and ownership decisions
2. Legal/entity setup workstream
3. Initial service package and pricing hypotheses
4. Partner and distributor strategy
5. Internal operating stack and security baseline
6. First-client acquisition and pilot-delivery readiness
7. Repository governance and issue backlog

Present the proposed design in reviewable sections. After approval, create a written design under `docs/superpowers/specs/`, then use the writing-plans skill to create a task-level implementation plan. Do not begin implementation until the design is approved.

When implementing:

- Create or update GitHub issues from `ops/launch-backlog.yaml`.
- Use the templates under `templates/`.
- Record material decisions in `docs/decisions/`.
- Keep canonical documents synchronized.
- Run repository verification before completion.
- End each work session by updating `knowledge/WORKING-LOG.md` with a concise factual summary and next actions.
