# Go-to-Market, Channel, and Data Plan

## Source and status

- **Status:** research-backed execution plan; proposed, not approved
- **Date:** 2026-08-19
- **Purpose:** convert the market research into a reproducible prospecting and validation system rather than a one-time market report.

## Core GTM principle

Do not buy a generic “Chicago SMB” list and spray broad managed-IT messaging.

Build a market model that can answer:

1. **Which exact business archetype is this?**
2. **Why is its technology/security exposure economically meaningful?**
3. **What trigger could make it buy now?**
4. **Who can introduce or influence the owner?**
5. **Which offer fits its size and complexity?**

## Market-data architecture

### Layer 1 — denominator data

Use public economic datasets to understand how many organizations exist and their economic structure.

#### Census SUSB

Use for:

- firm count;
- establishment count;
- employment;
- payroll;
- receipts;
- enterprise employment size;
- 3-digit NAICS at MSA level.

Current relevant release: 2022 SUSB MSA 3-digit NAICS.

Source: https://www.census.gov/data/tables/2022/econ/susb/2022-susb-annual.html

#### Census CBP

Use for newer employer-establishment counts, employment, payroll, detailed industry and establishment-size classes. The 2023 CBP API supports metropolitan statistical areas and employment-size classes, though current API use requires a Census API key.

Sources:

- https://www.census.gov/programs-surveys/cbp/data.html
- https://api.census.gov/data/2023/cbp/variables.html

#### Census Nonemployer Statistics

Use for zero-payroll establishment counts and receipts.

Source: https://www.census.gov/programs-surveys/nonemployer-statistics/data/datasets.html

### Layer 2 — identifiable-account sources

Census provides denominators, not generally a usable sales-account directory. Build account identities from public/licensed/business sources.

#### City of Chicago business-license data

The city's **Current Active Business Licenses** dataset was updated in August 2026 and contains roughly **54,000 license records** across 37 fields, including legal/DBA name, address, ZIP, license details, account number, and geography-related fields.

Source: https://data.cityofchicago.org/Community-Economic-Development/Business-Licenses-Current-Active/uupf-x98q

Important limitation: not every target professional business requires the same Chicago business license, and suburban businesses are outside the dataset. This is a lead source, not a market denominator.

The broader historical Business Licenses dataset is updated daily and can be joined to the Business Owners dataset through account/legal-name fields.

Source: https://data.cityofchicago.org/Community-Economic-Development/Business-Licenses/r5kz-chrr

#### Illinois Secretary of State business-entity search

Use to confirm legal entities, entity status, and selected officers/managers/agents where available.

Source: https://apps.ilsos.gov/businessentitysearch/

This is best used for validation/enrichment, not necessarily bulk prospect-list generation.

#### IDFPR professional-license data

Illinois Department of Financial & Professional Regulation maintains license lookup for professional regulation, real estate, banking/financial institutions, and bulk lookup options. It says single-license lookup is updated daily and bulk lookup generally weekly unless otherwise noted.

Source: https://idfpr.illinois.gov/checklicense.html

The professional-regulation universe includes CPAs/accounting firms, physicians and many other health professionals, architects, professional engineers/design firms, real estate firms/professionals, financial entities, and other regulated categories relevant to this study.

IDFPR's active-license reports are updated monthly and can provide an additional denominator/reference layer.

Source: https://idfpr.illinois.gov/dpr/active-license-report.html

#### CMS NPPES/NPI files

For healthcare, CMS publishes monthly and weekly downloadable NPPES data. As of 2026, Version 2 files include expanded name fields plus other-name, practice-location, and endpoint reference files.

Source: https://download.cms.gov/nppes/NPI_Files.html

NPI issuance does **not** verify professional licensure, so NPPES should be joined with state licensure and business information rather than treated as certification.

#### Professional associations and directories

Potential sources/channels include:

- Illinois CPA Society;
- Illinois State Bar Association;
- Chicago Bar Association;
- Chicago Medical Society;
- Chicagoland AGC and trade groups;
- Chicago Association of REALTORS / Illinois REALTORS;
- AIA Chicago / Small Firm Exchange;
- nonprofit and association networks.

Association membership counts are **not firm counts**, but member directories, events, sponsorship, and education can create much higher-trust acquisition paths than cold lists.

### Layer 3 — commercial enrichment

After public-source account identification, selectively enrich with tools such as:

- company website;
- LinkedIn / Sales Navigator or equivalent;
- employee count;
- key decision-maker;
- Microsoft/cloud signals where legally/ethically obtainable;
- office locations;
- service lines;
- recent growth/news/jobs;
- technology leadership roles;
- current providers where disclosed.

