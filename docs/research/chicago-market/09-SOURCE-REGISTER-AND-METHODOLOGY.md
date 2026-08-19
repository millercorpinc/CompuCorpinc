# Source Register and Methodology

## Source and status

- **Status:** research provenance and limitations register
- **Date:** 2026-08-19
- **Purpose:** make the Chicago market research reproducible and prevent modeled assumptions from becoming undocumented “facts.”

## Evidence taxonomy

### Measured

A value or requirement directly reported by an identified source.

Examples:

- Census establishment count;
- SBA employer count;
- association membership count;
- published competitor price range;
- IRS statement about WISP requirements.

### Derived

Arithmetic based only on measured values.

Examples:

- combined sector counts;
- percentage of national nonemployers above a receipt threshold;
- average receipts from total receipts / establishment count.

### Scenario

A calculation containing one or more assumptions not measured from the target market.

Examples:

- applying national nonemployer receipt distribution to Chicago;
- assuming 20% of broad-sector employer firms qualify;
- assuming 7.5% are in market in a year;
- assuming $18,000 first-year revenue.

### Hypothesis

A strategic interpretation to be tested.

Examples:

- 2–9-person law/accounting firms may be a sweet spot;
- incumbent-MSP coexistence may reduce sales friction;
- a productized microbusiness baseline may occupy white space.

## Primary economic sources

### SBA Office of Advocacy — Chicago metro profile

**Use:** common-year small-business structure, employer/nonemployer counts, industry, employment, payroll, lending.

**Source:** U.S. Small Business Administration, Office of Advocacy, *2025 Small Business Profiles for Major Metropolitan Areas*.

https://advocacy.sba.gov/2025/10/28/2025-small-business-profiles-for-major-metropolitan-areas/

**Underlying data:** Census SUSB and Nonemployer Statistics plus federal lending sources.

**Strength:** official federal synthesis and best common-year top-level Chicago baseline.

**Limitation:** broad industry groups; small-business definition can extend to 500 employees; not the same thing as the company's ICP.

### Census Nonemployer Statistics, 2023

**Use:** national nonemployer count, receipts, receipt-size distribution, legal form, metro nonemployer counts/receipts where published.

https://www.census.gov/programs-surveys/nonemployer-statistics.html

Data table:

https://data.census.gov/table/NONEMP2023.NS2300NONEMP

Datasets/API documentation:

https://www.census.gov/programs-surveys/nonemployer-statistics/data/datasets.html

**Strength:** canonical zero-payroll business dataset.

**Limitations:** receipt-size-class detail is not uniformly available at metro geography; receipts are gross business receipts, not owner income or profit.

### Census Statistics of U.S. Businesses, 2022

**Use:** firm/establishment counts, employment, annual payroll, receipts, enterprise size and 3-digit NAICS for MSAs.

https://www.census.gov/data/tables/2022/econ/susb/2022-susb-annual.html

**Important source note:** Census revised the 2022 MSA-by-3-digit-NAICS table in July 2025 to remove extraneous estimates. Use the revised file, not the file labeled OLD.

**Strength:** best next dataset for employer market economics and size bands.

**Limitation:** latest currently available SUSB annual release is 2022; MSA detail is 3-digit rather than full 6-digit NAICS.

### Census County Business Patterns, 2023

**Use:** more current employer-establishment counts, employment, payroll, NAICS and establishment employment-size class by MSA.

https://www.census.gov/programs-surveys/cbp/data.html

API variables:

https://api.census.gov/data/2023/cbp/variables.html

**Strength:** current detailed establishment structure.

**Limitation:** establishment size is not identical to enterprise/firm size; Census API currently requires a key for direct queries.

## Secondary economic cross-check

### Postal small-business metro synthesis

**Use:** newer employer/nonemployer summary values and cross-metro comparison.

https://www.usepostal.com/blog/us-areas-with-most-small-businesses

**Status:** secondary synthesis of Census/SBA data.

**Use rule:** directional cross-check only; prefer federal sources for canonical values.

## Accounting/tax/security sources

### IRS — Written Information Security Plans

