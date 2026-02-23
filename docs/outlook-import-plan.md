# Outlook Import Plan

Describes the requirements for the external process that exports Outlook
messages into the file-backed inbox.

## Overview

A separate process (not in this repo) reads a user's Outlook mailbox and
writes plain-text `.MSG` files to `work/C_WORK/MAIL/INBOX/` using the schema
defined in [inbox-contract.md](inbox-contract.md).

## Input

- Outlook mailbox access via Microsoft Graph API, MAPI, or `.pst` file.
- Source folder(s) configured by the operator (e.g. `Inbox`, `Tasks`).

## Output

One `.MSG` file per email, written to `work/C_WORK/MAIL/INBOX/`.

Filename format:

```text
YYYYMMDD_HHMMSS_<shortslug>__<ID>.MSG
```

## Importer behaviour

| Requirement         | Detail                                                     |
| ------------------- | ---------------------------------------------------------- |
| Deduplication       | Use Outlook `Message-ID` header (or SHA-256 of headers+body) as the `ID:` field; skip files already present. |
| Sanitise filename   | Lowercase subject → replace non-alphanumeric with `-` → truncate to 30 chars. |
| Preserve body       | Write full plain-text body; strip HTML but keep line breaks. |
| Timestamps          | Use `Date:` header from the original email (UTC).          |
| Attachments         | Out of scope for v1; note in BODY that attachments exist.  |
| Error handling      | On failure, write to `work/C_WORK/MAIL/FAILED/` with an error note. |
| Idempotency         | Running the importer twice must not create duplicate files. |

## Minimal acceptance criteria

1. Dropping a `.MSG` file (manually or via the importer) into
   `work/C_WORK/MAIL/INBOX/` makes it appear in `MAIL LIST` immediately.
2. The `ID:` field matches the Outlook `Message-ID` for deduplication.
3. The `DATE:` field is parseable as `YYYY-MM-DD HH:MM`.
4. The file ends with `END:` on its own line.

## Sample workflow

```text
Outlook Inbox
    │
    ▼
Importer script (Python / PowerShell / etc.)
    │  reads Message-ID, Date, From, To, Subject, Body
    │  sanitises filename
    │  skips if ID already seen
    │
    ▼
work/C_WORK/MAIL/INBOX/YYYYMMDD_HHMMSS_<slug>__<ID>.MSG
    │
    ▼
AI operator sees it on next MAIL LIST
```
