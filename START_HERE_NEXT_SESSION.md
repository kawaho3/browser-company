# START HERE — Resume Browser Company Without Any Prior Chat

**Repository:** https://github.com/kawaho3/browser-company  
**Date of this checkpoint:** 2026-11-16  
**Project type:** Native independently branded Chromium-compatible Windows x64 browser, NOT Electron or WebView2 prototype  
**Implementation state:** Planning/M0 research; no compiled browser or installer  
**Provisional foundation:** Brave Core, with Chromium inside its managed dependencies (80.4/100 versus direct Chromium 74.4/100 qualitative research score)  
**Important:** The foundation has **NOT yet been approved** for native integration.

## Read these in order

1. [AGENTS.md](AGENTS.md) — binding engineering rules and expensive-build gates.
2. [Master research and project handoff](docs/PROJECT_MASTER_HANDOFF_2026-11-16.md) — consolidated vision, architecture, 18 repository table, Brave/Chromium scorecard, source links, security/cost/tasks, complete M0 research appendix.
3. [Chat and decision history](docs/CHAT_AND_DECISION_LOG_2026-11-16.md) — chronology and superseded historical alternatives.
4. [Original master prompt (verbatim)](docs/archive/ORIGINAL_BROWSER_MASTER_PROMPT_2026-11.md) — 540-line original project requirements.
5. [Historical November 12 launch plan PDF text](docs/archive/HISTORICAL_LAUNCH_PLAN_2026-11-12_TEXT.md) — older WebView2 prototype alternative; not the current required foundation.
6. [All 18 study repositories](REPOSITORIES_TO_STUDY.txt) and [existing development backlog](docs/BACKLOG.md).
7. [Decision log](docs/DECISIONS.md), [feature matrix](docs/FEATURE_MATRIX.md) and [roadmap](docs/ROADMAP.md).
8. [M0 engineering PR #1](https://github.com/kawaho3/browser-company/pull/1) — **open/unmerged at this snapshot**; check GitHub live status before doing anything.

The master document also has a Word-compatible `.docx` counterpart at `docs/PROJECT_MASTER_HANDOFF_2026-11-16.docx`, for offline reading and archiving.

## Live verification checklist — do first in every session

- Fetch current `main`, open PRs/issues and branch heads; old status may be stale.
- Verify what exists in source and tests instead of treating documentation as implementation.
- Confirm `docs/DECISIONS.md` explicitly accepts a specific upstream **stable commit/tag**, security ownership, licensing/contributor terms and approved Windows build budget **before** any full native source download or build.
- Avoid unnecessary dependencies: Brave Core already manages Chromium and adblock integration. Do not merge whole browser engines.
- Keep work to the smallest testable authorized task; document exact commands, results, costs, files changed and PR URL.
- Add a durable dated note to [the continuity log](docs/CHAT_AND_DECISION_LOG_2026-11-16.md) at the end of the session.

## No approvals implied by this document

It does not authorize heavy native compilation, paid infrastructure, key creation, public releases or production AI. It does not mean Brave Core is already chosen, buildable, legally cleared, fully secure or running in our repository.

## Ready-to-use new-chat instruction

> Open https://github.com/kawaho3/browser-company. Read START_HERE_NEXT_SESSION.md and AGENTS.md first, then the master project handoff, all 18 repository references, and chat/decision log. Inspect main/open PRs live. Recommend the smallest allowed next task and implement it safely on a branch; do not download/build full Brave or Chromium, spend money, or publish software until approved. Preserve status, tests, links and a handoff in GitHub before finishing.
