# HKCU\Software

`HKCU\Software` 保存当前用户的软件、应用和部分系统组件配置。

## 文件

| Live 视图 | 离线文件 |
|---|---|
| `HKCU\Software` / `HKU\<SID>\Software` | `C:\Users\<user>\NTUSER.DAT` |

## 常用路径

| 路径 | 含义 |
|---|---|
| `Microsoft\Windows\CurrentVersion\Run` | 用户级登录启动项。 |
| `Microsoft\Command Processor` | `cmd.exe` 的 `AutoRun` 配置。 |
| `Microsoft\Terminal Server Client` | RDP 客户端历史。 |
| `Microsoft\Windows\CurrentVersion\Explorer` | Explorer / Shell 相关用户痕迹。 |
| `Microsoft\Windows\CurrentVersion\Internet Settings` | 用户代理、PAC、ZoneMap、WinINet 设置。 |
| `Classes` | 用户级 Classes，通常来自 `UsrClass.dat`。 |

## 注意

| 项 | 说明 |
|---|---|
| 用户归属 | 先通过 `ProfileList` 确认 SID 到 profile 的映射。 |
| live 查询 | `HKCU` 取决于运行命令的用户上下文。 |
| 配置残留 | 用户配置存在不等于近期使用。 |

## 相关 Artifact

[Run / RunOnce](../../artifacts/persistence/run-keys.md),
[Command Processor AutoRun](../../artifacts/persistence/command-processor-autorun.md),
[Terminal Server Client](../../artifacts/rdp/terminal-server-client.md),
[MountPoints2](../../artifacts/usb/mountpoints2.md)
