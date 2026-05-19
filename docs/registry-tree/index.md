# 注册表位置

这个入口按 Windows 原生注册表树组织，只做路径和含义速查。更完整的证据解释、检测思路和交叉验证放在 [调查场景](../questions/index.md) 与 [Artifact](../artifacts/index.md) 入口中。

## 根键速查

| 根键 | 含义 | 离线来源 |
|---|---|---|
| [HKEY_CLASSES_ROOT](hkey-classes-root.md) | 文件关联、COM、协议处理器的合并视图。 | `SOFTWARE\Classes` + 用户 `UsrClass.dat` |
| [HKEY_CURRENT_USER](hkey-current-user.md) | 当前用户配置，映射到 `HKEY_USERS\<SID>`。 | 用户 `NTUSER.DAT`，部分内容来自 `UsrClass.dat` |
| [HKEY_LOCAL_MACHINE](hkey-local-machine.md) | 机器级配置和系统数据库。 | `SAM`、`SECURITY`、`SOFTWARE`、`SYSTEM`、`BCD` |
| [HKEY_USERS](hkey-users.md) | 已加载用户 hive 和默认用户配置。 | 多个用户 `NTUSER.DAT` / `UsrClass.dat` |
| [HKEY_CURRENT_CONFIG](hkey-current-config.md) | 当前硬件配置映射。 | `SYSTEM` 中的 Hardware Profiles |

## HKLM 子树

| 子树 | 文件或来源 | 主要内容 |
|---|---|---|
| [SAM](hklm/sam.md) | `C:\Windows\System32\Config\SAM` | 本地账户、RID、组关系。 |
| [SECURITY](hklm/security.md) | `C:\Windows\System32\Config\SECURITY` | LSA、审计策略、安全策略。 |
| [SOFTWARE](hklm/software.md) | `C:\Windows\System32\Config\SOFTWARE` | 软件、策略、ProfileList、Winlogon、Defender、Classes。 |
| [SYSTEM](hklm/system.md) | `C:\Windows\System32\Config\SYSTEM` | ControlSet、服务、驱动、设备、网络、RDP 服务端。 |
| [HARDWARE](hklm/hardware.md) | 运行时生成 | 当前硬件枚举。 |
| [BCD00000000](hklm/bcd.md) | `\Boot\BCD` 或 EFI 分区 BCD | 启动配置数据库。 |

## 用户相关位置

| 位置 | 含义 |
|---|---|
| [HKCU\Software](hkcu/software.md) | 当前用户软件和应用配置。 |
| [HKCU Explorer](hkcu/explorer.md) | Explorer、Shell、MRU、RecentDocs、UserAssist 等用户痕迹入口。 |
| [Terminal Server Client](hkcu/terminal-server-client.md) | MSTSC 客户端连接历史。 |
| [SID 映射](hku/sid-mapping.md) | `ProfileList` 中 SID 到用户目录的映射。 |
| [NTUSER.DAT](hku/ntuser.md) | 用户级配置 hive。 |
| [UsrClass.dat](hku/usrclass.md) | 用户级 Classes、ShellBags、COM、MUI Cache 等。 |

## 读路径时先确认

| 问题 | 原因 |
|---|---|
| `HKCU` 对应哪个 SID？ | live 环境下 `HKCU` 取决于当前进程上下文。 |
| `CurrentControlSet` 对应哪个 `ControlSet00x`？ | 离线分析时要先读 `SYSTEM\Select`。 |
| `HKCR` 来自机器级还是用户级？ | `HKCR` 是 `HKLM\Software\Classes` 与 `HKCU\Software\Classes` 的合并视图。 |
| 是否存在 32 位视图？ | 64 位 Windows 上部分键会落在 `WOW6432Node`。 |
