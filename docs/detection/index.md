# 检测工程

注册表检测要把“路径命中”和“行为上下文”分开。许多合法软件会写入自启动项、服务和应用兼容性配置，因此检测规则应尽量描述高信号组合。

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

## 高价值检测入口

| 检测问题 | 注册表入口 | 交叉验证 |
|---|---|---|
| 登录启动项指向用户可写目录 | [Run / RunOnce](../artifacts/persistence/run-keys.md), [StartupApproved](../artifacts/persistence/startupapproved.md) | Sysmon 13, Prefetch, BAM |
| Winlogon 登录链被追加 | [Winlogon Userinit](../artifacts/persistence/winlogon-userinit.md), [Winlogon Shell](../artifacts/persistence/winlogon-shell.md) | 登录事件, 进程创建, Autoruns |
| LSASS 加载链异常 | [LSA Authentication Packages](../artifacts/persistence/lsa-authentication-packages.md) | 模块加载, 文件签名, 重启时间线 |
| cmd.exe 启动钩子 | [Command Processor AutoRun](../artifacts/persistence/command-processor-autorun.md) | cmd 子进程, PowerShell logs |
| Defender 被削弱 | [Defender Policies](../artifacts/security/defender-policies.md) | Defender Operational, GPO/MDM, EDR |
| RDP 服务端暴露 | [fDenyTSConnections](../artifacts/rdp/fdenytsconnections.md), [RDP-Tcp PortNumber](../artifacts/rdp/rdp-tcp-portnumber.md), [Firewall Policies](../artifacts/security/firewall-policies.md) | TerminalServices, Security 4624, firewall logs |
| 审计能力降低 | [Audit Policy](../artifacts/security/audit-policy.md) | Security 4719, GroupPolicy, event log gaps |
| 隐藏账户 | [SpecialAccounts\UserList](../artifacts/security/specialaccounts-userlist.md), [ProfileList](../artifacts/security/profilelist.md) | SAM, Security 4720/4732/4738 |
