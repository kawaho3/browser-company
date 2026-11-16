# Browser Company — MASTER PROJECT RESEARCH & DEVELOPER HANDOFF

**Snapshot date:** 2026-11-16 (India time)  
**Public repository:** https://github.com/kawaho3/browser-company  
**Target:** Windows desktop x64, native independently branded Chromium-compatible browser  
**Document status:** Consolidated research and handoff; not a signed-off technical ADR, production build or legal opinion.  
**Primary recommendation:** **Brave Core (provisional)**, not a separate second Chromium checkout.  
**Read first in a new chat:** [START_HERE_NEXT_SESSION.md](../START_HERE_NEXT_SESSION.md), [AGENTS.md](../AGENTS.md), [CHAT_AND_DECISION_LOG](CHAT_AND_DECISION_LOG_2026-11-16.md), then current GitHub PRs/issues.

## 1. Executive summary for any new developer/ChatGPT session

Our mission is to build an installable, maintainable real web browser that can eventually compete with Chrome. Reuse mature, compatible OSS instead of spending Codex credits reproducing established browser components. The user is the project maintainer and wants to work mainly with GPT-6 Astra/Codex, favoring low incremental software spending and transparent build/security costs.

**Current product implementation reality:** the latest verified main branch in the starting audit is documentation-only (21 tracked files, no browser core, runnable native desktop app, installer, AI assistant, Windows native CI or test binary). A separate M0 research pull request exists; it has not been merged at the point of archival.

**What we decided technically:** inspect exactly two *main foundations* — Brave Core and Chromium — rather than merging several full engines. The latest analysis scored Brave Core **80.4/100** and Chromium **74.4/100** under our qualitative weights and **recommended Brave Core**. This is only a **proposed** ADR. The owner must explicitly approve the stable revision, licensing policy, hardware/cost ceiling, and security owner before `pnpm init`, `gclient sync`, full checkout, native compilation, cloud purchase or release.

**Main open PR:** https://github.com/kawaho3/browser-company/pull/1  
Branch: `research/m0-foundation-audit-20261116`  
Includes source-backed M0 audit, feature matrix pointers, license metadata for 18 repos, offline Python reference validator, six unit tests and small pull-request-only CI. Earlier reported GitHub Actions runs passed. It **does not build a browser**.

**This archival work:** preserves the original 540-line user master prompt verbatim, earlier 7-page launch-plan text, chronologically reconstructed conversation/decision log, master research and Word version. This archive should not be mistaken for an export of absolutely every private chat turn.

## 2. Immutable user constraints / product requirements

- Actual independently branded native browser; **not Electron web wrapper, fake UI, disposable prototype or new rendering engine**.
- Windows desktop x64 first; no premature macOS/Linux/mobile promises.
- Exactly one primary foundation. Brave Core already uses and manages Chromium; don't merge duplicated Chromium source tree.
- No massive checkout/native build before the maintainer explicitly approves foundation and resources; no paid API, costly CI, cloud provisioning, model download, telemetry, signing keys, binaries or sensitive remote AI without permission.
- Inspect upstream first: avoid duplicated adblocking, password managers, rendering/network stacks, permissions, crypto and sandbox layers.
- Product-owned original brand, identity, UI, optional productivity research workspaces and later user-authorized AI. Don't copy Brave/Google trademarks, proprietary assets, services or credentials.
- Browser handles sensitive content: no browsing data/passwords/tokens in logs or AI by default. Treat webpage data as untrusted; consequential automation requires user permission and confirmation.
- Commit to small branches/PRs with honest test/verification evidence. Do not merge unreviewed PRs or bypass rules; do not overwrite existing work.
- Keep costs controlled and source/decision provenance clear. A public repo is not automatically a license for all its contents.

## 3. Current repository and GitHub status (checked 2026-11-16)

| Item | Verified observation |
| --- | --- |
| Main repository | https://github.com/kawaho3/browser-company |
| Default branch | `main` |
| Main starting commit | `dc6ae368307aad992a436d6812ac196e42be91c8` |
| Main tracked files | 21 |
| Main branch browser source | Absent |
| Main native Windows compilation | Absent |
| Signed installer and updater | Absent |
| Product AI integration | Absent |
| Open native implementation | No |
| M0 research PR | PR #1, still open/unmerged at archival check |
| Approved foundation ADR | Not yet |
| Third-party license SBOM | Not completed |
| Approved release/signing infrastructure | Not established |

Main tree is made of `.github/ISSUE_TEMPLATE` files, `.github/PULL_REQUEST_TEMPLATE.md`, `.gitignore`, `AGENTS.md`, `CONTRIBUTING.md`, `README.md`, `REPOSITORIES_TO_STUDY.txt`, `SECURITY.md`, and the existing `docs/` handbook. **Source documents and a passing Python validator are not a compiled browser.**

### File and responsibility index

| File or directory | Purpose | Current status |
| --- | --- | --- |
| `AGENTS.md` | Agent policy and expensive-build/approval gates | Active and binding |
| `README.md` | Product and repo entrance | Documentation |
| `CONTRIBUTING.md`, `SECURITY.md` | Contribution/security reporting policy | Draft operating process |
| `REPOSITORIES_TO_STUDY.txt` | Exactly 18 study repositories | Existing index, not installed deps |
| `docs/VISION.md` | Mission, differentiated workflows and metrics | Product proposal |
| `docs/ARCHITECTURE.md` | Engine/UI/profile/AI/trust boundaries | Provisional design |
| `docs/DECISIONS.md` | ADR-001 through ADR-006 | ADR-002 remains proposed |
| `docs/FEATURE_MATRIX.md` | P0 to P4 parity evidence | Not-built feature matrix |
| `docs/ROADMAP.md`, `docs/BACKLOG.md` | M0–M5, BC-001 onward | Evidence-gated plan |
| `docs/BUILD_AND_COST.md` | Cloud/native build concerns | Planned, not benchmarked |
| `docs/REUSE_CATALOG.md` | Reuse rationale | Candidate dependencies only |
| `docs/SECURITY_AND_PRIVACY.md` | Security and responsible AI controls | Design policies |
| `docs/LEGAL_AND_BRANDING.md` | Ownership, notices, company license | Maintainer/legal decisions pending |
| `docs/ONBOARDING.md` | Starting instructions for contributors | Documentation phase |
| `.github/` templates | Reviewable issue/PR process | Templates only |
| `docs/M0_FOUNDATION_AUDIT_2026-11-16.md` | Deep code-path evidence | In PR #1, **not main** |
| `scripts/validate_references.py`, `tests/test_validate_references.py` | Offline structure checks | In PR #1 only |
| `.github/workflows/m0-validation.yml` | Cheap PR validation | In PR #1 only |

