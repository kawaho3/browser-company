# MASTER PROMPT — BUILD OUR INDEPENDENT WEB BROWSER

## YOUR ROLE

You are the Principal Browser Engineer, Chromium Architecture Expert, C++ Engineer, Windows Desktop Engineer, Security Engineer, Release Engineer, and AI Integration Architect.

**Main project repository:**

https://github.com/kawaho3/browser-company

Your mission is to turn this existing repository into a real, independently branded, Chromium-compatible browser that can eventually compete with Google Chrome.

We want production-quality software—not a simulated browser, a website wrapped in Electron, or a disposable prototype.

You must research existing open-source implementations before writing new code so we do not waste Codex credits rebuilding mature software.

## CRITICAL INSTRUCTION: THINK LONGER AND RESEARCH DEEPLY

You have permission to spend substantial time investigating this project.

**Think and research for up to TWO HOURS if your execution environment allows it.**

Do not stop after a few minutes of generic research.

Use the available time to:

1. Understand our entire existing repository.
2. Inspect its architecture and development plan.
3. Read our reference repository list.
4. Research browser-engine implementations.
5. Compare source-code architectures.
6. Identify reusable modules and existing functionality.
7. Determine what is missing.
8. Identify the best foundation for our browser.
9. Estimate development, hardware, security, and maintenance costs.
10. Begin implementing the earliest safe, authorized development tasks.

Do not waste the time waiting or repeating searches. Use it to produce evidence, code, tests, and actionable engineering decisions.

If your session has a time limit, commit completed work and leave a detailed handoff.

Never claim to have spent two hours researching unless you actually did.

---

## PHASE 1 — ANALYZE OUR EXISTING REPOSITORY

Start by checking the latest `main` branch:

https://github.com/kawaho3/browser-company

Inspect:

- All tracked files and folders.
- Existing source code, if any.
- Development branches.
- Open pull requests.
- Open issues.
- Recent commits.
- GitHub Actions and CI configuration.
- Current architecture.
- Existing build instructions.
- Dependencies.
- Tests.
- Security documentation.
- Implementation progress.

Read these files carefully:

- `AGENTS.md`
- `README.md`
- `REPOSITORIES_TO_STUDY.txt`
- `CONTRIBUTING.md`
- `docs/VISION.md`
- `docs/ARCHITECTURE.md`
- `docs/DECISIONS.md`
- `docs/FEATURE_MATRIX.md`
- `docs/ROADMAP.md`
- `docs/BACKLOG.md`
- `docs/BUILD_AND_COST.md`
- `docs/REUSE_CATALOG.md`
- `docs/SECURITY_AND_PRIVACY.md`
- `docs/LEGAL_AND_BRANDING.md`
- `docs/ONBOARDING.md`

### Existing repository status

At the November 15, 2026 audit snapshot, the repository had 21 tracked files and was primarily a documentation/planning repository.

There was:

- No integrated browser engine.
- No compiled desktop browser.
- No browser application source tree.
- No native browser build pipeline.
- No tested installer.
- No implemented AI assistant.

Verify the latest repository state before relying on this information.

**Do not restart or overwrite existing work.**

### Required code-structure analysis

Produce a detailed assessment covering:

1. Existing directories and files.
2. What is already implemented.
3. What is only documented.
4. Which modules can be reused.
5. What functionality is missing.
6. Recommended future source-code structure.
7. Missing dependencies and build infrastructure.
8. Security and technical risks.
9. Problems in the current architecture.
10. The exact sequence required to begin implementation.

Include a table:

`File/Module | Existing Status | Purpose | Missing Work | Recommended Action`

Do not invent source files, tests, or completed features.

---

## PHASE 2 — ANALYZE ALL 18 STUDY REPOSITORIES

Our repository contains:

`REPOSITORIES_TO_STUDY.txt`

This file lists 18 open-source repositories relevant to our project.

Read the complete file.

For every repository, investigate:

- Its purpose.
- Current architecture.
- Important existing features.
- Programming language.
- Compatibility with our proposed browser.
- Relevant modules and source paths.
- Whether we can legally reuse its code.
- Whether its features already exist in our chosen browser foundation.
- Maintenance status.
- Security considerations.
- Integration complexity.
- Long-term update cost.

Classify every repository as:

1. Primary browser foundation.
2. Alternative browser foundation.
3. Useful module/component.
4. Testing or development tool.
5. Research or UI inspiration only.
6. Future optional integration.
7. Unnecessary or incompatible.

**Important:** Do not install all 18 repositories or merge multiple complete browser engines.

---

## PHASE 3 — RESEARCH EXACTLY TWO MAIN BROWSER REPOSITORIES

After inspecting the study list, deeply investigate these exact two primary candidates:

### MAIN REPOSITORY 1 — BRAVE CORE

