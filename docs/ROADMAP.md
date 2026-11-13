# Roadmap — Evidence-Gated Delivery

**The sequence below is a proposed plan, not a schedule promise.** Milestones depend on capability, build resources, maintainers and user testing. Budget guardrails matter more than arbitrary dates.

## M0 — Research and foundation selection (NOW)

Deliverables:
- [ ] Inspect Brave Core and direct Chromium, including release/update maintenance.
- [ ] Produce complete dependency/license/source-provenance inventory.
- [ ] Verify Chrome-parity feature availability and gaps (docs/FEATURE_MATRIX.md).
- [ ] Compare upstream patch burden, developer onboarding, build complexity and security response.
- [ ] Approve company-level license and contribution terms.
- [ ] Design secure credentials, signing, update/release and reporting ownership.
- [ ] Select the primary source via a signed-off ADR.
- [ ] Approve a realistic build machine and budget caps.

**Gate:** a documented decision with owner, evidence, risk register and approved costs.

## M1 — Reproducible unmodified upstream

- [ ] Pin stable upstream source and validate integrity.
- [ ] Build using appropriate hardware; record setup, RAM, disk, time and cost.
- [ ] Run upstream smoke tests and baseline performance measurements.
- [ ] Create a developer reproducibility guide and CI plan.
- [ ] Verify upstream security patch/merge process.

**Gate:** repeatable upstream build and smoke tests on Windows target or chosen platform. No new browser features before this gate.

## M2 — Independent browser identity and core parity

- [ ] Replace logos/name/trademarks with owned, reviewed assets and identifiers.
- [ ] Audit/remove or replace provider-owned services and keys.
- [ ] Test navigation, downloads, history, bookmarks, profiles, private mode, passwords and extensions.
- [ ] Prepare independent signed install/update strategy with rollback.
- [ ] Build minimum automated regression suite, a11y baseline and bug triage.

**Gate:** alpha browser on a test machine with security/update ownership understood.

## M3 — Productivity differentiation

- [ ] Validate user needs for vertical tabs, workspaces, tab search and split view.
- [ ] Implement one differentiating workflow with measured usability benefit.
- [ ] Improve performance; audit memory and battery regressions.
- [ ] Provide migration/import from existing browsers where legally/technically possible.

**Gate:** small external alpha feedback; stable use of critical workflows.

## M4 — Optional AI Research Workspace

- [ ] Decide local model support, constraints and model license.
- [ ] Add consent-driven page summarization/research with clear data-sharing UX.
- [ ] Isolate untrusted page content and AI tools; test prompt-injection scenarios.
- [ ] Only then evaluate controlled task automation with user review.

**Gate:** documented safety/privacy expectations and independent evaluation.

## M5 — Public release and expansion

- [ ] Legal/privacy disclosures, privacy testing, support, crash triage and incident response.
- [ ] Signed artifacts and updater reliability demonstrated.
- [ ] Upstream security release cadence sustained.
- [ ] Launch Windows version when gates pass; evaluate macOS/Linux/Android and sync separately.

**Gate:** actual user retention and security/quality data justify expansion.

## Out of scope until separately approved

Building a new rendering engine, arbitrary “all features” mega-PRs, proprietary Google sync/DRM access assumptions, unaudited copy-paste of other browsers, costly recurring services, and full-scale cloud builds without sizing/cost analysis.
