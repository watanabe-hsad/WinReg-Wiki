# Changelog

All notable changes to this project will be documented in this file.

The format follows the spirit of Keep a Changelog, and this project has not published a versioned release yet.

## [Unreleased]

### Added

- Added USB / device artifact pages and YAML:
  - USB
  - DeviceClasses
  - Enum SWD WPDBUSENUM
  - EMDMgmt
  - Portable Devices
  - VolumeInfoCache
- Added persistence / autorun artifact pages and YAML:
  - Active Setup
  - AppInit_DLLs
  - ShellServiceObjectDelayLoad
  - Print Monitors
  - LSA Security Packages
  - Drivers
- Added registry-tree path reference pages for USB/device and persistence paths:
  - `HKLM\SYSTEM\ControlSet00x\Enum\USB`
  - `HKLM\SYSTEM\ControlSet00x\Control\DeviceClasses`
  - `HKLM\SYSTEM\ControlSet00x\Enum\SWD\WPDBUSENUM`
  - `HKLM\SYSTEM\ControlSet00x\Control\Print\Monitors`
  - `HKLM\SYSTEM\ControlSet00x\Services\<DriverName>`
  - `HKLM\SYSTEM\ControlSet00x\Control\Lsa\Security Packages`
  - `HKLM\SOFTWARE\Microsoft\Active Setup`
  - `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Windows`
  - `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\ShellServiceObjectDelayLoad`
  - `HKLM\SOFTWARE\Microsoft\Windows Portable Devices`
  - `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\EMDMgmt`
  - `HKLM\SOFTWARE\Microsoft\Windows Search\VolumeInfoCache`
- Added registry-tree path reference pages for `HKLM\SYSTEM`: `Select`, `ControlSet00x`, `Services`, `Enum`, `MountedDevices`, `Terminal Server`, `Tcpip`, `TimeZoneInformation`, `ComputerName`, and `Lsa`.
- Added registry-tree path reference pages for `HKLM\SOFTWARE`: `ProfileList`, `Winlogon`, `Image File Execution Options`, `Policies`, `Windows Defender`, `Uninstall`, `WOW6432Node`, and `Classes`.
- Added registry-tree path reference pages for `HKCU`: `ComDlg32`, `RunMRU`, `RecentDocs`, `Internet Settings`, and `Classes`.
- Added registry-tree path reference pages for `HKU`: `.DEFAULT` and service-account SIDs.
- Added GitHub Pages deployment workflow at `.github/workflows/pages.yml`.
- Added project handoff and maintenance documents: `PROJECT_STATUS.md`, `ROADMAP.md`, and `CHANGELOG.md`.
- Added GitHub-ready README content with project positioning, local usage, content principles, current scope, contribution notes, and license status.
- Initialized local git repository on branch `main`; `origin` is now configured as `https://github.com/watanabe-hsad/WinReg-Wiki.git`.
- Added generated artifact data index output target: `docs/artifacts/generated-index.md`.
- Added missing YAML records for previously existing artifact pages: UserAssist, Amcache, ShimCache / AppCompatCache, Services, IFEO, Terminal Server Client, USBSTOR, and MountedDevices.
- Added user behavior artifact pages and YAML:
  - RunMRU
  - RecentDocs
  - OpenSavePidlMRU
  - LastVisitedPidlMRU
- Added RDP server-side artifact pages and YAML:
  - fDenyTSConnections
  - RDP-Tcp PortNumber
  - CredSSP / NLA
- Added security policy artifact pages and YAML:
  - UAC Policies
  - Firewall Policies
  - Audit Policy
  - SpecialAccounts\UserList

### Changed

