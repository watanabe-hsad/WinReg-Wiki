# HKCU\Software

`HKCU\Software` 保存当前用户的软件、应用和部分系统组件配置。

## 文件

| Live 视图 | 离线文件 |
|---|---|
| `HKCU\Software` / `HKU\<SID>\Software` | `C:\Users\<user>\NTUSER.DAT` |

## 常用路径

| 路径 | 含义 |
|---|---|
| [`Microsoft\Windows\CurrentVersion\Run`](microsoft/windows/currentversion/run.md) | 用户级登录启动项。 |
| `Microsoft\Command Processor` | `cmd.exe` 的 `AutoRun` 配置。 |
| [`Microsoft\Terminal Server Client`](microsoft/terminal-server-client.md) | RDP 客户端历史。 |
| [`Microsoft\Windows\CurrentVersion\Explorer`](microsoft/windows/currentversion/explorer.md) | Explorer / Shell 相关用户痕迹。 |
| [`Microsoft\Windows\CurrentVersion\Explorer\UserAssist`](microsoft/windows/currentversion/userassist.md) | Explorer 相关程序交互记录。 |
| [`Microsoft\Windows\CurrentVersion\Explorer\RunMRU`](microsoft/windows/currentversion/runmru.md) | Win+R 输入历史。 |
| [`Microsoft\Windows\CurrentVersion\Explorer\RecentDocs`](microsoft/windows/currentversion/recentdocs.md) | 最近文档名称和 MRU。 |
| [`Microsoft\Windows\CurrentVersion\Explorer\ComDlg32`](microsoft/windows/currentversion/comdlg32.md) | Common dialog MRU。 |
| [`Microsoft\Windows\CurrentVersion\Explorer\MountPoints2`](microsoft/windows/currentversion/mountpoints2.md) | 用户见过的卷、盘符和网络共享。 |
| [`Microsoft\Windows\CurrentVersion\Internet Settings`](microsoft/windows/currentversion/internet-settings.md) | 用户代理、PAC、ZoneMap、WinINet 设置。 |
| [`Classes`](classes.md) | 用户级 Classes，通常来自 `UsrClass.dat`。 |

## 注意

| 项 | 说明 |
|---|---|
| 用户归属 | 先通过 `ProfileList` 确认 SID 到 profile 的映射。 |
| live 查询 | `HKCU` 取决于运行命令的用户上下文。 |
| 配置残留 | 用户配置存在不等于近期使用。 |

## 相关场景

- [自启动与持久化](../../../questions/persistence.md)
- [Shell / Explorer 用户行为](../../../questions/shell-explorer.md)
- [常规注册表检查](../../../questions/registry-checklist.md)

## 补充阅读

[Run / RunOnce](../../../artifacts/persistence/run-keys.md),
[Command Processor AutoRun](../../../artifacts/persistence/command-processor-autorun.md),
[Terminal Server Client](../../../artifacts/rdp/terminal-server-client.md),
[MountPoints2](../../../artifacts/usb/mountpoints2.md)