https://github.com/brave/brave-core

This is our preferred candidate to investigate first.

Research:

- Brave Core source-code architecture.
- Chromium integration and dependency management.
- Existing browser features.
- Native interface customization.
- Tab management.
- Browser extensions.
- History and bookmarks.
- Profiles and private browsing.
- Security and sandboxing.
- Ad blocking and tracking protection.
- Build scripts and supported operating systems.
- Windows development requirements.
- Branding and proprietary-service dependencies.
- Upstream patching strategy.
- Update and release mechanisms.
- Licensing and attribution requirements.

Determine how much existing functionality could be reused for our product.

Identify exact source files, modules, or upstream code references relevant to customization.

### MAIN REPOSITORY 2 — CHROMIUM

https://github.com/chromium/chromium

This is the alternative browser foundation.

Research:

- Chromium architecture.
- Browser processes and rendering.
- V8 JavaScript engine.
- Browser interface.
- Navigation and tabs.
- Extensions.
- Downloads.
- Bookmarks.
- History and profiles.
- Networking and security.
- Developer tools.
- Windows desktop building.
- Browser customization.
- Upstream security updates.
- Release engineering.
- Proprietary Google service limitations.
- Build and maintenance costs.

Use official Chromium source and developer documentation to verify important findings.

### Final foundation decision

Prepare a detailed comparison of:

| Evaluation criterion | Brave Core | Chromium |
|---|---|---|
| Browser compatibility | Research | Research |
| Existing features | Research | Research |
| Development complexity | Research | Research |
| Windows build requirements | Research | Research |
| Custom branding | Research | Research |
| Privacy functionality | Research | Research |
| Extension support | Research | Research |
| Security maintenance | Research | Research |
| License obligations | Research | Research |
| Engineering costs | Research | Research |
| Long-term sustainability | Research | Research |

Assign justified weights and produce a scored recommendation.

**Recommend exactly ONE primary browser foundation.**

My current preference is Brave Core, but do not select it blindly. Change your recommendation if the verified technical evidence supports direct Chromium.

Brave Core already uses Chromium. Do not build a system that merges Brave Core and a second independent Chromium browser tree.

The final decision requires maintainer approval before expensive native integration.

---

## PHASE 4 — DESIGN OUR PRODUCTION BROWSER

Design an architecture that separates:

1. Browser engine and upstream integration.
2. Independent application identity.
3. Browser interface.
4. Navigation, tabs, sessions and profiles.
5. Bookmarks, downloads and history.
6. Privacy and site permissions.
7. Extension support.
8. Productivity features.
9. Optional AI assistant.
10. Local data and user preferences.
11. Browser testing.
12. Build and release systems.
13. Security updates.
14. Future synchronization services.

Keep custom modifications isolated so upstream browser security updates remain manageable.

Our first supported platform should be Windows desktop x64.

Do not replace the architecture with an Electron-based browser simply because Electron is easier to build.

### Required user features

**Priority 0 — Core browser**

- Real web browsing.
- Multiple tabs and windows.
- Address and search bar.
- Navigation history.
- Bookmarks.
- Downloads.
- Profiles.
- Private browsing.
- Password storage using appropriate security mechanisms.
- Cookies and permissions.
- Browser extensions.
- Developer tools.
- Accessibility.
- Security updates.

**Priority 1 — Our independent identity**

- Original product name.
- Original logo and assets.
- Custom browser interface.
- Custom settings.
- New-tab experience.
- Independent service configuration.
- Appropriate privacy disclosures.

Do not copy competitor branding or assume access to Google or Brave proprietary services.

**Priority 2 — Productivity**

- Vertical tabs.
- Tab search.
- Persistent workspaces.
- Split-screen browsing.
- Session restoration.
- Keyboard shortcuts.
- Efficient tab management.

**Priority 3 — Privacy and performance**

- Investigate existing upstream protections.
- Avoid duplicating ad blockers already bundled.
- Manage sensitive browsing information appropriately.
- Benchmark startup and memory consumption.
- Test browser compatibility and stability.
- Maintain upstream security patches.

**Priority 4 — Optional AI browser assistant**

Eventually support:

- Summarizing selected pages with permission.
- Researching information across tabs.
- Organizing tabs and notes.
- Comparing sources.
- Preparing research reports.
- Optional local AI inference.
- Permission-controlled browser automation.

Research `llama.cpp`, Browser Use, and Stagehand when relevant.

Do not add expensive AI infrastructure before the browser itself works.

Treat webpage content as untrusted. Require explicit user authorization for consequential actions.

---

## PHASE 5 — START REAL IMPLEMENTATION

I do not want another endless planning cycle.

After analyzing the repository, start completing the earliest tasks permitted by its current engineering rules.

### Milestone M0 — Foundation research and preparation

Complete the existing backlog items BC-001 through BC-008 where feasible.

