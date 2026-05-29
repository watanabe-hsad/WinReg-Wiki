# 安全策略与防护配置

## 检查目标

判断 UAC、Defender、防火墙、审计策略、LSA、RDP 和驱动相关配置是否被修改，并区分注册表值、策略来源和实际生效状态。

## 优先查看的注册表位置

| 注册表位置 | 用途 | 判断边界 |
|---|---|---|
| [Policies](../registry-tree/hklm/software/policies.md) | GPO / MDM / 本地策略写入位置。 | 值存在不说明来源。 |
| [Policies\System](../registry-tree/hklm/software/microsoft/windows/currentversion/policies/system.md) | UAC 和系统安全策略。 | 策略值不等于实际提权行为。 |
| [Windows Defender](../registry-tree/hklm/software/microsoft/windows-defender.md) | Defender 本地配置和排除项线索。 | 需结合 Tamper Protection 和 Defender 日志。 |
| [Defender Policies](../registry-tree/hklm/software/policies/microsoft/windows-defender.md) | Defender 策略禁用、排除项和实时保护相关值。 | 策略值不等于实际防护状态。 |
| [FirewallPolicy](../registry-tree/hklm/system/controlset/services/sharedaccess/firewallpolicy.md) | Windows Defender Firewall profile 和规则配置。 | 规则存在不等于连接发生。 |
| [WindowsFirewall Policies](../registry-tree/hklm/software/policies/microsoft/windowsfirewall.md) | 防火墙策略路径。 | 需与本地规则和 ActiveStore 对照。 |
| [EventLog](../registry-tree/hklm/system/controlset/services/eventlog.md) | 事件日志通道大小、保留和文件路径配置。 | 这里不是日志内容。 |
| [LSA](../registry-tree/hklm/system/controlset/control/lsa/index.md) | LSA 包、RunAsPPL、认证相关配置。 | 未知条目需验证 DLL 和模块加载。 |
| [KnownDLLs](../registry-tree/hklm/system/controlset/control/session-manager/knowndlls.md) | Known DLL 映射。 | 需与同版本基线和模块加载核对。 |
| [LSA Security Packages](../registry-tree/hklm/system/controlset/control/lsa/security-packages.md) | 安全包列表。 | 列表变化不等于 DLL 已加载。 |
| [SECURITY](../registry-tree/hklm/security.md) | 本地安全策略、审计策略、LSA Secrets。 | 需要专门工具解析。 |
| [Terminal Server](../registry-tree/hklm/system/controlset/control/terminal-server.md) | RDP 允许状态。 | 允许远程桌面不等于登录发生。 |
| [RDP-Tcp](../registry-tree/hklm/system/controlset/control/terminal-server/rdp-tcp.md) | RDP listener 端口、NLA 和安全层。 | 配置存在不等于端口可达。 |
| [CredSSP](../registry-tree/hklm/system/controlset/control/terminal-server/credssp.md) | CredSSP 认证兼容性策略。 | 需结合 GPO 和补丁级别。 |
| [LogonUI](../registry-tree/hklm/software/microsoft/windows/currentversion/authentication/logonui.md) | 登录界面最近用户和 SID 显示线索。 | 不证明登录成功。 |
| [Credential Providers](../registry-tree/hklm/software/microsoft/windows/currentversion/authentication/credential-providers.md) | 登录凭据提供器注册。 | 第三方身份组件可能合法注册。 |
| [Credential Provider Filters](../registry-tree/hklm/software/microsoft/windows/currentversion/authentication/credential-provider-filters.md) | 凭据提供器过滤器注册。 | 注册不等于某次登录使用。 |
| [CachedLogonsCount](../registry-tree/hklm/software/microsoft/windows-nt/currentversion/winlogon/cachedlogonscount.md) | 域登录缓存数量配置。 | 不是缓存凭据本体。 |
| [HKCU Policies](../registry-tree/hkcu/software/microsoft/windows/currentversion/policies.md) | 用户级策略入口。 | 需确认 SID 和策略来源。 |
| [HKCU Policies\Explorer](../registry-tree/hkcu/software/microsoft/windows/currentversion/policies/explorer.md) | 用户级 Explorer 策略。 | UI 限制不等于底层访问事实。 |
| [Drivers](../registry-tree/hklm/system/controlset/services/drivers.md) | kernel / file system driver 配置。 | 需结合驱动加载、签名和 Code Integrity。 |

## 判断要点

- Defender 排除项、禁用值和实时保护配置要记录路径、来源和是否被平台保护拦截。
- UAC 相关值通常位于 `Policies\System`，应结合管理员操作、服务创建和远程执行记录。
- 防火墙规则要区分本地规则、GPO / MDM 策略规则和 ActiveStore 状态。
- EventLog 配置变化说明日志可见性配置变化，不等于日志已经被清理。
- LSA 包、驱动、RDP 配置都先证明配置状态；实际加载或登录另证。

## 交叉验证

- Defender Operational、PowerShell `Set-MpPreference` / `Add-MpPreference`、安全产品日志。
- GroupPolicy Operational、MDM diagnostics、Intune / GPO 变更记录。
- Sysmon 6 / 7 / 12 / 13 / 14、Security 4657、EDR registry telemetry。
- Windows Firewall logs、TerminalServices logs、CodeIntegrity/Operational、LSASS module telemetry。

## 常见误判

- 企业 GPO、EDR、VPN、VDI、打印驱动和管理代理会写入大量安全策略相关值。
- Tamper Protection 可能让注册表值存在但实际未生效。
- 降低审计策略会影响日志可见性，但不能单独证明日志已被清理。

## 相关场景

- [账户与安全](accounts-security.md)
- [RDP 与远程访问](rdp.md)
- [反取证与清理痕迹](anti-forensics.md)
- [常规注册表检查](registry-checklist.md)

## 补充阅读

- [Defender Policies artifact](../artifacts/security/defender-policies.md)
- [UAC Policies artifact](../artifacts/security/uac-policies.md)
- [Firewall Policies artifact](../artifacts/security/firewall-policies.md)
- [Audit Policy artifact](../artifacts/security/audit-policy.md)
- [LSA Security Packages artifact](../artifacts/persistence/lsa-security-packages.md)
