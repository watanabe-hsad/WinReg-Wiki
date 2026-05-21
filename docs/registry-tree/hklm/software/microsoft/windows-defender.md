# HKLM\SOFTWARE\Microsoft\Windows Defender

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SOFTWARE\Microsoft\Windows Defender` |
| 离线 | `SOFTWARE\Microsoft\Windows Defender` |

## 离线位置

`C:\Windows\System32\Config\SOFTWARE`

## 作用

保存 Microsoft Defender 的产品配置、状态和本地数据入口。它不同于策略位置，也不同于 Defender Operational 日志。

## 常见子键和值

| 名称 | 类型 | 含义 | 常见数据 / 状态 | 说明 |
|---|---|---|---|---|
| `Exclusions` | Key | 排除项相关配置入口。 | 子键按类型分组 | 策略路径也可能在 `Policies` 下。 |
| `Features` | Key | Defender 功能相关配置。 | 视版本而定 | 具体 value 随平台变化。 |
| `Real-Time Protection` | Key | 实时防护相关状态或配置入口。 | 视版本而定 | 实际状态要另行验证。 |
| `Signature Updates` | Key | 签名更新相关配置。 | 视版本而定 | 可辅助判断更新状态。 |
| `SpyNet` | Key | 云保护 / MAPS 相关配置。 | 视版本和策略而定 | 需结合平台文档。 |

## 默认状态与版本差异

Microsoft Defender 平台随 Windows 版本和安全更新变化较多。第三方 AV、企业管理、Tamper Protection 和 Defender for Endpoint 都可能改变可见值和实际状态。

## 注意事项

- 这里的值不能单独证明 Defender 已开启或已关闭。
- 策略值通常优先查看 `HKLM\SOFTWARE\Policies\Microsoft\Windows Defender`。
- 实际防护状态要结合 Defender 日志、PowerShell 状态、服务状态、EDR 和策略来源验证。

## 取证提示

- 排除项、实时保护、签名更新异常可作为安全控制调查线索。
- 与 Defender Operational、PowerShell 操作日志、Sysmon registry telemetry 和 EDR tamper 告警交叉验证。

## 相关场景

- [安全策略与防护配置](../../../../questions/policy-security.md)
- [反取证与清理痕迹](../../../../questions/anti-forensics.md)
- [常规注册表检查](../../../../questions/registry-checklist.md)

## 相关位置

- [Defender Policies](../policies/microsoft/windows-defender.md)
- [HKLM Policies](../policies.md)
- [EventLog](../../system/controlset/services/eventlog.md)

## 补充阅读

- [Defender Policies artifact](../../../../artifacts/security/defender-policies.md)
- [Microsoft Learn: Microsoft Defender Antivirus in Windows](https://learn.microsoft.com/en-us/defender-endpoint/microsoft-defender-antivirus-windows)

