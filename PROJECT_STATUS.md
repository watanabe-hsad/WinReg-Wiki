# Project Status

## Current Goal

The project has been renamed and repositioned as `WinReg Wiki`: a concise Windows registry key/value lookup wiki with forensic leads. The current architecture is intentionally simple: `首页`, `注册表位置`, and `取证场景`.

Current content model:

- `首页`: explains the project scope, registry basics, and how to choose an entry point.
- `注册表位置`: primary dictionary-style entry point. Pages explain key/value location, hive source, common values, default/common state, short caveats, related scenarios, and related registry positions.
- `取证场景`: checklist-style investigation entry point. Scenario pages now primarily link to `docs/registry-tree/` pages and then list cross-validation sources.
- `docs/artifacts/`: supplemental/internal artifact detail. These pages are kept for field semantics, collection notes, parsing tools, false positives, and structured YAML data, but they are no longer the main reading path.

## Repository

- Local path: `/Users/hsad/Documents/CodeProject/registry-forensics-handbook-demo`
- Formal project name: `WinReg Wiki`
- GitHub repository: `https://github.com/watanabe-hsad/WinReg-Wiki.git`
- Repository name: `WinReg-Wiki`
- Default branch: `main`
- Current online site: pending confirmation after repository rename.
- Previously reachable custom-domain path: `http://hsad.xyz/windows-registry-forensics-handbook/`
- Local directory note: the local folder still has the older `registry-forensics-handbook-demo` name. Do not rename it unless local tooling and references are checked.

## Current Structure

- `docs/registry-tree/`: Windows native registry tree entry point. Root keys are directories with `index.md` files, using MkDocs Material `navigation.indexes` so section labels are clickable.
- `docs/questions/`: forensic scenario entry point. Scenario pages carry investigation checklists, evidence boundaries, cross-validation, common misreads, and primary links into registry-location pages.
- `docs/artifacts/`: manually written artifact pages. They are no longer a top-level navigation tab or primary reader flow; users enter them from `取证场景 -> Artifact 补充索引` or supplemental reading links.
- `data/artifacts/`: structured artifact YAML records. Current coverage is 42 artifact pages and 42 YAML records.
- `scripts/generate-artifact-index.py`: reads `data/artifacts/*.yml` and writes `docs/artifacts/generated-index.md`.
- `mkdocs.yml`: site configuration and navigation. Top-level nav is now `首页`, `注册表位置`, `取证场景`, plus auxiliary `贡献` and `标签`.
- `.github/workflows/pages.yml`: GitHub Actions workflow for MkDocs build and GitHub Pages deployment.

## Last Completed Round

- Added RDP and account/login registry-location pages:
  - `HKLM\SYSTEM\ControlSet00x\Control\Terminal Server\WinStations\RDP-Tcp`
  - `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\CredSSP`
  - `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\CachedLogonsCount`
  - `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Authentication\Credential Providers`
  - `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\UserList`
- Updated `mkdocs.yml` so the new pages are reachable through the native registry tree hierarchy without adding top-level navigation entries.
- Updated scenario pages so primary links include the new RDP/login registry-location pages:
  - `registry-checklist.md`
  - `rdp.md`
  - `accounts-security.md`
  - `policy-security.md`
- Compressed these RDP artifact pages into supplemental entries:
  - `fdenytsconnections.md`
  - `rdp-tcp-portnumber.md`
  - `credssp-nla.md`
- Artifact/YAML inventory remains 42 artifact pages and 42 YAML records. No YAML field model changes were made.

## Previous Completed Round

- Added and normalized another login/policy/execution-focused registry-tree batch:
  - `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Authentication\LogonUI`
  - `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System`
  - `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\Notify`
  - `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AeDebug`
  - `HKLM\SYSTEM\ControlSet00x\Control\Session Manager\AppCertDlls`
  - `HKCU\Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags`
- Rewrote existing `Winlogon`, `Image File Execution Options`, `ProfileList`, and `Terminal Server Client` registry-tree pages into the current short dictionary structure.
- Updated scenario pages so primary links include the new registry-location pages:
  - `registry-checklist.md`
  - `persistence.md`
  - `execution.md`
  - `anti-forensics.md`
  - `policy-security.md`
  - `accounts-security.md`
  - `software-install.md`
  - `questions/index.md`
- Compressed these artifact pages into supplemental entries:
  - `winlogon-userinit.md`
  - `winlogon-shell.md`
  - `uac-policies.md`
  - `specialaccounts-userlist.md`
  - `profilelist.md`
  - `terminal-server-client.md`
- Artifact/YAML inventory remains 42 artifact pages and 42 YAML records. No YAML field model changes were made.

## Previous Completed Round

