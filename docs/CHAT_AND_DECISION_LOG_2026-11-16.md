# Browser Company — conversation and decision continuity log

> Prepared 2026-11-16 as a durable project handoff. This is a **curated reconstruction** of available browser-company chat history, **not** an exported transcript of every ChatGPT message. The full master prompt is preserved separately where available; unknown messages are not fabricated.

## Source-of-truth and provenance

- **Original user-authored master prompt (verbatim, 540 lines):** [ORIGINAL_BROWSER_MASTER_PROMPT_2026-11.md](archive/ORIGINAL_BROWSER_MASTER_PROMPT_2026-11.md) — source attached as `Pasted text.txt`.
- **Historical launch document (extracted text, 7 PDF pages):** [HISTORICAL_LAUNCH_PLAN_2026-11-12_TEXT.md](archive/HISTORICAL_LAUNCH_PLAN_2026-11-12_TEXT.md) — extracted from the user's `Browser_Company_Launch_Plan.pdf`. It is an older alternative plan, **not a current architecture decision**.
- **Repository-maintained rules:** [AGENTS.md](../AGENTS.md), [DECISIONS.md](DECISIONS.md), [BACKLOG.md](BACKLOG.md), [ROADMAP.md](ROADMAP.md).
- **M0 research:** [PR #1](https://github.com/kawaho3/browser-company/pull/1), including [M0 foundation audit](https://github.com/kawaho3/browser-company/blob/research/m0-foundation-audit-20261116/docs/M0_FOUNDATION_AUDIT_2026-11-16.md). This PR was **open and unmerged** at this handoff.
- **Current project overview:** [PROJECT_MASTER_HANDOFF_2026-11-16.md](PROJECT_MASTER_HANDOFF_2026-11-16.md).
- Chat references below summarize available conversations and project context. Do not interpret them as exact quotes unless explicitly indicated.

## Chronology of product requests and decisions

### 2026-11-12 — Initial browser business and cost-conscious launch exploration

- The project was defined as an independent browser company, aiming to compete with Chrome and to be developed primarily by the maintainer and GPT-6 Astra/Codex with near-zero *incremental* software expenditure.
- An **earlier planning alternative**, preserved in the 7-page launch plan, proposed a Windows prototype using C#/.NET/WPF + WebView2 Evergreen, local workspaces, and basic tab/navigation workflows. It recommended testing a focused student/researcher use case and deferring deep extension parity and custom Chromium builds.
- Its estimates (prototype in 1–3 weeks, limited private beta in ~3–5 months) **apply to the former WebView2 prototype scope only**; they are not credible estimates for a native Brave/Chromium fork and must not be carried forward as delivery promises.
- That PDF's cost claims and product hypotheses are dated historical research; current prices, terms and requirements need fresh confirmation.

### 2026-11-13 — Scope changed to a native Chrome-compatible competitor

- The maintainer asked which publicly available browser repositories Codex should use, whether one or a combination was appropriate, and whether mature code could be reused instead of wasting credits.
- The explicit mission became a **real, independent, maintainable native Chromium-compatible browser** — not a website wrapped in Electron, not a disposable prototype, and not a merger of incompatible browser engines.
- Target platform set to **Windows desktop x64 first**.
- GitHub repository chosen for project continuity: **https://github.com/kawaho3/browser-company**.
- The maintainer asked that all goals, architecture guidance, contribution instructions and references be pushed into the repository so an unfamiliar developer could begin without the ChatGPT conversation.
- The planning repository was populated with AGENTS, README, CONTRIBUTING, SECURITY, architecture/vision/decisions, roadmap/backlog, cost/security/legal and reusable-code docs, plus GitHub issue and PR templates.

### 2026-11-15 — Reference repository index and M0 rules

- A 540-line **MASTER PROMPT — BUILD OUR INDEPENDENT WEB BROWSER** was supplied (archived above). It directs detailed research, a complete inventory of the existing repo and 18 study repos, analysis of exactly **Brave Core** versus **direct Chromium**, exactly one final candidate recommendation, Windows native builds only after approval, safe implementation, reproducible evidence, and truthful reporting.
- `REPOSITORIES_TO_STUDY.txt` lists exactly 18 research references; it does **not** mean the repositories are installed or legally approved dependencies.
- The audit snapshot showed 21 tracked files on `main`, with **no native browser source, compiled binary, installer, native build pipeline or integrated AI**. The repo documentation itself explicitly states its planning-only status.
- `AGENTS.md` defines non-negotiable gates: no full Brave/Chromium sync, heavy builds, paid services, production signing, large AI models, scheduled costly CI or unapproved sensitive data flows without maintainer consent.

### 2026-11-16 — Foundation engineering audit and research PR

- Latest verified pre-work `main` commit: `dc6ae368307aad992a436d6812ac196e42be91c8`; 21 tracked files; just the main branch; no earlier open PR or issue at initial check.
- The assistant remotely inspected Brave Core and Chromium code and published build guidance. Research snapshots: Brave Core `4d10ac1f2a4690548ccf5430ca02e72c851bfe74`, Chromium GitHub mirror `4773b76908fb09108dbca92c6e9045c0e5b49342`. **Neither is an approved stable source pin**.
- Brave source paths were found for vertical tabs, split view, extensions, downloads, Shields, Speedreader, installer and updater-related code. Chromium sources were examined for core browser UI, profiles, bookmarks, history, permissions, downloads, extensions, password management, networking, sandbox, accessibility and DevTools.
- A **weighted qualitative engineering comparison** ranked **Brave Core 80.4/100** against direct Chromium **74.4/100** for our privacy/productivity-first, limited-credit goals. These are *judgment-based scores*, not empirical benchmark results.
- **Exactly one candidate was recommended: Brave Core**, using its managed Chromium tree. **This recommendation is not an accepted ADR**; native integration remains blocked by `AGENTS.md` until the maintainer approves the foundation, stable pin, license strategy and resource budget.
- [PR #1](https://github.com/kawaho3/browser-company/pull/1) was opened on `research/m0-foundation-audit-20261116` with the source-backed M0 audit, 18-repo classification, expanded feature references, 6 unit tests, an offline validator, and bounded pull-request CI. Two reported CI runs passed; there was **no native build**. PR remained open and unmerged at this handoff.
- The maintainer separately asked, “which should chose as per ur research 'PHASE 3 — RESEARCH EXACTLY TWO MAIN BROWSER REPOSITORIES'”. Answer: **recommend Brave Core, not direct Chromium**, subject to engineering/licensing approval gates.

### 2026-11-16 — Continuity and document archival request (this task)

- The maintainer reported that lengthy ChatGPT chats become difficult to load and requested **all project findings, diagrams/charts, links, documents and available conversation context be pushed into the GitHub repository**, including a Word document, so future chats and developers can continue from files.
- This archival task does **not** authorize native Brave/Chromium checkout, merger of PR #1, or spending on cloud builds.
- This task preserves the original master prompt verbatim, the old PDF's extract as historical context, and a curated dated decision log. The user did not supply an export of every historical ChatGPT message, so **a complete verbatim chat archive cannot honestly be claimed**.

## Critical distinction: current direction versus historical alternative

| Topic | Earlier 2026-11-12 approach | Latest current project requirement |
| --- | --- | --- |
| Product | Narrow Windows workspace-browser prototype | Real independently branded native Chromium-compatible browser |
| Proposed base | C#/.NET/WPF + WebView2 | **Brave Core proposed**; direct Chromium alternative |
| Extensions/security/browser parity | Substantial gaps deferred | P0 browser feature and security gates required |
| Build | Lightweight Windows app | Heavy native Chromium-class source build, gated |
| Timing | 1–3 week prototype estimate | No measured or promised native fork completion date |
| Decision authority | Prototype plan advisory | `AGENTS.md`, `DECISIONS.md`, maintainer-approved ADR and budget |

**Do not resurrect the WebView2 plan or claim Brave is approved merely because one appeared in a previous assistant recommendation.** Document and seek a new decision if the scope changes again.

## Carry-forward requirements for future contributors and agents

1. Read [START_HERE_NEXT_SESSION.md](../START_HERE_NEXT_SESSION.md), [AGENTS.md](../AGENTS.md), [PROJECT_MASTER_HANDOFF_2026-11-16.md](PROJECT_MASTER_HANDOFF_2026-11-16.md), then check live open PRs/issues/branch heads; do not blindly trust this dated snapshot.
2. Keep exactly one Chromium-based browser foundation. Brave Core already manages Chromium. Never merge complete Firefox, Zen, Ladybird, Min, Chromium and Brave browser trees.
3. Verify reusability, upstream source paths, exact version, third-party licenses, security behavior and update cost before coding anything.
4. Record provenance for every assertion: user instruction versus assistant inference versus source-verified repository fact versus measured result.
5. Do **not** publish secrets, emails, credentials, real user browsing history, or confidential conversation content into a public GitHub repository.
6. Do not send page data to AI services without explicit user permission. Treat web content as untrusted instructions and require confirmation for consequential actions.
7. Keep M0, M1–M5 status accurate; never claim a native browser is compiled, private by default, Chrome-extension compatible or secure without evidence.
8. At the end of every work session, append a concise timestamped update: branch/commit/PR, files changed, tests run with exact command and outcome, active blockers, next safe smallest task, approval status, and updated source links. Preserve old entries rather than silently rewriting history.

## Proposed session-log template (append to this file, never overwrite earlier history)

~~~text
Date/time (timezone):
Maintainer request:
Base branch / starting SHA:
Source evidence inspected:
Decisions made (proposed or approved):
Files and commits:
PR(s) opened/merged (exact URL):
Tests commands and results:
Costs incurred / downloads / CI minutes:
Security/license/privacy considerations:
What was not done and why:
Required approval:
Smallest next task and acceptance test:
~~~

## Relevant permanent links

- Main repo: https://github.com/kawaho3/browser-company
- Open M0 PR at archival time: https://github.com/kawaho3/browser-company/pull/1
- Brave Core: https://github.com/brave/brave-core
- Chromium source: https://chromium.googlesource.com/chromium/src
- Chromium mirror: https://github.com/chromium/chromium
- Official Chromium Windows builds: https://chromium.googlesource.com/chromium/src/+/main/docs/windows_build_instructions.md
- Brave Windows contributor guidance: https://github.com/brave/brave-browser/wiki/Windows-Development-Environment
- Entire 18-repo list and links: [REPOSITORIES_TO_STUDY.txt](../REPOSITORIES_TO_STUDY.txt)
