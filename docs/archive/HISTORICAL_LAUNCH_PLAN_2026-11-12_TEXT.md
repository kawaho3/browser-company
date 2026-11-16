# Historical launch plan — source text preserved

> Provenance: text extracted from the user's *Browser_Company_Launch_Plan.pdf*, dated 12 November 2026 (7 pages). This preserves the earlier free-first WebView2 proposal as history, **not current architecture guidance**. See the newer full-browser master prompt and the Brave/Chromium M0 audit. PDF layout and embedded figures are not preserved in this text-only transcription.

~~~text
<PARSED TEXT FOR PAGE: 1 / 7>
 01 / BROWSER COMPANY PLAN



 Build a browser.
 Start with a focused product.
 A free-first plan for one founder working with GPT-6 Astra in Codex. Prepared 12 November 2026.


  The recommendation
  Start with a Windows browser application using an existing engine. Aim for a useful prototype
  with ₹0 additional software spend, then validate a narrow audience before a public launch.


 What “like Chrome” means for this plan
 We build our own name, interface, tabs, bookmarks and distinctive workflow. An existing browser
 engine handles web pages. Matching Chrome across security, extensions, sync, devices and every
 website is a much larger, ongoing undertaking.

   Approach                              Decision


   Windows app + WebView2                Recommended starting point. Reuse the Edge/Chromium rendering
                                         engine; build the product around it. [1, 2]


   Full Chromium fork                    Consider after demand is proven, if deep browser control is essential.
                                         You must keep merging and shipping upstream security changes.
                                         Building also needs substantial hardware and storage. [4]


   New browser engine                    Outside the scope of this two-person, near-zero-budget launch. This is
                                         a sustained systems-engineering project.



 A concrete first product to validate
 A workspace browser for students and researchers: save related tabs and notes by project,
 reopen work reliably, and keep the app’s own workspace data on the device. This is a proposed
 niche, not a proven demand claim.

 Interview 10 potential users. Find a repeated problem, show a small demo, and recruit 5 willing
 testers. A different logo alone is unlikely to justify switching browsers.

 Planning assumptions
 One existing Windows computer, reliable internet, an existing ChatGPT subscription, and roughly
 15-20 founder hours per week. Initial target: Windows 11. No paid AI service inside the browser,
 no account system, and no cloud sync. Hardware upgrades, electricity and internet are not
 included in ₹0.




Browser company launch plan | 12 November 2026                                                                    1
<PARSED TEXT FOR PAGE: 2 / 7>
 02 / BROWSER COMPANY PLAN



 The first version
 Recommended technical foundation
 C# + .NET + WPF + WebView2 Evergreen, with local files or SQLite for app-owned bookmarks
 and workspaces. .NET is free for commercial use. WebView2 embeds Microsoft’s browser
 technology; we do not need to compile Chromium to make this prototype. [1, 5]

 Evergreen receives runtime updates automatically, but a running app may need a restart to use
 them. Our own app code still needs testing, fixes and an update channel. [2]

   Include in the first useful version                        Defer until validated


   Address/search bar; back, forward, reload; tabs and        Android, iPhone, macOS and Linux releases.
   keyboard shortcuts.


   Bookmarks, history with deletion, download controls,       Account login, cloud sync, VPN and paid AI
   and clear error pages.                                     assistants.


   Workspace save/restore, basic local notes, export and      Custom password manager, full extension-store
   backup.                                                    support and advanced ad blocking.


   Permission prompts, clear site identity, crash recovery,   Promises of Chrome feature parity, lower RAM
   app update notices.                                        use or universal streaming support.



 Prove compatibility before polishing the interface
 Use a small technical prototype to test the actual services the audience needs: website login and
 logout, pop-ups, file uploads and downloads, PDFs, video/audio, camera/microphone permissions
 and external links. Test paid/DRM media only if it is a product requirement. An embedded engine
 is not the complete Chrome application.

 If an essential workflow fails because of the architecture, reassess the engine before spending
 weeks on design. Moving later to a Chromium fork would be a separate engineering project.

 Keep the security boundary simple
 Keep browser controls separate from website content. Do not expose native file, process or
 system APIs to arbitrary pages. Validate origins and any messages crossing into the app. Run
 without administrator privileges. [3]

 Electron is an alternative for desktop interfaces, but its own documentation warns about arbitrary
 untrusted content. It is not my default choice for this browser project. [6]

 What you need
 A supported Windows development environment; Git and a source repository; .NET SDK and an
 editor; WebView2 SDK; sample sites and a written test list. A PC with 16 GB RAM and an SSD is a
 comfortable planning target, not a verified minimum. No dedicated AI GPU is needed when using
 hosted Codex.



