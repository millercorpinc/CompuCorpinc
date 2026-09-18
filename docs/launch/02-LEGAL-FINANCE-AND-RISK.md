# Legal, Finance, and Risk Setup

## Source and status

- **Status:** launch execution index; material legal/tax decisions remain proposed pending professional review
- **Research update:** 2026-08-19
- **Company name:** use `[COMPANY_NAME]`; the repository name is a temporary project codename
- **Not legal, tax, accounting, or insurance advice:** executable documents and elections require qualified professional review

## Deep-dive legal architecture

Use the legal research set as the design brief for counsel and tax advisors:

1. `../legal/00-LEGAL-ARCHITECTURE-OVERVIEW.md`
2. `../legal/01-ENTITY-JURISDICTION-AND-TAX.md`
3. `../legal/02-FOUNDER-EQUITY-AND-INCENTIVE-DESIGN.md`
4. `../legal/03-CONTRACT-COMPLIANCE-AND-RISK-STACK.md`
5. `../legal/04-GOVERNING-LAW-AND-SOURCE-MATRIX.md`
6. `../legal/05-CURRENT-EQUITY-DRAFT-LEGAL-REVIEW.md`
7. `../legal/06-COUNSEL-AND-CPA-CLOSING-CHECKLIST.md`
8. `../decisions/ADR-0005-ENTITY-JURISDICTION-AND-INCENTIVE-ARCHITECTURE.md`

## Current proposed architecture

Pending founder approval and counsel/CPA validation, the current best-fit structure is:

- Illinois manager-managed LLC;
- initial partnership tax treatment;
- founder control encoded in the Operating Agreement rather than relying on a 51% percentage alone;
- true founder ownership separated from sales/execution incentive compensation;
- profits-interest/incentive units compared against phantom equity for long-term contributors;
- cash commission/profit-sharing preferred for early sales or short-term contributors unless actual equity is deliberately approved;
- Michigan registration/payroll/tax obligations triggered by actual Michigan activity;
- Delaware deferred unless the financing/investor model creates a concrete reason for it.

This is a proposal, not an approved entity/tax decision.

## Legal and entity

- Final-name availability and trademark screening
- Founder roster and ownership/business terms
- Entity and jurisdiction analysis
- Illinois manager-managed governance analysis
- Tax classification analysis
- Formation
- Registered agent
- Operating Agreement
- Initial member/manager/organizer consents
- Ownership/unit ledger and capitalization procedure
- Securities exemption and issuance procedure
- Foreign qualifications where required
- Michigan nexus/qualification trigger review
- Chicago business license/location analysis
- Local licenses and registrations
- Intellectual-property assignments
- Contractor and employee documents
- Annual compliance calendar

## Founder and incentive legal stack

- Founder term sheet
- Founder subscription/unit-purchase agreement
- Founder vesting / company repurchase mechanics
- Transfer restrictions and buy-sell provisions
- Death/disability/divorce/bankruptcy/departure rules
- IP/confidentiality/invention assignments
- Incentive-unit/profits-interest plan **or** phantom-equity plan
- Standard award agreement and joinder where applicable
- Performance-credit / attribution policy
- 83(b) procedure where applicable
- Securities exemption/notice memo for each issuance
- Tax distribution policy

The existing execution-equity draft is a business-design example and should **not** be signed in its current form. See `../legal/05-CURRENT-EQUITY-DRAFT-LEGAL-REVIEW.md`.

## Tax and finance

- EIN and tax registrations
- Federal tax classification/election analysis
- Illinois partnership/replacement-tax/PTE analysis
- Owner-state tax analysis
- Michigan payroll/withholding analysis if triggered
- Business bank account
- Accounting system and chart of accounts
- Expense and reimbursement policy
- Invoicing and collections
- Payroll when required
- Sales/use/lease-tax analysis
- Chicago Personal Property Lease Transaction Tax analysis before material cloud/software resale
- License-resale/re-lease documentation
- Financial forecast
- Capital and cash-reserve plan
- Tax-distribution model if partnership-taxed

### Current CTA/BOI note

As of the 2026-08-19 research date, FinCEN states that entities created in the United States and their beneficial owners are exempt from CTA beneficial-ownership-information reporting under the current rule. Re-check FinCEN at formation rather than copying a stale mandatory BOI task from older startup checklists.

## Insurance

Discuss with a qualified broker and align limits/exclusions with customer contract risk:

- General liability
- Professional liability / technology E&O
- Cyber/privacy liability
- Workers compensation / employers liability when triggered
- Crime/fidelity/social-engineering coverage
- Employment practices when appropriate
- Directors and officers when governance/investor exposure justifies it
- Hired/non-owned auto or commercial auto where relevant
- Umbrella/excess where appropriate

## Contract framework

### Customer

- Master Services Agreement
- Statements of Work
- Change Order
- Managed-services / recurring-governance schedule
- Service-level/support schedule where applicable
- Data protection and security addendum
- HIPAA Business Associate Agreement when triggered
- Customer administrative-access authorization
- Software/cloud/reseller schedule
- Third-party/vendor terms
- Acceptable-use and access authorization
- Incident/breach cooperation terms
- Customer offboarding and transition terms

### People

- Founder agreements
- Employee documents
- Contractor agreement + SOW
- Illinois Freelance Worker Protection Act compliant terms when applicable
- IP/confidentiality/invention assignment
- DTSA whistleblower-immunity notice
- Illinois Employee Patent Act notice for applicable employee invention assignments
- Security/access rules
- Worker-classification review

### Partners

- Subcontractor agreement
- Referral agreement
- Partner/channel agreement
- Distributor/CSP agreement review
- Security/privacy/BAA flow-downs
- Insurance and indemnity requirements
- Customer ownership and transition rules

## Privacy, security, and regulated-client triggers

The company should maintain a trigger matrix before contracting:

- Illinois personal information → PIPA security/breach obligations
- biometric information → BIPA review
- ePHI / healthcare client access → HIPAA business-associate analysis and BAA
- covered financial institution customer → GLBA/FTC Safeguards Rule vendor terms
- law firm confidential/privileged information → customer ethical/security requirements
- payment-card data → minimize and control PCI scope

The company's existing position remains correct: provide readiness, technical control design, remediation, evidence support, and continuing maintenance, while leaving legal advice, tax advice, and independent audit/attestation to appropriately qualified independent professionals.

## Definition of legal readiness

Gate 2 should not be considered complete merely because Articles were filed.

Evidence should include:

- entity formed and in good standing;
- manager-managed Operating Agreement executed;
- founder ownership and IP documents executed;
- securities/tax issuance process established;
- EIN/tax/banking/accounting established;
- applicable Illinois/Chicago/Michigan registrations resolved;
- insurance active;
- MSA/SOW/security contract package approved;
- contractor/employee templates approved;
- cloud/software tax model resolved before resale;
- secure corporate-record system established for executed confidential legal documents.
