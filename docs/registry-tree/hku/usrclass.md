# UsrClass.dat

`UsrClass.dat` 保存用户级 Classes、Shell 和 COM 相关配置，加载后常见为 `HKU\<SID>_Classes`，并参与 `HKCU\Software\Classes` / `HKCR` 合并视图。

## Windows 原生视图

Live 系统中可通过 `HKCU\Software\Classes` 或 `HKU\<SID>_Classes` 观察部分内容。与 `HKCR` 相关的有效视图需要同时考虑机器级 `HKLM\Software\Classes`。

## 离线 hive 文件来源

| 文件 | 路径 |
|---|---|
| `UsrClass.dat` | `C:\Users\<user>\AppData\Local\Microsoft\Windows\UsrClass.dat` |
| transaction logs | `UsrClass.dat.LOG1`、`UsrClass.dat.LOG2` |

## 典型取证价值

- 用户级 COM、文件关联、ShellBags、MUI Cache 相关线索。
- 调查用户级 hijack 时，定位影响范围是否只限某个 SID。

## 典型检测价值

- 监控用户级 COM / protocol hijack 指向用户可写目录。
- 扫描 `_Classes` 中可疑 `InprocServer32`、`LocalServer32`、`shell\open\command`。

## 常见误判

- 合法软件安装和用户偏好会产生大量 Classes 变更。
- `HKCR` 合并视图会掩盖真实来源，需要回到 `UsrClass.dat` 或 `SOFTWARE`。
- ShellBags、MUI Cache 等条目的时间语义依 artifact 而异，不能统一解释。

## 重点子路径

| 子路径 | 价值 | 相关 artifact |
|---|---|---|
| `Local Settings\Software\Microsoft\Windows\Shell\MuiCache` | 程序显示名和路径线索 | [MUICache](../../artifacts/execution/muicache.md) |
| `CLSID\{GUID}\InprocServer32` | 用户级 COM DLL 注册 | 待补充 |
| `<extension>\shell\open\command` | 用户级文件关联 | 待补充 |

## 关联 artifact 页面

- [MUICache](../../artifacts/execution/muicache.md)
