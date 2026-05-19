# Artifact 索引

这个入口按 artifact 类型组织。每个细页都优先回答路径、证据强度、时间戳语义、检测思路和交叉验证。结构化 YAML 生成的表格见 [Generated Data Index](generated-index.md)。

## 程序执行 / 程序存在

| Artifact | Hive | 证据语义 | 价值 |
|---|---|---|---|
| [UserAssist](execution/userassist.md) | `NTUSER.DAT` | 用户交互执行线索 | Explorer 相关程序交互 |
| [BAM / DAM](execution/bam-dam.md) | `SYSTEM` | SID 维度运行线索 | 近期程序活动与用户归属 |
| [Amcache](execution/amcache.md) | `Amcache.hve` | 程序存在 / 元数据 | 路径、哈希、版本信息 |
| [ShimCache / AppCompatCache](execution/shimcache.md) | `SYSTEM` | 程序路径缓存 | 兼容性缓存，执行语义需谨慎 |
| [MUICache](execution/muicache.md) | `UsrClass.dat`, `NTUSER.DAT` | Shell 显示缓存 | 程序路径和显示名线索 |

## 持久化 / 自启动

| Artifact | Hive | 证据语义 | 价值 |
|---|---|---|---|
| [Run / RunOnce](persistence/run-keys.md) | `NTUSER.DAT`, `SOFTWARE` | 登录启动配置 | 用户级和机器级 autorun |
| [StartupApproved](persistence/startupapproved.md) | `NTUSER.DAT`, `SOFTWARE` | 启动项状态 | 启用/禁用状态与 Run key 对齐 |
| [Services](persistence/services.md) | `SYSTEM` | 服务 / 驱动配置 | 高权限持久化 |
| [IFEO](persistence/ifeo.md) | `SOFTWARE` | Debugger 劫持 | 可执行文件启动劫持 |
| [Winlogon Userinit](persistence/winlogon-userinit.md) | `SOFTWARE` | 登录初始化链 | 登录后追加命令 |
| [Winlogon Shell](persistence/winlogon-shell.md) | `SOFTWARE`, `NTUSER.DAT` | 登录 Shell 配置 | Shell 替换或追加命令 |
| [LSA Authentication Packages](persistence/lsa-authentication-packages.md) | `SYSTEM` | LSASS 加载链配置 | 凭据访问与高权限持久化 |
| [Command Processor AutoRun](persistence/command-processor-autorun.md) | `NTUSER.DAT`, `SOFTWARE` | `cmd.exe` 启动钩子 | 隐蔽命令自动执行 |

## USB / 设备

| Artifact | Hive | 证据语义 | 价值 |
|---|---|---|---|
| [USBSTOR](usb/usbstor.md) | `SYSTEM` | USB 存储枚举 | 厂商、产品、序列号 |
| [MountedDevices](usb/mounteddevices.md) | `SYSTEM` | 卷和盘符映射 | 盘符、卷 GUID、设备映射 |
| [MountPoints2](usb/mountpoints2.md) | `NTUSER.DAT` | 用户见过的卷 / 共享 | 用户 SID 与卷、共享关联 |

## 用户行为 / Shell

| Artifact | Hive | 证据语义 | 价值 |
|---|---|---|---|
| [RunMRU](user-activity/runmru.md) | `NTUSER.DAT` | Run dialog 输入历史 | 命令、路径、UNC、URL 输入线索 |
| [RecentDocs](user-activity/recentdocs.md) | `NTUSER.DAT` | 最近文档名称线索 | 文件名、扩展名分组、MRU 顺序 |
| [OpenSavePidlMRU](user-activity/opensavepidlmru.md) | `NTUSER.DAT` | 文件对话框路径线索 | PIDL 解析出的打开/保存位置 |
| [LastVisitedPidlMRU](user-activity/lastvisitedpidlmru.md) | `NTUSER.DAT` | 应用与目录关系 | 应用程序和最近访问目录关联 |

## RDP / 远程访问

| Artifact | Hive | 证据语义 | 价值 |
|---|---|---|---|
| [Terminal Server Client](rdp/terminal-server-client.md) | `NTUSER.DAT` | RDP 客户端目标 | MSTSC 目标和用户名提示 |
| [fDenyTSConnections](rdp/fdenytsconnections.md) | `SYSTEM` | RDP 服务端允许状态 | 是否允许远程桌面连接 |
| [RDP-Tcp PortNumber](rdp/rdp-tcp-portnumber.md) | `SYSTEM` | RDP 监听端口配置 | 默认/非默认端口和暴露面 |
| [CredSSP / NLA](rdp/credssp-nla.md) | `SYSTEM`, `SOFTWARE` | RDP 认证安全配置 | NLA、SecurityLayer、CredSSP 策略 |

## 账户 / 安全策略

| Artifact | Hive | 证据语义 | 价值 |
|---|---|---|---|
| [ProfileList](security/profilelist.md) | `SOFTWARE` | SID 到 profile 映射 | 用户级 artifact 归属基础 |
| [Defender Policies](security/defender-policies.md) | `SOFTWARE` | 安全控制配置 | Defender 排除项和防护策略 |
| [UAC Policies](security/uac-policies.md) | `SOFTWARE` | 权限提升策略 | UAC、提示行为、远程本地账户 token 过滤 |
| [Firewall Policies](security/firewall-policies.md) | `SYSTEM`, `SOFTWARE` | 防火墙规则与配置 | 入站规则、profile 状态、RDP/WinRM 暴露 |
| [Audit Policy](security/audit-policy.md) | `SECURITY` | 日志可见性策略 | 审计能力和日志缺失解释 |
| [SpecialAccounts\UserList](security/specialaccounts-userlist.md) | `SOFTWARE` | 登录界面账户可见性 | 隐藏账户线索 |
