# Project Status

## Current Goal

The project has been renamed and repositioned as `WinReg Wiki`: a concise Windows registry key/value lookup wiki with forensic leads. The current architecture is intentionally simple: `首页`, `注册表位置`, and `取证场景`.

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
- `docs/questions/`: forensic scenario entry point. Scenario pages carry evidence semantics, cross-validation, detection ideas, and links into artifact pages.
- `docs/artifacts/`: manually written artifact pages. They are no longer a top-level navigation tab; users enter them from `取证场景 -> Artifact 索引` or related links.
- `data/artifacts/`: structured artifact YAML records. Current coverage is 42 artifact pages and 42 YAML records.
- `scripts/generate-artifact-index.py`: reads `data/artifacts/*.yml` and writes `docs/artifacts/generated-index.md`.
- `mkdocs.yml`: site configuration and navigation. Top-level nav is now `首页`, `注册表位置`, `取证场景`, plus auxiliary `贡献` and `标签`.
- `.github/workflows/pages.yml`: GitHub Actions workflow for MkDocs build and GitHub Pages deployment.

## Last Completed Round

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
- `注册表位置` is a path dictionary. It should explain key/value meaning, live/offline location, common writers, and short caveats.
- `取证场景` and artifact pages carry evidence interpretation, attacker usage, detection ideas, false positives, collection, and cross-validation.
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

The Material for MkDocs upstream warning about MkDocs 2.0 may appear during build; it is not currently a project build error.

## Next Priorities

- Confirm GitHub Pages settings for the new repository and decide whether the online path should remain under the old custom-domain path or move to a new path / subdomain.
- Continue cleaning registry-tree pages into the short dictionary structure where older pages still have extra prose.
- Add deeper registry-location pages for `HKCU\Environment`, user-level Run / Command Processor, ZoneMap, Printers, NetworkList, and TCP/IP Interfaces.
- Add remaining registry artifacts only after the architecture settles: KnownDLLs, App Paths, Winlogon Notify, BootExecute, CachedLogonsCount, LogonUI.
- Add contribution guide and source-quality expectations.
- Choose a license and add a `LICENSE` file.

## Notes For Next Agent

- Current branch is `main`.
- `origin` should point to `https://github.com/watanabe-hsad/WinReg-Wiki.git`.
- Do not assume the new GitHub Pages URL is already live. Check repository Pages settings before documenting a new URL.
- Preserve `site/` as ignored generated output.
- Always run the generated index script and strict build after navigation or link changes.
