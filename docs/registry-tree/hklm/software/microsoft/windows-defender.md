# HKLM\SOFTWARE\Microsoft\Windows Defender

`Microsoft\Windows Defender` 保存 Defender 本地配置和状态相关注册表项。

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SOFTWARE\Microsoft\Windows Defender` |
| 离线 | `SOFTWARE\Microsoft\Windows Defender` |

## 常见子键 / value

| 名称 | 类型 | 含义 |
|---|---|---|
| `Exclusions` | Key | 排除项相关配置，策略路径也可能在 `Policies` 下。 |
| `Features` | Key | 功能相关配置；具体 value 随版本变化。 |
| `Real-Time Protection` | Key | 实时防护相关配置，具体 value 需按版本确认。 |
| `Signature Updates` | Key | 签名更新相关配置。 |

## 说明

| 项 | 内容 |
|---|---|
| 数据来源 | `SOFTWARE` hive。 |
| 常见写入者 | Microsoft Defender、Windows Security、GPO、MDM、安全管理平台。 |
| 注意 | Defender 受 Tamper Protection、平台版本和策略来源影响；只读注册表不足以完整判断运行状态。 |

## 相关 Artifact

- [Defender Policies](../../../../artifacts/security/defender-policies.md)
- [Firewall Policies](../../../../artifacts/security/firewall-policies.md)
- [Audit Policy](../../../../artifacts/security/audit-policy.md)

