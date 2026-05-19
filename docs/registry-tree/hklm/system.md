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

`CurrentControlSet` 的映射由 [`HKLM\SYSTEM\Select`](system/select.md) 决定。

| Value | 含义 |
|---|---|
| `Current` | 当前使用的控制集编号。 |
| `Default` | 下次启动默认控制集。 |
| `Failed` | 最近失败启动相关控制集。 |
| `LastKnownGood` | 上一次已知良好配置。 |

## 常用路径

| 路径 | 含义 |
|---|---|
| [`Select`](system/select.md) | 控制集映射。 |
| [`ControlSet00x`](system/controlset.md) | 真实控制集。 |
| [`ControlSet00x\Services`](system/services.md) | 服务、驱动、网络组件配置。 |
| `ControlSet00x\Services\bam\State\UserSettings\<SID>` | BAM 程序活动记录。 |
| `ControlSet00x\Services\dam\State\UserSettings\<SID>` | DAM 相关记录。 |
| [`ControlSet00x\Enum`](system/enum.md) | 设备枚举树。 |
| `ControlSet00x\Enum\USBSTOR` | USB 存储设备枚举。 |
| `ControlSet00x\Enum\USB` | USB 设备枚举。 |
| [`MountedDevices`](system/mounteddevices.md) | 卷 GUID、盘符、设备映射。 |
| [`ControlSet00x\Control\Terminal Server`](system/terminal-server.md) | RDP 服务端开关。 |
| `ControlSet00x\Control\Terminal Server\WinStations\RDP-Tcp` | RDP listener、端口、NLA / 安全层。 |
| [`ControlSet00x\Services\Tcpip\Parameters`](system/tcpip.md) | TCP/IP 全局配置。 |
| `ControlSet00x\Services\Tcpip\Parameters\Interfaces\<GUID>` | 网卡 IP、DNS、DHCP、网关。 |
| [`ControlSet00x\Control\TimeZoneInformation`](system/timezone.md) | 时区和 Bias。 |
| [`ControlSet00x\Control\ComputerName`](system/computername.md) | 主机名。 |
| [`ControlSet00x\Control\Lsa`](system/lsa.md) | LSA 运行配置和认证包。 |
| `ControlSet00x\Services\SharedAccess\Parameters\FirewallPolicy` | Windows Firewall 配置。 |

## 注意

| 项 | 说明 |
|---|---|
| `ControlSet001` | 不一定是当前配置；先读 `Select\Current`。 |
| `Services` | 证明服务配置存在，不等于服务成功启动。 |
| `USBSTOR` | 证明设备枚举，不等于文件复制。 |
| `MountedDevices` | 盘符可复用，需结合卷 GUID 和设备信息。 |
| `TimeZoneInformation` | 会影响本地时间线解释。 |

## 相关 Artifact

[Services](../../artifacts/persistence/services.md),
[BAM / DAM](../../artifacts/execution/bam-dam.md),
[LSA Authentication Packages](../../artifacts/persistence/lsa-authentication-packages.md),
[USBSTOR](../../artifacts/usb/usbstor.md),
[MountedDevices](../../artifacts/usb/mounteddevices.md),
[fDenyTSConnections](../../artifacts/rdp/fdenytsconnections.md),
[RDP-Tcp PortNumber](../../artifacts/rdp/rdp-tcp-portnumber.md),
[CredSSP / NLA](../../artifacts/rdp/credssp-nla.md),
[Firewall Policies](../../artifacts/security/firewall-policies.md)
