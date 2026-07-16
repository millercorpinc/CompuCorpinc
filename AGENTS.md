# AGENTS.md

## Mission

Maintain this repository as the canonical, auditable operating system for **[COMPANY_NAME]**, a founder-led technology advisory, implementation, automation, security, and managed-governance company.

The company name is provisional. Never replace `[COMPANY_NAME]` globally until a formal decision record approves the legal and public names.

## Mandatory reading order

Before substantive work:

1. `docs/START-HERE.md`
2. `knowledge/MASTER-CONTEXT.md`
3. `knowledge/DECISION-STATUS.md`
4. The most relevant canonical documents under `docs/`
5. Relevant decision records under `docs/decisions/`
6. Relevant templates and skills

For a narrowly scoped task, do not read every file. Follow links from `docs/START-HERE.md` and load only the necessary context.

## Source boundary

The initial knowledge base is reconstructed only from the Startup project discussions available when this repository was created. It is a synthesis, not a verbatim transcript.

When adding new information:

- Identify whether it came from a founder decision, research, customer evidence, professional advice, or an assumption.
- Add provenance in the document's `Source and status` section.
- Never invent prior agreement.
- Never describe an open decision as settled.
- Preserve competing options until a decision is approved.

## Working method

Use relevant skills before acting.

For creative or design work:

1. Use the upstream Superpowers brainstorming workflow.
2. Identify the business decision or artifact being designed.
3. Propose alternatives and tradeoffs.
4. Obtain explicit approval before treating a design as canonical.
5. Record approved decisions.
6. Update affected canonical documents.
7. Run repository verification.

For implementation work:

1. Write or update a design/specification.
2. Produce a dependency-aware plan.
3. Work in small reviewable changes.
4. Test or validate before claiming completion.
5. Update documentation in the same change.

## Business invariants

Unless a decision record explicitly changes them:

- The company is advisory-led rather than help-desk-led.
- Microsoft is the principal platform specialization, not the only supported ecosystem.
- The company integrates and governs customer business systems rather than forcing every process into one vendor.
- Projects establish standards; recurring governance creates durable revenue.
- Security, documentation, maintainability, and operational ownership are built into delivery.
- Partner, distributor, referral, and independent-attestation relationships are part of the operating model.
- Licensing margin is supplemental; professional services and recurring accountability are the main value.
- Formal audits, legal advice, tax advice, and regulated attestations must be performed by qualified independent professionals where required.
- The company should productize repeatable work without pretending all clients are identical.
- Senior judgment is a core product and must not be buried beneath commodity support.

## Documentation rules

- Prefer one canonical home for each fact.
- Link to canonical content instead of duplicating long passages.
- When duplication is useful, label the canonical source.
- Use plain language and define specialized terms.
- Include scope, exclusions, assumptions, risks, owner, status, and next review date where relevant.
- Store approved decisions in `docs/decisions/`.
- Store unresolved questions in `knowledge/OPEN-QUESTIONS.md`.
- Store historical material under `knowledge/history/`.
- Do not delete historical concepts merely because they are no longer preferred; mark them superseded.

## Architecture rules

Model the company through connected layers:

1. Strategy and value proposition
2. Capabilities and value streams
3. Services and commercial packages
4. People, roles, partners, and governance
5. Processes and delivery lifecycle
6. Information and knowledge
7. Applications and integrations
8. Technology and security
9. Metrics, controls, and evidence

Every significant technology choice should trace to a business capability or operational requirement.

## Security and confidentiality

Assume this repository contains confidential business strategy.

- Never commit customer secrets, credentials, tokens, private keys, regulated data, or production exports.
- Use examples and synthetic data in templates.
- Keep secrets in approved secret-management systems.
- Flag any proposed workflow that would mix customer data without appropriate separation.
- Apply least privilege and auditable change control.
- Do not present this repository as legal, tax, accounting, or audit advice.

## Change completion criteria

A change is complete only when:

- The requested artifact exists and is internally coherent.
- Relevant links and indexes are updated.
- A decision record exists for newly settled material decisions.
- Open questions are updated.
- Validation passes.
- No temporary placeholders remain except intentionally approved placeholders such as `[COMPANY_NAME]`.
- The summary states what changed, what remains open, and which source assumptions were used.
