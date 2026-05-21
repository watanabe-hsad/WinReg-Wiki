# HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32

`ComDlg32` 保存 common open/save dialog 的用户级 MRU 相关配置。

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32` |
| 离线 | `NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32` |

## 常见子键 / value

| 名称 | 类型 | 含义 |
|---|---|---|
| `OpenSavePidlMRU` | Key | 按扩展名分组的打开/保存对话框 PIDL MRU。 |
| `OpenSavePidlMRU\*` | Key | 未按扩展名细分的 MRU。 |
| `LastVisitedPidlMRU` | Key | 应用程序与最近访问目录关系。 |
| `MRUListEx` | `REG_BINARY` | MRU 顺序列表。 |
| `<number>` | `REG_BINARY` | PIDL 数据，需解析工具还原路径。 |

## 说明

| 项 | 内容 |
|---|---|
| 数据来源 | 用户 `NTUSER.DAT`。 |
| 常见写入者 | Explorer common dialog、调用 common dialog 的应用。 |
| 注意 | PIDL 需要专门解析；路径线索不等于文件内容被读取。 |

## 相关 Artifact

- [OpenSavePidlMRU](../../../../../../artifacts/user-activity/opensavepidlmru.md)
- [LastVisitedPidlMRU](../../../../../../artifacts/user-activity/lastvisitedpidlmru.md)
- [RecentDocs](../../../../../../artifacts/user-activity/recentdocs.md)

