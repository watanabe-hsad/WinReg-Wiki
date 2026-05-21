# HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist

UserAssist 是 Explorer 维护的用户交互记录，常用于观察用户通过 Shell 触发过的程序线索。

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist\{GUID}\Count` |
| 用户 SID | `HKU\<SID>\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist\{GUID}\Count` |
| 离线 | `NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist\{GUID}\Count` |

## 离线位置

`C:\Users\<user>\NTUSER.DAT`

## 作用

保存 Explorer、开始菜单、快捷方式等 Shell 相关交互产生的程序记录。条目名称通常经过 ROT13 编码，解析工具会还原路径或显示名，并可能解释运行次数和最近运行时间字段。

## 常见子键 / 值

| 名称 | 类型 | 含义 |
|---|---|---|
| `{GUID}` | Key | UserAssist 分类 GUID，不同系统版本和交互类型可能不同。 |
| `Count` | Key | 具体条目列表。 |
| `<ROT13 entry>` | `REG_BINARY` | 编码后的路径或名称，数据中可能包含计数和时间字段。 |

## 默认状态 / 常见状态

普通交互式用户通常会有多个 `{GUID}\Count` 子键。Server Core、少量使用 Explorer 的服务器或新建账户可能记录较少。

## 版本差异

字段结构和计数解释随 Windows 版本变化。报告中应记录解析工具和版本，不要只凭原始二进制手工解释。

## 取证提示

UserAssist 更接近“用户通过 Shell 交互过程序”的线索，但不能覆盖所有执行方式，也不能单独证明用户双击或程序完整执行。

## 相关场景

- [程序执行痕迹](../../../../../../questions/execution.md)
- [Shell / Explorer 用户行为](../../../../../../questions/shell-explorer.md)
- [常规注册表检查](../../../../../../questions/registry-checklist.md)

## 相关位置

- [HKCU Explorer](explorer.md)
- [RunMRU](runmru.md)
- [RecentDocs](recentdocs.md)

