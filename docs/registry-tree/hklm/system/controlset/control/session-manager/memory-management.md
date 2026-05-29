# HKLM\SYSTEM\ControlSet00x\Control\Session Manager\Memory Management

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management` |
| 离线 | `SYSTEM\ControlSet00x\Control\Session Manager\Memory Management` |

## 离线位置

`C:\Windows\System32\Config\SYSTEM`

## 作用

保存内存管理相关配置，包括分页文件、关机清理 pagefile、内核分页和系统缓存等行为。它描述系统内存管理策略，不保存内存内容。

## 常见子键和值

| 名称 | 类型 | 含义 | 常见数据 / 状态 | 说明 |
|---|---|---|---|---|
| `PagingFiles` | `REG_MULTI_SZ` | 分页文件路径和大小配置。 | `C:\pagefile.sys ...` 常见 | 具体格式随配置而定。 |
| `ExistingPageFiles` | `REG_MULTI_SZ` | 已存在分页文件记录。 | 视系统状态而定 | 不等同当前内存内容。 |
| `ClearPageFileAtShutdown` | `REG_DWORD` | 关机时清理 paging file 的策略。 | `0` / `1` | `1` 通常表示关机清理 pagefile。 |
| `DisablePagingExecutive` | `REG_DWORD` | 内核和驱动分页相关配置。 | 视系统和策略而定 | 不应脱离性能/版本语境解释。 |
| `LargeSystemCache` | `REG_DWORD` | 系统缓存行为相关配置。 | 视 SKU 和角色而定 | Server / Client 基线不同。 |

## 默认状态与版本差异

默认值随 Windows 版本、SKU、物理内存、系统托管分页文件、服务器角色和安全基线变化。`ClearPageFileAtShutdown` 可能由本地安全策略或 GPO 配置。

## 注意事项

- 这里是内存管理配置，不是内存取证数据。
- `ClearPageFileAtShutdown=1` 说明关机清理策略，不证明某次关机已经发生。
- 离线分析仍需根据 `SYSTEM\Select` 找到当前控制集。

## 取证提示

- `ClearPageFileAtShutdown` 可作为 pagefile 取证可用性和清理策略线索。
- 分页文件路径变化应与磁盘文件、系统事件和策略来源一起看。

## 相关场景

- [反取证与清理痕迹](../../../../../../questions/anti-forensics.md)
- [网络与系统环境](../../../../../../questions/network.md)
- [常规注册表检查](../../../../../../questions/registry-checklist.md)

## 相关位置

- [Session Manager](index.md)
- [PendingFileRenameOperations](pending-file-rename-operations.md)
- [HKLM\SYSTEM](../../../index.md)

## 补充阅读

- [Microsoft Learn: Clear virtual memory pagefile](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/jj852241(v=ws.11))