IRS Tax Tip 2026-49, June 16, 2026:

https://www.irs.gov/newsroom/written-information-security-plans-are-essential-for-tax-pros

**Use:** current confirmation that WISPs are required and descriptions of core plan requirements.

### IRS — Protect Your Clients; Protect Yourself

https://www.irs.gov/tax-professionals/protect-your-clients-protect-yourself

**Use:** current tax-professional security resource hub; updated July 2026.

### FTC — Safeguards Rule

https://www.ftc.gov/business-guidance/resources/ftc-safeguards-rule-what-your-business-needs-know

**Use:** covered financial-institution examples, security-program requirements, service-provider obligations.

### Illinois CPA Society

https://www.icpas.org/about

**Use:** Illinois professional ecosystem/membership scale and membership composition.

**Limitation:** members are people, not firms; not every member is a prospect or located in the Chicago metro.

## Legal-market sources

### Illinois State Bar Association / ARDC private-practice structure

https://www.isba.org/ibj/2024/07/lawpulse/changingrolls

**Use:** private-practice lawyer counts and firm-size distribution.

**Limitation:** attorney count is not firm count; 2023 is the referenced data year.

### American Bar Association — 2024 Solo and Small Firm TechReport

https://www.americanbar.org/groups/law_practice/resources/tech-report/2024/2024-solo-and-small-firm-techreport/

**Use:** technology decision authority, budgets, support patterns, security maturity and small-firm technology behavior.

### ABA — 2024 Practice Management TechReport

https://www.americanbar.org/groups/law_practice/resources/tech-report/2024/2024-practice-management-techreport/

**Use:** technology-spend and practice-management signals by firm size.

### Chicago Bar Association

https://www.chicagobar.org/

**Use:** education/channel ecosystem and practice-management technology programming.

## Healthcare sources

### HHS HIPAA Security guidance

https://www.hhs.gov/hipaa/for-professionals/security/guidance/index.html

### HHS risk-analysis guidance

https://www.hhs.gov/hipaa/for-professionals/security/guidance/guidance-risk-analysis/index.html

### HHS cybersecurity/ransomware guidance

https://www.hhs.gov/hipaa/for-professionals/security/guidance/cybersecurity/index.html

**Use:** security requirements/readiness context, including small-provider resources.

### CMS NPPES/NPI downloadable files

https://download.cms.gov/nppes/NPI_Files.html

**Use:** healthcare provider/entity identity and practice-location data.

**Important limitation:** CMS explicitly says an NPI does not validate licensure or credentialing.

### Chicago Medical Society

https://www.cmsdocs.org/membership

**Use:** Chicago-area physician professional ecosystem signal.

**Limitation:** member/represented physician count is not a firm/practice count.

## Construction sources

### Chicagoland Associated General Contractors

https://chicagolandagc.org/about-us/

**Use:** member profile and aggregate construction-volume/employment signal.

Directory:

https://chicagolandagc.org/membership-directory/

**Limitation:** association members are a selected subset of the full Chicago construction market and include suppliers/professional services as well as contractors.

## Real-estate sources

### Chicago Association of REALTORS

https://chicagorealtor.com/membership/

**Use:** local professional ecosystem scale.

Advertising/sponsorship:

https://chicagorealtor.com/about-us/advertise-with-the-chicago-association-of-realtors/

**Use:** direct channel-access evidence.

### Illinois REALTORS

https://www.illinoisrealtors.org/about/

**Use:** statewide professional ecosystem scale.

### Illinois REALTORS 2026 scam warning

https://www.illinoisrealtors.org/blog/scam-alert-beware-of-virtual-meetings-with-fraudsters-posing-as-buyers/

**Use:** current example of cybersecurity targeting real-estate professionals.

## Architecture/engineering source

### AIA Chicago

Sponsor/membership statistics:

https://aiachicago.org/sponsor/

Small Firm Exchange / affinity groups:

https://aiachicago.org/affinitygroups/

**Use:** reachable architecture/design ecosystem and small-firm channel.

**Limitation:** membership is not firm count.

