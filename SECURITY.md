# Security Policy

## Current scope

**No browser application or distributable binary exists in this repository yet.** Documentation and planning are not proof of security readiness. Once implementation begins, a security response workflow, supported-versions table and disclosure contacts must be established.

## Reporting vulnerabilities

**Do not post exploitable vulnerabilities, credentials, private user data, or reproduction details in public issues or pull requests.**

If GitHub's private vulnerability reporting is enabled for this repository, use the repository's **Security** tab and **Report a vulnerability**. If it is not enabled, do not post sensitive details publicly; request that the maintainer establish a private reporting channel first.

The project does not currently promise a response SLA or paid bug bounty. Do not assume responsible-disclosure channels are active until confirmed.

## Security engineering requirements

- Inherit upstream Chromium sandboxing and promptly integrate critical upstream fixes.
- Treat webpages, downloaded files, extensions, AI outputs and remote services as untrusted.
- Keep secrets in OS-supported secure stores; never commit secrets or dump browsing data into logs.
- Require explicit user consent for browser automation and sensitive actions.
- Review updates, release signing, dependencies, cryptography, permissions, third-party services and crash-reporting before release.
- Avoid modifying sandbox, site isolation, TLS and certificate validation unless a narrowly reviewed change proves necessary.

See [Security and Privacy Architecture](docs/SECURITY_AND_PRIVACY.md).
