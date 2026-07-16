# Solution Opportunity Catalog

## Status

Initial working catalog recovered and formalized from the Startup project’s Top 200 solution-opportunity concept.

These entries are proposed discovery and solution patterns, not approved fixed-scope services. They must be validated through buyer conversations, delivery evidence, security review, and commercial modeling.

## Purpose

Use the catalog to:

- Make prospecting specific
- Improve discovery
- Match business situations to solution patterns
- Accelerate proposals
- Identify recurring-governance opportunities
- Build reusable intellectual property
- Rank productization investments

## Ranking model

Each opportunity should be scored from 1–5 on:

- Business impact
- Frequency in the target market
- Buyer urgency
- Identifiability
- Strategic fit
- Reusability
- Recurring-revenue potential
- Delivery effort
- Delivery risk
- Maintenance and support burden

Suggested initial formula:

> Priority = (Impact × Frequency × Urgency × Identifiability × Strategic Fit × Reusability × Recurring Potential) ÷ (Effort × Risk × Maintenance Burden)

The formula is a prioritization aid, not a substitute for judgment.

## Standard opportunity record

Each detailed opportunity should ultimately include:

- Identifier
- Business situation
- Likely buyer
- Trigger event
- Observable symptoms
- Business consequence
- Discovery questions
- Systems and data involved
- Candidate solution pattern
- Prerequisites
- Security and compliance considerations
- Estimated effort
- Delivery risk
- Maintenance burden
- Evidence and acceptance
- Recurring attach
- Reusable assets
- Reference projects and lessons
- Status and owner

## Initial 20 high-confidence opportunities

### SOL-001 — Uncontrolled Microsoft 365 administrator access

**Situation:** Multiple global administrators, shared administrator accounts, or normal user accounts holding broad privileges.

**Likely buyer:** Owner, IT manager, security or compliance leader.

**Business consequence:** Increased compromise risk, poor accountability, failed insurance or customer-security review.

**Discovery questions:**

- Who currently has global or privileged roles?
- Are administrator identities separate from daily-use identities?
- Is emergency access documented?
- Are role activations and changes reviewed?

**Candidate pattern:** Administrative hygiene, least privilege, separate admin identities, PIM or equivalent controls, emergency-access procedure, review cadence.

**Recurring attach:** Identity and privileged-access governance.

### SOL-002 — MFA exists but access is not actually governed

**Situation:** MFA is enabled, but Conditional Access, device trust, legacy authentication, or risk policies are incomplete.

**Likely buyer:** Owner, IT manager, insurance or compliance stakeholder.

**Business consequence:** False confidence and continued account-takeover exposure.

**Candidate pattern:** Entra identity baseline, authentication methods, Conditional Access, legacy-authentication controls, device and risk conditions, exception register.

**Recurring attach:** Access-policy review and Microsoft platform change management.

### SOL-003 — Unmanaged employee devices access company data

**Situation:** Users access email and files from devices with unknown encryption, patch, malware, or local-administrator status.

**Likely buyer:** Operations, IT, security, finance.

**Business consequence:** Data loss, ransomware, insurance gaps, inconsistent support.

**Candidate pattern:** Intune enrollment, compliance, Defender, encryption, update rings, application and local-admin standards, device retirement.

**Recurring attach:** Device administration and security review.

### SOL-004 — Joiner, mover, and leaver process is manual and inconsistent

**Situation:** HR, managers, IT, payroll, and application owners coordinate user changes through email or memory.

**Likely buyer:** Operations, HR, IT, finance.

**Business consequence:** Delayed onboarding, retained access, licensing waste, payroll or compliance errors.

**Candidate pattern:** Authoritative HR or request source, approval workflow, Entra and application provisioning, group-based access, task orchestration, evidence and offboarding checklist.

**Recurring attach:** User lifecycle administration and workflow monitoring.

### SOL-005 — Teams and SharePoint sprawl lacks ownership

**Situation:** Teams, groups, sites, and shared folders are created without naming, ownership, lifecycle, or external-sharing standards.

**Likely buyer:** Operations, IT, compliance, department leaders.

**Business consequence:** Data exposure, duplication, poor search, abandoned workspaces, unclear records.

**Candidate pattern:** Collaboration governance, provisioning standards, owner assignment, guest lifecycle, external-sharing policy, archive and review process.

**Recurring attach:** Collaboration and data-governance review.

