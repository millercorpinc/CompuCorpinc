# Secure Microsoft 365 Foundation

## Status

Presumptive launch service. The service architecture and working effort model are established; final public pricing, margin thresholds, and contract language require approval.

## Purpose

Create a secure, governed, documented, and supportable Microsoft 365 operating baseline for a small or lower-midmarket organization.

The service is not a generic tenant setup. It establishes identity, privileged access, endpoint trust, security controls, collaboration governance, data authority, logging, documentation, and operational ownership.

## Product variants

### Foundation Core

Designed primarily for organizations with fewer than 10 users that need the essential control plane without the complete depth of the Full Foundation.

- Estimated execution: 26–32 hours
- Working price range: $6,000–$9,000
- Historical sizing guidance:
  - 1–3 users: approximately $6,000
  - 4–7 users: approximately $7,000–$8,000
  - 8–10 users: approximately $9,000

Foundation Core retains:

- Entra identity baseline
- MFA and Conditional Access
- Administrative separation and privileged controls
- Intune and device trust
- Defender and endpoint security
- Email protection
- Basic data authority and sharing governance
- Incident readiness
- Clean documentation snapshot and handoff

Foundation Core may defer or reduce:

- Deep Secure Score tuning
- Broad SaaS application review
- Advanced retention analysis
- Documentation depth beyond the launch standard
- Selected future-state and maturity controls

### Full Foundation

Designed for organizations generally at 10 or more users, or smaller organizations that require the full operating and security baseline.

- Base execution estimate: 46 hours for a controlled greenfield or cooperative takeover environment
- Working price range: $12,000–$18,000 before complexity adjustments
- Historical target for a suitable environment: Microsoft Secure Score approximately 75–80%, with exceptions documented and business risk prioritized over score optimization

## Ideal customer

An approximately 1–150-user organization using or adopting Microsoft 365 that lacks a consistent identity, endpoint, collaboration, security, data, and administrative baseline.

Strongest fit:

- 10–150 employees for the Full Foundation
- Fewer than 10 users for Foundation Core
- Microsoft 365 Business Premium or functionally equivalent licensing direction
- Authorized sponsor and willingness to adopt standard controls

## Trigger events

- New Microsoft 365 tenant
- Provider takeover
- Acquisition or organizational separation
- Cyber-insurance or customer-security requirements
- Rapid growth
- Device-management rollout
- Security incident or near miss
- Executive concern about uncontrolled access or sharing
- Compliance-readiness initiative
- Need to establish a supportable baseline before recurring service

## Outcomes

- Governed identities and administrator access
- MFA and Conditional Access baseline
- Managed and trusted endpoints
- Endpoint and email security
- Controlled collaboration and sharing
- Defined data authority and retention direction
- Logging and incident readiness
- Named administrative ownership
- Complete baseline documentation
- Prioritized remaining risks and exceptions
- Readiness for recurring Microsoft Security and Governance

## Full Foundation work model

The recovered base estimate is 46 hours:

| Area | Base hours | Expected output |
|---|---:|---|
| Tenant foundation | 2 | Tenant and licensing baseline; initial configuration and ownership |
| Administrative hygiene | 3 | Named admins, separate admin identities where appropriate, emergency access, role cleanup |
| Identity baseline | 2 | Entra settings, MFA, Conditional Access, authentication and lifecycle standards |
| Privileged controls / PIM | 2 | Least privilege, activation or equivalent controls, privileged operating procedure |
| Intune foundation | 4 | Enrollment, platform, ownership, application, and configuration foundation |
| Device compliance | 2 | Compliance policies and access relationship |
| Endpoint security | 2 | Defender and endpoint protection baseline |
| Security baselines | 2 | Standard endpoint and platform security configurations |
| Update rings | 1 | Patch and update deployment standard |
| Email / Defender for Office 365 | 2 | Anti-phishing, anti-malware, safe links/attachments, mail-flow review as licensed |
| Secure Score review and tuning | 5 | Prioritized posture improvement, evidence, and documented exceptions |
| Data architecture and authority | 2 | Teams, SharePoint, OneDrive, ownership, and sharing direction |
| Retention | 3 | Business requirements, feasible policies, and open legal decisions |
| Backup and recovery review | 1 | Responsibility, capability, gaps, and recommendation |
| SaaS application control | 1 | Enterprise apps, consent, third-party access, and obvious high-risk cleanup |
| Logging and incident readiness | 2 | Audit/logging settings, contacts, escalation, and initial response readiness |
| Documentation, QA, and customer review | 10 | Baseline record, runbooks, evidence, testing, handoff, roadmap, and acceptance |
| **Total** | **46** | Base controlled environment |

The 46-hour total is a planning baseline, not an unconditional fixed-fee promise.

## Standard scope

### Discovery and prerequisites

- Executive sponsor and stakeholder confirmation
- Users, devices, domains, locations, and entities
- Existing providers and administrative owners
- Licensing review
- Business, security, insurance, and compliance context
- Known incidents and inherited risks
- Customer responsibilities and decision schedule

