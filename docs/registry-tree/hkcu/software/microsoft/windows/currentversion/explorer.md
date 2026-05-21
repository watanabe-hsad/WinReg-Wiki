# HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer

`Explorer` 保存当前用户 Shell / Explorer 相关配置和多类用户级 MRU 入口。

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer` |
| 离线 | `NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer` |

## 常见子键 / value

| 名称 | 类型 | 含义 |
|---|---|---|
| [`UserAssist\{GUID}\Count`](userassist.md) | Key | Explorer 相关程序交互记录。 |
| [`RunMRU`](runmru.md) | Key | Win+R Run dialog 输入历史。 |
| [`RecentDocs`](recentdocs.md) | Key | 最近文档名称和扩展名分组。 |
| [`ComDlg32`](comdlg32.md) | Key | 打开 / 保存对话框 MRU。 |
| [`MountPoints2`](mountpoints2.md) | Key | 用户见过的卷、盘符和网络共享。 |
| `StartupApproved` | Key | 启动项启用 / 禁用状态。 |

## 说明

| 项 | 内容 |
|---|---|
| 数据来源 | 用户 `NTUSER.DAT`。 |
| 常见写入者 | Explorer、Shell、文件对话框、应用程序调用。 |
| 注意 | 这些 key 多数是用户行为线索；条目存在不等于文件被读取、程序执行成功或设备发生文件复制。 |

## 相关场景

- [Shell / Explorer 用户行为](../../../../../../questions/shell-explorer.md)
- [程序执行痕迹](../../../../../../questions/execution.md)
- [USB 与外接设备](../../../../../../questions/usb.md)
- [常规注册表检查](../../../../../../questions/registry-checklist.md)

## 补充阅读

- [UserAssist](../../../../../../artifacts/execution/userassist.md)
- [RunMRU](../../../../../../artifacts/user-activity/runmru.md)
- [RecentDocs](../../../../../../artifacts/user-activity/recentdocs.md)
- [OpenSavePidlMRU](../../../../../../artifacts/user-activity/opensavepidlmru.md)
- [LastVisitedPidlMRU](../../../../../../artifacts/user-activity/lastvisitedpidlmru.md)
- [MountPoints2](../../../../../../artifacts/usb/mountpoints2.md)
