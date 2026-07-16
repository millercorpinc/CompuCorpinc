# Repository Setup

## Create the GitHub repository

Recommended initial settings:

- Private repository
- Descriptive temporary repository name that does not depend on the final company name
- Default branch: `main`
- Require pull requests for `main`
- Require status checks after the verification workflow is active
- Prevent force pushes and branch deletion
- Enable secret scanning and dependency alerts where available
- Restrict administrative access to founders who require it

## Local setup

```bash
git clone <repository-url>
cd <repository>
python scripts/verify_repository.py
```

## First commit sequence

1. Commit the repository foundation.
2. Install Superpowers using the setup instructions.
3. Commit the recorded upstream version only if the team intentionally vendors the copied skill files.
4. Create a branch for founder-governance work.
5. Use the Codex bootstrap instructions.

## Repository naming

Use a neutral working repository name such as:

- `company-operating-system`
- `consulting-business-foundation`
- `technology-firm-architecture`

Rename later after the public name is approved.
