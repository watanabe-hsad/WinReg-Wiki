# HKEY_CURRENT_USER

`HKEY_CURRENT_USER` 是当前进程安全上下文对应用户在 `HKEY_USERS\<SID>` 下的运行时映射。它是用户行为、用户级持久化、RDP 客户端历史、Shell 痕迹和用户偏好调查的主要入口。

## Native Registry View

Live 系统中路径为：

```text
HKCU
```

但 `HKCU` 不是独立 hive。它指向：

```text
HKU\<current-user-SID>
```

以管理员、远程管理工具、服务账户或 SYSTEM 上下文运行命令时，`HKCU` 可能不是被调查用户。任何 live collection 都要记录执行上下文。

## Offline Hive Source

| Live view | Offline file | Typical contents |
|---|---|---|
| `HKCU` / `HKU\<SID>` | `C:\Users\<user>\NTUSER.DAT` | Explorer 行为、RunMRU、RecentDocs、RDP Client、用户级 Run、Environment、Internet Settings。 |
| `HKCU\Software\Classes` / `HKU\<SID>_Classes` | `C:\Users\<user>\AppData\Local\Microsoft\Windows\UsrClass.dat` | 用户级 Classes、ShellBags、COM、MUI Cache 相关数据。 |

离线分析时，先用 [ProfileList](../artifacts/security/profilelist.md) 把 SID 映射到 `ProfileImagePath`，再把该用户的 `NTUSER.DAT` 和 `UsrClass.dat` 放到同一用户时间线中。

## Forensic Role

`HKCU` 主要回答“某个用户上下文中发生过或配置过什么”：

- 用户行为：Explorer、UserAssist、RunMRU、RecentDocs、OpenSavePidlMRU、MountPoints2。
- 用户级持久化：Run / RunOnce、Command Processor AutoRun、用户级 Winlogon Shell、StartupApproved。
- RDP 客户端：Terminal Server Client 目标、用户名提示。
- Shell 痕迹：RecentDocs、file dialog MRU、ShellBags、MUI Cache。
- 用户环境：Environment、Internet Settings、Proxy、ZoneMap、应用偏好。

HKCU 证据更适合做用户归属，但多数 Shell artifact 仍是“用户交互线索”，不能单独证明文件读取、数据外传或恶意意图。

## Detection Role

用户级检测重点包括：

- `Software\Microsoft\Windows\CurrentVersion\Run`、`RunOnce`。
- `Software\Microsoft\Command Processor\AutoRun`。
- `Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved`。
- `Software\Microsoft\Terminal Server Client` 新增异常目标。
- `Internet Settings` 中代理、PAC、ZoneMap 异常。
- Explorer MRU 中出现敏感文件名、攻击工具路径、未知共享或可移动卷。

用户级路径适合 hunting 低权限持久化和横向移动前的操作者痕迹。

## Timestamp Caveats

- `HKCU` live view 没有告诉你真实离线文件路径；报告应写 SID 和 hive 文件。
- Explorer MRU、RecentDocs、RunMRU、MountPoints2 的 key LastWrite 不等于单个条目的精确创建时间。
- 用户 hive 文件时间戳不等于用户登录时间；hive 可被后台服务加载。
- `NTUSER.DAT` 与 `UsrClass.dat` 是不同文件，时间线和 artifact 语义不能混用。

## Common Misinterpretations

| Misinterpretation | Safer interpretation |
|---|---|
| 查到 `HKCU` 就等于目标用户 | 先确认命令运行上下文；离线报告写 `HKU\<SID>` 和 ProfileList 映射。 |
| UserAssist 就能证明用户双击执行 | 它提示 Explorer 相关交互执行，启动方式和完整执行链需验证。 |
| RecentDocs 就能证明文件被打开阅读 | 它是最近文档线索；内容访问需 LNK、Jump Lists、应用日志、文件审计等。 |
| MountPoints2 就能证明 USB 文件复制 | 它证明用户 Shell 见过卷或共享；复制需文件系统或 EDR 证据。 |
| HKCU Run key 存在就说明程序已自启动 | 它证明配置存在；执行需登录和进程证据。 |

