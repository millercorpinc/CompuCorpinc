# Contract, Compliance, and Risk Stack

## Source and status

- **Status:** researched contract architecture for founder and counsel review
- **Research date:** 2026-08-19
- **Purpose:** specify the documents and legal controls required to move from an advisory/technology concept to a repeatable contracting system
- **Professional review required:** qualified counsel must convert these requirements into executable agreements

## Principle

The company should not operate from one giant generic contract.

Use a modular architecture:

> **MSA + SOW + service-specific schedules + security/data terms + regulated-client modules + third-party/reseller terms.**

This allows the company to keep stable legal terms in the MSA while changing scope, price, service levels, customer environment, and regulatory modules without rewriting the entire relationship.

## 1. Master Services Agreement

The MSA should establish the durable legal relationship.

### Parties and authority

- exact legal entity names;
- addresses and notice mechanics;
- signature authority;
- order of precedence among MSA, SOWs, schedules, change orders, and third-party terms;
- no authority of individual consultants to vary terms absent written authorization.

### Scope model

- services only as stated in executed SOWs;
- customer dependencies and responsibilities;
- assumptions and exclusions;
- no implied responsibility for systems outside scope;
- changes require a documented change order;
- emergency work process.

### Fees and payment

- fixed fee, T&M, recurring, and pass-through structures;
- deposits/upfront payment where used;
- invoicing cadence;
- payment term;
- late fees only to the extent lawful;
- collection costs where enforceable;
- disputed-invoice procedure;
- suspension rights;
- no setoff unless negotiated;
- taxes and tax-exemption documentation;
- third-party price changes;
- currency and payment method.

### Acceptance

For implementation work:

- objective deliverables;
- acceptance test/process;
- customer review window;
- defect/correction process;
- deemed acceptance only if counsel considers it appropriate;
- distinction between acceptance and ongoing support obligations.

### Warranties and disclaimers

Address:

- professional/workmanlike performance standard;
- no guarantee of perfect security or prevention of all incidents;
- customer responsibility for business decisions and residual risk;
- third-party vendor/service disclaimers;
- no legal, tax, accounting, audit, or regulated attestation advice;
- no warranty for customer-directed deviations from recommendation;
- emergency/unsupported configurations.

Avoid public or contractual claims such as “fully secure,” “compliant,” or “guaranteed” unless the statement can actually be substantiated.

### Limitation of liability

Counsel should design:

- aggregate cap;
- whether cap is tied to fees paid in a defined period or project fees;
- direct vs. consequential damages;
- lost profits/data/business interruption;
- carve-outs for confidentiality, IP infringement, gross negligence/willful misconduct, payment obligations, or other negotiated risks;
- separate/supercap treatment for security/privacy if commercially required;
- interaction with insurance coverage.

The contract limit should be coordinated with E&O and cyber policy limits rather than drafted independently.

### Indemnification

Define reciprocal or asymmetric indemnities as appropriate for:

- third-party IP claims;
- bodily injury/property damage;
- misuse or illegal customer-provided content/data;
- security/privacy breach caused by a party's breach of obligations;
- subcontractor acts where appropriate.

Use defense-control, notice, cooperation, and settlement-consent mechanics.

### Termination and transition

- termination for cause;
- cure period;
- insolvency;
- termination of recurring services;
- immediate suspension/termination for security or illegal activity;
- fees due on termination;
- committed third-party costs;
- credential revocation;
- data return/deletion;
- transition assistance and its pricing;
- final documentation package;
- survival provisions.

## 2. Statement of Work

Every SOW should identify:

- business objective;
- environment/customer;
- services and deliverables;
- exclusions;
- assumptions;
- dependencies;
- customer responsibilities;
- required access;
- delivery phases;
- timeline;
- acceptance criteria;
- fees/payment milestone;
- approved expenses;
- named project roles;
- change-control path;
- security/data classification;
- relevant service schedules;
- third-party products;
- recurring-services conversion opportunity.

The SOW should not silently expand the company's responsibility beyond what was priced.

## 3. Change Order

A fixed-fee consulting business needs a formal change-control instrument from day one.

Trigger examples:

- undocumented legacy configuration;
- migration conditions outside assessment evidence;
- additional users/sites/tenants;
- customer delays;
- new integrations;
- extra compliance requirements;
- after-hours work;
- emergency remediation;
- third-party dependency failure;
- materially incorrect customer information.

