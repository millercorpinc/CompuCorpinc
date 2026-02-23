# Inbox Contract

Defines the file format and folder layout for the file-backed mail system.

## Folder layout

| Host path                       | DOS path                    | Purpose               |
| ------------------------------- | --------------------------- | --------------------- |
| `work/C_WORK/MAIL/INBOX/`       | `C:\WORK\MAIL\INBOX\`       | Incoming messages     |
| `work/C_WORK/MAIL/OUTBOX/`      | `C:\WORK\MAIL\OUTBOX\`      | AI-drafted replies    |
| `work/C_WORK/MAIL/SENT/`        | `C:\WORK\MAIL\SENT\`        | Sent mail archive     |
| `work/C_WORK/MAIL/ARCHIVE/`     | `C:\WORK\MAIL\ARCHIVE\`     | Processed originals   |
| `work/C_WORK/MAIL/FAILED/`      | `C:\WORK\MAIL\FAILED\`      | Undeliverable mail    |
| `work/C_WORK/MAIL/LEDGER/`      | `C:\WORK\MAIL\LEDGER\`      | Processing log        |

## File extension

All mail files use the `.MSG` extension.

## Filename convention

```text
YYYYMMDD_HHMMSS_<shortslug>__<ID>.MSG
```

- `YYYYMMDD_HHMMSS` – timestamp of the original message (UTC).
- `<shortslug>` – sanitised subject, lowercase, hyphens only, max 30 chars.
- `<ID>` – unique message ID (from `Message-ID` header or exporter hash).

Example:

```text
20260222_091400_task-inventory__2026-02-22-001.MSG
```

## File format

Plain ASCII / UTF-8 text. The file is structured as follows:

```text
ID: <unique-message-id>
FROM: <sender@example.com>
TO: <recipient@example.com>
DATE: YYYY-MM-DD HH:MM
SUBJECT: <subject line>

BODY:
<free text, may include bullet points, blank lines>

DELIVERABLES:
- C:\WORK\ARTIFACTS\<filename>

DEFINITION_OF_DONE:
- <acceptance criterion>

END:
```

### Field rules

| Field              | Required | Notes                                      |
| ------------------ | -------- | ------------------------------------------ |
| `ID:`              | Yes      | Unique; used for deduplication             |
| `FROM:`            | Yes      | Sender email address                       |
| `TO:`              | Yes      | Recipient email address                    |
| `DATE:`            | Yes      | `YYYY-MM-DD HH:MM` format                  |
| `SUBJECT:`         | Yes      | Plain text; ≤ 78 chars recommended         |
| `BODY:`            | Yes      | Free text after the blank line             |
| `DELIVERABLES:`    | No       | List of expected output file paths         |
| `DEFINITION_OF_DONE:` | No    | Acceptance criteria                        |
| `END:`             | Yes      | Marks the end of the message               |

## Sample message

```text
ID: 2026-02-22-001
FROM: boss@company.com
TO: aiworker@company.com
DATE: 2026-02-22 09:14
SUBJECT: TASK: Inventory the WORK drive

BODY:
Please produce a complete inventory of the C:\WORK directory tree.
Include file counts and sizes by subdirectory.

DELIVERABLES:
- C:\WORK\ARTIFACTS\inventory.txt

DEFINITION_OF_DONE:
- inventory.txt exists and includes file counts + sizes by directory.

END:
```

## Ledger format

`C:\WORK\MAIL\LEDGER\PROCESSED.LOG` is an append-only plain-text log:

```text
YYYYMMDD HH:MM  PROCESSED  <filename>  <one-line status>
```

Example:

```text
20260222 10:47  PROCESSED  20260222_091400_task-inventory__2026-02-22-001.MSG  OK
```
