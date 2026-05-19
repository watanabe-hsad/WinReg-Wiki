# HKEY_LOCAL_MACHINE

`HKEY_LOCAL_MACHINE` 是机器级注册表视图，覆盖本地账户、安全策略、软件配置、服务驱动、设备枚举、网络、启动和部分安全产品策略。它常用于回答“这台机器被怎样配置过”和“哪些机器级配置有机会影响所有用户”。

## Native Registry View

在 `regedit.exe` 中从 `HKEY_LOCAL_MACHINE` 展开。常见子树包括：

- `HKLM\SAM`
- `HKLM\SECURITY`
- `HKLM\SOFTWARE`
- `HKLM\SYSTEM`
- `HKLM\HARDWARE`
- `HKLM\BCD00000000`

`CurrentControlSet` 是 `HKLM\SYSTEM` 下的运行时映射，不是离线 hive 中稳定存在的真实 key。离线分析必须先读 `HKLM\SYSTEM\Select`，再决定当前控制集对应哪个 `ControlSet00x`。

## Offline Hive Source

| Native subtree | Offline source | DFIR notes |
|---|---|---|
| `HKLM\SAM` | `C:\Windows\System32\Config\SAM` | 本地账户、组、RID、账户状态。常与 Security.evtx 和 [ProfileList](../artifacts/security/profilelist.md) 交叉验证。 |
| `HKLM\SECURITY` | `C:\Windows\System32\Config\SECURITY` | LSA Secrets、审计策略和安全策略。很多字段需要专用 parser。 |
| `HKLM\SOFTWARE` | `C:\Windows\System32\Config\SOFTWARE` | 软件、策略、Winlogon、IFEO、Defender、ProfileList、32 位视图。 |
| `HKLM\SYSTEM` | `C:\Windows\System32\Config\SYSTEM` | ControlSet、服务、驱动、设备、USB、网络、RDP 服务端、LSA 运行配置。 |
| `HKLM\HARDWARE` | 运行时生成 | 通常没有独立持久 hive，离线调查回到 `SYSTEM` 的 `Enum`、`Services` 和 Hardware Profiles。 |
| `HKLM\BCD00000000` | `\Boot\BCD` 或 EFI 分区 `\EFI\Microsoft\Boot\BCD` | 启动配置数据库，不在 `System32\Config` 常规 hive 集合内。 |

采集机器级 hive 时，尽量同时保留 `.LOG1`、`.LOG2` 和原始路径。后续工具可能使用 transaction logs 恢复尚未合并的状态。

## Forensic Role

`HKLM` 的核心取证价值是证明机器级配置存在，并把它放回系统上下文中解释：

- 服务、驱动、Winlogon、LSA、IFEO、Run key 等配置能说明持久化机会点。
- `SYSTEM` 中的设备枚举、USB、MountedDevices、网络接口和 RDP 服务端配置能说明机器状态和外设/网络环境。
- `SOFTWARE` 中的 ProfileList、Defender、Policies、Uninstall、WOW6432Node 能说明用户映射、软件、策略和安全控制。
- `SAM` 和 `SECURITY` 能辅助账户、权限、审计和凭据风险调查。

`HKLM` 证明的通常是“机器级配置或数据库状态”，不是“某个用户一定执行了某行为”。用户行为仍要回到 `HKCU` / `HKU\<SID>`、事件日志和文件系统时间线。

## Detection Role

检测工程中，`HKLM` 是高信号 registry telemetry 的主要来源：

- 持久化：`Services`、Drivers、Winlogon、IFEO、LSA、Run / RunOnce、Print Monitors。
- 防御规避：Defender exclusions、Firewall policies、UAC、Audit Policy、Tamper Protection 相关配置。
- 远程访问：RDP 允许状态、RDP 端口、Remote Assistance、WinRM / 服务配置。
- 系统环境：DNS、接口、代理、时区、ComputerName、ControlSet。

