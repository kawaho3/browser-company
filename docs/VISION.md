# Product Vision and Definition of Success

## North star

Build an independently operated browser company that can become a **credible competitor to Google Chrome**. Chrome is the product benchmark, not our source of proprietary assets, credentials, cloud services or trademarks.

This is a **multi-year ambition**, not a statement that a viable competitor has already been built.

## Value proposition

**A trustworthy browser that matches everyday web compatibility while making complex online work easier and offering meaningful control over privacy and AI.**

Hypotheses to validate with potential users:
1. Chrome compatibility is table stakes: sites, downloads, extensions, accessibility and reliability must work.
2. Native organization—vertical tabs, split views, workspaces, search—can improve heavy tab workflows.
3. Optional local/on-device AI and research assistance can reduce repetitive browsing tasks.
4. Clear permissions and privacy defaults can differentiate us if performance remains competitive.

Do not claim these hypotheses are proven until user research and measurements support them.

## Target audiences

- **Initial:** Windows desktop power users, researchers and students with complex tab/workspace usage.
- **Expansion:** developers, small teams and privacy-conscious everyday users.
- **Later:** macOS, Linux, Android and synchronized multi-device users, pending technical and operating feasibility.

## Experience pillars

| Pillar | What success looks like |
| --- | --- |
| Compatibility | Important sites, media, accessibility, extensions and web standards work as expected |
| Speed and efficiency | Competitive startup, navigation, memory and battery behavior, measured on real hardware |
| Privacy and trust | Transparent data flows; secure defaults and prompt security updates |
| Productivity | Tabs, workspaces, split views and search solve repeated user problems |
| AI as an option | Useful assistance with explicit permissions, local processing where feasible, no surprise uploads |
| Reliability | Reproducible tests, releases and rollback; no missed critical browser fixes |

## Product differentiation: proposed

A focused **AI Research Workspace**: organize web research into topic workspaces, summarize selected pages with permission, compare sources, search tabs/notes, and perform low-risk repeated tasks with explicit review. It must be useful even when AI is disabled.

## Scope and non-goals

**In scope, staged:** a full desktop browser; compatibility and extension support; privacy; custom user experience; optional AI; release engineering and updates.

**Not first-release commitments:** a new rendering engine; perfect parity with all Chrome proprietary services; mobile in the first milestone; built-in paid model services; browser crypto-wallet or rewards token economies; universal automated actions without consent.

## Measures and launch gates (proposals, not actual results)

- P0 critical user journeys pass smoke and regression tests.
- No known release-blocking security issues; upstream security patch process demonstrated.
- Critical websites, extensions, keyboard accessibility and import flows validated on target OS.
- Time to produce a signed, reproducible release measured and documented.
- Test real user task-completion rates, crash-free sessions and performance against a browser baseline.
- Observe willingness to switch and retention before expanding the feature count.

## Project principles

1. Reuse first; ownership of **new original code** is compatible with keeping third-party license obligations.
2. Every major new dependency needs a maintainer, license, version, update cadence and exit plan.
3. Every large build or hosted service gets a cost checkpoint.
4. Private data is not an implicit AI training or analytics input.
5. We compete through quality and differentiated workflows, not a long unchecked feature list.
