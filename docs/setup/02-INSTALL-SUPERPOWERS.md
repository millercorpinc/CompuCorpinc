# Install Superpowers

## Why

Superpowers provides upstream agent workflows for brainstorming, planning, implementation, testing, debugging, and review.

This repository does not embed an uncontrolled snapshot. It provides scripts that:

1. Clone or update the official upstream repository.
2. Copy all upstream skill directories into `.agents/skills/`.
3. Record the installed commit.
4. Preserve company-specific skills with the `company-` prefix.

## PowerShell

From the repository root:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
./scripts/install-superpowers.ps1
```

Optional pinned ref:

```powershell
./scripts/install-superpowers.ps1 -Ref "<tag-or-commit>"
```

## Bash

```bash
chmod +x scripts/install-superpowers.sh
./scripts/install-superpowers.sh
```

Optional pinned ref:

```bash
./scripts/install-superpowers.sh "<tag-or-commit>"
```

## Verify

Open Codex from the repository root and run:

```text
/skills
```

Confirm that the upstream skills and the `company-*` skills appear.

Then run:

```bash
python scripts/verify_repository.py
```

## Update policy

- Prefer a reviewed tag or commit rather than tracking `main` indefinitely.
- Review upstream release notes before updating.
- Run repository validation after every update.
- Avoid installing the same skills through multiple methods because duplicate names may appear.
- Record the approved version in a decision or dependency update pull request.