- Continued the registry-tree dictionary expansion with the next HKLM-focused batch:
  - `HKLM\SOFTWARE\Microsoft\Command Processor`
  - `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths`
  - `HKLM\SOFTWARE\Policies\Microsoft\WindowsFirewall`
  - `HKLM\SYSTEM\ControlSet00x\Control\Session Manager`
  - `HKLM\SYSTEM\ControlSet00x\Control\Session Manager\BootExecute`
  - `HKLM\SYSTEM\ControlSet00x\Control\Session Manager\KnownDLLs`
  - `HKLM\SYSTEM\ControlSet00x\Control\Session Manager\PendingFileRenameOperations`
- Updated `mkdocs.yml`, `docs/registry-tree/index.md`, `HKLM\SOFTWARE`, `HKLM\SYSTEM`, `ControlSet00x`, `Policies`, `FirewallPolicy`, and `Session Manager\Environment` pages so the new pages are reachable through the native registry tree.
- Updated scenario pages so primary links include the new registry-location pages:
  - `registry-checklist.md`
  - `persistence.md`
  - `execution.md`
  - `anti-forensics.md`
  - `policy-security.md`
  - `network.md`
  - `software-install.md`
  - `questions/index.md`
- Compressed these additional artifact pages into supplemental entries:
  - `drivers.md`
  - `appinit-dlls.md`
  - `ifeo.md`
- Artifact/YAML inventory remains 42 artifact pages and 42 YAML records. No YAML field model changes were made.

## Earlier Completed Round

- Expanded and normalized registry-location reference pages so `注册表位置` remains the primary dictionary entry point.
- Added or rewrote these registry-location pages in the short key/value style:
  - `HKCU\Environment`
  - `HKCU\Printers`
  - `HKCU\Software\Microsoft\Command Processor`
  - `HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings`
  - `HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap`
  - `HKLM\SYSTEM\ControlSet00x\Services\EventLog`
  - `HKLM\SYSTEM\ControlSet00x\Services\SharedAccess\Parameters\FirewallPolicy`
  - `HKLM\SOFTWARE\Microsoft\Windows Defender`
  - `HKLM\SOFTWARE\Policies\Microsoft\Windows Defender`
  - `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Profiles`
  - `HKLM\SYSTEM\ControlSet00x\Services\Tcpip\Parameters\Interfaces`
  - `HKLM\SYSTEM\ControlSet00x\Control\Session Manager\Environment`
- Updated registry-tree overview/support pages so HKCU, HKLM SOFTWARE, HKLM SYSTEM, Services, Tcpip, and Policies point to the new pages.
- Updated scenario pages so the main investigation path points to registry-location pages first:
  - `registry-checklist.md`
  - `network.md`
  - `policy-security.md`
  - `persistence.md`
  - `anti-forensics.md`
  - `execution.md`
  - `questions/index.md`
- Compressed these artifact pages into supplemental entries after moving their practical facts into registry-location/scenario pages:
  - `command-processor-autorun.md`
  - `defender-policies.md`
  - `firewall-policies.md`
  - `audit-policy.md`
  - `run-keys.md`
  - `services.md`
- Artifact/YAML inventory remains 42 artifact pages and 42 YAML records. Artifact pages remain supplemental/internal and are intentionally not part of the primary top-level navigation.

## Older Completed Round

- Refined the site into a registry-first dual-entry knowledge base:
  - scenario pages now use `取证场景 -> 注册表位置` as the main flow;
  - artifact pages are explicitly documented as supplemental/internal detail;
  - `docs/artifacts/index.md` is now `Artifact 补充索引`;
  - `docs/artifacts/generated-index.md` explains that generated YAML data is for maintenance/review, not the primary reader path.
- Added registry-location pages to cover common scenario links:
  - `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`
  - `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`
  - `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist`
  - `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\MountPoints2`
  - `HKLM\SYSTEM\ControlSet00x\Enum\USBSTOR`
- Added `取证场景 / 常规注册表检查` at `docs/questions/registry-checklist.md`.
- Reworked scenario pages into checklist-style pages with primary links to registry-location pages:
  - `execution.md`
  - `persistence.md`
  - `rdp.md`
  - `shell-explorer.md`
  - `usb.md`
  - `accounts-security.md`
  - `policy-security.md`
  - `network.md`
  - `software-install.md`
  - `anti-forensics.md`
- Updated key registry-location pages to include `相关场景` and changed old `相关 Artifact` sections to `补充阅读` where touched.
- Artifact/YAML inventory remains 42 artifact pages and 42 YAML records.

## Initial Completed Round

- Renamed the site and repository metadata to `WinReg Wiki`.
- Switched `origin` to `https://github.com/watanabe-hsad/WinReg-Wiki.git`.
- Kept `site_url` at the previously reachable custom-domain path until the new GitHub Pages path is confirmed.
- Collapsed top-level navigation:
  - removed `基础概念` from the top level and linked those pages from the homepage;
  - removed `注册表 Artifact` from the top level and moved artifact indexes under `取证场景`;
  - removed `检测工程` from the top level and moved it under `取证场景`.
