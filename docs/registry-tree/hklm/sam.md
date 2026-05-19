# HKLM\SAM

`HKLM\SAM` 对应本地 Security Account Manager 数据库。

## 文件

| 项 | 路径 |
|---|---|
| Hive | `C:\Windows\System32\Config\SAM` |
| 常用配套 hive | `SYSTEM`、`SECURITY` |

## 常用路径

| 路径 | 含义 |
|---|---|
| `SAM\SAM\Domains\Account\Users` | 本地用户 RID 和账户记录。 |
| `SAM\SAM\Domains\Account\Users\Names` | 用户名到 RID 的映射。 |
| `SAM\SAM\Domains\Builtin\Aliases` | 内置本地组。 |
| `SAM\SAM\Domains\Account\Aliases` | 本地组。 |

## 注意

| 项 | 说明 |
|---|---|
| 权限 | live 查看通常需要高权限。 |
| 域用户 | 域用户 profile 可能存在，但不一定有本地 SAM 用户。 |
| ProfileList | 用户目录映射在 `HKLM\SOFTWARE\...\ProfileList`，不在 SAM。 |

## 相关 Artifact

[ProfileList](../../artifacts/security/profilelist.md)
