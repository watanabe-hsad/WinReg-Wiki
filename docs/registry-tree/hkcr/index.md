# HKEY_CLASSES_ROOT

`HKEY_CLASSES_ROOT`，简称 `HKCR`，是 Classes 合并视图，不是独立 hive。

## 映射关系

| 视图 | 实际来源 |
|---|---|
| `HKCR` | `HKLM\Software\Classes` + `HKCU\Software\Classes` |
| 机器级 Classes | `C:\Windows\System32\Config\SOFTWARE` |
| 用户级 Classes | `C:\Users\<user>\AppData\Local\Microsoft\Windows\UsrClass.dat` |

用户级 Classes 可能覆盖或补充机器级 Classes。离线分析时应分别加载 `SOFTWARE` 和目标用户的 `UsrClass.dat`。

## 常用路径

| 路径 | 含义 |
|---|---|
| `<extension>` | 文件扩展名关联，例如 `.txt`、`.docx`。 |
| `<ProgID>` | 文件类型或应用程序标识。 |
| `CLSID\{GUID}` | COM class 注册。 |
| `CLSID\{GUID}\InprocServer32` | COM DLL 路径。 |
| `CLSID\{GUID}\LocalServer32` | COM EXE 路径。 |
| `<protocol>\shell\open\command` | URL scheme / 协议处理命令。 |
| `<extension>\shell\open\command` | 文件打开命令。 |

## 注意

| 项 | 说明 |
|---|---|
| 真实来源 | `HKCR` 看起来是一个根键，但数据来自机器级和用户级 Classes。 |
| 用户级覆盖 | `HKCU\Software\Classes` 可能改变当前用户看到的文件关联或 COM 解析。 |
| 离线分析 | 不存在单独的 `HKEY_CLASSES_ROOT` hive 文件。 |

## 相关 Artifact

[MUICache](../../artifacts/execution/muicache.md)
