# HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths` |
| 32 位视图 | `HKLM\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\App Paths` |
| 离线 | `SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths` |

## 离线位置

`C:\Windows\System32\Config\SOFTWARE`

## 作用

保存应用程序注册路径。应用可通过 `App Paths\<name>.exe` 注册可执行文件位置、搜索路径和启动相关元数据，便于 Shell 或 API 通过短名称解析程序路径。

## 常见子键和值

| 名称 | 类型 | 含义 | 常见数据 / 状态 | 说明 |
|---|---|---|---|---|
| `<app>.exe` | Key | 单个应用注册项。 | 应用安装时创建 | 子键名通常是可执行文件名。 |
| `(Default)` | `REG_SZ` | 应用程序完整路径。 | `C:\Program Files\...\app.exe` | 路径可能随安装位置变化。 |
| `Path` | `REG_SZ` / `REG_EXPAND_SZ` | 追加到应用搜索路径的目录。 | 安装目录、依赖目录 | 可影响 DLL 或子程序搜索。 |
| `UseUrl` | `REG_DWORD` | Shell 相关 URL 处理提示。 | 视应用而定 | 不应脱离应用上下文解释。 |

## 默认状态与版本差异

不同 Windows 版本和已安装软件会产生不同 App Paths 项。64 位系统上 32 位程序可能写入 `WOW6432Node` 视图。

## 注意事项

- App Paths 记录应用注册信息，不等于程序执行。
- 子键名可以伪装成常见程序名，应以默认路径、签名和文件时间线验证。
- `Path` 会影响该应用启动时的搜索环境，但实际加载结果要结合进程和模块证据。

## 取证提示

- 可用于确认程序安装路径、短名称解析路径和可疑路径劫持线索。
- 当 App Paths 指向用户可写目录或不存在路径时，应与执行日志、文件系统时间线和安装记录核对。

## 相关场景

- [程序执行痕迹](../../../../../../questions/execution.md)
- [软件安装与卸载](../../../../../../questions/software-install.md)
- [自启动与持久化](../../../../../../questions/persistence.md)
- [常规注册表检查](../../../../../../questions/registry-checklist.md)

## 相关位置

- [HKLM Uninstall](uninstall.md)
- [HKLM Run / RunOnce](run.md)
- [HKLM SOFTWARE](../../../index.md)
- [WOW6432Node](../../../wow6432node.md)

## 补充阅读

- [Microsoft Learn: Application registration](https://learn.microsoft.com/en-us/windows/win32/shell/app-registration)
