# HKEY_USERS

`HKEY_USERS`，简称 `HKU`，显示当前已加载的用户 hive。`HKCU` 是其中某个 `HKU\<SID>` 的映射。

## 常见子项

| 子项 | 含义 | 常见来源 |
|---|---|---|
| [`.DEFAULT`](default.md) | 默认系统账户配置，常用于登录界面和系统上下文。 | `C:\Windows\System32\Config\DEFAULT` |
| [`S-1-5-18`](service-sids.md) | Local System。 | 系统账户 hive |
| [`S-1-5-19`](service-sids.md) | Local Service。 | 服务账户 hive |
| [`S-1-5-20`](service-sids.md) | Network Service。 | 服务账户 hive |
| `<user-SID>` | 普通本地或域用户。 | `C:\Users\<user>\NTUSER.DAT` |
| `<user-SID>_Classes` | 用户级 Classes 视图。 | `C:\Users\<user>\AppData\Local\Microsoft\Windows\UsrClass.dat` |

## 用户映射

SID 到用户目录通常通过：

```text
HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList\<SID>
```

关键 value：

| Value | 含义 |
|---|---|
| `ProfileImagePath` | 用户 profile 目录。 |
| `Flags` | profile 状态标志。 |
| `State` | profile 加载 / 卸载相关状态。 |
| `Sid` | 二进制 SID。 |

## 注意

| 项 | 说明 |
|---|---|
| `.DEFAULT` | 不是所有用户的默认模板，也不是当前登录用户。 |
| 多用户机器 | 每个用户的 `NTUSER.DAT` 和 `UsrClass.dat` 要分开解析。 |
| 临时 profile | `ProfileList` 可能出现 `.bak` 或临时路径。 |
| live `HKU` | 只显示已加载 hive；未登录用户可能不在 live 树中。 |

## 相关页面

[SID 映射](sid-mapping.md),
[NTUSER.DAT](ntuser.md),
[UsrClass.dat](usrclass.md),
[ProfileList](../../artifacts/security/profilelist.md)
