# Architecture Decision Log (ADRs)

These are **planning decisions** as of 2026-11-13. They do not imply a tested implementation. Record any change with issue/PR link, author, date, options, evidence and consequences.

## ADR-001 — One primary browser foundation

- **Status:** Accepted as strategy, implementation pending.
- **Decision:** Use one Chromium-based browser base and integrate only compatible components.
- **Rationale:** Whole-browser mergers create incompatible engines, security update debt, duplicated systems and high cost.
- **Consequences:** Need an upstream patch/update strategy; feature work is bounded to the chosen platform.

## ADR-002 — Foundation selection

- **Status:** **Proposed, NOT final.**
- **Preferred candidate to audit:** Brave Core, because it already customizes Chromium and integrates mature privacy features.
- **Comparison candidate:** direct Chromium; potentially cleaner autonomy at the cost of additional feature work.
- **Exit evidence:** build machine needs, licensing impact, security patch cadence, branding/service removal complexity, extension behavior, capabilities and maintainer effort.
- **Owner action required:** approve an ADR selecting and pinning the base.

## ADR-003 — Initial platform

- **Status:** Proposed.
- **Decision:** Focus validation on Windows desktop first; widen OS support after stable, measured desktop releases.
- **Reason:** Avoid fragmenting limited build and QA resources.

## ADR-004 — Credit-conscious development

- **Status:** Accepted as working policy.
- **Decision:** Research/reuse before writing code; target cheap tests; gate full upstream synchronization and compilation behind explicit budget approval.

## ADR-005 — Optional, permissioned AI

- **Status:** Design principle accepted, implementation not chosen.
- **Decision:** AI must work as an optional module, respect page data boundaries and require approval for consequential actions. No default paid API commitment.
- **Open:** on-device model formats, runtime, supported hardware, accessibility and exact consent UX.

## ADR-006 — Company-owned product with third-party components

- **Status:** Goal agreed; **license specifics unresolved**.
- **Decision:** Keep original work and branding under company control while observing licenses of reused software.
- **Open:** company code license, contributor agreements, third-party notices and source-distribution plan.

## Open questions

1. Brave Core vs direct Chromium and exact stable upstream tag?
2. How to rebrand while maintaining an upgrade-friendly patch stack?
3. What production build infrastructure and signing key custody?
4. How are sync, updater, crash handling, search defaults and any cloud services owned?
5. What is the first winning differentiator supported by real user research?
6. Which project-wide license and contribution agreements are adopted?
7. What is a sustainable security patch SLA?

**Process:** write an ADR proposal in a PR; do not silently treat a candidate library as selected.
