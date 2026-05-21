# HKCU\Printers

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKCU\Printers` |
| 用户 SID | `HKU\<SID>\Printers` |
| 离线 | `NTUSER.DAT\Printers` |

## 离线位置

`C:\Users\<User>\NTUSER.DAT`

## 作用

保存用户级打印机连接、默认打印机和部分打印首选项。机器级打印服务、驱动和端口配置不在这里，应同时查看 `HKLM` 下的打印相关位置。

## 常见子键和值

| 名称 | 类型 | 含义 | 常见数据 / 状态 | 说明 |
|---|---|---|---|---|
| `Connections` | Key | 用户连接过的网络打印机。 | `,,server,printer` 形式常见 | 可提示打印资源和服务器名称。 |
| `DevModePerUser` | Key | 用户级打印设备模式。 | 二进制配置 | 需要打印相关工具或上下文解释。 |
| `Settings` | Key | 用户级打印设置。 | 视系统和打印机而定 | 具体 value 随驱动变化。 |
| `Defaults` | `REG_SZ` / `REG_BINARY` | 默认打印机或默认设置相关数据。 | 视版本而定 | 需结合系统版本确认。 |

## 默认状态与版本差异

无打印机或未连接网络打印资源的用户可能记录很少。企业环境中 GPO、打印服务器和驱动会影响子键形态。

## 注意事项

- 用户级打印机连接不等于该用户打印过某个文件。
- 网络打印机名称可提示内部服务器或共享资源，但需要日志和文件记录交叉验证。
- 打印驱动和 Spooler 组件配置主要在机器级位置。

## 取证提示

- 可辅助确认用户是否配置过某个打印资源或打印服务器。
- 与 PrintService 日志、Spool 文件、文档打开记录结合时，能帮助还原打印相关行为。

## 相关场景

- [Shell / Explorer 用户行为](../../questions/shell-explorer.md)
- [网络与系统环境](../../questions/network.md)
- [常规注册表检查](../../questions/registry-checklist.md)

## 相关位置

- [HKCU](index.md)
- [NTUSER.DAT](../hku/ntuser.md)
- [Print Monitors](../hklm/system/controlset/control/print-monitors.md)
