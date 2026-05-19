---
tags:
  - Execution
  - ProgramPresence
  - SYSTEM
  - HKLM
---

# BAM / DAM

<div class="rfh-meta" markdown>
<span class="rfh-badge high">取证价值 高</span>
<span class="rfh-badge medium">检测价值 中</span>
<span class="rfh-badge">用户 SID / 程序执行线索</span>
</div>

## 摘要

BAM / DAM 可在支持的 Windows 版本上为某个 SID 下的可执行路径提供“近期运行过”的强线索，并常带有解析为 FILETIME 的最后活动时间。

## 注册表路径

| View | Hive / File | Path | Scope |
|---|---|---|---|
| Live path | `HKLM\SYSTEM` | `CurrentControlSet\Services\bam\State\UserSettings\<SID>` | 用户 SID 维度 |
| Live path | `HKLM\SYSTEM` | `CurrentControlSet\Services\dam\State\UserSettings\<SID>` | 用户 SID 维度，较少见 |
| Offline hive path | `SYSTEM` | `ControlSet00x\Services\bam\State\UserSettings\<SID>` | 离线需先解析 `Select` |
| Offline hive path | `SYSTEM` | `ControlSet00x\Services\dam\State\UserSettings\<SID>` | 离线需先解析 `Select` |

## 原生注册表视图

在 live 系统中通常从 `HKLM\SYSTEM\CurrentControlSet\Services\bam\State\UserSettings` 展开。每个 SID 子键下的 value name 通常是 NT device path 风格的程序路径，例如 `\Device\HarddiskVolume3\Users\...\AppData\...\tool.exe`。

## 离线位置

离线镜像中对应 `C:\Windows\System32\Config\SYSTEM`。不要直接查 `CurrentControlSet`，先读取 `HKLM\SYSTEM\Select`，把 `Current` 对应到 `ControlSet00x`。SID 到用户目录需要用 [ProfileList](../security/profilelist.md) 交叉映射。

## 字段含义

| Field | Meaning |
|---|---|
| SID 子键 | 记录归属的用户 SID；系统账户和服务账户也可能出现 |
| value name | 可执行文件路径，常为 `\Device\HarddiskVolumeX\...` 格式 |
| value data | 二进制数据，常由工具解析出最后执行或最后活动时间；具体偏移和语义依版本与 parser |
| key LastWrite | 该 SID 子键内容变化时间，不是单个 value 的创建时间 |

## 取证含义

BAM / DAM 通常用于辅助判断某个用户上下文中是否运行过某个程序。它比“文件存在”更接近执行，但仍应与 Prefetch、Amcache、UserAssist、SRUM、事件日志或 EDR 进程事件交叉验证。对无 Prefetch 的服务器、SSD 场景或短生命周期工具，BAM 可能提供有价值补充。

## 可以证明

- 某个 SID 下存在与可执行路径相关的 BAM / DAM 记录。
- 在工具可解析的版本上，可辅助证明该程序近期在该用户上下文中运行或活跃过。
- 可将程序路径与用户 SID、卷路径和大致时间放入时间线。

## 不能证明

- 不能单独证明用户有意双击或前台交互。
- 不能覆盖所有执行方式、所有 Windows 版本和所有程序类型。
- 不能仅凭 value name 证明文件仍存在或路径仍映射到同一卷。
- 不能把 key LastWrite 当作某个程序的精确执行时间。

## 时间戳说明

常见 parser 会从 value data 中解析 FILETIME，并按 UTC 或本地时区显示。报告中应写明工具、版本和时区。key LastWrite 只能说明 SID 子键最近被修改，可能由新增、删除或更新任意 value 触发。`ControlSet00x` 的选择错误会导致读取到非当前控制集的旧状态。

## 系统版本差异

BAM 主要见于 Windows 10 及后续版本；Windows 7 不应预期存在同等语义的 BAM 记录。不同 Windows 10/11 build、Server 版本和电源管理策略下覆盖范围可能变化；具体偏移和时间语义以 parser 说明和样本验证为准。DAM 的可见性和价值通常低于 BAM，未命中不代表未执行。

## 攻击滥用

