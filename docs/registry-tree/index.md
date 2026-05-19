# 按注册表位置查

这个入口按 Windows 原生注册表树组织。调查时先区分“live 逻辑视图”和“离线 hive 文件”：`HKCU`、`HKCR`、`HKCC` 都不是单独的离线文件，直接把它们当作 hive 会导致用户归属、优先级和时间线判断错误。

| 原生根键 | Live 视图含义 | 离线分析入口 | 代表价值 |
|---|---|---|---|
| [HKEY_CLASSES_ROOT](hkey-classes-root.md) | `HKLM\Software\Classes` 与 `HKCU\Software\Classes` 的合并视图 | `SOFTWARE` + 用户 `UsrClass.dat` / `HKU\<SID>_Classes` | 文件关联、COM、协议处理器、MUI Cache |
| [HKEY_CURRENT_USER](hkey-current-user.md) | 当前登录用户在 `HKEY_USERS\<SID>` 下的映射 | `C:\Users\<user>\NTUSER.DAT`，以及用户 `UsrClass.dat` | 用户交互、Explorer、RDP 客户端、用户级持久化 |
| [HKEY_LOCAL_MACHINE](hkey-local-machine.md) | 本机级配置与安全数据库 | `SAM`、`SECURITY`、`SOFTWARE`、`SYSTEM`、`BCD` 等 | 服务、驱动、策略、账户、设备、网络、启动配置 |
| [HKEY_USERS](hkey-users.md) | 已加载用户 hive 与默认配置 | 多个用户 `NTUSER.DAT`、`UsrClass.dat`、`.DEFAULT` | 多用户归属、SID 映射、用户级 artifact 批量比较 |
| [HKEY_CURRENT_CONFIG](hkey-current-config.md) | 当前硬件配置映射 | 通常回到 `SYSTEM` hive 的 Hardware Profiles | 当前硬件 profile、显示和设备配置线索 |

## HKLM 子树

| 子树 | 离线文件 | 优先关注 |
|---|---|---|
| [HKLM\SAM](hklm/sam.md) | `C:\Windows\System32\Config\SAM` | 本地账户 RID、状态、组关系 |
| [HKLM\SECURITY](hklm/security.md) | `C:\Windows\System32\Config\SECURITY` | LSA Secrets、安全策略、审计策略 |
| [HKLM\SOFTWARE](hklm/software.md) | `C:\Windows\System32\Config\SOFTWARE` | 软件、策略、ProfileList、Winlogon、Defender |
| [HKLM\SYSTEM](hklm/system.md) | `C:\Windows\System32\Config\SYSTEM` | ControlSet、服务、驱动、设备、网络、BAM/DAM |
| [HKLM\HARDWARE](hklm/hardware.md) | 通常为运行时生成 | 当前硬件枚举，离线价值有限 |
| [HKLM\BCD00000000](hklm/bcd.md) | `\Boot\BCD` 或 EFI 分区 BCD | 启动项、启动调试、恢复配置 |

## 用户 hive 速查

| 位置 | 说明 | 相关页面 |
|---|---|---|
| `HKCU\Software` | 当前用户配置主入口 | [HKCU\Software](hkcu/software.md) |
| `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer` | Shell / Explorer 用户行为 | [HKCU Explorer](hkcu/explorer.md) |
| `HKCU\Software\Microsoft\Terminal Server Client` | MSTSC 客户端历史 | [Terminal Server Client](hkcu/terminal-server-client.md) |
| `HKU\<SID>` | 用户 SID 到 profile 的映射结果 | [SID 映射](hku/sid-mapping.md) |
| `HKU\<SID>` 对应文件 | `NTUSER.DAT` | [NTUSER.DAT](hku/ntuser.md) |
| `HKU\<SID>_Classes` 对应文件 | `UsrClass.dat` | [UsrClass.dat](hku/usrclass.md) |

!!! tip "离线分析最小上下文"
    记录每个 hive 的原始文件路径、挂载名称、用户 SID、`ProfileList` 映射、工具版本和解析时间。报告中写 `HKCU` 时，应说明它对应哪个用户 SID，而不是只写“当前用户”。
