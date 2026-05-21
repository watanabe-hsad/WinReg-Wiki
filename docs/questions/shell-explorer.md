# Shell / Explorer 用户行为

## 检查目标

判断某个用户是否在 Shell / Explorer 环境中见过程序、文件、目录、卷、网络共享或 Run dialog 输入。

## 优先查看的注册表位置

| 注册表位置 | 用途 | 判断边界 |
|---|---|---|
| [HKCU Explorer](../registry-tree/hkcu/software/microsoft/windows/currentversion/explorer.md) | Shell 用户行为入口。 | 需要继续展开具体子键。 |
| [UserAssist](../registry-tree/hkcu/software/microsoft/windows/currentversion/userassist.md) | Explorer 相关程序交互。 | 不覆盖所有执行方式。 |
| [RunMRU](../registry-tree/hkcu/software/microsoft/windows/currentversion/runmru.md) | Win+R 输入历史。 | 输入不等于命令执行成功。 |
| [RecentDocs](../registry-tree/hkcu/software/microsoft/windows/currentversion/recentdocs.md) | 最近文档名称和扩展名分组。 | 文件名出现不等于内容被读取。 |
| [ComDlg32](../registry-tree/hkcu/software/microsoft/windows/currentversion/comdlg32.md) | 打开 / 保存对话框 MRU。 | PIDL 解析结果需结合应用和文件系统。 |
| [MountPoints2](../registry-tree/hkcu/software/microsoft/windows/currentversion/mountpoints2.md) | 用户见过的卷、盘符或网络共享。 | 不证明文件复制或文件访问。 |
| [UsrClass.dat](../registry-tree/hku/usrclass.md) | 用户级 Classes / Shell 相关 hive。 | ShellBags、MUICache 等还需专门解析。 |

## 判断要点

- 先用 `ProfileList` 映射 SID，再解释对应用户的 `NTUSER.DAT` 和 `UsrClass.dat`。
- RunMRU 出现 `cmd`、`powershell`、UNC 路径或内部工具命令时，需结合进程日志和 Prefetch。
- RecentDocs、ComDlg32、LNK、Jump Lists 同时指向同一文件或目录时，用户行为判断更稳。
- MountPoints2 与 MountedDevices、USBSTOR、LNK 关联时，可把设备或共享归属到用户。

## 交叉验证

- LNK、Jump Lists、ShellBags、RecentDocs、OpenSavePidlMRU、LastVisitedPidlMRU。
- Prefetch、BAM / DAM、Amcache、ShimCache、Sysmon、EDR。
- `$MFT`、`$UsnJrnl`、文件访问审计、下载记录。
- 用户登录、锁屏/解锁、RDP 会话、交互式会话日志。

## 常见误判

- Shell 记录常说明“见过 / 交互过 / 浏览过”，不等于文件内容被阅读。
- 文件对话框 MRU 可能由打开或保存动作产生，需要结合应用上下文。
- 网络共享和 USB 卷可能由 Explorer 预览、自动播放或同步软件更新记录。

## 相关场景

- [程序执行痕迹](execution.md)
- [USB 与外接设备](usb.md)
- [常规注册表检查](registry-checklist.md)

## 补充阅读

- [UserAssist artifact](../artifacts/execution/userassist.md)
- [RunMRU artifact](../artifacts/user-activity/runmru.md)
- [RecentDocs artifact](../artifacts/user-activity/recentdocs.md)
- [OpenSavePidlMRU artifact](../artifacts/user-activity/opensavepidlmru.md)
- [MountPoints2 artifact](../artifacts/usb/mountpoints2.md)
