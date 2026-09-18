# 2026 Current-Law Validation Notes

## Source and status

- **Status:** current-law validation supplement; not legal advice and not an approved founder decision
- **Validation date:** 2026-08-19
- **Purpose:** capture high-change legal/tax rules that materially affect formation, equity, workers, Chicago operations, cloud resale, and regulated clients
- **Revalidation:** re-check these items immediately before formation, first equity grant, first worker engagement, and first cloud/software resale

This file supplements the durable architecture in `docs/legal/00-LEGAL-ARCHITECTURE-OVERVIEW.md` through `06-COUNSEL-AND-CPA-CLOSING-CHECKLIST.md`. Where a future law change conflicts with this note, the current official source controls.

## 1. Illinois LLC control is an Operating Agreement problem, not a percentage problem

Illinois currently provides that an LLC is member-managed unless the Operating Agreement expressly establishes manager management. In a member-managed LLC, each member has equal management rights by default. In a manager-managed LLC, ordinary business is managed by the manager or managers, but the statute also contains default rules for manager appointment/removal and member consent on specified matters.

### Design consequence

Do not rely on `51% ownership` as a complete control mechanism.

Counsel should expressly design:

- manager-managed status;
- initial manager designation;
- appointment/removal/replacement rights;
- manager vacancies;
- voting classes, if used;
- reserved matters;
- issuance/admission authority;
- amendment mechanics;
- conflict/related-party procedures;
- transfer/buyout/departure rules.

A percentage target can sit on top of that governance architecture, but it should not substitute for it.

### Minority/member rights remain relevant

Illinois currently gives members statutory information rights and permits judicial relief when managers or controlling members act illegally, fraudulently, or oppressively in a directly harmful manner. A court may order a remedy including a buyout rather than dissolution.

Therefore terms such as `sole discretion`, `final and binding`, and `not subject to appeal` should be used carefully. For incentive attribution, prefer a written formula, source records, good-faith determination, correction process, conflict procedure, and preservation of nonwaivable rights.

### Official sources

- Illinois Limited Liability Company Act, 805 ILCS 180/15-1: https://ilga.gov/documents/legislation/ilcs/documents/080501800K15-1.htm
- Member information rights, 805 ILCS 180/10-15: https://www.ilga.gov/legislation/ILCS/details?ActID=2290&ActName=Limited+Liability+Company+Act.&ChapAct=805%20ILCS%20180/
- Judicial dissolution/oppression remedies, 805 ILCS 180/35-1: https://www.ilga.gov/documents/legislation/ilcs/documents/080501800K35-1.htm

## 2. Profits interests can solve one problem while creating tax-partner administration

IRS guidance continues to distinguish a capital interest from a profits interest. A qualifying profits interest issued for services may fall within the Rev. Proc. 93-27 safe harbor. Rev. Proc. 2001-43 permits certain substantially nonvested profits interests to be treated as received on the grant date when the partnership and recipient satisfy specified treatment conditions.

### Design consequence

Profits interests are a strong candidate for a **small number of long-term, partner-like contributors**, but not a free substitute for cash compensation.

Expect counsel/CPA to address:

- liquidation hurdle/current value;
- grant-date valuation;
- vesting;
- capital accounts and allocations;
- tax distributions;
- K-1 administration;
- service-provider tax status;
- Section 83/83(b) treatment where relevant;
- state nonresident filings/withholding;
- securities-law exemption.

Do not award a profits interest to someone merely because the company wants to call the award `non-voting equity`.

### Official sources

- IRS Publication 541: https://www.irs.gov/publications/p541
- IRS discussion of Rev. Proc. 93-27 and Rev. Proc. 2001-43: https://www.irs.gov/irb/2005-24_IRB
- IRS Publication 525 / restricted property and Section 83(b): https://www.irs.gov/publications/p525

## 3. Rule 701 is useful but not a generic independent-salesperson exemption

SEC Rule 701 currently provides a compensatory securities exemption for eligible private-company grants to employees and qualifying consultants/advisors. The SEC's consultant/advisor requirements are narrower than `any contractor`: the person must be a natural person providing bona fide services, and the services cannot be in connection with capital raising or promoting/maintaining a securities market.

The SEC's Rule 701 adopting material also distinguishes independent salespersons who lack an employment relationship from the consultant/advisor category.

### Design consequence

For early outside sales roles:

