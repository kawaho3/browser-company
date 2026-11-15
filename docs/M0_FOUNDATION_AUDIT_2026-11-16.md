# M0 foundation audit — 2026-11-16

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
