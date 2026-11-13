# Builds, Codex Cloud and Cost Controls

> This repo has no application build yet. Commands here are either **documentation-only** or clearly labeled upstream references. Do not execute expensive initialization without approval.

## Roles of the environments

| Environment | Good for | Avoid assuming |
| --- | --- | --- |
| Codex Cloud | Repository analysis, documentation, code edits, targeted static/unit tests, PR preparation | Full Chromium/Brave source checkout and production compilation fit by default |
| Local powerful machine / dedicated build runner | Full native upstream compilation, platform builds, performance tests, release packaging | Free unlimited resources |
| GitHub Actions | Bounded CI, code quality, suitable preconfigured runners, signed pipeline after review | Unlimited free minutes, storage or sufficiently large default runners |
| Developer desktop | UI testing, reproducing browser behavior, platform-specific fixes | Reproducibility without pinned versions |

Chromium's current published Linux instructions specify **at least ~100 GB free disk space** and **more than 16 GB RAM recommended**; actual Brave/fork needs, platform requirements and costs must be measured. See [official Chromium Linux build instructions](https://chromium.googlesource.com/chromium/src/+/main/docs/linux/build_instructions.md) and [Brave Core setup](https://github.com/brave/brave-core#readme). Cloud resource tiers may change; verify them from the user's actual Codex environment.

## Budget-first development ladder

1. **Free/cheap research:** inspect source, issues and docs, record facts, design feature acceptance tests.
2. **Static validation:** formatting, linting, dependency manifest and unit tests on small packages.
3. **Component prototype:** constrained patch or API demonstration without downloading the full engine.
4. **Gated native integration:** approved full checkout/build on a capable machine; cache dependencies and record measured runtime.
5. **Gated release pipeline:** signed/tested builds on supported OS; security validation and rollback drills.

## Before requesting a full build

Write a ticket stating:
- upstream commit and checkout size estimate;
- target OS, architecture, toolchain and documented prerequisites;
- available CPU, RAM, storage and network;
- expected CI minutes, billable services and storage/caching costs;
- fallback if build fails due to resources;
- exact build command, expected artifact, logging and acceptance test;
- who approves repeated large builds.

## Reproducibility record template

| Item | Value |
| --- | --- |
| Target OS/architecture | TBD |
| Selected foundation/commit | TBD |
| Build machine CPU/RAM/disk | TBD |
| Toolchain versions | TBD |
| Build command | TBD after foundation selection |
| Clean build duration | Not measured |
| Incremental build duration | Not measured |
| Download / storage consumed | Not measured |
| Test results | Not executed |
| CI/billing cost | Not measured |
| Binary signing | Not configured |

Do not fill “not measured” cells with estimates presented as evidence.

## CI guidance

- No default scheduled workflow until costs are understood.
- Prevent untrusted fork PRs from receiving secrets.
- Review third-party actions and pin trusted versions/commit SHAs.
- Cache only when it reduces total cost without leaking secrets.
- Avoid uploading full browser sources, cookies, models, or huge binaries as PR artifacts.
- Separate unsigned PR/test builds from trusted release signing.
- Set concurrency, timeouts, storage retention and budget alerts before enabling full-build pipelines.

## Actual current setup

~~~bash
git clone https://github.com/kawaho3/browser-company.git
cd browser-company
# Only documentation exists here. There is no package install or build step yet.
~~~

Once M0 selects the foundation, replace this section with **tested** setup scripts and measured machine requirements.
