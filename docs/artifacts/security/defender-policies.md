---
tags:
  - SecurityPolicy
  - Defender
  - SOFTWARE
  - HKLM
---

# Defender Policies

<div class="rfh-meta" markdown>
<span class="rfh-badge high">取证价值 高</span>
<span class="rfh-badge high">检测价值 高</span>
<span class="rfh-badge">安全控制策略</span>
</div>

## 摘要

Defender Policies 记录 Microsoft Defender Antivirus 的策略配置；禁用实时保护、添加排除项或削弱扫描策略是常见防御规避线索。

## 注册表路径

| View | Hive / File | Path | Scope |
|---|---|---|---|
| Live path | `HKLM\SOFTWARE` | `Policies\Microsoft\Windows Defender` | 机器级策略 |
| Live path | `HKLM\SOFTWARE` | `Policies\Microsoft\Windows Defender\Real-Time Protection` | 实时保护策略 |
| Live path | `HKLM\SOFTWARE` | `Policies\Microsoft\Windows Defender\Exclusions\Paths` | 路径排除 |
| Live path | `HKLM\SOFTWARE` | `Policies\Microsoft\Windows Defender\Exclusions\Extensions` | 扩展名排除 |
| Live path | `HKLM\SOFTWARE` | `Policies\Microsoft\Windows Defender\Exclusions\Processes` | 进程排除 |
| Offline hive path | `SOFTWARE` | `Policies\Microsoft\Windows Defender\...` | 机器级 |

## 原生注册表视图

在 `regedit.exe` 中从 `HKLM\SOFTWARE\Policies\Microsoft\Windows Defender` 展开。该区域通常由 GPO、MDM、Defender 管理平台、本地管理员或攻击者写入。

## 离线位置

离线文件为 `C:\Windows\System32\Config\SOFTWARE`。若调查策略来源，需要同时收集 Group Policy 文件、MDM 诊断日志、Defender Operational 日志和安全产品控制台记录。

## 字段含义

| Field | Meaning |
|---|---|
| `DisableAntiSpyware` | 历史上用于禁用 Defender 的策略；新版本语义受 Tamper Protection 和平台版本影响 |
| `DisableRealtimeMonitoring` | 实时保护相关策略，常见于 `Real-Time Protection` 子键 |
| `DisableBehaviorMonitoring` | 行为监控相关策略 |
| `Exclusions\Paths` | 路径排除项，value name 通常为路径 |
| `Exclusions\Extensions` | 扩展名排除项 |
| `Exclusions\Processes` | 进程排除项 |
| key LastWrite | 策略 key 最近变化时间，不等于某个排除项精确创建时间 |

## 取证含义

这些 key 可证明 Defender 策略在本机注册表中存在。高风险证据包括排除用户可写目录、攻击工具目录、整个盘符、脚本扩展名，或禁用实时/行为监控。由于企业环境经常通过 GPO/MDM 管理 Defender，必须先区分授权策略和非授权变更。

## 可以证明

- 某个 Defender 策略或排除项在采集时存在。
- 可证明安全控制配置被削弱或为指定路径/进程放行。
- key LastWrite 可辅助定位策略区域最近变化。

## 不能证明

- 不能单独证明 Defender 实际已停止工作；需结合 Defender 状态和事件日志。
- 不能证明策略是攻击者写入还是 GPO/MDM 下发。
- 不能证明排除路径中的文件一定恶意或已执行。
- 在新版本中，某些旧策略值可能被忽略或受 Tamper Protection 限制。

## 时间戳说明

排除项和策略 value 通常没有独立时间戳。key LastWrite 可能由任意 value 变化触发。Defender Operational 事件、GroupPolicy Operational 事件、MDM 诊断日志、Sysmon Event ID 13 和 EDR telemetry 更适合证明写入时间和来源。

## 系统版本差异

Windows 10/11 和 Server 的 Defender 平台、Tamper Protection、EDR in block mode、企业管理方式会影响策略是否生效。`DisableAntiSpyware` 在新版本上不应简单解释为 Defender 已禁用。未知平台版本时写“策略值存在，实际生效需结合 Defender 状态验证”。

