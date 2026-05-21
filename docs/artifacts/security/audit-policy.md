---
tags:
  - SecurityPolicy
  - AuditPolicy
  - SECURITY
  - HKLM
---

# Audit Policy

此页保留审计策略 artifact 的补充细节。主入口请先查看注册表位置页和取证场景页。

## 对应注册表位置

| 位置 | 说明 |
|---|---|
| [HKLM\SECURITY](../../registry-tree/hklm/security.md) | 本地安全策略和 LSA 相关数据所在 hive。 |
| `HKLM\SECURITY\Policy\PolAdtEv` | 审计策略相关二进制数据，建议使用工具或 live 命令解释。 |

## 字段语义

| 字段 / 命令 | 含义 |
|---|---|
| `Policy\PolAdtEv` | 审计策略相关二进制结构。 |
| `auditpol /get /category:*` | live 系统查看有效高级审计策略。 |
| Security.evtx `4719` | System audit policy was changed。 |
| Security.evtx `1102` | Audit log was cleared。 |

## 采集与工具

```cmd
auditpol /get /category:*
secedit /export /cfg C:\Temp\secpol.cfg
reg save HKLM\SECURITY C:\Temp\SECURITY.hiv
```

- auditpol.exe：live 系统查看有效策略。
- secedit.exe：live 系统导出本地安全策略。
- Registry Explorer / RECmd：查看 SECURITY hive key 和 LastWrite。
- KAPE / Velociraptor：采集 SECURITY、Security.evtx 和 GroupPolicy 日志。

## 常见误读

- 审计策略降低不等于日志已经被清理。
- 某类日志缺失不等于事件没有发生，可能是审计策略未启用。
- 域策略、MDM、安全基线和本地策略合并行为复杂，未知环境应以 live 输出和 GPO 结果为准。

## 交叉验证

- Security.evtx `4719`、`1102`。
- GroupPolicy Operational、MDM diagnostics、EDR policy telemetry。
- Sysmon Event ID 13、Security 4657。
- 安全基线、GPO 变更记录和 SIEM 配置。

## 相关场景

- [安全策略与防护配置](../../questions/policy-security.md)
- [反取证与清理痕迹](../../questions/anti-forensics.md)
- [常规注册表检查](../../questions/registry-checklist.md)

## 参考资料

- [Microsoft Learn: auditpol](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol)
- [Microsoft Learn: Advanced security audit policy settings](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings)
- [MITRE ATT&CK: Indicator Removal](https://attack.mitre.org/techniques/T1070/)
