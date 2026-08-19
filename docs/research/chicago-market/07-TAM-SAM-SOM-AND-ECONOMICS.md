# TAM, SAM, SOM, and Market Economics

## Source and status

- **Status:** measured market inputs plus transparent planning scenarios
- **Date:** 2026-08-19
- **Decision status:** not an approved forecast, budget, or valuation
- **Core rule:** account counts are measured where possible; dollar opportunity is modeled only when assumptions are explicit.

## Why conventional TAM math would be misleading here

A statement such as:

> “Chicago has 1.1 million small businesses and each could spend $10,000, therefore the TAM is $11 billion”

would be analytically useless.

It ignores:

- most nonemployers have low receipts;
- many businesses are poor technical/industry fits;
- many already have providers;
- not every qualified account is buying in a given year;
- service scope and spend vary drastically by size;
- the company's actual early constraint will be sales/delivery capacity, not market count.

This file therefore uses a hierarchy:

1. **Broad opportunity substrate** — measured business populations in plausibly relevant sectors.
2. **Qualified SAM scenario** — an explicit fraction that might actually meet the company's ICP.
3. **Annual active-buying scenario** — a fraction of qualified accounts assumed to be in market in a given year.
4. **SOM / operating capacity** — how many accounts the company could realistically sell and deliver.

## 1. Broad Chicago opportunity substrate

Using the SBA Chicago 2022 common-year profile, six broad 2-digit sectors that appear especially relevant are:

- professional, scientific and technical services;
- healthcare and social assistance;
- construction;
- real estate, rental and leasing;
- finance and insurance; and
- information.

Measured counts sum to approximately:

| Population | Count |
|---|---:|
| Nonemployer establishments | **379,842** |
| Small employer firms | **94,109** |
| Combined broad-sector small-business population | **473,951** |

These are **not** TAM accounts. They are a broad opportunity substrate from which the true market must be filtered.

The six 2-digit sectors contain many irrelevant businesses, and they exclude potentially attractive businesses in other sectors.

## 2. Core employer-market SAM scenarios

### Starting point

Broad relevant-sector small employers: **94,109**.

The company is unlikely to fit all of them. Qualification should include:

- business/user size;
- M365/cloud fit;
- senior-IT gap;
- risk/operational complexity;
- economic capacity;
- geography;
- trigger condition;
- willingness to use an outside advisory/implementation partner.

### Scenario table

| Scenario | Share of broad employer substrate qualifying | Qualified accounts |
|---|---:|---:|
| Narrow | 10% | ~9,400 |
| Base | 20% | ~18,800 |
| Broad | 30% | ~28,200 |

These percentages are **planning assumptions**, not observed qualification rates.

The purpose is to show that even an aggressive filtering process still leaves a large enough market for a founder-led firm.

## 3. Annual active-buying scenarios

A serviceable account does not necessarily buy this year.

A useful planning equation is:

> qualified accounts × annual buying incidence × first-year revenue per won account

### Example employer scenarios

| Scenario | Qualified accounts | Assumed annual active-buying incidence | Assumed first-year revenue | Modeled annual spend in active market |
|---|---:|---:|---:|---:|
| Conservative | 10,000 | 5% | $15,000 | $7.5M |
| Base | 20,000 | 7.5% | $18,000 | **$27.0M** |
| High | 30,000 | 10% | $22,000 | $66.0M |

Every value in this table after the qualified-account pool is a **scenario assumption**.

This should not be labeled “Chicago IT TAM.” It is a way to test whether plausible market participation still produces a sufficiently large opportunity.

### Why $15k–$22k first-year revenue is plausible as a planning input

The repository already carries working hypotheses of:

- Foundation Core: ~$6k–$9k;
- Foundation Full: ~$12k–$18k;
- Complex: $18k+;
- recurring governance: ~$500–$2,000+/month;
- broader advisory retainers: ~$2k–$10k/month depending on scope.

A first-year relationship can therefore combine assessment/project/remediation and recurring governance.

