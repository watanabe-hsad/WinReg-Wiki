# Project Status

## Current Goal

GitHub Pages deployment is configured for the Windows Registry Forensics Handbook. The current maintenance state is to keep the site query-oriented, keep registry-tree pages concise, and continue artifact expansion.

## Repository

- Local path: `/Users/hsad/Documents/CodeProject/registry-forensics-handbook-demo`
- GitHub repository: `https://github.com/watanabe-hsad/windows-registry-forensics-handbook.git`
- GitHub Pages: `http://hsad.xyz/windows-registry-forensics-handbook/`
- Default GitHub Pages URL: `https://watanabe-hsad.github.io/windows-registry-forensics-handbook/`
- Repository name: `windows-registry-forensics-handbook`
- Default branch: `main`
- Local directory note: the local folder still has the older `registry-forensics-handbook-demo` name; consider renaming later after confirming no scripts or local references depend on it.

## Current Structure

- `docs/registry-tree/`: Windows native registry tree entry point. It explains live roots such as `HKLM`, `HKCU`, `HKU`, `HKCR`, `HKCC`, and maps them back to offline hive files.
- `docs/questions/`: investigation scenario entry point. Pages are organized by real DFIR questions such as execution, persistence, USB, RDP, accounts, security policy, network configuration, software installation, anti-forensics, and Shell / Explorer behavior.
- `docs/artifacts/`: manually written artifact pages. Artifact pages should remain practical and evidence-oriented, not generic registry encyclopedia entries.
- `data/artifacts/`: structured artifact YAML records for future generated indexes and exports.
- `scripts/`: lightweight automation. `scripts/generate-artifact-index.py` reads `data/artifacts/*.yml` and writes `docs/artifacts/generated-index.md`.
- `mkdocs.yml`: site configuration and navigation. It currently includes the generated artifact data index in the Artifact section.
- `.github/workflows/pages.yml`: GitHub Actions workflow that builds and deploys the MkDocs site to GitHub Pages.

## Last Completed Round

- Cleaned the registry-tree navigation and registry-location content style.
- Removed `navigation.sections` in favor of expanded multi-level navigation so the registry tree reads more like a hierarchy and avoids duplicate root labels.
- Rewrote registry-tree pages as concise key/value reference pages. Registry-location pages should explain what keys and values mean, with only brief forensic notes; deeper evidence and detection discussion belongs in scenario and artifact pages.
- Updated `site_url` to the currently reachable custom-domain project path: `http://hsad.xyz/windows-registry-forensics-handbook/`.
- Added GitHub Pages deployment workflow at `.github/workflows/pages.yml`.
- Added `site_url`, `repo_name`, `repo_url`, and `edit_uri` to `mkdocs.yml`.
- Updated `README.md` with the online site URL and deployment workflow notes.
- GitHub Pages custom-domain project URL: `http://hsad.xyz/windows-registry-forensics-handbook/`.
- Default GitHub Pages project URL: `https://watanabe-hsad.github.io/windows-registry-forensics-handbook/`.
- Deployment source should be GitHub Actions. If first-time Pages setup is needed, use: `Settings -> Pages -> Build and deployment -> Source -> GitHub Actions`.
- The Pages deployment changes were committed and pushed to `origin/main`. The latest pushed branch should contain `.github/workflows/pages.yml`, the `mkdocs.yml` Pages metadata, and the README / handoff documentation updates.
- On each push to `main`, the workflow runs:

```bash
python scripts/generate-artifact-index.py
mkdocs build --strict
```

Previous completed round:

- Added missing YAML records for the previously existing artifact pages: UserAssist, Amcache, ShimCache / AppCompatCache, Services, IFEO, Terminal Server Client, USBSTOR, and MountedDevices.
- Added user behavior artifact pages and YAML: RunMRU, RecentDocs, OpenSavePidlMRU, LastVisitedPidlMRU.
- Added RDP server-side artifact pages and YAML: fDenyTSConnections, RDP-Tcp PortNumber, CredSSP / NLA.
- Added security policy artifact pages and YAML: UAC Policies, Firewall Policies, Audit Policy, SpecialAccounts\UserList.
- Updated `mkdocs.yml`, manual artifact index, generated artifact index, investigation scenario pages, detection page, and registry-tree pages so the new artifact pages are linked from both scenario and registry-location paths.
- YAML coverage is currently complete for manual artifact pages: 30 artifact pages under `docs/artifacts/` excluding `index.md` and `generated-index.md`, and 30 YAML records under `data/artifacts/`.
- Regenerated `docs/artifacts/generated-index.md` from YAML.

Earlier completed round:

