---
tags:
  - Accounts
  - UserProfiles
  - SOFTWARE
  - HKLM
---

# ProfileList

此页保留 `ProfileList` 的补充细节。主入口请先查看注册表位置页和取证场景页。

## 对应注册表位置

| 位置 | 说明 |
|---|---|
| [HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList](../../registry-tree/hklm/software/microsoft/windows-nt/currentversion/profilelist.md) | SID 到用户 profile 目录的机器级映射。 |
| [HKEY_USERS](../../registry-tree/hku/index.md) | 已加载用户 hive 与 SID 视图。 |
| [HKU SID 映射](../../registry-tree/hku/sid-mapping.md) | 将 `HKU\<SID>`、`NTUSER.DAT` 和 `UsrClass.dat` 归属到具体用户。 |

## 字段语义

| 字段 | 类型 | 含义 |
|---|---|---|
| `<SID>` | Key | 用户、服务账户或系统账户的 profile 记录。 |
| `ProfileImagePath` | `REG_EXPAND_SZ` | profile 目录路径，常见为 `C:\Users\<User>`。 |
| `Flags` | `REG_DWORD` | profile 标志字段，需结合版本和工具解释。 |
| `State` | `REG_DWORD` | profile 加载 / 卸载相关状态。 |
| `ProfileLoadTimeHigh` / `ProfileLoadTimeLow` | `REG_DWORD` | 部分版本存在的 profile 加载时间字段。 |
| `.bak` 子键 | Key | profile 重建、临时 profile 或登录异常线索。 |

## 采集与工具

```powershell
Get-ChildItem "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList" |
  ForEach-Object {
    $p = Get-ItemProperty $_.PsPath
    [PSCustomObject]@{
      SID = $_.PSChildName
      ProfileImagePath = $p.ProfileImagePath
      State = $p.State
      Flags = $p.Flags
    }
  }
```

- Registry Explorer / RECmd：查看 SID 子键、value 和 key LastWrite。
- KAPE：采集 `SOFTWARE`、`NTUSER.DAT` 和 `UsrClass.dat`。
- Velociraptor：跨主机枚举 profile 映射和异常路径。

## 常见误读

- ProfileList 记录不等于账户当前仍存在于 SAM 或域中。
- SID 子键 LastWrite 不等于用户首次登录或最后登录时间。
- 服务账户、应用池账户、临时 profile、漫游 profile、FSLogix / VDI 都可能留下记录。
- 目录名不应直接当作账户名，需结合 SID、SAM、域记录和登录事件。

## 交叉验证

- SAM、本地域用户、域控制器登录记录。
- Security.evtx `4624`、`4634`、`4672`。
- User Profile Service operational log。
- `C:\Users\<User>` 目录、`NTUSER.DAT`、`UsrClass.dat` 文件时间线。
- UserAssist、MountPoints2、RDP Client、Run key 等用户级位置。

## 相关场景

- [账户与安全](../../questions/accounts-security.md)
- [Shell / Explorer 用户行为](../../questions/shell-explorer.md)
- [常规注册表检查](../../questions/registry-checklist.md)

## 参考资料

- [artefacts.help: ProfileList](https://artefacts.help/windows_registry_profilelist.html)
- [Microsoft Learn: User profiles](https://learn.microsoft.com/en-us/windows/client-management/client-tools/mandatory-user-profile)
