# Legal Architecture Overview

## Source and status

- **Status:** researched working recommendation for founder review and qualified legal/tax validation
- **Research date:** 2026-08-19
- **Scope:** entity structure, founder governance, equity/incentives, workforce, customer and partner contracts, intellectual property, privacy/security, multi-state operations, Chicago-specific issues, and launch compliance
- **Company name:** `[COMPANY_NAME]` remains the canonical placeholder. `CompuCorp` is a temporary project codename, not a proposed legal or public name.
- **Not legal or tax advice:** this document is an internal decision-support artifact. Formation documents, equity issuances, tax elections, securities exemptions, employment terms, and customer contracts should be reviewed by qualified Illinois counsel and a CPA/tax advisor before execution.

## Executive recommendation

The best current fit for the operating model is **an Illinois manager-managed LLC initially taxed as a partnership**, subject to founder approval and written counsel/CPA validation.

This is a recommendation, not an approved decision.

The reasons are structural rather than cosmetic:

1. The business is currently expected to be operationally centered in Chicago/Illinois.
2. The founders want flexible economics and potentially performance-based equity or profits interests.
3. The company is a closely held professional-services / technology business rather than a venture-funded product startup at launch.
4. An Illinois LLC can be drafted to separate economic participation from management authority.
5. Forming in Delaware or Michigan would not eliminate Illinois compliance if the company is actually transacting business from Chicago; it would generally add another state filing layer.
6. An S-corporation tax election may become attractive later, but the one-class-of-stock rule and payroll requirements should be evaluated only after the founder and incentive economics are stable.

## The most important correction to the current founder model

The existing `51% / 20% / 20% / 9%` model should be treated as an **economic allocation concept**, not the legal mechanism that creates founder control.

Under the Illinois Limited Liability Company Act, an Illinois LLC is member-managed unless the operating agreement expressly makes it manager-managed. In a member-managed LLC, each member has equal management rights by default. In a manager-managed LLC, ordinary business management is vested in the manager or managers. The operating agreement therefore needs to do the real control work.

The proposed control architecture is:

- manager-managed LLC;
- one named controlling manager at launch, or a founder-controlled manager appointment/removal mechanism;
- expressly defined manager authority;
- expressly defined member votes and reserved matters;
- carefully designed voting and non-voting economic classes if counsel recommends classes;
- clear issuance/admission mechanics for every new equity holder;
- objective attribution and calculation rules for performance incentives;
- transfer, repurchase, departure, death, disability, bankruptcy, divorce, and change-of-control rules;
- conflict-of-interest and related-party approval procedures;
- records, reporting, and tax-distribution provisions.

A bare statement that one founder owns 51% is not enough to replace this architecture.

## The second major correction: separate founder ownership from incentive compensation

The current documents mix three legally different things:

1. **Founder ownership** — the long-term ownership and governance bargain among the actual founders.
2. **Performance incentives** — compensation earned for sales, delivery, profit creation, or operational milestones.
3. **Worker status** — employee, contractor, LLC member/partner, officer, or advisor status.

These should not be collapsed into one agreement.

### Founder ownership

For people who are actually founders, use a founder ownership instrument with vesting/repurchase protection, governance rights, transfer restrictions, IP assignment, and departure rules. Market-standard technology-startup founder equity commonly uses four-year vesting with a one-year cliff; that is a useful benchmark, not a mandatory rule for this company.

### Performance incentives

The deal-based concept can still be used, but it should ordinarily sit inside a defined **incentive plan** rather than causing a fresh ad hoc issuance of ordinary membership interests on every project.

Possible instruments, in descending order of current fit:

1. LLC profits-interest / incentive-unit plan with performance vesting, if the tax and K-1 consequences are acceptable.
2. Phantom-equity or unit-appreciation plan if the company wants equity-like economics without adding legal/tax owners.
3. Cash commission / profit-sharing plan for sales and shorter-term contributors.
4. Actual capital interests only for people the founders intentionally want as real owners of current enterprise value.