- Renamed the project display name and repository metadata to `WinReg Wiki`.
- Switched repository metadata from the old handbook repository to `https://github.com/watanabe-hsad/WinReg-Wiki.git`.
- Simplified top-level navigation to `首页`, `注册表位置`, and `取证场景`, with `贡献` and `标签` as auxiliary entries.
- Moved artifact indexes and detection engineering under `取证场景` instead of keeping them as top-level tabs.
- Reworked `注册表位置` navigation to use section index pages and removed visible `概览` child items.
- Moved registry-tree files into a directory hierarchy closer to native Windows registry paths.
- Rewrote the homepage as a compact `WinReg Wiki` entry page.
- Updated `mkdocs.yml` so the new USB/device and persistence artifacts appear in `注册表 Artifact`, and the new path pages appear under `注册表位置`.
- Updated `docs/artifacts/index.md`, scenario pages, detection page, and registry-tree overview pages to link the new artifacts.
- Regenerated `docs/artifacts/generated-index.md`; it now includes 42 YAML-backed artifacts.
- Localized the top-level Artifact navigation to `注册表 Artifact`.
- Localized Artifact category navigation, manual artifact index headings, generated artifact data index headings, and generated category/value labels.
- Localized artifact page section headings and `docs/contributing/template.md` section headings to Chinese while keeping artifact file names and URLs in English.
- Reworked `docs/registry-tree/index.md` as a concise directory-style entry page.
- Expanded `mkdocs.yml` registry-location navigation to better match the Windows registry tree hierarchy.
- Changed registry-location navigation from section-style grouping to expanded multi-level tree navigation.
- Rewrote registry-tree pages to be concise key/value reference pages instead of long forensic-analysis pages.
- Updated `site_url` to `http://hsad.xyz/windows-registry-forensics-handbook/`.
- Updated README and project handoff notes to describe the current custom-domain project path and shorter URL options.
- Added `site_url`, `repo_name`, `repo_url`, and `edit_uri` repository metadata to `mkdocs.yml`.
- Updated `README.md` with the online site URL and GitHub Actions deployment notes.
- Updated `PROJECT_STATUS.md` with GitHub Pages deployment information, first-time Pages settings guidance, and pushed-branch handoff status.
- Pushed the current project state and GitHub Pages workflow to `origin/main`.
- Deepened core registry-tree pages for `HKEY_LOCAL_MACHINE`, `HKLM\SYSTEM`, `HKLM\SOFTWARE`, `HKEY_CURRENT_USER`, and `HKEY_USERS`.
- Enhanced `scripts/generate-artifact-index.py` to read all YAML records and generate a richer Markdown table with artifact, category, native root, hive/offline file, evidence type, forensic value, detection value, and primary paths.
- Added `PyYAML` to `requirements.txt` because artifact index generation depends on YAML parsing.
- Added the generated data index to MkDocs navigation without overwriting the manually curated artifact index.
- Updated `mkdocs.yml`, `docs/artifacts/index.md`, scenario pages, detection page, and registry-tree pages to link the new artifact pages.
- Previously regenerated `docs/artifacts/generated-index.md` with 30 YAML-backed artifacts before the current USB/device and persistence expansion.

### Verification

- `.venv/bin/python scripts/generate-artifact-index.py` and `.venv/bin/mkdocs build --strict` were run after the `WinReg Wiki` navigation and file-tree rewrite.
- `.venv/bin/mkdocs serve -a 127.0.0.1:8000` was used briefly for local preview of `注册表位置`, `注册表 Artifact`, and `结构化数据索引`.
- `.venv/bin/python scripts/generate-artifact-index.py` completed successfully and wrote `docs/artifacts/generated-index.md`.
- `.venv/bin/mkdocs build --strict` completed successfully.
- The Material for MkDocs upstream warning about MkDocs 2.0 appeared during build; it is not treated as a project build failure.

## Previous Unreleased Work

### Added

- Replaced the old hive-focused registry location entry with a Windows native registry tree entry.
- Added root registry-tree pages for `HKEY_CLASSES_ROOT`, `HKEY_CURRENT_USER`, `HKEY_LOCAL_MACHINE`, `HKEY_USERS`, and `HKEY_CURRENT_CONFIG`.
- Added HKLM subtree pages for `SAM`, `SECURITY`, `SOFTWARE`, `SYSTEM`, `HARDWARE`, and `BCD00000000`.
- Added artifact pages for:
  - BAM / DAM
  - MUICache
  - StartupApproved
  - Winlogon Userinit
  - Winlogon Shell
  - LSA Authentication Packages
  - Command Processor AutoRun
  - MountPoints2
  - ProfileList
  - Defender Policies
- Added matching structured YAML records for those 10 artifacts.
- Added scenario pages for accounts/security, policy/security, network, software installation, anti-forensics, and Shell / Explorer user behavior.

### Changed

- Updated homepage, investigation scenario index, artifact index, detection engineering page, and artifact template.
- Removed the old `docs/hives/*.md` pages from navigation and replaced them with `docs/registry-tree/`.

### Verification

- `.venv/bin/python scripts/generate-artifact-index.py` completed successfully.
- `.venv/bin/mkdocs build --strict` completed successfully.
