# 安全策略与防护配置

这类调查关注“安全控制是否被削弱”：UAC、Defender、防火墙、审计策略、LSA 和 RDP 安全配置。注册表能证明配置存在，但实际生效要用策略来源和运行状态验证。

## 优先级

| 优先级 | Artifact / Path | 主要价值 |
|---|---|---|
| 高 | [Defender Policies](../artifacts/security/defender-policies.md) | Defender 禁用、排除项、实时保护策略 |
| 高 | [UAC Policies](../artifacts/security/uac-policies.md) | UAC 相关配置，例如 `EnableLUA`、提示行为、远程本地账户 token 过滤 |
| 高 | [LSA Authentication Packages](../artifacts/persistence/lsa-authentication-packages.md) | LSA 认证包配置和 LSASS 加载链 |
| 高 | [LSA Security Packages](../artifacts/persistence/lsa-security-packages.md) | LSA 安全支持包配置和 SSP/AP 加载链 |
| 中 | [Firewall Policies](../artifacts/security/firewall-policies.md) | Windows Firewall 策略、入站规则、远程访问暴露 |
| 中 | [Audit Policy](../artifacts/security/audit-policy.md) | 审计和本地安全策略，影响日志可见性 |
| 中 | [Drivers](../artifacts/persistence/drivers.md) | 驱动加载配置，适合排查安全控制绕过或内核组件 |

## 高信号特征

- Defender 排除项指向用户可写目录、整盘根目录、攻击工具目录。
- `DisableRealtimeMonitoring`、行为监控、脚本扫描策略偏离基线。
- UAC 被关闭或降级后出现管理员令牌使用、服务创建或远程执行。
- 防火墙规则开放 RDP、SMB、WinRM 或异常高端口。
- LSA 包列表出现非基线条目，或与无签名 DLL、LSASS 模块加载接近。
- 新增 kernel driver 配置后出现 Code Integrity、EDR tampering 或安全服务异常。

## 交叉验证

- Defender Operational log、PowerShell `Set-MpPreference` / `Add-MpPreference` 日志。
- GroupPolicy Operational、MDM diagnostics、Intune / GPO 变更记录。
- Sysmon Event ID 13、Security 4657、EDR registry telemetry。
- 防火墙日志、服务创建事件、进程创建事件。
- Sysmon Event ID 6 / 7、CodeIntegrity/Operational、LSASS module telemetry。

## 结论写法

- 注册表策略证明“配置值存在”。对 Defender 和 UAC，必须再验证平台版本、Tamper Protection、GPO/MDM 来源和实时状态。
- 若策略值被写入但被 Tamper Protection 阻止，结论应写“存在禁用尝试或策略值”，不能写“防护已关闭”。