规则不应只做“路径命中”。更高信号的组合是：敏感 HKLM 路径被写入 + 写入进程异常 + value data 指向用户可写目录或脚本解释器 + 时间线中出现登录、重启、网络连接或 payload 落地。

## Timestamp Caveats

- 注册表 key LastWrite 是 key 级时间，不能直接解释为某个 value 的创建时间。
- `HKLM\SYSTEM\CurrentControlSet` 在 live 系统可用，离线报告应写实际 `ControlSet00x`。
- `SAM`、`SECURITY` 中很多字段是二进制结构，工具输出的时间字段必须标注 parser 和版本。
- 策略类 key 的 LastWrite 不等于策略生效时间；GPO、MDM、Defender、EDR 可能异步下发或阻止变更。
- `HARDWARE` 是运行时视图，不能用于单独证明历史设备连接。

## Common Misinterpretations

| Misinterpretation | Safer interpretation |
|---|---|
| `ControlSet001` 就是当前控制集 | 先读 `SYSTEM\Select\Current`，再映射到对应 `ControlSet00x`。 |
| HKLM 中出现配置就说明恶意执行过 | HKLM 多数只能证明配置存在；执行要用进程、登录、模块加载、Prefetch、BAM 等证据。 |
| Defender policy 值存在就说明 Defender 已关闭 | 新平台和 Tamper Protection 可能阻止或忽略某些值；需验证 Defender 状态和 Operational 日志。 |
| Services 中服务存在就说明服务成功启动 | 需要 Service Control Manager、Sysmon、进程或服务状态证据。 |
| ProfileList 里有用户目录就说明用户近期登录 | ProfileList 是映射记录；近期登录要查 Security.evtx 和 User Profile Service。 |

## High-Value Subkeys

| Subkey | Why it matters | Linked artifacts / pages |
|---|---|---|
| `SAM\SAM\Domains\Account\Users` | 本地账户 RID、状态、组关系调查入口。 | [HKLM\SAM](hklm/sam.md) |
| `SECURITY\Policy` | 审计策略、LSA Secrets、安全策略。 | [HKLM\SECURITY](hklm/security.md) |
| `SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList` | SID 到 profile 目录映射，是用户级证据归属基础。 | [ProfileList](../artifacts/security/profilelist.md) |
| `SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon` | 登录链和 Shell 配置，高价值持久化点。 | [Winlogon Userinit](../artifacts/persistence/winlogon-userinit.md), [Winlogon Shell](../artifacts/persistence/winlogon-shell.md) |
| `SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options` | Debugger 劫持和执行链干预。 | [IFEO](../artifacts/persistence/ifeo.md) |
| `SOFTWARE\Policies\Microsoft\Windows Defender` | Defender 策略、排除项、防护削弱。 | [Defender Policies](../artifacts/security/defender-policies.md) |
| `SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System` | UAC 和远程本地账户 token 过滤策略。 | [UAC Policies](../artifacts/security/uac-policies.md) |
| `SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\UserList` | 登录界面隐藏账户配置。 | [SpecialAccounts\UserList](../artifacts/security/specialaccounts-userlist.md) |
| `SYSTEM\Select` | `CurrentControlSet` 离线映射入口。 | [HKLM\SYSTEM](hklm/system.md) |
| `SYSTEM\ControlSet00x\Services` | 服务、驱动、BAM/DAM、RDP、Tcpip、LSA 相关配置。 | [Services](../artifacts/persistence/services.md), [BAM / DAM](../artifacts/execution/bam-dam.md) |
| `SYSTEM\ControlSet00x\Enum` | 设备枚举和 USB 调查入口。 | [USBSTOR](../artifacts/usb/usbstor.md) |
| `SYSTEM\MountedDevices` | 卷 GUID、盘符和设备映射。 | [MountedDevices](../artifacts/usb/mounteddevices.md) |
| `SYSTEM\ControlSet00x\Control\Terminal Server` | RDP 服务端允许状态和 listener 配置。 | [fDenyTSConnections](../artifacts/rdp/fdenytsconnections.md), [RDP-Tcp PortNumber](../artifacts/rdp/rdp-tcp-portnumber.md) |
| `SYSTEM\ControlSet00x\Services\SharedAccess\Parameters\FirewallPolicy` | Windows Firewall 规则和 profile 配置。 | [Firewall Policies](../artifacts/security/firewall-policies.md) |
| `SECURITY\Policy\PolAdtEv` | 审计策略底层数据。 | [Audit Policy](../artifacts/security/audit-policy.md) |