- use a clearly drafted cash commission plan by default;
- do not promise equity before securities counsel identifies the exemption;
- if actual securities are awarded, document recipient status, plan authority, exemption, disclosures, state-law compliance, approval, tax treatment, and ledger entry.

### Official sources

- SEC Rule 701 overview: https://www.sec.gov/resources-small-businesses/exempt-offerings/employee-benefit-plans-rule-701-0
- SEC Rule 701 consultant/advisor requirements: https://www.sec.gov/rules-regulations/1999/02/rule-701exempt-offerings-pursuant-compensatory-arrangements

## 4. Domestic BOI filing is currently not a formation task

FinCEN currently states that entities created in the United States and their beneficial owners are exempt from Corporate Transparency Act beneficial-ownership-information reporting under the March 2025 interim final rule.

### Design consequence

Do not copy an older startup checklist that automatically requires a newly formed domestic Illinois LLC to file a BOI report.

Instead:

- re-check FinCEN on the actual formation date;
- record the current determination in the formation closing checklist;
- do not submit unnecessary ownership data merely because an old template says to do so.

### Official source

- FinCEN BOI current guidance: https://www.fincen.gov/boi

## 5. Illinois partnership taxation has special multi-state consequences

Illinois currently taxes partnerships through a 1.5% replacement tax while income tax generally passes to the partners. Illinois also provides an elective PTE tax currently calculated at 4.95% and requires pass-through withholding/payments for many nonresident partners when a PTE election does not apply.

Illinois enacted additional PTE computation choices for tax years ending on or after December 31, 2026.

### Design consequence

Michigan-resident owners make the tax-distribution and withholding design more than boilerplate.

Before final ownership is signed, the CPA should model:

- Illinois replacement tax;
- Illinois PTE election under 2026 law;
- Illinois-source income of nonresident owners;
- pass-through withholding;
- Michigan owner returns/credits;
- guaranteed payments;
- self-employment tax;
- tax distributions;
- cash retained by the business.

### Illinois 2026 QSBS change

For tax years ending on or after December 31, 2026, Illinois has decoupled from the federal IRC Section 1202 exclusion for qualified small business stock gains. If a future Delaware C-corporation conversion is evaluated partly for federal QSBS treatment, do not assume Illinois will provide the same exclusion.

### Official sources

- IDOR partnership tax overview: https://tax.illinois.gov/research/taxinformation/income/partnership.html
- IDOR pass-through entity guidance: https://tax.illinois.gov/research/publications/pubs/pass-through-information.html
- IDOR July 2026 tax-change bulletin: https://tax.illinois.gov/research/publications/bulletins/fy-2027-01.html

## 6. Michigan is an activity/nexus workstream, not merely a founder-address field

Michigan LARA currently states that a foreign LLC that is `transacting business` in Michigan must obtain a Certificate of Authority and emphasizes that the phrase is technical, depends on proposed activities, statutory exclusions, and applicable decisions.

### Design consequence

Do not conclude either of the following from residence alone:

- `a Michigan founder automatically requires foreign qualification`; or
- `a remote Michigan founder can never create Michigan obligations`.

Create a trigger review when the company develops regular Michigan employees, held-out locations, recurring local customer delivery, company property, payroll accounts, or other significant Michigan operations.

### Official source

- Michigan LARA foreign LLC guidance: https://www.michigan.gov/lara/bureau-list/cscl/corps/limited-liability-co/types/foreign-limited-liability-company

## 7. Worker classification is a major risk in the proposed execution pool

The business model contemplates contributors doing the company's core implementation and delivery work. Merely labeling these contributors `independent contractors` is not determinative.

Illinois unemployment law currently presumes service by an individual is employment unless all three statutory elements are established: freedom from control/direction, service outside the usual course or outside all places of business, and an independently established trade/occupation/profession/business.

At the federal level, Department of Labor guidance is unusually fluid in 2026. On February 26, 2026, DOL proposed rescinding the 2024 independent-contractor rule and states that it is no longer applying the 2024 rule in its investigations while the 2026 rulemaking is pending.

### Design consequence

Before onboarding a recurring execution contributor, run a classification review that separately covers:

- IRS employment tax;
- FLSA/current DOL position;
- Illinois unemployment;
- Illinois wage/leave/freelance rules;
- workers compensation;
- Michigan law if the worker is there;
- benefits/payroll treatment;
- whether an LLC profits-interest award would make the person a tax partner.

The core delivery team is the group least suited to a casual `everyone is a 1099` assumption.

