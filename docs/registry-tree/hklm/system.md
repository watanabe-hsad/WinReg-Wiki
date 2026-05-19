# HKLM\SYSTEM

`HKLM\SYSTEM` 是 ControlSet、服务、驱动、设备、USB、网络、RDP 服务端配置、时间区域和系统身份信息的核心 hive。它是机器级时间线和配置还原的第一优先级来源之一。

## Native Registry View

Live 系统中常见路径是 `HKLM\SYSTEM\CurrentControlSet`。这个路径方便人工分析，但本质是运行时映射：

```text
HKLM\SYSTEM\CurrentControlSet -> HKLM\SYSTEM\ControlSet00x
```

映射关系由 `HKLM\SYSTEM\Select` 决定。离线 hive 中通常只有 `ControlSet001`、`ControlSet002` 等真实控制集，而没有可靠可用的 `CurrentControlSet`。

## Offline Hive Source

| Hive | Offline file | Notes |
|---|---|---|
| `SYSTEM` | `C:\Windows\System32\Config\SYSTEM` | ControlSet、服务、驱动、设备、网络、RDP、LSA 运行配置。 |
| transaction logs | `SYSTEM.LOG1`, `SYSTEM.LOG2` | 可能帮助恢复未合并的 registry transaction。 |

离线分析不能直接假设 `ControlSet001` 就是当前配置。应先读取：

```text
HKLM\SYSTEM\Select
```

常见 value：

| Value | Meaning |
|---|---|
| `Current` | live `CurrentControlSet` 指向的控制集编号。 |
| `Default` | 下次启动默认尝试使用的控制集。 |
| `Failed` | 最近失败启动相关控制集，可能为 `0`。 |
| `LastKnownGood` | 上一次已知良好配置。 |

## Forensic Role

`SYSTEM` 负责把“机器状态”串起来：

- `Services` 说明服务、驱动和部分内核/用户态组件如何启动。
- `Enum`、`USBSTOR`、`MountedDevices` 说明设备和卷如何被系统识别。
- `Control\Terminal Server` 和 `WinStations\RDP-Tcp` 说明 RDP 服务端是否允许连接、监听哪个端口。
- `Services\Tcpip\Parameters` 和 `Interfaces` 说明网络接口、DNS、DHCP 和主机网络配置。
- `Control\TimeZoneInformation`、`Control\ComputerName` 帮助解释时间线和主机身份。
- `Control\Lsa`、`Services\bam`、`Services\dam` 等路径连接安全配置和执行线索。

`Services`、`USBSTOR`、`MountedDevices` 和 RDP 服务端配置之间常在同一控制集内互相关联：服务/驱动提供能力，Enum 记录设备枚举，MountedDevices 记录卷映射，Terminal Server 记录远程访问配置。

## Detection Role

高价值监控点包括：

- 服务和驱动创建、修改、删除：`ControlSet00x\Services\*`。
- BAM/DAM 用户程序活动记录：`Services\bam\State\UserSettings`。
- LSA 包和保护配置：`Control\Lsa`。
- RDP 配置变化：`Control\Terminal Server`、`WinStations\RDP-Tcp`。
- DNS / DHCP / 接口配置变化：`Services\Tcpip\Parameters`、`Interfaces\<GUID>`。
- USB 和卷映射变化：`Enum\USBSTOR`、`MountedDevices`。

检测规则应把 registry set 事件与服务控制、驱动加载、网络连接、登录事件和文件落地时间线组合，而不是只对路径告警。

## Timestamp Caveats

- `ControlSet00x` 内的 key LastWrite 是对应 key 的更新时间，不是设备插入、服务启动或 value 创建的直接时间。
- `Select` 的 `Current` 决定当前控制集，但历史调查可能需要比较 `LastKnownGood` 或其他 control set。
- `Enum\USBSTOR` 和 `MountedDevices` 的 LastWrite 可提示枚举或映射变化，不能单独证明用户访问文件。
- `Services` key LastWrite 可提示配置变化，不能证明服务启动成功。
- `TimeZoneInformation` 影响本地时间解释；报告中应统一 UTC 或明确时区。

## Common Misinterpretations

| Misinterpretation | Safer interpretation |
|---|---|
| `ControlSet001` 一定是当前配置 | 先解析 `SYSTEM\Select\Current`。 |
| `Services\<name>` 存在说明服务正在运行 | 只能证明配置存在；运行状态需事件日志、进程、SCM 或 EDR。 |
| `USBSTOR` 存在说明用户复制过文件 | 只能证明设备枚举；文件操作需 LNK、Jump Lists、USN、EDR 等。 |
| `MountedDevices` 中有盘符说明当前盘符仍有效 | 盘符可复用；需要卷 GUID、序列号、USBSTOR 和文件系统交叉。 |
| `fDenyTSConnections=0` 说明发生过 RDP 登录 | 它证明允许配置，不证明连接成功。 |

## High-Value Subkeys

