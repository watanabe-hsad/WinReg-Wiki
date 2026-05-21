# 程序执行痕迹

## 检查目标

判断某个程序是否存在过、是否可能在某个用户上下文中执行过，以及注册表线索能支持到什么强度。

## 优先查看的注册表位置

| 注册表位置 | 用途 | 判断边界 |
|---|---|---|
| [UserAssist](../registry-tree/hkcu/software/microsoft/windows/currentversion/userassist.md) | Explorer / Shell 相关用户交互记录。 | 不覆盖命令行、服务、计划任务等所有执行方式。 |
| [Command Processor](../registry-tree/hkcu/software/microsoft/command-processor.md) | 用户级 `cmd.exe` `AutoRun` 和命令处理器配置。 | 证明配置存在，不证明 `cmd.exe` 已启动。 |
| [HKCU Environment](../registry-tree/hkcu/environment.md) | 用户级 `Path`、`TEMP`、自定义变量。 | 说明执行环境，不证明执行。 |
| [HKLM Environment](../registry-tree/hklm/system/controlset/control/session-manager/environment.md) | 系统级 `Path`、`ComSpec`、`PATHEXT`。 | 需结合具体进程环境。 |
| [HKLM\SYSTEM\Services](../registry-tree/hklm/system/controlset/services/index.md) | BAM / DAM、服务、驱动和网络组件配置所在控制集。 | `Services\bam` 是运行线索；普通服务项只证明配置存在。 |
| [Drivers](../registry-tree/hklm/system/controlset/services/drivers.md) | driver service 配置。 | 要证明加载需结合驱动加载事件或内存/模块证据。 |
| [HKLM Uninstall](../registry-tree/hklm/software/microsoft/windows/currentversion/uninstall.md) | 软件安装登记和路径线索。 | 证明安装登记，不证明执行。 |
| [HKCU Explorer](../registry-tree/hkcu/software/microsoft/windows/currentversion/explorer.md) | Shell 相关用户行为入口。 | 需要细分 UserAssist、RecentDocs、RunMRU、ComDlg32。 |
| [HKU / NTUSER.DAT](../registry-tree/hku/ntuser.md) | 用户级 hive 来源。 | 多用户机器必须先映射 SID。 |

## 判断要点

- UserAssist 与 Prefetch、BAM / DAM、进程日志指向同一程序、同一 SID 和接近时间时，程序执行判断更稳。
- `cmd.exe` AutoRun、`Path` 和 `ComSpec` 解释执行环境；是否触发要看进程创建和命令行。
- 只有 ShimCache、MUICache、Uninstall 或 Amcache 时，优先写“程序存在 / 被记录过 / 安装登记存在”。
- 对驱动、AppInit_DLLs、Print Monitors、LSA 包，先写“加载配置存在”；是否加载要另证。
- 路径位于 `%AppData%`、`%Temp%`、`Downloads`、可移动盘或网络共享时，应记录来源路径和文件系统时间线。

## 交叉验证

- Prefetch、SRUM、Amcache、ShimCache、BAM / DAM。
- Sysmon Event ID 1 / 6 / 7 / 11 / 12 / 13、Security 4688、EDR process telemetry。
- `$MFT`、`$UsnJrnl`、LNK、Jump Lists、下载记录。
- 服务和驱动加载：System.evtx、CodeIntegrity/Operational、DriverFrameworks。

## 常见误判

- UserAssist 的运行次数不一定等于真实执行次数。
- ShimCache 和 MUICache 不能单独证明程序执行。
- Amcache 更偏程序存在和元数据；不同 Windows 版本字段语义不同。
- key LastWrite 不能当作某个 value 的创建时间。

## 相关场景

- [Shell / Explorer 用户行为](shell-explorer.md)
- [自启动与持久化](persistence.md)
- [软件安装与卸载](software-install.md)
- [常规注册表检查](registry-checklist.md)

## 补充阅读

- [UserAssist artifact](../artifacts/execution/userassist.md)
- [BAM / DAM artifact](../artifacts/execution/bam-dam.md)
- [Amcache artifact](../artifacts/execution/amcache.md)
- [ShimCache artifact](../artifacts/execution/shimcache.md)
- [MUICache artifact](../artifacts/execution/muicache.md)