### Worker status

An agreement cannot turn someone into an independent contractor merely by saying so. Likewise, a person receiving a true partnership interest may become a partner for federal tax purposes and generally cannot simultaneously be treated as a W-2 employee of that same partnership for services performed as a partner.

This means the equity instrument and the worker-classification decision must be designed together.

## Why repeated deal-by-deal membership grants are legally expensive

Awarding tiny slices of actual LLC membership after each paid deal sounds simple operationally but can create disproportionate legal overhead:

- each issuance is an offer/sale of a security and needs an available federal and state exemption;
- each new member may acquire statutory information and other membership rights;
- partnership-taxed LLC members receive K-1s and generally are treated as self-employed rather than employees for services to the partnership;
- the operating agreement and capitalization records must remain synchronized;
- valuation and tax questions arise at each grant;
- vesting, repurchase, transfer, divorce, death, disability, and termination treatment must be clear;
- future financing or acquisition diligence becomes more difficult if dozens of small interests were issued inconsistently.

The better operational pattern is usually a **single approved plan + standardized award agreements + a controlled ledger**, with milestones tracked internally and formal grants made only through a defined approval process.

## Illinois versus Delaware versus Michigan

### Illinois — recommended default

Use Illinois if the actual operating center is Chicago and the company is not presently organizing for institutional venture financing.

Advantages for this company:

- one principal domestic entity instead of Delaware plus Illinois qualification;
- Illinois filing costs are modest;
- direct alignment between internal-affairs law and the state where the core business is expected to operate;
- flexible LLC operating-agreement architecture;
- no need to pay Delaware annual LLC tax solely for prestige.

Key Illinois design requirement: make the LLC manager-managed and do not rely on statutory defaults.

### Delaware — defer unless the financing model changes

Delaware LLC law is sophisticated and flexible, but a Delaware LLC operating from Chicago would generally still need to qualify in Illinois and maintain both Delaware and Illinois compliance. Delaware currently imposes a $400 annual LLC tax. For a closely held consulting/services company without an institutional financing requirement, the extra layer has no obvious launch benefit.

Reconsider Delaware if the business later expects:

- institutional venture capital;
- a Delaware C-corporation conversion in the near term;
- sophisticated external investors who insist on Delaware law;
- a transaction structure for which Delaware precedent materially matters.

### Michigan — operational nexus, not founder residence, should drive the decision

A founder/member living in Michigan does not by itself answer whether the company must qualify there. Michigan requires a foreign LLC that is “transacting business” in Michigan to obtain a Certificate of Authority, and the analysis depends on actual activities. Remote employees, regular operations, local offices, contracting, or sustained customer-delivery activity can also create tax/payroll or registration obligations.

If the real headquarters and majority of operations were instead going to be Michigan-based, forming there could be revisited. Based on the current Chicago-first operating plan, Illinois remains the cleaner starting point.

## Legal document stack

The company should treat the following as one connected legal system.

### 1. Formation and governance

- Articles of Organization identifying manager-managed status where appropriate
- Operating Agreement
- Organizer action / initial member consent
- Initial manager consent
- EIN documentation
- registered-agent records
- ownership ledger / cap table
- statement of authority if useful for banking or contracting
- bank authorization and signing-authority resolutions
- conflict-of-interest / related-party process
- annual compliance calendar

### 2. Founders and equity

- founder term sheet (business terms; generally nonbinding except clearly identified provisions)
- founder subscription/unit-purchase agreement
- founder vesting / company repurchase terms
- LLC incentive-unit / profits-interest plan if selected
- standardized award agreement and joinder
- phantom-equity plan if selected instead
- transfer restrictions, right of first refusal, permitted transfers, buy-sell mechanics
- change-of-control, drag/tag, and acceleration provisions if appropriate
- death, disability, divorce, bankruptcy, termination, and bad-actor treatment
- tax-distribution policy
- Section 83(b) workflow where applicable
- securities-law exemption checklist and approval record for each issuance

