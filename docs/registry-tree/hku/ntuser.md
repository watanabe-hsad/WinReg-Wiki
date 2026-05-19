# NTUSER.DAT

`NTUSER.DAT` 是用户主 hive 文件，加载后通常显示为 `HKU\<SID>`，当前登录用户再映射为 `HKCU`。它是用户行为、用户级持久化和应用配置调查的核心文件。

## Windows 原生视图

Live 视图为 `HKU\<SID>` 或 `HKCU`。同一台机器上每个用户通常都有自己的 `NTUSER.DAT`。

## 离线 hive 文件来源

| 文件 | 路径 |
|---|---|
| `NTUSER.DAT` | `C:\Users\<user>\NTUSER.DAT` |
| transaction logs | `NTUSER.DAT.LOG1`、`NTUSER.DAT.LOG2` |

## 典型取证价值

- 用户级 Run、UserAssist、RunMRU、RecentDocs、MountPoints2、RDP Client、Internet Settings。
- 把行为线索归属到具体 SID，并与文件系统、日志和用户会话时间线结合。

## 典型检测价值

- 批量扫描所有用户 hive 的自启动、代理、RDP 和 Shell 行为。
- 发现只影响单个用户的低权限持久化。

## 常见误判

- `NTUSER.DAT` 的文件时间戳不是某个内部 artifact 的活动时间。
- 用户 hive 可被系统后台加载，不能把加载时间等同于用户登录。
- hive transaction log 可能影响最终解析结果。

## 重点子路径

| 子路径 | 价值 | 相关 artifact |
|---|---|---|
| `Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist` | 用户交互程序线索 | [UserAssist](../../artifacts/execution/userassist.md) |
| `Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU` | Run dialog 输入历史 | [RunMRU](../../artifacts/user-activity/runmru.md) |
| `Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs` | 最近文档名称和扩展名线索 | [RecentDocs](../../artifacts/user-activity/recentdocs.md) |
| `Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePidlMRU` | 文件对话框路径线索 | [OpenSavePidlMRU](../../artifacts/user-activity/opensavepidlmru.md) |
| `Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\LastVisitedPidlMRU` | 应用与目录关系 | [LastVisitedPidlMRU](../../artifacts/user-activity/lastvisitedpidlmru.md) |
| `Software\Microsoft\Windows\CurrentVersion\Explorer\MountPoints2` | 用户见过的卷和共享 | [MountPoints2](../../artifacts/usb/mountpoints2.md) |
| `Software\Microsoft\Terminal Server Client` | RDP 客户端目标 | [Terminal Server Client](../../artifacts/rdp/terminal-server-client.md) |
| `Software\Microsoft\Command Processor` | cmd 自动执行 | [Command Processor AutoRun](../../artifacts/persistence/command-processor-autorun.md) |

## 关联 artifact 页面

- [Run / RunOnce](../../artifacts/persistence/run-keys.md)
- [RunMRU](../../artifacts/user-activity/runmru.md)
- [RecentDocs](../../artifacts/user-activity/recentdocs.md)
- [OpenSavePidlMRU](../../artifacts/user-activity/opensavepidlmru.md)
- [LastVisitedPidlMRU](../../artifacts/user-activity/lastvisitedpidlmru.md)
- [StartupApproved](../../artifacts/persistence/startupapproved.md)
- [MountPoints2](../../artifacts/usb/mountpoints2.md)
