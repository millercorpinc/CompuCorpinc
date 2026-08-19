const documentViews = {
  'launch-program': {
    category: 'Launch', title: 'Launch Program', status: 'Established baseline', source: 'docs/launch/00-LAUNCH-PROGRAM.md', summary: 'A dependency-aware path from developed concept to a legally established, commercially ready, secure, and deliverable business.', sections: [
      ['Objective', ['Move from concept to a company that can earn and complete a paid pilot with appropriate legal, commercial, security, delivery, and evidence foundations.']],
      ['Workstreams', ['Founder governance', 'Name, brand, and intellectual property', 'Legal entity, tax, finance, insurance, contracts, and risk', 'Service, pricing, partners, internal technology, sales, delivery, pilots, and specialist capacity']],
      ['Stage gates', ['Gate 1: Founder alignment, including roles, decision rights, ownership principles, conflict handling, capital, and compensation.', 'Gate 2: Legal readiness, including an approved name, entity, tax and banking setup, insurance, and contract framework.', 'Gate 3: Commercial readiness, including the initial customer, offer, scope, pricing, proposal process, and partner dependencies.', 'Gate 4: Delivery readiness, including security, documentation, access, testing, acceptance, escalation, and capacity.', 'Gate 5: Pilot launch, including a qualified opportunity, signed agreement, delivery owner, success measures, and evidence capture.']]
    ]
  },
  '90-day-launch': {
    category: 'Launch', title: '90-Day Launch Plan', status: 'Working plan', source: 'docs/operations/01-90-DAY-LAUNCH-PLAN.md', summary: 'A short execution horizon that sequences foundation work, commercial readiness, and the first paid pilot.', sections: [
      ['Days 1–30: establish', ['Resolve founder and legal dependencies.', 'Set up finance, insurance, contracts, and internal security.', 'Choose the first customer profile and launch offer.']],
      ['Days 31–60: prepare', ['Build the warm-network account list.', 'Create discovery, proposal, and delivery materials.', 'Research Microsoft and distributor pathways.', 'Test the internal operating stack and handoff process.']],
      ['Days 61–90: validate', ['Contract the first paid pilot.', 'Measure planned versus actual effort.', 'Capture customer proof and lessons.', 'Offer a defined recurring-governance next step.']],
      ['Success criteria', ['A legally and commercially usable operating core exists.', 'The first offer has defined scope, exclusions, pricing assumptions, and delivery evidence.', 'The team can run a qualified opportunity through signed scope, delivery, acceptance, and closeout.']]
    ]
  },
  'launch-backlog': {
    category: 'Launch', title: 'Launch Backlog', status: 'Working backlog', source: 'ops/launch-backlog.yaml', summary: 'The execution queue for launch tasks, ownership, dependencies, and evidence. Task status must be maintained in the repository backlog.', sections: [
      ['How to use it', ['Treat each backlog item as work with an owner, dependency, completion evidence, and status.', 'Do not mark a task complete because an intention exists; record the artifact or external confirmation that proves completion.', 'Keep unresolved decisions visible until the relevant founder or qualified professional approves them.']],
      ['Priority work', ['Founder terms and authority', 'Name, entity, tax, banking, insurance, and contracts', 'Secure Workplace Foundation scope and commercial model', 'Internal security baseline and operating stack', 'Partner and distributor qualification', 'Sales readiness and first paid pilot']],
      ['Completion evidence', ['Founder and counsel-ready terms', 'Formation and insurance records', 'Approved service brief, cost model, and proposal flow', 'Tested internal controls and delivery playbook', 'Partner evaluation record', 'Signed pilot, acceptance, closeout, and lessons']]
    ]
  },
  'founder-term-sheet': {
    category: 'Governance', title: 'Founder Term Sheet', status: 'Draft working recommendation', source: 'docs/launch/04-FOUNDER-TERM-SHEET.md', summary: 'A reviewable working structure for founder control, sales and execution incentives, and the legal questions that must be settled before equity is issued.', sections: [
      ['Working assumptions', ['The founder carrying legal and financial responsibility retains final control.', 'Sales and execution are distinct roles with different compensation and ownership logic.', 'Equity is earned and vested through real company outcomes, not promises or pipeline alone.', 'A future-use pool is reserved for later hires or strategic contributors.']],
      ['Illustrative allocation', ['Founder-controlled equity: 51% minimum.', 'Sales pool: 20%.', 'Execution pool: 20%.', 'Reserved future-use buffer: 9%.', 'These percentages are a working recommendation, not an approved ownership decision.']],
      ['Guardrails', ['No contributor can bind the company without written authorization.', 'Unvested equity remains with the company.', 'Each contributor has a role-specific cap.', 'A qualifying deal must be paid and accepted before incentive vesting.']],
      ['Counsel review required', ['Entity and tax structure', 'Issuance timing, voting, reserved decisions, departure, and buyout terms', 'IP assignment, confidentiality, worker classification, contract authority, repurchase, and clawback rights']]
    ]
  },
  'legal-finance-risk': {
    category: 'Launch', title: 'Legal, Finance, and Risk Setup', status: 'Execution checklist', source: 'docs/launch/02-LEGAL-FINANCE-AND-RISK.md', summary: 'A checklist for professional review and operational setup. It is not legal, tax, accounting, or insurance advice.', sections: [
      ['Legal and entity', ['Name availability and trademark screening', 'Entity and jurisdiction analysis', 'Formation, registered agent, operating agreement, and required registrations', 'IP assignments and contractor or employee documents']],
      ['Tax and finance', ['EIN and tax registrations', 'Tax election analysis', 'Business bank account and accounting system', 'Expense, invoicing, collections, payroll, sales-tax, and license-resale analysis', 'Financial forecast and capital or cash-reserve plan']],
      ['Insurance', ['Discuss general liability, professional liability or E&O, cyber liability, workers compensation, crime or fidelity, employment practices, directors and officers, auto, and umbrella coverage with a qualified broker.']],
      ['Contract framework', ['Master services agreement and statements of work', 'Managed-services and service-level schedules', 'Data protection, security, confidentiality, and access terms', 'Subcontractor, partner, referral, change-order, offboarding, and transition terms']]
    ]
  },
  'secure-workplace-foundation': {
    category: 'Services', title: 'Secure Workplace Foundation', status: 'Presumptive launch service', source: 'docs/services/01-SECURE-WORKPLACE-FOUNDATION.md', summary: 'A standardized Microsoft 365 foundation for organizations that need consistent identity, endpoint, collaboration, security, and administrative controls.', sections: [
      ['Ideal customer and triggers', ['A 10–150-person Microsoft 365 organization without a consistent baseline.', 'Common triggers include a new tenant, acquisition, provider change, cyber-insurance pressure, rapid growth, device-management rollout, or an access-control concern.']],
      ['Standard outcomes', ['Governed identities and administrator access', 'MFA and Conditional Access baseline', 'Managed endpoints and endpoint security', 'Controlled collaboration and sharing', 'Clear ownership, documentation, prioritized risks, and readiness for recurring governance']],
      ['Delivery sequence', ['Discovery and inventory', 'Baseline assessment', 'Target configuration and exceptions', 'Pilot and production rollout', 'Verification, documentation, handoff, and recurring-governance proposal']],
      ['Scope boundaries', ['Complex tenant migration, large data migration, custom application remediation, advanced compliance, 24x7 support, network redesign, hardware replacement, formal attestation, extensive end-user remediation, and unsupported systems require explicit treatment or exclusion.']],
      ['Working commercial model', ['Foundation Core: $6,000–$9,000 for a small baseline.', 'Foundation Full: $12,000–$18,000 for a normal operating business.', 'Foundation Complex: $18,000+ where takeover, migration, regulatory, or nonstandard complexity is material.', 'These are working planning assumptions requiring customer and cost-model validation.']]
    ]
  },
  'open-questions': {
    category: 'Governance', title: 'Open Questions', status: 'Open decisions', source: 'knowledge/OPEN-QUESTIONS.md', summary: 'The unresolved questions that must remain visible instead of being silently converted into policy.', sections: [
      ['Founder and legal', ['What is the final company name?', 'What ownership, vesting, voting, compensation, authority, and departure terms will founders approve?', 'What legal and tax structure will qualified advisors recommend?']],
      ['Commercial and delivery', ['Which launch offer sequence will be approved?', 'What pricing, margin, support boundary, service levels, exclusions, and escalation model will be used?', 'What is the first pilot customer and what evidence will validate the offer?']],
      ['Partners and systems', ['Which distributor or indirect CSP will be selected?', 'Which specialist and independent-professional relationships are required?', 'Which internal operating tools meet the requirements without overbuilding?']],
      ['Decision rule', ['Record owner, status, evidence needed, and next review date for each question. Do not describe an open question as settled in customer-facing or canonical material.']]
    ]
  },
  'partner-strategy': {
    category: 'Partners', title: 'Partner Strategy and Evaluation', status: 'Draft working strategy', source: 'docs/business/05A-PARTNER-STRATEGY-AND-EVALUATION.md', summary: 'A partner model that keeps the company accountable for customer strategy and governance while using external organizations for distribution, specialists, regulated work, and coverage.', sections: [
      ['Partner categories', ['Microsoft partner pathway', 'Distributor or indirect CSP', 'Security, compliance, legal, tax, accounting, networking, field, development, data, and analytics specialists', 'Referral relationships with accountants, lawyers, brokers, consultants, vendors, and channel partners']],
      ['Keep internal', ['Customer strategy and discovery', 'Target-state architecture and project ownership', 'Service standards, governance, documentation, communication, commercial ownership, and scope control']],
      ['Partner-led when appropriate', ['Licensing and billing', 'Specialist security assessments', 'Independent audit or attestation', 'Telecom, physical installation, field services, hardware, and specialist engineering']],
      ['Evaluation criteria', ['Capability, route to market, provisioning, billing, support, economics, onboarding, automation, security, transition, enablement, contract complexity, and customer experience.', 'Do not select a distributor on margin alone.']]
    ]
  },
  'partner-distributor-setup': {
    category: 'Partners', title: 'Partner and Distributor Setup', status: 'Launch setup guide', source: 'docs/launch/04-PARTNER-AND-DISTRIBUTOR-SETUP.md', summary: 'A practical setup sequence for comparing candidate partner pathways before committing customer or licensing operations to one provider.', sections: [
      ['Setup sequence', ['Confirm the legal entity and launch offer.', 'Document the customer and licensing operating model.', 'Shortlist Microsoft, distributor, specialist, referral, and independent-professional candidates.', 'Run a structured comparison and record evidence.', 'Pilot the selected relationship before scaling.']],
      ['Questions to resolve', ['Who owns customer billing, support, renewals, and escalations?', 'What are the security, data, tax, credit, and contract requirements?', 'How does customer onboarding, transition, termination, and offboarding work?', 'What enablement and automation capabilities are available?']],
      ['Decision guardrail', ['Partner selection remains candidate-neutral until the evidence, commercial model, customer experience, security posture, and exit path support a decision.']]
    ]
  },
  'partner-playbook': {
    category: 'Partners', title: 'Partner Playbook', status: 'Working playbook', source: 'docs/operations/04-PARTNER-PLAYBOOK.md', summary: 'Operating rules for qualifying, engaging, reviewing, and exiting partner relationships.', sections: [
      ['Before engagement', ['Define role, scope, customer ownership, contracting party, pricing, confidentiality, data handling, security, insurance, liability, and escalation.', 'Confirm independence requirements where regulated or attestation work is involved.']],
      ['During delivery', ['Keep the company accountable for the customer relationship, architecture, standards, scope, communication, and governance.', 'Use least-necessary access, documented handoffs, explicit changes, and evidence of partner performance.']],
      ['Review and exit', ['Review service quality, security, economics, customer experience, conflicts, and continuity on a defined cadence.', 'Maintain termination, transition, access expiration, and customer communication plans.']]
    ]
  },
  'partner-profile': {
    category: 'Templates', title: 'Partner Profile Template', status: 'Reusable template', source: 'templates/PARTNER-PROFILE.md', summary: 'A structured record for partner evidence, risk, commercial terms, ownership, and review decisions.', sections: [
      ['Profile fields', ['Organization, category, capabilities, contacts, service territory, credentials, insurance, and relevant customer references.', 'State the proposed role, scope, customer ownership, contracting party, and internal accountable owner.']],
      ['Risk and controls', ['Record security posture, data handling, access model, continuity, independence, liability, indemnification, and known conflicts.', 'Document required customer data, access expiration, incident route, and transition plan.']],
      ['Commercial and review', ['Capture pricing, referral economics, billing, support, escalation, renewal, termination, and customer-impact assumptions.', 'Set qualification status, decision owner, next review date, evidence links, and open questions.']]
    ]
  },
  'chicago-market-assessment': {
    category: 'Launch', title: 'Chicago Market and Microsoft Assessment Brief', status: 'Proposed working brief', source: 'docs/launch/07-CHICAGO-MARKET-AND-MICROSOFT-ASSESSMENT-BRIEF.md', summary: 'A proposed Chicago and Chicagoland launch test covering physicians, accounting, field services, and regulated professional firms.', sections: [
      ['Launch market', ['Test physicians and clinics, CPA and accounting firms, construction and field services, and legal or other regulated professional firms.', 'Use approximately five accounts per track as a flexible starting point, then compare response, urgency, buying access, delivery complexity, price acceptance, and referral potential.']],
      ['Entry offer', ['Lead with a paid, fixed-fee Technology and Security Baseline Assessment.', 'Make the Microsoft baseline one week. Add business-systems and vertical-risk modules as separate optional one-week modules.', 'Require assessment evidence before migration or takeover work.']],
      ['Microsoft baseline', ['Entra ID, MFA, Conditional Access, privileged access, Intune, device compliance, Defender, email security, Teams, SharePoint, OneDrive, sharing controls, licensing review, Secure Score, and operational handoff.', 'Purview, retention, advanced Defender, and PIM are licensing-dependent and validated during discovery.']],
      ['Deliverables and boundaries', ['Executive findings report, technical baseline report, and target-state roadmap.', 'Technology readiness and remediation support only. No legal advice, formal certification, audit, attestation, unlimited help desk, hardware replacement, or network redesign.']],
      ['Temporary Bernard Cole (Ben) and Michael rule', ['Bernard Cole (Ben) owns logistics, project workspace, action tracking, delivery coordination, and operational follow-through.', 'Bernard also brings senior Microsoft 365, EUC, endpoint, security operations, migration, automation, and vendor-governance experience to technical delivery.', 'Michael leads customer meetings, relationship cadence, commercial continuity, and the executive narrative.', 'Both contribute to delivery; each engagement names one project lead and Harvey reviews technical findings and high-risk decisions.']]
    ]
  }
};

