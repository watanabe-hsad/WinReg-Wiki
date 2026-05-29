# HKLM\SOFTWARE\Classes

`HKLM\SOFTWARE\Classes` 保存机器级文件关联、COM class、协议处理器和 shell 扩展配置。

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SOFTWARE\Classes` |
| 离线 | `SOFTWARE\Classes` |

## 常见子键 / value

| 名称 | 类型 | 含义 |
|---|---|---|
| `.<ext>` | Key | 文件扩展名关联。 |
| `<ProgID>` | Key | ProgID 对应的打开方式和 shell action。 |
| `CLSID\{GUID}` | Key | COM class 注册。 |
| `Interface\{GUID}` | Key | COM interface 注册。 |
| `Applications` | Key | 应用程序关联注册。 |

## 说明

| 项 | 内容 |
|---|---|
| 数据来源 | `SOFTWARE` hive。 |
| 常见写入者 | 应用安装器、COM 组件注册、系统组件。 |
| 注意 | `HKCR` 是 `HKLM\SOFTWARE\Classes` 与用户级 `HKCU\Software\Classes` 的合并视图。 |

## 补充阅读

- [MUICache](../../../artifacts/execution/muicache.md)
- [IFEO](../../../artifacts/persistence/ifeo.md)
- [Run / RunOnce](../../../artifacts/persistence/run-keys.md)