Browser company launch plan | 12 November 2026                                                                2
<PARSED TEXT FOR PAGE: 3 / 7>
 03 / BROWSER COMPANY PLAN



 Cost: free prototype,
 separate launch budget
 Amounts below distinguish published pricing from planning allowances. Vendor facts checked 12 November 2026;
 taxes, local checkout prices and eligibility can differ.


   Item                                  Initial cost / treatment


   Development tools and local app       Target ₹0 with the free toolchain and existing computer. No backend is
   data                                  required for local workspaces. [1, 5]


   GPT-6 Astra in Codex                  Use your plan’s allowance; extra project spend can be ₹0 if you stay
                                         within it. Usage is limited and depends on task size. Your existing
                                         subscription remains a cost. [7]


   ChatGPT Plus baseline                 Official list price: US$20/month. At that price, 3-5 months is
                                         US$60-100 before tax/local pricing. This is not an extra charge if
                                         already budgeted. [7]


   App distribution and signing          Target ₹0 through approved Microsoft Store MSIX distribution.
                                         New-flow registration and Store MSIX signing are free; verification and
                                         certification still apply. [8, 9]


   Website / custom domain               A custom domain is optional. Set aside ₹1,000-2,000/year if wanted;
                                         this is a planning allowance, not a registrar quote.


   Direct-download code signing          Optional alternative to Store MSIX. Microsoft lists indicative OV
                                         certificates at US$150-300/year; provider totals and eligibility need a
                                         quote. [10]


   Security review and business          Quote separately. Review depth, company structure, accounting,
   setup                                 privacy work and jurisdiction determine cost. These are not covered by
                                         a ₹0 prototype claim.



 Three spending decisions
 • Prototype: ₹0 additional software budget; use the existing machine and subscription. Delay
 optional spending.

 • Small pilot: keep the same architecture; use Store distribution if accepted. An optional
 ₹1,000-5,000 yearly allowance can cover a domain and minor expenses, not professional services.

 • Public business: set a separate budget for independent review, legal/accounting needs,
 support and ongoing maintenance. There is no honest fixed total before this scope is defined.

 Normal browsing connects users directly to websites; you do not pay to relay all their traffic. Hosting users’ AI
 requests, sync or a VPN would create new operating costs. If downloads were self-hosted, 10,000 downloads × 200
 MB would be about 2 TB of delivery; that is a sizing example, not a bill.




