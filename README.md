# Browser Company

**Mission:** Build an independent, secure, fast, privacy-respecting browser that can become a credible competitor to Google Chrome—using a disciplined combination of mature open-source components and original product innovation.

> **Status: PLANNING / DOCUMENTATION ONLY (2026-11-13).** This repository does **not** yet contain a browser fork, compiled application, installer, running AI agent, CI build, or completed security review. Do not describe planned features as implemented.

## Product thesis

- **Parity first:** reliable browsing, tabs, downloads, history, profiles, extension compatibility, accessibility, and timely security fixes.
- **Differentiation next:** powerful workspaces, efficient tab management, optional private/on-device AI assistance, and permission-controlled browser automation.
- **Reuse over rewrite:** choose exactly one browser foundation. Audit upstream features and compatible libraries before generating code.
- **Sustainable operation:** an independent product needs updates, testing, distribution, privacy practices, and maintenance—not just a one-time build.
- **Budget conscious:** development is intended to be Codex-assisted, with limited credits and a preference for free/open-source tools. Full Chromium-class builds need a suitably resourced machine/CI, not an assumed small cloud sandbox.

**Provisional technical direction:** evaluate [Brave Core](https://github.com/brave/brave-core) (a Chromium customization layer) against direct [Chromium](https://github.com/chromium/chromium) before committing to a fork. Brave Core is **not yet chosen or vendored**.

## Start here

| Audience | Start |
| --- | --- |
| New contributor | [Onboarding](docs/ONBOARDING.md) and [Contributing](CONTRIBUTING.md) |
| Codex / AI coding agent | [AGENTS.md](AGENTS.md) first |
| Product / design | [Vision](docs/VISION.md) and [Feature matrix](docs/FEATURE_MATRIX.md) |
| Tech lead | [Architecture](docs/ARCHITECTURE.md), [Reuse catalog](docs/REUSE_CATALOG.md), [Complete repository study list](REPOSITORIES_TO_STUDY.txt), [Decision log](docs/DECISIONS.md) |
| Build engineer | [Build, environments & cost](docs/BUILD_AND_COST.md) |
| Security / legal | [Security policy](SECURITY.md), [Security & privacy](docs/SECURITY_AND_PRIVACY.md), [Ownership & licensing](docs/LEGAL_AND_BRANDING.md) |
| Project manager | [Roadmap](docs/ROADMAP.md) and [Backlog](docs/BACKLOG.md) |

## Current milestone: M0 — due diligence

1. Audit existing Brave Core / Chromium features, versions, maintenance, licenses and architecture.
2. Build a verified feature inventory. Mark assumptions and untested claims clearly.
3. Select the primary foundation in an Architecture Decision Record (ADR).
4. Agree on project and contribution licensing, trademarks, and governance.
5. Prove a *small, bounded* integration path before an approved full upstream checkout/build.
6. Prepare a reproducible builder and measure disk, RAM, build time, and cost.

**M0 exit criteria:** a documented stack decision, evidence-backed risks, a license inventory, build plan, benchmark baseline, and an approved implementation scope. No product release before security and update processes exist.

## Development strategy

~~~mermaid
flowchart TD
    A[Product goals and acceptance criteria] --> B[Audit Chromium / Brave Core]
    B --> C{Capability already exists?}
    C -->|Yes| D[Reuse, configure and test upstream]
    C -->|No| E[Evaluate maintained compatible OSS]
    E --> F{License, security and integration pass?}
    F -->|Yes| G[Integrate a small component]
    F -->|No| H[Implement the narrow missing feature]
    D --> I[Targeted tests]
    G --> I
    H --> I
    I --> J[Review, release and monitor]
~~~

## Non-negotiable practices

- Never merge Firefox, Brave, Chromium and other complete browser trees into one application.
- Avoid reimplementing encryption, sandboxing, password protection or web rendering.
- Never include paid APIs, large model downloads, external telemetry, or costly CI/build jobs without explicit approval.
- Never claim Chrome proprietary services (sync, DRM, Google service keys) come automatically with Chromium.
- Never distribute third-party trademarks or covered code without meeting relevant conditions.
- Do not use “works” or “tested” for an unexecuted build.

## How to contribute right now

This is a **public planning repository**, not yet an open-source licensed browser source tree. Open a proposal or research issue, improve documentation, and review [CONTRIBUTING.md](CONTRIBUTING.md). The maintainer must decide the top-level license and contributor terms before accepting substantial new code.

### Project links

- Repository: https://github.com/kawaho3/browser-company
- Issues: https://github.com/kawaho3/browser-company/issues
- Security: [SECURITY.md](SECURITY.md)

*This project is independent; it is not affiliated with Google, Chromium, Brave, Mozilla, Microsoft, or OpenAI.*
