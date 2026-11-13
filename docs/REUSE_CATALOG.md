# Open-Source Reuse Catalog

**Rule:** a GitHub URL is a **candidate**, not an installed dependency, approved license assessment, or integration guarantee. The selected foundation's existing implementation must be inspected before adding anything.

| Role | Candidate | Why consider it | Preliminary action |
| --- | --- | --- | --- |
| Browser base | [Brave Core](https://github.com/brave/brave-core) | Chromium customization layer, managed dependencies, privacy features | Audit first; preferred candidate |
| Alternative base | [Chromium](https://github.com/chromium/chromium) | Widely used web engine and browser | Compare with Brave Core; do not merge both as separate browsers |
| Desktop prototype only | [Min Browser](https://github.com/minbrowser/min) | Smaller Electron-based reference | **Not** strategic final foundation for full extension parity |
| UX reference | [Zen Browser](https://github.com/zen-browser/desktop) | Workspace/UI ideas; Firefox-based | Inspiration only, don't merge |
| Chromium privacy reference | [Ungoogled Chromium](https://github.com/ungoogled-software/ungoogled-chromium) | Disabling/removing Google integrations | Evaluate applicable patches only |
| Brave ad blocker | [adblock-rust](https://github.com/brave/adblock-rust) | Filter engine | Already managed in Brave Core; don't double-include |
| Reading mode | [Mozilla Readability](https://github.com/mozilla/readability) | Article extraction | Only after auditing existing reader mode; sanitize output |
| On-device inference | [llama.cpp](https://github.com/ggml-org/llama.cpp) | Local model runtime | Experimental after browser works; check model licenses |
| On-device transcription | [whisper.cpp](https://github.com/ggml-org/whisper.cpp) | Local speech-to-text | Later, optional |
| Agent automation research | [Browser Use](https://github.com/browser-use/browser-use) | Browser task automation patterns | Research only; approval & prompt-injection controls |
| Agent automation alternative | [Stagehand](https://github.com/browserbase/stagehand) | AI-assisted automation patterns | Compare against Browser Use; don't add both by default |
| Browser end-to-end testing | [Playwright](https://github.com/microsoft/playwright) | Automated workflows/regression | High-priority dev dependency if compatible |
| Browser conformance | [web-platform-tests](https://github.com/web-platform-tests/wpt) | Standards tests | Use targeted tests; huge suite |
| React UI library | [Fluent UI](https://github.com/microsoft/fluentui) | Potential components for React surfaces | **Not** native Chromium UI drop-in |
| Electron packaging | [electron-builder](https://github.com/electron-userland/electron-builder) | Packaging Electron prototypes | **Not** Chromium native fork builder |
| macOS updater candidate | [Sparkle](https://github.com/sparkle-project/Sparkle) | Native macOS update framework | Only if macOS app architecture fits |

## Dependency due-diligence checklist

Before copying, vendoring, forking, or installing, record:
- **Provenance:** exact URL, commit/tag, maintenance and last relevant update.
- **License:** SPDX identifier verified against repository license file; file-level differences; attribution and source obligations; patents/trademarks.
- **Engineering fit:** language, runtime, platform, native ABI, toolchain, process boundary, sandbox implications, package size and update strategy.
- **Security:** threat model, vulnerability advisories, extension permissions, network communication and privacy.
- **Cost:** size of dependency graph, build memory/disk/time, CI usage, API fees, bundled model size and maintenance effort.
- **Decision:** keep current upstream feature, adopt, adapt a small compatible part, or reject.

## Why not combine everything?

Combining full browser forks multiplies Chromium patch divergence, merge conflicts, security-update lag, license obligations and build cost. For this project, choose **one core** and minimize separate vendors.

## Licensing status

No components above have been formally accepted. The main Brave Core repo indicates MPL 2.0, but distributed artifacts can contain many independently licensed parts. Verify exact files and licenses as part of an SBOM; see [LEGAL_AND_BRANDING](LEGAL_AND_BRANDING.md).

## Useful upstream documentation

- [Brave Core source/build overview](https://github.com/brave/brave-core#readme)
- [Chromium developer documentation](https://www.chromium.org/developers/)
- [Chromium Linux build requirements](https://chromium.googlesource.com/chromium/src/+/main/docs/linux/build_instructions.md)
- [Chromium Windows build requirements](https://chromium.googlesource.com/chromium/src/+/main/docs/windows_build_instructions.md)
