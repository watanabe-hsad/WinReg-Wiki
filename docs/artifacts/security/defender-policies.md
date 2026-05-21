---
tags:
  - SecurityPolicy
  - Defender
  - SOFTWARE
  - HKLM
---

# Defender Policies

此页保留 Defender 策略 artifact 的补充细节。主入口请先查看注册表位置页和取证场景页。

## 对应注册表位置

| 位置 | 说明 |
|---|---|
| [HKLM\SOFTWARE\Microsoft\Windows Defender](../../registry-tree/hklm/software/microsoft/windows-defender.md) | Defender 产品配置主位置。 |
| [HKLM\SOFTWARE\Policies\Microsoft\Windows Defender](../../registry-tree/hklm/software/policies/microsoft/windows-defender.md) | Defender 策略位置，常见于 GPO / MDM / 本地策略。 |

## 字段语义

| Value / 子键 | 类型 | 含义 |
|---|---|---|
| `DisableAntiSpyware` | `REG_DWORD` | 历史禁用策略；新版本需结合 Tamper Protection 和平台状态解释。 |
| `DisableRealtimeMonitoring` | `REG_DWORD` | 实时保护相关策略。 |
| `DisableBehaviorMonitoring` | `REG_DWORD` | 行为监控相关策略。 |
| `DisableIOAVProtection` | `REG_DWORD` | 下载 / 附件扫描相关策略。 |
| `DisableScriptScanning` | `REG_DWORD` | 脚本扫描相关策略。 |
| `Exclusions\Paths` | Key | 路径排除项。 |
| `Exclusions\Extensions` | Key | 扩展名排除项。 |
| `Exclusions\Processes` | Key | 进程排除项。 |

## 采集与工具

```powershell
Get-MpPreference | Select-Object ExclusionPath, ExclusionProcess, ExclusionExtension,
  DisableRealtimeMonitoring, DisableBehaviorMonitoring
reg query "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender" /s
```

- Registry Explorer / RECmd：查看策略 key、排除项和 LastWrite。
- KAPE：采集 SOFTWARE、Defender Operational、Group Policy 和 PowerShell 日志。
- Velociraptor：跨主机枚举 Defender 策略与排除项。

## 常见误读

- 策略值存在不等于 Defender 实际已关闭；需要结合 Defender 状态、平台版本和 Tamper Protection。
- 排除项可能来自 EDR/AV 兼容性、数据库、备份、虚拟化、开发编译目录或安全团队排障。
- key LastWrite 只能说明 key 变化，不能精确到单个排除项创建时间。

## 交叉验证

- Microsoft-Windows-Windows Defender/Operational。
- PowerShell `Set-MpPreference` / `Add-MpPreference` 日志。
- Sysmon Event ID 13、Security 4657、EDR registry telemetry。
- GroupPolicy Operational、MDM diagnostics、Intune / GPO 变更记录。

## 相关场景

- [安全策略与防护配置](../../questions/policy-security.md)
- [反取证与清理痕迹](../../questions/anti-forensics.md)
- [常规注册表检查](../../questions/registry-checklist.md)

## 参考资料

- [Microsoft Learn: Defender Policy CSP](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-defender)
- [Microsoft Learn: Tamper Protection](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/prevent-changes-to-security-settings-with-tamper-protection)
- [MITRE ATT&CK: Impair Defenses](https://attack.mitre.org/techniques/T1562/)
