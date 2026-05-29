# HKLM\SYSTEM\ControlSet00x\Control\Session Manager\SubSystems

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\SubSystems` |
| 离线 | `SYSTEM\ControlSet00x\Control\Session Manager\SubSystems` |

## 离线位置

`C:\Windows\System32\Config\SYSTEM`

## 作用

保存 Windows 子系统启动配置。`Windows` value 用于定义 Win32 子系统相关初始化参数，其中包含 `csrss.exe`、`winsrv.dll`、desktop heap 等配置片段。

## 常见子键和值

| 名称 | 类型 | 含义 | 常见数据 / 状态 | 说明 |
|---|---|---|---|---|
| `Windows` | `REG_EXPAND_SZ` | Win32 子系统配置字符串。 | 包含 `%SystemRoot%\system32\csrss.exe`、`winsrv`、`SharedSection` 等片段 | 修改错误可能影响登录或会话初始化。 |
| `Optional` | `REG_MULTI_SZ` | 可选子系统列表。 | 视版本和配置而定 | 多数普通客户端无需手工解释。 |

## 默认状态与版本差异

具体配置随 Windows 版本、SKU 和补丁级别变化。不要把某台主机的 `Windows` 字符串作为通用基线；应与同版本可信系统或官方说明对照。

## 注意事项

- 该位置属于会话初始化配置，不能单独证明程序执行。
- `Windows` value 是复合配置字符串，解释时应保留原文。
- 离线分析需先解析 `SYSTEM\Select` 确认当前控制集。

## 取证提示

- 异常可写路径、非系统 DLL 或明显偏离基线的子系统配置可作为启动 / 会话初始化排查线索。
- 需要与系统启动事件、文件签名、模块加载和同版本基线交叉验证。

## 相关场景

- [自启动与持久化](../../../../../../questions/persistence.md)
- [程序执行痕迹](../../../../../../questions/execution.md)
- [常规注册表检查](../../../../../../questions/registry-checklist.md)

## 相关位置

- [Session Manager](index.md)
- [BootExecute](bootexecute.md)
- [KnownDLLs](knowndlls.md)

## 补充阅读

- [Microsoft Learn: Desktop heap overview](https://learn.microsoft.com/en-us/troubleshoot/windows-server/performance/desktop-heap-limitation-out-of-memory)
