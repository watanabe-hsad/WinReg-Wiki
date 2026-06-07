# HKLM\SYSTEM\ControlSet00x

`ControlSet00x` 是 Windows 保存系统控制配置的真实控制集，`CurrentControlSet` 是运行时映射。

<div class="ww-fact-card" markdown>
<div class="ww-fact-card__top">
<div><span class="ww-card-kicker">Registry Fact Card</span><strong>HKLM\SYSTEM\ControlSet00x</strong></div>
<span class="ww-badge ww-badge--status">stable / high</span>
</div>
<div class="ww-fact-grid" markdown>
<div><span>Root</span><span class="ww-badge ww-badge--hive">HKLM</span></div>
<div><span>Hive</span><span class="ww-badge ww-badge--hive">SYSTEM</span></div>
<div><span>Offline file</span><strong>C:\Windows\System32\Config\SYSTEM</strong></div>
<div class="ww-fact-wide"><span>Native path</span><div class="ww-path-stack"><span class="ww-path-pill">HKLM\SYSTEM\CurrentControlSet</span><span class="ww-path-pill">HKLM\SYSTEM\ControlSet001</span><span class="ww-path-pill">HKLM\SYSTEM\ControlSet002</span></div></div>
</div>
<div class="ww-fact-footer">
<div><span>Topics</span><span class="ww-chip ww-chip--topic">系统配置</span><span class="ww-chip ww-chip--topic">设备</span><span class="ww-chip ww-chip--topic">持久化</span></div>
<div><span>Scenarios</span><span class="ww-chip ww-chip--scenario">常规注册表检查</span><span class="ww-chip ww-chip--scenario">自启动与持久化</span><span class="ww-chip ww-chip--scenario">USB 与外接设备</span><span class="ww-chip ww-chip--scenario">RDP 与远程访问</span></div>
<div><span>Related data</span><span class="ww-chip ww-chip--data">data/registry: hklm-system-controlset</span><span class="ww-chip ww-chip--data">artifact: services</span><span class="ww-chip ww-chip--data">artifact: fdenytsconnections</span><span class="ww-chip ww-chip--data">artifact: rdp-tcp-portnumber</span></div>
</div>
</div>

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SYSTEM\CurrentControlSet` |
| 离线 | `SYSTEM\ControlSet001`、`SYSTEM\ControlSet002` 等 |

## 常见子键 / value

| 名称 | 类型 | 含义 |
|---|---|---|
| `Control` | Key | 系统控制配置，例如 LSA、Session Manager、Terminal Server、TimeZoneInformation、ComputerName。 |
| `Enum` | Key | 设备枚举树。 |
| `Services` | Key | 服务、驱动和网络组件配置。 |
| `Hardware Profiles` | Key | 硬件配置 profile；`HKCC` 通常映射到其中的 current profile。 |

## 说明

| 项 | 内容 |
|---|---|
| 数据来源 | `SYSTEM` hive。 |
| 常见写入者 | Windows 启动过程、服务控制管理器、PnP、驱动、系统配置工具。 |
| 注意 | 多个 `ControlSet00x` 可能并存；需要用 `Select\Current` 判断当前控制集。 |

## 相关场景

- [常规注册表检查](../../../../questions/registry-checklist.md)
- [自启动与持久化](../../../../questions/persistence.md)
- [USB 与外接设备](../../../../questions/usb.md)
- [RDP 与远程访问](../../../../questions/rdp.md)
- [反取证与清理痕迹](../../../../questions/anti-forensics.md)

## 补充阅读

- [Services](../../../../artifacts/persistence/services.md)
- [fDenyTSConnections](../../../../artifacts/rdp/fdenytsconnections.md)
- [RDP-Tcp PortNumber](../../../../artifacts/rdp/rdp-tcp-portnumber.md)

## 参考

- [Microsoft Learn: HKLM\SYSTEM\CurrentControlSet\Services registry tree](https://learn.microsoft.com/en-us/windows-hardware/drivers/install/hklm-system-currentcontrolset-services-registry-tree)
