# SID 映射

用户级注册表分析需要先把 SID 映射到用户目录。

## 主要路径

```text
HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList\<SID>
```

## 常用 value

| Value | 含义 |
|---|---|
| `ProfileImagePath` | 用户 profile 目录。 |
| `Flags` | profile 标志。 |
| `State` | profile 状态。 |
| `Sid` | 二进制 SID。 |

## 用户 hive

| 注册表视图 | 文件 |
|---|---|
| `HKU\<SID>` | `C:\Users\<user>\NTUSER.DAT` |
| `HKU\<SID>_Classes` | `C:\Users\<user>\AppData\Local\Microsoft\Windows\UsrClass.dat` |

## 注意

| 项 | 说明 |
|---|---|
| `.bak` | 可能表示 profile 修复或临时 profile 情况。 |
| 域用户 | 域用户可能没有本地 SAM 用户记录。 |
| 删除用户 | ProfileList 和目录可能残留。 |

## 补充阅读

[ProfileList](../../artifacts/security/profilelist.md)
