# HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs

`RecentDocs` 保存 Explorer 维护的最近文档名称和 MRU 顺序。

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs` |
| 离线 | `NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs` |

## 离线位置

`C:\Users\<user>\NTUSER.DAT`

## 作用

记录 Explorer 维护的最近文档名称、扩展名分组和 MRU 顺序。它更接近用户环境中的“文件名被记录过”线索，不保存文件内容。

## 常见子键和值

| 名称 | 类型 | 含义 |
|---|---|---|
| `MRUListEx` | `REG_BINARY` | MRU 顺序。 |
| `<number>` | `REG_BINARY` | 最近文档条目，通常可解析出文件名。 |
| `.<ext>` | Key | 按扩展名分组的最近文档。 |

## 默认状态与版本差异

新建或少量使用 Explorer 的账户可能为空。条目结构、扩展名分组和清理行为随 Windows 版本、用户配置和隐私设置变化。

## 注意事项

- 文件名出现说明用户环境记录过该名称，不直接证明文件内容被读取。
- `MRUListEx` 是顺序列表，不是独立时间戳。
- 扩展名子键和根键可能记录不同粒度的最近文档。

## 取证提示

- 与 LNK、Jump Lists、ComDlg32、ShellBags 和文件系统时间线一起使用。
- 多用户系统应先通过 ProfileList 确认 SID 与用户目录。

## 相关场景

- [Shell / Explorer 用户行为](../../../../../../questions/shell-explorer.md)
- [常规注册表检查](../../../../../../questions/registry-checklist.md)

## 相关位置

- [HKCU Explorer](explorer.md)
- [RunMRU](runmru.md)
- [ComDlg32](comdlg32.md)

## 补充阅读

- [RecentDocs](../../../../../../artifacts/user-activity/recentdocs.md)
- [OpenSavePidlMRU](../../../../../../artifacts/user-activity/opensavepidlmru.md)
- [UserAssist](../../../../../../artifacts/execution/userassist.md)
- [Eric Zimmerman tools: RECmd / Registry Explorer](https://ericzimmerman.github.io/#!index.md)