## Nonprofit sources

### IRS Exempt Organizations Business Master File

https://www.irs.gov/charities-non-profits/exempt-organizations-business-master-file-extract-eo-bmf

**Use:** canonical nonprofit/entity source for a future Chicago lead/denominator pipeline.

### Chicago Social Impact Atlas

https://caparipartners.com/atlas

**Use:** regional synthesis of April 2026 IRS Business Master File showing approximately 42,000 active 501(c)(3) organizations across the 13-county Chicago region.

**Status:** secondary analysis built from official IRS source data.

**Limitation:** nonprofit existence is not evidence of budget, staff, technology complexity, or serviceability.

## Cyber-risk sources

### CISA — Small and Medium-Sized Business Resources

https://www.cisa.gov/small-and-medium-sized-business-resources

**Use:** current small-business security guidance and core safeguards.

### CISA — StopRansomware Guide

https://www.cisa.gov/stopransomware/ransomware-guide

**Use:** ransomware resilience, backup, testing, response.

### FBI — 2025 Internet Crime Report

https://www.fbi.gov/file-repository/2025_ic3report.pdf/view

**Use:** current complaint/loss scale and cyber-enabled fraud patterns.

### FBI — Business Email Compromise

https://www.fbi.gov/how-we-can-help-you/scams-and-safety/common-frauds-and-scams/business-email-compromise

**Use:** BEC scenarios and recommended verification/security practices.

### FTC — Cybersecurity for Small Business

https://www.ftc.gov/business-guidance/small-businesses/cybersecurity

**Use:** small-business security and cyber-insurance framing.

## Commercial claims/insurance source

### Coalition 2026 Cyber Claims Report

https://www.coalitioninc.com/announcements/2026-cyber-claims-report

**Use:** current insured-portfolio claims patterns such as BEC/funds-transfer-fraud/ransomware severity.

**Status:** commercial insurer data.

**Critical limitation:** Coalition policyholders are not a representative sample of all U.S. or Chicago small businesses. Never convert Coalition claim frequency into a Chicago SMB prevalence statistic.

## Competitor/pricing sources

### Framework IT — Chicago pricing guide, updated April 2026

https://www.frameworkit.com/blog/managed-it-services-cost-chicago

### Links Technology — Illinois MSP pricing guide, May 2026

https://www.linkstechnology.com/blog/how-much-does-a-managed-service-provider-actually-cost-in-illinois-2026-pricing-guide

### Datastrive — managed IT pricing guide, May 2026

https://datastrive.com/managed-it-services-pricing-guide/

### Representative Chicago IT competitors

- PSM Partners: https://www.psmpartners.com/chicago-it-company/
- PSM law firms: https://www.psmpartners.com/law-firm-it-service-support/
- ArchiTechture: https://www.architechture.tech/
- CTS law firms: https://www.onlinects.com/industries-served/law-firms/
- CTI law firms: https://www.ctinc.com/it-services-law-firms-chicago/
- GO Technology/eDiscovery: https://gochicagoit.com/managed-it-services/ediscovery-software-support/

**Status:** vendor-authored commercial claims.

**Use rule:** competitor positioning and published price signals only. Do not treat as independent evidence of service quality, customer satisfaction, actual realized prices, or market averages.

## Public lead-data sources

### City of Chicago current active business licenses

https://data.cityofchicago.org/Community-Economic-Development/Business-Licenses-Current-Active/uupf-x98q

**Use:** Chicago business identity/location/license leads.

**Limitation:** licenses are not one-to-one with businesses; not all target firms require the same license; does not cover suburbs.

### City of Chicago historical Business Licenses

https://data.cityofchicago.org/Community-Economic-Development/Business-Licenses/r5kz-chrr

**Use:** historical/current license data and linkage to business-owner data.

### Illinois Secretary of State business entity search

https://apps.ilsos.gov/businessentitysearch/

**Use:** legal-entity validation/enrichment.

### IDFPR license lookup

https://idfpr.illinois.gov/checklicense.html

**Use:** licensed professional/entity identification and verification; bulk lookup is available for supported divisions.

