# Current Equity Draft — Legal Review

## Source and status

- **Status:** issue-spotting review of existing repository drafts; not a legal opinion
- **Research date:** 2026-08-19
- **Documents reviewed:**
  - `docs/launch/01-FOUNDER-GOVERNANCE.md`
  - `docs/launch/02-FOUNDER-EQUITY-AND-VESTING.md`
  - `docs/launch/03-EXECUTION-EQUITY-TERMS.md`
  - `docs/launch/04-FOUNDER-TERM-SHEET.md`
- **Purpose:** identify what can be retained conceptually and what should not be converted directly into a signed agreement

## Overall assessment

The existing documents are **good business-design notes but not yet a safe legal implementation**.

The underlying principles are coherent:

- preserve founder control;
- do not split equity equally by friendship/default;
- reward sales for commercial outcomes;
- reward execution for actual value/profit contribution;
- reserve room for future contributors;
- avoid giving permanent equity for mere enthusiasm.

The primary legal issue is that the drafts jump too quickly from those principles to “actual equity” without first deciding what the equity legally is, how it is taxed, what securities exemption applies, what membership rights attach, and whether the recipient remains an employee/contractor or becomes a partner.

## Severity 1 — fix before anyone signs or relies on the terms

### 1. The 51% concept does not itself create legal control

**Current draft concept:** founder retains at least 51% voting/control and therefore final authority.

**Problem:** an Illinois LLC is member-managed by default, and each member has equal management rights unless the operating agreement expressly creates manager management. The current draft therefore cannot be treated as a substitute for the Operating Agreement.

**Required correction:**

- form as manager-managed;
- make manager authority explicit;
- define appointment/removal mechanics;
- define member votes and reserved matters;
- specify voting classes if used;
- define admission/issuance authority.

### 2. Independent-contractor language conflicts with potential partner status

**Current draft concept:** the execution contributor is an independent contractor who may vest actual company equity.

**Problem:** if the company is a partnership-taxed LLC and the award makes the contributor a partner/member for federal tax purposes, IRS guidance generally treats that partner as self-employed rather than an employee for services to the partnership. Separately, merely labeling a worker an independent contractor does not determine worker classification.

**Required correction:** decide, before grant, whether each category is:

- founder/member;
- employee;
- independent contractor;
- consultant/advisor;
- profits-interest holder/partner;
- phantom-equity participant.

Then draft the compensation package around the real status.

### 3. The actual security being issued is undefined

**Current draft concept:** “equity” is awarded up to stated percentages.

**Problem:** `equity` is not a legal instrument. The tax, control, accounting, and securities results differ materially among:

- capital membership units;
- profits interests/incentive units;
- options;
- phantom units;
- unit appreciation rights;
- contractual profit sharing.

**Required correction:** select the instrument and define it in the Operating Agreement and incentive plan before promising percentages.

### 4. Securities exemption process is missing

**Current draft concept:** company can award equity under the contributor agreement.

**Problem:** every actual security offer/sale needs registration or an exemption. Rule 701 may work for some compensatory recipients, but SEC guidance specifically excludes independent salespersons without an employment relationship from the consultant/advisor category.

**Required correction:** each award must have a securities-law checklist and documented federal/state exemption.

### 5. “Sole and final discretion / no appeal” is too aggressive

**Current draft concept:** company/founder has sole and final authority over value attribution and the determination is final and not subject to appeal except as required by law.

**Problem:** Illinois does not allow the Operating Agreement to eliminate the implied covenant of good faith and fair dealing. Members/transferees can also have statutory remedies for illegal, fraudulent, or oppressive conduct. Ambiguous unilateral discretion can also become a contract dispute even before those statutes matter.

**Required correction:** use objective definitions, contemporaneous records, a good-faith standard, mathematical correction procedure, conflict procedure, and accountant determination for qualifying calculation disputes.

### 6. No tax-distribution architecture

**Current draft concept:** contributors earn equity based on project outcomes.

**Problem:** a partnership-taxed owner can be allocated taxable income without receiving corresponding cash.

**Required correction:** Operating Agreement needs tax distributions and tax-allocation mechanics before adding service-provider owners.

### 7. No valuation/hurdle mechanics

**Current draft concept:** a participant can earn a percentage of total company equity after a deal.

**Problem:** if a service provider receives a capital interest in existing enterprise value, that can create compensation income. A profits interest requires the instrument/economics to be structured so the recipient generally participates in future value rather than current liquidation value.

**Required correction:** if using profits interests, establish valuation/hurdle rules and document them at grant.

## Severity 2 — material governance/commercial issues

### 8. Percentage denominators are undefined

The drafts use percentages such as 51%, 20%, 7%, 5%, and 0.50% without always defining whether they refer to:

- issued and outstanding equity;
- fully diluted equity;
- voting power;
- profits share;
- liquidation economics;
- pre- or post-future pool.

**Required correction:** every percentage needs a defined denominator and dilution rule.

### 9. “Vested equity stays forever” may create unwanted permanent minority owners

The termination section says the contributor retains vested equity.

That may be acceptable for a true co-owner, but it can leave the company permanently tied to a departed delivery contributor.

