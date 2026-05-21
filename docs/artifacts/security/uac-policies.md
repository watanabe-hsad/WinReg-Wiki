---
tags:
  - SecurityPolicy
  - UAC
  - SOFTWARE
  - HKLM
---

# UAC Policies

此页保留 UAC policy artifact 的补充细节。主入口请先查看注册表位置页和取证场景页。

## 对应注册表位置

| 位置 | 说明 |
|---|---|
| [HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System](../../registry-tree/hklm/software/microsoft/windows/currentversion/policies/system.md) | UAC、管理员审批模式、登录提示和远程本地账户过滤相关策略。 |

## 字段语义

| Value | 类型 | 含义 |
|---|---|---|
| `EnableLUA` | `REG_DWORD` | UAC 总开关相关值。 |
| `ConsentPromptBehaviorAdmin` | `REG_DWORD` | 管理员提权提示行为。 |
| `ConsentPromptBehaviorUser` | `REG_DWORD` | 标准用户提权提示行为。 |
| `PromptOnSecureDesktop` | `REG_DWORD` | 是否在安全桌面显示 UAC 提示。 |
| `LocalAccountTokenFilterPolicy` | `REG_DWORD` | 远程本地管理员令牌过滤相关值。 |

## 采集与工具

```cmd
reg query "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System"
```

- Registry Explorer / RECmd：查看 SOFTWARE hive。
- KAPE / Velociraptor：采集策略、GroupPolicy、MDM 和登录事件。
- `secedit`、GPO / MDM 结果：核对策略来源和有效配置。

## 常见误读

- UAC 策略值存在不等于管理员提权实际发生。
- GPO、MDM、企业安全基线、kiosk、VDI 和兼容性策略可能合法调整。
- 某些配置变更需要重启才完整生效。

## 交叉验证

- Sysmon Event ID 13、Security 4657。
- GroupPolicy Operational、MDM diagnostics、Intune / GPO 变更记录。
- Security 4624、4672、服务创建和远程执行 telemetry。

## 相关场景

- [安全策略与防护配置](../../questions/policy-security.md)
- [账户与安全](../../questions/accounts-security.md)
- [RDP 与远程访问](../../questions/rdp.md)
- [常规注册表检查](../../questions/registry-checklist.md)

## 参考资料

- [Microsoft Learn: User Account Control settings and configuration](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/user-account-control/settings-and-configuration)
- [Microsoft Learn: User Account Control and remote restrictions](https://learn.microsoft.com/en-us/troubleshoot/windows-server/windows-security/user-account-control-and-remote-restriction)
- [MITRE ATT&CK: Impair Defenses](https://attack.mitre.org/techniques/T1562/)
