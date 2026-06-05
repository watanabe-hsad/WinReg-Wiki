# 检测工程

注册表检测要把“路径命中”和“行为上下文”分开。许多合法软件会写入自启动项、服务和应用兼容性配置，因此检测规则应尽量描述可验证的组合。

## 通用策略

| 策略 | 示例 |
|---|---|
| 路径异常 | 机器级启动项指向用户 profile |
| 命令异常 | 启动项调用脚本解释器、下载器或 LOLBin |
| 名称伪装 | 服务名或 value name 模仿系统组件 |
| 时间线接近 | 新增启动项后立刻出现网络连接或进程启动 |
| 账户异常 | 普通用户上下文写入敏感位置 |
| 安全控制削弱 | Defender 排除项新增后出现 payload 落地 |
| 加载链异常 | LSA Authentication Packages 新增非基线包 |

## Sysmon 关注点

| Event ID | 用途 |
|---|---|
| 1 | Process Create |
| 6 | Driver Loaded |
| 7 | Image Loaded |
| 11 | File Create |
| 12 | Registry Object Created or Deleted |
| 13 | Registry Value Set |
| 14 | Registry Key and Value Renamed |

## Sigma 草稿示例

```yaml
title: Suspicious Run Key Command From User Writable Path
status: experimental
logsource:
  product: windows
  category: registry_set
detection:
  selection_key:
    TargetObject|contains:
      - '\Software\Microsoft\Windows\CurrentVersion\Run'
      - '\Software\Microsoft\Windows\CurrentVersion\RunOnce'
  selection_path:
    Details|contains:
      - '\AppData\'
      - '\Temp\'
      - '\Downloads\'
  condition: selection_key and selection_path
falsepositives:
  - Updaters and collaboration software
level: medium
```

## 常用检测入口

| 检测问题 | 注册表入口 | 交叉验证 |
|---|---|---|
| 登录启动项指向用户可写目录 | [HKCU Run](../registry-tree/hkcu/software/microsoft/windows/currentversion/run.md), [HKLM Run](../registry-tree/hklm/software/microsoft/windows/currentversion/run.md) | Sysmon 13, Prefetch, BAM, StartupApproved |
| Winlogon 登录链被追加 | [Winlogon](../registry-tree/hklm/software/microsoft/windows-nt/currentversion/winlogon.md) | 登录事件, 进程创建, Autoruns |
| LSASS 加载链异常 | [LSA](../registry-tree/hklm/system/controlset/control/lsa/index.md), [LSA Security Packages](../registry-tree/hklm/system/controlset/control/lsa/security-packages.md) | 模块加载, 文件签名, 重启时间线 |
| AppInit_DLLs 启用或指向异常 DLL | [AppInit_DLLs](../registry-tree/hklm/software/microsoft/windows-nt/currentversion/appinit-dlls.md) | Sysmon 7, DLL 签名, WOW6432Node |
| Active Setup 新增异常 StubPath | [Active Setup](../registry-tree/hklm/software/microsoft/active-setup.md) | 用户登录, 进程创建, Prefetch |
| Print Monitor 注册异常 DLL | [Print Monitors](../registry-tree/hklm/system/controlset/control/print-monitors.md) | Spooler 模块加载, PrintService, 文件签名 |
| Kernel driver 持久化或易受攻击驱动 | [Drivers](../registry-tree/hklm/system/controlset/services/drivers.md) | Sysmon 6, Code Integrity, System.evtx |
| `cmd.exe` 启动钩子 | [HKCU Command Processor](../registry-tree/hkcu/software/microsoft/command-processor.md), [HKLM Command Processor](../registry-tree/hklm/software/microsoft/command-processor.md) | cmd 子进程, PowerShell logs |
| Defender 配置被调整 | [Defender Policies](../registry-tree/hklm/software/policies/microsoft/windows-defender.md), [Windows Defender](../registry-tree/hklm/software/microsoft/windows-defender.md) | Defender Operational, GPO/MDM, EDR |
| RDP 服务端配置变化 | [Terminal Server](../registry-tree/hklm/system/controlset/control/terminal-server.md), [RDP-Tcp](../registry-tree/hklm/system/controlset/control/terminal-server/rdp-tcp.md), [FirewallPolicy](../registry-tree/hklm/system/controlset/services/sharedaccess/firewallpolicy.md) | TerminalServices, Security 4624, firewall logs |
| 审计或日志配置变化 | [SECURITY](../registry-tree/hklm/security.md), [EventLog](../registry-tree/hklm/system/controlset/services/eventlog.md) | Security 4719, GroupPolicy, event log gaps |
| 账户显示或 profile 异常 | [SpecialAccounts\UserList](../registry-tree/hklm/software/microsoft/windows-nt/currentversion/winlogon/specialaccounts-userlist.md), [ProfileList](../registry-tree/hklm/software/microsoft/windows-nt/currentversion/profilelist.md), [SAM](../registry-tree/hklm/sam.md) | SAM, Security 4720/4732/4738 |
| 新外接设备出现 | [USB](../registry-tree/hklm/system/controlset/enum/usb.md), [USBSTOR](../registry-tree/hklm/system/controlset/enum/usbstor.md), [SWD\WPDBUSENUM](../registry-tree/hklm/system/controlset/enum/swd-wpdbusenum.md) | SetupAPI.dev.log, DriverFrameworks, LNK/Jump Lists |

## 补充阅读

- [Artifact 补充索引](../artifacts/index.md)
- [结构化数据索引](../artifacts/generated-index.md)
