# HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Windows

`Windows` key 中的 `AppInit_DLLs` 相关 value 控制 AppInit DLL 加载配置。

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Windows` |
| Live 32 位视图 | `HKLM\SOFTWARE\WOW6432Node\Microsoft\Windows NT\CurrentVersion\Windows` |
| 离线 | `SOFTWARE\Microsoft\Windows NT\CurrentVersion\Windows` |

## 常见子键 / value

| 名称 | 类型 | 含义 |
|---|---|---|
| `AppInit_DLLs` | `REG_SZ` | AppInit DLL 列表或路径。 |
| `LoadAppInit_DLLs` | `REG_DWORD` | 是否启用 AppInit DLL 加载。 |
| `RequireSignedAppInit_DLLs` | `REG_DWORD` | 是否要求签名 DLL。 |

## 说明

| 项 | 内容 |
|---|---|
| 数据来源 | `SOFTWARE` hive。 |
| 常见写入者 | 系统配置、旧版软件、安全软件、安装程序。 |
| 注意 | 需要同时考虑启用状态、签名要求、Secure Boot、WOW6432Node 和进程是否加载 `User32.dll`。 |

## 补充阅读

- [AppInit_DLLs](../../../../../../artifacts/persistence/appinit-dlls.md)

