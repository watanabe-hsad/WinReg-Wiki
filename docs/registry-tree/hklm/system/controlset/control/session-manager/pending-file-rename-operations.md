# HKLM\SYSTEM\ControlSet00x\Control\Session Manager\PendingFileRenameOperations

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SYSTEM\CurrentControlSet\Control\Session Manager /v PendingFileRenameOperations` |
| 离线 | `SYSTEM\ControlSet00x\Control\Session Manager /v PendingFileRenameOperations` |

## 离线位置

`C:\Windows\System32\Config\SYSTEM`

## 作用

保存下次重启时处理的文件重命名或删除队列。安装器、更新器、卸载器和系统组件可能在文件被占用时写入该 value，让 Session Manager 在重启早期完成操作。

## 常见子键和值

| 名称 | 类型 | 含义 | 常见数据 / 状态 | 说明 |
|---|---|---|---|---|
| `PendingFileRenameOperations` | `REG_MULTI_SZ` | 待处理文件重命名 / 删除列表。 | 路径成对出现常见 | 空目标常用于删除。 |
| `PendingFileRenameOperations2` | `REG_MULTI_SZ` | 备用或扩展队列。 | 视版本和组件而定 | 不一定存在。 |

## 默认状态与版本差异

正常系统可不存在该 value，或在安装、更新、卸载后短暂存在。格式和路径表现随 Windows 版本、安装器和 API 使用方式变化。

## 注意事项

- 队列存在不等于文件已经删除或重命名；需要确认是否发生重启和文件系统结果。
- 正常更新、驱动安装、卸载软件和安全产品升级都可能写入该 value。
- 路径可能使用 NT native path，需要工具或人工转换。

## 取证提示

- 指向日志、恶意载荷、驱动文件、安全工具文件或临时目录时，可作为清理或替换计划线索。
- 与 `$MFT`、`$UsnJrnl`、安装日志、重启时间和服务/驱动配置一起看。

## 相关场景

- [反取证与清理痕迹](../../../../../../questions/anti-forensics.md)
- [软件安装与卸载](../../../../../../questions/software-install.md)
- [自启动与持久化](../../../../../../questions/persistence.md)
- [常规注册表检查](../../../../../../questions/registry-checklist.md)

## 相关位置

- [Session Manager](index.md)
- [EventLog](../../services/eventlog.md)
- [Drivers](../../services/drivers.md)

## 补充阅读

- [Microsoft Learn: MoveFileExW](https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-movefileexw)
