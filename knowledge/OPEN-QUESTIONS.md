# Open Questions

These are the genuine unresolved decisions. Do not re-list established business architecture as if it were unknown.

## Name and legal identity

- What is the final legal and public company name?
- Are the name, domain, and marks available and acceptable?
- `CompuCorp` is a temporary project codename only; continue using `[COMPANY_NAME]` in canonical legal/business documents until the final name is approved.

## Founder governance

- Who are the legal founders and owners?
- Which early contributors should be true owners versus incentive-plan participants only?
- Is the 51% controlling-founder target still the intended economic and/or fully diluted voting target?
- What founder vesting schedule applies to each true founder?
- How should significant pre-formation work be credited, if at all?
- What capital contributions and cash commitments apply?
- What decisions require manager authority, member approval, unanimity, majority, or function-level authority?
- How is the manager appointed and removed?
- What happens upon departure, disability, death, divorce, bankruptcy, deadlock, or sale?
- What repurchase/call rights apply to vested and unvested founder interests?
- Who owns pre-existing and newly created intellectual property?
- Who can bind the company contractually and at what spending/contract thresholds?

## Entity, tax, and incentive architecture

### Proposed direction awaiting founder/professional approval

`docs/decisions/ADR-0005-ENTITY-JURISDICTION-AND-INCENTIVE-ARCHITECTURE.md` proposes:

- Illinois manager-managed LLC;
- initial federal partnership tax treatment;
- founder control encoded in the Operating Agreement rather than relying on a percentage alone;
- true founder ownership separated from contributor incentives;
- profits-interest/incentive units compared with phantom equity for long-term contributors;
- cash commission/profit-sharing preferred for shorter-term contributors unless actual equity is deliberately approved;
- Delaware deferred absent a concrete financing/investor reason;
- Michigan registration/payroll/tax obligations triggered by actual Michigan activity.

### Questions to approve or revise

- Do the founders approve Illinois as the formation state subject to counsel validation?
- Do the founders approve a manager-managed rather than member-managed Illinois LLC?
- Should there be one controlling manager or a small manager board?
- Is partnership tax treatment the correct launch classification after the CPA models actual founder economics?
- Should long-term contributor incentives use profits interests, phantom equity, cash incentives, or a hybrid?
- How many people should actually become legal LLC members/partners?
- Is a later S-corporation election a likely goal, and would the selected economic rights remain compatible?
- Is institutional outside equity financing reasonably expected within 24–36 months, creating a reason to reconsider Delaware/C-corporation structure?
- Who administers the incentive plan and attribution process?
- What tax-distribution policy applies if the company is partnership-taxed?
- What federal and state securities-exemption process will counsel use for founder and incentive grants?

## Multi-state operations

- Which founders/employees/contractors will regularly work from Michigan?
- Will any Michigan residence or office be represented publicly as a company location?
- At what activity threshold does counsel require Michigan foreign qualification?
- Which Michigan payroll, withholding, unemployment, and workers-compensation registrations are required before the first Michigan employee begins work?
- How will Illinois/Michigan owner-state and employee reciprocity rules be handled by payroll/tax providers?

## Legal, tax, finance, and risk

- Which registrations are required at formation and at first hire/customer?
- What Chicago business-license/location requirements apply to the actual principal operating location?
- What insurance limits and coverages are appropriate for technology E&O, cyber, general liability, workers compensation, crime/social engineering, and D&O if needed?
- What contract liability cap/indemnity positions are acceptable and insurable?
- What startup capital and cash reserve are required?
- What financial controls and reporting cadence apply?
- What secure corporate-record system will hold executed confidential legal/tax documents rather than relying on GitHub?

## Cloud, software, and reseller tax

- Will `[COMPANY_NAME]` act as reseller/lessor, agent, billing intermediary, or referral partner for Microsoft/cloud subscriptions?
- Who is legally responsible for collecting/remitting Chicago Personal Property Lease Transaction Tax where applicable?
- How do Chicago sourcing rules apply to customer users/locations?
- Which Illinois software-license/lease-tax exclusions or exemptions apply?
- What resale/re-lease documentation is required?
- Are governance/support services truly optional or contractually mandatory with the cloud subscription?
- How should invoices separate software/cloud, optional services, tax, and pass-through charges?
- Which distributor/CSP contract terms shift or retain tax responsibility?

