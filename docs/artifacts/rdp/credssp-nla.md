---
tags:
  - RDP
  - RemoteAccess
  - CredSSP
  - NLA
  - SYSTEM
---

# CredSSP / NLA

此页保留 RDP CredSSP / NLA 配置的补充细节。主入口请先查看注册表位置页和取证场景页。

## 对应注册表位置

| 位置 | 说明 |
|---|---|
| [RDP-Tcp](../../registry-tree/hklm/system/controlset/control/terminal-server/rdp-tcp.md) | RDP listener 的 NLA 和安全层配置。 |
| [CredSSP](../../registry-tree/hklm/system/controlset/control/terminal-server/credssp.md) | CredSSP encryption oracle remediation 等策略参数。 |

## 字段语义

| Value | 类型 | 含义 |
|---|---|---|
| `UserAuthentication` | `REG_DWORD` | RDP listener 是否要求 Network Level Authentication 的相关配置。 |
| `SecurityLayer` | `REG_DWORD` | RDP listener 安全层配置。 |
| `AllowEncryptionOracle` | `REG_DWORD` | CredSSP encryption oracle remediation 策略。 |

## 采集与工具

```cmd
reg query "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v UserAuthentication
reg query "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v SecurityLayer
reg query "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\CredSSP\Parameters" /s
```

- Registry Explorer / RECmd：离线读取 `SYSTEM` 和 `SOFTWARE` hive。
- KAPE / Velociraptor：采集 RDP、GPO、TerminalServices 和防火墙上下文。

## 常见误读

- 认证配置降低不等于 RDP 登录成功。
- GPO、兼容性排障、旧客户端和补丁级别会影响这些值。
- 配置值可能存在但被策略、服务状态或补丁行为影响实际生效。

## 交叉验证

- GroupPolicy Operational、TerminalServices logs、Security.evtx。
- Windows Firewall rules、RDP 端口、TermService 状态。
- 补丁级别、GPO / MDM 策略和 EDR registry telemetry。

## 相关场景

- [RDP 与远程访问](../../questions/rdp.md)
- [安全策略与防护配置](../../questions/policy-security.md)
- [常规注册表检查](../../questions/registry-checklist.md)

## 参考资料

- [Microsoft Learn: CredSSP encryption oracle remediation](https://learn.microsoft.com/en-us/troubleshoot/windows-server/remote/credssp-encryption-oracle-remediation)
- [MITRE ATT&CK: Remote Services - RDP](https://attack.mitre.org/techniques/T1021/001/)
