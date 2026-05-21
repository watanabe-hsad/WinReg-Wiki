---
tags:
  - Persistence
  - Drivers
  - Services
  - SYSTEM
  - HKLM
---

# Drivers

<div class="rfh-meta" markdown>
<span class="rfh-badge high">取证价值 高</span>
<span class="rfh-badge high">检测价值 高</span>
<span class="rfh-badge">驱动配置</span>
</div>

## 摘要

驱动服务位于 `HKLM\SYSTEM\ControlSet00x\Services`，`Type`、`Start` 和 `ImagePath` 可用于识别 kernel / file system driver 的加载配置。

## 注册表路径

| 视图 | Hive / 文件 | 路径 | Value | 范围 |
|---|---|---|---|---|
| Live path | `HKLM\SYSTEM` | `CurrentControlSet\Services\<DriverName>` | `Type` / `Start` / `ImagePath` | 机器级 |
| Offline hive path | `SYSTEM` | `ControlSet00x\Services\<DriverName>` | `Type` / `Start` / `ImagePath` | 机器级，需解析 `Select` |

## 原生注册表视图

在 `regedit.exe` 中展开 `HKLM\SYSTEM\CurrentControlSet\Services`。驱动与普通服务共享该树，需要通过 `Type` 区分。

## 离线位置

离线文件为 `C:\Windows\System32\Config\SYSTEM`。必须先解析 `HKLM\SYSTEM\Select`，不要假设 `ControlSet001` 一定是当前配置。

## 字段含义

| 字段 | 含义 |
|---|---|
| `Type` | `REG_DWORD`，常见 `1` 为 kernel driver，`2` 为 file system driver，`0x10/0x20` 为 Win32 service。 |
| `Start` | `REG_DWORD`，常见 `0` boot、`1` system、`2` auto、`3` demand、`4` disabled。 |
| `ImagePath` | 驱动文件路径，常见为 `System32\drivers\<name>.sys`。 |
| `Group` | 加载组，影响启动阶段顺序。 |
| `ErrorControl` | 加载失败处理策略。 |
| `Parameters` | 驱动私有参数，含义由驱动决定。 |

## 取证含义

该配置可证明系统存在驱动服务条目以及其加载方式。`Start=0/1/2` 的 kernel/file system driver 更适合优先排查，尤其当 `ImagePath` 指向异常目录、无签名或最近创建的 `.sys` 文件。

## 可以证明

- 系统配置了某个驱动服务。
- 驱动启动类型、镜像路径和加载组。
- 是否存在异常驱动持久化配置或残留。

## 不能证明

- 不能单独证明驱动已成功加载。
- 不能单独证明驱动具备恶意功能。
- 不能只凭 `Start=3` 排除风险，按需加载驱动仍可能被触发。

## 时间戳说明

驱动服务 key LastWrite 支持配置变化分析，不等同驱动加载时间。加载时间应结合 System.evtx、Sysmon Event ID 6、Code Integrity、EDR 和内存证据。

## 系统版本差异

Windows 7 / 10 / 11 / Server 都使用 Services 树保存驱动配置。驱动签名、Kernel Mode Code Signing、HVCI、Secure Boot 和阻止列表行为随版本与策略变化，需按环境验证。

## 攻击滥用

攻击者可安装恶意或易受攻击驱动，用于内核持久化、防护绕过、EDR tampering 或 rootkit 行为。也可能创建残留服务项等待后续触发。

## 检测思路

- 新增 `Type=1/2` 且 `Start=0/1/2` 的服务。
- `ImagePath` 指向用户可写目录、临时目录、非标准扩展或无签名 `.sys`。
- 驱动文件创建后紧接服务 key 创建或修改。
- 关联 Sysmon Event ID 6、Code Integrity 事件和服务控制事件。

## 常见误报

- EDR、VPN、备份软件、磁盘加密、虚拟化、存储驱动、打印驱动、硬件厂商工具。
- Windows Update、驱动更新和 OEM 管理工具。
- 已禁用或卸载残留的旧驱动项。

## 采集方式

=== "PowerShell"

    ```powershell
    Get-ChildItem "HKLM:\SYSTEM\CurrentControlSet\Services" |
      ForEach-Object {
        $p = Get-ItemProperty $_.PsPath -ErrorAction SilentlyContinue
        if ($p.Type -band 0x3) {
          [pscustomobject]@{Name=$_.PSChildName; Type=$p.Type; Start=$p.Start; ImagePath=$p.ImagePath}
        }
      }
    ```

=== "reg.exe"

    ```cmd
    reg query "HKLM\SYSTEM\CurrentControlSet\Services" /s /v ImagePath
    ```

=== "Offline"

    ```text
    Collect SYSTEM hive, System.evtx, CodeIntegrity logs, driver files, and file-system timeline.
    ```

## 解析工具

- Autoruns / Autorunsc
- Registry Explorer
- RECmd
- KAPE
- Velociraptor
- Sigcheck

## 交叉验证

- [Services](services.md)
- Sysmon Event ID 6、7、11、13。
- System.evtx Service Control Manager events。
- Microsoft-Windows-CodeIntegrity/Operational。
- 驱动文件签名、哈希、创建/修改时间、EDR telemetry。

## 示例结论

- `Services\abcdrv` 配置为 `Type=1`、`Start=1`，`ImagePath=\SystemRoot\System32\drivers\abcdrv.sys`，可证明系统存在 system-start kernel driver 配置；是否加载需结合 Sysmon 6 或内存证据确认。
- 该驱动文件无签名且创建时间早于服务 key LastWrite 数分钟，支持“先落地文件、后注册驱动”的时间线判断。

## 参考资料

- [Microsoft Learn: HKLM\SYSTEM\CurrentControlSet\Services Registry Tree](https://learn.microsoft.com/en-us/windows-hardware/drivers/install/hklm-system-currentcontrolset-services-registry-tree)
- [MITRE ATT&CK: Kernel Modules and Extensions](https://attack.mitre.org/techniques/T1547/006/)
- [Microsoft Sysinternals: Autoruns](https://learn.microsoft.com/en-us/sysinternals/downloads/autoruns)

## 相关页面

- 场景：[自启动与持久化](../../questions/persistence.md)、[程序执行](../../questions/execution.md)
- 注册表位置：[HKLM\SYSTEM\ControlSet00x\Services\Drivers](../../registry-tree/hklm/system/controlset/services/drivers.md)

