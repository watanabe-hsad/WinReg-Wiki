---
tags:
  - UserActivity
  - Shell
  - RecentDocs
  - NTUSER.DAT
---

# RecentDocs

<div class="rfh-meta" markdown>
<span class="rfh-badge medium">取证价值 中</span>
<span class="rfh-badge low">检测价值 低</span>
<span class="rfh-badge">最近文档名称线索</span>
</div>

## 摘要

RecentDocs 记录用户 Shell 最近接触过的文档名称和扩展名分组，可提示文件交互线索，但不能单独证明文件内容被读取。

## 注册表路径

| View | Hive / File | Path | Scope |
|---|---|---|---|
| Live path | `HKCU` | `Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs` | 当前用户 |
| Live path | `HKCU` | `Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs\.<ext>` | 当前用户，按扩展名分组 |
| Offline hive path | `NTUSER.DAT` | `Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs` | 用户 SID |

## 原生注册表视图

在 `regedit.exe` 中从 `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs` 展开。扩展名子键如 `.docx`、`.pdf`、`.zip` 会保存同类型最近文档条目。

## 离线位置

`C:\Users\<user>\NTUSER.DAT`。需要用 [ProfileList](../security/profilelist.md) 映射 SID，避免把不同用户的 RecentDocs 混在一起。

## 字段含义

| Field | Meaning |
|---|---|
| 根 key value | 最近文档名称或 shell item 数据，具体编码需工具解析 |
| `.<ext>` 子键 | 按扩展名分组的最近文档列表 |
| `MRUListEx` | 最近使用顺序，二进制结构 |
| key LastWrite | 对应 key 最近变化时间，不等于文件打开时间 |

## 取证含义

RecentDocs 可提示用户 profile 中出现过某些文件名、扩展名和最近使用顺序。它适合用来发现敏感文件名、压缩包、脚本、文档、外接盘或共享访问线索。它不提供完整路径时，应与 LNK、Jump Lists、ShellBags 和 file system artifacts 结合。

## 可以证明

- 某个用户 hive 中存在特定文件名或扩展名分组记录。
- 可提示用户 Shell 最近接触过某类文件。
- `MRUListEx` 可辅助判断条目相对顺序。

## 不能证明

- 文件内容被读取或修改。
- 文件来自哪个完整路径，除非解析数据中可恢复路径。
- 文件当前仍存在。
- key LastWrite 是具体文档打开时间。

## 时间戳说明

RecentDocs value 通常没有独立时间戳。根 key 和扩展名子键 LastWrite 可提示列表更新，但不能精确到单个文档条目。工具解析出的 MRU 顺序和 LastWrite 应分别报告。

## 系统版本差异

Windows 7/10/11 常见 RecentDocs，但 Jump Lists 在新系统中往往提供更强路径和时间线信息。Server 和禁用 Explorer 的系统记录可能有限。版本差异细节待验证。

## 攻击滥用

攻击者打开敏感文档、压缩包、脚本或从外接介质浏览文件时可能留下 RecentDocs。攻击者也可能清理 Explorer 最近项目以降低用户行为痕迹。

## 检测思路

- RecentDocs 出现敏感文件名、泄露清单、凭据文件、`.kdbx`、`.pst`、`.zip`、`.7z`、`.ps1`。
- RecentDocs 与 LNK、Jump Lists、MountPoints2 指向同一可移动介质或共享。
- RecentDocs key 更新接近大量文件访问、压缩或外传事件。

## 常见误报

- 正常办公文档、下载文件、邮件附件、压缩包、浏览器保存文件。
- 应用预览、文件对话框或 Explorer 自动更新最近项目。

## 采集方式

=== "PowerShell"

    ```powershell
    Get-ChildItem "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs" -Recurse -ErrorAction SilentlyContinue
    ```

=== "reg.exe"

    ```cmd
    reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs" /s
    ```

=== "Offline"

    ```text
    Collect C:\Users\<user>\NTUSER.DAT and parse RecentDocs root and extension subkeys.
    ```

## 解析工具

- Registry Explorer
- RECmd
- RegRipper
- KAPE
- Velociraptor

## 交叉验证

- LNK
- Jump Lists
- ShellBags
- OpenSavePidlMRU
- LastVisitedPidlMRU
- `$MFT`
- `$UsnJrnl`
- EDR file events

## 示例结论

- `RecentDocs\.kdbx` contains `Passwords.kdbx` in the user hive; this proves the user's RecentDocs list references that filename, but not that the database was opened successfully or read.
- RecentDocs, Jump List, and `$MFT` all reference `E:\Finance\Q4.zip` near the same time window; together they support a stronger user file interaction finding than RecentDocs alone.

## 参考资料

- [artefacts.help: RecentDocs](https://artefacts.help/windows_registry_recentdocs.html)
- [SANS DFIR Poster: Windows Forensic Analysis](https://www.sans.org/posters/windows-forensic-analysis/)

## 相关页面

- 场景：[Shell / Explorer 用户行为](../../questions/shell-explorer.md)
- 注册表位置：[HKEY_CURRENT_USER](../../registry-tree/hkcu/index.md), [HKCU Explorer](../../registry-tree/hkcu/software/microsoft/windows/currentversion/explorer.md)
