# Cyber Risk and Buying Triggers

## Source and status

- **Status:** current threat/risk research mapped to commercial hypotheses
- **Date:** 2026-08-19
- **Boundary:** risk evidence supports prioritization and offer design; it does not prove that a prospect will buy.

## Why cyber risk matters commercially

The company's best market is not simply “businesses that could be hacked.” That includes nearly every modern business.

The useful market is organizations where:

1. ordinary cloud/email/device weaknesses can create a large business consequence;
2. the organization lacks senior security/technology ownership;
3. a buyer can understand the consequence; and
4. a trigger converts abstract risk into a funded project.

## Current national threat signal

The FBI's 2025 Internet Crime Report combined more than **1 million complaints** and reported losses exceeding **$20 billion**. The FBI separately said cyber-enabled fraud complaints were approximately 453,000 with more than $17.7 billion in reported losses.

Sources:

- FBI, *2025 Internet Crime Report*: https://www.fbi.gov/file-repository/2025_ic3report.pdf/view
- FBI 2026 release: https://www.fbi.gov/news/press-releases/cryptocurrency-and-ai-scams-bilk-americans-of-billions

These values are reported complaints/losses, not a complete estimate of all cybercrime and not small-business-only statistics.

## Business email compromise is particularly relevant to the target market

The FBI defines BEC around compromised/spoofed business communications and payment instructions. Its current examples include a homebuyer receiving fake title-company wire instructions and businesses receiving fraudulent payment requests.

FBI recommended defenses include:

- MFA;
- independently verifying changes to account/payment procedures;
- checking addresses/domains carefully;
- resisting urgency; and
- verifying payment requests through a known channel.

Source: https://www.fbi.gov/how-we-can-help-you/scams-and-safety/common-frauds-and-scams/business-email-compromise

### Why this fits small professional firms

BEC turns ordinary systems—email, identity, invoicing, vendor records, and payment processes—into direct financial risk.

That makes the risk concrete for:

- law firms;
- real estate;
- construction;
- accounting;
- finance/insurance;
- property management;
- professional services with vendor payments.

It also creates an offer that combines **technology controls and operating procedure**, which fits the company's advisory-led positioning better than selling endpoint software alone.

## Ransomware and resilience

CISA says cyber incidents have surged among small businesses that often lack resources to defend against ransomware and other attacks.

Its small-business resources emphasize:

- phishing resistance;
- strong passwords;
- MFA;
- software updates;
- logging;
- backups; and
- encryption.

CISA also provides SCuBA tools for assessing and hardening SaaS/cloud configurations.

Source: https://www.cisa.gov/small-and-medium-sized-business-resources

CISA's StopRansomware guidance specifically recommends maintaining **offline, encrypted backups** and regularly testing backup availability/integrity because ransomware may attempt to encrypt or delete accessible backups.

Source: https://www.cisa.gov/stopransomware/ransomware-guide

### Commercial implication

A baseline assessment should not stop at “you have antivirus.” It should test whether the customer can:

- prevent common identity compromise;
- see meaningful events;
- maintain least privilege;
- recover files/systems;
- restore business operations;
- identify accountable owners; and
- execute an incident process.

## Current cyber-insurance claims signal

Coalition's 2026 Cyber Claims Report, based on its own insured population, reported:

- global claims frequency up 3% in 2025;
- average claim loss around $116,000;
- BEC claim frequency up 15%;
- funds-transfer fraud accounting for 27% of claims; and
- initial ransomware demands up 47% year over year.

Source: Coalition, 2026 Cyber Claims Report announcement: https://www.coalitioninc.com/announcements/2026-cyber-claims-report

This is **commercial insurer data from Coalition's policyholders**, not a representative Census of all U.S. small businesses. Use it as a current claims-pattern signal, not a universal loss rate.

## Control-to-offer map