**Required correction:** model company call/buyback rights on vested interests, price, payment terms, good/bad leaver treatment, death/disability, and tax effects.

### 10. No transfer controls

The drafts do not yet comprehensively address:

- transfers to third parties;
- divorce;
- death;
- trusts/estate planning;
- bankruptcy;
- charging orders;
- right of first refusal;
- permitted family transfers;
- drag/tag rights.

These belong primarily in the Operating Agreement.

### 11. No complete IP chain

The founder governance document identifies IP as a decision point but the execution agreement does not contain a full IP/confidentiality/invention assignment system.

**Required correction:** separate IP/confidentiality agreement or integrated provisions with:

- present assignment;
- pre-existing IP schedule;
- background-IP license;
- third-party/open-source disclosure;
- Illinois Employee Patent Act notice where applicable;
- federal DTSA whistleblower notice;
- customer deliverable alignment.

### 12. No plan administration / ledger process

Deal-based vesting needs an actual operating system:

- plan administrator;
- records;
- calculation statement;
- grant approval;
- award signature;
- cap-table update;
- tax reporting;
- securities record;
- annual reconciliation.

Without this, the company can create conflicting oral/written ownership promises.

## Severity 3 — drafting and operating improvements

### 13. “Qualifying Deal” should separate business credit from legal vesting

Current definition requires signed agreement, payment, delivery begun/accepted, and attributable contribution.

Improve by defining separate dates:

- Contracted Date;
- Collected Revenue Date;
- Customer Acceptance Date;
- Measurement Date;
- Credit Approval Date;
- Legal Grant/Vesting Date.

That prevents confusion over when tax/security ownership actually changes.

### 14. Execution Profit needs accounting rules

The current formula is directionally sound but leaves room for disputes.

Define:

- cash collected versus accrued revenue;
- refunds/credits;
- internal labor cost rate;
- contractor costs;
- reimbursed expenses;
- pass-through licensing;
- overhead allocation, if any;
- bad debt;
- sales commission;
- warranty/rework reserve;
- timing of final calculation.

### 15. Profit attribution should avoid purely subjective “value creation”

Use project records and predefined role categories/weights when possible.

For example:

- project lead;
- architecture/technical lead;
- implementation contributor;
- project management/operations;
- specialized deliverable owner.

Adjustments can be allowed, but the reason should be documented.

### 16. Existing founder reserve should model future dilution

The current 9% future-use buffer is a useful planning idea but may be too small or too large depending on hiring/investor strategy.

Treat it as an open planning reserve rather than a legal promise until the actual instrument and hiring plan are known.

## Recommended replacement architecture

### True founders

Use:

- manager-managed Operating Agreement;
- Founder Unit Purchase/Subscription Agreement;
- founder vesting/repurchase provisions;
- IP/confidentiality/invention assignment;
- tax/securities closing set.

### Long-term execution leaders

Evaluate:

- profits-interest/incentive units if partner/K-1 treatment is acceptable; or
- phantom equity if the company wants economic alignment without actual membership.

### Short-term/intermittent execution contributors

Prefer:

- cash project bonus/profit share;
- potentially phantom credits;
- actual equity only by explicit exception.

### Sales leader

Prefer at launch:

- cash commission / collected-revenue incentive;
- possible long-term incentive after relationship/status is settled;
- do not assume Rule 701 covers an independent salesperson.

## Suggested rewrite of the core principle

Replace:

> No equity vests without a real, qualifying business event.

With:

> No performance-based incentive is earned unless the written plan's objective performance conditions are satisfied. Founder ownership and founder vesting are governed separately by the founder ownership documents. Any actual equity issuance requires formal approval, applicable tax and securities compliance, and entry in the company's ownership ledger.

This preserves the philosophy without creating the wrong legal inference.

## Suggested rewrite of attribution authority

Replace a unilateral/finality clause with a structure similar to:

> The Plan Administrator will determine performance credits and incentive calculations in good faith under the written plan, using the company's contemporaneous accounting, CRM, project, delivery, and customer-acceptance records. A participant may identify objective calculation or factual errors within the stated review period. The Plan Administrator's determination after review will control for plan administration, subject to the Operating Agreement, the governing award agreement, applicable law, and any independent-accountant procedure expressly provided by the plan.

This is example architecture for counsel to refine, not executable contract language.

## What can remain from the current documents

Retain as business concepts:

- founder control objective;
- non-equal default ownership philosophy;
- sales/execution separation;
- performance-based incentives;
- contribution-margin concept;
- individual caps;
- future reserve;
- no ownership for vague future promises;
- explicit contract authority;
- need for counsel/tax review.

Do not treat the present percentage or contract language as approved until the legal/tax structure is settled.

## Next action

Use `02-FOUNDER-EQUITY-AND-INCENTIVE-DESIGN.md` as the design brief for counsel. Counsel should return with at least two executable alternatives:

1. **Illinois manager-managed LLC + partnership tax + profits-interest/incentive plan**; and
2. **Illinois manager-managed LLC + founder units + phantom/cash incentive plan**, with an explanation of whether an S-corporation election could later be made without breaking the economics.

Compare administrative cost, founder control, tax treatment, recipient experience, future hiring, and acquisition/financing diligence before approval.
