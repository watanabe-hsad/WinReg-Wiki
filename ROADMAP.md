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
- Next: add or deepen `Session Manager\SubSystems`, `Session Manager\Memory Management`, machine-level `AppCompatFlags`, `Terminal Server\WinStations\RDP-Tcp`, Credential Providers, CachedLogonsCount, and additional HKCU network / shell policy locations.

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
- Keep `scripts/generate-artifact-index.py` small and dependency-light.
- Generate `docs/artifacts/generated-index.md` from YAML without overwriting manual narrative indexes.
- Add stable fields for ATT&CK mappings, event IDs, collection commands, parser support, and confidence levels.
- Consider exporting JSON later only if a real consumer appears.

## Phase 5: Detection Mappings and Tool Integration

- Current status: scenario pages now link primarily to registry-location pages and keep artifact links as supplemental reading.
- Current status: `取证场景 / 常规注册表检查` provides the first cross-scenario registry checklist.
- Current status: `registry-checklist`, `network`, `policy-security`, `persistence`, `anti-forensics`, and `execution` now link to the latest registry-location pages before artifact supplements.
- Current status: `command-processor-autorun`, `defender-policies`, `firewall-policies`, `audit-policy`, `run-keys`, and `services` artifact pages have been compressed into supplemental entries.
- Current status: `drivers`, `appinit-dlls`, and `ifeo` artifact pages have also been compressed into supplemental entries.
- Current status: `winlogon-userinit`, `winlogon-shell`, `uac-policies`, `specialaccounts-userlist`, `profilelist`, and `terminal-server-client` artifact pages have also been compressed into supplemental entries.
- Add Sigma-friendly registry path selectors for high-value persistence and policy weakening keys.
- Add Sysmon, Security.evtx, Defender, TerminalServices, PowerShell, and EDR telemetry references per artifact.
- Add Velociraptor and KAPE collection notes where useful.
- Build detection-engineering pages around evidence combinations instead of raw path matches.
- Add false-positive families for enterprise software, EDR, VPN, VDI, backup, database, and management tooling.

## Phase 6: Publishing and Contribution Workflow

- Finalize repository metadata and GitHub remote.
- Add `LICENSE` after the maintainer chooses a license.
- Add contribution guidance and citation/source-quality expectations.
- Add lightweight CI for `mkdocs build --strict` and generated index freshness.
- Review README, homepage, navigation, and first-visit experience before publishing.
- Tag a first release only after content and license are ready.
