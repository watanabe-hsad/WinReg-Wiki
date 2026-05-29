# HKCU\Software\Classes

`HKCU\Software\Classes` 保存用户级文件关联、COM 和 shell 扩展配置。

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKCU\Software\Classes` |
| 离线 | 通常来自 `C:\Users\<user>\AppData\Local\Microsoft\Windows\UsrClass.dat` |

## 常见子键 / value

| 名称 | 类型 | 含义 |
|---|---|---|
| `Local Settings\Software\Microsoft\Windows\Shell` | Key | ShellBags、MUICache 等 Shell 数据位置。 |
| `CLSID\{GUID}` | Key | 用户级 COM class 注册。 |
| `.<ext>` | Key | 用户级文件扩展名关联。 |
| `<ProgID>` | Key | 用户级 ProgID 配置。 |

## 说明

| 项 | 内容 |
|---|---|
| 数据来源 | `UsrClass.dat`，部分环境中也可能映射到用户 Classes 视图。 |
| 常见写入者 | Explorer、应用安装器、COM 注册、Shell 扩展。 |
| 注意 | `HKCR` 会合并机器级和用户级 Classes；离线分析时不要把 `HKCR` 当成独立 hive。 |

## 补充阅读

- [MUICache](../../../artifacts/execution/muicache.md)
- [OpenSavePidlMRU](../../../artifacts/user-activity/opensavepidlmru.md)
- [LastVisitedPidlMRU](../../../artifacts/user-activity/lastvisitedpidlmru.md)
