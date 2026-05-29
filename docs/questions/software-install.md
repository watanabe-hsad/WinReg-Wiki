# 软件安装与卸载

## 检查目标

区分软件安装登记、程序文件存在、程序执行和用户见过程序这些不同证据语义。

## 优先查看的注册表位置

| 注册表位置 | 用途 | 判断边界 |
|---|---|---|
| [HKLM Uninstall](../registry-tree/hklm/software/microsoft/windows/currentversion/uninstall.md) | 机器级软件安装 / 卸载登记。 | 不证明程序当前仍安装或执行过。 |
| [HKLM\SOFTWARE](../registry-tree/hklm/software/index.md) | 软件、策略、Classes、Winlogon 等机器级入口。 | 需要进入具体子路径解释。 |
| [WOW6432Node](../registry-tree/hklm/software/wow6432node.md) | 32 位应用注册表视图。 | 64 位系统需同时检查。 |
| [App Paths](../registry-tree/hklm/software/microsoft/windows/currentversion/app-paths.md) | 应用程序注册路径。 | 注册路径不等于程序执行。 |
| [AppCompatFlags](../registry-tree/hkcu/software/microsoft/windows-nt/currentversion/appcompatflags.md) | 用户级兼容性配置和 PCA 记录。 | 更偏程序存在 / 交互线索。 |
| [HKLM AppCompatFlags](../registry-tree/hklm/software/microsoft/windows-nt/currentversion/appcompatflags.md) | 机器级兼容性配置入口。 | 可能来自兼容性数据库或安装过程。 |
| [AppCompatFlags\Layers](../registry-tree/hklm/software/microsoft/windows-nt/currentversion/appcompatflags/layers.md) | 机器级兼容层配置。 | 路径记录不等于程序当前存在。 |
| [UserAssist](../registry-tree/hkcu/software/microsoft/windows/currentversion/userassist.md) | 用户 Shell 交互程序线索。 | 不覆盖所有执行方式。 |
| [HKCU Run](../registry-tree/hkcu/software/microsoft/windows/currentversion/run.md) | 用户级安装器或应用自启动。 | 配置存在不等于执行成功。 |

## 判断要点

- `DisplayName`、`DisplayVersion`、`Publisher`、`InstallLocation`、`InstallDate`、`UninstallString` 和 App Paths 默认路径要一起看。
- `InstallDate` 是安装器写入的字符串，可靠性取决于安装器。
- 便携软件可能没有 Uninstall 记录，但会出现在 Amcache、Prefetch、UserAssist、AppCompatFlags 或文件系统时间线。
- 卸载后 Uninstall 记录可能被删除，残留证据需要从文件系统和执行 artifact 还原。

## 交叉验证

- MSI logs、Windows Installer events、Program Files、Start Menu、服务、计划任务。
- Amcache、ShimCache、Prefetch、BAM / DAM、UserAssist。
- `$MFT`、`$UsnJrnl`、下载记录、浏览器历史、软件自身日志。

## 常见误判

- Uninstall 记录存在不等于软件当前仍存在。
- `InstallDate` 不一定是文件落地时间或首次执行时间。
- 正常远控、VPN、同步盘、压缩工具和管理代理也可能接近调查窗口安装。

## 相关场景

- [程序执行痕迹](execution.md)
- [自启动与持久化](persistence.md)
- [常规注册表检查](registry-checklist.md)

## 补充阅读

- [Amcache artifact](../artifacts/execution/amcache.md)
- [MUICache artifact](../artifacts/execution/muicache.md)
- [UserAssist artifact](../artifacts/execution/userassist.md)