The delivery team should be authorized to identify scope change but not to give away unpriced work.

## 4. Managed Services / Recurring Governance Schedule

This should define the boundary more tightly than the MSA.

Include:

- included services;
- excluded services;
- covered users/devices/tenants;
- service window;
- support channels;
- response targets versus resolution targets;
- severity definitions;
- maintenance windows;
- escalation;
- customer-designated contacts;
- change limits;
- project work excluded from recurring fee;
- minimum technical baseline/prerequisites;
- unsupported/end-of-life systems;
- third-party vendor dependency;
- security-event process;
- pricing and overage;
- renewal and repricing;
- offboarding.

Do not sell “unlimited support” unless the economics and exclusions truly support it.

## 5. Customer Administrative-Access Authorization

Because the company will administer privileged technology systems, use explicit authorization that covers:

- systems/accounts the company may access;
- authority to make configuration changes within SOW scope;
- emergency change authority;
- named/admin accounts;
- least privilege;
- MFA;
- customer ownership of tenant/accounts;
- company credential vault;
- logging;
- customer approvals for high-risk changes;
- prohibition on shared personal credentials when avoidable;
- exit/revocation procedure.

This should align with the delivery playbook and cyber insurance representations.

## 6. Data Protection and Security Addendum

Illinois Personal Information Protection Act § 45 requires reasonable security measures for records containing Illinois residents' personal information and requires contracts involving disclosure of such information to include a provision requiring reasonable security measures by the recipient.

The DPA/security addendum should therefore be real operational language, not generic “industry standard security” boilerplate.

Cover:

- data roles and purpose limitation;
- categories of data;
- authorized personnel;
- least privilege;
- encryption;
- MFA;
- endpoint controls;
- secrets/credential management;
- logging;
- vulnerability/patching expectations;
- subcontractors;
- secure development/change control;
- incident detection and notice;
- investigation/cooperation;
- evidence preservation;
- data return/deletion;
- retention;
- geographic or customer restrictions where required;
- audit/evidence rights proportionate to company size and service.

## 7. Incident / breach terms

Do not promise a notification deadline that the operating team cannot meet.

Contract language should distinguish:

- security event;
- confirmed security incident;
- breach of protected/personal information;
- legally reportable breach.

Define:

- initial notice to customer;
- updates;
- preservation of logs/evidence;
- forensic cooperation;
- legal/forensic decision authority;
- regulator/data-subject notification responsibility;
- costs and insurance coordination;
- communications/public statements.

Customer-specific law may require stricter timing than the baseline contract.

## 8. HIPAA module

The company can become a HIPAA business associate when providing IT/support services to a covered entity and the service involves access to protected health information. HHS expressly identifies IT contractors that require PHI access as a common business-associate example.

When triggered:

- execute a BAA before PHI access;
- apply HIPAA Security Rule controls appropriate to the role;
- flow obligations to subcontractors that access PHI;
- include breach/security-incident cooperation;
- restrict use/disclosure;
- address return/destruction;
- document customer versus company responsibilities.

Do not use a BAA merely as marketing. If the company signs one, operations must actually support it.

## 9. Financial-sector / GLBA module

For customers subject to the FTC Safeguards Rule or related financial privacy/security regimes, expect vendor-management provisions requiring the customer to select capable service providers, contractually require safeguards, and periodically assess the provider.

The company should maintain a reusable financial-client evidence package:

- security overview;
- access controls;
- incident response;
- encryption;
- logging;
- vulnerability management;
- subcontractor controls;
- insurance;
- business continuity;
- recent security review/evidence appropriate to maturity.

Do not claim GLBA compliance for the customer as a legal conclusion.

## 10. Law-firm clients

Law firms can impose unusually strict confidentiality, privilege, and incident obligations even where no standalone MSP statute controls the relationship.

Contract and operations should address:

- confidential/privileged material;
- matter-level access restrictions;
- eDiscovery/hold issues when relevant;
- subcontractors and support access;
- logging;
- data location;
- incident notice;
- secure disposal;
- customer ethical/security requirements.

The company should not interpret legal-ethics rules for a law firm; the client or its counsel should specify required controls.

## 11. Illinois biometric information