### SOL-006 — Sensitive files are exchanged through email attachments

**Situation:** Customer, financial, legal, employee, or other sensitive files are sent as attachments rather than controlled links or upload requests.

**Likely buyer:** Finance, legal, HR, operations, compliance.

**Business consequence:** Uncontrolled copies, forwarding risk, retention ambiguity, poor audit trail.

**Candidate pattern:** SharePoint/OneDrive secure exchange, request files, permission standards, expiration and ownership, sensitivity or retention controls where justified.

**Recurring attach:** Sharing review and data-governance maintenance.

### SOL-007 — Microsoft licensing does not match actual security needs

**Situation:** Licenses are purchased inconsistently or security features are unavailable, unused, or duplicated.

**Likely buyer:** CFO, owner, IT manager.

**Business consequence:** Overspend, missing controls, operational complexity.

**Candidate pattern:** License and capability inventory, target baseline, group-based licensing, renewal ownership, distributor workflow.

**Recurring attach:** License oversight through the approved indirect-CSP/distributor pathway.

### SOL-008 — Security posture is measured only by Secure Score

**Situation:** The organization pursues score increases without business context, ownership, or exception management.

**Likely buyer:** Security, IT, compliance, owner.

**Business consequence:** Misallocated effort, disruptive controls, unaddressed material risk.

**Candidate pattern:** Risk-based Secure Score review, control ownership, priority roadmap, documented exceptions, evidence, recurring review.

**Recurring attach:** Microsoft Security and Governance.

### SOL-009 — Email protection is incomplete or inconsistently configured

**Situation:** Anti-phishing, anti-malware, safe-link, safe-attachment, impersonation, domain, or mail-flow controls are incomplete.

**Likely buyer:** Owner, IT, security, finance.

**Business consequence:** Business email compromise, fraud, malware, reputational loss.

**Candidate pattern:** Defender for Office 365 baseline as licensed, domain and mail-flow review, executive and financial-user protections, user-reporting and incident procedure.

**Recurring attach:** Email-security review and incident readiness.

### SOL-010 — No practical incident-response ownership exists

**Situation:** Logs may exist, but contacts, decision rights, escalation, evidence, containment, and communications are undefined.

**Likely buyer:** Owner, operations, security, legal, insurance.

**Business consequence:** Slow and chaotic response, increased loss, missed contractual or insurance obligations.

**Candidate pattern:** Scaled incident-response plan, contact tree, logging baseline, evidence procedure, partner escalation, tabletop exercise.

**Recurring attach:** Incident-readiness review and tabletop cadence.

### SOL-011 — Provider transition lacks a responsible takeover process

**Situation:** A customer wants to replace an MSP or administrator, but access, documentation, licensing, backups, contracts, and open issues are unclear.

**Likely buyer:** Owner, COO, CFO, IT manager.

**Business consequence:** Lockout, service interruption, hidden risk, duplicate costs.

**Candidate pattern:** Paid takeover assessment, access recovery, provider inventory, contract and license map, risk register, staged transition, customer-owned documentation.

**Recurring attach:** Governance and vendor coordination.

### SOL-012 — Customer lacks a technology roadmap and budget sequence

**Situation:** Technology spending is reactive and vendor-driven.

**Likely buyer:** Owner, president, CFO, COO.

**Business consequence:** Waste, repeated emergencies, weak security prioritization, stalled modernization.

**Candidate pattern:** Fractional technology roadmap, risk and capability assessment, investment sequence, budget, ownership, quarterly governance.

**Recurring attach:** Fractional technology leadership.

### SOL-013 — CRM close does not initiate delivery and billing reliably

**Situation:** A sold opportunity requires manual creation of projects, tasks, billing schedules, folders, and internal notifications.

**Likely buyer:** Sales, operations, finance, professional-services leadership.

**Business consequence:** Delayed kickoff, missed billing, incomplete handoff, rekeying errors.

**Candidate pattern:** Closed-won orchestration using supported connectors, APIs, Power Automate/Logic Apps, project and billing creation, exception handling, evidence.

**Recurring attach:** Automation monitoring and business-system governance.

### SOL-014 — Time, project status, and invoice data do not reconcile

**Situation:** PSA/project, accounting, CRM, and reporting systems contain inconsistent project, customer, time, billing, or collection information.

**Likely buyer:** CFO, operations, professional-services leader.

**Business consequence:** Revenue leakage, slow close, poor forecast, billing disputes.

