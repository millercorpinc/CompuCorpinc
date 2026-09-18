# ADR-0005 — Entity, Jurisdiction, and Incentive Architecture

## Status

**Proposed — requires founder approval and qualified Illinois legal/tax validation before adoption.**

## Date

2026-08-19

## Context

The company is currently designed as a founder-led technology advisory, implementation, security, automation, and managed-governance business. The initial operating plan is Chicago/Chicagoland first, while some proposed participants are located in Michigan.

Existing founder/equity drafts use a planning model of 51% controlling-founder equity, a 20% sales pool, a 20% execution pool, and a 9% future reserve, with sales/execution ownership earned primarily through paid business outcomes.

Legal research identified that the intended economics, governance, worker status, tax treatment, and securities compliance should be separated rather than implemented through a single deal-based equity contract.

## Decision proposed

Subject to counsel/CPA validation:

1. Form the operating company as an **Illinois manager-managed LLC**.
2. Initially use **federal partnership tax treatment** unless the tax advisor recommends otherwise based on the final founder/incentive economics.
3. Encode control through the Operating Agreement, manager appointment/removal, voting rights, and reserved matters rather than relying on a 51% percentage alone.
4. Separate **true founder ownership** from **sales/execution incentive compensation**.
5. Use actual founder units with vesting/repurchase protection for true founders.
6. Evaluate an LLC **profits-interest/incentive-unit plan** against a **phantom-equity/unit-appreciation plan** for non-founder long-term contributors.
7. Prefer cash commission/profit-sharing for early sales and short-term contributors unless actual equity is deliberately approved and a securities exemption is documented.
8. Treat Michigan as a foreign-qualification/payroll/tax trigger based on actual business activity, not merely participant residence.
9. Defer Delaware unless the financing/investor strategy creates a concrete reason for Delaware law or a Delaware C corporation.

## Rationale

### Illinois

Illinois best matches the currently expected principal operating location and avoids a second formation-state layer with no identified financing benefit.

### Manager-managed structure

Illinois LLC default rules make an LLC member-managed unless the operating agreement establishes manager management. A member-managed structure is inconsistent with the intended founder-control model because members have equal management rights by default.

### Partnership tax treatment

Partnership taxation preserves flexibility for properly structured profits interests and differentiated economic arrangements. It also creates K-1, self-employment, allocation, and tax-distribution complexity, so it should be confirmed rather than assumed.

### Incentive separation

The current deal-based concept is better suited to a performance incentive plan than repeated issuances of ordinary membership interests. Actual equity grants create securities, tax, membership-right, valuation, and capitalization obligations.

### S-corporation timing

An S election may be reconsidered after the ownership/incentive design stabilizes. S corporations must generally preserve one class of economic stock rights, which can conflict with bespoke distribution/liquidation economics.

### Delaware

A Delaware LLC actually operating in Illinois would generally add Delaware maintenance and Illinois foreign qualification without an identified launch-stage benefit. Reconsider if institutional investors or a venture-style C-corporation financing model emerges.

## Alternatives considered

### Delaware LLC

**Benefit:** sophisticated entity law and contracting familiarity.  
**Cost:** second-state maintenance and Illinois qualification; no current investor requirement.  
**Disposition:** defer.

### Michigan LLC

**Benefit:** potentially appropriate if principal operations move to Michigan.  
**Cost:** likely Illinois foreign qualification if Chicago remains operating center.  
**Disposition:** defer under current Chicago-first assumptions.

### Illinois S corporation / LLC taxed as S corporation at formation

**Benefit:** can be tax-efficient for mature owner-operated service businesses in appropriate circumstances.  
**Cost:** one-class-of-stock economics, payroll/reasonable-compensation requirements, and reduced flexibility for current incentive design.  
**Disposition:** model later with CPA after incentive structure is settled.

### Delaware C corporation

**Benefit:** standard for institutional venture financing and stock-option programs.  
**Cost:** mismatched to current closely held services model; corporate tax and additional state administration.  
**Disposition:** revisit if capital strategy changes.

## Risks and required validation

Before approval, counsel/CPA must validate:

- exact founder roster and ownership;
- Illinois manager appointment/removal and reserved-matter structure;
- fiduciary-duty/conflict provisions;
- capital vs. profits-interest characterization;
- Section 83/83(b) treatment;
- securities exemptions and state notice filings;
- partner versus employee/contractor tax treatment;
- Illinois/Michigan multi-state tax and payroll;
- tax distributions;
- future S-election compatibility;
- future corporate conversion path.

## Consequences if approved

- `docs/launch/02-FOUNDER-EQUITY-AND-VESTING.md` must become a business/economic brief, not the executable legal agreement.
- `docs/launch/03-EXECUTION-EQUITY-TERMS.md` must not be signed in its current form.
- Counsel should draft the Operating Agreement, founder ownership documents, and selected incentive plan as one coordinated package.
- Every actual securities issuance must use a documented approval/exemption workflow.
- The launch backlog must add Michigan nexus, Chicago cloud/software tax, worker-classification, and equity-compliance tasks.

## Evidence

- `docs/legal/00-LEGAL-ARCHITECTURE-OVERVIEW.md`
- `docs/legal/01-ENTITY-JURISDICTION-AND-TAX.md`
- `docs/legal/02-FOUNDER-EQUITY-AND-INCENTIVE-DESIGN.md`
- `docs/legal/05-CURRENT-EQUITY-DRAFT-LEGAL-REVIEW.md`

## Approval

Not approved by this research pass. Founder approval and professional validation are required before changing the canonical entity/tax decision status to approved.