If any solution captures, stores, transmits, or configures biometric identifiers/information, perform a BIPA review before implementation.

Do not treat fingerprints, face templates, or other biometric authentication data as ordinary account data. BIPA has specific policy, notice/consent, retention, sale/disclosure, and destruction concepts.

Default design principle: minimize the company's direct possession of customer biometric data and use platform-native controls where feasible.

## 12. Software / cloud / CSP schedule

If the company resells Microsoft/cloud/software subscriptions, use a separate schedule.

Cover:

- whether the company is reseller, agent, or billing intermediary;
- customer acceptance of vendor terms;
- no ownership of third-party software;
- vendor service availability/warranty limitations;
- license quantities and true-up;
- renewals;
- cancellation windows;
- vendor price/currency changes;
- suspension for nonpayment;
- customer tenant ownership;
- transition of subscriptions on termination;
- distributor dependencies;
- taxes;
- Chicago lease-tax handling;
- support boundaries;
- data-processing roles.

Do not bury third-party recurring liabilities inside the professional-services SOW.

## 13. Tax clause architecture

The MSA/reseller schedule should allocate responsibility for:

- sales/use/lease transaction taxes;
- exemptions and certificates;
- tax added to invoice;
- customer self-assessment where legally appropriate;
- changes in law/rate;
- taxes on company net income excluded from customer pass-through;
- audit cooperation.

For Chicago cloud/software transactions, tax counsel/CPA should approve the actual billing model before launch.

## 14. Subcontractor agreement

The company's operating model assumes specialists and contractors. Use a real subcontractor framework containing:

- independent-contractor relationship, subject to actual classification facts;
- no authority to bind company/customer;
- SOW and rate;
- payment;
- Illinois Freelance Worker Protection Act compliant written terms when applicable;
- confidentiality;
- IP assignment;
- pre-existing IP schedule;
- DTSA whistleblower-immunity notice;
- customer confidentiality;
- security/access rules;
- credential handling;
- incident reporting;
- background/credential requirements if justified;
- customer-flow-down requirements;
- BAA/DPA flow-down if triggered;
- insurance;
- indemnity;
- warranty of services;
- non-solicit/non-circumvention only to the extent lawful and appropriately drafted;
- return/deletion of information;
- termination and access revocation.

## 15. Illinois Freelance Worker Protection Act

Illinois' Act covers specified natural-person independent contractors providing services in Illinois or for an Illinois contracting entity when the compensation threshold is met ($500 in a single contract or aggregated over 120 days), subject to statutory exclusions.

The company should standardize written contractor SOWs that include:

- products/services;
- value/rate/method of compensation;
- payment due date or mechanism;
- dates/services to be provided;
- any additional statutory content required by current Department rules.

If a contract lacks a payment date, the Act generally makes payment due no later than 30 days after completion. Civil remedies can include double underpayment, statutory damages, fees, and costs.

## 16. Worker classification

Calling someone a contractor does not control legal status. IRS guidance looks to the actual relationship, including behavioral control, financial control, and type of relationship.

Create a classification review before onboarding a recurring contributor. Red flags for employee treatment can include extensive control over how/when work is performed, integration into ongoing operations, indefinite relationship, exclusivity, company-provided tools, and employee-like benefits or supervision.

Also remember the separate rule: if the LLC is taxed as a partnership and a person becomes a partner/member for tax purposes, the IRS generally treats that person as self-employed rather than an employee for services to the partnership.

## 17. Restrictive covenants

Do not use a broad template noncompete reflexively.

Illinois' Freedom to Work Act currently restricts employee noncompetes and nonsolicits based on annualized earnings thresholds and imposes procedural/substantive requirements. In 2026, the statutory thresholds are $75,000 for noncompetes and $45,000 for nonsolicits; they increase on January 1, 2027.

For any restrictive covenant:

- identify employee/contractor status and governing state;
- protect legitimate interests narrowly;
- use confidentiality/trade-secret/IP protections first;
- confirm compensation threshold if Illinois employee;
- give required review notice/time;
- reassess Michigan law for Michigan workers;
- avoid language broader than customer/role/geography/duration actually requires.

## 18. Confidentiality and trade secrets

Federal DTSA law requires employers to provide whistleblower-immunity notice in contracts governing trade secrets/confidential information if the employer wants access to certain exemplary damages and attorney-fee remedies. For this notice, “employee” expressly includes contractors and consultants.

