# Chicago Small-Business Market Size

## Source and status

- **Status:** measured market baseline plus explicitly labeled derived values
- **Date:** 2026-08-19
- **Preferred comparison year:** 2022 for employer/nonemployer common-year comparison
- **Primary geography:** Chicago-Naperville-Elgin metropolitan area

## Why the common-year baseline matters

Employer and nonemployer business datasets are published on different schedules. Combining a 2023 nonemployer count with a 2022 employer count can be useful for a current directional estimate, but it creates false precision if presented as one observed total.

For structural comparisons, this research therefore uses the SBA Office of Advocacy's 2025 metro profile, which places employer and nonemployer counts on a common 2022 basis using Census data.

Primary source: U.S. Small Business Administration, Office of Advocacy, *2025 Small Business Profiles for Major Metropolitan Areas*: https://advocacy.sba.gov/2025/10/28/2025-small-business-profiles-for-major-metropolitan-areas/

Underlying federal datasets include Census Statistics of U.S. Businesses (SUSB) and Nonemployer Statistics (NES).

## Common-year Chicago small-business universe

| Size category | Businesses | Share of small-business count |
|---|---:|---:|
| Nonemployer establishments | 898,077 | 81.7% |
| Employer firms, 1–19 employees | 177,996 | 16.2% |
| Employer firms, 20–499 employees | 22,617 | 2.1% |
| **Total small businesses** | **1,098,690** | **100%** |

### Important interpretation

The market is **numerically dominated by zero-payroll businesses**. This does not mean 82% of economic output comes from nonemployers. It means business-count statistics and economic-value statistics answer different questions.

The employer market is far smaller in count but carries much more employment, payroll, organizational complexity, and average revenue per firm.

The nonemployer market is enormous in count and highly skewed economically. It includes both low-receipt activity and a much smaller but still potentially substantial population of serious owner-operated businesses.

## Employer-small-business economic scale

The same SBA profile reports approximately **1.9 million small-business employees** in the Chicago metro, representing roughly **44.6% of employees** in the region's private-sector business base.

A secondary 2023/2022 synthesis using Census/SBA data reports approximately:

- 200,613 small employer firms;
- 1,863,195 small-business employees; and
- $121.6 billion in annual payroll.

Source for the secondary synthesis: Postal, *U.S. Areas With the Most Small Businesses*, based on Census/SBA data: https://www.usepostal.com/blog/us-areas-with-most-small-businesses

Treat the secondary figures as a current directional cross-check, not as the canonical federal table.

### What payroll tells us

Payroll is useful because it demonstrates that the small-employer economy is not a niche. Tens of billions of dollars of annual labor expense sit inside the addressable regional economy before considering software, rent, insurance, professional services, capital expenditures, or other operating costs.

It does **not** tell us what percentage will be spent on technology services.

## Capital-flow signal

The SBA Chicago profile reports, for 2023 lending activity, approximately:

- **$2.7 billion** in Community Reinvestment Act-reported loans to metro businesses with revenues below $1 million;
- **$8.5 billion** in new business lending through loans of $1 million or less; and
- **$3.1 billion** through loans of $100,000 or less.

These figures are not technology budgets. They are useful evidence that a large micro/small-business financing economy exists alongside the business counts.

## Industry structure

The SBA Chicago profile shows that the nonemployer and employer populations are not distributed uniformly.

| Industry | Nonemployer businesses | Small employers | Approx. total small businesses | Initial relevance |
|---|---:|---:|---:|---|
| Transportation & warehousing | 174,522 | 16,119 | 190,641 | Mixed; needs hard filtering |
| Professional, scientific & technical services | 117,711 | 30,560 | 148,271 | Very high |
| Other services | 89,922 | 21,346 | 111,268 | Mixed |
| Real estate, rental & leasing | 86,117 | 9,084 | 95,201 | High but economically uneven |
| Construction | 72,743 | 22,426 | 95,169 | Very high |
| Health care & social assistance | 69,795 | 21,208 | 91,003 | Very high |
| Retail trade | 61,507 | 15,705 | 77,212 | Selective |
| Arts, entertainment & recreation | 48,701 | 3,576 | 52,277 | Selective |
| Educational services | 28,386 | 3,429 | 31,815 | Selective |
| Finance & insurance | 22,690 | 8,371 | 31,061 | High, specialized |
| Accommodation & food services | 17,445 | 16,500 | 33,945 | Lower initial fit |
| Wholesale trade | 12,660 | 10,295 | 22,955 | Selective |
| Information | 10,786 | 2,460 | 13,246 | High technical fit, competitive |
| Manufacturing | 8,950 | 8,057 | 17,007 | Selective/high complexity |

### Interpretation

The business model does not require dominating the whole small-business market. Several relevant sectors each contain **tens of thousands to more than one hundred thousand** small organizations.

