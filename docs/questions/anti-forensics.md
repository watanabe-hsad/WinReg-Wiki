# 反取证与清理痕迹

反取证调查关注日志被清理、审计被关闭、安全工具被削弱、关键 artifact 被删除或时间线出现异常空洞。注册表可以证明配置变化和清理目标，但“清理发生”通常需要事件日志、文件系统和 EDR 一起确认。

## 优先级

| 优先级 | Artifact / Path | 主要价值 |
|---|---|---|
| 高 | [Defender Policies](../artifacts/security/defender-policies.md) | 防护削弱、排除项、禁用尝试 |
| 高 | `HKLM\SYSTEM\CurrentControlSet\Services\EventLog` | 事件日志服务和通道配置 |
| 高 | [Audit Policy](../artifacts/security/audit-policy.md) | 审计策略相关数据，影响日志可见性 |
| 中 | [StartupApproved](../artifacts/persistence/startupapproved.md) | 启动项被禁用或状态被清理的线索 |
| 中 | `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System` | UAC 降级或关闭 |

## 高信号特征

- Defender 排除项新增后，日志或 EDR 显示恶意文件落地。
- 审计策略被关闭，随后关键时段 Security.evtx 出现空洞。
- EventLog 服务配置异常，通道大小被调小，日志清理事件 `1102` 出现。
- 多个用户 hive 中执行 artifact 同时缺失，但文件系统和 EDR 仍显示活动。

## 交叉验证

- Security.evtx `1102`、`4719`，System.evtx 服务事件。
- Defender Operational、PowerShell logs、Sysmon 12/13/14。
- `$MFT`、`$LogFile`、`$UsnJrnl`、Volume Shadow Copy。
- EDR tamper alerts、GPO/MDM 变更、管理员操作记录。

## 结论写法

- “日志策略被修改”不等于“日志已被清理”；需要 1102、日志文件时间线或 EDR 支持。
- “artifact 缺失”不是反取证证据本身，只有在应存在的上下文里缺失并伴随清理痕迹时才有意义。
