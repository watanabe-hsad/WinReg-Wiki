# HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32

`ComDlg32` 保存 common open/save dialog 的用户级 MRU 相关配置。

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32` |
| 离线 | `NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32` |

## 离线位置

`C:\Users\<user>\NTUSER.DAT`

## 作用

记录调用 Windows common open/save dialog 的应用产生的路径和文件选择 MRU。常见数据使用 PIDL，需要工具解析为路径、文件名或目录关系。

## 常见子键和值

| 名称 | 类型 | 含义 |
|---|---|---|
| `OpenSavePidlMRU` | Key | 按扩展名分组的打开/保存对话框 PIDL MRU。 |
| `OpenSavePidlMRU\*` | Key | 未按扩展名细分的 MRU。 |
| `LastVisitedPidlMRU` | Key | 应用程序与最近访问目录关系。 |
| `MRUListEx` | `REG_BINARY` | MRU 顺序列表。 |
| `<number>` | `REG_BINARY` | PIDL 数据，需解析工具还原路径。 |

## 默认状态与版本差异

记录取决于应用是否使用 common dialog、用户行为和系统版本。部分现代应用可能不写入这些传统 MRU 子键。

## 注意事项

- PIDL 需要专门解析；不要只凭原始二进制写路径结论。
- 记录可能来自打开或保存动作，需要结合应用上下文。
- 路径线索不等于文件内容被读取。

## 取证提示

- 与 LNK、Jump Lists、RecentDocs、ShellBags 和文件系统时间线一起看。
- `LastVisitedPidlMRU` 可帮助关联应用程序与目录，但不能单独证明文件被打开。

## 相关场景

- [Shell / Explorer 用户行为](../../../../../../questions/shell-explorer.md)
- [常规注册表检查](../../../../../../questions/registry-checklist.md)

## 相关位置

- [HKCU Explorer](explorer.md)
- [RecentDocs](recentdocs.md)
- [RunMRU](runmru.md)

## 补充阅读

- [OpenSavePidlMRU](../../../../../../artifacts/user-activity/opensavepidlmru.md)
- [LastVisitedPidlMRU](../../../../../../artifacts/user-activity/lastvisitedpidlmru.md)
- [RecentDocs](../../../../../../artifacts/user-activity/recentdocs.md)
- [Eric Zimmerman tools: RECmd / Registry Explorer](https://ericzimmerman.github.io/#!index.md)