The professional/scientific/technical, healthcare, construction, real-estate, finance/insurance, and information categories alone provide a large substrate for further qualification.

However, a 2-digit NAICS category is far too broad for lead generation. The next data stage should resolve these sectors into 3- and 6-digit NAICS codes and then map them to target archetypes.

## Sector economic signals from the SBA profile

Small employer firms in several likely target sectors already support substantial payroll:

| Sector | Small-business employees | Annual payroll |
|---|---:|---:|
| Health care & social assistance | ~255,608 | ~$13.36B |
| Professional, scientific & technical services | ~197,972 | ~$19.88B |
| Manufacturing | ~178,624 | ~$11.91B |
| Other services | ~149,986 | ~$7.03B |
| Accommodation & food services | ~234,937 | ~$6.58B |

Payroll is not addressable technology spend, but these values help distinguish economically substantial sectors from count-heavy low-receipt populations.

## A better market hierarchy than “SMB”

For this company, the region should be modeled as at least four economic/operating layers:

### Layer 1 — nonemployer / owner-operated

- approximately 898,000 on the 2022 common-year baseline;
- very heterogeneous receipts;
- almost no internal IT by definition of headcount, though contractors may be present;
- productized offering required for most viable prospects.

### Layer 2 — micro-employer, 1–9 employees

Census CBP/SUSB support finer employment-size bands than the SBA profile's 1–19 summary. This group should be extracted in the next data pipeline because it likely contains many of the company's best small professional-practice opportunities.

Hypothesis: the 2–9 professional-practice market may be a particularly attractive intersection of high owner access, meaningful business risk, enough budget, and low internal IT maturity.

### Layer 3 — small employer, roughly 10–49

Likely strongest initial fit for the current assessment/Foundation model:

- enough users and applications for architecture/governance complexity;
- usually still accessible to owners/partners;
- often no full senior technology/security function;
- enough economic scale to support fixed-fee remediation and recurring governance.

### Layer 4 — 50–150/200-user organizations

Higher project and recurring value, but:

- more likely to have existing IT staff/MSPs;
- procurement and change complexity increase;
- incumbent displacement is harder;
- strongest wedge may be targeted assessment, remediation, security architecture, governance, or automation rather than full managed-service replacement.

## Geography: Chicago city vs metro

The metro should remain the primary sizing unit because:

- the actual commercial network extends through Cook and surrounding counties;
- professional practices, contractors, healthcare offices, manufacturers, and technology firms are heavily suburban as well as urban;
- the user's planned Illinois-first operating model is not confined to Chicago city limits.

For outreach execution, the market can later be divided into:

- Chicago city;
- inner Cook suburbs;
- DuPage;
- Lake;
- Will;
- Kane/McHenry;
- Northwest Indiana only if foreign-state/regulatory and delivery economics justify it; and
- Michigan separately under the legal nexus framework.

## Current-data update

Census's 2023 Nonemployer Statistics are newer than the common-year SBA profile. A secondary synthesis reports approximately **916,466 Chicago metro nonemployer establishments** for 2023, up from 898,077 on the 2022 baseline.

Use this as evidence that the large nonemployer universe persists, but do not combine it with older employer data and label the result a single-year official total.

## Data infrastructure available for deeper sizing

### Census County Business Patterns — current employer detail

Census 2023 County Business Patterns provides:

- establishments;
- employment;
- first-quarter payroll;
- annual payroll;
- geography;
- NAICS industry; and
- employment-size class.

The CBP API supports metropolitan/micropolitan geography and detailed NAICS. This is the preferred source for a reproducible Chicago employer-account model.

Source: https://www.census.gov/programs-surveys/cbp/data.html

### Census SUSB — firm-level economic detail

The latest SUSB release currently available is 2022. Metro tables can provide firm/establishment counts, employment, payroll, and receipts with industry detail.

Source: https://www.census.gov/programs-surveys/susb/data/tables.html

### Census Nonemployer Statistics — zero-payroll detail

NES provides establishment counts and receipts for businesses without paid employees. Metro files are available, but not every table dimension—especially receipt-size class—is available at metro geography.

Source: https://www.census.gov/programs-surveys/nonemployer-statistics/data/datasets.html

## Required next dataset

Build a machine-readable Chicago opportunity table with fields such as:

- NAICS 2/3/6 digit;
- industry label;
- nonemployer establishment count;
- nonemployer receipts where available;
- employer firms/establishments by `<5`, `5–9`, `10–19`, `20–49`, `50–99`, `100–249` bands where available;
- employment;
- payroll;
- receipts;
- average receipts per establishment where meaningful;
- regulatory/security intensity score;
- Microsoft/cloud fit score;
- workflow/automation potential;
- estimated owner access;
- existing-provider likelihood;
- proposed offer;
- proposed channel.

This table should become the basis for target-list design and should replace broad anecdotes when the data are available.
