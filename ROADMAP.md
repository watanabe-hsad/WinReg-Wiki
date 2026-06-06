# Roadmap

Current project name: `WinReg Wiki`.

## Phase 1: Core Structure

- Keep the homepage as a compact Wiki entry page.
- Keep top-level navigation limited to `首页`, `注册表位置`, and `取证场景`.
- Keep MkDocs Material configuration simple and avoid heavy theme customization.
- Treat registry-location pages and scenario pages as the two primary reader entry points.
- Keep artifact pages as supplemental detail for evidence semantics, timestamp notes, detection ideas, false positives, collection, tooling, and cross validation.
- Keep `data/artifacts/*.yml` alongside manual pages for structured future use.

## Phase 2: Registry Tree Depth

- Current status: registry-location navigation uses section index pages and follows a Windows-registry-like hierarchy instead of investigation themes.
- Current status: `docs/registry-tree/coverage.md` tracks covered, to-deepen, and planned registry locations by root key and topic.
- Current status: visible `概览` child items have been removed from registry-location navigation.
- Completed path-reference pages: `HKLM\SYSTEM\Select`, `ControlSet00x`, `Services`, `Enum`, `MountedDevices`, `Terminal Server`, `Tcpip`, `TimeZoneInformation`, `ComputerName`, and `Lsa`.
- Completed path-reference pages: `HKLM\SOFTWARE\ProfileList`, `Winlogon`, `Image File Execution Options`, `Policies`, `Windows Defender`, `Uninstall`, `WOW6432Node`, and `Classes`.
- Completed path-reference pages: HKCU Explorer, ComDlg32, RunMRU, RecentDocs, Internet Settings, Classes, Terminal Server Client, plus HKU `.DEFAULT` and service-account SID pages.
- Completed path-reference pages: device-specific pages for USB, DeviceClasses, `SWD\WPDBUSENUM`, EMDMgmt, Portable Devices, and VolumeInfoCache.
- Completed path-reference pages: persistence/load-chain pages for Active Setup, AppInit_DLLs, ShellServiceObjectDelayLoad, Print Monitors, LSA Security Packages, and driver service entries.
- Completed path-reference pages added for the registry-first scenario rewrite: HKLM Run / RunOnce, HKCU Run / RunOnce, UserAssist, MountPoints2, and USBSTOR.
- Completed path-reference pages for the registry-tree expansion:
  - `HKCU\Environment`
  - `HKCU\Printers`
  - `HKCU\Software\Microsoft\Command Processor`
  - `HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap`
  - `HKLM\SYSTEM\ControlSet00x\Services\EventLog`
  - `HKLM\SYSTEM\ControlSet00x\Services\SharedAccess\Parameters\FirewallPolicy`
  - `HKLM\SOFTWARE\Microsoft\Windows Defender`
  - `HKLM\SOFTWARE\Policies\Microsoft\Windows Defender`
  - `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Profiles`
  - `HKLM\SYSTEM\ControlSet00x\Services\Tcpip\Parameters\Interfaces`
  - `HKLM\SYSTEM\ControlSet00x\Control\Session Manager\Environment`
- Completed follow-up path-reference pages:
  - `HKLM\SOFTWARE\Microsoft\Command Processor`
  - `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths`
  - `HKLM\SOFTWARE\Policies\Microsoft\WindowsFirewall`
  - `HKLM\SYSTEM\ControlSet00x\Control\Session Manager`
  - `HKLM\SYSTEM\ControlSet00x\Control\Session Manager\BootExecute`
  - `HKLM\SYSTEM\ControlSet00x\Control\Session Manager\KnownDLLs`
  - `HKLM\SYSTEM\ControlSet00x\Control\Session Manager\PendingFileRenameOperations`
- Completed login/policy/execution reference pages:
  - `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Authentication\LogonUI`
  - `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System`
  - `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\Notify`
  - `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AeDebug`
  - `HKLM\SYSTEM\ControlSet00x\Control\Session Manager\AppCertDlls`
  - `HKCU\Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags`
- Completed RDP/account reference pages:
  - `HKLM\SYSTEM\ControlSet00x\Control\Terminal Server\WinStations\RDP-Tcp`
  - `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\CredSSP`
  - `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\CachedLogonsCount`
  - `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Authentication\Credential Providers`
  - `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\UserList`
- Completed registry-tree normalization pass:
  - remaining artifact-link section headings in registry-location pages were renamed to `## 补充阅读`;
  - scan now returns no registry-tree hits for old artifact-template headings or subjective priority phrases.
- Completed follow-up reference pages:
  - `HKLM\SYSTEM\ControlSet00x\Control\Session Manager\SubSystems`
  - `HKLM\SYSTEM\ControlSet00x\Control\Session Manager\Memory Management`
  - `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags`
  - `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Layers`
  - `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Authentication\Credential Provider Filters`
  - `HKCU\Software\Microsoft\Windows\CurrentVersion\Policies`
  - `HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer`
- Next: use the coverage matrix to add or deepen `HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System`, `Attachments`, `Associations`, Explorer `Advanced`, Explorer `TypedPaths`, ShellBags / BagMRU, `Enum\STORAGE`, and `DeviceContainers`.

## Phase 3: High-Value Artifacts

