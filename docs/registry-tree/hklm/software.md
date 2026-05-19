# HKLM\SOFTWARE

`HKLM\SOFTWARE` 是机器级软件、策略、登录流程、应用兼容性、Defender、ProfileList、Classes 和 32 位重定向视图的核心 hive。它经常回答“这台机器装了什么、策略怎样配置、哪些机器级持久化存在”。

## Native Registry View

Live 系统中路径为：

```text
HKLM\SOFTWARE
```

64 位 Windows 上需要区分 64 位视图和 32 位视图：

```text
HKLM\SOFTWARE
HKLM\SOFTWARE\WOW6432Node
```

同一软件、Run key、Uninstall 记录或 COM 注册可能只存在于其中一个视图。分析工具和采集进程的位数会影响看到的 registry view。

## Offline Hive Source

| Hive | Offline file | Notes |
|---|---|---|
| `SOFTWARE` | `C:\Windows\System32\Config\SOFTWARE` | 机器级软件、策略、ProfileList、Winlogon、IFEO、Defender、Classes。 |
| transaction logs | `SOFTWARE.LOG1`, `SOFTWARE.LOG2` | 可能包含尚未合并的 registry transaction。 |

离线分析 `SOFTWARE` 时不要把机器级配置归属到某个用户。用户级配置应回到目标用户 `NTUSER.DAT` 或 `UsrClass.dat`。

## Forensic Role

`HKLM\SOFTWARE` 在 DFIR 中通常用于：

- 软件安装与卸载：`CurrentVersion\Uninstall`、安装路径、Publisher、版本、卸载命令。
- 持久化：Run / RunOnce、StartupApproved、IFEO、Winlogon、Active Setup、AppInit_DLLs。
- 用户映射：ProfileList 把 SID 映射到 profile，是所有用户级 hive 归属的基础。
- 安全策略：Defender、Policies、UAC、防火墙和企业策略。
- 兼容性和执行辅助：AppCompatFlags、Image File Execution Options。
- 32 位应用视图：WOW6432Node 中可能存在被 64 位视图漏掉的软件和启动项。
- Classes：机器级 COM、文件关联、协议处理器，参与 `HKCR` 合并视图。

## Detection Role

检测工程应重点监控：

- `Run` / `RunOnce` value set，尤其 value data 指向用户可写目录、脚本解释器或 LOLBin。
- `Image File Execution Options\<exe>\Debugger` 被写入。
- `Winlogon\Userinit`、`Winlogon\Shell` 非默认或追加命令。
- Defender policy / exclusions 被新增或削弱。
- `Policies` 中 UAC、Firewall、Audit、PowerShell、Windows Script Host 等策略变化。
- `WOW6432Node` 下同名路径，避免只监控 64 位视图。

## Timestamp Caveats

- `Uninstall` 子键 LastWrite 可能反映安装、升级、卸载或修复，不等于软件首次执行。
- Run key LastWrite 是 key 级更新时间，不能精确到某个 value 创建。
- `Winlogon` key LastWrite 可能由 `Shell`、`Userinit`、`AutoAdminLogon` 或其他 value 触发。
- `Policies` 的 key LastWrite 证明本地 registry 状态变化，不证明 GPO/MDM 来源或实际生效。
- 32 位和 64 位 registry view 的 LastWrite 需要分别解释。

## Common Misinterpretations

| Misinterpretation | Safer interpretation |
|---|---|
| Uninstall 记录存在说明软件当前仍安装 | 它证明安装登记存在；卸载残留、升级残留和手工删除都可能存在。 |
| Run key 存在说明程序已执行 | Run key 证明登录启动配置；执行要结合登录、StartupApproved、Prefetch、BAM、进程日志。 |
| Defender policy 禁用值存在说明 Defender 已关闭 | 需结合 Defender platform、Tamper Protection、Operational 日志和 `Get-MpPreference`。 |
| 只查 `HKLM\SOFTWARE` 就覆盖所有机器级软件 | 32 位软件可能只在 `WOW6432Node`。 |
| HKLM Classes 中 COM 注册就是有效解析结果 | `HKCU\Software\Classes` 可能覆盖或参与合并，需要结合 `HKCR` 语义。 |

## High-Value Subkeys

