---
tags:
  - Persistence
  - Autoruns
  - HKCU
  - HKLM
---

# StartupApproved

<div class="rfh-meta" markdown>
<span class="rfh-badge medium">取证价值 中</span>
<span class="rfh-badge medium">检测价值 中</span>
<span class="rfh-badge">启动项状态 / 用户选择</span>
</div>

## 摘要

StartupApproved 记录 Windows 对启动项的启用/禁用状态，可解释为什么某个 Run key 或 Startup Folder 项存在但未自动启动。

## 注册表路径

| View | Hive / File | Path | Scope |
|---|---|---|---|
| Live path | `HKCU` | `Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run` | 当前用户 |
| Live path | `HKCU` | `Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\StartupFolder` | 当前用户 |
| Live path | `HKLM` | `Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run` | 机器级 |
| Live path | `HKLM` | `Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run32` | 32 位机器级视图 |
| Live path | `HKLM` | `Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\StartupFolder` | 机器级 Startup Folder |
| Offline hive path | `NTUSER.DAT` | `Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\...` | 用户级 |
| Offline hive path | `SOFTWARE` | `Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\...` | 机器级 |

## 原生注册表视图

在 `regedit.exe` 中从 `HKCU` 或 `HKLM` 的 `Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved` 展开。它通常与 `Run / RunOnce`、Startup Folder 和任务管理器“启动应用”界面相关。

## 离线位置

用户级状态在目标用户 `NTUSER.DAT`；机器级状态在 `C:\Windows\System32\Config\SOFTWARE`。分析时应同时读取对应的启动命令来源，例如 [Run / RunOnce](run-keys.md) 和 Startup Folder 文件系统路径。

## 字段含义

| Field | Meaning |
|---|---|
| 子键 `Run` / `Run32` | 对应注册表 Run 启动项状态 |
| 子键 `StartupFolder` | 对应 Startup Folder 快捷方式状态 |
| value name | 通常与启动项 value name 或快捷方式名称匹配 |
| value data | 二进制状态，工具通常可解析为 enabled / disabled 及状态更新时间；具体字节语义依 OS 版本 |
| key LastWrite | 容器最近变化时间，不等于某个启动项状态的精确切换时间 |

## 取证含义

StartupApproved 本身不保存完整启动命令。它回答的是“这个启动项当前或最近被 Windows 标记为启用还是禁用”。如果 Run key 存在但 StartupApproved 显示 disabled，报告应说明该命令被配置过，但自动启动状态可能被用户、系统或策略禁用。

## 可以证明

- 某个启动项名称在 StartupApproved 中有状态记录。
- 可辅助判断启动项被启用、禁用或由 Windows 管理过。
- 与 Run key / Startup Folder 对齐后，可解释启动项配置和实际生效状态的差异。

## 不能证明

- 不能单独证明启动命令是什么。
- 不能单独证明程序已经在登录时执行。
- 不能把 StartupApproved 记录当作启动项创建证据。
- 不能仅凭 disabled 状态排除历史执行。

## 时间戳说明

value data 中可能包含状态更新时间或保留字段，解析依工具和 Windows 版本。key LastWrite 只说明 StartupApproved 子键整体发生变化。报告中应把“状态更新时间”和“Run key LastWrite”“Startup Folder LNK 时间”分开描述。

## 系统版本差异

StartupApproved 主要见于 Windows 8/10/11 的启动应用管理机制；Windows 7 语义不同或不存在同等路径。`Run32`、`StartupFolder` 等子键在不同版本和安装状态下可能不完整。未知版本应标记为待验证，不要假定所有启动项都有 StartupApproved 记录。

## 攻击滥用

攻击者可创建 Run key 后尝试同步写入 StartupApproved 使其显示为 enabled，也可能删除 disabled 记录来影响任务管理器显示。反过来，管理员或用户禁用恶意启动项后，StartupApproved 可留下状态变化线索。

## 检测思路

- 新增可疑 Run key 后短时间内出现对应 StartupApproved enabled 状态。
- StartupApproved 中出现名称伪装系统组件、但对应 Run key 指向用户可写目录。
- StartupApproved 被批量清理或状态频繁切换，结合 Sysmon Event ID 13 监控 `\Explorer\StartupApproved\`。
- Run key 存在而 StartupApproved 缺失或异常时，标记为需要人工核对，不直接定性。

## 常见误报

- 用户通过任务管理器启用/禁用启动应用。
- 合法安装器、更新器和企业管理工具创建或修改启动项状态。
- Windows 升级、应用卸载和清理工具可能留下孤立 StartupApproved 记录。

## 采集方式

=== "PowerShell"

    ```powershell
    Get-ChildItem "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved" -Recurse -ErrorAction SilentlyContinue
    Get-ChildItem "HKLM:\Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved" -Recurse -ErrorAction SilentlyContinue
    ```

=== "reg.exe"

    ```cmd
    reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved" /s
    reg query "HKLM\Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved" /s
    ```

=== "Offline"

    ```text
    Collect SOFTWARE plus each user's NTUSER.DAT.
    Correlate StartupApproved values with Run keys and Startup Folder LNK files.
    ```

## 解析工具

- Autoruns：适合 live triage，能显示启动项启停状态。
- Registry Explorer：适合人工查看二进制 value、LastWrite。
- RECmd：适合批量导出并和 Run key 合并分析。
- KAPE：可收集 registry hives、Startup Folder、LNK。
- Velociraptor：适合跨主机查询 StartupApproved 与 Run key 差异。

## 交叉验证

- [Run / RunOnce](run-keys.md)
- Startup Folder LNK、Scheduled Tasks、Services。
- Sysmon Event ID 12/13/14、Security 4688、EDR registry telemetry。
- Prefetch、BAM/DAM、UserAssist 证明是否实际执行。

## 示例结论

- `HKCU\...\Run` 中存在 `OneDrive Update` 指向 `C:\Users\alice\AppData\Roaming\onedrive.exe`，StartupApproved `Run\OneDrive Update` 解析为 enabled；该组合可证明用户级启动项配置存在且未被 StartupApproved 禁用，但仍不能单独证明登录时已执行。
- `HKLM\...\Run` 残留 `Updater`，StartupApproved 显示 disabled，且对应文件已删除；报告应写为“历史启动项配置与禁用状态残留”，而不是“当前仍会启动”。

## 相关页面

- 场景：[自启动与持久化](../../questions/persistence.md)
- 注册表位置：[HKCU Explorer](../../registry-tree/hkcu/explorer.md)、[HKLM\SOFTWARE](../../registry-tree/hklm/software.md)

## 参考资料

- [Microsoft Sysinternals: Autoruns](https://learn.microsoft.com/en-us/sysinternals/downloads/autoruns)
- [Eric Zimmerman tools](https://ericzimmerman.github.io/)
