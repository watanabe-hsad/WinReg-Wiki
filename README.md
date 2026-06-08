# WinReg Wiki

WinReg Wiki is a MkDocs Material knowledge base for Windows registry key/value lookup and registry-related forensic leads. The current homepage is a compact search-first registry database entrance: start with search, quick filters, registry path cards, or scenario cards.

GitHub repository: `https://github.com/watanabe-hsad/WinReg-Wiki.git`

The project is organized as a wiki, not a long-form incident response handbook. Registry-location pages explain where keys live and what values mean. Forensic scenario pages combine registry locations into checklists. Artifact pages are retained as supplemental entries for field semantics, collection notes, parser support, and structured data.

## Main Entry Points

- Registry Explorer: use the filterable card database generated from `data/registry/` to search by path, Hive, topic, status, or scenario.
- Registry tree: start from Windows native roots such as `HKEY_LOCAL_MACHINE`, `HKEY_CURRENT_USER`, `HKEY_USERS`, `HKEY_CLASSES_ROOT`, and `HKEY_CURRENT_CONFIG`.
- Structured registry index: use generated root / topic / hive tables when a static list is faster than interactive filtering.
- Forensic scenarios: start from cards for program execution, persistence, USB devices, RDP, account anomalies, policy changes, network configuration, software installation, and cleanup traces.
- Artifact supplemental index: use when a scenario or registry-location page needs deeper artifact-specific notes.

## Online Site

The current online address is still pending confirmation after the repository rename. The previously reachable project path is:

http://hsad.xyz/windows-registry-forensics-handbook/

Do not treat a shorter URL as live until GitHub Pages and DNS settings are confirmed. Candidate future paths:

- `https://hsad.xyz/winreg/`
- `https://winreg.hsad.xyz/`

The subdomain option is cleaner for a long-lived wiki, but it requires maintainer confirmation.

## Data Model

Structured data is split by purpose:

| Directory | Purpose |
|---|---|
| `data/registry/` | Registry-location facts for generated registry indexes and coverage. |
| `data/artifacts/` | Artifact-level facts for supplemental artifact index pages. |

Generated outputs:

| Script | Output |
|---|---|
| `scripts/generate-registry-index.py` | `docs/registry-tree/generated-index.md`, `docs/registry-tree/coverage.md`, `docs/assets/registry-index.json` |
| `scripts/generate-artifact-index.py` | `docs/artifacts/generated-index.md` |
| `scripts/check-content-style.py` | Fails on old project names, old artifact headings, English artifact-template headings, and subjective priority wording. |

Markdown pages remain manually maintained. Generated index pages should not be edited by hand.

