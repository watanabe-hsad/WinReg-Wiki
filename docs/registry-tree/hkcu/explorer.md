# HKCU Explorer

`HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer` 是 Explorer / Shell 用户痕迹的主要入口。

## 文件

| Live 视图 | 离线文件 |
|---|---|
| `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer` | `C:\Users\<user>\NTUSER.DAT` |
| ShellBags / Classes 相关内容 | `C:\Users\<user>\AppData\Local\Microsoft\Windows\UsrClass.dat` |

## 常用路径

| 路径 | 含义 |
|---|---|
| `UserAssist\{GUID}\Count` | Explorer 相关程序交互记录。 |
| `RunMRU` | Win+R 输入历史。 |
| `RecentDocs` | 最近文档名称和扩展名分组。 |
| `ComDlg32\OpenSavePidlMRU` | 打开 / 保存对话框中的路径和文件线索。 |
| `ComDlg32\LastVisitedPidlMRU` | 应用程序与最近访问目录关系。 |
| `MountPoints2` | 用户见过的卷、盘符、网络共享。 |
| `StartupApproved` | 启动项启停状态。 |

## 注意

| 项 | 说明 |
|---|---|
| 自动产生 | Explorer、文件对话框、应用调用都可能写入相关键。 |
| 文件打开 | RecentDocs / MRU 是线索，不直接等于文件内容被读取。 |
| 时间戳 | key LastWrite 是容器更新时间，不是单条记录的精确创建时间。 |

## 相关 Artifact

[UserAssist](../../artifacts/execution/userassist.md),
[RunMRU](../../artifacts/user-activity/runmru.md),
[RecentDocs](../../artifacts/user-activity/recentdocs.md),
[OpenSavePidlMRU](../../artifacts/user-activity/opensavepidlmru.md),
[LastVisitedPidlMRU](../../artifacts/user-activity/lastvisitedpidlmru.md),
[MountPoints2](../../artifacts/usb/mountpoints2.md),
[StartupApproved](../../artifacts/persistence/startupapproved.md)