- Rebuilt `注册表位置` navigation as a registry-like section-index tree:
  - `HKEY_CLASSES_ROOT` -> `docs/registry-tree/hkcr/index.md`
  - `HKEY_CURRENT_USER` -> `docs/registry-tree/hkcu/index.md`
  - `HKEY_LOCAL_MACHINE` -> `docs/registry-tree/hklm/index.md`
  - `HKEY_USERS` -> `docs/registry-tree/hku/index.md`
  - `HKEY_CURRENT_CONFIG` -> `docs/registry-tree/hkcc/index.md`
- Removed visible `概览` child entries from registry-tree navigation. Click the section itself to open that level's `index.md`.
- Moved HKCU/HKLM subtree pages deeper so paths better match native registry hierarchy, for example:
  - `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer`
  - `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon`
  - `HKLM\SYSTEM\ControlSet00x\Services`
  - `HKLM\SYSTEM\ControlSet00x\Control\Lsa`
- Rewrote `docs/index.md` as a compact Wiki homepage.
- Updated `README.md`, `CHANGELOG.md`, and `ROADMAP.md` for the new name and architecture.

Previous completed content state:

- Added USB/device and persistence artifacts with matching YAML:
  - USB, DeviceClasses, Enum SWD WPDBUSENUM, EMDMgmt, Portable Devices, VolumeInfoCache.
  - Active Setup, AppInit_DLLs, ShellServiceObjectDelayLoad, Print Monitors, LSA Security Packages, Drivers.
- Generated artifact index contains 42 YAML-backed artifacts.

## Important Decisions

- Treat the project as a Wiki, not a blog or long-form DFIR handbook.
- Top-level navigation should stay small: homepage, registry tree, forensic scenarios.
- `注册表位置` is the primary path dictionary. It should explain key/value meaning, live/offline location, common writers, default/common state, and short caveats.
- `取证场景` carries investigation logic, cross-validation, common misreads, and links back to registry-location pages.
- Artifact pages carry supplemental evidence interpretation, collection, parsing tools, false positives, and structured YAML data. Do not make artifact pages a top-level navigation system again unless the information architecture changes intentionally.
- Keep English filenames and URLs; use Chinese navigation and display text where practical.
- Keep `data/artifacts/*.yml` stable and backward-compatible. It drives the generated index and future exports.
- Timestamp interpretation must stay conservative. Do not treat key LastWrite as the creation time of a specific value.
- Mapping relationships must be explicit: `HKCU` maps to `HKU\<SID>`, `HKCR` is a merged Classes view, `HKCC` maps into `SYSTEM`, and `CurrentControlSet` is resolved through `HKLM\SYSTEM\Select`.
- License remains `TBD`.

## Verification

Last verified locally:

```bash
.venv/bin/python scripts/generate-artifact-index.py
.venv/bin/mkdocs build --strict
```

Both commands completed successfully after the registry-first scenario rewrite. The Material for MkDocs upstream warning about MkDocs 2.0 may appear during build; it is not currently a project build error. MkDocs may also print INFO that artifact pages are not in `nav`; this is expected because artifact pages are supplemental.

Latest verification for the registry-tree expansion and artifact compression:

```bash
.venv/bin/python scripts/generate-artifact-index.py
.venv/bin/mkdocs build --strict
```

Both commands completed successfully. The generated index remained valid for 42 YAML-backed artifacts. The MkDocs Material upstream warning and MkDocs INFO about artifact pages outside `nav` are expected in the current architecture.

## Next Priorities

- Confirm GitHub Pages settings for the new repository and decide whether the online path should remain under the old custom-domain path or move to a new path / subdomain.
- Continue cleaning registry-tree pages into the short dictionary structure where older pages still have extra artifact-style prose.
- Continue cleaning older registry-tree pages into the same short dictionary structure used by the latest HKCU/HKLM additions.
- Continue migrating useful artifact facts into registry-location and scenario pages; keep artifacts as supplemental detail.
- Add deeper registry-location pages for `Session Manager\SubSystems`, `Session Manager\Memory Management`, machine-level `AppCompatFlags`, `AppCompatFlags\Layers`, `Terminal Server\WinStations` policy subkeys, Credential Provider Filters, and additional HKCU network / shell policy locations.
- Add remaining registry artifacts only after the architecture settles: CachedLogonsCount, LogonUI, Winlogon Notify, App Paths, KnownDLLs, BootExecute, AeDebug, AppCertDlls, Credential Providers, and AppCompatFlags if they need structured YAML-backed supplement pages.
- Add contribution guide and source-quality expectations.
- Choose a license and add a `LICENSE` file.

## Notes For Next Agent

- Current branch is `main`.
- `origin` should point to `https://github.com/watanabe-hsad/WinReg-Wiki.git`.
- Do not assume the new GitHub Pages URL is already live. Check repository Pages settings before documenting a new URL.
- Preserve `site/` as ignored generated output.
- Always run the generated index script and strict build after navigation or link changes.