- Added `PROJECT_STATUS.md`, `ROADMAP.md`, and `CHANGELOG.md` so future maintenance does not depend on chat history.
- Rewrote the README as a GitHub-ready project homepage and documented `License: TBD`.
- Initialized a local git repository on branch `main` and set `origin` to `https://github.com/watanabe-hsad/windows-registry-forensics-handbook.git`. The project has since been committed and pushed to `origin/main`.
- Deepened `HKEY_LOCAL_MACHINE`, `HKLM\SYSTEM`, `HKLM\SOFTWARE`, `HKEY_CURRENT_USER`, and `HKEY_USERS` with native/offline mapping, forensic role, detection role, timestamp caveats, common misinterpretations, high-value subkeys, linked artifacts, collection notes, and analyst checklists.
- Enhanced `scripts/generate-artifact-index.py` so it reads all `data/artifacts/*.yml` records and writes `docs/artifacts/generated-index.md`.
- Added `PyYAML` to `requirements.txt` and added the generated artifact data index to MkDocs navigation.

Earlier completed round:

- Replaced the old hive entry with a Windows native registry tree entry.
- Added registry-tree pages for `HKEY_CLASSES_ROOT`, `HKEY_CURRENT_USER`, `HKEY_LOCAL_MACHINE`, `HKEY_USERS`, `HKEY_CURRENT_CONFIG`, and HKLM subtrees.
- Added artifact pages for BAM / DAM, MUICache, StartupApproved, Winlogon Userinit, Winlogon Shell, LSA Authentication Packages, Command Processor AutoRun, MountPoints2, ProfileList, and Defender Policies.
- Expanded `data/artifacts/*.yml` structured records.
- Added scenario pages for accounts/security, policy/security, network, software install, anti-forensics, and Shell / Explorer user behavior.

## Important Decisions

- Keep the two primary user entries: investigation scenarios and the Windows native registry tree.
- Keep the site knowledge-base oriented. Prefer concise, objective reference text over subjective prose.
- Registry-tree pages should stay clean: path, source hive, key/value meaning, short caveats, and linked artifacts.
- Artifact pages must use a fixed evidence-oriented template.
- Evidence semantics come first: `What It Can Prove` and `What It Cannot Prove` must remain separate.
- Timestamp interpretation must stay conservative. Do not treat key LastWrite as the creation time of a specific value.
- Mapping relationships must be explicit and accurate: `HKCU` maps to `HKU\<SID>`, `HKCR` is a merged classes view, `HKCC` maps into `SYSTEM` hardware profiles, and `CurrentControlSet` is a runtime mapping resolved through `HKLM\SYSTEM\Select`.
- YAML structured artifact data must be preserved and extended. It is the source for generated indexes and future exports.
- Do not overwrite manually curated indexes such as `docs/artifacts/index.md` with generated output.

## Verification

Last verified locally in the most recent round:

```bash
.venv/bin/python scripts/generate-artifact-index.py
.venv/bin/mkdocs build --strict
```

Both commands completed successfully. The Material for MkDocs upstream warning about MkDocs 2.0 appeared during build and is expected; it is not currently a project build error.

Remote verification was also performed with `git ls-remote origin refs/heads/main`; the remote `main` hash matched local `HEAD` after the Pages and handoff updates were pushed.

## Next Priorities

- Confirm GitHub Pages settings in the repository UI if the first workflow run does not publish: `Settings -> Pages -> Build and deployment -> Source -> GitHub Actions`.
- If a shorter URL is desired, use a project custom domain such as `registry.hsad.xyz` or move the site to the apex/root domain. The current `/windows-registry-forensics-handbook/` suffix is expected for a GitHub Pages project site.
- Choose a license and add a `LICENSE` file. Suggested split: docs under `CC BY 4.0`, scripts under `MIT`, or a simpler single-repo `MIT` if preferred.
- Add persistence pages for AppInit_DLLs, Active Setup, ShellServiceObjectDelayLoad, Print Monitors, LSA Security Packages, Services DLL details, and Drivers.
- Add USB and device pages for USB, DeviceClasses, Enum\SWD\WPDBUSENUM, EMDMgmt, Portable Devices, and VolumeInfoCache.
- Add account/security pages for CachedLogonsCount, LogonUI, local group membership details, and SAM user record interpretation.
- Add network/system pages for NetworkList, Tcpip Interfaces, Internet Settings proxy, ZoneMap, TimeZoneInformation, ComputerName, and Select / ControlSet.
- Add detection mapping fields such as ATT&CK technique, common event IDs, Sigma-friendly registry path selectors, and known false-positive families.
- Add contribution and citation guidance before public release.
- Decide on license and add a `LICENSE` file.
- Consider renaming the local directory from `registry-forensics-handbook-demo` to `windows-registry-forensics-handbook` after confirming local tooling will not break.

## Notes For Next Agent

- This directory is now initialized as a git repository with `origin` set to `https://github.com/watanabe-hsad/windows-registry-forensics-handbook.git`.
- Current branch is `main` tracking `origin/main`.
- GitHub Pages deployment is configured through `.github/workflows/pages.yml`.
- The user explicitly allowed commit and push for GitHub Pages setup in this round, and the Pages configuration has been pushed to GitHub.
- Preserve `site/` as ignored generated output.
- Prefer small content increments with strict build validation.
- If changing generated artifact index behavior, update this file and `CHANGELOG.md`.
