# Windows Registry Forensics Handbook

Windows Registry Forensics Handbook is a MkDocs Material knowledge base for Windows registry forensics, DFIR, incident response, threat hunting, and detection engineering.

GitHub repository: `https://github.com/watanabe-hsad/windows-registry-forensics-handbook.git`

The handbook is not a general Windows Registry encyclopedia. It is an investigation-oriented registry artifact handbook: each page should help an analyst understand where to look, what a key or value can prove, what it cannot prove, how timestamps should be interpreted, how attackers may abuse the location, what detection logic can watch, and which external artifacts should be used for validation.

## Main Entry Points

The site keeps two primary navigation paths:

- Investigation scenarios: start from questions such as program execution, persistence, USB devices, RDP, account anomalies, security policy changes, network configuration, software installation, and anti-forensics.
- Native registry tree: start from Windows native roots such as `HKEY_LOCAL_MACHINE`, `HKEY_CURRENT_USER`, `HKEY_USERS`, `HKEY_CLASSES_ROOT`, and `HKEY_CURRENT_CONFIG`, then map the live view back to offline hive files.

## Online Site

The handbook is intended to be published with GitHub Pages:

https://watanabe-hsad.github.io/windows-registry-forensics-handbook/

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

- Keep the handbook practical: prioritize paths, fields, evidence semantics, timestamps, abuse cases, detection ideas, false positives, collection notes, parsing tools, and cross validation.
- Separate evidence strength clearly: configuration exists, program exists, user interaction, program execution, device presence, policy weakening, and malicious behavior are different claims.
- Do not treat registry key LastWrite as a value creation time unless that is explicitly supported by the artifact and tool output.
- Explain live-to-offline mappings accurately: `HKCU`, `HKCR`, `HKCC`, and `CurrentControlSet` are views or mappings, not simple standalone hive files.
- Keep Windows version differences explicit. If the behavior is not verified for a version, mark it as pending verification instead of guessing.
- Preserve artifact page structure so pages remain comparable and maintainable.

## Current Scope

Current coverage includes:

- Program execution and program presence: UserAssist, BAM / DAM, Amcache, ShimCache / AppCompatCache, MUICache.
- Persistence and autoruns: Run / RunOnce, StartupApproved, Services, IFEO, Winlogon Userinit, Winlogon Shell, LSA Authentication Packages, Command Processor AutoRun.
- USB and external devices: USBSTOR, MountedDevices, MountPoints2.
- RDP and remote access: Terminal Server Client, plus registry-tree guidance for RDP server configuration.
- Accounts and security policy: ProfileList, Defender Policies, LSA-related configuration.
- Native registry tree pages for HKCR, HKCU, HKLM, HKU, HKCC, and core HKLM subtrees.

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

The local directory is currently still named `registry-forensics-handbook-demo`; the intended GitHub repository name is `windows-registry-forensics-handbook`.

## License

License: TBD