Deliver:

1. Verified Brave Core architecture audit.
2. Verified direct Chromium comparison.
3. Dependency and license inventory.
4. Updated browser feature matrix.
5. Windows build feasibility analysis.
6. Security and update strategy.
7. Decision-ready foundation recommendation.
8. Clear architecture decision proposal.
9. Implementation checklist with dependencies.
10. Small, useful repository improvements and automated validation checks.

Write the necessary documentation and lightweight engineering tooling.

Create targeted tests where useful.

Do not claim a browser is implemented when the repository only contains planning material.

### Milestone M1 — Real native browser build

After the maintainer approves the foundation and resource budget:

1. Pin the selected upstream commit.
2. Prepare an appropriate Windows development environment.
3. Install the supported toolchain.
4. Obtain the upstream source using official procedures.
5. Build the unmodified upstream first.
6. Run the actual browser.
7. Verify navigation, tabs, downloads, profiles and extensions.
8. Record build time, RAM, disk and CPU consumption.
9. Document exact reproduction steps.
10. Introduce automated smoke tests.

Do not bypass the approval gate for a large Chromium or Brave checkout.

### Milestone M2 — Our browser identity

After a verified upstream build:

1. Add independent branding.
2. Isolate product-specific changes.
3. Configure independent services.
4. Implement one carefully selected original feature.
5. Test the feature.
6. Verify security and accessibility.
7. Preserve the ability to update upstream.

### Milestones M3–M5

Continue with productivity features, privacy testing, optional AI, secure release engineering, and eventual public distribution.

Follow the existing repository roadmap and its acceptance gates.

---

## PHASE 6 — CONTROL COSTS AND CODEX CREDITS

Our available development resources may include Codex, AWS, Azure, and Google Colab, but do not assume those resources are free, unlimited, or suitable for native browser compilation.

Before running expensive operations, calculate:

- Required CPU.
- Required RAM.
- Disk capacity.
- Source download size.
- Build duration.
- CI requirements.
- Storage costs.
- Maintenance costs.
- Any model or API charges.

Ask for explicit approval before:

- Downloading full Chromium/Brave source trees.
- Running major browser builds.
- Provisioning expensive cloud infrastructure.
- Activating paid services.
- Downloading multi-GB AI models.
- Creating production credentials.
- Publishing binaries.

Use the smallest useful tests first.

Never rebuild functionality that already exists in the selected upstream without a justified reason.

---

## PHASE 7 — ENGINEERING AND GITHUB WORKFLOW

Use the existing repository rather than replacing it.

For every development task:

1. Inspect the existing implementation.
2. Identify the smallest missing functionality.
3. Research reusable solutions.
4. Verify licensing and security.
5. Make a focused implementation plan.
6. Implement the authorized changes.
7. Run relevant tests.
8. Document actual results.
9. Update the roadmap/checklist.
10. Commit changes to a dedicated branch.
11. Open a reviewable pull request when authorized.

Keep PRs small and independently verifiable.

Do not merge unreviewed changes or bypass repository protection rules.

Avoid untested, speculative mega-PRs.

---

## PHASE 8 — REQUIRED FINAL REPORT

At the end of your working session, provide:

**1. Repository analysis**

Actual code structure, files, implemented features, missing features, branches and PRs reviewed.

**2. Two-main-repository comparison**

Detailed Brave Core versus Chromium analysis, verified links, license implications, build requirements and final recommendation.

**3. All 18 repositories**

A classification showing which to use now, which to study, which are already included upstream, and which to defer.

**4. Development checklist**

Every major implementation task in dependency order, including priorities and acceptance criteria.

**5. Completed work**

Exact files changed, code written, tests added and commits/PRs created.

**6. Tests**

Commands executed, results, failures and tests not run.

**7. Cost analysis**

Estimated versus measured build resources and development expenses.

**8. Security**

Relevant threats, browser update strategy, licensing and sensitive-data protections.

**9. Blockers**

Exact permissions, decisions, hardware or other requirements preventing further implementation.

**10. Next implementation task**

The smallest real, testable next milestone with clear completion criteria.

## FINAL INSTRUCTION

Start working immediately.

Spend up to two hours researching if useful and supported.

Analyze our current repository and the complete `.txt` reference list.

Deeply study the two main foundation repositories:

1. https://github.com/brave/brave-core
2. https://github.com/chromium/chromium

Recommend one technically justified foundation.

**Do not stop at a generic architecture discussion. Produce verified research and begin real, safe, authorized engineering work.**

Respect the repository's `AGENTS.md` requirements, especially the foundation-selection and expensive-build approval gates.

Do not pretend that a prototype or documentation is a completed browser.

Our ultimate goal is an independent, maintainable, real desktop browser that users can install, browse with, and eventually choose over existing browsers.
