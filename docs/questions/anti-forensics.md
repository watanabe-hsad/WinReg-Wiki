# 反取证与清理痕迹

## 检查目标

判断日志、审计、安全工具或常见注册表线索是否被配置削弱、清理或异常缺失。

## 优先查看的注册表位置

| 注册表位置 | 用途 | 判断边界 |
|---|---|---|
| [Policies](../registry-tree/hklm/software/policies.md) | 安全策略、UAC、Defender、防火墙策略入口。 | 值存在不等于实际生效。 |
| [Windows Defender](../registry-tree/hklm/software/microsoft/windows-defender.md) | Defender 排除项和本地状态线索。 | Tamper Protection 可能阻止生效。 |
| [Defender Policies](../registry-tree/hklm/software/policies/microsoft/windows-defender.md) | Defender 禁用、排除项和实时保护相关策略。 | 需验证平台版本和实际状态。 |
| [EventLog](../registry-tree/hklm/system/controlset/services/eventlog.md) | 事件日志通道大小、保留和文件路径配置。 | 不是日志内容本身。 |
| [FirewallPolicy](../registry-tree/hklm/system/controlset/services/sharedaccess/firewallpolicy.md) | 防火墙 profile 和规则配置。 | 规则变化不等于连接发生。 |
| [WindowsFirewall Policies](../registry-tree/hklm/software/policies/microsoft/windowsfirewall.md) | 防火墙策略位置。 | 策略存在不等于 ActiveStore 状态。 |
| [SECURITY](../registry-tree/hklm/security.md) | 审计和本地安全策略。 | 需要专门工具解析。 |
| [Services](../registry-tree/hklm/system/controlset/services/index.md) | EventLog、Defender、EDR、日志相关服务配置。 | 服务配置异常要结合事件日志。 |
| [PendingFileRenameOperations](../registry-tree/hklm/system/controlset/control/session-manager/pending-file-rename-operations.md) | 重启后待删除或重命名队列。 | 队列存在不等于操作已完成。 |
| [BootExecute](../registry-tree/hklm/system/controlset/control/session-manager/bootexecute.md) | 启动早期执行项。 | 异常项需结合重启和文件证据。 |
| [HKCU Environment](../registry-tree/hkcu/environment.md) | 用户级环境变量。 | 可解释命令环境变化。 |
| [HKLM Environment](../registry-tree/hklm/system/controlset/control/session-manager/environment.md) | 系统级环境变量。 | `Path` 异常需结合进程证据。 |
| [HKCU Explorer](../registry-tree/hkcu/software/microsoft/windows/currentversion/explorer.md) | 用户行为 artifact 所在入口。 | 缺失不是反取证证据本身。 |

## 判断要点

- Defender 排除项、禁用尝试和审计策略变化应与日志、EDR 和进程记录对齐。
- EventLog 服务配置异常、通道大小变化和日志清理事件要分开解释。
- `PendingFileRenameOperations` 可解释计划删除或替换，但必须确认重启和文件系统结果。
- 环境变量变化可能用于影响执行环境，也可能来自正常安装器或开发工具。
- 多个用户 hive 中预期存在的 Shell 线索同时缺失时，才考虑清理方向。
- “没有发现”只能写成证据缺口，不能直接写成清理结论。

## 交叉验证

- Security.evtx `1102`、`4719`，System.evtx 服务事件。
- Defender Operational、PowerShell logs、Sysmon 12 / 13 / 14。
- `$MFT`、`$LogFile`、`$UsnJrnl`、Volume Shadow Copy。
- EDR tamper alerts、GPO/MDM 变更、管理员操作记录。

## 常见误判

- GPO、MDM、安全产品和企业基线会正常调整审计、防火墙和 Defender 策略。
- 用户行为 artifact 缺失可能来自未使用 Explorer、Server Core、短生命周期用户或采集范围不足。
- 日志空洞可能来自日志轮转、通道大小设置或采集不完整。

## 相关场景

- [安全策略与防护配置](policy-security.md)
- [程序执行痕迹](execution.md)
- [常规注册表检查](registry-checklist.md)

## 补充阅读

- [Defender Policies artifact](../artifacts/security/defender-policies.md)
- [Audit Policy artifact](../artifacts/security/audit-policy.md)
- [StartupApproved artifact](../artifacts/persistence/startupapproved.md)