### What is missing

A stable approved Brave tag/commit; usable Windows x64 toolchain and checkout; reproducible GN/Ninja native binary; independent product identifiers/assets; testing of browser parity; secure updater and signed installer; privacy declarations; update SLA and owner; test profiles; independent optional cloud services; source/SBOM/notice inventory; user interviews and performance measurements.

## 4. Foundation decision — exactly two primary repositories

| Dimension | Brave Core | Direct Chromium |
| --- | --- | --- |
| Repo | https://github.com/brave/brave-core | https://github.com/chromium/chromium |
| Runtime | Chromium (Blink/V8) managed inside Brave's dependency strategy | Chromium (Blink/V8) directly |
| Native language/toolchain | Mainly C++ / Rust components, GN + Chromium native toolchain | Mainly C++ / Rust, GN + native toolchain |
| Extension/bookmark/profile foundations | Inherited Chromium with Brave product adaptations | Browser architecture included |
| Privacy / adblocking | Existing Shields/adblock integration | More product-level integration needed |
| Vertical tabs / split view | Verified source paths already exist | Browser tab infrastructure; product customization requires work |
| Independent services/branding | More Brave-specific coupling to audit | Cleaner departure point |
| Security updates | Must track Brave and its Chromium rev/patched tree | Tracks Chromium more directly |
| Core license metadata | Brave Core MPL-2.0 plus independently licensed dependencies | Chromium largely BSD-3-Clause plus third-party licenses |
| Native build expense | Heavy, unmeasured | Heavy, unmeasured |
| Recommendation | **Provisional winner** | Contingency if Brave decoupling/licensing becomes too costly |

### Weighted research scorecard (subjective, not measured)

| Criterion | Weight | Brave (1–5) | Chromium (1–5) |
| --- | ---: | ---: | ---: |
| Web compatibility / core browser | 18% | 5 | 5 |
| Productivity capability reuse | 20% | 5 | 4 |
| Privacy integration reuse | 14% | 5 | 2 |
| Windows build feasibility | 10% | 3 | 3 |
| Independent branding/services | 10% | 2 | 4 |
| Upstream security maintenance | 10% | 3 | 4 |
| Licensing/integration maintenance | 10% | 3 | 4 |
| Effort to initial differentiated alpha | 8% | 4 | 3 |
| **Weighted final** | **100%** | **402/500 = 80.4%** | **372/500 = 74.4%** |

`Brave Core  [################----] 80.4 / 100`  
`Chromium    [###############-----] 74.4 / 100`

**Final technical recommendation as of this research:** **Brave Core alone.** **Final maintainer sign-off is pending**. The exact source snapshot used for remote inspection is NOT the required stable release pin for M1.

### Upstream evidence snapshots (not approved release pins)

- Brave Core inspected master SHA: `4d10ac1f2a4690548ccf5430ca02e72c851bfe74`  
  https://github.com/brave/brave-core/tree/4d10ac1f2a4690548ccf5430ca02e72c851bfe74
- Chromium inspected GitHub mirror main SHA: `4773b76908fb09108dbca92c6e9045c0e5b49342`  
  https://github.com/chromium/chromium/tree/4773b76908fb09108dbca92c6e9045c0e5b49342
- Chromium official source and documentation: https://chromium.googlesource.com/chromium/src
- Windows official build documentation: https://chromium.googlesource.com/chromium/src/+/main/docs/windows_build_instructions.md
- Brave Windows contributor information: https://github.com/brave/brave-browser/wiki/Windows-Development-Environment
- Upstream Brave manifest/build command evidence: `brave-core/package.json`, `DEPS`, `patches/`, `browser/`, `components/`.

### Verified candidate code paths for feature reuse

| Feature | Brave Core or Chromium source location |
| --- | --- |
| Brave vertical tabs and tab models | https://github.com/brave/brave-core/tree/4d10ac1f2a4690548ccf5430ca02e72c851bfe74/browser/ui/tabs |
| Brave split view | https://github.com/brave/brave-core/tree/4d10ac1f2a4690548ccf5430ca02e72c851bfe74/browser/ui/split_view |
| Brave speedreader | https://github.com/brave/brave-core/tree/4d10ac1f2a4690548ccf5430ca02e72c851bfe74/browser/ui/speedreader |
| Brave extension modifications | https://github.com/brave/brave-core/tree/4d10ac1f2a4690548ccf5430ca02e72c851bfe74/browser/extensions |
| Brave download integration | https://github.com/brave/brave-core/tree/4d10ac1f2a4690548ccf5430ca02e72c851bfe74/browser/download |
| Shields and tracking | https://github.com/brave/brave-core/tree/4d10ac1f2a4690548ccf5430ca02e72c851bfe74/components/brave_shields |
| Brave identity/installer/updater sources | `brave-core/app/`, `installer/`, `updater/`, `resources/` |
| Chromium browser tabs/navigation/windows | https://github.com/chromium/chromium/tree/4773b76908fb09108dbca92c6e9045c0e5b49342/chrome/browser/ui |
| Chromium profiles/private mode | https://github.com/chromium/chromium/tree/4773b76908fb09108dbca92c6e9045c0e5b49342/chrome/browser/profiles |
| Chromium extensions | https://github.com/chromium/chromium/tree/4773b76908fb09108dbca92c6e9045c0e5b49342/chrome/browser/extensions |
| Chromium bookmarks/downloads/history | `chrome/browser/bookmarks/`, `chrome/browser/download/`, `components/history/` |
| Chromium permissions/passwords | `components/permissions/`, `components/content_settings/`, `components/password_manager/` |
| Chromium networking/sandbox | `services/network/`, `sandbox/` |
| Chromium DevTools/a11y/PDF/print | `chrome/browser/devtools/`, `ui/accessibility/`, `pdf/`, `chrome/browser/printing/` |

