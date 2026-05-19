---
tags:
  - Accounts
  - UserProfiles
  - SOFTWARE
  - HKLM
---

# ProfileList

<div class="rfh-meta" markdown>
<span class="rfh-badge high">取证价值 高</span>
<span class="rfh-badge medium">检测价值 中</span>
<span class="rfh-badge">SID 映射 / 用户归属</span>
</div>

## 摘要

ProfileList 是把 SID 映射到本地用户 profile 目录的基础 artifact，几乎所有用户级注册表结论都需要它来确认归属。

## 注册表路径

| View | Hive / File | Path | Scope |
|---|---|---|---|
| Live path | `HKLM\SOFTWARE` | `Microsoft\Windows NT\CurrentVersion\ProfileList\<SID>` | 机器级 |
| Offline hive path | `SOFTWARE` | `Microsoft\Windows NT\CurrentVersion\ProfileList\<SID>` | 机器级 |

## 原生注册表视图

在 `regedit.exe` 中展开 `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList`。每个 SID 子键通常对应一个本地、域或服务账户 profile。

## 离线位置

离线文件为 `C:\Windows\System32\Config\SOFTWARE`。用户 hive 文件位于 `ProfileImagePath` 指向的目录下，例如 `C:\Users\alice\NTUSER.DAT` 和 `C:\Users\alice\AppData\Local\Microsoft\Windows\UsrClass.dat`。

## 字段含义

| Field | Meaning |
|---|---|
| SID 子键 | 用户或系统账户 SID |
| `ProfileImagePath` | profile 目录路径，常含 `%SystemDrive%` |
| `Flags` / `State` | profile 状态字段，需按版本和工具解释 |
| `ProfileLoadTimeHigh` / `ProfileLoadTimeLow` | 部分版本存在的 profile 加载时间字段，解析需工具支持 |
| `.bak` 子键 | profile 重建、临时 profile 或登录异常线索 |

## 取证含义

ProfileList 不直接证明用户行为，但它是解释用户级 artifact 的前置证据。报告中写 `HKCU`、`NTUSER.DAT`、`UsrClass.dat`、UserAssist、MountPoints2 或 RDP Client 时，都应能追溯到 ProfileList 的 SID 与目录映射。

## 可以证明

- 某个 SID 在系统上有或曾有 profile 映射。
- 对应用户目录路径是什么。
- 可辅助识别临时 profile、异常 profile 路径、删除用户残留。

## 不能证明

- 不能单独证明账户当前存在于 SAM 或域中。
- 不能单独证明用户近期登录。
- 不能单独证明用户执行过程序或访问过文件。
- 不能把目录名直接等同于账户名或显示名。

## 时间戳说明

SID 子键 LastWrite 可提示 profile 记录变化，但不等于用户首次登录或最后登录时间。`ProfileLoadTimeHigh/Low` 若存在，应由工具解析并明确字段来源。用户登录时间应结合 Security.evtx、User Profile Service 日志和 hive 文件时间线。

## 系统版本差异

Windows 7/10/11/Server 都使用 ProfileList，但 `State`、`Flags`、`.bak` 和加载时间字段表现可能不同。域账户、Azure AD、临时 profile、漫游 profile、FSLogix/VDI 场景需要额外验证。未知字段不要强行解释。

## 攻击滥用

攻击者可能创建本地账户、隐藏账户、修改 profile 路径或利用已删除用户残留隐藏工具。ProfileList 可帮助发现 profile 指向非标准目录、SID 与 SAM/日志不一致、或登录后立即出现用户级持久化。

## 检测思路

- 新增 ProfileList SID 后短时间内出现 Run key、RDP Client、Command Processor AutoRun 或可疑文件落地。
- `ProfileImagePath` 指向非标准位置、可移动卷、临时目录或拼写伪装目录。
- `.bak` profile、临时 profile 频繁出现，结合登录失败和用户 profile service 事件调查。
- ProfileList SID 与 SAM、本地域用户、域登录事件不一致。

## 常见误报

- 域用户首次登录、VDI/FSLogix、漫游 profile、系统升级或 profile 修复。
- 删除用户后 registry 与目录可能长期残留。
- 安装服务账户、应用池账户和系统账户会产生非普通用户 SID。

## 采集方式

=== "PowerShell"

    ```powershell
    Get-ChildItem "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList" |
      ForEach-Object {
        $p = Get-ItemProperty $_.PsPath
        [PSCustomObject]@{ SID = $_.PSChildName; ProfileImagePath = $p.ProfileImagePath; State = $p.State; Flags = $p.Flags }
      }
    ```

=== "reg.exe"

    ```cmd
    reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList" /s
    ```

=== "Offline"

    ```text
    Load SOFTWARE hive, export ProfileList, then map each SID to NTUSER.DAT and UsrClass.dat.
    ```

## 解析工具

- Registry Explorer：适合查看 SID 子键和 LastWrite。
- RECmd：适合批量导出 ProfileList。
- KAPE：可采集 SOFTWARE 和所有用户 hive。
- Velociraptor：适合跨主机枚举 profile 映射和异常路径。
- RegRipper：可通过插件输出 profilelist 信息。

## 交叉验证

- SAM 本地账户、域控制器登录记录、Security.evtx `4624`、`4634`、`4672`。
- User Profile Service operational log。
- `C:\Users\<user>` 目录、`NTUSER.DAT`、`UsrClass.dat` 文件时间线。
- UserAssist、MountPoints2、RDP Client、Run key 等用户级 artifact。

## 示例结论

- `ProfileList\S-1-5-21-...\1001` 的 `ProfileImagePath` 为 `C:\Users\alice`，该 SID 下 `NTUSER.DAT` 中存在 RDP Client 记录；报告可将该 RDP 客户端痕迹归属到 alice profile，而不是泛称 HKCU。
- ProfileList 新增 SID 指向 `C:\Users\Public\Documents\svc`，同时间段 SAM 出现新本地管理员；该组合支持“异常本地账户及非标准 profile 路径”调查方向。

## 相关页面

- 场景：[账户与安全](../../questions/accounts-security.md)
- 注册表位置：[HKLM\SOFTWARE](../../registry-tree/hklm/software.md)、[HKU SID 映射](../../registry-tree/hku/sid-mapping.md)

## 参考资料

- [artefacts.help: ProfileList](https://artefacts.help/windows_registry_profilelist.html)
- [Microsoft Learn: User profiles](https://learn.microsoft.com/en-us/windows/client-management/client-tools/mandatory-user-profile)
