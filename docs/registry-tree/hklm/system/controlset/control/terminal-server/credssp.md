# HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\CredSSP

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\CredSSP` |
| 常见参数 | `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\CredSSP\Parameters` |
| 离线 | `SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\CredSSP` |

## 离线位置

`C:\Windows\System32\Config\SOFTWARE`

## 作用

保存 CredSSP 相关策略参数。该位置常用于远程桌面认证兼容性和 encryption oracle remediation 策略，属于认证安全配置，不是 RDP 连接记录。

## 常见子键和值

| 名称 | 类型 | 含义 | 常见数据 / 状态 | 说明 |
|---|---|---|---|---|
| `Parameters` | Key | CredSSP 参数子键。 | 可能不存在 | 通常由策略或补丁配置产生。 |
| `AllowEncryptionOracle` | `REG_DWORD` | CredSSP encryption oracle remediation 策略。 | 视策略而定 | 需结合补丁级别和 GPO 解释。 |

## 默认状态与版本差异

该路径和值与 CVE-2018-0886 相关补丁、域策略、RDP 客户端兼容性和系统版本有关。未配置时 key 可能不存在；存在也不等于实际 RDP 登录发生。

## 注意事项

- CredSSP 策略值说明认证兼容性配置，不说明凭据是否被窃取。
- GPO / MDM 可能周期性写入或覆盖该路径。
- 解释时应同时查看 RDP-Tcp 的 `UserAuthentication`、`SecurityLayer` 和实际 TerminalServices 日志。

## 取证提示

- 放宽 CredSSP 配置可作为远程访问安全边界变化线索。
- 需要与 GroupPolicy Operational、Security.evtx、TerminalServices 和防火墙记录交叉验证。

## 相关场景

- [RDP 与远程访问](../../../../../../questions/rdp.md)
- [安全策略与防护配置](../../../../../../questions/policy-security.md)
- [常规注册表检查](../../../../../../questions/registry-checklist.md)

## 相关位置

- [RDP-Tcp](rdp-tcp.md)
- [Policies\System](../../../../software/microsoft/windows/currentversion/policies/system.md)
- [Terminal Server](../terminal-server.md)

## 补充阅读

- [CredSSP / NLA artifact](../../../../../../artifacts/rdp/credssp-nla.md)
- [Microsoft Learn: CredSSP encryption oracle remediation](https://learn.microsoft.com/en-us/troubleshoot/windows-server/remote/credssp-encryption-oracle-remediation)
