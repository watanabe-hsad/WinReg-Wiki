# HKLM\SYSTEM

`HKLM\SYSTEM` 保存控制集、服务、驱动、设备枚举、网络接口、RDP 服务端配置、时间区域和主机名。

## 文件

| 项 | 路径 |
|---|---|
| Hive | `C:\Windows\System32\Config\SYSTEM` |
| Transaction logs | `SYSTEM.LOG1`, `SYSTEM.LOG2` |

## ControlSet

live 系统常见路径：

```text
HKLM\SYSTEM\CurrentControlSet
```

离线分析时使用真实控制集：

```text
HKLM\SYSTEM\ControlSet001
HKLM\SYSTEM\ControlSet002
```

`CurrentControlSet` 的映射由 [`HKLM\SYSTEM\Select`](select.md) 决定。

| Value | 含义 |
|---|---|
| `Current` | 当前使用的控制集编号。 |
| `Default` | 下次启动默认控制集。 |
| `Failed` | 最近失败启动相关控制集。 |
| `LastKnownGood` | 上一次已知良好配置。 |

## 常用路径

| 路径 | 含义 |
|---|---|
| [`Select`](select.md) | 控制集映射。 |
| [`ControlSet00x`](controlset/index.md) | 真实控制集。 |
| [`ControlSet00x\Services`](controlset/services/index.md) | 服务、驱动、网络组件配置。 |
| [`ControlSet00x\Services\<DriverName>`](controlset/services/drivers.md) | 驱动服务配置。 |
| `ControlSet00x\Services\bam\State\UserSettings\<SID>` | BAM 程序活动记录。 |
| `ControlSet00x\Services\dam\State\UserSettings\<SID>` | DAM 相关记录。 |
| [`ControlSet00x\Enum`](controlset/enum/index.md) | 设备枚举树。 |
| [`ControlSet00x\Enum\USBSTOR`](controlset/enum/usbstor.md) | USB 存储设备枚举。 |
| [`ControlSet00x\Enum\USB`](controlset/enum/usb.md) | USB 设备枚举。 |
| [`ControlSet00x\Enum\SWD\WPDBUSENUM`](controlset/enum/swd-wpdbusenum.md) | Windows Portable Devices 枚举。 |
| [`ControlSet00x\Control\DeviceClasses`](controlset/control/deviceclasses.md) | 设备接口类注册。 |
| [`MountedDevices`](mounteddevices.md) | 卷 GUID、盘符、设备映射。 |
| [`ControlSet00x\Control\Terminal Server`](controlset/control/terminal-server.md) | RDP 服务端开关。 |
| `ControlSet00x\Control\Terminal Server\WinStations\RDP-Tcp` | RDP listener、端口、NLA / 安全层。 |
| [`ControlSet00x\Control\Print\Monitors`](controlset/control/print-monitors.md) | 打印端口监视器配置。 |
| [`ControlSet00x\Services\EventLog`](controlset/services/eventlog.md) | 事件日志通道配置。 |
| [`ControlSet00x\Services\SharedAccess\Parameters\FirewallPolicy`](controlset/services/sharedaccess/firewallpolicy.md) | Windows Defender Firewall 本地配置。 |
| [`ControlSet00x\Services\Tcpip\Parameters`](controlset/services/tcpip.md) | TCP/IP 全局配置。 |
| [`ControlSet00x\Services\Tcpip\Parameters\Interfaces\<GUID>`](controlset/services/tcpip/parameters/interfaces.md) | 网卡 IP、DNS、DHCP、网关。 |
| [`ControlSet00x\Control\TimeZoneInformation`](controlset/control/timezone.md) | 时区和 Bias。 |
| [`ControlSet00x\Control\ComputerName`](controlset/control/computername.md) | 主机名。 |
| [`ControlSet00x\Control\Session Manager\Environment`](controlset/control/session-manager/environment.md) | 系统级环境变量。 |
| [`ControlSet00x\Control\Lsa`](controlset/control/lsa/index.md) | LSA 运行配置和认证包。 |
| [`ControlSet00x\Control\Lsa\Security Packages`](controlset/control/lsa/security-packages.md) | LSA 安全支持包列表。 |
| `ControlSet00x\Services\SharedAccess\Parameters\FirewallPolicy` | Windows Firewall 配置。 |

## 注意

| 项 | 说明 |
|---|---|
| `ControlSet001` | 不一定是当前配置；先读 `Select\Current`。 |
| `Services` | 证明服务配置存在，不等于服务成功启动。 |
| `USBSTOR` | 证明设备枚举，不等于文件复制。 |
| `MountedDevices` | 盘符可复用，需结合卷 GUID 和设备信息。 |
| `TimeZoneInformation` | 会影响本地时间线解释。 |

## 相关场景

- [常规注册表检查](../../../questions/registry-checklist.md)
- [自启动与持久化](../../../questions/persistence.md)
- [USB 与外接设备](../../../questions/usb.md)
- [RDP 与远程访问](../../../questions/rdp.md)
- [安全策略与防护配置](../../../questions/policy-security.md)
- [网络与系统环境](../../../questions/network.md)

## 补充阅读

[Services](../../../artifacts/persistence/services.md),
[Drivers](../../../artifacts/persistence/drivers.md),
[BAM / DAM](../../../artifacts/execution/bam-dam.md),
[LSA Authentication Packages](../../../artifacts/persistence/lsa-authentication-packages.md),
[LSA Security Packages](../../../artifacts/persistence/lsa-security-packages.md),
[Print Monitors](../../../artifacts/persistence/print-monitors.md),
[USB](../../../artifacts/usb/usb.md),
[DeviceClasses](../../../artifacts/usb/deviceclasses.md),
[Enum SWD WPDBUSENUM](../../../artifacts/usb/swd-wpdbusenum.md),
[USBSTOR](../../../artifacts/usb/usbstor.md),
[MountedDevices](../../../artifacts/usb/mounteddevices.md),
[fDenyTSConnections](../../../artifacts/rdp/fdenytsconnections.md),
[RDP-Tcp PortNumber](../../../artifacts/rdp/rdp-tcp-portnumber.md),
[CredSSP / NLA](../../../artifacts/rdp/credssp-nla.md),
[Firewall Policies](../../../artifacts/security/firewall-policies.md)