Browser company launch plan | 12 November 2026                                                                       3
<PARSED TEXT FOR PAGE: 4 / 7>
 04 / BROWSER COMPANY PLAN



 A realistic delivery sequence
 Planning estimate, not a delivery guarantee: 1-3 weeks for a basic technical prototype and roughly 3-5 months for a
 limited private beta at 15-20 hours per week. A beginner or tighter Codex allowance may need longer. Public
 release depends on the gates below.


   When              Work                                          Pass condition


   Week 1            Audience interviews, choose one               5 people agree to test; write a one-page
                     problem, select 10 essential sites.           product scope.


   Weeks 2-3         One-window prototype; navigation,             Essential sites and sign-in flows work;
                     tabs and compatibility checks.                document engine limitations.


   Weeks 4-8         Core browsing, bookmarks, history,            Normal use works; restart and failed
                     downloads and local persistence.              operations do not lose user data.


   Weeks 9-12        Workspace feature, accessibility,             Users can finish the target workflow without
                     keyboard use, recovery and packaging.         developer help.


   Weeks 13-16       Private beta with 10-20 testers;              Track repeat use and blockers; fix critical
                     performance and security work.                defects; arrange independent review.


   Weeks             Address review findings; test updates         Release gates pass. Otherwise stay in beta or
   17-20+            and Store submission.                         narrow the product.



 How you and Codex work together

   Owner                          Responsibility


   You                            Product decisions, Windows testing, tester interviews, accounts, spending,
                                  release approval and customer support.


   GPT-6 Astra / Codex            Draft and explain code, implement scoped features, investigate errors, write
                                  meaningful tests, review changes and maintain documentation.


   Independent specialist,        Review the native/web security boundary and release mechanism. Get local
   before broad release           business/privacy advice where needed. AI review is useful but not
                                  independent assurance.



 Control credit use and rework
 Keep a backlog and a short project specification. Ask Codex for one testable feature at a time,
 retain working commits, and provide exact errors. Use Standard speed if it meets the need; check
 the usage dashboard. If allowance runs out, wait for reset rather than adding paid credits. No
 separate OpenAI API is needed for this plan. [7]




Browser company launch plan | 12 November 2026                                                                         4
<PARSED TEXT FOR PAGE: 5 / 7>
 05 / BROWSER COMPANY PLAN



 The difficulties we must
 handle
   Challenge                       Practical response


   Security and privacy            Treat every visited page as untrusted. Keep native access closed; test
                                   permission prompts, certificate errors, downloads and hostile pop-ups. Avoid
                                   collecting browsing history. [3]


   Compatibility                   Maintain a repeatable list of target sites. Login, extensions and DRM can
                                   differ from Chrome. Google Chrome Sync is not automatically available to a
                                   Chromium derivative. [11]


   Memory and performance          Measure startup time, memory with representative tabs, CPU and video
                                   playback on the same machine. Reusing Chromium technology does not
                                   guarantee beating Chrome.


   Continuous maintenance          Test runtime updates; ship our app fixes; maintain a vulnerability-report
                                   contact and an emergency response process. Evergreen does not fix
                                   mistakes in our own application. [2]


   Distribution and trust          Prepare reproducible versioned builds, working updates and clear publisher
                                   identity. Store approval is not guaranteed; direct downloads may require
                                   paid signing. [8-10]


   Winning users                   Recruit one narrow audience and measure continued use. Marketing,
                                   onboarding and support are founder work even when Codex writes the
                                   application.


   Licences and claims             Use an original brand, retain required third-party notices and review
                                   licences. Verify any codec/DRM distribution terms. Describe actual privacy
                                   and performance behavior, not aspirations.



 Public release gate
 • Independent review findings are addressed; no known critical security issues remain. Passing
 tests does not prove the absence of vulnerabilities.

 • Fresh install, update, uninstall, runtime restart, crash recovery and data deletion work on
 supported Windows configurations.

 • Downloaded files are not silently executed; permissions show the requesting site; untrusted
 pages cannot call native app APIs.

 • Licences, privacy notice, support contact, dependency inventory and a workable security-update
 process are ready.

 During development, use dedicated test profiles and non-sensitive accounts. Do not encourage testers to move
 banking, primary passwords or confidential work into an unreviewed prototype.



