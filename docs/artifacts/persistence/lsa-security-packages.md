---
tags:
  - Persistence
  - CredentialAccess
  - LSA
  - SYSTEM
  - HKLM
---

# LSA Security Packages

<div class="rfh-meta" markdown>
<span class="rfh-badge high">取证价值 高</span>
<span class="rfh-badge high">检测价值 高</span>
<span class="rfh-badge">SSP 加载链</span>
</div>

## 摘要

`LSA\Security Packages` 指定可由 Local Security Authority 使用的安全支持包，异常条目可能导致 LSASS 加载第三方 SSP/AP 组件。

## 注册表路径

| 视图 | Hive / 文件 | 路径 | Value | 范围 |
|---|---|---|---|---|
| Live path | `HKLM\SYSTEM` | `CurrentControlSet\Control\Lsa` | `Security Packages` | 机器级 |
| Live path | `HKLM\SYSTEM` | `CurrentControlSet\Control\Lsa\OSConfig` | `Security Packages` | 系统受限配置 |
| Offline hive path | `SYSTEM` | `ControlSet00x\Control\Lsa` | `Security Packages` | 机器级，需解析 `Select` |

## 原生注册表视图

在 `regedit.exe` 中展开 `HKLM\SYSTEM\CurrentControlSet\Control\Lsa`。该页面聚焦 `Security Packages`，与 `Authentication Packages` 相关但语义不同，调查时应同时查看两者和 `RunAsPPL`。

## 离线位置

离线文件为 `C:\Windows\System32\Config\SYSTEM`。先解析 `Select\Current` 到当前 ControlSet，再检查 `ControlSet00x\Control\Lsa`。

## 字段含义

| 字段 | 含义 |
|---|---|
| `Security Packages` | `REG_MULTI_SZ`，列出 LSA 可加载的 SSP/AP 包名。 |
| `OSConfig\Security Packages` | 系统预配置项；Windows 8.1 以后对移除/替换 inbox 包有更多限制。 |
| `RunAsPPL` | LSA protection 状态，影响 LSASS 防护但不等同无风险。 |
| key LastWrite | Lsa key 最近变化，不等同 SSP 实际加载时间。 |

## 取证含义

该配置证明系统允许特定安全包参与 LSA 安全服务。非基线包名可能对应第三方认证、VPN、安全产品，也可能被攻击者用于 LSASS 上下文持久化或凭据访问。

## 可以证明

- 当前 ControlSet 中配置了哪些 LSA Security Packages。
- 是否存在非基线、异常新增或被移除的包名。
- 配置具备 LSASS 加载链风险，需要进一步验证 DLL。

## 不能证明

- 不能单独证明 SSP DLL 已加载。
- 不能单独证明凭据被窃取。
- 不能把 `Security Packages` 与 `Authentication Packages` 混为同一字段。

## 时间戳说明

`Control\Lsa` key LastWrite 只能说明 LSA 配置 key 发生过变化。实际加载应结合系统启动、LSASS 模块加载、Code Integrity、EDR 和内存证据。

## 系统版本差异

Windows 8.1 以后 Microsoft 对 inbox security packages 的移除/替换有限制，并指定 `Control\Lsa\Security Packages` 用于第三方包。不同 Server、域控、安全产品基线可能差异很大。

## 攻击滥用

攻击者可添加自定义 SSP/AP 包名，配合 DLL 放置和重启/登录让 LSASS 加载组件。该方式通常需要管理员权限，并与凭据访问风险直接相关。

## 检测思路

- `Security Packages` 出现非组织基线包名。
- `Security Packages` 被非安装器、非安全产品进程修改。
- 包名对应 DLL 位于异常目录、无签名或最近创建。
- 关联 LSASS 模块加载、Credential Guard / RunAsPPL 状态和系统重启时间线。

## 常见误报

- VPN、MFA、智能卡、中间件、EDR、DLP、身份管理和旧版认证组件。
- 域控制器和成员服务器的默认基线可能不同。
- 安全产品升级可能短时间改变 LSA 包列表。

## 采集方式

=== "PowerShell"

    ```powershell
    Get-ItemProperty "HKLM:\SYSTEM\CurrentControlSet\Control\Lsa" |
      Select-Object "Security Packages","Authentication Packages","RunAsPPL"
    ```

=== "reg.exe"

    ```cmd
    reg query "HKLM\SYSTEM\CurrentControlSet\Control\Lsa" /v "Security Packages"
    reg query "HKLM\SYSTEM\CurrentControlSet\Control\Lsa\OSConfig" /v "Security Packages"
    ```

=== "Offline"

    ```text
    Collect SYSTEM hive and resolve Select\Current before inspecting ControlSet00x\Control\Lsa.
    ```

## 解析工具

- Autoruns / Autorunsc
- Registry Explorer
- RECmd
- KAPE
- Velociraptor

## 交叉验证

- [LSA Authentication Packages](lsa-authentication-packages.md)
- Sysmon Event ID 7、13。
- Security 4657、System reboot events。
- LSASS 模块列表、内存取证、EDR telemetry。
- DLL 文件签名、哈希和文件系统时间线。

## 示例结论

- `Security Packages` 中新增 `sspmod`，且对应 DLL 无签名并在入侵窗口创建；该证据可证明 LSA Security Package 加载链被配置为包含非基线包。
- 当前只有注册表配置，无 LSASS 模块加载或重启证据，因此不能单独证明该 SSP 已生效。

## 参考资料

- [Microsoft Learn: Restrictions on registering and installing a security package](https://learn.microsoft.com/en-us/windows/win32/secauthn/restrictions-around-registering-and-installing-a-security-package)
- [MITRE ATT&CK: Security Support Provider](https://attack.mitre.org/techniques/T1547/005/)
- [Microsoft Sysinternals: Autoruns](https://learn.microsoft.com/en-us/sysinternals/downloads/autoruns)

## 相关页面

- 场景：[自启动与持久化](../../questions/persistence.md)、[安全策略与防护配置](../../questions/policy-security.md)
- 注册表位置：[HKLM\SYSTEM\ControlSet00x\Control\Lsa\Security Packages](../../registry-tree/hklm/system/controlset/control/lsa/security-packages.md)

