# HKLM\SYSTEM\ControlSet00x\Control\Session Manager

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SYSTEM\CurrentControlSet\Control\Session Manager` |
| 离线 | `SYSTEM\ControlSet00x\Control\Session Manager` |

## 离线位置

`C:\Windows\System32\Config\SYSTEM`

## 作用

保存 Session Manager 子系统相关配置，包括启动阶段执行项、对象管理器相关列表、系统级环境变量和延迟文件操作队列。该位置靠近系统启动和会话初始化流程，解释时需要区分“配置存在”和“已经执行 / 生效”。

## 常见子键和值

| 名称 | 类型 | 含义 | 常见数据 / 状态 | 说明 |
|---|---|---|---|---|
| `AppCertDlls` | Key | AppCert DLL 配置。 | 默认通常为空或不存在 | 非空时需验证 DLL 来源。 |
| `BootExecute` | `REG_MULTI_SZ` | 启动早期执行项。 | `autocheck autochk *` 常见 | 异常条目需验证文件和来源。 |
| `KnownDLLs` | Key | Known DLL 对象名到 DLL 文件名映射。 | 系统维护 | 影响系统 DLL 解析。 |
| `PendingFileRenameOperations` | `REG_MULTI_SZ` | 下次重启处理的重命名 / 删除队列。 | 安装、更新、卸载时常见 | 不等于操作已经完成。 |
| `Environment` | Key | 系统级环境变量。 | 视系统和软件而定 | 与 HKCU 环境变量组合。 |
| `Memory Management` | Key | 内存管理相关配置。 | 系统维护 | 本站暂未展开。 |
| `AppCompatCache` | Key / Value | ShimCache / AppCompatCache 数据位置。 | 版本相关 | 需专门工具解析。 |

## 默认状态与版本差异

Session Manager 子键和值随 Windows 版本、角色、更新状态和已安装软件变化。默认 `BootExecute` 常见为 `autocheck autochk *`，但不要把单一基线当作所有系统的绝对状态。

## 注意事项

- 离线分析必须先用 `HKLM\SYSTEM\Select` 确定当前控制集。
- `PendingFileRenameOperations` 说明队列存在，不证明重启后已经执行。
- KnownDLLs 异常需要结合文件系统、签名和内存模块证据。

## 取证提示

- 可辅助检查启动阶段执行、系统级环境污染、待删除文件和 DLL 解析相关配置。
- 发现异常项后，应回到具体子页面和场景页做边界判断。

## 相关场景

- [自启动与持久化](../../../../../../questions/persistence.md)
- [程序执行痕迹](../../../../../../questions/execution.md)
- [反取证与清理痕迹](../../../../../../questions/anti-forensics.md)
- [常规注册表检查](../../../../../../questions/registry-checklist.md)

## 相关位置

- [ControlSet00x](../../index.md)
- [AppCertDlls](appcertdlls.md)
- [Services](../../services/index.md)
- [LSA](../lsa/index.md)
- [HKLM Environment](environment.md)

## 补充阅读

- [ShimCache artifact](../../../../../../artifacts/execution/shimcache.md)