攻击者不需要主动写入 BAM；执行落地工具、LOLBin 或临时 payload 后，系统可能自动留下记录。攻击者可能通过清理对应 SID 子键、删除整个 BAM value、使用内存执行或 LOLBin 代理执行来降低直接路径暴露。

## 检测思路

- BAM value path 指向 `%AppData%`、`%Temp%`、`Downloads`、`ProgramData` 可写子目录或可疑随机目录。
- 短时间内出现新 BAM 记录，同时有 `powershell.exe`、`wscript.exe`、`mshta.exe`、`rundll32.exe`、`regsvr32.exe`、压缩包释放或网络连接。
- 同一 SID 下出现大量一次性路径、已删除路径或工具链命名，例如 `rclone.exe`、`procdump.exe`、`mimikatz.exe`、`nanodump.exe`。
- Sysmon Event ID 13 监控 `\Services\bam\State\UserSettings\` 下 value set，结合 Event ID 1 进程创建。

## 常见误报

- 软件更新器、浏览器下载器、会议软件、压缩工具、企业管理脚本会在用户目录下执行。
- 安全产品、EDR、IT 运维工具可能短时间执行多个辅助程序。
- 便携软件和开发工具常位于用户 profile 或 `Downloads`，需要结合签名、父进程和用户活动判断。

## 采集方式

=== "PowerShell"

    ```powershell
    Get-ChildItem "HKLM:\SYSTEM\CurrentControlSet\Services\bam\State\UserSettings" -ErrorAction SilentlyContinue |
      ForEach-Object { Get-ItemProperty $_.PsPath }
    ```

=== "reg.exe"

    ```cmd
    reg query "HKLM\SYSTEM\CurrentControlSet\Services\bam\State\UserSettings" /s
    reg query "HKLM\SYSTEM\CurrentControlSet\Services\dam\State\UserSettings" /s
    ```

=== "Offline"

    ```text
    Copy C:\Windows\System32\Config\SYSTEM and transaction logs.
    Parse ControlSet00x\Services\bam\State\UserSettings after resolving SYSTEM\Select.
    ```

## 解析工具

- RECmd：适合对 `SYSTEM` hive 批量解析和输出 CSV。
- Registry Explorer：适合人工浏览 value data、LastWrite 和路径。
- RegRipper：可用于插件化解析，覆盖情况取决于插件版本。
- KAPE：可批量采集 `SYSTEM`、事件日志和相关执行 artifact。
- Velociraptor：适合 live hunting 和跨主机注册表查询。

## 交叉验证

- Prefetch：确认程序执行次数、最后运行时间和路径。
- Amcache / ShimCache：确认程序存在、路径和兼容性缓存。
- UserAssist：确认 Explorer 交互执行线索。
- SRUM、Sysmon Event ID 1、Security 4688、EDR process telemetry。
- `$MFT`、`$UsnJrnl`、签名信息和文件哈希。

## 示例结论

- `SYSTEM` hive 的 `Services\bam\State\UserSettings\S-1-5-21-...\` 下存在 `\Device\HarddiskVolume3\Users\alice\AppData\Local\Temp\7zS...\rclone.exe`，parser 显示最后活动时间为 `2026-05-18 14:22:31 UTC`；该证据可辅助证明该 SID 下曾运行该路径程序，但仍需用进程日志或文件系统时间线确认执行链。
- BAM 记录、Prefetch 和 Sysmon Event ID 1 均指向同一路径 `C:\Users\alice\Downloads\updater.exe`，时间相差 2 分钟内，可较稳妥支持“该程序在 alice 用户上下文中执行过”的结论。

## 相关页面

- 场景：[程序执行](../../questions/execution.md)
- 注册表位置：[HKLM\SYSTEM](../../registry-tree/hklm/system.md)、[HKEY_LOCAL_MACHINE](../../registry-tree/hkey-local-machine.md)

## 参考资料

- [artefacts.help: BAM / DAM](https://artefacts.help/windows_registry_bam_dam.html)
- [13Cubed: Windows 10 Program Execution Artifacts](https://www.youtube.com/watch?v=7byz1dR_CLg)
- [Eric Zimmerman tools](https://ericzimmerman.github.io/)
