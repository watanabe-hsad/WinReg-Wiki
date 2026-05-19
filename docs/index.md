# Windows 注册表取证与检测手册

<p class="rfh-kicker">Registry Forensics & Detection Handbook</p>

这个 demo 的目标不是做一份“注册表路径大全”，而是做一份调查导向的注册表地图：当你在做取证、应急响应、威胁狩猎或检测规则设计时，能快速知道该看哪里、能证明什么、不能证明什么、怎么交叉验证。

## 两个入口

<div class="grid cards" markdown>

- **按调查场景查**

    从真实问题进入，例如“有没有程序执行痕迹”“有没有自启动”“是否插入过 USB”“是否连接过 RDP”。

    [进入调查场景](questions/index.md)

- **按注册表位置查**

    从 Windows 原生根键进入，例如 `HKEY_LOCAL_MACHINE`、`HKEY_CURRENT_USER`、`HKEY_USERS`，再落到 `SYSTEM`、`SOFTWARE`、`NTUSER.DAT`、`UsrClass.dat` 等离线 hive。

    [进入注册表位置](registry-tree/index.md)

</div>

## 当前覆盖

当前手册已经从 demo 扩展为按调查问题和注册表原生结构组织的实战索引，优先覆盖高价值 artifact：

| 场景 | 示例条目 |
|---|---|
| 程序执行 / 程序存在 | [UserAssist](artifacts/execution/userassist.md), [Amcache](artifacts/execution/amcache.md), [ShimCache](artifacts/execution/shimcache.md), [BAM / DAM](artifacts/execution/bam-dam.md), [MUICache](artifacts/execution/muicache.md) |
| 持久化 | [Run / RunOnce](artifacts/persistence/run-keys.md), [StartupApproved](artifacts/persistence/startupapproved.md), [Services](artifacts/persistence/services.md), [IFEO](artifacts/persistence/ifeo.md), [Winlogon Userinit](artifacts/persistence/winlogon-userinit.md), [Winlogon Shell](artifacts/persistence/winlogon-shell.md), [LSA Authentication Packages](artifacts/persistence/lsa-authentication-packages.md), [Command Processor AutoRun](artifacts/persistence/command-processor-autorun.md) |
| USB / 外接设备 | [USBSTOR](artifacts/usb/usbstor.md), [MountedDevices](artifacts/usb/mounteddevices.md), [MountPoints2](artifacts/usb/mountpoints2.md) |
| 远程访问 | [Terminal Server Client](artifacts/rdp/terminal-server-client.md) |
| 账户 / 安全 / 防护策略 | [ProfileList](artifacts/security/profilelist.md), [Defender Policies](artifacts/security/defender-policies.md), [LSA Authentication Packages](artifacts/persistence/lsa-authentication-packages.md) |

## 页面原则

每个 artifact 页面都尽量回答这些问题：

- 这个注册表项通常记录什么？
- 它能证明什么，不能证明什么？
- 时间戳语义是什么？
- 攻击者可能怎么利用？
- 检测时有哪些高信号特征？
- 应该和哪些日志、文件或其他 artifact 交叉验证？

!!! note "取证语义优先"
    注册表很少单独定案。这个手册会尽量把“配置存在”“用户交互”“程序执行”“设备连接”“恶意行为”这些不同证据语义区分开。
