# HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU

`RunMRU` 保存 Win+R Run dialog 的输入历史。

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU` |
| 离线 | `NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU` |

## 离线位置

`C:\Users\<user>\NTUSER.DAT`

## 作用

记录用户在 Explorer Run dialog 中输入过的命令、路径、URL 或 UNC。它是输入历史，不是命令执行日志。

## 常见子键和值

| 名称 | 类型 | 含义 |
|---|---|---|
| `MRUList` | `REG_SZ` | MRU 顺序，使用字母引用具体 value。 |
| `a`, `b`, `c` ... | `REG_SZ` | 用户输入过的命令、路径、URL 或 UNC。 |

## 默认状态与版本差异

新账户或未使用 Run dialog 的用户可能为空。记录行为受 Explorer、隐私设置和用户清理影响。

## 注意事项

- 输入历史不等于命令成功执行。
- `MRUList` 表示顺序，不表示每条命令的时间。
- live `HKCU` 取决于当前进程上下文；离线分析应定位具体 SID。

## 取证提示

- 输入 `cmd`、`powershell`、脚本路径、UNC 或内网主机名时，应结合进程创建、Prefetch、UserAssist 和日志确认。
- URL 或 UNC 线索可与浏览器历史、网络日志、LNK、Jump Lists 交叉验证。

## 相关场景

- [Shell / Explorer 用户行为](../../../../../../questions/shell-explorer.md)
- [程序执行痕迹](../../../../../../questions/execution.md)
- [常规注册表检查](../../../../../../questions/registry-checklist.md)

## 相关位置

- [HKCU Explorer](explorer.md)
- [UserAssist](userassist.md)
- [RecentDocs](recentdocs.md)

## 补充阅读

- [RunMRU](../../../../../../artifacts/user-activity/runmru.md)
- [UserAssist](../../../../../../artifacts/execution/userassist.md)
- [RecentDocs](../../../../../../artifacts/user-activity/recentdocs.md)
- [Eric Zimmerman tools: RECmd / Registry Explorer](https://ericzimmerman.github.io/#!index.md)
