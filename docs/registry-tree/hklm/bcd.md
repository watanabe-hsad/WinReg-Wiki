# HKLM\BCD00000000

`HKLM\BCD00000000` 是 Boot Configuration Data 被加载后的注册表视图。并非所有分析场景都会看到这个根键，但在启动项、恢复环境、调试启动和安全启动异常调查中很有价值。

## Windows 原生视图

Live 系统中可通过 `bcdedit` 查看 BCD，也可能在注册表中看到 `HKLM\BCD00000000`。不同启动布局、EFI 分区和权限状态会影响可见性。

## 离线 hive 文件来源

| 场景 | 常见文件 |
|---|---|
| BIOS / legacy | 系统分区或启动分区的 `\Boot\BCD` |
| UEFI | EFI System Partition 中的 `\EFI\Microsoft\Boot\BCD` |

BCD 使用 registry hive 格式，但不是 `C:\Windows\System32\Config` 下的常规 hive。离线镜像中需要先确认系统分区和 EFI 分区。

## 典型取证价值

- 检查启动项、默认启动对象、恢复环境、debug settings、testsigning、safeboot 等配置。
- 调查启动级持久化、恢复环境滥用或安全启动被削弱。

## 典型检测价值

- 监控 `bcdedit` 修改、启动调试开启、testsigning 开启、recovery 或 safeboot 异常配置。
- 与命令行日志、EDR 进程事件、启动失败日志结合。

## 常见误判

- IT 维护、驱动开发、故障排查可能合法修改 BCD。
- BCD 时间线需要结合文件系统时间戳和命令执行日志，不能只看最终配置。
- 多系统启动环境中存在多个 BCD 文件，必须确认被调查系统实际使用哪个。

## 重点子路径

| 子路径 / 对象 | 价值 |
|---|---|
| Boot Manager object | 默认启动项、timeout |
| OS Loader object | 内核、启动参数、debug/testsigning |
| Recovery objects | 恢复环境与故障恢复路径 |

## 关联 artifact 页面

当前暂无专门 BCD artifact 页面；优先与进程执行、服务驱动和事件日志交叉验证。

## References

- [Microsoft Learn: BCDEdit command-line options](https://learn.microsoft.com/en-us/windows-hardware/drivers/devtest/bcdedit--set)