**Do not confuse a verified source directory with tested end-user behavior in our fork.** Future maintainers must inspect exact source code and build results for the approved commit.

## 5. All 18 reference repositories, with intended integration outcome

| # | Repository and URL | Primary classification | Current disposition |
| --- | --- | --- | --- |
| 01 | Chromium — https://github.com/chromium/chromium | Alternative browser foundation | Compare only if using Brave |
| 02 | Brave Core — https://github.com/brave/brave-core | Proposed primary foundation | License/branding/build gate first |
| 03 | Zen — https://github.com/zen-browser/desktop | Firefox-based UI reference | Ideas only, no engine merge |
| 04 | Ungoogled Chromium — https://github.com/ungoogled-software/ungoogled-chromium | Chromium privacy patch reference | Study patches, beware drift |
| 05 | Firefox — https://github.com/mozilla-firefox/firefox | Independent browser benchmark | Gecko incompatible with Chromium fusion |
| 06 | Ladybird — https://github.com/LadybirdBrowser/ladybird | Independent engine research | Not short path to Chrome parity |
| 07 | Min — https://github.com/minbrowser/min | Small Electron UX reference | Not production native base |
| 08 | adblock-rust — https://github.com/brave/adblock-rust | Existing Brave-managed engine | Do **not** add second copy |
| 09 | Readability — https://github.com/mozilla/readability | Optional reader feature | Audit Speedreader first |
| 10 | llama.cpp — https://github.com/ggml-org/llama.cpp | Future local AI runtime | Defer models/hardware costs |
| 11 | whisper.cpp — https://github.com/ggml-org/whisper.cpp | Future local transcription | Defer |
| 12 | Browser Use — https://github.com/browser-use/browser-use | AI automation research | Security/permission patterns only |
| 13 | Stagehand — https://github.com/browserbase/stagehand | Alternative AI framework | Compare instead of auto-including |
| 14 | Playwright — https://github.com/microsoft/playwright | Browser E2E testing | Test custom binary after M1 |
| 15 | WPT — https://github.com/web-platform-tests/wpt | Web standard test suite | Targeted subsets later |
| 16 | Fluent UI — https://github.com/microsoft/fluentui | Optional React/web controls | Not a Chromium Views substitute |
| 17 | electron-builder — https://github.com/electron-userland/electron-builder | Electron packaging | Not native Chromium fork installer |
| 18 | Sparkle — https://github.com/sparkle-project/Sparkle | Optional macOS updater | Not Windows; defer |

The reference list is a research index and **not** a dependency manifest, install checklist, license approval or statement of current compatibility. Check precise version, license files, patents/trademarks, active advisories and transitive dependencies before adoption.

## 6. Proposed production architecture

```text
 Windows x64 application (original identity + signed installer/update)
     |
     +-- Native browser UI (menus, tabs, omnibox, settings, a11y)
     |      +-- Workspaces/vertical tabs/split view (reuse upstream first)
     |
     +-- Browser processes, profiles, permissions, extensions
     |      +-- Bookmarks/history/downloads/passwords/sessions
     |
     +-- SINGLE UPSTREAM: Brave Core + Brave-managed Chromium
     |      +-- Chromium content, network, Blink/V8, sandbox, site isolation
     |      +-- Existing Brave privacy/Shield components, audited services
     |
     +-- Product-specific patch/overlay layer (small, pinned, reviewable)
     |
     +-- Optional permissioned local AI adapter (AFTER core browser works)
     |
     +-- Release signing, secure updater and incident response
```

Proposed *future* product-tree (NOT currently implemented): `product/branding`, `product/ui`, `product/features/workspaces`, `product/services`, `patches/product`, `tools`, `tests/smoke/windows`, `docs/builds`. No separate second copy of Chromium is needed when using Brave Core. Keep the patch delta small and rebasable so critical Chromium security updates remain timely.

## 7. Feature backlog by priority

| Priority | Scope | Acceptance conditions |
| --- | --- | --- |
| P0 browser | Real navigation, tabs/windows, omnibox/search, bookmarks/history/downloads, multi-profiles/private mode, passwords/cookies/permissions, extensions, devtools, accessibility, TLS/sandbox and security updates | Actual installed Windows build; repeatable user-journey smoke tests |
| P1 identity | Original legally cleared name, logo/icons, native UI, settings, new tab, independent provider config/privacy disclosures | No competitor asset/secret dependence; working settings, accessible UI |
| P2 productivity | Vertical tabs, tab search, persistent workspaces, split view, session restoration, shortcuts | Persistence, focus/keyboard/a11y and regression tests |
| P3 privacy/performance | Verified upstream privacy controls, no duplicate blocker, startup/RAM/CPU/battery benchmarks, compatibility suite | Test measurements and timely patch workflow |
| P4 optional AI | Selected-page summarization, cross-tab research, notes, comparisons, reports, optional local inference, permissioned automation | Explicit consent, untrusted page-data isolation, confirmation/stop controls |

## 8. Milestones and exact approval sequence

| Milestone | Next work | Exit gate |
| --- | --- | --- |
| **M0** | BC-001 Brave audit; 002 Chromium comparison; 003 license strategy; 004 parity; 005 Windows feasibility; 006 security/update; 007 user interviews; 008 ADR | Approved single foundation, stable commit, contributor license, machine/budget, security owner |
| **M1** | Unmodified approved Brave upstream clone/build/run and resource logging; browser smoke tests | Native Windows executable, measured reproducible build and tab/profile/download/extension results |
| **M2** | Company brand/resources/service endpoint changes with minimal fork patching | Independently named installed alpha that passes P0 checks |
| **M3** | User-validated workspaces/vertical tabs/split view and migration | Task usability, persistence, compatibility, a11y and performance evidence |
| **M4** | Optional local/remote AI after permission and threat model | Consent, injection protection, no secret exfiltration, review/stop |
| **M5** | Secure signed installer/update/releases, notices, support, privacy policy, broader QA | Sustainable security patches and controlled public release |

