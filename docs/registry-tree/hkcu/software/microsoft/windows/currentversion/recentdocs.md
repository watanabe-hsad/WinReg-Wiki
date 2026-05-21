# HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs

`RecentDocs` 保存 Explorer 维护的最近文档名称和 MRU 顺序。

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs` |
| 离线 | `NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs` |

## 常见子键 / value

| 名称 | 类型 | 含义 |
|---|---|---|
| `MRUListEx` | `REG_BINARY` | MRU 顺序。 |
| `<number>` | `REG_BINARY` | 最近文档条目，通常可解析出文件名。 |
| `.<ext>` | Key | 按扩展名分组的最近文档。 |

## 说明

| 项 | 内容 |
|---|---|
| 数据来源 | 用户 `NTUSER.DAT`。 |
| 常见写入者 | Explorer / Shell。 |
| 注意 | 文件名出现说明用户环境记录过该名称，不直接证明文件内容被读取。 |

## 相关 Artifact

- [RecentDocs](../../../../../../artifacts/user-activity/recentdocs.md)
- [OpenSavePidlMRU](../../../../../../artifacts/user-activity/opensavepidlmru.md)
- [UserAssist](../../../../../../artifacts/execution/userassist.md)

