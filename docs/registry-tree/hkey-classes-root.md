# HKEY_CLASSES_ROOT

`HKEY_CLASSES_ROOT` 是面向程序和 Shell 的合并视图，不是单独 hive。它把机器级 `HKLM\Software\Classes` 与用户级 `HKCU\Software\Classes` 呈现为一个逻辑根键，常见于文件关联、COM 注册、协议处理器和 Shell 扩展调查。

## Windows 原生视图

在 `regedit.exe` 中从 `HKEY_CLASSES_ROOT` 展开。它是系统为应用兼容和 Shell 解析提供的视图；实际数据应回到 `HKLM\Software\Classes` 与当前用户的 `HKCU\Software\Classes` 核对。用户级关联、协议处理器或 COM 注册可能改变有效解析结果。

## 离线 hive 文件来源

| 逻辑来源 | 离线文件 | 备注 |
|---|---|---|
| `HKLM\Software\Classes` | `C:\Windows\System32\Config\SOFTWARE` | 机器级文件关联、COM 和 Shell 注册 |
| `HKCU\Software\Classes` | 通常来自用户 `UsrClass.dat` / `HKU\<SID>_Classes` | 需要先用 [ProfileList](../artifacts/security/profilelist.md) 确认 SID 与 profile |

离线分析时不要寻找名为 `HKEY_CLASSES_ROOT` 的单独文件。需要分别加载机器级 `SOFTWARE` 和目标用户的 `UsrClass.dat`，再判断二者是否共同影响同一个扩展名、CLSID 或协议。

## 典型取证价值

- 判断某类文件、URL scheme 或 COM 对象在案发时可能由哪个程序处理。
- 发现用户级 COM hijacking、协议处理器劫持、Shell open command 劫持。
- 在 [MUICache](../artifacts/execution/muicache.md) 等用户级 Shell artifact 中确认程序显示名和路径线索。

## 典型检测价值

- 监控 `Classes\CLSID\{GUID}\InprocServer32`、`LocalServer32` 指向用户可写目录。
- 监控 `Classes\<extension>\shell\open\command` 或 `Classes\<protocol>\shell\open\command` 调用脚本解释器、下载器或 LOLBin。
- 区分机器级 installer 正常注册与用户级覆盖。用户级覆盖更适合做威胁狩猎入口。

## 常见误判

- 软件安装、浏览器、压缩软件、云盘客户端会大量写入文件关联和 Shell 扩展。
- 只看 `HKCR` 合并视图可能看不出数据来自机器级还是用户级；报告中应写明真实 hive。
- `LastWrite` 是 key 级变化时间，不代表某个 COM value 的创建时间。

## 重点子路径

| 子路径 | 用途 | 调查提示 |
|---|---|---|
| `HKLM\Software\Classes` | 机器级类注册 | 与用户级覆盖对比 |
| `HKU\<SID>_Classes` | 用户级类注册 | 关注低权限持久化和 hijack |
| `Classes\CLSID\{GUID}\InprocServer32` | COM DLL 加载 | 路径、签名、加载进程交叉验证 |
| `Classes\<extension>` | 文件扩展名关联 | 结合 RecentDocs、LNK、Jump Lists |
| `Classes\<protocol>\shell\open\command` | URL scheme 处理 | 关注命令行和参数注入 |

## 关联 artifact 页面

- [MUICache](../artifacts/execution/muicache.md)
- [Image File Execution Options](../artifacts/persistence/ifeo.md)

## References

- [Microsoft Learn: Registry hives](https://learn.microsoft.com/en-us/windows/win32/sysinfo/registry-hives)
- [Microsoft Learn: Predefined keys](https://learn.microsoft.com/en-us/windows/win32/sysinfo/predefined-keys)
