# WinReg Wiki

WinReg Wiki is a MkDocs Material knowledge base for Windows registry key/value lookup and forensic leads.

GitHub repository: `https://github.com/watanabe-hsad/WinReg-Wiki.git`

The project is organized as a wiki rather than a long-form handbook. Registry-location pages explain where keys live and what values mean. Forensic scenario pages explain investigation checks and cross-validation. Artifact pages are retained as supplemental entries for detailed field semantics, collection notes, parsing tools, and structured data.

## Main Entry Points

- Registry tree: start from Windows native roots such as `HKEY_LOCAL_MACHINE`, `HKEY_CURRENT_USER`, `HKEY_USERS`, `HKEY_CLASSES_ROOT`, and `HKEY_CURRENT_CONFIG`.
- Forensic scenarios: start from questions such as program execution, persistence, USB devices, RDP, account anomalies, security policy changes, network configuration, software installation, and anti-forensics.
- Artifact supplemental index: use only when a scenario or registry-location page needs deeper artifact-specific notes.

## Online Site

Current online address is still pending confirmation after the repository rename. The previously reachable project path is:

http://hsad.xyz/windows-registry-forensics-handbook/

The GitHub Pages path for the new repository should be confirmed in GitHub Pages settings before documenting it as live.

Deployment is handled by GitHub Actions. On each push to `main`, the workflow:

1. installs dependencies from `requirements.txt`;
2. regenerates `docs/artifacts/generated-index.md` from `data/artifacts/*.yml`;
3. runs `mkdocs build --strict`;
4. deploys the generated `site/` directory to GitHub Pages.

## Local Preview

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/generate-artifact-index.py
mkdocs serve
```

Then open:

```text
http://127.0.0.1:8000
```

Strict build check:

```bash
.venv/bin/mkdocs build --strict
```

Generate the structured artifact data index:

```bash
.venv/bin/python scripts/generate-artifact-index.py
```

## Content Principles

- Keep pages concise and query-oriented.
- Registry-tree pages should read like a key/value dictionary: path, source hive, common values, short notes, related scenarios.
- Keep deeper investigation logic in scenario pages; keep artifact pages as supplemental details rather than the main reading path.
- Separate evidence strength clearly: configuration exists, program exists, user interaction, program execution, device presence, policy weakening, and malicious behavior are different claims.
- Do not treat registry key LastWrite as a value creation time unless that is explicitly supported by the artifact and tool output.
- Explain live-to-offline mappings accurately: `HKCU`, `HKCR`, `HKCC`, and `CurrentControlSet` are views or mappings, not simple standalone hive files.
- Keep Windows version differences explicit. If behavior is not verified for a version, mark it as pending verification instead of guessing.

## Current Scope

Current coverage includes:

- Registry tree pages for HKCR, HKCU, HKLM, HKU, HKCC, and core HKLM / HKCU subtrees.
- Registry-location references for environment variables, Command Processor, Internet Settings / ZoneMap, Printers, NetworkList Profiles, TCP/IP interfaces, EventLog, FirewallPolicy, and Defender policy locations.
- Program execution and program presence artifacts: UserAssist, BAM / DAM, Amcache, ShimCache / AppCompatCache, MUICache.
- Persistence and autoruns: Run / RunOnce, StartupApproved, Services, Drivers, IFEO, Active Setup, AppInit_DLLs, Winlogon Userinit, Winlogon Shell, LSA Authentication Packages, LSA Security Packages, Command Processor AutoRun, ShellServiceObjectDelayLoad, Print Monitors.
- USB and external devices: USB, USBSTOR, DeviceClasses, SWD WPDBUSENUM, MountedDevices, MountPoints2, EMDMgmt, Portable Devices, VolumeInfoCache.
- RDP and remote access: Terminal Server Client, fDenyTSConnections, RDP-Tcp PortNumber, CredSSP / NLA.
- Accounts and security policy: ProfileList, Defender Policies, UAC Policies, Firewall Policies, Audit Policy, SpecialAccounts\UserList.

## Structured Data

Structured artifact data lives in `data/artifacts/*.yml`. The generator in `scripts/generate-artifact-index.py` reads those YAML files and writes a generated Markdown index to `docs/artifacts/generated-index.md`.

Manual narrative indexes such as `docs/artifacts/index.md` should not be overwritten by generated output.

## Contributing

Contributions should follow the artifact template in `docs/contributing/template.md`.

Before opening a pull request, run:

```bash
.venv/bin/python scripts/generate-artifact-index.py
.venv/bin/mkdocs build --strict
```

When adding or changing an artifact, update both the Markdown page and `data/artifacts/*.yml` if structured data exists for that artifact.

## Project Status

Maintainer and future-agent handoff notes live in:

- `PROJECT_STATUS.md`
- `ROADMAP.md`
- `CHANGELOG.md`

The local directory is currently still named `registry-forensics-handbook-demo`; the formal project name is `WinReg Wiki`.

## License

License: TBD