Do not collect or commit sensitive personal information unnecessarily. Respect applicable outreach/privacy rules and platform terms.

## Proposed master account table

Create a structured prospect dataset with fields such as:

### Identity

- account_id;
- legal name;
- DBA;
- website/domain;
- address;
- city/ZIP/county;
- entity/legal form if known;
- source record IDs;
- source freshness date.

### Classification

- NAICS 2/3/6 digit;
- vertical archetype;
- professional license type;
- association where publicly known;
- employer/nonemployer hypothesis;
- estimated employee/user band.

### Economic indicators

- receipts/revenue band if lawfully sourced;
- project/transaction scale proxies;
- office count;
- years in business;
- professional headcount;
- growth signal.

### Technology/risk indicators

- Microsoft 365 likely/known;
- current IT leader;
- current MSP/provider if known;
- regulated data;
- payment/wire exposure;
- cyber-insurance known;
- external customer-security pressure;
- contractors/external collaborators;
- remote/distributed operations;
- major business systems.

### Commercial

- ICP score;
- current trigger;
- likely buyer;
- warm path/referrer;
- proposed entry offer;
- outreach date/status;
- meeting outcome;
- current annual tech/provider spend if disclosed;
- willingness-to-pay data;
- win/loss;
- first-year revenue;
- gross margin;
- recurring attach.

## NAICS research plan

The 2-digit sector view is too broad. Build the next research dataset at **3-digit and then 6-digit NAICS** around likely archetypes.

Priority families to resolve:

### Professional services

- legal services;
- accounting/tax/bookkeeping/payroll;
- architectural services;
- engineering services;
- management/technical consulting;
- design/advertising/specialist professional services.

### Healthcare

- physician offices;
- dental offices;
- mental-health practices;
- outpatient services;
- therapy and other relevant independent-practice categories.

### Construction/field

- general contractors;
- specialty trades;
- building equipment contractors;
- other commercial/project-oriented subsegments.

### Real estate

- brokerages;
- property management;
- appraisal;
- title/closing-adjacent categories where appropriate;
- commercial vs residential where data allow.

### Finance/insurance

Break down by actual regulated activity; never use the broad category as one compliance market.

## Initial interview design

The current repository calls for at least ten buyer interviews. This research supports increasing the structured sample to **30–40 interviews** so size-band effects can be observed.

### Recommended 32-interview matrix

Four primary vertical tracks × eight interviews each:

- accounting/tax;
- legal;
- healthcare;
- construction/field/property.

Within each track:

- 2 owner-operated / 1–4 user businesses;
- 2 businesses around 5–9 users;
- 2 around 10–49 users;
- 2 around 50+ users where available.

If a particular vertical lacks viable microbusiness economics, that is a useful result rather than a sampling failure.

## Standard interview questions

### Business context

1. What does the business do and how many people—including contractors—need system access?
2. Approximate revenue/receipt band?
3. Which systems would stop the business if unavailable?
4. Which types of client/customer data are sensitive?

### Current technology operating model

5. Who owns technology decisions?
6. Who administers Microsoft/email, endpoints, applications, backups, and vendors?
7. Is there an MSP or internal IT person? What do they actually do?
8. Approximate annual technology/provider spend?
9. What is frustrating or still unmanaged despite that spend?

### Security/pressure

10. Cyber insurance?
11. Client/security questionnaires?
12. Industry/regulatory requirements?
13. Any phishing, payment-fraud, ransomware, data-loss, former-user-access, or restore incident?
14. When were backups/restore last tested?
15. Can they produce an inventory of users, devices, admins, applications, and owners?

### Buying behavior

16. What would cause them to fund a technology/security project this quarter?
17. How would they evaluate an outside advisor?
18. Would they buy an independent assessment without changing MSPs?
19. Would a fixed-price remediation/Foundation be easier to buy than open-ended consulting?
20. What price ranges feel trivial, plausible, material, or impossible?

### Microbusiness-specific

21. Would they pay for a professional baseline with no unlimited help desk?
22. Would annual/semiannual security review be more attractive than monthly service?
23. Would they buy through/rely on a recommendation from their CPA, lawyer, insurer, professional association, or software vendor?

## Channel strategy

### Channel 1 — warm professional network

Still the fastest first evidence source.

Use warm introductions to obtain **unusually candid current-spend and current-provider data**, not merely easy sales leads.

### Channel 2 — accounting/legal cross-referral network

These professionals advise the same small-business owners the company wants to reach.

Potential two-way model:

- company refers formal legal/tax/compliance work out;
- advisor refers technology remediation in;
- each party retains professional independence;
- no implication of audit/attestation independence where prohibited;
- referral economics, if any, receive legal/ethical review.

