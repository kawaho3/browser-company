# New Developer Onboarding

Welcome. This document is the fastest path from finding this repository to making a useful contribution.

## 0. Know what exists today

As of 2026-11-13, the repository is a **planning and documentation hub**. No Chromium/Brave fork, installer, compiled binary, cloud backend or runnable AI agent has been added. A developer cannot currently compile a Browser Company browser from this repository.

## 1. Read in this order

1. [README](../README.md) — mission and current status.
2. [VISION](VISION.md) — the product users should eventually get.
3. [ARCHITECTURE](ARCHITECTURE.md) and [DECISIONS](DECISIONS.md) — what we propose and what is still open.
4. [FEATURE_MATRIX](FEATURE_MATRIX.md) — current unverified feature requirements.
5. [REUSE_CATALOG](REUSE_CATALOG.md) — candidates to research before coding.
6. [BUILD_AND_COST](BUILD_AND_COST.md) and [SECURITY_AND_PRIVACY](SECURITY_AND_PRIVACY.md) — constraints and release gates.
7. [CONTRIBUTING](../CONTRIBUTING.md) and [AGENTS](../AGENTS.md) (for Codex).

## 2. Start a research/documentation contribution

~~~bash
git clone https://github.com/kawaho3/browser-company.git
cd browser-company
git checkout -b research/foundation-comparison
# Update relevant Markdown documents with citations and a clear status.
git diff --check
git status
~~~

Open a focused GitHub issue or PR following the templates. External browser source is **not** checked into this repo.

## 3. How to describe findings

Use this record in an issue:

~~~text
Topic:
Question:
Upstream repository + exact commit/tag:
Source paths / primary links:
What is verified:
What remains unverified:
License / security implications:
Build/RAM/disk/CI implications:
Recommended decision + alternative:
Acceptance test for follow-on work:
~~~

## 4. When development starts

A maintainer will announce (and document):
- selected foundation and pinned revision;
- repo layout/fork strategy and company license;
- supported toolchain and operating systems;
- verified build commands and machine sizing;
- fast local tests and CI contract;
- secure release/update and contribution processes.

Until then **do not invent build commands**, download 100+ GB of browser source by default, or submit unreviewed third-party code.

## 5. First-week plan for a contributor

- **Day 1:** read docs, review one open question, raise a scoped issue.
- **Days 2-3:** investigate an upstream feature or build constraint using primary sources.
- **Days 4-5:** propose one decision-ready PR with evidence, alternatives, test plan and cost.
- **After review:** take the next bounded work package assigned from docs/BACKLOG.md.

## 6. Definition of done for planning work

A different developer should be able to reproduce the research, understand the trade-offs, know what is unverified, and take the next step without asking the original author for hidden context.