This is **not evidence that customers will accept these prices**. Paid pilots and competitive proposals must validate them.

## 4. Microbusiness/nonemployer SAM scenarios

### Starting point

Broad relevant-sector nonemployer substrate: **379,842**.

This needs far more aggressive qualification because national NES data show roughly three quarters of nonemployers have receipts below $50,000.

Potential filters:

- receipts at least ~$100k/$250k depending on risk and offer price;
- professional/regulated activity;
- sensitive data;
- meaningful payment/wire exposure;
- business-critical cloud dependence;
- several identities/devices/contractors despite zero payroll;
- external security requirement;
- owner willing to buy professional services.

### Qualified-account scenarios

| Scenario | Share of broad nonemployer substrate qualifying | Qualified accounts |
|---|---:|---:|
| Narrow | 5% | ~19,000 |
| Base | 10% | ~38,000 |
| Broad | 15% | ~57,000 |

Again, these are **not measured Chicago qualification rates**.

They demonstrate that the microbusiness opportunity does not need a high qualification percentage to become materially large.

## 5. Productized microbusiness annual-spend scenario

A microbusiness product would need very different economics from the full Foundation.

Illustrative base scenario:

- 38,000 qualified accounts;
- 8% in market in a given year;
- $4,000 average first-year product/review revenue.

Modeled annual active-market spend:

> **$12.16 million**

This is a scenario only. The correct price, active-buying rate, qualified-account rate, acquisition cost, delivery hours, support burden, and retention are all unknown.

The strategic value of the calculation is simply this:

> The microbusiness hypothesis can fail very aggressive filters and still remain worth testing because the underlying population is enormous.

## 6. Why employee-market and microbusiness economics must remain separate

| Variable | Core employer service | Productized microbusiness service |
|---|---|---|
| Sales motion | Consultative / founder-led | Referral/channel + standardized qualification |
| Discovery | Custom enough to understand environment | Highly scripted/pre-flight |
| Implementation | Moderate customization | Narrow supported architecture |
| Price | ~$6k–$18k+ project hypotheses | Likely materially lower |
| Recurring | Governance/advisory, potentially MSP-like services | Light annual/semiannual governance or limited subscription |
| Support | Selective or separate schedule | Must avoid unlimited help desk unless economics prove it |
| Buyer | Owner/COO/CFO/IT lead | Owner/professional principal |
| Margin driver | Senior judgment + repeatable delivery | Automation + strict scope + channel CAC |
| Main risk | project complexity / scope creep | low ticket + high acquisition/support cost |

Combining these into one forecast would hide the fundamental difference in unit economics.

## 7. Capacity-limited SOM

For an early founder-led service company, **SOM should be built from capacity**, not from “1% of TAM.”

### Example new-logo project revenue

At an illustrative average of $15,000 first-year project/service revenue:

| Won accounts/year | New-logo revenue |
|---|---:|
| 20 | $300,000 |
| 50 | $750,000 |
| 100 | $1,500,000 |

These values exclude recurring carryover and are not a forecast.

### Example recurring revenue

At an illustrative average recurring relationship of $1,500/month:

| Recurring clients | Monthly recurring revenue | Annualized recurring revenue |
|---|---:|---:|
| 20 | $30,000 | $360,000 |
| 50 | $75,000 | $900,000 |
| 100 | $150,000 | $1.8M |

The company's actual delivery/support capacity may make 100 recurring clients impossible without additional staffing and standardization. That is exactly why a capacity model is required before calling any of these outcomes realistic.

## 8. Delivery-capacity model

For each offer define:

- founder strategy/review hours;
- sales/pre-sales hours;
- project-management hours;
- execution hours;
- subcontractor hours/cost;
- QA/documentation hours;
- warranty/rework hours;
- recurring hours per account/month;
- help-desk/escalation hours if included;
- administrative overhead;
- travel/on-site hours.

The existing greenfield Foundation estimate is approximately **46 execution hours** before broader sales/admin overhead.