### Channel 3 — insurance brokers

Cyber/commercial insurance can create a recurring trigger around renewal and security questionnaires.

Test whether brokers value a technology partner who can remediate—not sell insurance—and produce customer-owned evidence.

### Channel 4 — professional associations

Rather than begin with expensive sponsorship, test educational value:

- practical WISP technology workshop for tax firms;
- “What your law firm's M365 configuration actually proves” session;
- BEC/wire-fraud controls for real estate/construction;
- HIPAA technology evidence for small practices;
- secure external collaboration for architects/contractors.

Education must remain accurate and avoid pretending the company provides legal/compliance certification.

### Channel 5 — Microsoft/distributor ecosystem

Potential lead sources:

- customers needing security/tenant remediation;
- customers below larger partner delivery thresholds;
- license customers lacking governance;
- migration/modern-work referrals.

Avoid building the entire GTM around vendor referrals until the economics and program eligibility are confirmed.

### Channel 6 — incumbent MSP coexistence

A non-obvious channel is MSPs that do not want to deliver:

- fractional technology strategy;
- M365 architecture modernization;
- complex security remediation;
- workflow/integration projects;
- regulated-readiness documentation.

This turns nominal competitors into specialists/referral partners where boundaries are clear.

## Direct-outreach strategy

Use account-specific trigger hypotheses rather than generic IT messaging.

Examples:

- accounting/tax: WISP/Safeguards evidence;
- law: client confidentiality + BEC + unsupported M365 governance;
- healthcare: risk-analysis remediation + Microsoft/device evidence;
- construction: subcontractor access + field-device/payment workflow;
- real estate: email/domain/wire-transfer security;
- growing consultancy: owner-administered M365 + onboarding/offboarding + workflow automation.

## Acquisition experiment design

For each channel, run a small controlled test.

Example:

- 50 tightly qualified accounts;
- one vertical;
- one trigger message;
- one entry offer;
- same qualification standard;
- track delivered, replies, meetings, assessments, projects, recurring conversion.

Do not change message, segment, price, and offer simultaneously or the results become uninterpretable.

## Required metrics

### Funnel

- targeted accounts;
- valid contacts;
- outreach delivered;
- response;
- qualified meeting;
- paid assessment;
- implementation;
- recurring service.

### Economics

- cash acquisition spend;
- founder/sales hours;
- CAC per qualified meeting;
- CAC per customer;
- first-year revenue;
- gross profit;
- payback;
- recurring gross margin.

### Product evidence

- actual assessment hours;
- remediation hours;
- findings by category;
- scope variance;
- implementation conversion;
- recurring attach;
- support tickets/escalations after delivery;
- customer outcome;
- referral/case-study permission.

### Segment evidence

- employee/user band;
- receipt/revenue band;
- industry;
- trigger;
- incumbent provider;
- current spend;
- buyer role;
- channel.

## Market-model feedback loop

Every customer/prospect should improve the market model:

> public-market data → account score → interview → proposal → delivery evidence → revised score/offer → better target list

The database should eventually answer questions such as:

- Which vertical closes fastest?
- Does 2–9 users outperform 10–49 on gross profit per sales hour?
- What receipt threshold makes the microbusiness product viable?
- Which triggers predict paid assessments?
- Which incumbent-provider conditions predict coexistence vs replacement?
- Which association/referral source produces the lowest CAC?
- Which vertical creates the most recurring expansion?

## 90-day research-to-market sequence

### Weeks 1–2 — quantitative base

- extract SUSB Chicago MSA 3-digit data;
- map target NAICS;
- build initial public-source account table;
- score 100–200 accounts;
- identify warm paths.

### Weeks 2–6 — interviews

- run 30–40 structured interviews;
- capture current spend/provider/trigger data;
- rank size bands and verticals;
- identify 5–10 paid-pilot candidates.

### Weeks 4–8 — offer tests

- paid Baseline Assessment;
- test incumbent-MSP coexistence;
- test one microbusiness fixed-scope baseline;
- record all delivery time and customer objections.

### Weeks 8–12 — decision

Compare:

- close rate;
- first-year revenue;
- gross margin;
- sales effort;
- recurring attach;
- support burden;
- referral density;
- technical repeatability.

Then decide whether to:

- select a preferred vertical;
- preserve multi-vertical professional-services positioning;
- launch a microbusiness product;
- defer microbusiness;
- deepen a channel partnership; or
- revise pricing/service scope.

## Governance

All market research should distinguish:

- observed external data;
- self-reported prospect data;
- company delivery evidence;
- modeled assumptions.

Do not silently promote a modeled conversion rate, receipt threshold, or vertical preference into an approved business fact.
