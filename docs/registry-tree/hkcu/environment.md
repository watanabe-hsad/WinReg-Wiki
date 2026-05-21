# HKCU\Environment

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKCU\Environment` |
| 用户 SID | `HKU\<SID>\Environment` |
| 离线 | `NTUSER.DAT\Environment` |

## 离线位置

`C:\Users\<User>\NTUSER.DAT`

## 作用

保存用户级环境变量。用户登录后，Windows 会把用户级环境变量与系统级环境变量合并到进程环境中。具体进程看到的值还受父进程、登录会话、服务上下文和应用启动方式影响。

## 常见子键和值

| 名称 | 类型 | 含义 | 常见数据 / 状态 | 说明 |
|---|---|---|---|---|
| `Path` | `REG_EXPAND_SZ` / `REG_SZ` | 用户级可执行文件搜索路径追加项。 | 视用户软件而定 | 会与系统级 `Path` 合并。 |
| `TEMP` | `REG_EXPAND_SZ` / `REG_SZ` | 用户临时目录。 | `%USERPROFILE%\AppData\Local\Temp` 常见 | 可能被应用或用户改写。 |
| `TMP` | `REG_EXPAND_SZ` / `REG_SZ` | 用户临时目录。 | `%USERPROFILE%\AppData\Local\Temp` 常见 | 通常与 `TEMP` 一致。 |
| `<CustomName>` | `REG_SZ` / `REG_EXPAND_SZ` | 用户自定义环境变量。 | 视软件和用户配置而定 | 开发工具、脚本、代理和管理软件可能写入。 |

## 默认状态与版本差异

默认值视 Windows 版本、用户配置、域策略和安装软件而定。不要假设所有用户都有相同 `Path`、`TEMP` 或自定义变量。

## 注意事项

- `HKCU` 是当前进程用户视图；离线分析要回到具体用户的 `NTUSER.DAT`。
- 环境变量值存在不等于所有进程都使用该值；已经启动的进程可能保留旧环境。
- 用户级 `Path` 会影响命令搜索顺序，但实际命中哪个可执行文件还取决于当前目录、系统级 `Path`、`PATHEXT` 和调用方式。

## 取证提示

- 可用于解释某用户会话中的命令搜索路径、临时目录和脚本运行环境。
- 用户级 `Path` 或自定义变量指向用户可写目录时，可作为持久化或执行环境污染的线索。
- 需要结合进程创建日志、脚本内容和文件系统时间线判断实际使用情况。

## 相关场景

- [自启动与持久化](../../questions/persistence.md)
- [程序执行痕迹](../../questions/execution.md)
- [反取证与清理痕迹](../../questions/anti-forensics.md)
- [常规注册表检查](../../questions/registry-checklist.md)

## 相关位置

- [HKCU](index.md)
- [NTUSER.DAT](../hku/ntuser.md)
- [系统级 Environment](../hklm/system/controlset/control/session-manager/environment.md)

## 补充阅读

- [Microsoft Learn: Recognized environment variables](https://learn.microsoft.com/en-us/windows/deployment/usmt/usmt-recognized-environment-variables)
