# HKCU\Software

`HKCU\Software` 是用户级应用配置和行为 artifact 的主入口。离线分析时它对应目标用户 `NTUSER.DAT` 中的 `Software` 子树。

## Windows 原生视图

Live 系统中路径为 `HKCU\Software`。注意命令运行身份：以管理员或服务账户运行时，`HKCU` 可能不是被调查用户。

## 离线 hive 文件来源

| 逻辑路径 | 离线文件 |
|---|---|
| `HKCU\Software` / `HKU\<SID>\Software` | `C:\Users\<user>\NTUSER.DAT` |

## 典型取证价值

- 用户级自启动、RDP 历史、Explorer 行为、代理设置、应用配置。
- 将行为归属到具体 SID，而不是仅证明机器上存在痕迹。

## 典型检测价值

- 监控用户级 Run key、Command Processor AutoRun、Internet Settings、ZoneMap、Terminal Server Client。
- 针对非管理员写入高风险用户级持久化做狩猎。

## 常见误判

- 多用户机器上只加载当前用户 hive 会漏掉其他用户。
- 用户配置残留不等于近期使用。
- GPO 或应用同步可能自动写入部分用户配置。

## 重点子路径

| 子路径 | 价值 | 相关 artifact |
|---|---|---|
| `Microsoft\Windows\CurrentVersion\Run` | 用户级登录启动 | [Run / RunOnce](../../artifacts/persistence/run-keys.md) |
| `Microsoft\Command Processor` | cmd 自动执行命令 | [Command Processor AutoRun](../../artifacts/persistence/command-processor-autorun.md) |
| `Microsoft\Terminal Server Client` | RDP 客户端目标 | [Terminal Server Client](../../artifacts/rdp/terminal-server-client.md) |
| `Microsoft\Windows\CurrentVersion\Explorer` | Shell / Explorer 行为 | [HKCU Explorer](explorer.md) |
| `Microsoft\Windows\CurrentVersion\Internet Settings` | 代理与区域配置 | 网络调查 |

## 关联 artifact 页面

- [MUICache](../../artifacts/execution/muicache.md)
- [MountPoints2](../../artifacts/usb/mountpoints2.md)
- [StartupApproved](../../artifacts/persistence/startupapproved.md)
