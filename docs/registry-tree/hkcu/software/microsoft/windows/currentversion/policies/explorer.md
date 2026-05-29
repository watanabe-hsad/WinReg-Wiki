# HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer` |
| HKU | `HKU\<SID>\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer` |
| 离线 | `NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer` |

## 离线位置

`C:\Users\<User>\NTUSER.DAT`

## 作用

保存用户级 Explorer / Shell 策略。常用于限制开始菜单、运行框、控制面板、驱动器显示或访问等用户界面行为。

## 常见子键和值

| 名称 | 类型 | 含义 | 常见数据 / 状态 | 说明 |
|---|---|---|---|---|
| `NoRun` | `REG_DWORD` | 限制运行对话框相关策略。 | `0` / `1` | 需结合组策略来源。 |
| `NoDrives` | `REG_DWORD` | 隐藏指定驱动器。 | 位掩码 | 隐藏不等于禁止底层访问。 |
| `NoViewOnDrive` | `REG_DWORD` | 限制访问指定驱动器。 | 位掩码 | 与 `NoDrives` 含义不同。 |
| `NoControlPanel` | `REG_DWORD` | 限制控制面板 / 设置入口。 | `0` / `1` | 版本表现可能不同。 |
| `NoFolderOptions` | `REG_DWORD` | 限制文件夹选项入口。 | `0` / `1` | 常见于受管终端。 |

## 默认状态与版本差异

未配置策略的用户通常没有这些值。Explorer 策略行为随 Windows 版本、Shell UI、GPO 模板和企业管理方式变化。

## 注意事项

- 这些值主要影响用户界面和用户范围策略，不等于底层文件系统事件。
- `NoDrives`、`NoViewOnDrive` 是位掩码，解释时需保留原始值并转换。
- 策略可能来自 GPO、MDM、本地策略、管理工具或镜像基线。

## 取证提示

- 可辅助解释用户为什么看不到运行框、控制面板或特定驱动器。
- 需与 GroupPolicy、Shell 行为、用户 hive LastWrite 和管理员操作记录交叉验证。

## 相关场景

- [Shell / Explorer 用户行为](../../../../../../../questions/shell-explorer.md)
- [安全策略与防护配置](../../../../../../../questions/policy-security.md)
- [反取证与清理痕迹](../../../../../../../questions/anti-forensics.md)
- [常规注册表检查](../../../../../../../questions/registry-checklist.md)

## 相关位置

- [HKCU Policies](../policies.md)
- [HKCU Explorer](../explorer.md)
- [HKLM Policies](../../../../../../hklm/software/policies.md)

## 补充阅读

- [Microsoft Learn: Policy CSP - ADMX Explorer](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-admx-explorer)
