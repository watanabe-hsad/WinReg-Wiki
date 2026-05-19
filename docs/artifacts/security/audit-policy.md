---
tags:
  - SecurityPolicy
  - AuditPolicy
  - SECURITY
  - HKLM
---

# Audit Policy

<div class="rfh-meta" markdown>
<span class="rfh-badge high">取证价值 高</span>
<span class="rfh-badge high">检测价值 高</span>
<span class="rfh-badge">日志可见性策略</span>
</div>

## 摘要

Audit Policy 决定 Windows 安全事件是否被记录；降低审计能力会直接影响 DFIR 可见性，但策略值本身不能证明日志已被删除。

## 注册表路径

| View | Hive / File | Path | Scope |
|---|---|---|---|
| Live path | `HKLM\SECURITY` | `Policy\PolAdtEv` | 机器级 |
| Live / policy context | `HKLM\SECURITY` | `Policy` | 机器级 |
| Offline hive path | `SECURITY` | `Policy\PolAdtEv` | 机器级 |

## 原生注册表视图

审计策略底层数据位于 `HKLM\SECURITY\Policy`，其中许多字段是二进制结构，不建议手工凭十六进制解释。Live 系统优先使用 `auditpol.exe` 查看有效策略。

## 离线位置

`C:\Windows\System32\Config\SECURITY`。分析时通常同时收集 `SYSTEM`、`SOFTWARE`、Security.evtx、GroupPolicy Operational 和本地域策略文件。

## 字段含义

| Field | Meaning |
|---|---|
| `Policy\PolAdtEv` | 审计策略相关二进制数据 |
| Advanced Audit Policy | 细粒度审计子类别，live 系统可用 `auditpol /get /category:*` 查看 |
| key LastWrite | SECURITY policy key 更新时间，不等于某个审计子项修改时间 |

## 取证含义

Audit Policy 决定哪些登录、对象访问、策略变更、权限使用、进程创建等事件会被记录。攻击者可能降低审计策略来制造日志空洞，管理员也可能因性能、噪声或基线调整修改策略。

## 可以证明

- 采集时本机存在某些审计策略状态。
- 可辅助解释为什么某类事件缺失。
- 可提示审计能力被降低或偏离基线。

## 不能证明

- 日志已经被清理。
- 某个事件没有发生。
- 策略变更一定由攻击者执行。
- 二进制字段含义可在不使用 parser 的情况下可靠解释。

## 时间戳说明

SECURITY hive 的 policy key LastWrite 是 key 级时间。审计策略变更应优先用 Security.evtx `4719`、GroupPolicy Operational、MDM 或 EDR telemetry 验证。日志清理应查 `1102` 和日志文件时间线。

## 系统版本差异

Windows 7/10/11/Server 支持基础和高级审计策略。域策略、Advanced Audit Policy、Legacy audit policy 和本地策略合并行为复杂，未知环境应以 live `auditpol` 和 GPO 结果为准。

## 攻击滥用

攻击者可能关闭进程创建、登录、对象访问、策略变更或特权使用审计，降低后续活动可见性。也可能清理 Security.evtx 造成明显事件。

## 检测思路

- Security.evtx `4719` 显示 System audit policy was changed。
- 高价值审计子类别从 Success/Failure 改为 No Auditing。
- 审计策略降低后出现登录、服务创建、远程执行或 Defender 异常。
- 非 GPO/MDM 进程修改审计策略。

## 常见误报

- GPO 基线更新、噪声优化、性能调优、合规策略变更、实验室配置。

## 采集方式

=== "Live"

    ```cmd
    auditpol /get /category:*
    secedit /export /cfg C:\Temp\secpol.cfg
    ```

=== "reg.exe"

    ```cmd
    reg save HKLM\SECURITY C:\Temp\SECURITY.hiv
    ```

=== "Offline"

    ```text
    Collect SECURITY hive and Security.evtx. Prefer parser or live auditpol output when available.
    ```

## 解析工具

- Registry Explorer
- RECmd
- KAPE
- Velociraptor
- auditpol.exe for live systems
- secedit.exe for live export

## 交叉验证

- Security.evtx `4719`
- Security.evtx `1102`
- GroupPolicy Operational log
- MDM diagnostics
- Sysmon Event ID 13
- EDR policy telemetry

## 示例结论

- `auditpol /get` shows Process Creation auditing disabled on a server where baseline requires Success auditing; this proves reduced process logging visibility, not that malware disabled it.
- Security.evtx `4719` occurs five minutes before a gap in process telemetry and service creation; this supports a timeline of audit weakening before persistence activity.

## 参考资料

- [Microsoft Learn: auditpol](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol)
- [Microsoft Learn: Advanced security audit policy settings](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings)
- [MITRE ATT&CK: Indicator Removal](https://attack.mitre.org/techniques/T1070/)

## 相关页面

- 场景：[安全策略与防护配置](../../questions/policy-security.md), [反取证与清理痕迹](../../questions/anti-forensics.md)
- 注册表位置：[HKLM\SECURITY](../../registry-tree/hklm/security.md)
