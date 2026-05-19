---
tags:
  - UserActivity
  - ComDlg32
  - NTUSER.DAT
---

# LastVisitedPidlMRU

<div class="rfh-meta" markdown>
<span class="rfh-badge high">取证价值 高</span>
<span class="rfh-badge low">检测价值 低</span>
<span class="rfh-badge">应用与目录关系</span>
</div>

## Summary

LastVisitedPidlMRU 记录应用程序与最近访问目录之间的关系，常用于把“哪个程序打开过哪个位置”与 OpenSavePidlMRU 交叉分析。

## Registry Paths

| View | Hive / File | Path | Scope |
|---|---|---|---|
| Live path | `HKCU` | `Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\LastVisitedPidlMRU` | 当前用户 |
| Offline hive path | `NTUSER.DAT` | `Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\LastVisitedPidlMRU` | 用户 SID |

## Native Registry View

在 `regedit.exe` 中展开 `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\LastVisitedPidlMRU`。value 通常包含应用程序名和 PIDL / shell item 数据。

## Offline Location

`C:\Users\<user>\NTUSER.DAT`。该 artifact 应与同一用户的 OpenSavePidlMRU、RecentDocs、LNK 和 Jump Lists 共同解释。

## Data Meaning

| Field | Meaning |
|---|---|
| numbered values | 常包含应用程序名和最近访问位置的 PIDL 数据 |
| `MRUListEx` | 最近使用顺序 |
| application name | 与 common dialog 交互的程序，例如 `excel.exe`、`notepad.exe`、`chrome.exe` |
| PIDL data | 可解析为目录、卷、网络位置或 shell namespace |

## Forensic Meaning

LastVisitedPidlMRU 的价值在于把应用程序和目录关联起来。它适合回答“哪个应用最近通过 common dialog 访问过哪个位置”，尤其适合与 OpenSavePidlMRU 的文件名/路径线索合并。

## What It Can Prove

- 某个用户 hive 中存在应用与最近访问位置的 MRU 记录。
- 可辅助证明某应用通过文件对话框访问过某目录或 shell 位置。
- 可与 OpenSavePidlMRU 组合恢复更完整的应用-目录-文件关系。

## What It Cannot Prove

- 应用成功打开或保存了文件。
- 目录中的具体文件内容被读取。
- 应用行为一定由用户主动触发。
- LastWrite 是具体文件访问时间。

## Timestamp Notes

key LastWrite 表示 LastVisitedPidlMRU key 最近变化。PIDL 或 shell item 中可能存在对象时间字段，但不一定代表应用访问时间。报告中应区分 key LastWrite、MRU 顺序、PIDL 内部时间和文件系统时间。

## OS Version Notes

Windows 7/10/11 常见该 artifact，但不同应用框架、common dialog 实现和隐私设置会影响覆盖范围。UWP/现代应用行为待验证。

## Attacker Usage

攻击者使用图形工具、编辑器、压缩工具、浏览器上传对话框或远控文件管理器时，可能留下应用与目录的关联。清理最近项目和 Explorer MRU 可能删除部分痕迹。

## Detection Ideas

- `powershell_ise.exe`、`notepad.exe`、压缩工具、浏览器或远控工具关联敏感共享或可移动盘目录。
- LastVisitedPidlMRU 中的应用-目录关系与 OpenSavePidlMRU 文件名和 Jump Lists 时间线一致。
- 应用访问目录接近大规模压缩、上传或文件拷贝事件。

## False Positives

- 正常办公、编辑器、浏览器、压缩软件、开发工具都会使用 common dialog。
- 应用名出现不等于恶意；必须结合目录、文件名、用户角色和时间线。

## Collection

=== "PowerShell"

    ```powershell
    Get-ItemProperty "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\LastVisitedPidlMRU" -ErrorAction SilentlyContinue
    ```

=== "reg.exe"

    ```cmd
    reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\LastVisitedPidlMRU"
    ```

=== "Offline"

    ```text
    Collect NTUSER.DAT and parse LastVisitedPidlMRU with a PIDL-aware parser.
    ```

## Parsing Tools

- Registry Explorer
- RECmd
- ShellBags Explorer for shell item context
- RegRipper
- KAPE
- Velociraptor

## Cross Validation

- OpenSavePidlMRU
- RecentDocs
- LNK
- Jump Lists
- ShellBags
- UserAssist
- `$MFT`
- EDR process and file telemetry

## Example Findings

- LastVisitedPidlMRU associates `winrar.exe` with `\\10.10.4.20\share`; this supports that the user context had a file dialog relationship between WinRAR and that share, but not that compression or exfiltration succeeded.
- LastVisitedPidlMRU shows `notepad.exe` visiting `C:\Users\Public\Scripts`, while OpenSavePidlMRU contains `payload.ps1`; together they support focused review of script editing activity in that user profile.

## References

- [artefacts.help: LastVisitedPidlMRU](https://artefacts.help/windows_registry_lastvisitedpidlmru.html)
- [Eric Zimmerman tools](https://ericzimmerman.github.io/)

## Related Pages

- 场景：[Shell / Explorer 用户行为](../../questions/shell-explorer.md)
- 注册表位置：[HKEY_CURRENT_USER](../../registry-tree/hkey-current-user.md), [HKCU Explorer](../../registry-tree/hkcu/explorer.md)
