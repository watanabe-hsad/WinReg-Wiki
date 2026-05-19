---
tags:
  - UserActivity
  - Shell
  - NTUSER.DAT
  - HKCU
---

# RunMRU

<div class="rfh-meta" markdown>
<span class="rfh-badge medium">取证价值 中</span>
<span class="rfh-badge low">检测价值 低</span>
<span class="rfh-badge">Run 对话框输入历史</span>
</div>

## 摘要

RunMRU 记录用户在 Windows Run dialog 中输入过的命令或路径，可提示用户意图和交互，但不能单独证明命令执行成功。

## 注册表路径

| View | Hive / File | Path | Scope |
|---|---|---|---|
| Live path | `HKCU` | `Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU` | 当前用户 |
| Offline hive path | `NTUSER.DAT` | `Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU` | 用户 SID |

## 原生注册表视图

在 `regedit.exe` 中从 `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU` 展开。离线时应读取目标用户的 `NTUSER.DAT`，并用 [ProfileList](../security/profilelist.md) 记录 SID 到 profile 的映射。

## 离线位置

`C:\Users\<user>\NTUSER.DAT`。多用户主机必须逐个用户 hive 检查，不能把 live `HKCU` 输出泛化到所有用户。

## 字段含义

| Field | Meaning |
|---|---|
| `a`、`b`、`c` 等 value | 用户输入过的命令、路径、URL 或控制面板项 |
| `MRUList` | value 字母的最近使用顺序，左侧通常较新 |
| key LastWrite | RunMRU key 最近变化时间，不是某个 value 的精确创建时间 |

## 取证含义

RunMRU 适合回答“用户是否在 Run dialog 中输入过这段文本”。它对横向移动、命令执行、打开共享路径、启动管理工具很有帮助。它的证据语义是用户输入历史，不是进程创建日志。

## 可以证明

- 某个用户 hive 中存在 Run dialog 输入历史。
- 可提示用户输入过 `cmd`、`powershell`、UNC 路径、URL、控制面板命令或程序名。
- `MRUList` 可辅助判断条目相对新旧顺序。

## 不能证明

- 命令一定执行成功。
- 程序一定存在或被启动。
- 输入者一定是键盘前的本人。
- key LastWrite 是某个具体条目的创建时间。

## 时间戳说明

RunMRU value 没有独立时间戳。key LastWrite 表示 RunMRU key 的直接内容最近变化，可能由新增、删除或重排 MRU 导致。报告中应把 LastWrite 写为“RunMRU 更新附近时间”，而不是“命令执行时间”。

## 系统版本差异

RunMRU 在 Windows 7/10/11 常见，但 Windows 版本、隐私设置、Run dialog 使用方式和策略可能影响记录。Server Core 或很少使用 Explorer 的系统可能没有该 artifact。版本差异细节待验证。

## 攻击滥用

攻击者或操作者可能通过 Win+R 输入 `cmd`、`powershell`、`mstsc`、`\\host\share`、`regedit`、`control` 等命令。清理时可能删除 RunMRU 或清空 Explorer 历史。

## 检测思路

- RunMRU 中出现 `\\host\ADMIN$`、`\\host\C$`、未知 SMB 共享或公网 URL。
- RunMRU 中出现 `powershell -enc`、`cmd /c`、`mshta`、`rundll32`、`regsvr32` 等命令片段。
- RunMRU LastWrite 与进程日志、LNK、Jump Lists、ShellBags 或网络连接时间接近。

## 常见误报

- 管理员、开发人员、helpdesk 经常使用 Run dialog。
- 用户打开控制面板项、程序、网络共享和系统工具会产生正常记录。
- 企业远程支持和培训场景可能大量出现 `mstsc`、`cmd` 或 UNC 路径。

## 采集方式

=== "PowerShell"

    ```powershell
    Get-ItemProperty "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU" -ErrorAction SilentlyContinue
    ```

=== "reg.exe"

    ```cmd
    reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU"
    ```

=== "Offline"

    ```text
    Collect C:\Users\<user>\NTUSER.DAT and inspect Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU.
    ```

## 解析工具

- Registry Explorer
- RECmd
- RegRipper
- KAPE
- Velociraptor

## 交叉验证

- Sysmon Event ID 1 / Security 4688
- PowerShell logs
- UserAssist
- LNK
- Jump Lists
- ShellBags
- Network share access logs

## 示例结论

- `NTUSER.DAT` for SID `S-1-5-21-...-1001` contains RunMRU value `a=\\10.10.4.20\share`; this proves the user profile contains a Run dialog input for that UNC path, but does not prove the share was successfully accessed.
- RunMRU includes `powershell -enc ...`, and Sysmon Event ID 1 shows `powershell.exe` with matching command line two minutes later; together these support user-context command execution, not RunMRU alone.

## 参考资料

- [artefacts.help: RunMRU](https://artefacts.help/windows_registry_runmru.html)
- [SANS DFIR Poster: Windows Forensic Analysis](https://www.sans.org/posters/windows-forensic-analysis/)

## 相关页面

- 场景：[Shell / Explorer 用户行为](../../questions/shell-explorer.md)
- 注册表位置：[HKEY_CURRENT_USER](../../registry-tree/hkey-current-user.md), [HKCU Explorer](../../registry-tree/hkcu/explorer.md), [HKEY_USERS](../../registry-tree/hkey-users.md)
