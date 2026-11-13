# Proposed Technical Architecture

> **Provisional design — not implemented.** Finalize primary browser foundation after M0 audit.

## Core decision: one browser foundation, many bounded modules

**Candidate A: Brave Core + its managed Chromium tree (preferred to evaluate first).** Reuses a substantial Chromium customization layer and its existing ad-blocking integration.

**Candidate B: direct Chromium fork.** Cleaner starting line, but requires building and maintaining more custom features.

**Not viable:** merging whole Brave, Firefox/Zen, Chromium, and Min Browser repositories. They have incompatible engine/toolchain/product architectures.

~~~mermaid
flowchart TB
    UI[Company branded UX<br/>Tabs, workspaces, settings, accessibility]
    APP[Browser application layer<br/>Profiles, history, downloads, bookmarks, extensions]
    CORE[Chosen Chromium-based foundation<br/>Brave Core OR Chromium directly]
    WEB[Chromium rendering, networking, JS engine, sandbox, storage]
    PRIV[Privacy and protections<br/>Prefer audited upstream functions]
    AI[Optional local AI adapter<br/>On-device engine / approved remote provider]
    ACTION[Permissioned automation broker]
    SYNC[Future opt-in sync service]
    RELEASE[Build, signing, update, monitoring]
    UI --> APP --> CORE --> WEB
    APP --> PRIV
    APP --> AI
    AI --> ACTION
    APP -. opt-in .-> SYNC
    CORE --> RELEASE
~~~

The diagram shows **responsibility boundaries**, not verified API integrations.

## Layer boundaries

### Browser core

Let upstream own renderer processes, JavaScript execution, networking, sandbox, site isolation, certificate handling and most extension plumbing. Keep company-specific patches minimal and upstream version pinned.

### Product customization

Design a clearly isolated application layer for identity/branding, start page, tab search, vertical tabs, sessions, workspaces, split view and settings. Integrate using supported extension points or small, reviewable patches after source audit.

### Privacy

Start with existing protections; do not duplicate native adblock-rust if it is already part of the selected Brave Core checkout. Review filter handling, permissions, anti-fingerprinting claims, safe browsing decisions and user controls.

### AI adapter (optional)

Use a product-facing interface such as: summarize selected content, answer questions from explicitly shared context, extract an outline, organize tabs, and prepare a draft action plan. Potential candidate: llama.cpp as an **on-device inference engine**, with model license and hardware support separately reviewed. A model engine is not the entire assistant.

### Browser automation broker

Enforce explicit action boundaries: per-task permission, read/write separation, confirmation for consequential actions, restricted site access, ability to stop, audit without sensitive content, and defense against webpage prompt injection. Browser Use / Stagehand are research candidates, not automatic production dependencies.

### Sync and cloud services (later)

Treat browser identity, cross-device sync, updates, crash reporting and any remote AI as separate services requiring independent architecture, infrastructure costs, privacy and security review. Do not assume Google Chrome or Brave-owned backend credentials can be reused.

## Data classification

| Class | Examples | Default handling |
| --- | --- | --- |
| Sensitive local | Passwords, cookies, tokens, browsing history | Local/OS-supported protection; avoid telemetry |
| User content | Open pages, selected text, research workspaces | Never send to AI cloud without explicit opt-in |
| Public config | App version, non-secret feature flags | Integrity validation and signed release metadata |
| Anonymous diagnostics | Crash counters, sanitized errors | Only after explicit product/privacy decision |

## Cross-cutting requirements

- Windows desktop first for initial evaluation; other targets after feasibility review.
- A11y, localization and keyboard use built into feature acceptance tests.
- Security release cadence tied to upstream Chromium updates.
- Reproducible build and signing pipeline before public binary distribution.
- No unapproved proprietary Google services, Widevine/DRM claims, cloud APIs or model hosting.

## Architecture acceptance

An approved ADR must specify exact upstream tag/commit, patch strategy, dependency ownership, build OS/requirements, update strategy, license obligations, feature-test baseline and exit criteria. See [DECISIONS](DECISIONS.md).