| Subkey | What to look for | Linked artifacts / scenarios |
|---|---|---|
| `Microsoft\Windows\CurrentVersion\Run` | 机器级登录启动项。 | [Run / RunOnce](../../artifacts/persistence/run-keys.md) |
| `Microsoft\Windows\CurrentVersion\RunOnce` | 一次性登录启动项，常见于安装器也常被滥用。 | [Run / RunOnce](../../artifacts/persistence/run-keys.md) |
| `Microsoft\Windows\CurrentVersion\Uninstall` | 软件安装、卸载、DisplayName、InstallLocation、Publisher。 | [软件安装与卸载](../../questions/software-install.md) |
| `Microsoft\Windows NT\CurrentVersion\Image File Execution Options` | Debugger 劫持、SilentProcessExit、MitigationOptions。 | [IFEO](../../artifacts/persistence/ifeo.md) |
| `Microsoft\Windows NT\CurrentVersion\Winlogon` | `Userinit`、`Shell`、AutoAdminLogon、登录链持久化。 | [Winlogon Userinit](../../artifacts/persistence/winlogon-userinit.md), [Winlogon Shell](../../artifacts/persistence/winlogon-shell.md) |
| `Microsoft\Windows\CurrentVersion\Explorer` | StartupApproved、Shell 相关机器级状态。 | [StartupApproved](../../artifacts/persistence/startupapproved.md) |
| `Microsoft\Windows Defender` | Defender 本地状态线索，具体生效需结合策略和日志。 | [Defender Policies](../../artifacts/security/defender-policies.md) |
| `Policies` | GPO/MDM/本地策略落点，含 Defender、UAC、防火墙等。 | [安全策略与防护配置](../../questions/policy-security.md) |
| `Policies\Microsoft\Windows Defender` | Defender 排除项和保护策略。 | [Defender Policies](../../artifacts/security/defender-policies.md) |
| `Microsoft\Windows\CurrentVersion\Policies\System` | UAC、提示行为、远程本地账户 token 过滤。 | [UAC Policies](../../artifacts/security/uac-policies.md) |
| `Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\UserList` | 登录界面隐藏账户配置。 | [SpecialAccounts\UserList](../../artifacts/security/specialaccounts-userlist.md) |
| `Microsoft\Windows\CurrentVersion\Policies\System\CredSSP\Parameters` | CredSSP / encryption oracle remediation policy。 | [CredSSP / NLA](../../artifacts/rdp/credssp-nla.md) |
| `WOW6432Node` | 32 位软件、Run、Uninstall、Classes 视图。 | 软件安装 / 持久化调查 |
| `Classes` | 机器级文件关联、COM、协议处理器，参与 `HKCR` 合并视图。 | [HKEY_CLASSES_ROOT](../hkey-classes-root.md) |
| `Microsoft\Windows NT\CurrentVersion\ProfileList` | SID 到 profile 路径映射。 | [ProfileList](../../artifacts/security/profilelist.md) |

## Linked Artifacts

- [Run / RunOnce](../../artifacts/persistence/run-keys.md)
- [StartupApproved](../../artifacts/persistence/startupapproved.md)
- [IFEO](../../artifacts/persistence/ifeo.md)
- [Winlogon Userinit](../../artifacts/persistence/winlogon-userinit.md)
- [Winlogon Shell](../../artifacts/persistence/winlogon-shell.md)
- [Command Processor AutoRun](../../artifacts/persistence/command-processor-autorun.md)
- [ProfileList](../../artifacts/security/profilelist.md)
- [Defender Policies](../../artifacts/security/defender-policies.md)
- [UAC Policies](../../artifacts/security/uac-policies.md)
- [SpecialAccounts\UserList](../../artifacts/security/specialaccounts-userlist.md)
- [CredSSP / NLA](../../artifacts/rdp/credssp-nla.md)
- [MUICache](../../artifacts/execution/muicache.md) for user Classes contrast.

## Collection Notes

=== "Live"

    ```cmd
    reg query "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
    reg query "HKLM\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Run"
    reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"
    reg query "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender" /s
    reg save HKLM\SOFTWARE C:\Temp\SOFTWARE.hiv
    ```

=== "Offline"

    ```text
    Collect:
    C:\Windows\System32\Config\SOFTWARE
    C:\Windows\System32\Config\SOFTWARE.LOG1
    C:\Windows\System32\Config\SOFTWARE.LOG2

    Then parse:
    Run / RunOnce
    Uninstall
    IFEO
    Winlogon
    Explorer\StartupApproved
    Policies
    WOW6432Node
    Classes
    ProfileList
    ```

## Analyst Checklist

- Check both 64-bit and 32-bit views for Run, Uninstall, Classes, and application keys.
- For Run / RunOnce, record value name, full command, path existence, signing, file hash, user-writable status, and StartupApproved state.
- For Uninstall, separate installed software inventory from execution evidence.
- For Defender policies, validate policy source, Tamper Protection, Defender Operational events, and live Defender status.
- For Winlogon, compare `Userinit` and `Shell` against environment baseline and verify login or process evidence.
- For ProfileList, map SID to profile before reading user hives.
- For Classes / COM, compare machine-level `Classes` with user-level `HKU\<SID>_Classes`.

## References

- [Microsoft Learn: Registry hives](https://learn.microsoft.com/en-us/windows/win32/sysinfo/registry-hives)
- [Microsoft Learn: 32-bit and 64-bit application data in the registry](https://learn.microsoft.com/en-us/windows/win32/winprog64/shared-registry-keys)
