# HKLM\SYSTEM\ControlSet00x\Control\Session Manager\BootExecute

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SYSTEM\CurrentControlSet\Control\Session Manager /v BootExecute` |
| 离线 | `SYSTEM\ControlSet00x\Control\Session Manager /v BootExecute` |

## 离线位置

`C:\Windows\System32\Config\SYSTEM`

## 作用

`BootExecute` 保存启动早期由 Session Manager 处理的执行项。常见默认数据为 `autocheck autochk *`，用于启动时磁盘检查。该 value 变化可能影响重启早期的执行流程。

## 常见子键和值

| 名称 | 类型 | 含义 | 常见数据 / 状态 | 说明 |
|---|---|---|---|---|
| `BootExecute` | `REG_MULTI_SZ` | 启动早期执行项列表。 | `autocheck autochk *` 常见 | 额外条目需验证程序来源。 |

## 默认状态与版本差异

常见默认值为 `autocheck autochk *`。不同系统版本、磁盘检查工具、厂商工具或安全产品可能带来差异，未知项不要仅凭名称判断。

## 注意事项

- `BootExecute` 配置存在不等于异常条目已执行；需要重启和执行证据。
- 修改时间只能从 key LastWrite 和外部 telemetry 推断，不能精确到单个字符串项。
- 离线分析需解析 `SYSTEM\Select`，不要直接假设某个 `ControlSet00x` 是当前控制集。

## 取证提示

- 额外条目、指向非系统路径的条目或无法解释的可执行名称，需要结合启动日志、文件系统时间线和 EDR telemetry。
- 可与服务、驱动、KnownDLLs、PendingFileRenameOperations 一起检查启动阶段异常。

## 相关场景

- [自启动与持久化](../../../../../../questions/persistence.md)
- [反取证与清理痕迹](../../../../../../questions/anti-forensics.md)
- [常规注册表检查](../../../../../../questions/registry-checklist.md)

## 相关位置

- [Session Manager](index.md)
- [Services](../../services/index.md)
- [Drivers](../../services/drivers.md)

## 补充阅读

- [Microsoft Sysinternals: Autoruns](https://learn.microsoft.com/en-us/sysinternals/downloads/autoruns)
