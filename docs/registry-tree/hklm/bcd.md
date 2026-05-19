# HKLM\BCD00000000

`HKLM\BCD00000000` 是 Boot Configuration Data 加载后的注册表视图。

## 文件

| 启动方式 | 常见位置 |
|---|---|
| BIOS / legacy | `\Boot\BCD` |
| UEFI | `\EFI\Microsoft\Boot\BCD` |

BCD 使用 registry hive 格式，但不在 `C:\Windows\System32\Config` 常规 hive 集合中。

## 常用对象

| 对象 | 含义 |
|---|---|
| Boot Manager | 默认启动项、timeout、display order。 |
| OS Loader | 系统加载项、启动参数、debug / testsigning。 |
| Recovery object | 恢复环境配置。 |

## 注意

| 项 | 说明 |
|---|---|
| 查看工具 | live 系统通常用 `bcdedit` 查看。 |
| 多启动 | 多系统环境可能存在多个 BCD 文件。 |
| 配置修改 | 驱动开发、故障排查和维护也会修改 BCD。 |