### 3. People and intellectual property

- employee offer / employment agreement as applicable
- contractor master agreement + statement of work
- Illinois Freelance Worker Protection Act compliant terms when applicable
- confidentiality and trade-secret agreement with federal DTSA notice
- invention/IP assignment with Illinois Employee Patent Act notice for employees
- pre-existing-IP schedule and license-back mechanics
- acceptable use, security, access, and customer-data rules
- background check / credential requirements only where justified and lawful
- worker-classification checklist

### 4. Customer contracting

- Master Services Agreement
- Statement of Work
- change order
- recurring managed-services/service schedule
- SLA/support schedule if offered
- data protection and security addendum
- HIPAA Business Associate Agreement when the company handles ePHI as a business associate
- customer administrative-access authorization
- software/cloud/reseller schedule
- third-party terms and flow-downs
- incident notification and cooperation terms
- IP ownership and deliverable licensing terms
- acceptance criteria
- warranty/disclaimer framework
- limitation of liability
- indemnification
- payment, collections, suspension, and taxes
- termination, offboarding, credential return, data return/deletion, and transition assistance

### 5. Partners and subcontractors

- subcontractor agreement
- security/privacy flow-down
- IP assignment / deliverable rights
- insurance and indemnity requirements
- BAA or other regulated-data flow-down when triggered
- referral agreement
- reseller/distributor/CSP contract review
- customer ownership / non-circumvention rules where legally appropriate
- transition and termination rights

### 6. Public-facing legal materials

- website terms if the site becomes transactional or collects substantive user information
- privacy notice calibrated to actual data collection
- cookie/analytics disclosures where applicable
- marketing-claim review for security/compliance representations
- trademark clearance and filing strategy for the final name

## Laws and regimes that should be on the launch radar

The detailed source matrix is in `04-GOVERNING-LAW-AND-SOURCE-MATRIX.md`. The primary launch regimes include:

- Illinois Limited Liability Company Act, 805 ILCS 180
- Illinois Securities Law of 1953, 815 ILCS 5
- federal Securities Act exemptions, including Rule 701 and Regulation D where applicable
- Internal Revenue Code partnership rules, Section 83, and profits-interest guidance
- Illinois Freelance Worker Protection Act, 820 ILCS 193
- Illinois Freedom to Work Act, 820 ILCS 90, for restrictive covenants with employees
- Illinois Employee Patent Act, 765 ILCS 1060
- federal Defend Trade Secrets Act notice requirement, 18 U.S.C. § 1833(b)
- Illinois Personal Information Protection Act, 815 ILCS 530
- Illinois Biometric Information Privacy Act if biometric information is handled
- HIPAA/HITECH when serving covered entities and accessing ePHI
- FTC Safeguards Rule / GLBA service-provider requirements when serving covered financial institutions
- Illinois and Chicago sales/lease-tax rules for cloud/software/resale activity
- Chicago business licensing rules
- Michigan foreign-qualification, payroll, unemployment, workers-compensation, and tax rules as actual Michigan operations develop

## Chicago issue that deserves special attention before cloud resale

The company intends to evaluate Microsoft/cloud distribution and licensing. Chicago's Personal Property Lease Transaction Tax expressly reaches certain nonpossessory computer leases and currently carries a 15% rate. Illinois also changed its treatment of leases/rentals beginning in 2025, with special rules for software and for property already subject to qualifying local lease taxes.

Before becoming the reseller/lessor of record or bundling mandatory services into cloud charges, the company should obtain a written sales/use/lease-tax analysis covering:

- who is legally the licensor/lessor;
- customer location sourcing;
- Chicago tax applicability;
- Illinois software-license exemptions;
- resale/re-lease documentation;
- whether consulting/support charges are truly optional or become part of taxable lease price;
- invoicing and collection mechanics;
- distributor responsibilities versus company responsibilities.

