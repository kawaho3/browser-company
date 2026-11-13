# Security, Privacy and Responsible AI Requirements

**No production security claims until engineering and testing demonstrate them.** A browser is high-risk software handling hostile websites, secrets, extensions, downloads, and often sensitive user information.

## Threats to address

| Trust boundary | Example threat | Expected control |
| --- | --- | --- |
| Website -> browser core | Renderer exploit, malicious content, navigation tricks | Current Chromium security patches, sandbox, site isolation |
| Extension -> site/browser data | Excessive permissions, exfiltration | Permission review, inherited extension architecture, testing |
| File download -> local system | Malicious executable, unsafe file handling | Safe download UX, OS protections and supported reputation checks |
| Browser profile -> local storage | Credential/cookie exposure | Existing secure stores, profile separation, no secrets in logs |
| Updater -> installed binary | Supply chain compromise | Signed artifacts, verified update metadata, rollback and provenance |
| Page content -> AI assistant | Prompt injection, secret extraction, false instructions | Page text treated as untrusted data; data minimization, no silent tool execution |
| AI -> user accounts | Unauthorized purchases, deletions or sends | Explicit scopes, confirmation for consequential actions, cancel/stop |
| Telemetry -> provider | Unexpected data sharing | Off until policy/consent and security design exist |

## Security update operating model

- Track upstream Chromium/Brave security advisories and release changes.
- Assign a maintainer to triage critical updates and regressions.
- Maintain an upgradable patch stack with minimal divergence.
- Verify patch applicability, compile, targeted regression tests, signed release and rollback.
- Record supported release versions, reporting contacts and patch policy before public launch.

## AI-specific baseline

- Opt-in by feature; disclose local versus remote processing clearly.
- Require explicit page selection or approved site scope for sensitive content.
- Never put passwords, session tokens, private key material or hidden page content into prompts by default.
- Do not execute instructions embedded in webpages as developer/system commands.
- Require preview/confirmation for email, purchases, uploads, submissions, destructive operations, changes to security settings or financial actions.
- Provide a kill switch and ability to review actions.
- Test adversarial webpages and manipulated retrieved content.

## Data practices

Plan product requirements for: retention limits, export and deletion, local encryption where appropriate, account protection, support/diagnostics redaction, consent revocation and transparency. Avoid making speculative “zero data collection” claims until verified against actual binary/service network behavior.

## Release blockers

No release if: known critical exploitable flaws are unresolved; security updates cannot be delivered; signing keys are not protected; private user data is sent unexpectedly; extension permissions are bypassed; or AI acts on high-impact pages without user approval.

See [SECURITY.md](../SECURITY.md) for private reporting guidance.