function documentLink(key, label) {
  return `<a class="doc-link" href="document.html?doc=${key}">${label || documentViews[key].title}</a>`;
}

function renderDocumentLibrary() {
  const library = document.querySelector('#document-library');
  if (!library) return;
  const groups = {};
  Object.entries(documentViews).forEach(([key, view]) => {
    groups[view.category] ||= [];
    groups[view.category].push(`<article class="document-card"><span class="card-kicker">${view.status}</span><h3>${view.title}</h3><p>${view.summary}</p>${documentLink(key, 'Open web view')}</article>`);
  });
  library.innerHTML = Object.entries(groups).map(([category, cards]) => `<section class="document-group"><h3>${category}</h3><div class="document-grid">${cards.join('')}</div></section>`).join('');
}

function renderDocument() {
  const view = document.querySelector('#document-view');
  if (!view) return;
  const key = new URLSearchParams(window.location.search).get('doc');
  const documentView = documentViews[key];
  if (!documentView) {
    view.innerHTML = '<section class="page-hero"><div class="container"><p class="eyebrow">Document library</p><h1>That working view is not available.</h1><p class="lead">Choose a document from the library to continue.</p><a class="primary" href="documents.html">Open document library</a></div></section>';
    return;
  }
  document.title = `CompuCorp | ${documentView.title}`;
  view.innerHTML = `<section class="page-hero"><div class="container"><p class="eyebrow">${documentView.category} · ${documentView.status}</p><h1>${documentView.title}</h1><p class="lead">${documentView.summary}</p><p class="notice">Web view of ${documentView.source}. The canonical repository document remains authoritative; this page does not approve open decisions.</p></div></section><section class="section"><div class="container document-content">${documentView.sections.map(([heading, items]) => `<section class="document-section"><h2>${heading}</h2>${items.length === 1 ? `<p>${items[0]}</p>` : `<ul>${items.map(item => `<li>${item}</li>`).join('')}</ul>`}</section>`).join('')}<a class="secondary" href="documents.html">Back to document library</a></div></section>`;
}

document.addEventListener('DOMContentLoaded', () => {
  renderDocumentLibrary();
  renderDocument();
  const yearNode = new Date().getFullYear();
  const footerText = document.querySelector('.site-footer p');
  if (footerText) footerText.textContent = footerText.textContent.replace('· Not for external distribution', `· ${yearNode} · Not for external distribution`);
});
