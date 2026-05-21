# HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList` |
| 离线 | `SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList` |

## 离线位置

`C:\Windows\System32\Config\SOFTWARE`

## 作用

`ProfileList` 保存 SID 到用户 profile 目录的映射。它用于把机器级账户标识、用户目录、`NTUSER.DAT` 和 `UsrClass.dat` 关联起来。

## 常见子键和值

| 名称 | 类型 | 含义 | 常见数据 / 状态 | 说明 |
|---|---|---|---|---|
| `<SID>` | Key | 单个用户、服务账户或系统账户 profile 记录。 | `S-1-5-21-...`、`S-1-5-18` 等 | 不要把所有 SID 都当作交互用户。 |
| `ProfileImagePath` | `REG_EXPAND_SZ` | profile 目录路径。 | `%SystemDrive%\Users\<User>` | 可能指向临时、漫游或 VDI profile。 |
| `Flags` | `REG_DWORD` | profile 标志字段。 | 视版本和状态而定 | 需用工具或基线解释。 |
| `State` | `REG_DWORD` | profile 加载 / 卸载相关状态。 | 视状态而定 | 不等同于登录成功时间。 |
| `ProfileLoadTimeHigh` / `ProfileLoadTimeLow` | `REG_DWORD` | 部分版本存在的 profile 加载时间字段。 | FILETIME 高低位 | 需工具解析。 |
| `.bak` 子键 | Key | profile 重建或临时 profile 线索。 | `<SID>.bak` | 需结合 User Profile Service 日志。 |

## 默认状态与版本差异

常见交互用户、系统账户和服务账户都可能出现在该位置。`State`、`Flags`、加载时间字段和 `.bak` 行为随 Windows 版本、域环境、漫游 profile、FSLogix / VDI 和 profile 修复流程变化。

## 注意事项

- ProfileList 记录不等于账户当前仍存在于 SAM 或域中。
- SID 子键 LastWrite 不等于用户首次登录或最后登录时间。
- 目录名不能直接当作账户名，需要结合 SID、SAM、域记录和登录事件。

## 取证提示

- 解析用户级 hive 前，先用 `ProfileList` 建立 SID 与目录映射。
- 非标准 `ProfileImagePath`、`.bak` 子键、临时 profile 和删除用户残留可作为账户调查线索。

## 相关场景

- [账户与安全](../../../../../../questions/accounts-security.md)
- [Shell / Explorer 用户行为](../../../../../../questions/shell-explorer.md)
- [常规注册表检查](../../../../../../questions/registry-checklist.md)

## 相关位置

- [HKEY_USERS](../../../../../hku/index.md)
- [HKU SID 映射](../../../../../hku/sid-mapping.md)
- [NTUSER.DAT](../../../../../hku/ntuser.md)
- [UsrClass.dat](../../../../../hku/usrclass.md)

## 补充阅读

- [ProfileList artifact](../../../../../../artifacts/security/profilelist.md)
