# HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\ShellServiceObjectDelayLoad

`ShellServiceObjectDelayLoad` 保存 Explorer Shell 延迟加载的 COM 对象列表。

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\ShellServiceObjectDelayLoad` |
| COM 注册 | `HKLM\SOFTWARE\Classes\CLSID\{GUID}` |
| 离线 | `SOFTWARE\Microsoft\Windows\CurrentVersion\ShellServiceObjectDelayLoad` |

## 常见子键 / value

| 名称 | 类型 | 含义 |
|---|---|---|
| `<ValueName>` | `REG_SZ` | Shell service object 名称到 CLSID 的映射。 |
| `{GUID}` | Value data | COM CLSID。 |
| `InprocServer32` | `REG_SZ` | CLSID 对应 DLL 路径，位于 COM 注册处。 |

## 说明

| 项 | 内容 |
|---|---|
| 数据来源 | `SOFTWARE` hive；COM 合并视图涉及 `Classes`。 |
| 常见写入者 | Windows Shell 组件、Shell 扩展、同步盘、企业桌面软件。 |
| 注意 | 需要从 CLSID 继续解析 DLL；HKCR 是合并视图，离线分析应看 `SOFTWARE\Classes` 和用户 `UsrClass.dat`。 |

## 相关 Artifact

- [ShellServiceObjectDelayLoad](../../../../../../artifacts/persistence/shellserviceobjectdelayload.md)

