# HKLM\SYSTEM\ControlSet00x\Control\Session Manager\KnownDLLs

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\KnownDLLs` |
| 离线 | `SYSTEM\ControlSet00x\Control\Session Manager\KnownDLLs` |

## 离线位置

`C:\Windows\System32\Config\SYSTEM`

## 作用

`KnownDLLs` 保存 Windows Known DLL 映射。系统会对部分常用 DLL 使用预定义对象和文件名映射，减少重复加载并影响 DLL 解析路径。

## 常见子键和值

| 名称 | 类型 | 含义 | 常见数据 / 状态 | 说明 |
|---|---|---|---|---|
| `DllDirectory` | `REG_EXPAND_SZ` / `REG_SZ` | Known DLL 文件目录。 | `%SystemRoot%\System32` 常见 | 目录异常需要验证。 |
| `KnownDllPath` | `REG_EXPAND_SZ` / `REG_SZ` | Known DLL 搜索路径相关值。 | 视版本而定 | 不同版本可能不存在或不同。 |
| `<dll name>` | `REG_SZ` | DLL 映射名。 | `kernel32.dll`、`user32.dll` 等常见 | 具体列表随版本变化。 |

## 默认状态与版本差异

KnownDLLs 列表由 Windows 维护，随版本、架构和更新状态变化。32 位组件可能还涉及 WoW64 相关 KnownDLLs 配置，需按系统位数解释。

## 注意事项

- KnownDLLs 异常不等于 DLL 已被加载；需要模块加载、进程或内存证据。
- 不要把正常版本差异当作篡改；应与同版本基线或可信系统比较。
- 修改该区域通常需要高权限，写入主体和时间线很关键。

## 取证提示

- 关注 `DllDirectory`、非标准 DLL 名、指向非系统目录或与基线不一致的条目。
- 与 DLL 搜索顺序劫持、进程模块加载和系统文件完整性检查一起验证。

## 相关场景

- [自启动与持久化](../../../../../../questions/persistence.md)
- [程序执行痕迹](../../../../../../questions/execution.md)
- [安全策略与防护配置](../../../../../../questions/policy-security.md)
- [常规注册表检查](../../../../../../questions/registry-checklist.md)

## 相关位置

- [Session Manager](index.md)
- [HKLM SOFTWARE Classes](../../../../software/classes.md)
- [App Paths](../../../../software/microsoft/windows/currentversion/app-paths.md)

## 补充阅读

- [Microsoft Sysinternals: Autoruns](https://learn.microsoft.com/en-us/sysinternals/downloads/autoruns)
