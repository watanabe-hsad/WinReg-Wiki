---
tags:
  - USB
  - UserActivity
  - NTUSER.DAT
  - HKCU
---

# MountPoints2

<div class="rfh-meta" markdown>
<span class="rfh-badge high">取证价值 高</span>
<span class="rfh-badge low">检测价值 低</span>
<span class="rfh-badge">用户见过的卷 / 共享</span>
</div>

## 摘要

MountPoints2 记录用户 Shell 见过的卷、盘符、可移动介质或网络位置，可把设备/卷线索归属到具体用户。

## 注册表路径

| View | Hive / File | Path | Scope |
|---|---|---|---|
| Live path | `HKCU` | `Software\Microsoft\Windows\CurrentVersion\Explorer\MountPoints2` | 当前用户 |
| Live path | `HKU\<SID>` | `Software\Microsoft\Windows\CurrentVersion\Explorer\MountPoints2` | 指定 SID |
| Offline hive path | `NTUSER.DAT` | `Software\Microsoft\Windows\CurrentVersion\Explorer\MountPoints2` | 用户级 |

## 原生注册表视图

在 live 系统中从 `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\MountPoints2` 展开。子键可能包含卷 GUID、盘符相关记录、网络共享路径等，取决于用户访问历史和 Windows 版本。

## 离线位置

对应目标用户 `C:\Users\<user>\NTUSER.DAT`。必须先用 [ProfileList](../security/profilelist.md) 确认 `HKU\<SID>` 属于哪个用户，再与 `SYSTEM\MountedDevices`、`USBSTOR` 和 SetupAPI 日志关联。

## 字段含义

| Field | Meaning |
|---|---|
| volume GUID 子键 | 用户 Shell 见过的卷标识或挂载点线索 |
| `##server#share` 形式子键 | 网络共享访问线索 |
| `_Autorun`、`Shell` 等子键 | 与自动播放、Shell 行为相关的历史配置或动作 |
| key LastWrite | MountPoints2 子键最近变化时间，可提示用户访问或 Shell 更新，但需交叉验证 |

## 取证含义

MountPoints2 的核心价值是把“某个卷或共享曾在用户上下文中出现”归属到 SID。它比 `MountedDevices` 更接近用户层视角，但不能单独证明文件复制、文件打开或设备物理插入。

## 可以证明

- 某个用户 hive 中存在指定卷、盘符或网络共享的 MountPoints2 记录。
- 可辅助证明该用户上下文曾见过或访问过该位置。
- 与 USBSTOR、MountedDevices、LNK、Jump Lists 结合，可把设备和用户行为连接起来。

## 不能证明

- 不能单独证明 USB 设备插入时间。
- 不能单独证明文件被打开、复制或外传。
- 不能证明卷当前仍连接，也不能证明盘符仍相同。
- 不能把 key LastWrite 直接当作首次插入时间。

## 时间戳说明

MountPoints2 子键 LastWrite 可能在用户首次访问、再次浏览、自动播放配置变化或 Shell 更新时变化。对卷 GUID 子键和子项分别查看 LastWrite。报告中应写成“可提示该用户 Shell 在该时间附近更新过该挂载点记录”，避免写成“设备插入时间”。

## 系统版本差异

Windows 7/10/11 都可能存在 MountPoints2，但子键形态、自动播放相关内容和 Shell 行为可能变化。Server 上如果 Explorer 使用较少，记录可能有限。网络共享、可移动磁盘和 MTP 设备的表现不同，未知设备类型应标记待验证。

## 攻击滥用

攻击者使用 USB、挂载 VHD、访问 SMB 共享或运行来自外接卷的工具时，可能留下 MountPoints2 线索。攻击者可能清理用户 hive 中的 MountPoints2、RecentDocs、LNK 或 Jump Lists，造成设备行为链断裂。

## 检测思路

- 低频用于实时检测，更适合事后狩猎：用户 hive 中出现敏感共享、攻击者基础设施主机名、异常卷 GUID。
- MountPoints2 新记录与 LNK、Jump Lists、USBSTOR、网络登录事件在短时间内相互印证。
- 用户访问 `\\host\ADMIN$`、`\\host\C$`、未知 NAS 或临时共享后出现可疑进程执行。

## 常见误报

- 正常 USB 使用、企业共享盘、打印扫描共享、OneDrive/同步软件、备份软件。
- Explorer 浏览、文件对话框、自动播放设置都可能更新记录。
- 盘符复用和卷重格式化可能导致表面相似但实际不同的映射。

## 采集方式

=== "PowerShell"

    ```powershell
    Get-ChildItem "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\MountPoints2" -Recurse -ErrorAction SilentlyContinue
    ```

=== "reg.exe"

    ```cmd
    reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\MountPoints2" /s
    ```

=== "Offline"

    ```text
    Collect each user's NTUSER.DAT plus SYSTEM hive.
    Correlate MountPoints2 with SYSTEM\MountedDevices and ControlSet00x\Enum\USBSTOR.
    ```

## 解析工具

- Registry Explorer：适合查看子键结构和 LastWrite。
- RECmd：适合批量导出所有用户 MountPoints2。
- RegRipper：可用插件解析，注意插件版本。
- KAPE：采集 user hives、LNK、Jump Lists、USB artifact。
- Velociraptor：适合跨主机搜索共享名或卷 GUID。

## 交叉验证

- [USBSTOR](usbstor.md)、[MountedDevices](mounteddevices.md)。
- SetupAPI.dev.log、DriverFrameworks-UserMode/Operational、Partition/Diagnostic。
- LNK、Jump Lists、RecentDocs、ShellBags。
- `$MFT`、`$UsnJrnl`、文件访问审计、EDR removable media events。

## 示例结论

- `NTUSER.DAT` 中 `MountPoints2\{volume-guid}` 的 LastWrite 为 `2026-05-17 09:13:22 UTC`，同一卷 GUID 可在 `SYSTEM\MountedDevices` 映射到历史 `E:`；该证据可提示该用户 Shell 在该时间附近见过该卷，但不能单独证明文件复制。
- `MountPoints2\##10.10.4.20#share`、Jump List 和 `cmd.exe /c copy` 进程日志时间接近，可支持用户访问 SMB 共享并执行文件操作的调查方向。

## 相关页面

- 场景：[USB 与外接设备](../../questions/usb.md)、[Shell / Explorer 用户行为](../../questions/shell-explorer.md)
- 注册表位置：[HKCU Explorer](../../registry-tree/hkcu/explorer.md)、[NTUSER.DAT](../../registry-tree/hku/ntuser.md)

## 参考资料

- [artefacts.help: MountPoints2](https://artefacts.help/windows_registry_mountpoints2.html)
- [SANS DFIR Poster: Windows Forensic Analysis](https://www.sans.org/posters/windows-forensic-analysis/)