| Risk | Business consequence | Baseline control area | Potential evidence deliverable |
|---|---|---|---|
| Account takeover | Fraud, data access, lateral movement | MFA, Conditional Access, admin hygiene | MFA/admin/access-policy evidence |
| BEC | Payment diversion, client fraud | Identity + email + domain + payment procedure | email-authentication and payment-verification checklist |
| Ransomware | Downtime, data loss, extortion | endpoint, patching, backup, IR | recovery evidence + incident runbook |
| Lost/stolen device | data exposure | device management, encryption, remote wipe | managed/encrypted device inventory |
| Stale users/vendors | unauthorized access | lifecycle/offboarding/access review | identity/access register |
| SaaS sprawl | hidden data and weak ownership | application inventory/governance | SaaS owner/access map |
| Excess sharing | client/data leakage | SharePoint/OneDrive/Teams governance | sharing-risk report |
| Admin compromise | tenant-wide control loss | privileged access/break glass | privileged-account register |
| Vendor compromise | third-party entry path | vendor access and contracts | service-provider/access inventory |
| No logging | slow detection/investigation | audit/logging baseline | logging coverage matrix |
| No tested recovery | prolonged outage | backup/restore testing | restore test evidence |

## Buying triggers

Risk becomes commercially useful when attached to a **time-bound reason to act**.

### External triggers

- cyber-insurance renewal or application;
- client/customer security questionnaire;
- WISP/Safeguards Rule review;
- HIPAA risk analysis;
- contractual security requirement;
- bank/lender/surety request;
- vendor due diligence;
- audit/readiness project;
- new privacy/security requirement.

### Business-change triggers

- business formation or first professional office;
- growth past owner-managed IT;
- new partner or executive;
- merger/acquisition;
- employee/partner departure;
- new location;
- remote/hybrid expansion;
- migration to Microsoft 365;
- EHR/practice-management/project-system change;
- new major customer;
- new cyber policy;
- large transaction/project.

### Pain triggers

- phishing incident;
- ransomware/data loss;
- compromised mailbox;
- mistaken wire/ACH attempt;
- lost device;
- former employee still has access;
- MSP relationship failure;
- unresolved Microsoft licensing/security issue;
- customer cannot answer “who has access to what?”;
- failed restore;
- insurance premium/exclusion surprise.

## Trigger-led prospecting model

Rather than send “need IT support?” outreach, map each market to a condition.

### Tax/accounting

> Is your WISP backed by actual identity, device, backup, access, and service-provider evidence—or is it mostly a document?

### Law

> If a partner mailbox were compromised today, could the firm prove what the attacker could access and stop a fraudulent payment request?

### Healthcare

> Can the practice demonstrate the technical controls and recovery evidence behind its security risk analysis?

### Construction

> Who can access each active project's files and payment workflows—including subcontractors who are no longer on the job?

### Real estate

> What prevents one compromised inbox from changing where a closing or vendor payment is sent?

These are working research messages, not approved marketing copy.

## Baseline minimum viable control set

The cross-industry evidence consistently supports a minimum technical operating baseline around:

1. authoritative identity;
2. MFA, preferably stronger/phishing-resistant methods where practical;
3. privileged/admin separation;
4. managed, encrypted, patched endpoints;
5. secure email/domain configuration;
6. controlled external sharing;
7. software/SaaS inventory and ownership;
8. tested backup/recovery;
9. useful logging;
10. documented onboarding/offboarding;
11. incident-response contacts/process;
12. payment-change verification for wire-exposed firms;
13. periodic access/security review.

This maps closely to the existing Secure Workplace Foundation concept and supports the idea that the company can reuse a common architecture while changing vertical modules and business narratives.

## Cyber insurance as channel and trigger

FTC's small-business cyber guidance explicitly recommends that businesses consider cyber insurance and explains that coverage may include breach response, data restoration, business interruption, extortion/fraud, forensics, regulatory costs, and third-party liability.

Source: https://www.ftc.gov/business-guidance/small-businesses/cybersecurity

Potential strategy:

- partner with independent commercial/cyber brokers;
- make the assessment useful before renewal;
- produce customer-owned evidence without promising insurance approval;
- remediate gaps identified by insurer questionnaires;
- review annually.

This could become an important channel because the broker has a natural reason to care about the customer's risk quality but usually does not want to operate the customer's technology.

## Measure triggers in pilots

For every prospect, record:

- trigger category;
- trigger date/deadline;
- who created the pressure;
- financial consequence if unaddressed;
- whether budget already exists;
- current provider;
- decision-maker;
- close/no-close;
- time-to-close;
- implementation scope;
- recurring conversion.

After 20–30 opportunities, compare close rate by trigger. The best future vertical may be the market with the most **repeatable triggers**, not simply the highest account count.