IDFPR active license reports:

https://idfpr.illinois.gov/dpr/active-license-report.html

## Key analytical limitations

### 1. “Small business” is broader than the company's target

Federal small-business tables often include employers up to 499 employees. The company's target is much narrower.

### 2. Business, firm, establishment, license, professional, and member are different units

Never add these together casually.

- **Firm:** enterprise/business organization.
- **Establishment:** one physical/economic location.
- **Nonemployer establishment:** taxable business with no paid employees under NES rules.
- **Professional licensee:** person or entity holding a regulated credential.
- **Association member:** member of an organization.
- **Business license:** a license record, not necessarily a unique firm.

### 3. Receipts are not profit

Census nonemployer receipts are gross receipts. A contractor with $500,000 receipts can have very different owner economics from a consultant with $500,000 receipts.

### 4. Industry categories hide enormous variation

2-digit NAICS is a discovery tool, not a sales segment. Move to 3/6-digit NAICS before target-list construction.

### 5. National distributions are not Chicago observations

The Chicago nonemployer receipt-band estimates in this research are **scenarios based on national distribution**, explicitly because equivalent metro receipt-size-class detail is not currently published in the same table.

### 6. Security need is not purchase intent

A firm can have objectively poor controls and never buy. Buying triggers, budget, trust, and sales access determine actual opportunity.

### 7. Competitor pricing is not neutral market research

MSPs publish prices to sell services. Use multiple providers and actual prospect invoices/proposals to validate real spend.

### 8. Association counts overstate reachable firms if treated as accounts

Members can be students, retired professionals, employees of large firms, duplicate members, or people outside the exact target geography.

## Research quality rules going forward

1. Prefer official federal/state/local sources for market counts and regulations.
2. Preserve source year next to each important statistic.
3. Keep common-year comparisons separate from “latest available” mixed-year comparisons.
4. Label derived arithmetic.
5. Label scenarios visibly.
6. Never convert an association-member count directly to firm TAM.
7. Never infer technology spend solely from payroll/revenue.
8. Validate competitor pricing with actual buyers/proposals.
9. Replace broad NAICS assumptions with 3/6-digit data as the market dataset develops.
10. Replace modeled qualification rates with observed lead/interview/pilot evidence as soon as available.

## Research backlog

### Priority 1 — exact Chicago 3-digit market extraction

Extract the revised 2022 SUSB Chicago MSA 3-digit NAICS table and build a target-sector table with:

- firms;
- establishments;
- employment;
- payroll;
- receipts;
- enterprise employment size.

### Priority 2 — nonemployer target NAICS

Extract Chicago metro NES counts/receipts for precise professional, healthcare, construction, real-estate and finance categories available in the dataset.

### Priority 3 — identifiable account list

Join:

- City licenses;
- state entity data;
- IDFPR/bulk license data;
- NPPES;
- public professional directories;
- websites/enrichment.

### Priority 4 — observed spend

Collect 30–40 structured interviews and actual anonymized spend/provider data.

### Priority 5 — offer economics

Run paid pilots and replace assumptions with:

- actual CAC;
- close rate;
- project hours;
- gross margin;
- recurring attach;
- churn/support load.

## Current research confidence

| Conclusion | Confidence |
|---|---|
| Chicago contains an enormous small-business population | Very high |
| Nonemployers dominate business count | Very high |
| Nonemployer economic distribution is highly skewed | Very high nationally; metro distribution needs more work |
| Professional/healthcare/construction/real-estate sectors are large | High |
| Accounting/tax has strong explicit security pressure | Very high |
| Small law firms retain high buyer control over technology | High |
| Healthcare has meaningful security/regulatory pressure | Very high |
| Generic MSP competition in Chicago is crowded | High |
| 2–9-user professional practices are a sweet spot | Medium; needs customer evidence |
| Microbusiness security baseline can be profitable | Low/medium hypothesis; requires pilot economics |
| Incumbent-MSP coexistence is a strong wedge | Medium; requires sales testing |
| A particular vertical should become permanent focus | Low; do not decide yet |
