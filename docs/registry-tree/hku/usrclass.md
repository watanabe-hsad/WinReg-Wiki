# UsrClass.dat

`UsrClass.dat` 保存用户级 Classes、COM、Shell 和部分 Explorer 相关数据。

## 文件

| 项 | 路径 |
|---|---|
| Hive | `C:\Users\<user>\AppData\Local\Microsoft\Windows\UsrClass.dat` |
| Transaction logs | `UsrClass.dat.LOG1`, `UsrClass.dat.LOG2` |

## 常见视图

| 视图 | 含义 |
|---|---|
| `HKU\<SID>_Classes` | 用户级 Classes hive。 |
| `HKCU\Software\Classes` | 当前用户 Classes 视图。 |
| `HKCR` | 与机器级 Classes 合并后的视图。 |

## 常用路径

| 路径 | 含义 |
|---|---|
| `Local Settings\Software\Microsoft\Windows\Shell\MuiCache` | 程序路径和显示名缓存。 |
| `Local Settings\Software\Microsoft\Windows\Shell\BagMRU` | ShellBags 路径树。 |
| `Local Settings\Software\Microsoft\Windows\Shell\Bags` | ShellBags 视图配置。 |
| `CLSID\{GUID}\InprocServer32` | 用户级 COM DLL 注册。 |
| `<extension>\shell\open\command` | 用户级文件关联命令。 |

## 注意

| 项 | 说明 |
|---|---|
| `HKCR` | 合并视图会隐藏真实来源。 |
| 用户级覆盖 | 用户级 Classes 可影响当前用户的 COM 和文件关联解析。 |
| ShellBags | 目录浏览线索，不等于文件打开或复制。 |

## 相关 Artifact

[MUICache](../../artifacts/execution/muicache.md)