This should be resolved before the first material CSP/reseller transaction, not after invoices are issued.

## Regulated-client service boundaries

The proposed Chicago prospect lanes include healthcare, accounting/financial, and legal clients. The company is not merely selling generic IT into those verticals; in some engagements it may become a regulated service provider or contractually inherit sector obligations.

Build a trigger matrix:

| Trigger | Legal/contract consequence to review |
|---|---|
| access to electronic protected health information | HIPAA business-associate analysis; BAA; HIPAA security/privacy flow-downs |
| service to a GLBA-covered financial institution | Safeguards Rule vendor-security terms; customer-specific security requirements |
| personal information of Illinois residents | Illinois reasonable-security and breach-response requirements |
| biometric identifiers or biometric information | BIPA collection/consent/retention/disclosure analysis |
| client privileged/confidential legal information | law-firm confidentiality/security obligations and contractual controls |
| payment-card data | PCI contractual/technical scope; minimize card-data handling |
| customer administrator credentials | privileged-access, logging, authorization, credential-vault, termination controls |

## Current CTA / BOI status

As of this research date, FinCEN states that entities created in the United States and their beneficial owners are exempt from Corporate Transparency Act BOI reporting under the 2025 interim final rule. Do **not** blindly include a domestic BOI filing as a launch task. Instead, re-check FinCEN at the actual formation date because this area has changed rapidly.

## Top risks in the present repository drafts

1. **51% is being used as if it automatically creates control.** It does not replace a manager-managed operating agreement.
2. **The execution-equity draft calls recipients contractors while potentially making them equity owners.** Worker and partner tax status must be reconciled.
3. **“Sole and final discretion” is too broad.** Illinois operating agreements cannot eliminate the implied covenant of good faith and fair dealing, and members/transferees have statutory remedies for oppressive conduct.
4. **Every true equity grant is a securities issuance.** The plan needs an exemption and approval workflow.
5. **A sales contractor may not fit Rule 701 simply because the award is compensatory.** SEC guidance specifically excludes independent salespersons without an employment relationship from the consultant/advisor category; another exemption may be needed.
6. **Actual LLC ownership creates tax administration.** Partnership-taxed LLC members generally receive K-1s and are self-employed for services to the partnership.
7. **Current IP language is not yet a complete chain-of-title system.** Use present assignment, pre-existing-IP schedules, customer-license rules, Illinois invention notice, and DTSA whistleblower notice.
8. **Cloud/software tax architecture is missing.** This matters particularly in Chicago.
9. **Michigan operations need an explicit nexus trigger.** Do not wait until payroll or contracts have accumulated.
10. **The customer contract package needs regulated-data modules.** The same MSA/SOW should not be expected to solve every healthcare/financial/legal-client issue by itself.

## Recommended legal design sequence

1. Approve founder identities, roles, desired economics, and desired control outcome.
2. Have Illinois startup/business counsel and a CPA/tax attorney validate Illinois manager-managed LLC vs. corporation and the initial tax classification.
3. Choose the founder ownership instrument separately from the contributor incentive instrument.
4. Draft the operating agreement around the chosen structure before any non-founder equity is issued.
5. Create the equity/incentive plan and securities/tax issuance workflow.
6. Execute founder IP/confidentiality and ownership documents.
7. Form the entity and complete EIN, banking, accounting, registrations, and insurance.
8. Complete Illinois/Chicago/Michigan nexus and tax registrations based on actual operations.
9. Finalize the MSA/SOW/security/reseller/partner contract stack.
10. Perform the Chicago cloud/software tax analysis before becoming a material reseller.
11. Do not sign the first paid pilot until contract, access, security, insurance, and data-handling controls are aligned.

## Source links

Primary and high-quality secondary sources used for this overview are maintained in `04-GOVERNING-LAW-AND-SOURCE-MATRIX.md` so they can be re-validated before execution.