### Tenant and licensing

- Tenant setup or responsible takeover
- Domain and tenant review
- Licensing alignment
- Administrative ownership
- Existing configuration and material-risk inventory

### Identity and administrator baseline

- MFA
- Conditional Access
- Supported authentication methods
- Separate administrative identities where appropriate
- Emergency access
- Least-privileged roles
- Privileged Identity Management or equivalent controls where appropriate
- Joiner, mover, and leaver procedure
- Guest and external-user direction

### Endpoint management and trust

- Intune foundation
- Enrollment approach
- Device ownership and support standards
- Compliance policies
- Security baselines
- Endpoint protection
- Disk encryption
- Update rings
- Local-administrator direction
- Device retirement procedure

### Messaging and collaboration security

- Exchange and email-protection baseline
- Teams, SharePoint, OneDrive, and group ownership
- External sharing
- Guest access
- Data authority and document-location decisions
- Basic information lifecycle and retention direction

### Security posture and incident readiness

- Secure Score assessment and prioritized improvement
- Defender configuration as licensed
- Enterprise-app and consent review
- Logging and audit settings
- Incident contacts and escalation
- Risk and exception register

### Documentation and handoff

- Customer and environment profile
- Architecture and configuration baseline
- Administrative-access model
- User lifecycle runbook
- Device and security runbooks
- Collaboration and sharing standard
- Open-risk and exception register
- Test and evidence package
- Roadmap
- Customer review and acceptance

## Common exclusions

Unless explicitly included:

- Complex tenant-to-tenant migration
- Large email, file, or application-data migration
- Identity federation redesign
- Extensive Active Directory remediation
- Advanced Purview or eDiscovery implementation
- Formal legal-records analysis
- Custom application remediation
- Advanced compliance implementation
- 24x7 monitoring or support
- Broad end-user help desk
- Network redesign
- Hardware replacement
- Application packaging beyond agreed baseline
- Formal audit, examination, attestation, or legal opinion
- Unsupported operating systems or applications
- Remediation of every Secure Score recommendation regardless of business value

## Prerequisites

- Authorized executive sponsor
- Administrative access
- Accurate or discoverable user and device inventory
- Licensing authority
- Customer availability for decisions
- Agreement on legacy-risk treatment
- Backup or recovery plan for material changes
- Supported devices and operating systems, or an approved exception plan
- Timely access to the incumbent provider when applicable

## Complexity adjustments

Re-estimate or use a paid assessment when any of the following are material:

- Provider is uncooperative
- Administrative access is missing or contested
- Multiple tenants, domains, entities, or identity systems
- Tenant-to-tenant migration
- Hybrid identity or legacy Active Directory complexity
- Large unmanaged-device population
- Unsupported devices or applications
- Significant data cleanup or migration
- Regulated or high-sensitivity data
- Advanced retention or legal requirements
- Multiple locations or unusual network dependencies
- Existing incident or compromise
- Incomplete records
- Material custom integrations

## Delivery stages

1. Qualification and product-variant selection
2. Discovery and inventory
3. Baseline assessment
4. Target configuration and exceptions
5. Commercial scope and approval
6. Pilot
7. Production rollout
8. Verification
9. Documentation and handoff
10. Recurring-governance proposal

## Acceptance evidence

- Approved configuration baseline
- Named administrative ownership
- MFA and Conditional Access evidence
- Privileged-access model
- Managed-device inventory
- Compliance and endpoint-security status
- Email-security baseline
- Sharing and collaboration settings
- Data-authority and retention direction
- Logging and incident contacts
- User and device lifecycle runbooks
- Open-risk and exception register
- Test results
- Customer acceptance

## Pricing status

### Current working baseline

- Foundation Core: $6,000–$9,000; 26–32 hours
- Full Foundation: $12,000–$18,000; 46-hour controlled-environment baseline

### Historical superseded estimate

An earlier $3,500–$7,500 range was developed before the work was decomposed into the 46-hour delivery model. It is retained only as historical context and must not be used as the Full Foundation planning baseline.

Final price must account for:

- Environment complexity
- Takeover risk
- User and device count
- Migration
- Customer readiness
- Licensing
- Partner costs
- Project management
- Documentation and QA
- Warranty and support burden
- Required margin and contingency

## Commercial structure

Keep three layers distinct:

1. Foundation project fee
2. Microsoft licenses passed through cleanly through the approved indirect-CSP/distributor pathway
3. Ongoing Microsoft Security and Governance service

## Recurring attach

- Microsoft Security and Governance
- Security and configuration review
- User and device administration
- License oversight
- Documentation maintenance
- Platform change management
- Roadmap and quarterly review
- Automation monitoring
- Selective escalation or help-desk support where explicitly included

## Required closeout lesson

Every completed Foundation must record:

- Estimated versus actual hours by work area
- Scope changes
- Customer delays
- Rework
- Security outcomes
- Documentation completeness
- Support issues during warranty
- Recommended changes to scope, prerequisites, price, or templates
