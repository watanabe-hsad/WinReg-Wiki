# HKCU\Software\Microsoft\Windows\CurrentVersion\Policies

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKCU\Software\Microsoft\Windows\CurrentVersion\Policies` |
| HKU | `HKU\<SID>\Software\Microsoft\Windows\CurrentVersion\Policies` |
| 离线 | `NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Policies` |

## 离线位置

`C:\Users\<User>\NTUSER.DAT`

## 作用

保存用户级 Windows 策略配置入口。它可包含 Explorer、System、Attachments 等用户范围策略，通常由本地策略、GPO、MDM、管理工具或应用配置写入。

## 常见子键和值

| 名称 | 类型 | 含义 | 常见数据 / 状态 | 说明 |
|---|---|---|---|---|
| `Explorer` | Key | Explorer / Shell 用户策略。 | 视策略而定 | 常见限制 UI、驱动器、控制面板等行为。 |
| `System` | Key | 用户范围系统策略。 | 视策略而定 | 具体值需按版本和策略解释。 |
| `Attachments` | Key | 附件管理器相关策略。 | 视策略而定 | 与下载文件区域标记相关。 |

## 默认状态与版本差异

普通用户 hive 中该路径可能不存在或只包含少量策略。域环境、企业管理、VDI、教育/网吧终端和加固模板可能写入较多值。

## 注意事项

- HKCU 策略只适用于对应用户 SID。
- 策略值存在不等于用户主动修改，也不直接说明策略来源。
- 离线分析需先用 ProfileList / HKU 映射确认用户归属。

## 取证提示

- 用户级策略可解释 Shell 限制、下载/附件处理、控制面板访问和用户环境差异。
- 需要与 GroupPolicy Operational、MDM、管理员操作和同用户 Shell 行为线索验证。

## 相关场景

- [安全策略与防护配置](../../../../../../questions/policy-security.md)
- [Shell / Explorer 用户行为](../../../../../../questions/shell-explorer.md)
- [反取证与清理痕迹](../../../../../../questions/anti-forensics.md)
- [常规注册表检查](../../../../../../questions/registry-checklist.md)

## 相关位置

- [Policies\Explorer](policies/explorer.md)
- [HKCU Explorer](explorer.md)
- [HKU NTUSER.DAT](../../../../../hku/ntuser.md)

## 补充阅读

- [HKLM Policies](../../../../../hklm/software/policies.md)
