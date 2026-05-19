# HKEY_CURRENT_USER

`HKEY_CURRENT_USER`，简称 `HKCU`，是当前用户在 `HKEY_USERS\<SID>` 下的映射。它不是独立 hive。

## 映射关系

| Live 视图 | 实际位置 | 离线文件 |
|---|---|---|
| `HKCU` | `HKU\<current-user-SID>` | `C:\Users\<user>\NTUSER.DAT` |
| `HKCU\Software\Classes` | `HKU\<SID>_Classes` | `C:\Users\<user>\AppData\Local\Microsoft\Windows\UsrClass.dat` |

live 查询时，`HKCU` 取决于命令运行上下文。以管理员、服务账户或 `SYSTEM` 运行时，`HKCU` 可能不是目标用户。

## 常用路径

| 路径 | 含义 |
|---|---|
| [HKCU\Software](hkcu/software.md) | 用户软件和应用配置入口。 |
| [`Software\Microsoft\Windows\CurrentVersion\Explorer`](hkcu/explorer.md) | Explorer / Shell 用户行为入口。 |
| `Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist` | Explorer 相关程序交互记录。 |
| [`Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU`](hkcu/software/runmru.md) | Win+R 输入历史。 |
| [`Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs`](hkcu/software/recentdocs.md) | 最近文档记录。 |
| [`Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32`](hkcu/software/comdlg32.md) | 打开 / 保存对话框 MRU。 |
| `Software\Microsoft\Windows\CurrentVersion\Explorer\MountPoints2` | 用户见过的卷、盘符、网络共享。 |
| [`Software\Microsoft\Terminal Server Client`](hkcu/terminal-server-client.md) | MSTSC 客户端连接历史。 |
| `Software\Microsoft\Windows\CurrentVersion\Run` | 用户级登录启动项。 |
| `Software\Microsoft\Command Processor` | `cmd.exe` 的 `AutoRun` 配置。 |
| `Environment` | 用户级环境变量。 |
| [`Software\Microsoft\Windows\CurrentVersion\Internet Settings`](hkcu/software/internet-settings.md) | 用户代理、PAC、ZoneMap、WinINet 设置。 |

## 注意

| 项 | 说明 |
|---|---|
| 用户归属 | 报告中尽量写 `HKU\<SID>` 和 profile 路径，不只写 `HKCU`。 |
| `NTUSER.DAT` | 用户级配置和大量用户行为痕迹。 |
| `UsrClass.dat` | 用户级 Classes、ShellBags、COM、MUICache 等。 |
| 时间戳 | key LastWrite 是 key 级更新时间，不等于某个 value 的创建时间。 |

## 相关 Artifact

[UserAssist](../artifacts/execution/userassist.md),
[RunMRU](../artifacts/user-activity/runmru.md),
[RecentDocs](../artifacts/user-activity/recentdocs.md),
[OpenSavePidlMRU](../artifacts/user-activity/opensavepidlmru.md),
[LastVisitedPidlMRU](../artifacts/user-activity/lastvisitedpidlmru.md),
[Run / RunOnce](../artifacts/persistence/run-keys.md),
[MountPoints2](../artifacts/usb/mountpoints2.md),
[Terminal Server Client](../artifacts/rdp/terminal-server-client.md)
