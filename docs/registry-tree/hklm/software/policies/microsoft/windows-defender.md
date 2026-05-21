# HKLM\SOFTWARE\Policies\Microsoft\Windows Defender

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SOFTWARE\Policies\Microsoft\Windows Defender` |
| 离线 | `SOFTWARE\Policies\Microsoft\Windows Defender` |

## 离线位置

`C:\Windows\System32\Config\SOFTWARE`

## 作用

保存 Microsoft Defender Antivirus 相关策略值。这里表示注册表中的策略配置或配置尝试，不等同于 Defender 运行时状态或日志。

## 常见子键和值

| 名称 | 类型 | 含义 | 常见数据 / 状态 | 说明 |
|---|---|---|---|---|
| `DisableAntiSpyware` | `REG_DWORD` | 旧版 Defender 禁用相关策略。 | 版本相关 | 新版本语义和有效性受限制。 |
| `Real-Time Protection\DisableRealtimeMonitoring` | `REG_DWORD` | 实时保护相关策略。 | `0` / `1` | 需验证实际状态。 |
| `Real-Time Protection\DisableBehaviorMonitoring` | `REG_DWORD` | 行为监控相关策略。 | `0` / `1` | 受版本和策略影响。 |
| `Real-Time Protection\DisableIOAVProtection` | `REG_DWORD` | 下载 / 附件扫描相关策略。 | `0` / `1` | 需结合 Defender 状态。 |
| `Real-Time Protection\DisableScriptScanning` | `REG_DWORD` | 脚本扫描相关策略。 | `0` / `1` | 需结合平台版本。 |
| `Exclusions\Paths` | Key | 路径排除项。 | value 名可能为路径 | 排除项可能来自策略或管理平台。 |
| `Exclusions\Processes` | Key | 进程排除项。 | value 名可能为进程路径 | 需要检查来源和生效状态。 |
| `Exclusions\Extensions` | Key | 扩展名排除项。 | value 名可能为扩展名 | 影响扫描范围。 |

## 默认状态与版本差异

Defender 策略语义随 Windows 版本、Defender 平台版本、Tamper Protection、企业管理状态和第三方 AV 状态变化。不要把某个禁用值直接写成“防护已关闭”。

## 注意事项

- 注册表中存在策略值，只能说明配置存在或曾被写入。
- Tamper Protection 可能阻止或忽略部分注册表修改。
- 实际状态应使用 Defender 日志、PowerShell / WMI 状态、GPO / MDM 结果和安全平台记录验证。

## 取证提示

- 排除项指向用户可写目录、整盘根目录、下载目录、脚本目录或攻击工具目录时，需要结合文件落地和执行时间线。
- 禁用类策略与 Defender Operational、PowerShell 操作、Sysmon registry telemetry 和 EDR tamper 告警一起看。

## 相关场景

- [安全策略与防护配置](../../../../../questions/policy-security.md)
- [反取证与清理痕迹](../../../../../questions/anti-forensics.md)
- [常规注册表检查](../../../../../questions/registry-checklist.md)

## 相关位置

- [HKLM Policies](../../policies.md)
- [Windows Defender](../../microsoft/windows-defender.md)
- [EventLog](../../../system/controlset/services/eventlog.md)

## 补充阅读

- [Defender Policies artifact](../../../../../artifacts/security/defender-policies.md)
- [Microsoft Learn: Policy CSP - Defender](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-defender)
- [Microsoft Learn: Tamper protection](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/prevent-changes-to-security-settings-with-tamper-protection)
