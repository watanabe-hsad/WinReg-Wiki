---
tags:
  - RDP
  - RemoteAccess
  - CredSSP
  - NLA
  - SYSTEM
---

# CredSSP / NLA

<div class="rfh-meta" markdown>
<span class="rfh-badge medium">取证价值 中</span>
<span class="rfh-badge high">检测价值 高</span>
<span class="rfh-badge">RDP 认证安全配置</span>
</div>

## 摘要

CredSSP / NLA 相关注册表配置影响 RDP 认证安全边界；禁用 NLA 或降低安全层会增加暴露风险，但不能单独证明 RDP 登录发生。

## 注册表路径

| View | Hive / File | Path | Value | Scope |
|---|---|---|---|---|
| Live path | `HKLM\SYSTEM` | `CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp` | `UserAuthentication` | 机器级 |
| Live path | `HKLM\SYSTEM` | `CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp` | `SecurityLayer` | 机器级 |
| Live path | `HKLM\SOFTWARE` | `Microsoft\Windows\CurrentVersion\Policies\System\CredSSP\Parameters` | `AllowEncryptionOracle` | 机器级 |
| Offline hive path | `SYSTEM` / `SOFTWARE` | 上述对应路径 | 相关 value | 机器级 |

## 原生注册表视图

RDP listener 配置通常位于 `HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp`。CredSSP oracle remediation 相关策略可能位于 `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\CredSSP\Parameters`。

## 离线位置

`RDP-Tcp` 配置来自 `C:\Windows\System32\Config\SYSTEM`；CredSSP policy 配置来自 `C:\Windows\System32\Config\SOFTWARE`。离线时需要同时采集这两个 hive。

## 字段含义

| Field | Meaning |
|---|---|
| `UserAuthentication` | 常用于表示是否要求 Network Level Authentication；具体数值语义需按版本和策略验证 |
| `SecurityLayer` | RDP listener 安全层配置，降低安全层可能增加风险 |
| `AllowEncryptionOracle` | CredSSP encryption oracle remediation 策略相关值 |
| key LastWrite | 配置 key 更新，不等于连接或登录时间 |

## 取证含义

这些值用于判断 RDP 服务端认证安全配置是否被降低。NLA 被关闭时，攻击者可在认证前触达更多 RDP 交互面；CredSSP 策略过度放宽也可能增加中间人或降级风险。取证报告应把它写成“认证安全配置状态”，不要写成“已被 RDP 登录”。

## 可以证明

- RDP listener 或 CredSSP 策略中存在某个安全配置值。
- 可辅助判断 NLA 是否被要求、安全层是否偏离基线。
- 可提示 RDP 暴露面是否被降低安全性。

## 不能证明

- RDP 登录发生过。
- 凭据被窃取。
- 配置实际生效，除非结合策略和服务状态验证。
- 降低配置一定是攻击者行为。

## 时间戳说明

`RDP-Tcp` 和 CredSSP policy key LastWrite 只表示配置 key 最近变化。GPO/MDM 可能覆盖本地值，服务可能需要重启后生效。实际认证事件应从 TerminalServices 和 Security.evtx 验证。

## 系统版本差异

NLA、CredSSP 和 encryption oracle remediation 行为受 Windows 版本、补丁级别、域策略和 RDP 客户端版本影响。未知版本应标记为待验证，避免只凭数值作最终生效判断。

## 攻击滥用

攻击者可能关闭 NLA、降低安全层或放宽 CredSSP 策略，以便兼容旧客户端、降低认证门槛或绕过某些安全控制。也可能在行动后恢复原值。

## 检测思路

- `UserAuthentication` 从要求 NLA 的基线改为不要求。
- `SecurityLayer` 或 CredSSP policy 偏离企业安全基线。
- RDP 安全配置降低后出现防火墙开放、RDP 连接尝试或登录事件。
- 非 GPO/MDM 进程写入 RDP-Tcp 或 CredSSP policy keys。

## 常见误报

- 老旧客户端兼容、临时排障、远程支持、GPO 基线调整、测试环境。

## 采集方式

=== "PowerShell"

    ```powershell
    Get-ItemProperty "HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" |
      Select-Object UserAuthentication, SecurityLayer
    Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\CredSSP\Parameters" -ErrorAction SilentlyContinue
    ```

=== "reg.exe"

    ```cmd
    reg query "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v UserAuthentication
    reg query "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v SecurityLayer
    reg query "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\CredSSP\Parameters" /s
    ```

=== "Offline"

    ```text
    Collect SYSTEM and SOFTWARE hives. Resolve SYSTEM\Select before reading RDP-Tcp.
    ```

## 解析工具

- Registry Explorer
- RECmd
- KAPE
- Velociraptor
- RegRipper

## 交叉验证

- `fDenyTSConnections`
- RDP `PortNumber`
- TerminalServices logs
- Security.evtx LogonType `10`
- GroupPolicy Operational logs
- Firewall rules and network telemetry

## 示例结论

- `UserAuthentication` differs from the organization's RDP NLA baseline in the current control set; this proves a configuration deviation, not a successful RDP session.
- CredSSP policy was relaxed by `reg.exe`, followed by RDP logon attempts in TerminalServices logs; together these support a security-control weakening timeline.

## 参考资料

- [Microsoft Learn: Configure Network Level Authentication for Remote Desktop Services](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/clients/remote-desktop-allow-access)
- [Microsoft Learn: CredSSP updates for CVE-2018-0886](https://learn.microsoft.com/en-us/troubleshoot/windows-server/remote/credssp-encryption-oracle-remediation)
- [MITRE ATT&CK: Remote Services - RDP](https://attack.mitre.org/techniques/T1021/001/)

## 相关页面

- 场景：[RDP 与远程访问](../../questions/rdp.md)
- 注册表位置：[HKLM\SYSTEM](../../registry-tree/hklm/system.md), [HKLM\SOFTWARE](../../registry-tree/hklm/software.md)
