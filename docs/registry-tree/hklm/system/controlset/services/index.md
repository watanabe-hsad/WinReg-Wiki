# HKLM\SYSTEM\ControlSet00x\Services

`Services` 保存服务、驱动、网络组件和部分系统组件的配置。

<div class="ww-fact-card" markdown>
<div class="ww-fact-card__top">
<div><span class="ww-card-kicker">Registry Fact Card</span><strong>HKLM\SYSTEM\ControlSet00x\Services</strong></div>
<span class="ww-badge ww-badge--status">stable / high</span>
</div>
<div class="ww-fact-grid" markdown>
<div><span>Root</span><span class="ww-badge ww-badge--hive">HKLM</span></div>
<div><span>Hive</span><span class="ww-badge ww-badge--hive">SYSTEM</span></div>
<div><span>Offline file</span><strong>C:\Windows\System32\Config\SYSTEM</strong></div>
<div class="ww-fact-wide"><span>Native path</span><div class="ww-path-stack"><span class="ww-path-pill">HKLM\SYSTEM\CurrentControlSet\Services</span><span class="ww-path-pill">HKLM\SYSTEM\ControlSet00x\Services</span></div></div>
</div>
<div class="ww-fact-footer">
<div><span>Topics</span><span class="ww-chip ww-chip--topic">系统配置</span><span class="ww-chip ww-chip--topic">持久化</span><span class="ww-chip ww-chip--topic">网络</span></div>
<div><span>Scenarios</span><span class="ww-chip ww-chip--scenario">自启动与持久化</span><span class="ww-chip ww-chip--scenario">程序执行痕迹</span><span class="ww-chip ww-chip--scenario">常规注册表检查</span></div>
<div><span>Related data</span><span class="ww-chip ww-chip--data">data/registry: hklm-system-controlset-services</span><span class="ww-chip ww-chip--data">artifact: services</span><span class="ww-chip ww-chip--data">artifact: drivers</span><span class="ww-chip ww-chip--data">artifact: bam-dam</span></div>
</div>
</div>

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SYSTEM\CurrentControlSet\Services` |
| 离线 | `SYSTEM\ControlSet00x\Services` |

## 常见子键 / value

| 名称 | 类型 | 含义 |
|---|---|---|
| `<ServiceName>` | Key | 单个服务或驱动配置。 |
| [`EventLog`](eventlog.md) | Key | Windows Event Log 服务和通道配置。 |
| [`SharedAccess\Parameters\FirewallPolicy`](sharedaccess/firewallpolicy.md) | Key | Windows Defender Firewall 本地配置。 |
| [`Tcpip`](tcpip.md) | Key | TCP/IP 全局和接口配置。 |
| `ImagePath` | `REG_EXPAND_SZ` / `REG_SZ` | 服务可执行文件或驱动路径。 |
| `Type` | `REG_DWORD` | 服务类型，例如 Win32 service、kernel driver。 |
| `Start` | `REG_DWORD` | 启动类型，例如 boot、system、auto、demand、disabled。 |
| `DisplayName` | `REG_SZ` | 显示名称。 |
| `ObjectName` | `REG_SZ` | 服务运行账户。 |
| `Parameters` | Key | 服务私有参数；具体含义由服务决定。 |

## 说明

| 项 | 内容 |
|---|---|
| 数据来源 | `SYSTEM` hive。 |
| 常见写入者 | Service Control Manager、驱动安装程序、系统组件、管理工具。 |
| 注意 | 配置存在不等于服务成功启动；启动状态需结合事件日志或运行时状态。 |

## 相关场景

- [自启动与持久化](../../../../../questions/persistence.md)
- [程序执行痕迹](../../../../../questions/execution.md)
- [安全策略与防护配置](../../../../../questions/policy-security.md)
- [常规注册表检查](../../../../../questions/registry-checklist.md)

## 补充阅读

- [Services](../../../../../artifacts/persistence/services.md)
- [Firewall Policies](../../../../../artifacts/security/firewall-policies.md)
- [BAM / DAM](../../../../../artifacts/execution/bam-dam.md)

## 参考

- [Microsoft Learn: HKLM\SYSTEM\CurrentControlSet\Services registry tree](https://learn.microsoft.com/en-us/windows-hardware/drivers/install/hklm-system-currentcontrolset-services-registry-tree)
- [Microsoft Sysinternals: Autoruns](https://learn.microsoft.com/en-us/sysinternals/downloads/autoruns)
