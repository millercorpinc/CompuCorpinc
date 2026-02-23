# Architecture

## Overview

```text
┌─────────────────────────────────────────────────────────────────┐
│  Host machine                                                   │
│                                                                 │
│  ┌──────────────┐   mount C:\WORK   ┌───────────────────────┐  │
│  │ work/C_WORK/ │ ◄────────────────► │  DOSBox-X process     │  │
│  │  MAIL/       │                   │  (FreeDOS shell)       │  │
│  │  JOURNAL/    │                   │                        │  │
│  │  ARTIFACTS/  │                   │  AI operator types     │  │
│  │  NOTES/      │                   │  commands at human     │  │
│  └──────┬───────┘                   │  pace via agent        │  │
│         │                           │  controller            │  │
│  ┌──────▼───────┐                   └────────────────────────┘  │
│  │  Outlook     │                                               │
│  │  importer    │  writes .MSG files → MAIL/INBOX/              │
│  │  (external)  │                                               │
│  └──────────────┘                                               │
│                                                                 │
│  ┌──────────────┐                                               │
│  │  OBS / ffmpeg│  captures DOSBox-X window → recordings        │
│  └──────────────┘                                               │
└─────────────────────────────────────────────────────────────────┘
```

## Components

### DOSBox-X workstation

- Config: `ops/dosbox/dosbox-x.conf`
- Autoexec: `ops/dosbox/autoexec.bat` (embedded in config)
- Mounts `work/C_WORK` as `C:\WORK` at startup.

### File-backed mail system

- **No real mail server.** Mail is plain-text `.MSG` files.
- The host drops files into `work/C_WORK/MAIL/INBOX/`.
- The AI operator uses `MAIL.BAT` to list, read, reply, and archive.
- See [inbox-contract.md](inbox-contract.md) for the file schema.

### AI operator

- Controlled by an external agent controller (not in this repo).
- Reads its "constitution" from `agent/operator_prompt.txt`.
- Types at human pace according to `agent/pacing_profile.json`.
- See [realism.md](realism.md) for behaviour rules.

### Live capture

- OBS window capture or ffmpeg x11grab records the DOSBox-X window.
- See `ops/stream/` for details.

## Data flow

```text
Outlook export → .MSG file → work/C_WORK/MAIL/INBOX/
                                     │
                             DOSBox-X sees C:\WORK\MAIL\INBOX\
                                     │
                          AI: MAIL LIST → MAIL READ → work → MAIL REPLY → MAIL ARCHIVE
                                     │
                             OUTBOX/ holds reply until picked up
                             SENT/   holds permanent sent copy
                             ARCHIVE/ holds processed originals
```
