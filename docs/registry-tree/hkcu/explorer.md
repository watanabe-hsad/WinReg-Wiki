# HKCU Explorer

`HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer` 聚合了大量用户 Shell 行为线索。它不是单个 artifact，而是一组用于还原用户交互、文件访问、设备访问和启动项状态的入口。

## Windows 原生视图

Live 路径为 `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer`。离线时从目标用户 `NTUSER.DAT` 的同名子路径读取。

## 离线 hive 文件来源

| 逻辑路径 | 离线文件 |
|---|---|
| `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer` | `C:\Users\<user>\NTUSER.DAT` |
| ShellBags / Classes 相关用户级视图 | `C:\Users\<user>\AppData\Local\Microsoft\Windows\UsrClass.dat` |

## 典型取证价值

- 用户是否通过 Explorer 触发程序、打开文件、访问目录、见过外接卷或网络位置。
- 与 LNK、Jump Lists、RecentDocs、ShellBags 共同建立用户行为时间线。

## 典型检测价值

- 监控 StartupApproved 禁用状态被绕过、用户级启动项变化。
- 发现用户与可疑路径、可移动介质、远程共享之间的交互线索。

## 常见误判

- Explorer 自动枚举、预览、文件对话框和应用调用也会产生痕迹。
- 这些 artifact 多数不能单独证明文件内容被读取或程序完整执行。
- key LastWrite 可能只表示容器更新，不等于某个条目的精确创建时间。

## 重点子路径

| 子路径 | 价值 | 相关 artifact |
|---|---|---|
| `UserAssist\{GUID}\Count` | Explorer 交互程序痕迹 | [UserAssist](../../artifacts/execution/userassist.md) |
| `RunMRU` | Win+R / Run 对话框输入 | [RunMRU](../../artifacts/user-activity/runmru.md) |
| `RecentDocs` | 最近文档类型和名称线索 | [RecentDocs](../../artifacts/user-activity/recentdocs.md) |
| `ComDlg32\OpenSavePidlMRU` | 文件打开/保存对话框路径线索 | [OpenSavePidlMRU](../../artifacts/user-activity/opensavepidlmru.md) |
| `ComDlg32\LastVisitedPidlMRU` | 应用程序与最近访问目录关系 | [LastVisitedPidlMRU](../../artifacts/user-activity/lastvisitedpidlmru.md) |
| `MountPoints2` | 用户见过的卷和网络位置 | [MountPoints2](../../artifacts/usb/mountpoints2.md) |
| `StartupApproved` | 启动项启停状态 | [StartupApproved](../../artifacts/persistence/startupapproved.md) |

## 关联 artifact 页面

- [UserAssist](../../artifacts/execution/userassist.md)
- [MUICache](../../artifacts/execution/muicache.md)
- [RunMRU](../../artifacts/user-activity/runmru.md)
- [RecentDocs](../../artifacts/user-activity/recentdocs.md)
- [OpenSavePidlMRU](../../artifacts/user-activity/opensavepidlmru.md)
- [LastVisitedPidlMRU](../../artifacts/user-activity/lastvisitedpidlmru.md)
- [MountPoints2](../../artifacts/usb/mountpoints2.md)
- [StartupApproved](../../artifacts/persistence/startupapproved.md)
