# Runbook

Single source of truth for launching, operating, and maintaining the
dos-ai-operator workstation.

## Prerequisites

| Tool      | Minimum version | Notes                              |
| --------- | --------------- | ---------------------------------- |
| DOSBox-X  | 2024.03.01+     | <https://dosbox-x.com/>            |
| ffmpeg    | 6.0+            | for screen recording               |
| OBS       | 30+             | optional, for streaming            |
| shellcheck| 0.9+            | CI linting of `.sh` files          |

## 1. Launch the workstation

```bash
dosbox-x -conf ops/dosbox/dosbox-x.conf
```

DOSBox-X reads `[autoexec]` from the config, mounts `work/C_WORK` as `C:\WORK`,
and drops you at a `C:\WORK>` prompt.

> **Tip:** On Windows, use backslashes in the mount path or DOSBox-X's
> `%~dp0` expansion. The config uses relative paths (`..\..\work\C_WORK`)
> because DOSBox-X is run from `ops/dosbox/`.

## 2. Mount C:\WORK manually (if needed)

Inside DOSBox-X:

```dos
mount c ../../work/C_WORK
c:
cd \WORK
```

## 3. Check the mail inbox

```dos
MAIL LIST
```

Lists all `.MSG` files in `C:\WORK\MAIL\INBOX\`.

## 4. Inject an email (host side)

Copy or write a `.MSG` file to `work/C_WORK/MAIL/INBOX/`.  
File naming convention:

```text
YYYYMMDD_HHMMSS_<shortslug>__<ID>.MSG
```

Example:

```text
20260222_091400_task-inventory__2026-02-22-001.MSG
```

The file appears in `MAIL LIST` immediately (no restart required).

## 5. Read, reply, archive mail

```dos
MAIL READ   20260222_091400_task-inventory__2026-02-22-001.MSG
MAIL REPLY  20260222_091400_task-inventory__2026-02-22-001.MSG
MAIL ARCHIVE 20260222_091400_task-inventory__2026-02-22-001.MSG
```

See `MAIL HELP` for the full command reference.

## 6. Record the session

### ffmpeg (Linux/X11)

```bash
bash ops/stream/ffmpeg_desktop_record.sh
```

Output is written to `work/captures/dos_session_YYYYMMDD_HHMMSS.mp4`.  
Press `q` in the ffmpeg terminal to stop recording.

### OBS

See `ops/stream/obs_notes.md`.

## 7. CI / linting

```bash
# ShellCheck (requires shellcheck installed)
shellcheck ops/stream/ffmpeg_desktop_record.sh

# Markdown lint (requires markdownlint-cli)
markdownlint "**/*.md" --ignore node_modules
```

Both run automatically in GitHub Actions on every push/PR.

## Troubleshooting

See [troubleshooting.md](troubleshooting.md).