## 攻击滥用

攻击者常添加排除路径以放行 payload、工具目录或勒索软件工作目录，也会尝试关闭实时保护、行为监控、脚本扫描或提交样本。常见写入工具包括 PowerShell `Set-MpPreference`、`reg.exe`、GPO 滥用或直接 API 调用。

## 检测思路

- 新增排除路径指向 `%Temp%`、`%AppData%`、`Downloads`、`ProgramData` 非标准目录、整盘根目录或网络共享。
- 排除进程为脚本解释器、压缩工具、备份工具、未知可执行文件或攻击工具。
- `DisableRealtimeMonitoring`、`DisableBehaviorMonitoring` 等从安全基线偏离。
- 监控 `\Policies\Microsoft\Windows Defender\` registry set，关联 `powershell.exe Set-MpPreference`、`reg.exe add`、GPO 变更。
- 排除项新增后短时间内出现恶意文件落地、服务创建或大规模文件修改。

## 常见误报

- 企业 EDR/AV 兼容性排除、数据库、备份、虚拟化、开发编译目录。
- GPO/MDM 正常下发策略或安全团队临时排障。
- 某些 Defender 策略由安全基线模板写入，必须与组织标准比较。

## 采集方式

=== "PowerShell"

    ```powershell
    Get-MpPreference | Select-Object ExclusionPath, ExclusionProcess, ExclusionExtension,
      DisableRealtimeMonitoring, DisableBehaviorMonitoring
    Get-ChildItem "HKLM:\SOFTWARE\Policies\Microsoft\Windows Defender" -Recurse -ErrorAction SilentlyContinue
    ```

=== "reg.exe"

    ```cmd
    reg query "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender" /s
    ```

=== "Offline"

    ```text
    Load SOFTWARE hive and inspect Policies\Microsoft\Windows Defender.
    Collect Microsoft-Windows-Windows Defender/Operational.evtx and GroupPolicy logs.
    ```

## 解析工具

- Registry Explorer、RECmd：适合导出策略和 LastWrite。
- KAPE：采集 SOFTWARE、Defender logs、Group Policy、PowerShell logs。
- Velociraptor：适合跨主机枚举 Defender preferences 和 registry policies。
- Microsoft Defender PowerShell cmdlets：live 状态核对。
- RegRipper：可通过插件或自定义路径提取策略。

## 交叉验证

- Microsoft-Windows-Windows Defender/Operational 事件。
- PowerShell logs：`Set-MpPreference`、`Add-MpPreference`。
- Sysmon Event ID 13、Security 4657、EDR registry telemetry。
- GroupPolicy Operational、MDM diagnostics、Intune / GPO change records。
- 文件落地、服务创建、进程执行、勒索软件文件修改时间线。

## 示例结论

- `Exclusions\Paths` 中新增 `C:\Users\Public\Music`，同目录随后出现未签名 payload 和服务创建事件；该证据可证明 Defender 路径排除项存在，并与 payload 落地时间线高度相关，但策略来源需继续核对。
- `DisableRealtimeMonitoring=1` 存在于策略路径，但 Defender Operational 日志显示 Tamper Protection 阻止变更；报告应写为“存在禁用尝试/策略值”，不能写成“实时保护已关闭”。

## 相关页面

- 场景：[安全策略与防护配置](../../questions/policy-security.md)、[反取证与清理痕迹](../../questions/anti-forensics.md)
- 注册表位置：[HKLM\SOFTWARE](../../registry-tree/hklm/software/index.md)、[HKEY_LOCAL_MACHINE](../../registry-tree/hklm/index.md)

## 参考资料

- [Microsoft Learn: Microsoft Defender Antivirus policy settings](https://learn.microsoft.com/en-us/defender-endpoint/configure-microsoft-defender-antivirus-features)
- [Microsoft Learn: Configure and validate exclusions](https://learn.microsoft.com/en-us/defender-endpoint/configure-extension-file-exclusions-microsoft-defender-antivirus)
- [MITRE ATT&CK: Impair Defenses](https://attack.mitre.org/techniques/T1562/)