### Official sources

- Illinois Unemployment Insurance Act, 820 ILCS 405/212: https://www.ilga.gov/Documents/legislation/ilcs/documents/082004050K212.htm
- U.S. DOL 2026 rulemaking: https://www.dol.gov/agencies/whd/flsa/misclassification/2026rulemaking
- IRS worker classification: https://www.irs.gov/businesses/small-businesses-self-employed/independent-contractor-self-employed-or-employee

## 8. Illinois restrictive covenants require more than a signature

For employee agreements entered into under current Illinois law:

- a noncompete is barred unless annualized earnings exceed $75,000 in 2026;
- a nonsolicit is barred unless annualized earnings exceed $45,000 in 2026;
- those thresholds increase to $80,000 and $47,500 on January 1, 2027;
- enforceability also requires adequate consideration, an employment relationship, legitimate business interest, no undue hardship, and no public injury;
- the employer must advise the employee in writing to consult an attorney and provide at least 14 calendar days before employment or at least 14 days to review, although the employee may voluntarily sign earlier.

### Design consequence

Do not make a broad noncompete the default IP/confidentiality protection. Build protection first around:

- confidentiality;
- trade-secret controls;
- IP assignment;
- customer/data access rules;
- narrowly justified nonsolicitation/noncompetition only where current law and actual role support it.

### Official sources

- 820 ILCS 90/10: https://ilga.gov/documents/legislation/ilcs/documents/082000900K10.htm
- 820 ILCS 90/15: https://www.ilga.gov/documents/legislation/ilcs/documents/082000900K15.htm
- 820 ILCS 90/20: https://www.ilga.gov/documents/legislation/ilcs/documents/082000900K20.htm

## 9. Chicago business licensing is a real launch dependency

Chicago's current code states that all businesses must be licensed to operate in the City unless another regulated/specific license, preemption, or permit applies. The Limited Business License fee is $500 as of January 1, 2026 and is generally assessed every two years; CPI adjustments begin in January 2027.

If a Chicago residence is actually used as the business location, the home-occupation rules must also be checked. The code distinguishes a true home occupation from an owner/employee merely doing administrative, clerical, or research work from home for an entity whose principal place of business is elsewhere.

### Design consequence

Before formation is treated as `launch complete`, document:

- principal business location;
- whether that address is held out publicly;
- applicable Chicago license category;
- home-occupation/zoning status where relevant;
- license issuance or written exemption/determination.

### Current code sources

- Chicago Municipal Code § 4-4-020: https://codelibrary.amlegal.com/codes/chicago/latest/chicago_il/0-0-0-2608842
- Chicago Municipal Code § 4-5-010: https://codelibrary.amlegal.com/codes/chicago/latest/chicago_il/0-0-0-2609232
- Chicago Municipal Code § 4-6-270: https://codelibrary.amlegal.com/codes/chicago/latest/chicago_il/0-0-0-2610163

## 10. Chicago cloud/software tax can directly affect the reseller model

Chicago's current Personal Property Lease Transaction Tax defines `nonpossessory computer lease` to include remote access to a provider's computer/software to input, modify, or retrieve data without more than de minimis provider intervention. The ordinance currently imposes a 15% tax on taxable leases/rentals.

For a nonpossessory computer lease, mandatory ancillary services can be included in the taxable lease price even if separately stated; a service is treated as optional only when the customer could obtain the same computer lease from the same lessor without that service.

Chicago also has specific exemptions, including a small-new-business exemption for qualifying nonpossessory computer leases. The exemption has detailed conditions and documentation requirements; do not assume eligibility without tax review.

The ordinance also provides a re-lease mechanism where the lessee in turn acts as lessor and supplies specified documentation.

### Design consequence

Before the first material Microsoft/cloud resale transaction, have a state/local tax professional approve:

- distributor vs. reseller/agent role;
- tax-collection party;
- Chicago customer sourcing;
- re-lease/resale documentation;
- small-new-business exemption eligibility, if relevant;
- mandatory vs. optional service packaging;
- invoice design;
- registrations and returns;
- customer exemption documentation;
- contract tax-change language.

### Current code sources