- Completed in current content set: RunMRU, RecentDocs, OpenSavePidlMRU, LastVisitedPidlMRU.
- Add remaining execution and user-behavior pages: ShellBags, AppCompatFlags Compatibility Assistant Store, RunMRU variants if OS differences require separate notes.
- Completed persistence pages: Active Setup, AppInit_DLLs, ShellServiceObjectDelayLoad, Print Monitors, LSA Security Packages, and Drivers.
- Completed USB and device pages: USB, DeviceClasses, Enum\SWD\WPDBUSENUM, EMDMgmt, Portable Devices, and VolumeInfoCache.
- Add remaining persistence pages: App Paths, KnownDLLs, Winlogon Notify, BootExecute, AppCompatFlags Compatibility Assistant Store, Services DLL details, and WMI-related registry locations if evidence-backed.
- Add remaining USB/device pages: deeper USBSTOR instance interpretation, `Enum\STORAGE`, DeviceContainers, device install properties, and per-user ShellBags/MountPoints2 variants.
- Completed in current content set: fDenyTSConnections, RDP-Tcp PortNumber, CredSSP / NLA.
- Add remaining RDP and remote access pages: Remote Assistance, RD Gateway / client cache if registry-backed evidence is identified.
- Completed in current content set: UAC Policies, Audit Policy, Firewall Policies, SpecialAccounts\UserList.
- Add remaining security and policy pages: CachedLogonsCount, LogonUI, local group membership details, SAM user record interpretation.

## Phase 4: Structured Data and Generated Indexes

- Current status: every manual artifact page currently has a matching YAML record; after the USB/device and persistence expansion this is 42 artifact pages and 42 YAML records.
- Current status: generated artifact index display is localized to Chinese while preserving YAML field names.
- Current status: `data/registry/` MVP is established with 10 registry-location YAML records.
- Current status: `scripts/generate-registry-index.py` generates `docs/registry-tree/generated-index.md` and `docs/registry-tree/coverage.md` without overwriting manual registry-location pages.
- Current status: core artifact YAML records can link back to registry entries via `registry_entry_ids`.
- Current status: `docs/contributing/registry-data-schema.md` documents the registry YAML field model and the relationship between registry data and artifact data.
- Keep `scripts/generate-artifact-index.py` small and dependency-light.
- Generate `docs/artifacts/generated-index.md` from YAML without overwriting manual narrative indexes.
- Next: expand registry YAML coverage to about 30 core pages before adding more generated index views.
- Next: continue building artifact-to-registry relationships with `registry_entry_ids`.
- Next: add stable fields for ATT&CK mappings, event IDs, collection commands, parser support, and confidence levels only when the page set is ready.
- Consider exporting JSON later only if a real consumer appears.

## Phase 5: Detection Mappings and Tool Integration

- Current status: scenario pages now link primarily to registry-location pages and keep artifact links as supplemental reading.
- Current status: `docs/detection/index.md` now links detection entry rows primarily to registry-location pages instead of artifact pages.
- Current status: `取证场景 / 常规注册表检查` provides the first cross-scenario registry checklist.
- Current status: `registry-checklist`, `network`, `policy-security`, `persistence`, `anti-forensics`, and `execution` now link to the latest registry-location pages before artifact supplements.
- Current status: `command-processor-autorun`, `defender-policies`, `firewall-policies`, `audit-policy`, `run-keys`, and `services` artifact pages have been compressed into supplemental entries.
- Current status: `drivers`, `appinit-dlls`, and `ifeo` artifact pages have also been compressed into supplemental entries.
- Current status: `winlogon-userinit`, `winlogon-shell`, `uac-policies`, `specialaccounts-userlist`, `profilelist`, and `terminal-server-client` artifact pages have also been compressed into supplemental entries.
- Current status: `fdenytsconnections`, `rdp-tcp-portnumber`, and `credssp-nla` artifact pages have also been compressed into supplemental entries.
- Add Sigma-friendly registry path selectors for high-value persistence and policy weakening keys.
- Add Sysmon, Security.evtx, Defender, TerminalServices, PowerShell, and EDR telemetry references per artifact.
- Add Velociraptor and KAPE collection notes where useful.
- Build detection-engineering pages around evidence combinations instead of raw path matches.
- Add false-positive families for enterprise software, EDR, VPN, VDI, backup, database, and management tooling.

## Phase 6: Publishing and Contribution Workflow

- Current status: repository metadata and GitHub remote point to `watanabe-hsad/WinReg-Wiki`.
- Current status: contribution guidance and source-quality expectations live in `docs/contributing/index.md`.
- Current status: CI runs artifact index generation, registry index generation, content style check, generated-file diff check, and `mkdocs build --strict`.
- Current status: README, generated registry indexes, registry-tree coverage, and contribution docs document the v0.1 content model.
- Current status: Visual UX Redesign is complete for the search-first homepage, Registry Explorer entry, scenario-card directory, registry checklist dashboard, generated registry index, coverage matrix, and high-visible Registry Fact Cards.
- Current status: desktop, narrow/mobile, and dark-mode previews were checked locally with MkDocs serve; generated and checklist tables use container-level horizontal scrolling on narrow screens.
- Next UI: refine search behavior when Material exposes a cleaner programmatic search trigger, add more topic-specific generated sections after registry YAML coverage expands, and consider a small screenshot set after the final production URL is confirmed.
- Add `LICENSE` after the maintainer chooses a license.
- Confirm GitHub Pages / custom domain target before changing `site_url`. Candidate paths: `https://hsad.xyz/winreg/` or `https://winreg.hsad.xyz/`.
- Review homepage, navigation, and first-visit experience once the final URL is confirmed.
- Next: prepare a `v0.1` tag after URL and License decisions are made.
