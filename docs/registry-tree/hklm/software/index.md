# HKLM\SOFTWARE

`HKLM\SOFTWARE` 保存机器级软件、策略、登录流程、ProfileList、Defender、Classes 和 32 位重定向视图。

## 文件

| 项 | 路径 |
|---|---|
| Hive | `C:\Windows\System32\Config\SOFTWARE` |
| Transaction logs | `SOFTWARE.LOG1`, `SOFTWARE.LOG2` |

## 32 位视图

64 位 Windows 同时存在：

```text
HKLM\SOFTWARE
HKLM\SOFTWARE\WOW6432Node
```

32 位软件、COM、Uninstall 记录或 Run key 可能只在 `WOW6432Node`。

## 常用路径

| 路径 | 含义 |
|---|---|
| [`Microsoft\Active Setup\Installed Components`](microsoft/active-setup.md) | Active Setup 机器级组件定义。 |
| [`Microsoft\Command Processor`](microsoft/command-processor.md) | 机器级 `cmd.exe` 配置和 `AutoRun`。 |
| [`Microsoft\Windows\CurrentVersion\App Paths`](microsoft/windows/currentversion/app-paths.md) | 应用程序注册路径。 |
| [`Microsoft\Windows\CurrentVersion\Authentication\LogonUI`](microsoft/windows/currentversion/authentication/logonui.md) | 登录界面相关状态和显示线索。 |
| [`Microsoft\Windows\CurrentVersion\Policies\System`](microsoft/windows/currentversion/policies/system.md) | UAC 和系统安全策略。 |
| [`Microsoft\Windows\CurrentVersion\Run`](microsoft/windows/currentversion/run.md) | 机器级登录启动项。 |
| [`Microsoft\Windows\CurrentVersion\RunOnce`](microsoft/windows/currentversion/run.md) | 机器级一次性登录启动项。 |
| [`Microsoft\Windows\CurrentVersion\Uninstall`](microsoft/windows/currentversion/uninstall.md) | 软件安装登记。 |
| [`Microsoft\Windows NT\CurrentVersion\Image File Execution Options`](microsoft/windows-nt/currentversion/ifeo.md) | IFEO、Debugger、进程启动相关配置。 |
| [`Microsoft\Windows NT\CurrentVersion\AeDebug`](microsoft/windows-nt/currentversion/aedebug.md) | 应用崩溃后调试器配置。 |
| [`Microsoft\Windows NT\CurrentVersion\Windows`](microsoft/windows-nt/currentversion/appinit-dlls.md) | `AppInit_DLLs`、`LoadAppInit_DLLs` 等。 |
| [`Microsoft\Windows NT\CurrentVersion\Winlogon`](microsoft/windows-nt/currentversion/winlogon.md) | `Userinit`、`Shell`、自动登录等。 |
| [`Microsoft\Windows NT\CurrentVersion\Winlogon\Notify`](microsoft/windows-nt/currentversion/winlogon/notify.md) | Winlogon notification package。 |
| [`Microsoft\Windows NT\CurrentVersion\ProfileList`](microsoft/windows-nt/currentversion/profilelist.md) | SID 到用户 profile 路径的映射。 |
| `Microsoft\Windows\CurrentVersion\Explorer` | Explorer 机器级配置、StartupApproved。 |
| [`Microsoft\Windows\CurrentVersion\ShellServiceObjectDelayLoad`](microsoft/windows/currentversion/shellserviceobjectdelayload.md) | Explorer Shell COM 延迟加载配置。 |
| [`Microsoft\Windows Portable Devices`](microsoft/windows-portable-devices.md) | 便携设备元数据。 |
| [`Microsoft\Windows NT\CurrentVersion\EMDMgmt`](microsoft/windows-nt/currentversion/emdmgmt.md) | EMDMgmt / ReadyBoost 相关记录。 |
| [`Microsoft\Windows Search\VolumeInfoCache`](microsoft/windows-search/volumeinfocache.md) | Windows Search 卷信息缓存。 |
| [`Microsoft\Windows NT\CurrentVersion\NetworkList\Profiles`](microsoft/windows-nt/currentversion/networklist/profiles.md) | 网络配置文件。 |
| [`Microsoft\Windows Defender`](microsoft/windows-defender.md) | Defender 本地状态和配置线索。 |
| [`Policies`](policies.md) | GPO / MDM / 本地策略写入位置。 |
| [`Policies\Microsoft\Windows Defender`](policies/microsoft/windows-defender.md) | Defender 策略和排除项。 |
| [`Policies\Microsoft\WindowsFirewall`](policies/microsoft/windowsfirewall.md) | Windows Firewall 策略配置。 |
| `Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\UserList` | 登录界面隐藏用户配置。 |
| [`WOW6432Node`](wow6432node.md) | 32 位应用注册表视图。 |
| [`Classes`](classes.md) | 机器级文件关联、COM、协议处理器。 |

## 注意

| 项 | 说明 |
|---|---|
| `Uninstall` | 记录软件登记，不等于程序执行。 |
| `Policies` | 表示注册表中的策略状态，不直接说明来源或实际生效。 |
| Defender policy | 需结合平台版本、Tamper Protection 和 Defender 日志判断。 |
| `Classes` | `HKCU\Software\Classes` 可参与覆盖，最终视图见 `HKCR`。 |

## 相关场景

- [自启动与持久化](../../../questions/persistence.md)
- [安全策略与防护配置](../../../questions/policy-security.md)
- [程序执行痕迹](../../../questions/execution.md)
- [账户与安全](../../../questions/accounts-security.md)
- [网络与系统环境](../../../questions/network.md)
- [常规注册表检查](../../../questions/registry-checklist.md)

## 补充阅读

[Run / RunOnce](../../../artifacts/persistence/run-keys.md),
[Active Setup](../../../artifacts/persistence/active-setup.md),
[StartupApproved](../../../artifacts/persistence/startupapproved.md),
[IFEO](../../../artifacts/persistence/ifeo.md),
[AppInit_DLLs](../../../artifacts/persistence/appinit-dlls.md),
[Winlogon Userinit](../../../artifacts/persistence/winlogon-userinit.md),
[Winlogon Shell](../../../artifacts/persistence/winlogon-shell.md),
[ShellServiceObjectDelayLoad](../../../artifacts/persistence/shellserviceobjectdelayload.md),
[Portable Devices](../../../artifacts/usb/portable-devices.md),
[EMDMgmt](../../../artifacts/usb/emdmgmt.md),
[VolumeInfoCache](../../../artifacts/usb/volumeinfocache.md),
[ProfileList](../../../artifacts/security/profilelist.md),
[Defender Policies](../../../artifacts/security/defender-policies.md),
[UAC Policies](../../../artifacts/security/uac-policies.md),
[SpecialAccounts\UserList](../../../artifacts/security/specialaccounts-userlist.md)