M0 package progress: BC-001 and 002 source research done; 003 and 004 partially documented; 005 planned but not measured; 006 strategy drafted but not staffed; 007 interviews not done; 008 recommended Brave Core but **unapproved**. M1–M5 not started.

## 9. Build, cost, credit and infrastructure planning

| Dimension | Planning target / minimum evidence | Measured result |
| --- | --- | --- |
| Operating system | Windows desktop x64, release-specific SDK/Visual Studio requirements | Not measured |
| CPU | Proposed 12–24 logical threads for practical builder | Not measured |
| RAM | Proposed 32–64 GB practical build machine | Not measured |
| SSD | Proposed 200–300 GB free; Chromium Windows public docs call for at least 100 GB | Not measured |
| Source size | Multi-gigabyte checkout and dependencies; exact pinned revision unknown | No source downloaded |
| Clean build duration | To be measured with approved native toolchain | Not measured |
| Cloud instance/CI | Hourly compute + disk + networking + CI + security maintenance | No expensive runner provisioned |
| Software subscriptions | Use existing credits where possible; no unapproved API fees | No new paid service for M0 |
| Release/signing/support | Future non-zero production operations; need quotes | Not configured |

**Cost-control ladder:** public remote research -> offline static checks -> unit tests -> bounded component smoke -> explicit approval -> large checkout -> native build -> test -> branded release signing/distribution. Avoid accidental GitHub Actions heavyweight jobs, uncontrolled artifacts, untrusted PR secrets, surprise cloud bills and redundant source downloads.

The old PDF's `₹0` prototype assumption and ~1–3 week timeline referred to **WebView2**, not a production full native Brave-based browser. Do not claim a Chrome competitor can ship for free in that time.

## 10. Security, compliance and maintenance blockers

| Threat / concern | Required control |
| --- | --- |
| Malicious webpages / renderer compromise | Track patched Chromium; retain sandbox, site isolation and TLS validation |
| Extension privilege creep | Review permission prompts, install/update behavior, least privilege and MV3 cases |
| Passwords, cookies and profiles | OS-backed secure storage; no secret logs; deletion and private-session tests |
| Hostile downloads | Confirm/cancel UX, permissions, OS/reputation checks where permitted |
| Browser update supply chain | Company-controlled signed binaries/metadata, protected keys, staged update/rollback |
| Upstream vulnerability lag | Assigned maintainers and release cadence; rebasable downstream patch stack |
| Third-party licenses/trademarks | MPL-2.0 covered-file duties, Chromium mixed licenses, SBOM/notices/source offers; no copied marks |
| Google/Brave service dependencies | Audit and replace/remove provider keys, Sync, DRM, VPN/rewards/cloud services as necessary |
| Optional AI prompt injection | Page text treated as *data*, not executable instructions; permission scope and action confirmation |
| Privacy/telemetry | No surprise transmission; review actual binary and disclosure policy before release |

**Outstanding owner approvals:** 1) provisional Brave/Core ADR and stable tag; 2) root project and contributor license strategy; 3) Windows machine budget and permitted checkout/build; 4) security/release owners; 5) original product branding; 6) user research and representative target sites. Do not claim these are resolved.

## 11. Engineering evidence, tests and exact state at this handoff

Prior M0 PR #1 reports offline validator plus 6 unit tests and successful bounded PR CI. The last visible run in that session was: https://github.com/kawaho3/browser-company/actions/runs/43750092066 (success). No full Chromium/Brave native build, Windows install, extension test, password security test, package signing, performance benchmark or product AI deployment has been performed in this project record.

