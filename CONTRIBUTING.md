# Contributing to Browser Company

Thanks for helping build an independent competitor in the browser market. The project is at **planning / research stage**; there is no runnable browser here yet.

## Choose a contribution

- **Research:** verify an existing Chromium/Brave capability and link specific upstream source, issue, or documentation.
- **Documentation:** improve architecture, comparison, technical decisions, security constraints or onboarding clarity.
- **Product design:** submit measurable user requirements and acceptance criteria.
- **Code:** only after a maintainer has selected a foundation, settled contributor licensing, and opened an implementation issue.

Start with [ONBOARDING](docs/ONBOARDING.md) and [BACKLOG](docs/BACKLOG.md).

## Workflow

1. Check open issues, decision log and existing docs before proposing a duplicate feature.
2. Open a narrowly scoped issue with context, alternatives and acceptance criteria. For security problems, use [SECURITY.md](SECURITY.md), **not** a public issue.
3. Create a branch from the current main, for example docs/reuse-audit.
4. Keep each pull request focused, link its issue and state whether it changes a decision.
5. Explain how you verified claims; link upstream docs or code rather than guessing.
6. Report checks performed and work left unverified. Do not claim unavailable tests were run.
7. Seek maintainer review before merging or pulling in external dependencies.

## Contribution checklist

- [ ] Clear goal, scope, reproducible evidence and explicit acceptance criteria.
- [ ] No unlicensed third-party code, copied proprietary assets, passwords or tokens.
- [ ] License and integration review for any external dependency.
- [ ] Security/privacy implications identified, including any page or AI data flows.
- [ ] No expensive build, model download, paid service or new scheduled CI without approval.
- [ ] Relevant docs and feature status updated.
- [ ] PR template completed.

## Local work (documentation phase)

~~~bash
git clone https://github.com/kawaho3/browser-company.git
cd browser-company
git checkout -b docs/my-improvement
# Edit Markdown files and check relative links.
git add .
git commit -m "docs: clarify <topic>"
git push -u origin docs/my-improvement
# Open a pull request into main.
~~~

There is currently no project-specific build command. See [BUILD_AND_COST](docs/BUILD_AND_COST.md) rather than running upstream setup steps speculatively.

## License and ownership note

This repository currently has **no top-level license**. Public visibility does not automatically grant broad reuse rights. Discuss source-code submissions in an issue first; a repository license and contributor policy must be approved before substantial implementation contributions. Every introduced dependency needs license and notice review. See [LEGAL_AND_BRANDING](docs/LEGAL_AND_BRANDING.md).

## Behavior

Be respectful, discuss ideas and evidence rather than people, and do not post personal information, proprietary material, security exploit details, or harassment. Maintainers may moderate contributions that violate these expectations.
