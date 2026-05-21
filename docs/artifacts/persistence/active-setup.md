---
tags:
  - Persistence
  - Autoruns
  - ActiveSetup
  - SOFTWARE
  - HKLM
  - HKCU
---

# Active Setup

<div class="rfh-meta" markdown>
<span class="rfh-badge high">取证价值 高</span>
<span class="rfh-badge high">检测价值 高</span>
<span class="rfh-badge">用户登录初始化</span>
</div>

## 摘要

`Active Setup` 是 Windows 在用户登录时执行每用户初始化命令的机制，异常 `StubPath` 可用于跨用户登录触发持久化。

## 注册表路径

| 视图 | Hive / 文件 | 路径 | Value | 范围 |
|---|---|---|---|---|
| Live path | `HKLM\SOFTWARE` | `Microsoft\Active Setup\Installed Components\<Component>` | `StubPath` | 机器级组件定义 |
| Live path | `HKCU` | `Software\Microsoft\Active Setup\Installed Components\<Component>` | `Version` / `Locale` | 用户级完成状态 |
| Offline hive path | `SOFTWARE` | `Microsoft\Active Setup\Installed Components\<Component>` | `StubPath` | 机器级 |
| Offline hive path | `NTUSER.DAT` | `Software\Microsoft\Active Setup\Installed Components\<Component>` | `Version` / `Locale` | 单用户 |

## 原生注册表视图

在 `regedit.exe` 中分别查看 `HKLM\SOFTWARE\Microsoft\Active Setup\Installed Components` 和当前用户的 `HKCU\Software\Microsoft\Active Setup\Installed Components`。离线分析时需要把 `HKCU` 映射回对应用户的 `NTUSER.DAT`。

## 离线位置

机器级组件定义在 `C:\Windows\System32\Config\SOFTWARE`。用户级完成状态在 `C:\Users\<user>\NTUSER.DAT`。多用户调查时应逐个用户 hive 对比 HKLM 组件和 HKCU 镜像。

## 字段含义

| 字段 | 含义 |
|---|---|
| `<Component>` | 组件 GUID 或名称。攻击者可能使用伪装成 Microsoft 组件的名称。 |
| `StubPath` | 用户登录时可能被执行的命令。 |
| `Version` | HKLM 与 HKCU 版本比较相关；HKCU 缺失或版本落后时可能触发执行。 |
| `Locale` | 区域设置比较相关，具体行为需结合版本验证。 |
| `IsInstalled` | 常见为 `REG_DWORD`，用于表示组件安装状态；语义需结合组件实现。 |
| key LastWrite | key 最近更新，不等同 `StubPath` 首次执行时间。 |

## 取证含义

HKLM 下的 Active Setup 项证明系统配置了一个可在用户登录初始化阶段运行的组件。HKCU 下对应项通常表示某用户已完成或记录过该组件初始化。异常 `StubPath` 指向用户可写目录、脚本解释器或网络路径时，是持久化调查的高信号线索。

## 可以证明

- 机器级或用户级 Active Setup 组件配置存在。
- 指定用户是否存在对应 HKCU 镜像项，可辅助判断该用户是否已被初始化过。
- `StubPath` 可证明登录初始化链中配置了待执行命令。

## 不能证明

- 不能单独证明命令已经执行成功。
- 不能单独证明所有用户都会触发；需要比较 HKCU 镜像、版本和登录时间。
- 不能只凭组件名判断恶意，需检查命令、文件签名和上下文。

## 时间戳说明

HKLM 组件 key LastWrite 支持判断配置最近变更。HKCU 镜像 key LastWrite 可作为某用户初始化状态变化线索，但不能直接等同用户登录时间或命令执行时间。执行时间应结合登录事件、进程创建和 Prefetch / Amcache / BAM。

## 系统版本差异

Active Setup 在 Windows 7 / 10 / 11 / Server 中均常见。不同应用、浏览器和企业组件写入的字段可能不同；`Version` 比较细节和 WOW6432Node 行为在具体版本中需验证。

## 攻击滥用

攻击者可在 HKLM Active Setup 下创建组件并写入 `StubPath`，使后续用户登录时以该用户权限执行 payload；也可利用版本递增让已初始化用户再次触发。

## 检测思路

- 监控 `HKLM\SOFTWARE\Microsoft\Active Setup\Installed Components\*\StubPath` 新增或修改。
- 关注 `StubPath` 指向 `%AppData%`、`%Temp%`、`Downloads`、UNC、脚本解释器或 LOLBin。
- 对比新组件创建时间、用户登录事件和随后的进程创建。
- 在 64 位系统上同时检查 `HKLM\SOFTWARE\WOW6432Node\Microsoft\Active Setup\Installed Components`。

## 常见误报

- 浏览器、Office、企业软件、VDI 配置、输入法、协作软件和安装器可能合法使用 Active Setup。
- 软件升级可能递增 `Version` 并重新触发用户初始化。
- 企业镜像或 GPO 脚本可能批量写入组件。

## 采集方式

=== "PowerShell"

    ```powershell
    Get-ChildItem "HKLM:\SOFTWARE\Microsoft\Active Setup\Installed Components" |
      Get-ItemProperty | Select-Object PSChildName, StubPath, Version, Locale, IsInstalled
    ```

=== "reg.exe"

    ```cmd
    reg query "HKLM\SOFTWARE\Microsoft\Active Setup\Installed Components" /s
    reg query "HKCU\Software\Microsoft\Active Setup\Installed Components" /s
    ```

=== "Offline"

    ```text
    Collect SOFTWARE and each user's NTUSER.DAT. Compare HKLM component definitions with per-user HKCU mirrors.
    ```

## 解析工具

- Autoruns / Autorunsc
- Registry Explorer
- RECmd
- KAPE
- Velociraptor

## 交叉验证

- Security.evtx 登录事件、User Profile Service 事件。
- Sysmon Event ID 1、12、13。
- Prefetch、Amcache、BAM / DAM、ShimCache。
- 文件系统时间线、签名、哈希和安装日志。

## 示例结论

- `HKLM\SOFTWARE\Microsoft\Active Setup\Installed Components\{A1B2...}` 的 `StubPath` 指向 `%AppData%\updater.exe`，可证明系统配置了用户登录初始化命令；是否已执行需结合目标用户 HKCU 镜像和进程日志确认。
- 多个用户 `NTUSER.DAT` 中缺失该组件镜像，说明这些用户后续登录仍可能触发 HKLM `StubPath`。

## 参考资料

- [MITRE ATT&CK: Active Setup](https://attack.mitre.org/techniques/T1547/014/)
- [Microsoft Sysinternals: Autoruns](https://learn.microsoft.com/en-us/sysinternals/downloads/autoruns)

## 相关页面

- 场景：[自启动与持久化](../../questions/persistence.md)
- 注册表位置：[HKLM\SOFTWARE\Microsoft\Active Setup](../../registry-tree/hklm/software/microsoft/active-setup.md)