Browser company launch plan | 12 November 2026                                                                  5
<PARSED TEXT FOR PAGE: 6 / 7>
 06 / BROWSER COMPANY PLAN



 Turn the product into a
 business
 First prove that people return
 Use interviews and an opt-in weekly check-in before building an analytics backend. Suggested
 pilot target: 20 people install, 10 return in week two, and 5 name the same feature as useful.
 These are internal decision thresholds, not industry benchmarks. If users do not return, revise the
 product before expanding platforms.

 An early revenue hypothesis
 Keep basic browsing free. Test willingness to pay for advanced local workspace organization or
 managed setup/support for small teams. Validate pricing with actual users before implementing
 billing. Search revenue agreements and large advertising income should not be assumptions in
 the initial business model.

 As an arithmetic example only, 100 paying users × ₹150/month = ₹15,000/month gross revenue,
 before taxes, payment/store fees, support, refunds and other costs. Neither that price nor that
 customer count is a forecast.

 Business formation and ownership
 If you will operate in India, ask a local accountant or lawyer to compare suitable structures,
 registration, ongoing filing/accounting costs, tax treatment and privacy obligations before taking
 payments or signing commercial agreements. Keep this budget separate from app development.

 DPIIT recognition is a separate process with eligibility rules; Startup India says its recognition
 application has no government fee. That does not mean incorporation or ongoing compliance is
 free. [13]

 Choose the product name after checking conflicts. Decide whether your own application code will
 be open source or proprietary after reviewing dependency licences. Keep source, release keys,
 publisher accounts and backups under accounts you control.

 The first seven days

   Day          Concrete output


   1            Choose one target audience and write the problem in one sentence.


   2-3          Interview potential users; list essential websites and recruit five testers.


   4            Check the Windows PC, create the repository and install the free toolchain.


   5-6          Build a minimal WebView2 prototype; test navigation, login and downloads.


   7            Record failures, confirm the engine choice and freeze a small version-one scope.




Browser company launch plan | 12 November 2026                                                         6
<PARSED TEXT FOR PAGE: 7 / 7>
 07 / BROWSER COMPANY PLAN



 Sources and estimate notes
 Primary documentation checked 12 November 2026. Numbered references support factual platform/pricing claims.
 Schedules, spending allowances, product choices and pilot targets are planning judgments for this scenario.

 [1] Microsoft: WebView2 overview
 https://learn.microsoft.com/en-us/microsoft-edge/webview2/

 [2] Microsoft: Runtime distribution and Evergreen updates
 https://learn.microsoft.com/en-us/microsoft-edge/webview2/concepts/distribution

 [3] Microsoft: Secure WebView2 applications
 https://learn.microsoft.com/en-us/microsoft-edge/webview2/concepts/security

 [4] Chromium: Windows build requirements
 https://chromium.googlesource.com/chromium/src/+/main/docs/windows_build_instructions.md

 [5] .NET: Free tools and commercial-use licensing
 https://dotnet.microsoft.com/en-us/platform/free

 [6] Electron: Security guidance for untrusted content
 https://www.electronjs.org/docs/latest/tutorial/security/

 [7] OpenAI: Codex plans, usage and pricing
 https://learn.chatgpt.com/docs/pricing

 [8] Microsoft: Developer-account registration
 https://learn.microsoft.com/en-us/windows/apps/publish/partner-center/open-a-developer-account?pivots=store-installer-
 msix

 [9] Microsoft: Store distribution and MSIX signing
 https://learn.microsoft.com/en-us/windows/apps/publish/get-started?tabs=individual,msix-pwa-getting-started

 [10] Microsoft: Windows code-signing options
 https://learn.microsoft.com/en-us/windows/apps/package-and-deploy/code-signing-options

 [11] Chromium: Google API and browser-sign-in restrictions
 https://www.chromium.org/developers/how-tos/api-keys/

 [12] GitHub: Software releases and distribution limits
 https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases

 [13] Startup India: Recognition, eligibility and fee distinction
 https://www.startupindia.gov.in/content/sih/en/startupgov/startup_recognition_page.html

 Distribution fallback: GitHub Releases can host versioned binaries under its current service rules. It does not
 provide publisher signing, security review or an app updater; public downloads also require appropriate repository
 visibility. [12]

 Scope limit: this plan does not certify a finished application, guarantee Store acceptance or estimate a full
 Chrome-equivalent company. Revisit scope and prices after the compatibility prototype.




Browser company launch plan | 12 November 2026                                                                            7
~~~
