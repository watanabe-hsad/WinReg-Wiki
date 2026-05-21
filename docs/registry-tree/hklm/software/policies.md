# HKLM\SOFTWARE\Policies

`HKLM\SOFTWARE\Policies` 保存机器级策略写入位置。

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SOFTWARE\Policies` |
| 离线 | `SOFTWARE\Policies` |

## 常见子键 / value

| 名称 | 类型 | 含义 |
|---|---|---|
| `Microsoft` | Key | Microsoft 产品和 Windows 组件策略。 |
| [`Microsoft\Windows Defender`](policies/microsoft/windows-defender.md) | Key | Defender 策略。 |
| `Microsoft\WindowsFirewall` | Key | Windows Firewall 策略。 |
| `Microsoft\Windows\System` | Key | 部分系统策略；具体 value 需按子组件确认。 |

## 说明

| 项 | 内容 |
|---|---|
| 数据来源 | `SOFTWARE` hive。 |
| 常见写入者 | GPO、MDM、本地策略、管理软件。 |
| 注意 | 注册表中存在策略值不直接说明策略来源；来源需要结合 GroupPolicy、MDM 或管理平台证据。 |

## 相关场景

- [安全策略与防护配置](../../../questions/policy-security.md)
- [反取证与清理痕迹](../../../questions/anti-forensics.md)
- [常规注册表检查](../../../questions/registry-checklist.md)

## 相关位置

- [Defender Policies](policies/microsoft/windows-defender.md)
- [Windows Defender](microsoft/windows-defender.md)
- [FirewallPolicy](../system/controlset/services/sharedaccess/firewallpolicy.md)

## 补充阅读

- [Defender Policies](../../../artifacts/security/defender-policies.md)
- [Firewall Policies](../../../artifacts/security/firewall-policies.md)
- [UAC Policies](../../../artifacts/security/uac-policies.md)