Source audit baseline: [M0 foundation PR #1](https://github.com/kawaho3/browser-company/pull/1) with [full audit](https://github.com/kawaho3/browser-company/blob/research/m0-foundation-audit-20261116/docs/M0_FOUNDATION_AUDIT_2026-11-16.md). Until merged, the contents exist on its branch and must not be claimed to exist on `main`.

## 12. Session continuation protocol (do not rely on long ChatGPT context)

1. Open https://github.com/kawaho3/browser-company and read `START_HERE_NEXT_SESSION.md`, `AGENTS.md`, this master handoff and the conversation decision log.
2. Inspect current `main` and every relevant PR/branch/CI status; archival status is dated.
3. Check `docs/DECISIONS.md` before deciding a foundation; a user asking which to choose is **not** automatically written permission to download/build.
4. Consult `REPOSITORIES_TO_STUDY.txt`, current M0 audit and exact upstream revisions before writing code.
5. Choose the smallest safe task matching `docs/BACKLOG.md`, explain acceptance, implementation, tests, security, licensing and costs, and do it on a review branch.
6. Before finishing, append date, head SHA, PR URL, actual commands/results, costs, blockers, and next task to `docs/CHAT_AND_DECISION_LOG_2026-11-16.md` (or a successor dated log). Commit durable developer setup and evidence; do not rely on remembered chat.
7. Never overwrite this primary-source record when later decisions change; create an ADR/history entry and explicitly mark older guidance superseded.

### Copy/paste starter for a new Codex or ChatGPT session

> Continue the native browser project at https://github.com/kawaho3/browser-company. Inspect current main and open PRs. Read AGENTS.md, START_HERE_NEXT_SESSION.md, docs/PROJECT_MASTER_HANDOFF_2026-11-16.md, docs/CHAT_AND_DECISION_LOG_2026-11-16.md, docs/DECISIONS.md and REPOSITORIES_TO_STUDY.txt. The project is documentation/M0 stage; no native browser compiled. Brave Core alone is the recommended but *not yet approved* foundation (80.4 vs Chromium 74.4 subjective score). PR #1 holds the M0 audit and cheap tests. Check its merge/CI state. Respect AGENTS.md gates: no large checkout/build, paid infrastructure, binaries or external AI without explicit approval. Preserve exact files changed/tests/links in a dated GitHub handoff and open a reviewable PR for the smallest authorized task.

## 13. Complete research and chat-source index

| Source | Link / location |
| --- | --- |
| Master prompt, archived verbatim | [docs/archive/ORIGINAL_BROWSER_MASTER_PROMPT_2026-11.md](archive/ORIGINAL_BROWSER_MASTER_PROMPT_2026-11.md) |
| Historical earlier WebView2 PDF text | [docs/archive/HISTORICAL_LAUNCH_PLAN_2026-11-12_TEXT.md](archive/HISTORICAL_LAUNCH_PLAN_2026-11-12_TEXT.md) |
| Reconstructed chat/decision timeline | [docs/CHAT_AND_DECISION_LOG_2026-11-16.md](CHAT_AND_DECISION_LOG_2026-11-16.md) |
| Current project handbook | [README](../README.md), [AGENTS](../AGENTS.md), [VISION](VISION.md), [ARCHITECTURE](ARCHITECTURE.md), [DECISIONS](DECISIONS.md) |
| Feature, implementation and cost | [FEATURE_MATRIX](FEATURE_MATRIX.md), [ROADMAP](ROADMAP.md), [BACKLOG](BACKLOG.md), [BUILD_AND_COST](BUILD_AND_COST.md), [REUSE_CATALOG](REUSE_CATALOG.md) |
| Security and legal | [SECURITY_AND_PRIVACY](SECURITY_AND_PRIVACY.md), [LEGAL_AND_BRANDING](LEGAL_AND_BRANDING.md), [SECURITY.md](../SECURITY.md) |
| Developer workflow | [ONBOARDING](ONBOARDING.md), [CONTRIBUTING](../CONTRIBUTING.md) |
| 18 publicly available repositories | [REPOSITORIES_TO_STUDY.txt](../REPOSITORIES_TO_STUDY.txt) |
| Current M0 PR / tested research | https://github.com/kawaho3/browser-company/pull/1 |
| Brave Core / Chromium | https://github.com/brave/brave-core and https://chromium.googlesource.com/chromium/src |

## Appendix A — Detailed source-backed M0 research record

This appendix reproduces the separate PR #1 engineering audit so the master archive remains useful even when a future conversation cannot load the earlier thread. The original PR is authoritative for its own commit/test history. Duplicated historical content below remains subject to the same **proposed/unapproved** qualifications.

---


**Status: proposal for maintainer review; NOT an approved foundation selection or build result.** Target: Windows desktop x64. Research snapshots below are immutable source commit IDs, not selected release pins. No native code was checked out, built or exercised during this audit.

## Scope, evidence and reproducibility

- Project main at audit start: [dc6ae368307a](https://github.com/kawaho3/browser-company/commit/dc6ae368307aad992a436d6812ac196e42be91c8) (21 tracked files; documentation only; no native build/workflows).
- Brave Core master snapshot: [4d10ac1f2a46](https://github.com/brave/brave-core/tree/4d10ac1f2a4690548ccf5430ca02e72c851bfe74); upstream package.json reports version 1.102.8 at research time. Not a stability or release endorsement.
- Chromium GitHub mirror main snapshot: [4773b76908fb](https://github.com/chromium/chromium/tree/4773b76908fb09108dbca92c6e9045c0e5b49342). Chromium's source of record and documentation are at [chromium.googlesource.com](https://chromium.googlesource.com/chromium/src).
- Source reviewed remotely through the GitHub repository API, README, dependency manifests, and official Windows build documentation. No executable tests or audits of transitive license files. Paths listed below existed on these branches during remote inspection; functionality is *not* validated in our product.

## Existing repository code structure (BC-001 prerequisite)

| File/module | Existing status | Purpose | Missing work | Action |
| --- | --- | --- | --- | --- |
| README.md, AGENTS.md | Documentation only | Mission and agent rules | Implementation proof | Preserve accuracy and approval gates |
| CONTRIBUTING.md, SECURITY.md | Documentation only | Contributor and disclosure process | Approved license, response contact | Maintainer review |
| REPOSITORIES_TO_STUDY.txt | 18 recorded candidates | Reuse research index | Automated integrity check and SPDX review | Validate list offline; audit exact versions |
| .github/ISSUE_TEMPLATE/*.md, .github/PULL_REQUEST_TEMPLATE.md | Templates only | Review workflow | Automated validation | Add bounded CI checks |
| .gitignore | Present | Local exclusions | Native build exclusions later | Defer until foundation selected |
| docs/VISION.md | Proposal | Product requirements | User evidence | BC-007 interviews |
| docs/ARCHITECTURE.md | Proposal | Responsibility boundaries | Concrete selected-upstream interfaces | Revise after M1 |
| docs/DECISIONS.md | Open ADR-002 | Decision gate | Maintainer approval, pinned stable revision | Add proposal link; do not mark accepted |
| docs/FEATURE_MATRIX.md | Not-built matrix | Parity requirements | Verified target binaries/tests | Link upstream source paths and smoke checks |
| docs/ROADMAP.md, docs/BACKLOG.md | Planning checklists | Staged deliverables | Measured proof | Track research as partial |
| docs/BUILD_AND_COST.md | Planning estimates | Resource guardrails | Real Windows machine measurements | Obtain approval before checkout |
| docs/REUSE_CATALOG.md | Candidate list | Avoid duplicate work | Exact third-party licensing | Review per integration |
| docs/SECURITY_AND_PRIVACY.md, docs/LEGAL_AND_BRANDING.md | Policies/drafts | Trust, licensing, brand | Operational owner, notices, agreements | Pre-release gates |
| docs/ONBOARDING.md | Documentation | Developer handoff | Native build guide | Post-approval M1 |
| src/, product/, tests/, native build configuration | Absent at audit start | Future browser/product implementation | Entire integration and verification | No full engine implementation until approval |

Problems: there are no reproducible native commands, version-pinned dependencies, installer, Windows runner, signing identities, security-release SLA, binary artifacts or active browser tests. Do not label documented features implemented. The root project license is intentionally undecided; do not assume public-source rights for project contributions.

## Candidate A: Brave Core (BC-001)

Brave Core is a Chromium customization layer, **not a second independent renderer**. Its [README](https://github.com/brave/brave-core/blob/4d10ac1f2a4690548ccf5430ca02e72c851bfe74/README.md), [package.json](https://github.com/brave/brave-core/blob/4d10ac1f2a4690548ccf5430ca02e72c851bfe74/package.json), [DEPS](https://github.com/brave/brave-core/blob/4d10ac1f2a4690548ccf5430ca02e72c851bfe74/DEPS), and [patches](https://github.com/brave/brave-core/tree/4d10ac1f2a4690548ccf5430ca02e72c851bfe74/patches) show an upstream Chromium checkout managed with depot_tools/gclient and Brave's patch stack. The README places brave-core at src/brave. Brave depends on adblock-rust through an FFI integration; do not vendor it twice.

Verified code entry points (relative to Brave Core repository, before checkout into src/brave):
- [browser/ui/tabs](https://github.com/brave/brave-core/tree/4d10ac1f2a4690548ccf5430ca02e72c851bfe74/browser/ui/tabs): vertical_tab_controller.cc, tree_tab_model.cc, tree_tab_session_manager.cc, tab prefs.
- [browser/ui/split_view](https://github.com/brave/brave-core/tree/4d10ac1f2a4690548ccf5430ca02e72c851bfe74/browser/ui/split_view): split navigation and feature controls.
- [browser/ui/speedreader](https://github.com/brave/brave-core/tree/4d10ac1f2a4690548ccf5430ca02e72c851bfe74/browser/ui/speedreader): Speedreader user interface/helper.
- [browser/extensions](https://github.com/brave/brave-core/tree/4d10ac1f2a4690548ccf5430ca02e72c851bfe74/browser/extensions), [browser/download](https://github.com/brave/brave-core/tree/4d10ac1f2a4690548ccf5430ca02e72c851bfe74/browser/download): extension/download adaptations and tests.
- [components/brave_shields](https://github.com/brave/brave-core/tree/4d10ac1f2a4690548ccf5430ca02e72c851bfe74/components/brave_shields), [components/brave_adblock_ui](https://github.com/brave/brave-core/tree/4d10ac1f2a4690548ccf5430ca02e72c851bfe74/components/brave_adblock_ui): existing protection/UI.
- [app](https://github.com/brave/brave-core/tree/4d10ac1f2a4690548ccf5430ca02e72c851bfe74/app), [resources](https://github.com/brave/brave-core/tree/4d10ac1f2a4690548ccf5430ca02e72c851bfe74/resources), [installer](https://github.com/brave/brave-core/tree/4d10ac1f2a4690548ccf5430ca02e72c851bfe74/installer), [updater](https://github.com/brave/brave-core/tree/4d10ac1f2a4690548ccf5430ca02e72c851bfe74/updater): product identity, resources, install and update-related code. Presence of updater code does NOT supply our update service or signing.
- [components/ai_chat](https://github.com/brave/brave-core/tree/4d10ac1f2a4690548ccf5430ca02e72c851bfe74/components/ai_chat): research only; not our own licensed service or ready-made assistant.

Brave advantages: extensive Chromium-based functionality, mature tabs/split/privacy code, established patch/build scripts. Risks: significant Brave-specific service and UI coupling, MPL-2.0 covered-file obligations, rebranding/attribution audit, complex Chrome patch rebase, third-party licensing and security updates. Services for rewards, VPN, search, sync, wallet, proprietary endpoints, etc. must be individually assessed; deletion must not break unrelated functionality. Existing Brave tests and released browser are not proof that our fork has passed them.

## Candidate B: direct Chromium (BC-002)

[Chromium](https://chromium.googlesource.com/chromium/src) provides Blink/V8 via the multi-process browser architecture and renderer, network service, sandbox, persistent profiles, Chrome-style browser UI and extensions. Relevant source entry points at the GitHub mirror snapshot:
- [content/browser](https://github.com/chromium/chromium/tree/4773b76908fb09108dbca92c6e9045c0e5b49342/content/browser) and [content/renderer](https://github.com/chromium/chromium/tree/4773b76908fb09108dbca92c6e9045c0e5b49342/content/renderer) — browser/renderer boundary.
- [chrome/browser/ui](https://github.com/chromium/chromium/tree/4773b76908fb09108dbca92c6e9045c0e5b49342/chrome/browser/ui) — native browser windows, tabs, omnibox/views.
- [chrome/browser/profiles](https://github.com/chromium/chromium/tree/4773b76908fb09108dbca92c6e9045c0e5b49342/chrome/browser/profiles) — profiles/incognito policies.
- [chrome/browser/bookmarks](https://github.com/chromium/chromium/tree/4773b76908fb09108dbca92c6e9045c0e5b49342/chrome/browser/bookmarks), [chrome/browser/download](https://github.com/chromium/chromium/tree/4773b76908fb09108dbca92c6e9045c0e5b49342/chrome/browser/download), [chrome/browser/extensions](https://github.com/chromium/chromium/tree/4773b76908fb09108dbca92c6e9045c0e5b49342/chrome/browser/extensions) — everyday browser capabilities.
- [components/password_manager](https://github.com/chromium/chromium/tree/4773b76908fb09108dbca92c6e9045c0e5b49342/components/password_manager), [services/network](https://github.com/chromium/chromium/tree/4773b76908fb09108dbca92c6e9045c0e5b49342/services/network), [sandbox](https://github.com/chromium/chromium/tree/4773b76908fb09108dbca92c6e9045c0e5b49342/sandbox) — credentials, network and process protection.

Advantages: fewer preexisting Brave-specific integrations, cleaner brand/service independence, direct upstream security cadence and broad customization potential. Disadvantages: substantial privacy blocking, native tab/workspace differentiation, release/signing/updates and other integration must be engineered independently. Proprietary Google Sync, proprietary DRM, commercial API keys and platform services are not included by right. Extension compatibility must be tested rather than assumed.

## Weighted foundation decision (BC-008 proposal; maximum 500 points)

Scores 1 (poor) to 5 (excellent); weighted score = weight x score. These are engineering judgements for **our stated privacy/productivity-first, resource-constrained product**; they are not measured benchmarks.

| Criterion | Weight | Brave score | Chromium score | Rationale |
| --- | ---: | ---: | ---: | --- |
| Web compatibility and core features | 18 | 5 | 5 | Same Chromium engine lineage; native core plumbing |
| Productivity capability reuse | 20 | 5 | 4 | Brave paths for vertical tabs, split view, reader; Chromium core tab models |
| Privacy protection reuse | 14 | 5 | 2 | Brave Shields and adblock integration; direct Chromium requires extra product work |
| Windows build feasibility | 10 | 3 | 3 | Both require heavyweight native toolchain and build |
| Independent branding/service decoupling | 10 | 2 | 4 | Brave has substantial product/service-specific integration |
| Upstream security-update maintainability | 10 | 3 | 4 | Extra Brave patch/rebase layer versus direct Chromium |
| License/compliance and dependency maintenance | 10 | 3 | 4 | Brave adds MPL-covered code/indirect deps; Chromium still mixed licenses |
| Time/credit cost to differentiated first alpha | 8 | 4 | 3 | Reusing existing Brave privacy/productivity likely reduces custom implementation |
| **Total / 500** | **100** | **402 (80.4%)** | **372 (74.4%)** | **Provisional; no build measurements** |

**Recommend exactly one foundation for M1 feasibility: Brave Core, subject to written maintainer approval.** This recommendation does not finalize ADR-002. Reconsider direct Chromium if service decoupling requires broad invasive patches, licensing cannot be satisfied, or security-update lag becomes unacceptable. Do not combine two checked-out browser trees.

## All 18 study repositories (BC-003 preliminary inventory)

Metadata is from public GitHub repository metadata inspected 2026-11-16 (most pushed 2026-11-13 to 15; Readability last pushed 2026-08-04, Min 2026-11-08). **License column is GitHub-reported SPDX only**, not file-level distribution clearance. NOASSERTION is not a permissive license. All entries remain uninstalled. These are suitability decisions, not signed integration approvals.

| # | Repository | Language / metadata SPDX | Classification, integration cost and current action |
| --- | --- | --- | --- |
| 01 | [Chromium](https://github.com/chromium/chromium) | C++ ecosystem / BSD-3-Clause | Alternative foundation; huge native dependency/build; compare only |
| 02 | [Brave Core](https://github.com/brave/brave-core) | C++ / MPL-2.0 | **Proposed sole primary**; high fork/build cost; audit service/patch footprint |
| 03 | [Zen Browser](https://github.com/zen-browser/desktop) | C++ and Firefox ecosystem / MPL-2.0 | UI/workspace inspiration; Gecko incompatibility blocks engine merge |
| 04 | [Ungoogled Chromium](https://github.com/ungoogled-software/ungoogled-chromium) | Python + patches / BSD-3-Clause | Privacy patch ideas only; patch drift and service-breakage risk |
| 05 | [Firefox](https://github.com/mozilla-firefox/firefox) | JS/C++/Rust / NOASSERTION | Reference/benchmark; Gecko is incompatible as a direct Chromium module; inspect Mozilla file-level licenses |
| 06 | [Ladybird](https://github.com/LadybirdBrowser/ladybird) | Rust/C++ / BSD-2-Clause | Independent-engine research; not Chrome-extension parity foundation |
| 07 | [Min](https://github.com/minbrowser/min) | JS/Electron / Apache-2.0 | UX/prototype inspiration only; not native release toolchain |
| 08 | [adblock-rust](https://github.com/brave/adblock-rust) | Rust / MPL-2.0 | Already Brave-managed: **do not duplicate**; inspect FFI/license in chosen checkout |
| 09 | [Readability](https://github.com/mozilla/readability) | JavaScript / Apache-2.0 | Optional reading module; upstream Speedreader first, sanitize extracted HTML |
| 10 | [llama.cpp](https://github.com/ggml-org/llama.cpp) | C++ / MIT | Future local inference; models have separate licenses/hardware cost |
| 11 | [whisper.cpp](https://github.com/ggml-org/whisper.cpp) | C++ / MIT | Optional future voice; packaging/model cost and private audio review |
| 12 | [Browser Use](https://github.com/browser-use/browser-use) | Python / MIT | AI automation research; remote model, permission/injection and process-boundary risks |
| 13 | [Stagehand](https://github.com/browserbase/stagehand) | TypeScript / MIT | Alternative AI automation research; no need to integrate both; API/service cost risk |
| 14 | [Playwright](https://github.com/microsoft/playwright) | TypeScript / Apache-2.0 | Preferred bounded E2E dev tool after M1; custom executable support must be tested |
| 15 | [WPT](https://github.com/web-platform-tests/wpt) | HTML/Python/JS / NOASSERTION | Browser standards test source; select subsets, check test-file licenses |
| 16 | [Fluent UI](https://github.com/microsoft/fluentui) | TypeScript / NOASSERTION | Only optional compatible web/React settings surface; NOT a native Views replacement |
| 17 | [electron-builder](https://github.com/electron-userland/electron-builder) | TypeScript / MIT | **Unnecessary/incompatible** for Chromium native distribution |
| 18 | [Sparkle](https://github.com/sparkle-project/Sparkle) | Objective-C/Swift / NOASSERTION | Future optional macOS updater; not Windows; Brave has a managed Sparkle-related dependency |

Before use, inspect exact tag/commit, LICENSE and per-file notices, advisories, dependency manifests, transitive dependencies, maintenance ownership, privacy implications and source-offer obligations. License/security due diligence is **incomplete**. Especially audit the shipped adblock engine, Brave-controlled service integrations and Chromium third_party.

## Windows build gate / costs (BC-005)

Official [Chromium Windows instructions](https://chromium.googlesource.com/chromium/src/+/main/docs/windows_build_instructions.md): Windows 10+, x64; **minimum 8 GB RAM, >16 GB recommended, at least 100 GB free NTFS**, SSD strongly recommended; current instructions mention VS 2026, appropriate SDK/MFC/ATL. The [Brave Windows wiki](https://github.com/brave/brave-browser/wiki/Windows-Development-Environment) provides additional requirements and may describe VS 2022: **toolchain requirements must be confirmed for the approved stable Brave tag**, not mixed from two independent revisions.

Proposed first-builder budget (not measured): 12–24 logical CPU threads, 32–64 GB RAM, >=200–300 GB available SSD, Windows 11 x64, supported Visual Studio/SDK and depot_tools. Source download size, clean build duration, incremental duration and CI costs are **unknown until the approved trial**; do not substitute figures for actual measurements. Estimate future cloud spend as instance hourly price x billed hours + persistent SSD and egress + CI minutes + signing/security operations; zero-cloud-cost M0 checks do not imply a free production browser.

Cost ladder: offline static checks -> isolated unit tests -> bounded component checks -> **approval gate** -> official upstream full checkout and unmodified build -> recorded smoke tests -> identity changes -> signed releases. Use no scheduled heavyweight CI. Obtain explicit maintainer confirmation of foundation, exact release revision, machine/toolchain, spending limit and rollback/caching plan **before** pnpm init, gclient sync or build. Benchmark baseline RAM, disk, CPU and elapsed wall-clock; retain redacted command logs. This audit performed no native build.

## Security, privacy, licensing and releases (BC-006)

- Browser/renderer: inherit Chromium site isolation, sandbox, TLS, network service; require dedicated review before modifying them. Test Windows x64 sandbox and exploit-relevant regression cases.
- Profiles, passwords, cookies: use inherited OS-backed secrets protection; no credential logs. Verify profile isolation, private mode lifecycle and storage deletion.
- Downloads and extensions: permission test cases, safe download UX, extension API version and updater paths. Never claim every Chrome Web Store extension works.
- Updater/signing: our own signing identities and distribution/update service are required. Design signed update metadata, staged rollout, expiry/rollback and key recovery; Brave's updater code alone is not sufficient. No release keys or installers created in M0.
- Vulnerability response: nominate security owner and private contact; track stable upstream security updates; set a **proposed** critical-fix triage target pending maintainer decision, test and produce a patched build. Do not claim an SLA exists.
- AI: page content is untrusted; deny access by default, require consent for selected page input and specific confirmation before writes, payments, submissions or uploads. No default remote AI, telemetry or cross-tab secret collection.
- Trademarks/services: company owns only original work/assets; upstream code retains its licenses. MPL-2.0 covered-source requirements and Chromium/third-party notices need distribution review. Google/Brave service keys, trademarks, Sync and proprietary DRM are not transferable by default.
- Release gate: signed installer, documented notice/source availability, privacy policy, secure updater, security contact, reproducible smoke tests and tested incident response must exist before public distribution.

## Proposed post-approval architecture

Keep a **single** approved Brave-managed Chromium source checkout outside the small planning repository, pinned to a release SHA. Later create minimal product-specific sources and a documented patch/overlay manifest rather than copying or independently maintaining all of Chromium:

~~~
product/
  branding/               # company-owned assets after trademark clearance
  ui/                     # approved UX integration after M1
  features/workspaces/    # first differentiator after baseline validation
  services/               # independent service configuration
patches/product/          # narrowly documented, tested downstream patches
tools/                    # build environment and provenance verification
tests/smoke/windows/      # real installed browser test flows
docs/builds/              # measured builder records and reproducibility
~~~

Respect upstream engine, browser/renderer, profile/storage, extension and release trust boundaries. Source layout is proposed, NOT present or built.

## Dependency-ordered development and acceptance gates

| Order | Backlog | Required output | Status now |
| --- | --- | --- | --- |
| 1 | BC-001 | Brave deps, source map, candidate snapshot and divergence risks | **Research evidence present; no transitive SBOM** |
| 2 | BC-002 | Chromium source-map/cost/service comparison | **Research evidence present; no benchmark** |
| 3 | BC-003 | License inventory, decision on project license and contributors | **Metadata inventory; maintainer/legal decision BLOCKED** |
| 4 | BC-004 | P0 parity map with paths and target tests; then binary evidence | **Source pointers; binary tests BLOCKED** |
| 5 | BC-005 | Windows feasibility + budget; measured build later | **Requirements/planning complete; measurements BLOCKED** |
| 6 | BC-006 | Threats, security updates, release policy owner | **Design proposed; operational ownership BLOCKED** |
| 7 | BC-007 | 5–10 user interviews and prioritized pain points | **NOT DONE — requires actual users** |
| 8 | BC-008 | Single-foundation ADR, exact stable pin, licensing/budget approval | **Brave proposed; maintainer sign-off BLOCKED** |
| 9 | BC-101 | Unmodified native upstream runs on Windows; measured cost | **NOT STARTED — gated** |
| 10 | BC-102 | Navigation, tabs, profiles, download, extension smoke results | **NOT STARTED — depends on BC-101** |
| 11 | BC-103–105 | Original identity, secure release plan, validated UI | **NOT STARTED — post-baseline** |
| 12 | BC-201–205 | Workspaces, split-view, privacy validation, optional AI | **NOT STARTED — staged** |

**Smallest next real native milestone after approval:** pin a stable Brave release; build *unmodified* on dedicated Windows x64 hardware using source-appropriate official instructions; produce a run log, clean resource metrics, launch screenshot, and navigation/tabs/downloads/profiles/extensions smoke results. Abort before product patches if the upstream baseline fails. No M1 gate is implicitly approved by this document.

## Limitations and decision request

Verified: repository layout, list of 18, Github metadata and source directories, Brave package/dependency/patch overview, published Windows prerequisites. Not verified: full license SBOM, exact transitive security vulnerabilities, viable company rebranding, unmodified Windows build, binary behavior, specific stable release pin, operating expenses and code signing. GitHub metadata “recent push” does not establish secure maintenance or compatibility.

**Maintainer decisions required:** approve/refuse the provisional Brave Core selection; choose an exact stable Brave upstream revision; decide company-source and contributor license policy; supply/approve Windows build machine and a cost ceiling; nominate security and release owners. Until then, keep ADR-002 proposed and do not initiate large downloads or builds.