- Definitions, § 3-32-020: https://codelibrary.amlegal.com/codes/chicago/latest/chicago_il/0-0-0-2606446
- 15% rate, § 3-32-030: https://codelibrary.amlegal.com/codes/chicago/latest/chicago_il/0-0-0-2606475
- Exemptions, § 3-32-050: https://codelibrary.amlegal.com/codes/chicago/latest/chicago_il/0-0-0-2606488
- Re-lease, § 3-32-060: https://codelibrary.amlegal.com/codes/chicago/latest/chicago_il/0-0-0-2606508
- Collection/remittance, § 3-32-070: https://codelibrary.amlegal.com/codes/chicago/latest/chicago_il/0-0-0-2606512
- Registration, § 3-32-090: https://codelibrary.amlegal.com/codes/chicago/latest/chicago_il/0-0-0-2606523
- Illinois lease-tax FAQ: https://tax.illinois.gov/research/publications/pubs/lease-tax-faqs.html

## 11. Healthcare clients can make the company a HIPAA business associate

HHS currently identifies an IT contractor/MSP that creates, receives, maintains, or transmits ePHI while performing maintenance/support as a business associate. HHS also states that a cloud provider can be a business associate even when data is encrypted and the provider lacks the decryption key.

Mere sale of software, without PHI access, does not by itself make the vendor a business associate.

### Design consequence

For the proposed physician/clinic lane:

- determine BA status during discovery;
- execute a BAA before BA-level PHI access;
- flow BA requirements to applicable subcontractors;
- ensure privileged-support practices actually support the BAA;
- separate software resale from PHI-accessing support where facts permit;
- do not market `HIPAA compliant` as a generic product certification.

### Official sources

- HHS business associates: https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/business-associates/index.html
- HHS cloud guidance: https://www.hhs.gov/hipaa/for-professionals/special-topics/health-information-technology/cloud-computing/index.html
- HHS software vendor FAQ: https://www.hhs.gov/hipaa/for-professionals/faq/256/is-software-vendor-business-associate/index.html

## 12. CPA/tax-preparer clients can impose FTC Safeguards Rule vendor obligations

The FTC Safeguards Rule requires covered financial institutions to maintain a written information-security program and to oversee service providers. Current FTC guidance states that covered institutions must select service providers capable of safeguarding customer information, put security expectations in contracts, monitor them, and periodically reassess their suitability.

### Design consequence

For the proposed CPA/accounting lane, expect customers to request real vendor-security evidence, not merely an NDA.

Prepare reusable evidence around:

- written security program;
- identity/MFA/access control;
- encryption;
- asset/data inventory;
- vulnerability management;
- incident response;
- security awareness;
- subcontractor controls;
- business continuity;
- insurance;
- security-review evidence.

### Official source

- FTC Safeguards Rule guidance: https://www.ftc.gov/business-guidance/resources/ftc-safeguards-rule-what-your-business-needs-know

## 13. Recommended legal implementation order

The legal work should now proceed in this order:

1. **Founder classification:** identify true founders/owners versus incentive participants.
2. **Economic term sheet:** settle ownership targets, service expectations, founder vesting, capital, compensation, and exit rules.
3. **Entity/tax memo:** Illinois LLC/partnership recommendation validated against actual founders and Michigan residency.
4. **Operating Agreement architecture:** manager control, member votes, conflicts, transfers, tax distributions, admissions/issuances, exits.
5. **Founder issuance:** founder purchase/restricted-unit/IP documents and tax workflow.
6. **Incentive selection:** profits interests versus phantom/cash/hybrid; do not issue ad hoc ordinary units per deal.
7. **Worker classification:** determine employee/contractor/partner status before services begin.
8. **Commercial contract stack:** MSA/SOW/change order/security/access/managed-service/subcontractor modules.
9. **Chicago launch review:** license/location plus cloud/software tax design.
10. **Michigan trigger review:** qualification/payroll/withholding/unemployment/workers-compensation before material Michigan operations.
11. **Regulated-client modules:** HIPAA/BAA, FTC/GLBA service-provider terms, law-firm confidentiality, BIPA where triggered.
12. **Insurance alignment:** bind E&O/cyber/general liability/workers compensation as applicable and align contract caps/indemnities.

## Counsel instruction

The research in this repository is intended to make professional review faster and more precise. It is not intended to replace counsel.

Ask counsel to identify explicitly:

- which recommendations are accepted as written;
- which are changed and why;
- which statutory rules cannot be modified by the Operating Agreement;
- which equity instrument is selected;
- which securities exemption applies to each founder/incentive category;
- which state registrations are required on day one;
- which items are deferred until a stated trigger.

Store the executed confidential documents outside the public GitHub repository and keep only sanitized architecture/status records here.