**Candidate pattern:** System-of-record definition, master-data map, synchronization, reconciliation reports, exception workflow, ownership.

**Recurring attach:** Integration monitoring and financial-workflow governance.

### SOL-015 — Accounts-receivable follow-up is manual

**Situation:** Aging, reminders, account notes, promises, and escalations are handled through spreadsheets and individual email.

**Likely buyer:** CFO, controller, AR manager, owner.

**Business consequence:** Slow collections, inconsistent customer treatment, poor visibility.

**Candidate pattern:** Accounting/CRM integration, aging triggers, communication workflow, promise-to-pay tracking, escalation, dashboards, audit trail.

**Recurring attach:** Automation maintenance and reporting governance.

### SOL-016 — Vendor onboarding and access review are fragmented

**Situation:** Procurement, legal, security, finance, and business owners review vendors through email with no consistent evidence or renewal review.

**Likely buyer:** Operations, finance, security, legal, compliance.

**Business consequence:** Unapproved data sharing, contract risk, duplicate tools, missed renewals.

**Candidate pattern:** Vendor intake, risk tier, approvals, contract and renewal record, access inventory, evidence, recurring review.

**Recurring attach:** Vendor and SaaS governance.

### SOL-017 — Compliance evidence is gathered from scratch each cycle

**Situation:** Control owners manually search for screenshots, policies, approvals, and logs when customers, insurers, or auditors request them.

**Likely buyer:** Compliance, security, CFO, operations.

**Business consequence:** High effort, inconsistent evidence, delayed reviews, control drift.

**Candidate pattern:** Control and evidence map, owner cadence, approved repository, automated evidence where reliable, exception and remediation workflow.

**Recurring attach:** Compliance readiness and control maintenance.

### SOL-018 — Remote or legacy applications require a secure workspace

**Situation:** Users need remote access to applications that cannot be safely or practically delivered to unmanaged endpoints.

**Likely buyer:** Operations, IT, security, application owner.

**Business consequence:** VPN complexity, insecure remote access, inconsistent performance, support burden.

**Candidate pattern:** Azure Virtual Desktop or Windows 365 assessment, identity, network, image, profile, application, storage, security, cost, and operating design.

**Recurring attach:** Virtual-workspace governance and support.

### SOL-019 — Customer and employee data has no clear authority or retention owner

**Situation:** Data is duplicated across mailboxes, Teams, SharePoint, file shares, SaaS systems, and personal storage with no retention decision.

**Likely buyer:** Legal, compliance, HR, finance, operations, IT.

**Business consequence:** Excess exposure, inconsistent records, inability to find authoritative information.

**Candidate pattern:** Information inventory, system-of-record decisions, ownership, sharing, retention requirements, migration or cleanup roadmap, policy and exceptions.

**Recurring attach:** Data-governance review.

### SOL-020 — Executive reporting depends on manual spreadsheet assembly

**Situation:** Data is exported and reconciled manually from CRM, finance, PSA, HR, service, or operational systems.

**Likely buyer:** Owner, CFO, COO, department leader.

**Business consequence:** Slow reporting, inconsistent definitions, hidden errors, limited decision confidence.

**Candidate pattern:** Metric definitions, authoritative sources, data model, controlled refresh, Power BI or appropriate reporting, exception and ownership process.

**Recurring attach:** Data-quality, reporting, and integration governance.

## Catalog expansion categories

Expand deliberately across:

- Identity and access
- Endpoint and device management
- Messaging and collaboration
- Data governance
- Security operations
- Compliance readiness
- Virtual workspace
- CRM and sales operations
- Professional services and project operations
- Finance and collections
- HR and workforce operations
- Vendor and procurement
- Customer service and communications
- Reporting and analytics
- Industry-specific systems
- Provider transition and modernization
- Executive strategy and governance

## Promotion to a packaged service

An opportunity may become a packaged service only after:

- Repeated buyer relevance is demonstrated
- Scope and prerequisites can be bounded
- A reusable solution pattern exists
- Security and support implications are understood
- Effort and cost evidence exists
- Acceptance can be defined
- Recurring ownership is understood
- The company has the required skills and partners

## Next actions

1. Score the initial 20 opportunities.
2. Select the first 5 for detailed solution-pattern documents.
3. Use buyer interviews to validate language and urgency.
4. Link opportunities to actual projects and evidence.
5. Expand toward 200 only with high-quality, specific entries.
