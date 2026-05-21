---
tags:
  - Accounts
  - SecurityPolicy
  - SOFTWARE
  - HKLM
---

# SpecialAccounts\UserList

此页保留 `SpecialAccounts\UserList` artifact 的补充细节。主入口请先查看注册表位置页和取证场景页。

## 对应注册表位置

| 位置 | 说明 |
|---|---|
| [HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon](../../registry-tree/hklm/software/microsoft/windows-nt/currentversion/winlogon.md) | 登录配置和 `SpecialAccounts\UserList` 所在位置。 |
| [LogonUI](../../registry-tree/hklm/software/microsoft/windows/currentversion/authentication/logonui.md) | 登录界面最近用户和 SID 显示线索。 |

## 字段语义

| Value | 类型 | 含义 |
|---|---|---|
| `<username>` | `REG_DWORD` | 用户名显示控制项。 |
| `0` | `REG_DWORD` | 通常表示隐藏该账户，不在欢迎 / 登录界面显示。 |
| `1` | `REG_DWORD` | 通常表示显示该账户。 |

## 采集与工具

```cmd
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\UserList"
```

- Registry Explorer / RECmd：查看 SOFTWARE hive 和 LastWrite。
- KAPE / Velociraptor：采集 SOFTWARE、SAM、Security.evtx 和本地组信息。

## 常见误读

- `UserList\<username>=0` 不证明账户存在、启用、登录过或具备管理员权限。
- Kiosk、共享设备、VDI、OEM / 运维账户可能合法隐藏登录界面显示。
- key LastWrite 不是账户创建时间。

## 交叉验证

- SAM 本地账户和本地组成员。
- Security.evtx `4720`、`4722`、`4726`、`4732`、`4733`、`4738`。
- ProfileList、LogonUI、RDP logs、EDR account telemetry。

## 相关场景

- [账户与安全](../../questions/accounts-security.md)
- [安全策略与防护配置](../../questions/policy-security.md)
- [常规注册表检查](../../questions/registry-checklist.md)

## 参考资料

- [Microsoft Learn: Winlogon and credential providers](https://learn.microsoft.com/en-us/windows/win32/secauthn/winlogon-and-credential-providers)
- [MITRE ATT&CK: Create Account](https://attack.mitre.org/techniques/T1136/)
