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
| `Microsoft\Windows Defender` | Key | Defender 策略。 |
| `Microsoft\WindowsFirewall` | Key | Windows Firewall 策略。 |
| `Microsoft\Windows\System` | Key | 部分系统策略；具体 value 需按子组件确认。 |

## 说明

| 项 | 内容 |
|---|---|
| 数据来源 | `SOFTWARE` hive。 |
| 常见写入者 | GPO、MDM、本地策略、管理软件。 |
| 注意 | 注册表中存在策略值不直接说明策略来源；来源需要结合 GroupPolicy、MDM 或管理平台证据。 |

## 相关 Artifact

- [Defender Policies](../../../artifacts/security/defender-policies.md)
- [Firewall Policies](../../../artifacts/security/firewall-policies.md)
- [UAC Policies](../../../artifacts/security/uac-policies.md)

