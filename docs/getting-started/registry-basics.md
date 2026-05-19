# 注册表基础

Windows 注册表是一个层级化配置数据库。取证分析时通常不直接把 `HKLM`、`HKCU` 当成文件，而是回到具体 hive 文件。

| 逻辑根 | 常见 hive 文件 | 说明 |
|---|---|---|
| `HKLM\SYSTEM` | `C:\Windows\System32\Config\SYSTEM` | 服务、驱动、设备枚举、ControlSet |
| `HKLM\SOFTWARE` | `C:\Windows\System32\Config\SOFTWARE` | 软件、系统组件、应用兼容性数据 |
| `HKLM\SAM` | `C:\Windows\System32\Config\SAM` | 本地账户数据库 |
| `HKLM\SECURITY` | `C:\Windows\System32\Config\SECURITY` | 安全策略、LSA secret 等 |
| `HKCU` | `C:\Users\<user>\NTUSER.DAT` | 当前用户配置和活动痕迹 |
| `HKCU\Software\Classes` | `C:\Users\<user>\AppData\Local\Microsoft\Windows\UsrClass.dat` | Shell、COM、ShellBag 等用户级数据 |

## 离线分析注意点

- `HKCU` 在离线镜像里不是一个单独文件，需要按用户加载 `NTUSER.DAT`。
- `CurrentControlSet` 是运行时映射，离线分析时应结合 `SYSTEM\Select` 判断当前 control set。
- 64 位系统存在 WOW64 注册表重定向，`HKLM\Software\Wow6432Node` 代表 32 位视图。
- hive transaction log 可能包含尚未合并的历史状态。