| Subkey | What to look for | Linked artifacts / scenarios |
|---|---|---|
| `Select` | `Current`、`Default`、`Failed`、`LastKnownGood`。 | [注册表基础](../../getting-started/registry-basics.md) |
| `ControlSet00x` | 当前和历史控制集差异。 | 先用 `Select` 映射。 |
| `ControlSet00x\Services` | `ImagePath`、`Start`、`Type`、`ServiceDll`、驱动和服务持久化。 | [Services](../../artifacts/persistence/services.md) |
| `ControlSet00x\Services\bam\State\UserSettings\<SID>` | SID 维度程序活动线索。 | [BAM / DAM](../../artifacts/execution/bam-dam.md) |
| `ControlSet00x\Services\dam\State\UserSettings\<SID>` | DAM 相关活动线索，覆盖范围需验证。 | [BAM / DAM](../../artifacts/execution/bam-dam.md) |
| `ControlSet00x\Enum` | 设备枚举树，USB、PCI、SCSI、SWD 等。 | USB / 设备调查 |
| `ControlSet00x\Enum\USBSTOR` | USB 存储厂商、产品、序列号。 | [USBSTOR](../../artifacts/usb/usbstor.md) |
| `ControlSet00x\Enum\USB` | USB 设备枚举，不限存储。 | 待补充 artifact |
| `MountedDevices` | 卷 GUID、盘符、设备路径映射。 | [MountedDevices](../../artifacts/usb/mounteddevices.md) |
| `ControlSet00x\Control\Terminal Server` | `fDenyTSConnections`、RDP 允许状态。 | [fDenyTSConnections](../../artifacts/rdp/fdenytsconnections.md) |
| `ControlSet00x\Control\Terminal Server\WinStations\RDP-Tcp` | `PortNumber`、NLA/安全层相关配置。 | [RDP-Tcp PortNumber](../../artifacts/rdp/rdp-tcp-portnumber.md), [CredSSP / NLA](../../artifacts/rdp/credssp-nla.md) |
| `ControlSet00x\Control\TimeZoneInformation` | 时区、Bias、Daylight 信息。 | 时间线解释 |
| `ControlSet00x\Control\ComputerName` | 主机名和 ActiveComputerName。 | 网络与资产识别 |
| `ControlSet00x\Services\Tcpip\Parameters` | 主机名、域、DNS、全局 TCP/IP 配置。 | [网络与系统环境](../../questions/network.md) |
| `ControlSet00x\Services\Tcpip\Parameters\Interfaces\<GUID>` | 网卡 IP、DHCP、DNS、网关。 | [网络与系统环境](../../questions/network.md) |
| `ControlSet00x\Control\Lsa` | LSA 包、RunAsPPL、安全包。 | [LSA Authentication Packages](../../artifacts/persistence/lsa-authentication-packages.md) |
| `ControlSet00x\Services\SharedAccess\Parameters\FirewallPolicy` | Windows Firewall profile 和规则配置。 | [Firewall Policies](../../artifacts/security/firewall-policies.md) |

## Linked Artifacts

- [Services](../../artifacts/persistence/services.md)
- [BAM / DAM](../../artifacts/execution/bam-dam.md)
- [LSA Authentication Packages](../../artifacts/persistence/lsa-authentication-packages.md)
- [USBSTOR](../../artifacts/usb/usbstor.md)
- [MountedDevices](../../artifacts/usb/mounteddevices.md)
- [MountPoints2](../../artifacts/usb/mountpoints2.md)
- [Terminal Server Client](../../artifacts/rdp/terminal-server-client.md) for client-side RDP context.
- [fDenyTSConnections](../../artifacts/rdp/fdenytsconnections.md)
- [RDP-Tcp PortNumber](../../artifacts/rdp/rdp-tcp-portnumber.md)
- [CredSSP / NLA](../../artifacts/rdp/credssp-nla.md)
- [Firewall Policies](../../artifacts/security/firewall-policies.md)

## Collection Notes

=== "Live"

    ```cmd
    reg query HKLM\SYSTEM\Select
    reg query HKLM\SYSTEM\CurrentControlSet\Services /s
    reg query HKLM\SYSTEM\MountedDevices
    reg query "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server" /s
    reg save HKLM\SYSTEM C:\Temp\SYSTEM.hiv
    ```

=== "Offline"

    ```text
    Collect:
    C:\Windows\System32\Config\SYSTEM
    C:\Windows\System32\Config\SYSTEM.LOG1
    C:\Windows\System32\Config\SYSTEM.LOG2

    Then:
    1. Load SYSTEM.
    2. Read Select\Current.
    3. Map CurrentControlSet to ControlSet00x.
    4. Parse Services, Enum, MountedDevices, Terminal Server, Tcpip, TimeZoneInformation, ComputerName.
    ```

## Analyst Checklist

- Resolve `Select\Current` before interpreting `ControlSet00x`.
- Compare current and non-current control sets when investigating failed boot, rollback, or persistence cleanup.
- For services, collect `ImagePath`, `Start`, `Type`, `ObjectName`, `Parameters\ServiceDll`, signature, file hash, and SCM events.
- For USB, tie `USBSTOR` serial, `MountedDevices` volume mapping, user [MountPoints2](../../artifacts/usb/mountpoints2.md), LNK, Jump Lists, and SetupAPI.
- For RDP, separate service configuration from actual logon evidence in Security.evtx and TerminalServices logs.
- For network, separate static `NameServer` from `DhcpNameServer`, and record interface GUIDs.
- Record timezone before interpreting local timestamps from logs or tools.

## References

- [Microsoft Learn: Registry hives](https://learn.microsoft.com/en-us/windows/win32/sysinfo/registry-hives)
- [Microsoft Learn: Services registry tree](https://learn.microsoft.com/en-us/windows-hardware/drivers/install/hklm-system-currentcontrolset-services-registry-tree)
