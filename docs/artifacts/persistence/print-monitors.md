---
tags:
  - Persistence
  - Print
  - Services
  - SYSTEM
  - HKLM
---

# Print Monitors

<div class="rfh-meta" markdown>
<span class="rfh-badge high">取证价值 高</span>
<span class="rfh-badge high">检测价值 高</span>
<span class="rfh-badge">Spooler DLL 加载</span>
</div>

## 摘要

`Print\Monitors` 定义打印端口监视器 DLL，异常 `Driver` 可使 Spooler 在系统上下文加载非基线 DLL。

## 注册表路径

| 视图 | Hive / 文件 | 路径 | Value | 范围 |
|---|---|---|---|---|
| Live path | `HKLM\SYSTEM` | `CurrentControlSet\Control\Print\Monitors\<MonitorName>` | `Driver` | 机器级 |
| Offline hive path | `SYSTEM` | `ControlSet00x\Control\Print\Monitors\<MonitorName>` | `Driver` | 机器级，需解析 `Select` |

## 原生注册表视图

在 `regedit.exe` 中展开 `HKLM\SYSTEM\CurrentControlSet\Control\Print\Monitors`。每个子键通常代表一个端口监视器，`Driver` 指定 DLL 名或路径。

## 离线位置

离线文件为 `C:\Windows\System32\Config\SYSTEM`。先解析 `HKLM\SYSTEM\Select\Current`，必要时比较多个 ControlSet。

## 字段含义

| 字段 | 含义 |
|---|---|
| `<MonitorName>` | 端口监视器名称，例如本地端口、标准 TCP/IP 端口或厂商组件。 |
| `Driver` | 监视器 DLL 名或路径，常见位于 `System32`。 |
| key LastWrite | 监视器配置最近变化，不等同 DLL 加载时间。 |

## 取证含义

该配置可证明系统注册了打印端口监视器。Spooler 服务运行时可能加载对应 DLL，因此异常监视器是持久化和权限提升调查的重要入口。是否已加载要结合 Spooler 状态、模块加载和打印事件。

## 可以证明

- 系统配置了哪些 Print Monitors。
- `Driver` 指向的 DLL 名称或路径。
- 是否存在非基线、无签名或异常路径的监视器 DLL。

## 不能证明

- 不能单独证明 DLL 已被 Spooler 加载。
- 不能单独证明打印任务发生。
- 不能只凭非 Microsoft 名称判断恶意，打印机厂商组件很常见。

## 时间戳说明

子键 LastWrite 可用于定位监视器配置变化。DLL 文件时间线、Spooler 启动时间和模块加载时间需要另行采集。离线非当前 ControlSet 的 LastWrite 只描述对应控制集。

## 系统版本差异

Windows 7 / 10 / 11 / Server 都可能存在该路径。默认监视器、打印子系统限制和 PrintNightmare 后的安全策略差异需按版本和补丁级别验证。

## 攻击滥用

攻击者可创建恶意 monitor 子键并设置 `Driver` 为 DLL，使 Spooler 以高权限加载该 DLL。该方式通常需要管理员权限，并可能配合重启 Spooler 或系统重启。

## 检测思路

- 新增 `Control\Print\Monitors\<Name>\Driver`。
- `Driver` 指向用户可写目录、临时目录、网络路径或无签名 DLL。
- Spooler 服务启动后加载非基线 DLL。
- 注册表修改进程不是打印机安装器、驱动安装器或管理工具。

## 常见误报

- 打印机驱动、PDF 打印器、扫描仪、厂商打印管理软件、企业打印服务器组件。
- 系统更新、驱动升级或 Point and Print 部署。
- VDI、远程桌面打印重定向和第三方打印代理。

## 采集方式

=== "PowerShell"

    ```powershell
    Get-ChildItem "HKLM:\SYSTEM\CurrentControlSet\Control\Print\Monitors" |
      ForEach-Object { Get-ItemProperty $_.PsPath | Select-Object PSChildName, Driver }
    ```

=== "reg.exe"

    ```cmd
    reg query "HKLM\SYSTEM\CurrentControlSet\Control\Print\Monitors" /s
    ```

=== "Offline"

    ```text
    Collect SYSTEM hive, System.evtx, PrintService logs, and suspected monitor DLL files.
    ```

## 解析工具

- Autoruns / Autorunsc
- Registry Explorer
- RECmd
- KAPE
- Velociraptor

## 交叉验证

- System.evtx Spooler 服务启动/停止。
- Microsoft-Windows-PrintService/Admin and Operational。
- Sysmon Event ID 7、13、11。
- DLL 签名、哈希、文件系统时间线。
- EDR module telemetry 和服务状态。

## 示例结论

- `Control\Print\Monitors\Update Monitor` 的 `Driver` 指向 `C:\Users\Public\spool.dll`，可证明 Spooler 加载链中注册了非基线 monitor；是否加载需用 Spooler 模块证据确认。
- 该 monitor 子键 LastWrite 与打印机驱动安装时间一致，且 DLL 为厂商签名组件，当前更符合正常驱动安装。

## 参考资料

- [MITRE ATT&CK: Port Monitors](https://attack.mitre.org/techniques/T1547/010/)
- [Microsoft Learn: MONITORREG structure](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/winsplp/ns-winsplp-_monitorreg)
- [Microsoft Sysinternals: Autoruns](https://learn.microsoft.com/en-us/sysinternals/downloads/autoruns)

## 相关页面

- 场景：[自启动与持久化](../../questions/persistence.md)
- 注册表位置：[HKLM\SYSTEM\ControlSet00x\Control\Print\Monitors](../../registry-tree/hklm/system/print-monitors.md)

