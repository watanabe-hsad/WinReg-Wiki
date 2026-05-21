---
tags:
  - Persistence
  - Autoruns
  - HKCU
  - HKLM
---

# Run / RunOnce

此页保留 Run / RunOnce artifact 的补充细节。主入口请先查看注册表位置页和取证场景页。

## 对应注册表位置

| 范围 | 位置 | 说明 |
|---|---|---|
| 用户级 | [HKCU\Software\Microsoft\Windows\CurrentVersion\Run](../../registry-tree/hkcu/software/microsoft/windows/currentversion/run.md) | 当前用户登录自启动。 |
| 机器级 | [HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run](../../registry-tree/hklm/software/microsoft/windows/currentversion/run.md) | 机器级登录自启动。 |
| 32 位视图 | [WOW6432Node](../../registry-tree/hklm/software/wow6432node.md) | 32 位应用写入的 Run 位置可能出现在此视图。 |

## 字段语义

| Key / Value | 类型 | 含义 |
|---|---|---|
| `Run` | Key | 用户登录时加载的常驻启动项。 |
| `RunOnce` | Key | 用户登录后执行一次的启动项。 |
| `<value name>` | `REG_SZ` / `REG_EXPAND_SZ` | 显示名或任意名称。 |
| `<value data>` | 字符串命令 | 可执行文件路径或命令行。 |

## 采集与工具

```cmd
reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Run"
reg query "HKLM\Software\Microsoft\Windows\CurrentVersion\Run"
```

- Autoruns：适合 live 系统快速枚举自启动位置。
- Registry Explorer / RECmd：适合离线 hive 和 LastWrite。
- KAPE / Velociraptor：跨用户、跨主机采集和基线对比。

## 常见误读

- 启动项存在不等于程序已经执行。
- key LastWrite 不是单个 value 的精确创建时间。
- 正常软件、驱动工具、同步盘、VPN、浏览器和企业代理常写入 Run key。

## 交叉验证

- Prefetch、Amcache、Shimcache、BAM/DAM。
- Sysmon Event ID 1 / 13、Security 4688 / 4657。
- Startup folder、Scheduled Tasks、Services。
- 文件签名、哈希、路径权限和文件系统时间线。

## 相关场景

- [自启动与持久化](../../questions/persistence.md)
- [程序执行痕迹](../../questions/execution.md)
- [常规注册表检查](../../questions/registry-checklist.md)

## 参考资料

- [Microsoft Sysinternals: Autoruns](https://learn.microsoft.com/en-us/sysinternals/downloads/autoruns)
- [MITRE ATT&CK: Registry Run Keys / Startup Folder](https://attack.mitre.org/techniques/T1060/)