## Local Preview

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
.venv/bin/python scripts/generate-artifact-index.py
.venv/bin/python scripts/generate-registry-index.py
.venv/bin/python scripts/check-content-style.py
.venv/bin/mkdocs serve
```

Then open:

```text
http://127.0.0.1:8000/windows-registry-forensics-handbook/
```

The path prefix comes from the current pending `site_url`. If the production URL is changed later, update this preview note together with `mkdocs.yml`.

Strict build check:

```bash
.venv/bin/python scripts/generate-artifact-index.py
.venv/bin/python scripts/generate-registry-index.py
.venv/bin/python scripts/check-content-style.py
.venv/bin/mkdocs build --strict
```

## GitHub Pages

Deployment is handled by GitHub Actions. On each push to `main`, the workflow:

1. installs dependencies from `requirements.txt`;
2. regenerates artifact and registry indexes;
3. checks generated files are committed;
4. runs the content style check;
5. runs `mkdocs build --strict`;
6. deploys the generated `site/` directory to GitHub Pages.

## Visual System

The site keeps MkDocs Material and uses a small project-specific CSS system in `docs/stylesheets/extra.css`.

- `ww-compact-head`, `ww-search-panel`, `ww-dashboard-grid`, and `ww-stat-card` shape the quiet search-first homepage.
- `ww-registry-explorer`, `ww-explorer-toolbar`, and `ww-explorer-card` power the compact JSON-backed Registry Explorer.
- `ww-feature-card`, `ww-path-card`, `ww-root-card`, `ww-scenario-card`, and `ww-check-card` provide database-style entry and checklist cards.
- `ww-chip`, `ww-badge`, `ww-path-pill`, and `ww-fact-card` keep registry paths and page facts scannable.
- Tables are styled for dense reference reading and use container-level horizontal scrolling on narrow screens.

The visual direction is restrained and dense: Microsoft Learn-like documentation clarity with RegSeek / DFIRHub-style search, filters, dashboard stats, and compact database entry patterns. It intentionally avoids heavy frontend frameworks, marketing-page layout, oversized hero blocks, and decorative visual effects.

## Content Principles

- Keep pages concise and query-oriented.
- Registry-tree pages should read like a key/value dictionary: path, source hive, common values, short notes, related scenarios.
- Keep deeper investigation logic in scenario pages; keep artifact pages as supplemental details rather than the main reading path.
- Separate evidence strength clearly: configuration exists, program exists, user interaction, program execution, device presence, policy value exists, and malicious behavior are different claims.
- Do not treat registry key LastWrite as a value creation time unless that is explicitly supported by the artifact and tool output.
- Explain live-to-offline mappings accurately: `HKCU`, `HKCR`, `HKCC`, and `CurrentControlSet` are views or mappings, not simple standalone hive files.
- Keep Windows version differences explicit. If behavior is not verified for a version, write that it is version-dependent instead of guessing.

## Current Scope

Current coverage includes:

- Registry tree pages for HKCR, HKCU, HKLM, HKU, HKCC, and core HKLM / HKCU subtrees.
- Generated registry structured index and coverage matrix under `docs/registry-tree/`.
- Registry-location references for environment variables, Command Processor, Internet Settings / ZoneMap, Printers, NetworkList Profiles, TCP/IP interfaces, EventLog, FirewallPolicy, Defender policies, WindowsFirewall policies, App Paths, LogonUI, UAC policy, AppCompatFlags, AeDebug, Winlogon, Session Manager, USBSTOR, MountedDevices, Services, Run keys, and ProfileList.
- Program execution and program presence artifacts: UserAssist, BAM / DAM, Amcache, ShimCache / AppCompatCache, MUICache.
- Persistence and autoruns: Run / RunOnce, StartupApproved, Services, Drivers, IFEO, Active Setup, AppInit_DLLs, Winlogon Userinit, Winlogon Shell, LSA Authentication Packages, LSA Security Packages, Command Processor AutoRun, ShellServiceObjectDelayLoad, Print Monitors.
- USB and external devices: USB, USBSTOR, DeviceClasses, SWD WPDBUSENUM, MountedDevices, MountPoints2, EMDMgmt, Portable Devices, VolumeInfoCache.
- RDP and remote access: Terminal Server Client, fDenyTSConnections, RDP-Tcp PortNumber, CredSSP / NLA.
- Accounts and security policy: ProfileList, Defender Policies, UAC Policies, Firewall Policies, Audit Policy, SpecialAccounts\UserList.

## Contributing

Contributions should follow:

- `docs/contributing/index.md`
- `docs/contributing/template.md`
- `docs/contributing/registry-data-schema.md`

Before opening a pull request, run:

```bash
.venv/bin/python scripts/generate-artifact-index.py
.venv/bin/python scripts/generate-registry-index.py
.venv/bin/python scripts/check-content-style.py
.venv/bin/mkdocs build --strict
```

When adding or changing an artifact, update both the Markdown page and `data/artifacts/*.yml` if structured data exists for that artifact. When adding structured registry facts, update `data/registry/*.yml`, regenerate the registry index and JSON, and keep the registry-tree Markdown page human maintained.

## Project Status

Maintainer and future-agent handoff notes live in:

- `PROJECT_STATUS.md`
- `ROADMAP.md`
- `CHANGELOG.md`

The local directory is currently still named `registry-forensics-handbook-demo`; the formal project name is `WinReg Wiki`.

## License

License: TBD. Current recommendation is to choose either a documentation / code split such as `CC BY 4.0` for content and `MIT` for scripts, or a single repository-wide `MIT` license if the maintainer wants the simplest option.