Every employee/contractor confidentiality agreement should therefore include the statutory notice or an approved policy cross-reference.

Trade-secret protection also requires operational secrecy measures. Contract language should be backed by access controls, data classification, least privilege, offboarding, logging, and confidentiality markings where appropriate.

## 19. IP assignment

### Employees

Illinois' Employee Patent Act limits invention-assignment clauses for inventions developed entirely on an employee's own time without employer resources unless the statutory business/R&D/work relationship exceptions apply. If an Illinois employment agreement requires invention assignment, the employer must provide the statutory written notification.

### Contractors

Do not rely solely on “work made for hire.” Copyright work-made-for-hire status for commissioned contractors is limited to specified statutory categories and requires a signed writing. Use a present assignment of deliverable IP plus work-made-for-hire language where applicable.

### Required IP chain

For every contributor:

- list pre-existing/background IP;
- assign newly created company deliverables/IP to the company to the extent legally permitted;
- license necessary background IP to the company/customer;
- require disclosure of third-party/open-source components;
- require further-assurances cooperation;
- define moral-rights waiver/consent where lawful;
- preserve employee statutory carve-outs;
- ensure customer SOW says what IP the customer receives.

## 20. Customer IP model

Decide this before first custom automation project.

Recommended baseline to evaluate:

- customer owns its data, customer-specific content, and customer-provided materials;
- company retains pre-existing tools, templates, generic methods, know-how, scripts, frameworks, and reusable components;
- customer receives an appropriate perpetual or term license to embedded company background IP necessary to use paid deliverables;
- bespoke deliverable ownership is specified in the SOW;
- open-source and third-party components remain subject to their licenses;
- improvements/generalized learning that do not disclose customer confidential information remain company know-how.

Without this distinction, custom automation work can accidentally give away the reusable operating system of the company.

## 21. Marketing and professional-boundary controls

Because the company will market security/compliance readiness:

- say `readiness`, `assessment`, `remediation`, `evidence support`, or `control implementation` when that is what is delivered;
- do not say the company “certifies,” “attests,” “guarantees compliance,” or gives legal opinions unless that function is actually performed by a qualified professional with appropriate independence;
- separate technical control assessment from legal interpretation;
- have independent CPA/auditor/legal partners perform functions that require credentialing or independence.

This is already consistent with the repository architecture and should be retained.

## 22. Insurance-to-contract alignment

Before signing customer paper, broker and counsel should align:

- commercial general liability;
- technology E&O/professional liability;
- cyber/privacy liability;
- workers compensation/employers liability;
- crime/social engineering/funds transfer where relevant;
- hired/non-owned auto if applicable;
- D&O when equity/governance/investor exposure justifies it.

Check:

- limits;
- deductibles/retentions;
- retroactive date;
- contractual-liability exclusions;
- professional-services definition;
- cyber sublimits;
- ransomware/social-engineering coverage;
- subcontractor coverage;
- customer-required additional insured / certificates;
- whether contract indemnities exceed insured risk.

## Primary sources

- Illinois Freelance Worker Protection Act: https://www.ilga.gov/Legislation/ILCS/Articles?ActID=4441&Chapter=EMPLOYMENT&ChapterID=68&MajorTopic=BUSINESS+AND+EMPLOYMENT
- Illinois Freedom to Work Act § 10: https://ilga.gov/legislation/ilcs/fulltext?DocName=082000900K10
- Illinois Employee Patent Act § 2: https://www.ilga.gov/documents/legislation/ilcs/documents/076510600K2.htm
- Federal DTSA notice, 18 U.S.C. § 1833(b): https://uscode.house.gov/view.xhtml?req=(title:18%20section:1833%20edition:prelim)
- Illinois Personal Information Protection Act § 45: https://www.ilga.gov/documents/legislation/ilcs/documents/081505300K45.htm
- IRS worker/owner guidance: https://www.irs.gov/businesses/small-businesses-self-employed/paying-yourself
- HHS Business Associate guidance: https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/business-associates/index.html
- FTC Safeguards Rule guidance: https://www.ftc.gov/business-guidance/privacy-security/gramm-leach-bliley-act
- U.S. Copyright Office work-made-for-hire guidance: https://www.copyright.gov/circs/circ30.pdf
