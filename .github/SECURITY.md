# Security Policy

## Supported versions

| Version | Supported |
| ------- | --------- |
| main    | ✅        |

## Reporting a vulnerability

Please **do not** open a public issue for security vulnerabilities.

Email the maintainer directly at the address in the GitHub profile, or use
[GitHub's private vulnerability reporting](https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing/privately-reporting-a-security-vulnerability).

Include:

- A description of the vulnerability
- Steps to reproduce
- Potential impact
- Any suggested mitigations

You will receive an acknowledgement within 72 hours. We aim to release a fix
within 14 days for high-severity issues.

## Scope

This repository contains:

- Shell scripts (`ops/stream/ffmpeg_desktop_record.sh`) – ensure no arbitrary
  command injection is possible when the script is run.
- DOS batch files (`work/C_WORK/MAIL.BAT`) – run only inside a DOSBox-X
  sandbox; not a direct attack surface.
- Documentation and configuration only – no production server code.
