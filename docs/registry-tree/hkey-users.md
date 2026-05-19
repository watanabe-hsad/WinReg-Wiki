# HKEY_USERS

`HKEY_USERS` 展示当前系统已加载的用户 hive，是多用户分析、SID 归属、`.DEFAULT` 区分和用户级 artifact 批量比较的核心入口。

## Native Registry View

Live 系统中常见子键包括：

```text
HKU\.DEFAULT
HKU\S-1-5-18
HKU\S-1-5-19
HKU\S-1-5-20
HKU\S-1-5-21-...\<RID>
HKU\S-1-5-21-...\<RID>_Classes
```

`HKCU` 是其中某个 `HKU\<SID>` 的运行时映射。`HKU\<SID>_Classes` 通常对应用户 `UsrClass.dat`。Live 系统只显示已加载 hive，未登录用户不一定出现在 `HKU` 中。

## Offline Hive Source

| Live key | Offline source | Notes |
|---|---|---|
| `HKU\<SID>` | `C:\Users\<user>\NTUSER.DAT` | 用户主 hive，包含 Explorer、Run、RDP Client、Internet Settings 等。 |
| `HKU\<SID>_Classes` | `C:\Users\<user>\AppData\Local\Microsoft\Windows\UsrClass.dat` | 用户 Classes / Shell 数据，参与 `HKCU\Software\Classes` 和 `HKCR` 合并视图。 |
| `HKU\.DEFAULT` | `C:\Windows\System32\Config\DEFAULT` | 系统默认配置，通常不是普通用户活动历史。 |

SID 到用户目录的权威映射优先来自：

```text
HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList\<SID>\ProfileImagePath
```

见 [ProfileList](../artifacts/security/profilelist.md)。

## Forensic Role

`HKU` 的核心价值是防止把不同用户混在一起：

- 多用户机器上，同一 artifact 可能在多个 SID 中存在，含义和时间线不同。
- `.DEFAULT`、SYSTEM、LOCAL SERVICE、NETWORK SERVICE 与普通用户 hive 不能混用。
- 域账户、本地账户、服务账户、临时 profile 和删除用户残留都可能留下不同形态的 hive。
- `NTUSER.DAT` 与 `UsrClass.dat` 分工不同，必须按文件解释 artifact。

## Detection Role

检测和 hunting 中，`HKU` 适合做横向枚举：

- 扫描所有用户的 Run key、Command Processor AutoRun、Terminal Server Client、Internet Settings。
- 比较每个 SID 的 Explorer MRU、MountPoints2、UserAssist、RecentDocs。
- 搜索用户级 COM / protocol hijack：`HKU\<SID>_Classes\CLSID`、`shell\open\command`。
- 发现隐藏账户、新 profile、临时 profile 或异常 profile 路径。

## Timestamp Caveats

- `HKU` live view 是否显示某个 SID，取决于 hive 是否加载，不等于用户是否当前登录。
- `.DEFAULT` key 时间不代表普通用户行为。
- `NTUSER.DAT` 和 `UsrClass.dat` 文件时间戳不等于内部 artifact 时间。
- `ProfileList` key LastWrite 不等于用户首次或最后登录时间。
- 删除账户后，ProfileList、用户目录和 hive 文件可能继续残留。

## Common Misinterpretations

| Misinterpretation | Safer interpretation |
|---|---|
| `.DEFAULT` 是默认用户或最近登录用户 | `.DEFAULT` 通常是系统默认配置，不是普通用户活动历史。 |
| `HKU` 中没有某 SID 就说明用户不存在 | 未加载 hive 不会显示；离线要查 ProfileList 和用户目录。 |
| `C:\Users\alice` 就一定是 alice 当前账户 | 目录名可重命名或残留；以 SID 和 ProfileList 为准。 |
| 域账户一定在 SAM 中有本地账户记录 | 域账户 profile 可存在，但本地 SAM 不一定有对应用户。 |
| `_Classes` 和主 SID hive 可以混为一谈 | `_Classes` 通常来自 `UsrClass.dat`，证据语义不同。 |

## High-Value Subkeys

