---
tags:
  - Accounts
  - SecurityPolicy
  - SOFTWARE
  - HKLM
---

# SpecialAccounts\UserList

<div class="rfh-meta" markdown>
<span class="rfh-badge high">取证价值 高</span>
<span class="rfh-badge medium">检测价值 中</span>
<span class="rfh-badge">登录界面隐藏账户</span>
</div>

## 摘要

`SpecialAccounts\UserList` 可控制账户是否显示在登录界面，常用于隐藏本地账户线索，但不能单独证明账户被新建或用于登录。

## 注册表路径

| View | Hive / File | Path | Scope |
|---|---|---|---|
| Live path | `HKLM\SOFTWARE` | `Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\UserList` | 机器级 |
| Offline hive path | `SOFTWARE` | `Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\UserList` | 机器级 |

## 原生注册表视图

在 `regedit.exe` 中展开 `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\UserList`。value name 通常是用户名，DWORD value 控制是否在登录 UI 中显示。

## 离线位置

`C:\Windows\System32\Config\SOFTWARE`。需要与 `SAM`、Security.evtx、本地组成员和 [ProfileList](profilelist.md) 交叉验证。

## 字段含义

| Field | Meaning |
|---|---|
| value name | 用户名 |
| `0` | 通常表示隐藏该账户，不在欢迎/登录界面显示 |
| `1` | 通常表示显示该账户 |
| key LastWrite | UserList key 最近变化时间，不等于账户创建或登录时间 |

## 取证含义

该键可提示有人试图隐藏账户可见性。它常与异常本地账户、新管理员成员、RDP 登录、服务账户滥用、持久化账户一起调查。它不保存账户 SID、密码、组成员或登录事实。

## 可以证明

- 某用户名在登录界面显示控制列表中存在。
- DWORD 值可提示该用户名是否被隐藏或显示。
- key LastWrite 可辅助定位 UserList 配置变化窗口。

## 不能证明

- 账户存在于 SAM 或域中。
- 账户是攻击者创建的。
- 账户登录过。
- 账户具有管理员权限。

## 时间戳说明

`UserList` key LastWrite 是 key 级时间。具体 value 无独立时间戳。账户创建/修改要用 SAM、Security.evtx `4720`/`4738`，组成员变化用 `4732`/`4733`。

## 系统版本差异

该机制常见于 Windows 桌面和 Server，但登录 UI、域加入状态、自动登录、kiosk、VDI 和策略会影响可见性。未知版本应将结论限定为“配置存在”。

## 攻击滥用

攻击者可新建本地账户后写入 `UserList\<username>=0`，减少登录界面可见性。也可隐藏已有管理员或备用账户，以维持交互式或远程访问路径。

## 检测思路

- `UserList` 中出现非基线用户名且 value 为 `0`。
- 新账户 `4720` 后短时间内写入 UserList。
- UserList 隐藏账户随后加入 Administrators 或 Remote Desktop Users。
- 隐藏账户出现 RDP LogonType `10` 或服务创建行为。

## 常见误报

- Kiosk、共享设备、VDI、OEM/运维账户、合法隐藏服务账户、企业登录体验定制。

## 采集方式

=== "PowerShell"

    ```powershell
    Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\UserList" -ErrorAction SilentlyContinue
    ```

=== "reg.exe"

    ```cmd
    reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\UserList"
    ```

=== "Offline"

    ```text
    Load SOFTWARE hive and inspect Winlogon\SpecialAccounts\UserList.
    Collect SAM and Security.evtx for account validation.
    ```

## 解析工具

- Registry Explorer
- RECmd
- KAPE
- Velociraptor
- RegRipper

## 交叉验证

- SAM local users
- Security.evtx `4720`, `4722`, `4732`, `4738`
- ProfileList
- RDP logs
- Local group membership
- EDR account telemetry

## 示例结论

- `SpecialAccounts\UserList` contains `backupsvc=0`; this proves the username is configured to be hidden from the logon UI, but does not prove the account exists or has logged on.
- A local account was created, added to Administrators, and then added to UserList with value `0` within four minutes; this supports a hidden-account persistence finding when validated with SAM and Security.evtx.

## 参考资料

- [Microsoft Learn: Winlogon and credential providers](https://learn.microsoft.com/en-us/windows/win32/secauthn/winlogon-and-credential-providers)
- [MITRE ATT&CK: Create Account](https://attack.mitre.org/techniques/T1136/)

## 相关页面

- 场景：[账户与安全](../../questions/accounts-security.md), [安全策略与防护配置](../../questions/policy-security.md)
- 注册表位置：[HKLM\SOFTWARE](../../registry-tree/hklm/software/index.md)
