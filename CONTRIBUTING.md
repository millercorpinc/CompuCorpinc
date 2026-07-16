# Contributing

This repository may begin with a small founder group, but changes should still be reviewable and traceable.

## Branches

Use short-lived branches:

- `docs/<topic>`
- `architecture/<topic>`
- `service/<offering>`
- `launch/<workstream>`
- `decision/<topic>`
- `automation/<topic>`

## Pull requests

Every pull request should state:

- The problem or decision addressed
- Documents or capabilities affected
- Assumptions introduced or removed
- Validation performed
- Open questions remaining
- Whether founder approval is required

Use `.github/PULL_REQUEST_TEMPLATE.md`.

## Decisions

Create a decision record when a change establishes or reverses:

- Company name or brand architecture
- Ownership or governance
- Legal/entity structure
- Initial target market
- Service boundaries
- Pricing model
- Partner or distributor commitment
- Material technology platform
- Security standard
- Data handling or retention policy
- Hiring or contractor model

## Reviews

At least one other founder should review material business decisions. Professional matters require appropriate external review.

## Documentation quality

Run:

```bash
python scripts/verify_repository.py
```

before merging.