| Subkey | What to look for | Linked artifacts / pages |
|---|---|---|
| `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList` | SID 到 profile 目录映射。 | [ProfileList](../artifacts/security/profilelist.md) |
| `HKU\<SID>\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist` | 用户交互执行线索。 | [UserAssist](../artifacts/execution/userassist.md) |
| `HKU\<SID>\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU` | Run 对话框输入历史。 | [RunMRU](../artifacts/user-activity/runmru.md) |
| `HKU\<SID>\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs` | 最近文档线索。 | [RecentDocs](../artifacts/user-activity/recentdocs.md) |
| `HKU\<SID>\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePidlMRU` | 文件对话框打开/保存路径线索。 | [OpenSavePidlMRU](../artifacts/user-activity/opensavepidlmru.md) |
| `HKU\<SID>\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\LastVisitedPidlMRU` | 应用与最近访问目录关系。 | [LastVisitedPidlMRU](../artifacts/user-activity/lastvisitedpidlmru.md) |
| `HKU\<SID>\Software\Microsoft\Windows\CurrentVersion\Explorer\MountPoints2` | 用户见过的卷和共享。 | [MountPoints2](../artifacts/usb/mountpoints2.md) |
| `HKU\<SID>\Software\Microsoft\Terminal Server Client` | RDP 客户端目标。 | [Terminal Server Client](../artifacts/rdp/terminal-server-client.md) |
| `HKU\<SID>\Software\Microsoft\Windows\CurrentVersion\Run` | 用户级登录启动项。 | [Run / RunOnce](../artifacts/persistence/run-keys.md) |
| `HKU\<SID>\Software\Microsoft\Command Processor` | cmd AutoRun 用户级持久化。 | [Command Processor AutoRun](../artifacts/persistence/command-processor-autorun.md) |
| `HKU\<SID>_Classes\Local Settings\Software\Microsoft\Windows\Shell\MuiCache` | 程序路径和显示名缓存。 | [MUICache](../artifacts/execution/muicache.md) |
| `HKU\<SID>_Classes\CLSID` | 用户级 COM hijack。 | [UsrClass.dat](hku/usrclass.md) |
| `HKU\.DEFAULT` | 系统默认用户配置，通常用于系统上下文。 | 谨慎解释，不要归属普通用户。 |

## Linked Artifacts

- [ProfileList](../artifacts/security/profilelist.md)
- [UserAssist](../artifacts/execution/userassist.md)
- [MUICache](../artifacts/execution/muicache.md)
- [RunMRU](../artifacts/user-activity/runmru.md)
- [RecentDocs](../artifacts/user-activity/recentdocs.md)
- [OpenSavePidlMRU](../artifacts/user-activity/opensavepidlmru.md)
- [LastVisitedPidlMRU](../artifacts/user-activity/lastvisitedpidlmru.md)
- [Run / RunOnce](../artifacts/persistence/run-keys.md)
- [StartupApproved](../artifacts/persistence/startupapproved.md)
- [Command Processor AutoRun](../artifacts/persistence/command-processor-autorun.md)
- [MountPoints2](../artifacts/usb/mountpoints2.md)
- [Terminal Server Client](../artifacts/rdp/terminal-server-client.md)
- [SID 映射](hku/sid-mapping.md)
- [NTUSER.DAT](hku/ntuser.md)
- [UsrClass.dat](hku/usrclass.md)

## Collection Notes

=== "Live"

    ```cmd
    reg query HKU
    reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList" /s
    whoami /user
    ```

=== "Offline"

    ```text
    1. Collect SOFTWARE hive and parse ProfileList.
    2. For each relevant SID, collect:
       C:\Users\<user>\NTUSER.DAT
       C:\Users\<user>\NTUSER.DAT.LOG1 / LOG2
       C:\Users\<user>\AppData\Local\Microsoft\Windows\UsrClass.dat
       UsrClass.dat.LOG1 / LOG2
    3. Keep a SID -> profile path -> hive file mapping table in notes.
    ```

## Analyst Checklist

- Build a SID mapping table before reading user artifact output.
- Separate local users, domain users, service accounts, system accounts, temporary profiles, and deleted profile remnants.
- Do not attribute `.DEFAULT` to a human user.
- For each artifact, record which hive file produced it: `NTUSER.DAT` or `UsrClass.dat`.
- Compare the same path across all users to identify outliers.
- Use Security.evtx, User Profile Service logs, SAM, domain logs, and file system timelines to validate account existence and login activity.
- When reporting `HKCU`, rewrite it as `HKU\<SID>` plus profile path for offline evidence.

## References

- [Microsoft Learn: Registry hives](https://learn.microsoft.com/en-us/windows/win32/sysinfo/registry-hives)
- [Microsoft Learn: Predefined keys](https://learn.microsoft.com/en-us/windows/win32/sysinfo/predefined-keys)
