# HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU

`RunMRU` 保存 Win+R Run dialog 的输入历史。

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU` |
| 离线 | `NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU` |

## 常见子键 / value

| 名称 | 类型 | 含义 |
|---|---|---|
| `MRUList` | `REG_SZ` | MRU 顺序，使用字母引用具体 value。 |
| `a`, `b`, `c` ... | `REG_SZ` | 用户输入过的命令、路径、URL 或 UNC。 |

## 说明

| 项 | 内容 |
|---|---|
| 数据来源 | 用户 `NTUSER.DAT`。 |
| 常见写入者 | Explorer Run dialog。 |
| 注意 | 输入历史不等于命令成功执行；需要结合进程、Prefetch、UserAssist 等证据。 |

## 相关 Artifact

- [RunMRU](../../../artifacts/user-activity/runmru.md)
- [UserAssist](../../../artifacts/execution/userassist.md)
- [RecentDocs](../../../artifacts/user-activity/recentdocs.md)