## Workforce and intellectual property

- Which early contributors are employees versus independent contractors based on actual working facts?
- Which contractor engagements trigger the Illinois Freelance Worker Protection Act?
- Which restrictive covenants, if any, are genuinely necessary and lawful for Illinois/Michigan workers?
- What Illinois Employee Patent Act notice and assignment language applies to employees?
- Have all founder/contributor agreements included the federal DTSA whistleblower-immunity notice?
- What pre-existing/background IP is each founder/contributor bringing?
- What reusable company tools/templates/scripts remain company IP versus customer-owned bespoke deliverables?

## Customer contract and regulated-data triggers

- What is the approved liability/insurance position for the MSA?
- Which services require a dedicated managed-services schedule or SLA?
- What administrative-access authority may consultants exercise without additional customer approval?
- What incident notification commitments can operations actually meet?
- What triggers a HIPAA Business Associate Agreement?
- What financial-sector customer requirements are expected under GLBA/FTC Safeguards Rule vendor-management provisions?
- How will biometric data be avoided or handled if BIPA is implicated?
- What additional confidentiality/security terms will law-firm customers require?

## Launch sequencing

### Proposed direction awaiting founder approval

- Chicago and Chicagoland first
- Four parallel prospect tracks: physicians/clinics, CPA and accounting firms, construction/field services, and legal or other regulated professional firms
- Paid Technology and Security Baseline Assessment first, with optional one-week business-systems and vertical-risk modules
- Migration or takeover work requires assessment evidence first and separate scope
- See `docs/launch/07-CHICAGO-MARKET-AND-MICROSOFT-ASSESSMENT-BRIEF.md`

### Questions to approve or revise

- Is the four-track Chicago test the approved first 90-day market experiment?
- Is the paid Technology and Security Baseline Assessment the approved entry offer?
- Should the Microsoft baseline remain one week, with business-systems, vertical-risk, and migration modules separately scoped?
- What is the minimum evidence required before publishing assessment or implementation pricing?
- Which Foundation tier should follow a successful assessment: Core, Full, Complex, or a custom sequenced approach?

## Commercial model and pricing

- What is the approved price for the core assessment and each optional module?
- What is the approved launch pricing for Foundation Core, Full Foundation, and Complex Foundation engagements?
- What conditions require change orders, add-ons, or re-pricing for legacy tenant takeover, migration, or backup complexity?
- What minimum evidence is required before quoting greenfield tenant work at the full fixed-fee standard?

## Managed-service boundary

- Which support requests are included?
- What hours and response targets apply?
- Is end-user help desk included, optional, or referred?
- What prerequisites are required before taking operational responsibility?
- What is excluded or separately project-priced?

## Commercial controls

- What gross-margin targets apply?
- Which costs are pass-through?
- What deposits, payment terms, and suspension rules apply?
- How are license-price changes handled?
- What discount and change-order authority applies?
- Is 100% upfront the default payment rule, and who may approve exceptions?

## Partnerships and distribution

- Which Microsoft partner pathway is appropriate under current program rules?
- Which distributor/indirect CSP best supports the company?
- Which capabilities must be internal, subcontracted, or referred?
- Which initial partners are qualified?
- How are customer ownership, referral economics, confidentiality, liability, and independence handled?

## Internal operating stack

- Which specific products will support CRM, quoting, project/service management, documentation, accounting, security, secrets, and automation?
- Which system is authoritative for each information object?
- What can be delayed until after the first pilots?

## Execution

- Who is the first pilot customer?
- What launch date and capacity are realistic?
- What founder time commitment is available?
- Which metrics define successful first-quarter execution?
- What are Bernard Cole's (Ben's) and Michael's formal titles, availability, and authority? Bernard's relevant Microsoft and operations experience is documented from the supplied profile; confirm the intended company role separately.
- Who is the named project lead for each pilot, and what does shared acceptance ownership mean in practice?
- How much weekly capacity can Bernard, Michael, and Harvey commit during the first 90 days?
