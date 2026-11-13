# Initial Backlog and Work Packages

This is the **planning backlog**. Turn each work package into small GitHub issues with explicit owner, dependency, evidence and acceptance criteria. Nothing below is currently completed.

## P0 — Start here (M0)

| ID | Work item | Acceptance criteria |
| --- | --- | --- |
| BC-001 | Inventory Brave Core architecture | Current upstream branch/tag, dependency and build map, referenced source paths |
| BC-002 | Evaluate direct Chromium alternative | Compare customization cost, release process, missing services and patch burden |
| BC-003 | Licensing and ownership policy | SPDX/component review, company license decision, contributor terms recommendation |
| BC-004 | Chrome parity matrix | Every P0 row has an upstream source reference, verification state and target test |
| BC-005 | Build feasibility experiment plan | Target OS/machine, documented resource requirements, projected budget, rollback |
| BC-006 | Security/update review | Threat model, upstream patch process, signing and incident-response ownership |
| BC-007 | Differentiator user research | 5-10 interviews or another pre-agreed evidence set, ranked pain points and product hypotheses |
| BC-008 | Architecture ADR | Single selected foundation with version, build gate and maintained-patch strategy |

## P1 — After M0 approval

| ID | Work item | Acceptance criteria |
| --- | --- | --- |
| BC-101 | Reproducible baseline build | Exact commands, pinned versions, successful binary/test results and measured resources |
| BC-102 | Initial regression suite | Critical navigation, profiles, download, extension and bookmarks workflows |
| BC-103 | Product rebranding plan | Full trademark/service asset inventory and approved independent identifiers |
| BC-104 | Release/update pipeline design | Key custody, update verification, rollback and trusted CI boundaries |
| BC-105 | Product UI prototype | Accessibility-ready design and user-tested primary workflows |

## P2 — After verified baseline build

| ID | Work item | Acceptance criteria |
| --- | --- | --- |
| BC-201 | Vertical tabs/workspaces | Keyboard/a11y flows, persistence, performance and tests |
| BC-202 | Split view / tab search | User acceptance tests and no site-permission regression |
| BC-203 | On-device AI feasibility | Supported hardware, runtime/model licenses, measured memory/battery, consent |
| BC-204 | Reader/research workspace | Content sanitization, source preservation, evaluated workflows |
| BC-205 | Permissioned automation prototype | Threat model, explicit approval, injection tests, stop/rollback |

## Suggested first contributions

- Compare Brave vs direct Chromium with an evidence table and verified upstream links.
- Audit services/components not included in an independent Chromium fork.
- Write a measurable Windows browser baseline QA script/spec.
- Draft a component license/SBOM template and requirements for a contributor license decision.
- Research CI build machine configurations and realistic costs without running the builds.

**Use GitHub issue templates**. For large epics, create several independently testable PRs. Do not open one mega-task asking Codex to build the complete browser.
