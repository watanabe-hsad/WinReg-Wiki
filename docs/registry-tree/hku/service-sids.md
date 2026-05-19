# HKEY_USERS 服务账户 SID

`HKEY_USERS` 中的服务账户 SID 表示系统内置服务账户的用户 hive 视图。

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKEY_USERS\S-1-5-18`、`HKEY_USERS\S-1-5-19`、`HKEY_USERS\S-1-5-20` |
| 离线 | 取决于账户和加载状态；常见配置来自系统 hive 或服务账户 profile |

## 常见子键 / value

| 名称 | 类型 | 含义 |
|---|---|---|
| `S-1-5-18` | Key | Local System。 |
| `S-1-5-19` | Key | Local Service。 |
| `S-1-5-20` | Key | Network Service。 |
| `Software` | Key | 该账户上下文下的软件配置。 |
| `Environment` | Key | 该账户上下文下的环境变量。 |

## 说明

| 项 | 内容 |
|---|---|
| 数据来源 | live 已加载 hive；离线来源需结合账户 profile 和系统配置确认。 |
| 常见写入者 | Windows 服务、系统组件、以服务账户运行的应用。 |
| 注意 | 服务账户的 `HKCU` 与普通交互式用户不同；live 采集时应记录执行上下文。 |

## 相关 Artifact

- [Command Processor AutoRun](../../artifacts/persistence/command-processor-autorun.md)
- [ProfileList](../../artifacts/security/profilelist.md)