## High-Value Subkeys

| Subkey | What to look for | Linked artifacts / scenarios |
|---|---|---|
| `Software\Microsoft\Windows\CurrentVersion\Explorer` | Shell / Explorer 行为总入口。 | [HKCU Explorer](hkcu/explorer.md) |
| `Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist` | Explorer 相关程序交互执行线索。 | [UserAssist](../artifacts/execution/userassist.md) |
| `Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU` | Win+R / Run 对话框输入历史。 | [RunMRU](../artifacts/user-activity/runmru.md) |
| `Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs` | 最近文档名称、扩展名和用户活动线索。 | [RecentDocs](../artifacts/user-activity/recentdocs.md) |
| `Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePidlMRU` | 文件打开/保存对话框路径和文件名线索。 | [OpenSavePidlMRU](../artifacts/user-activity/opensavepidlmru.md) |
| `Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\LastVisitedPidlMRU` | 应用与最后访问目录关系。 | [LastVisitedPidlMRU](../artifacts/user-activity/lastvisitedpidlmru.md) |
| `Software\Microsoft\Windows\CurrentVersion\Explorer\MountPoints2` | 用户见过的卷、盘符、网络共享。 | [MountPoints2](../artifacts/usb/mountpoints2.md) |
| `Software\Microsoft\Terminal Server Client` | RDP 客户端目标和用户名提示。 | [Terminal Server Client](../artifacts/rdp/terminal-server-client.md) |
| `Software\Microsoft\Windows\CurrentVersion\Run` | 用户级登录启动项。 | [Run / RunOnce](../artifacts/persistence/run-keys.md) |
| `Software\Microsoft\Command Processor` | `AutoRun`，cmd.exe 启动钩子。 | [Command Processor AutoRun](../artifacts/persistence/command-processor-autorun.md) |
| `Environment` | 用户级环境变量，可能影响执行链和 PATH hijack。 | 持久化 / 执行调查 |
| `Software\Microsoft\Windows\CurrentVersion\Internet Settings` | Proxy、PAC、ZoneMap、WinINet 配置。 | [网络与系统环境](../questions/network.md) |
| `Software\Classes` | 用户级 Classes / COM / 文件关联，通常由 `UsrClass.dat` 支撑。 | [UsrClass.dat](hku/usrclass.md), [MUICache](../artifacts/execution/muicache.md) |

## Linked Artifacts

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
- [ProfileList](../artifacts/security/profilelist.md)

## Collection Notes

=== "Live"

    ```cmd
    whoami /user
    reg query HKCU
    reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer" /s
    reg query "HKCU\Software\Microsoft\Terminal Server Client" /s
    reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Run"
    ```

=== "Offline"

    ```text
    1. Load SOFTWARE and parse ProfileList.
    2. Map SID -> ProfileImagePath.
    3. Collect:
       C:\Users\<user>\NTUSER.DAT
       C:\Users\<user>\NTUSER.DAT.LOG1 / LOG2
       C:\Users\<user>\AppData\Local\Microsoft\Windows\UsrClass.dat
       UsrClass.dat.LOG1 / LOG2
    4. Report findings as HKU\<SID>, not generic HKCU.
    ```

## Analyst Checklist

- Confirm which SID `HKCU` represents before interpreting any live output.
- Map the SID to profile path with [ProfileList](../artifacts/security/profilelist.md).
- Separate `NTUSER.DAT` artifacts from `UsrClass.dat` artifacts.
- For user behavior, look for at least two independent sources before claiming a user opened or executed something.
- For user-level persistence, check Run key, StartupApproved, Command Processor AutoRun, Startup Folder, and scheduled tasks.
- For RDP client history, separate client-side target history from server-side logon evidence.
- Normalize paths and account for deleted profiles, renamed directories, domain accounts, and temporary profiles.

## References

- [Microsoft Learn: Registry hives](https://learn.microsoft.com/en-us/windows/win32/sysinfo/registry-hives)
- [Microsoft Learn: Predefined keys](https://learn.microsoft.com/en-us/windows/win32/sysinfo/predefined-keys)
