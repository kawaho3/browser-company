# Ownership, Open Source, Branding and Compliance

**Planning guidance, not legal advice.** Legal review is required before distribution.

## What the company can own

The company can own its **original code, designs, brand assets and infrastructure** subject to agreements with contributors and contractors. It cannot claim exclusive ownership of the upstream Chromium or Brave code. A derivative browser may combine company-owned code with third-party code under different licenses.

## Project-wide license decision is still OPEN

This repository has **no root LICENSE file on purpose**: the owner has not chosen a licensing strategy for new project code and docs. Public repository visibility is not itself an open-source license. Before substantial outside code contribution or shipping, decide:
- proprietary, permissive open source, or open-core approach for **new** code;
- whether contributor license agreement or DCO is appropriate;
- attribution, source distribution, patent and trademark policies;
- whether the chosen base imposes file-level or distribution-specific obligations.

## Third-party obligations

- [Brave Core](https://github.com/brave/brave-core) advertises **MPL-2.0**; covered source files and modifications have applicable MPL obligations when distributed. Confirm the precise rules, notices and scope.
- Chromium is largely BSD-style but includes many dependencies and licenses; audit the actual final distribution rather than assuming one license.
- Components such as Readability, Playwright, llama.cpp and others require their **own** license, notice, provenance and update review.
- A GitHub page, README, product screenshot or release binary is not necessarily permission to copy trademarked branding, proprietary services, protected assets or data.

## Company identity

- Choose and clear a new product name and logo before replacing Brave/Chromium identity.
- Do not ship Brave/Google names, logos or service keys as if they were owned by this project.
- Audit icons, fonts, artwork, default search agreements, user-agent representations, privacy claims and installer publisher identity.
- Before releasing binaries decide domain ownership, code-signing certificates, support contacts and a public privacy policy.

## Proprietary or service-dependent features

Google account sync, provider API keys, some security APIs, proprietary codecs/DRM and content services may need separate contracts, independent backends or alternate implementations. Chrome-compatible rendering does not grant access to all Chrome services.

## Compliance checklist for each release

- [ ] SBOM/license inventory with file-level exceptions reviewed.
- [ ] Notices/attributions and required source availability planned.
- [ ] Contributor provenance/rights checked.
- [ ] Product name/logo/trademark review complete.
- [ ] Privacy and data-processing disclosures approved.
- [ ] Encryption/crypto export and regional obligations reviewed if relevant.
- [ ] Code signing and update identity established.
- [ ] Release notes and security support policy published.
