---
tags:
  - UserActivity
  - ComDlg32
  - NTUSER.DAT
---

# OpenSavePidlMRU

<div class="rfh-meta" markdown>
<span class="rfh-badge high">取证价值 高</span>
<span class="rfh-badge low">检测价值 低</span>
<span class="rfh-badge">文件对话框路径线索</span>
</div>

## 摘要

OpenSavePidlMRU 记录 common file dialog 中打开或保存过的文件/路径 MRU，可恢复用户通过文件对话框接触过的位置，但 PIDL 解析需要工具支持。

## 注册表路径

| View | Hive / File | Path | Scope |
|---|---|---|---|
| Live path | `HKCU` | `Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePidlMRU` | 当前用户 |
| Live path | `HKCU` | `Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePidlMRU\*` | 所有扩展名分组 |
| Offline hive path | `NTUSER.DAT` | `Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePidlMRU` | 用户 SID |

## 原生注册表视图

在 `regedit.exe` 中展开 `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePidlMRU`。子键可按扩展名分组，也可能有 `*` 分组。

## 离线位置

`C:\Users\<user>\NTUSER.DAT`。该 artifact 是用户级 Shell / common dialog 痕迹，离线分析必须记录 SID 和 profile 映射。

## 字段含义

| Field | Meaning |
|---|---|
| 扩展名子键 | 按文件扩展名或 `*` 汇总的打开/保存 MRU |
| numbered values | PIDL / shell item 二进制数据，工具可解析为路径、文件名或 shell namespace |
| `MRUListEx` | 最近使用顺序 |
| key LastWrite | 该扩展名 MRU 子键最近变化时间 |

## 取证含义

OpenSavePidlMRU 适合还原用户在应用打开/保存文件对话框中浏览或选择过的位置。它可以补足 RecentDocs 不含完整路径的弱点，也能把应用、扩展名、目录和文件系统时间线连接起来。

## 可以证明

- 某个用户 profile 中存在文件对话框 MRU 记录。
- PIDL 解析可恢复路径、文件名、卷、网络位置或 shell namespace。
- `MRUListEx` 可辅助判断相对最近顺序。

## 不能证明

- 文件内容被读取或保存成功。
- 应用执行了实际打开/写入操作。
- 解析出的路径当前仍存在。
- key LastWrite 是单个文件操作时间。

## 时间戳说明

OpenSavePidlMRU 的时间语义以 key LastWrite 和 MRU 顺序为主。PIDL 内部可能包含 shell item 时间字段，但语义依对象类型和 parser，报告时应标注工具并保持保守。

## 系统版本差异

Windows 7/10/11 常见该路径。不同 common dialog 版本、应用框架、UWP/现代应用和禁用最近项目设置可能影响覆盖范围。PIDL 结构解析差异待验证时应写明工具版本。

## 攻击滥用

攻击者打开、保存或上传文件时，common dialog 可能留下目标目录和文件名。清理 Explorer MRU 或最近项目会削弱但不一定完全删除相关痕迹。

## 检测思路

- PIDL 解析路径指向敏感目录、可移动卷、SMB 共享或攻击工具工作目录。
- OpenSavePidlMRU 与 LastVisitedPidlMRU 显示某应用访问敏感目录。
- 文件对话框记录与浏览器上传、压缩、加密或外传工具执行时间接近。

## 常见误报

- 正常办公应用、浏览器上传下载、压缩工具、编辑器、邮件客户端会频繁更新。
- 文件预览、另存为和打开对话框都可能产生记录，但不一定完成最终操作。

## 采集方式

=== "PowerShell"

    ```powershell
    Get-ChildItem "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePidlMRU" -Recurse -ErrorAction SilentlyContinue
    ```

=== "reg.exe"

    ```cmd
    reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePidlMRU" /s
    ```

=== "Offline"

    ```text
    Collect NTUSER.DAT and parse ComDlg32\OpenSavePidlMRU with a tool that decodes PIDL / shell items.
    ```

## 解析工具

- Registry Explorer
- RECmd
- ShellBags Explorer for shell item context
- RegRipper
- KAPE
- Velociraptor

## 交叉验证

- LastVisitedPidlMRU
- RecentDocs
- LNK
- Jump Lists
- ShellBags
- `$MFT`
- `$UsnJrnl`
- Browser upload/download history

## 示例结论

- OpenSavePidlMRU `.zip` for user SID `S-1-5-21-...-1001` parses to `E:\HR\payroll.zip`; this supports that a file dialog in that user context referenced the archive, but not that the file was opened or exfiltrated.
- OpenSavePidlMRU and LastVisitedPidlMRU both associate `excel.exe` activity with `\\fileserver\Finance`; with Jump List entries, this strengthens the finding that the user interacted with finance documents through Office.

## 参考资料

- [artefacts.help: OpenSavePidlMRU](https://artefacts.help/windows_registry_opensavepidlmru.html)
- [Eric Zimmerman tools](https://ericzimmerman.github.io/)

## 相关页面

- 场景：[Shell / Explorer 用户行为](../../questions/shell-explorer.md)
- 注册表位置：[HKEY_CURRENT_USER](../../registry-tree/hkey-current-user.md), [HKCU Explorer](../../registry-tree/hkcu/explorer.md)
