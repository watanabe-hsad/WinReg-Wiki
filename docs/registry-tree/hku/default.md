# HKEY_USERS\.DEFAULT

`.DEFAULT` 是系统默认账户相关 hive 的 live 挂载视图，不代表所有普通用户的默认设置。

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKEY_USERS\.DEFAULT` |
| 离线 | `C:\Windows\System32\Config\DEFAULT` |

## 常见子键 / value

| 名称 | 类型 | 含义 |
|---|---|---|
| `Control Panel` | Key | 登录界面和系统上下文相关的部分用户界面配置。 |
| `Software` | Key | 系统默认账户的软件配置。 |
| `Keyboard Layout` | Key | 键盘布局相关配置。 |
| `Environment` | Key | 系统默认账户环境变量。 |

## 说明

| 项 | 内容 |
|---|---|
| 数据来源 | `DEFAULT` hive。 |
| 常见写入者 | Windows 安装、登录界面、系统上下文配置。 |
| 注意 | `.DEFAULT` 不是 `C:\Users\Default\NTUSER.DAT`，也不是当前登录用户。 |

## 补充阅读

- 暂无专门 artifact 页面
- [ProfileList](../../artifacts/security/profilelist.md)

