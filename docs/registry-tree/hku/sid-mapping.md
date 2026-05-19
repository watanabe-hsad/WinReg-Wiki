# HKU SID 映射

用户级注册表分析的第一步是把 `HKU\<SID>` 映射到实际用户目录和账户上下文。没有 SID 映射，`HKCU`、`NTUSER.DAT`、`UsrClass.dat` 的结论都容易写错归属。

## Windows 原生视图

Live 系统中，已加载用户 hive 会显示为 `HKU\<SID>`；当前用户映射为 `HKCU`。`HKU\<SID>_Classes` 通常对应用户的 `UsrClass.dat`。

## 离线 hive 文件来源

| 数据 | 来源 |
|---|---|
| SID 到 profile 目录 | `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList` |
| 用户主 hive | `C:\Users\<user>\NTUSER.DAT` |
| 用户 Classes hive | `C:\Users\<user>\AppData\Local\Microsoft\Windows\UsrClass.dat` |

## 典型取证价值

- 把用户级 artifact 精确归属到 SID 和 profile。
- 发现临时 profile、被删除用户残留、异常 profile 路径。
- 区分本地账户、域账户、服务账户和系统内置 SID。

## 典型检测价值

- 对 profile 路径指向非标准目录或可疑挂载点做狩猎。
- 发现账户新增后短时间内出现用户级持久化或 RDP 历史。

## 常见误判

- `C:\Users\name` 不一定等于当前账户显示名。
- 域账户可能在本地没有 SAM 用户记录。
- 删除账户后 ProfileList、目录和 hive 可能仍有残留。

## 重点子路径

| 子路径 | 价值 | 相关 artifact |
|---|---|---|
| `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList\<SID>` | SID 与用户目录映射 | [ProfileList](../../artifacts/security/profilelist.md) |
| `HKU\<SID>` | 用户主 hive | [NTUSER.DAT](ntuser.md) |
| `HKU\<SID>_Classes` | 用户 Classes hive | [UsrClass.dat](usrclass.md) |

## 关联 artifact 页面

- [ProfileList](../../artifacts/security/profilelist.md)
