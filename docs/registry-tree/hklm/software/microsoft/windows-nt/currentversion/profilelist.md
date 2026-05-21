# HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList

`ProfileList` 保存 SID 到用户 profile 路径的映射。

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList` |
| 离线 | `SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList` |

## 常见子键 / value

| 名称 | 类型 | 含义 |
|---|---|---|
| `<SID>` | Key | 单个用户或服务账户 profile 配置。 |
| `ProfileImagePath` | `REG_EXPAND_SZ` | 用户 profile 目录。 |
| `Flags` | `REG_DWORD` | Profile 状态标志。 |
| `State` | `REG_DWORD` | Profile 加载 / 卸载相关状态。 |
| `Sid` | `REG_BINARY` | 二进制 SID。 |

## 说明

| 项 | 内容 |
|---|---|
| 数据来源 | `SOFTWARE` hive。 |
| 常见写入者 | User Profile Service、登录流程、profile 创建/迁移流程。 |
| 注意 | 多用户分析时先用这里映射 SID 和目录，再解析对应 `NTUSER.DAT` / `UsrClass.dat`。 |

## 相关场景

- [账户与安全](../../../../../../questions/accounts-security.md)
- [常规注册表检查](../../../../../../questions/registry-checklist.md)
- [Shell / Explorer 用户行为](../../../../../../questions/shell-explorer.md)

## 补充阅读

- [ProfileList](../../../../../../artifacts/security/profilelist.md)
- [UserAssist](../../../../../../artifacts/execution/userassist.md)
- [Terminal Server Client](../../../../../../artifacts/rdp/terminal-server-client.md)
