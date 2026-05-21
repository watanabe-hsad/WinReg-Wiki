# HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon

`Winlogon` 保存交互式登录流程相关配置。

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon` |
| 离线 | `SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon` |

## 常见子键 / value

| 名称 | 类型 | 含义 |
|---|---|---|
| `Userinit` | `REG_SZ` | 登录初始化程序列表，默认通常包含 `userinit.exe`。 |
| `Shell` | `REG_SZ` | 用户 Shell，默认通常为 `explorer.exe`。 |
| `AutoAdminLogon` | `REG_SZ` | 自动登录相关开关。 |
| `DefaultUserName` | `REG_SZ` | 自动登录或登录界面相关用户名值。 |
| `SpecialAccounts\UserList` | Key | 登录界面账户显示控制。 |

## 说明

| 项 | 内容 |
|---|---|
| 数据来源 | `SOFTWARE` hive。 |
| 常见写入者 | Windows 登录组件、系统设置、GPO、管理工具。 |
| 注意 | 这里是登录配置，不等同于登录事件；登录是否发生需结合日志。 |

## 相关场景

- [自启动与持久化](../../../../../../questions/persistence.md)
- [账户与安全](../../../../../../questions/accounts-security.md)
- [常规注册表检查](../../../../../../questions/registry-checklist.md)

## 补充阅读

- [Winlogon Userinit](../../../../../../artifacts/persistence/winlogon-userinit.md)
- [Winlogon Shell](../../../../../../artifacts/persistence/winlogon-shell.md)
- [SpecialAccounts\UserList](../../../../../../artifacts/security/specialaccounts-userlist.md)
