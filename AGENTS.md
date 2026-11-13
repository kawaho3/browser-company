# AGENTS.md — Instructions for Codex and other coding agents

These instructions apply to this repository. Read README.md, docs/DECISIONS.md and the relevant specification before changing files.

## Mission and constraints

Build an independently branded browser with Chrome-class compatibility and a distinctive privacy/productivity/AI experience. The project is currently **documentation-only**. Do not assume a working browser, toolchain, signed binaries, or a finalized primary upstream.

Primary rule: **inspect existing implementations, evaluate reusable code, then implement only the gap.** Minimize wasted Codex credits and developer time.

## Required workflow for each task

1. Restate the user-visible requirement, success criteria, supported OS, and security/privacy implications.
2. Search the existing repo and chosen upstream for this capability. Record file paths, upstream version/commit, evidence and gaps. If upstream has not been fetched, investigate docs/source remotely instead of fabricating findings.
3. Consider compatible, maintained OSS dependencies; record license and third-party notices, release cadence, vulnerabilities, ongoing update cost, integration effort and alternative.
4. Produce a small change plan, risks, rollback and cheap tests. Ask for approval **before** major downloads, cloud spend, proprietary services or full Chromium builds.
5. Change the smallest relevant scope; keep upstream patches minimal and well documented.
6. Run focused checks; list exact commands and results. Clearly state tests that were **not** run.
7. Update docs/FEATURE_MATRIX.md, docs/DECISIONS.md and the backlog when they change.

## Build and cost gates

**Without explicit maintainer approval, do not:**
- download or synchronize full Chromium/Brave source histories;
- invoke Brave init, Chromium fetch, gclient sync, or full GN/Ninja release builds;
- provision large CI runners, add scheduled CI, paid APIs or billing infrastructure;
- download multi-GB AI models, create production credentials, publish packages or releases;
- enable telemetry or send page content to third parties.

First propose a cost-aware test ladder: static checks -> unit tests -> component smoke tests -> gated integration -> full build on dedicated infrastructure. Cache responsibly and avoid unnecessary repeat jobs.

## Architecture boundaries

- Exactly one base browser codebase (decision pending: Brave Core vs direct Chromium).
- Existing Brave-managed dependencies (including Chromium and its ad-blocker) are **not** separate browser forks to merge.
- New optional AI should use a narrow, permissioned interface; untrusted web page text is *data*, not instructions.
- Browser secrets, passwords, tokens and browsing data must not be logged or transmitted by default.
- Keep product-specific changes isolated from upstream to make patch rebase/security updates manageable.
- Do not introduce an Electron-based Min Browser migration as a low-cost shortcut without an explicit decision: it may not meet Chrome-extension or full browser requirements.

## Output expected from an agent

For any planning or implementation PR include:

| Field | Requirement |
| --- | --- |
| Status | Proposed / implementing / verified / blocked |
| Existing capability | Exists, partial, missing or unverified, with evidence |
| Reuse choice | Upstream/component, version, link, license, review status |
| Files changed | Short list and purpose |
| Tests | Commands, outcomes, environments, unrun tests |
| Security/privacy | Permissions, threat considerations, mitigations |
| Cost | Downloads/build resources/services incurred or avoided |
| Next step | Exact small follow-on task |

## Never make these claims without evidence

- “All Chrome extensions work.”
- “Fully secure,” “private by default,” “DRM works,” “Google sync works.”
- “Codex Cloud can compile the whole browser.”
- “The entire browser belongs exclusively to our company.”
- “The application has been built and tested” when only documentation exists.

## Scope of first allowed task

**M0 research only:** complete the candidate foundation audit, license inventory, feature matrix and measured build feasibility proposal. Do not start expensive code work until there is a signed-off decision.