## Linked Artifacts

- [BAM / DAM](../artifacts/execution/bam-dam.md)
- [Run / RunOnce](../artifacts/persistence/run-keys.md)
- [StartupApproved](../artifacts/persistence/startupapproved.md)
- [Services](../artifacts/persistence/services.md)
- [IFEO](../artifacts/persistence/ifeo.md)
- [Winlogon Userinit](../artifacts/persistence/winlogon-userinit.md)
- [Winlogon Shell](../artifacts/persistence/winlogon-shell.md)
- [LSA Authentication Packages](../artifacts/persistence/lsa-authentication-packages.md)
- [MountedDevices](../artifacts/usb/mounteddevices.md)
- [USBSTOR](../artifacts/usb/usbstor.md)
- [ProfileList](../artifacts/security/profilelist.md)
- [Defender Policies](../artifacts/security/defender-policies.md)
- [UAC Policies](../artifacts/security/uac-policies.md)
- [Firewall Policies](../artifacts/security/firewall-policies.md)
- [Audit Policy](../artifacts/security/audit-policy.md)
- [SpecialAccounts\UserList](../artifacts/security/specialaccounts-userlist.md)
- [fDenyTSConnections](../artifacts/rdp/fdenytsconnections.md)
- [RDP-Tcp PortNumber](../artifacts/rdp/rdp-tcp-portnumber.md)
- [CredSSP / NLA](../artifacts/rdp/credssp-nla.md)

## Collection Notes

=== "Live"

    ```cmd
    reg save HKLM\SAM C:\Temp\SAM.hiv
    reg save HKLM\SECURITY C:\Temp\SECURITY.hiv
    reg save HKLM\SOFTWARE C:\Temp\SOFTWARE.hiv
    reg save HKLM\SYSTEM C:\Temp\SYSTEM.hiv
    reg query HKLM\SYSTEM\Select
    ```

=== "Offline"

    ```text
    Collect:
    C:\Windows\System32\Config\SAM
    C:\Windows\System32\Config\SECURITY
    C:\Windows\System32\Config\SOFTWARE
    C:\Windows\System32\Config\SYSTEM
    C:\Windows\System32\Config\*.LOG1 / *.LOG2 when available
    EFI or boot partition BCD when boot configuration is in scope
    ```

Live `reg save` may require administrative privileges and can be affected by EDR or tamper controls. Offline acquisition should preserve original file paths and timestamps.

## Analyst Checklist

- Identify which HKLM hive files were collected and whether transaction logs are present.
- Resolve `SYSTEM\Select` before using any `ControlSet00x` path.
- Separate machine-level evidence from user-level evidence; do not attribute HKLM findings to a user without supporting logs.
- Check whether suspicious machine-level paths point into user-writable directories.
- Compare sensitive policy values with organization baseline, GPO/MDM source, and security product state.
- For persistence findings, ask what trigger is required: boot, service start, user logon, cmd startup, LSASS load, or process launch.
- For every timestamp in a report, state whether it is key LastWrite, parser-decoded internal time, event log time, or file system time.

## References

- [Microsoft Learn: Registry hives](https://learn.microsoft.com/en-us/windows/win32/sysinfo/registry-hives)
- [Microsoft Learn: Predefined keys](https://learn.microsoft.com/en-us/windows/win32/sysinfo/predefined-keys)
