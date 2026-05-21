# HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\Notify

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\Notify` |
| 离线 | `SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\Notify` |

## 离线位置

`C:\Windows\System32\Config\SOFTWARE`

## 作用

保存 Winlogon notification package 相关配置。该机制用于让指定 DLL 接收登录、注销、锁定等 Winlogon 事件通知；现代系统中较少见，遇到时应谨慎核对来源。

## 常见子键和值

| 名称 | 类型 | 含义 | 常见数据 / 状态 | 说明 |
|---|---|---|---|---|
| `<PackageName>` | Key | 单个 notification package。 | 厂商或组件名称 | 名称可伪装。 |
| `DLLName` | `REG_SZ` / `REG_EXPAND_SZ` | 通知 DLL 名称或路径。 | DLL 文件名或路径 | 需验证文件存在、签名和目录。 |
| `Logon` / `Logoff` | `REG_SZ` | 事件回调函数名。 | 函数名 | 具体 value 视组件而定。 |
| `Startup` / `Shutdown` | `REG_SZ` | 启动 / 关机通知回调。 | 函数名 | 不一定存在。 |
| `Asynchronous` | `REG_DWORD` | 异步处理提示。 | `0` / `1` | 语义需结合组件。 |

## 默认状态与版本差异

该机制与 Windows 版本和登录架构有关。较新系统上该位置通常不是主流扩展点，合法旧组件或安全产品仍可能留有配置。

## 注意事项

- 配置存在不等于 DLL 已加载或回调已执行。
- DLL 名称未带路径时需要结合默认 DLL 搜索路径和文件位置分析。
- 应与 Winlogon、LSA 包、Credential Provider 和服务配置分开解释。

## 取证提示

- 关注非系统目录、用户可写目录、无签名 DLL 或与近期文件落地时间接近的子键。
- 与模块加载、Winlogon 进程行为、文件签名和安全产品日志交叉验证。

## 相关场景

- [自启动与持久化](../../../../../../../questions/persistence.md)
- [账户与安全](../../../../../../../questions/accounts-security.md)
- [常规注册表检查](../../../../../../../questions/registry-checklist.md)

## 相关位置

- [Winlogon](../winlogon.md)
- [LSA](../../../../../system/controlset/control/lsa/index.md)
- [Policies\System](../../../windows/currentversion/policies/system.md)

## 补充阅读

- [Winlogon Shell artifact](../../../../../../../artifacts/persistence/winlogon-shell.md)
- [Winlogon Userinit artifact](../../../../../../../artifacts/persistence/winlogon-userinit.md)
