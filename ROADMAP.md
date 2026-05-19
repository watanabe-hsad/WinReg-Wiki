# Roadmap

## Phase 1: Core Structure

- Keep the homepage as a dual entry point: investigation scenarios and Windows native registry tree.
- Keep MkDocs Material configuration simple and avoid heavy theme customization.
- Maintain a consistent artifact page template with evidence semantics, timestamp notes, detection ideas, false positives, collection, tooling, and cross validation.
- Keep `data/artifacts/*.yml` alongside manual pages for structured future use.

## Phase 2: Registry Tree Depth

- Deepen `HKLM\SYSTEM` with ControlSet, Services, Enum, USB, MountedDevices, RDP server configuration, network interfaces, time zone, and computer name analysis.
- Deepen `HKLM\SOFTWARE` with Run / RunOnce, Uninstall, IFEO, Winlogon, Explorer, Defender, Policies, Classes, and WOW6432Node.
- Deepen `HKCU` and `HKU\<SID>` with user hive mapping, Explorer behavior, RunMRU, RecentDocs, ComDlg32, RDP client history, Environment, user-level persistence, `NTUSER.DAT`, and `UsrClass.dat`.
- Add practical analyst checklists to major registry tree pages.

## Phase 3: High-Value Artifacts

- Completed in current content set: RunMRU, RecentDocs, OpenSavePidlMRU, LastVisitedPidlMRU.
- Add remaining execution and user-behavior pages: ShellBags, AppCompatFlags Compatibility Assistant Store, RunMRU variants if OS differences require separate notes.
- Add persistence pages: AppInit_DLLs, Active Setup, ShellServiceObjectDelayLoad, Print Monitors, LSA Security Packages, Services DLL details, Drivers.
- Add USB and device pages: USB, DeviceClasses, Enum\SWD\WPDBUSENUM, EMDMgmt, Portable Devices, VolumeInfoCache.
- Completed in current content set: fDenyTSConnections, RDP-Tcp PortNumber, CredSSP / NLA.
- Add remaining RDP and remote access pages: Remote Assistance, RD Gateway / client cache if registry-backed evidence is identified.
- Completed in current content set: UAC Policies, Audit Policy, Firewall Policies, SpecialAccounts\UserList.
- Add remaining security and policy pages: CachedLogonsCount, LogonUI, local group membership details, SAM user record interpretation.

## Phase 4: Structured Data and Generated Indexes

- Current status: every manual artifact page currently has a matching YAML record.
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
