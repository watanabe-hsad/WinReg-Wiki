# NTUSER.DAT

`NTUSER.DAT` 是用户主 hive，加载后通常显示为 `HKU\<SID>`，当前用户再映射为 `HKCU`。

## 文件

| 项 | 路径 |
|---|---|
| Hive | `C:\Users\<user>\NTUSER.DAT` |
| Transaction logs | `NTUSER.DAT.LOG1`, `NTUSER.DAT.LOG2` |

## 常用路径

| 路径 | 含义 |
|---|---|
| `Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist` | Explorer 相关程序交互。 |
| `Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU` | Run dialog 输入历史。 |
| `Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs` | 最近文档记录。 |
| `Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32` | 打开 / 保存对话框 MRU。 |
| `Software\Microsoft\Windows\CurrentVersion\Explorer\MountPoints2` | 用户见过的卷和共享。 |
| `Software\Microsoft\Terminal Server Client` | RDP 客户端历史。 |
| `Software\Microsoft\Windows\CurrentVersion\Run` | 用户级启动项。 |
| `Software\Microsoft\Command Processor` | `cmd.exe` AutoRun。 |

## 注意

| 项 | 说明 |
|---|---|
| 用户归属 | 通过 `ProfileList` 确认 SID。 |
| hive 时间 | 文件时间戳不等于内部 artifact 活动时间。 |
| 加载状态 | hive 可被后台加载，不等于用户正在登录。 |

## 补充阅读

[UserAssist](../../artifacts/execution/userassist.md),
[RunMRU](../../artifacts/user-activity/runmru.md),
[RecentDocs](../../artifacts/user-activity/recentdocs.md),
[OpenSavePidlMRU](../../artifacts/user-activity/opensavepidlmru.md),
[LastVisitedPidlMRU](../../artifacts/user-activity/lastvisitedpidlmru.md),
[Terminal Server Client](../../artifacts/rdp/terminal-server-client.md)