Illustrative theoretical delivery only:

- 20 Foundations × 46 hours = 920 execution hours;
- 50 × 46 = 2,300 hours;
- 100 × 46 = 4,600 hours.

That immediately shows why standardization, contributor capacity, and service mix matter more than raw market size.

## 9. Revenue opportunity by service layer

The market should be modeled as multiple revenue layers rather than one spend bucket.

### Layer A — assessment

Variables:

- target accounts;
- assessment price;
- paid-assessment close rate;
- hours;
- gross margin.

### Layer B — implementation/remediation

Variables:

- percentage of assessments converting;
- average project value;
- direct delivery cost;
- scope variance.

### Layer C — recurring governance

Variables:

- implementation-to-recurring attach;
- monthly price;
- average monthly service hours;
- retention/churn;
- tooling/license costs.

### Layer D — automation/integration expansion

Variables:

- accounts with workflow opportunities;
- project frequency;
- average project value;
- reusable solution patterns.

### Layer E — licensing/partner margin

Supplemental only under current strategy.

## 10. Per-account lifetime-value framework

Do not estimate LTV from arbitrary SaaS multiples.

For service clients:

> LTV contribution = initial gross profit + recurring gross profit over retained months + expansion gross profit − expected support/warranty losses − acquisition cost

Track it by vertical and size band.

Possible early finding:

- accounting firms may have strong recurring security demand but seasonal support peaks;
- construction may generate more automation/integration expansion;
- law may pay more for professional service but have competitive MSP incumbents;
- microbusiness may have lower revenue but very efficient acquisition if association/broker channels work.

Only delivery evidence can resolve these tradeoffs.

## 11. Customer acquisition cost framework

Separate channels:

- warm network;
- founder outbound;
- LinkedIn/commercial prospecting;
- association sponsorship;
- educational events/webinars;
- insurance/referral partners;
- CPA/law/consulting partners;
- Microsoft/distributor ecosystem;
- paid search/content;
- direct mail where tested.

For each channel measure:

> cash spend + founder/sales labor → qualified meetings → paid assessments → projects → recurring clients

A 900,000-account market is economically irrelevant if it costs more to find and educate a customer than the product generates in gross profit.

## 12. Market-share reality

Because the addressable Chicago business population is so large, the company does **not** need material metro market share to build a substantial founder-led services company.

For example, 100 recurring accounts would be approximately:

- 0.11% of the 94,109 broad relevant-sector small-employer population; or
- far less than 0.1% of the overall Chicago small-business universe.

The practical problem is therefore:

> acquire and serve a tiny, high-quality subset extremely well.

This is strategically better than designing for generic scale before product-market fit.

## 13. What data would turn this from scenario planning into a real market model

Priority measurements:

1. exact Chicago MSA employer counts by 3-digit NAICS and enterprise employment band from SUSB;
2. employer payroll and receipts by target 3-digit NAICS;
3. nonemployer counts and receipts by target NAICS;
4. firm-level lead sources tied to those categories;
5. actual annual technology spend from interviews;
6. incumbent MSP/provider spend;
7. assessment willingness to pay;
8. implementation conversion rate;
9. recurring attach/retention;
10. delivery hours and gross margin;
11. sales-cycle length;
12. acquisition cost by channel.

Census confirms that the revised 2022 SUSB MSA-by-3-digit-NAICS tables include firm/establishment counts, employment, annual payroll, and receipts. That dataset should be incorporated into the next quantitative extraction.

Source: https://www.census.gov/data/tables/2022/econ/susb/2022-susb-annual.html

## Bottom line

The research supports three conclusions without requiring inflated TAM claims:

1. **Core employer market:** there are vastly more plausibly relevant Chicago accounts than an early-stage firm could serve.
2. **Microbusiness market:** even severe filtering of the enormous nonemployer pool leaves a potentially meaningful experimental market.
3. **SOM:** early success will be determined by acquisition efficiency, service repeatability, margin, and founder/delivery capacity—not by market share.
