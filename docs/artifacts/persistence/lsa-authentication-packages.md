---
tags:
  - Persistence
  - CredentialAccess
  - LSA
  - SYSTEM
  - HKLM
---

# LSA Authentication Packages

<div class="rfh-meta" markdown>
<span class="rfh-badge high">取证价值 高</span>
<span class="rfh-badge high">检测价值 高</span>
<span class="rfh-badge">LSASS 加载链</span>
</div>

## 摘要

`LSA\Authentication Packages` 控制 LSASS 可加载的认证包，新增非基线包可能导致高权限持久化或凭据访问。

## 注册表路径

| View | Hive / File | Path | Value | Scope |
|---|---|---|---|---|
| Live path | `HKLM\SYSTEM` | `CurrentControlSet\Control\Lsa` | `Authentication Packages` | 机器级 |
| Offline hive path | `SYSTEM` | `ControlSet00x\Control\Lsa` | `Authentication Packages` | 机器级，需解析 `Select` |
| Related | `HKLM\SYSTEM` | `CurrentControlSet\Control\Lsa` | `Security Packages` / `Notification Packages` | 相关 LSA 加载点 |

## 原生注册表视图

在 `regedit.exe` 中展开 `HKLM\SYSTEM\CurrentControlSet\Control\Lsa`。默认 `Authentication Packages` 常见为 `msv1_0`。调查时同时查看 `Security Packages`、`Notification Packages`、`RunAsPPL` 等相关 value。

## 离线位置

离线文件为 `C:\Windows\System32\Config\SYSTEM`。需要先解析 `HKLM\SYSTEM\Select` 到当前 `ControlSet00x`。如果比较历史 ControlSet，分别标注控制集来源。

## 字段含义

| Field | Meaning |
|---|---|
| `Authentication Packages` | REG_MULTI_SZ，列出 LSA 认证包名称 |
| `msv1_0` | 常见默认包，处理 NTLM/MSV 认证场景 |
| 新增条目 | 可能表示额外认证包 DLL 将由 LSASS 加载，通常位于系统搜索路径 |
| key LastWrite | Lsa key 最近变化时间，不能直接等于某个包首次加载时间 |

## 取证含义

该配置可证明系统被配置为允许 LSASS 加载指定认证包。恶意认证包一旦被加载，可能获得 LSASS 进程上下文能力并接触认证材料。新增条目是高风险配置证据，但是否已经加载通常需要重启/登录事件、模块加载、内存或 EDR 证据确认。

## 可以证明

- 当前或某个 ControlSet 中配置了哪些 LSA Authentication Packages。
- 是否存在非基线包名或异常新增项。
- 配置具备高权限持久化和凭据访问潜力。

## 不能证明

- 不能单独证明 DLL 已被 LSASS 加载。
- 不能单独证明凭据被窃取。
- 不能只凭包名判断 DLL 文件路径和签名，需解析搜索路径并检查文件。

## 时间戳说明

`Control\Lsa` key LastWrite 可能由多个 LSA value 修改触发。LSA 包实际加载时间应通过 LSASS 模块加载、系统启动、事件日志或内存证据确认。离线读取非当前 ControlSet 时，LastWrite 只能说明该控制集内配置变化。

## 系统版本差异

Windows 7/10/11/Server 都存在 LSA 相关配置，但默认值、Credential Guard、LSA protection (`RunAsPPL`) 和安全产品集成会影响风险判断。默认 authentication package 基线需按 OS、域环境和安全软件建立；未知条目不要直接删除，应先确认厂商和签名。

## 攻击滥用

攻击者可注册自定义认证包，借由 LSASS 加载实现持久化或凭据访问。该路径通常需要管理员权限，可能配合 DLL 放置、服务重启、系统重启或触发登录流程。

## 检测思路

- `Authentication Packages` 不等于组织基线，尤其出现非 Microsoft 包名。
- LSA 相关 value 被 `reg.exe`、PowerShell、安装器以外进程修改。
- 新增包名对应 DLL 位于用户可写目录、无签名或最近创建。
- 监控 registry set：`\SYSTEM\CurrentControlSet\Control\Lsa\Authentication Packages`。
- 关联 LSASS 模块加载事件、Code Integrity、EDR module telemetry。

## 常见误报

- MFA、智能卡、VPN、EDR、DLP、身份管理产品可能合法增加 LSA 组件。
- 域控制器、安全基线和旧版认证组件的默认值可能不同。
- 安装或升级安全产品时出现短时间变更。

## 采集方式

=== "PowerShell"

    ```powershell
    Get-ItemProperty "HKLM:\SYSTEM\CurrentControlSet\Control\Lsa" |
      Select-Object "Authentication Packages","Security Packages","Notification Packages","RunAsPPL"
    ```

=== "reg.exe"

    ```cmd
    reg query "HKLM\SYSTEM\CurrentControlSet\Control\Lsa" /v "Authentication Packages"
    reg query "HKLM\SYSTEM\CurrentControlSet\Control\Lsa" /v "Security Packages"
    ```

=== "Offline"

    ```text
    Load SYSTEM hive, resolve Select\Current, inspect ControlSet00x\Control\Lsa.
    Export package names and compare with known-good baseline.
    ```

## 解析工具

- Registry Explorer：适合核对 REG_MULTI_SZ 和 LastWrite。
- RECmd：适合批量抽取 LSA value。
- Autoruns：可辅助查看 LSA providers。
- KAPE：采集 SYSTEM、event logs、Autoruns 输出。
- Velociraptor：适合多主机基线比较。

## 交叉验证

- LSASS 模块加载、EDR module telemetry、Sysmon Event ID 7。
- Sysmon Event ID 13、Security 4657 证明 value set。
- 文件系统：DLL 路径、签名、哈希、创建/修改时间。
- Security 登录事件、系统重启事件、服务控制事件。
- Credential Guard、RunAsPPL 状态和安全产品基线。

## 示例结论

- `Authentication Packages` 包含默认 `msv1_0` 之外的 `authsvc`，且 `C:\Windows\System32\authsvc.dll` 无签名、创建时间与入侵时间线接近；该证据可证明 LSA 加载链被配置为包含非基线包，是否已加载需用 LSASS 模块证据确认。
- `Control\Lsa` LastWrite 与 Sysmon Event ID 13 对齐，修改进程为 `powershell.exe`，随后系统重启；该组合显著提升 LSA 持久化生效的可能性。

## 相关页面

- 场景：[自启动与持久化](../../questions/persistence.md)、[账户与安全](../../questions/accounts-security.md)
- 注册表位置：[HKLM\SYSTEM](../../registry-tree/hklm/system.md)、[HKLM\SECURITY](../../registry-tree/hklm/security.md)

## 参考资料

- [Microsoft Learn: LSA Authentication](https://learn.microsoft.com/en-us/windows/win32/secauthn/lsa-authentication)
- [Microsoft Learn: MSV1_0 Authentication Package](https://learn.microsoft.com/en-us/windows/win32/secauthn/msv1-0-authentication-package)
- [MITRE ATT&CK: Authentication Package](https://attack.mitre.org/techniques/T1547/002/)
