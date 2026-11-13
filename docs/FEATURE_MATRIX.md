# Feature Inventory and Parity Matrix

**Not an implementation report.** This repository contains **no browser source**. “Upstream likely” is research guidance only; verification requires code references, a selected upstream commit, and tests.

Legend: **U** = expected in Chromium-derived upstream, **B** = Brave-specific candidate, **N** = new product work, **?** = not verified. All shipped-status cells for **our product are NOT BUILT**.

| Feature | Expected reuse route | Our product | Priority / verification |
| --- | --- | --- | --- |
| Tabbed browsing, navigation | U | Not built | P0: inspect and smoke test |
| Bookmarks, history, downloads | U | Not built | P0: import/export and persistence tests |
| Browser profiles & private mode | U/B | Not built | P0: isolation tests |
| Site permissions / TLS / sandbox | U | Not built | P0: security baseline |
| Browser extensions | U | Not built | P0: validate extension installation, APIs and updates |
| Passwords/autofill | U | Not built | P0: OS storage and threat review |
| PDF viewer, print, media | U, but proprietary codecs/DRM vary | Not built | P0: test and license-check |
| Privacy blocking | B | Not built | P0: upstream feature audit and filter tests |
| Installer and auto-update | U/B integration + own infrastructure | Not built | P0: release/security gate |
| UI theme, start page, tab search | U/B + N | Not built | P1: UX specs |
| Vertical tabs | U/B + N | Not built | P1: baseline audit then implement |
| Workspaces/tab groups | U/B + N | Not built | P1: persistence and accessibility |
| Split view | N / upstream audit | Not built | P1: navigation/isolation |
| Reader mode | U/B or Readability candidate | Not built | P1: sanitization and fidelity |
| Screenshot/annotation | U/B + N | Not built | P1: permission boundaries |
| Translation | U/B or independent provider | Not built | P2: external service/licensing |
| Optional page summarization | N + optional local model | Not built | P2: explicit consent |
| Research workspace/search | N | Not built | P2: usability experiments |
| AI browser automation | N / external patterns | Not built | P3: approval, rollback, injection defense |
| Cross-device sync | N service or licensed integration | Not built | P3: account/storage and security design |
| Android/macOS/Linux releases | Platform-specific work | Not built | P3: after desktop stability |
| Crash reporting / analytics | Optional independent services | Not built | P0 design; privacy choice |

## Required evidence for each verified row

- Upstream repo + pinned commit/tag + source path.
- Does feature actually work in the selected fork and target OS?
- Test command/steps, environment, result, date and artifact or screenshot where useful.
- Dependencies, license conditions, blockers, feature gaps.
- Owner and follow-up issue.

## Definition of parity

Parity means the **specified user journey passes repeatable tests**, not that a repository contains similarly named code. Add real testing data as work proceeds; never silently replace “not built” with “done.”

## Testing baseline

- Daily browse: search, 10-tab session, new window, incognito, back/forward, downloads and history.
- Accounts: site login/session persistence with permission boundaries; multiple profiles.
- Extensions: representative manifest/permission cases and extension update.
- Performance: page load, cold start, memory during many tabs, battery in representative workloads.
- Web compatibility: trusted sites from several categories with clear expected behavior.
- Security: crash handling, malicious download warnings where supported, sandbox/permissions.
- Accessibility: keyboard-only flows, focus order, labels, contrast, screen-reader smoke checks.
