# Roadmap

## Phase 1: Core Structure

- Keep the homepage as a dual entry point: investigation scenarios and Windows native registry tree.
- Keep MkDocs Material configuration simple and avoid heavy theme customization.
- Maintain a consistent artifact page template with evidence semantics, timestamp notes, detection ideas, false positives, collection, tooling, and cross validation.
- Keep `data/artifacts/*.yml` alongside manual pages for structured future use.

## Phase 2: Registry Tree Depth

- Current status: registry-location navigation now follows a Windows-registry-like hierarchy instead of investigation themes.
- Completed path-reference pages: `HKLM\SYSTEM\Select`, `ControlSet00x`, `Services`, `Enum`, `MountedDevices`, `Terminal Server`, `Tcpip`, `TimeZoneInformation`, `ComputerName`, and `Lsa`.
- Completed path-reference pages: `HKLM\SOFTWARE\ProfileList`, `Winlogon`, `Image File Execution Options`, `Policies`, `Windows Defender`, `Uninstall`, `WOW6432Node`, and `Classes`.
- Completed path-reference pages: HKCU Explorer, ComDlg32, RunMRU, RecentDocs, Internet Settings, Classes, Terminal Server Client, plus HKU `.DEFAULT` and service-account SID pages.
- Completed path-reference pages: device-specific pages for USB, DeviceClasses, `SWD\WPDBUSENUM`, EMDMgmt, Portable Devices, and VolumeInfoCache.
- Completed path-reference pages: persistence/load-chain pages for Active Setup, AppInit_DLLs, ShellServiceObjectDelayLoad, Print Monitors, LSA Security Packages, and driver service entries.
- Next: add HKCU ZoneMap, Printers, Environment, user-level Run / Command Processor, and network profile pages.

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
