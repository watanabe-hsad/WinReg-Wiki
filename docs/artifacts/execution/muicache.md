---
tags:
  - Execution
  - ProgramPresence
  - NTUSER.DAT
  - UsrClass.dat
  - HKCU
---

# MUICache

<div class="rfh-meta" markdown>
<span class="rfh-badge medium">取证价值 中</span>
<span class="rfh-badge low">检测价值 低</span>
<span class="rfh-badge">程序存在 / Shell 显示线索</span>
</div>

## 摘要

MUICache 记录 Windows Shell 为程序显示名称缓存的路径与字符串，可辅助证明某个用户环境中出现过某个程序路径，但不能单独证明程序执行。

## 注册表路径

| View | Hive / File | Path | Scope |
|---|---|---|---|
| Live path | `HKCU` | `Software\Classes\Local Settings\Software\Microsoft\Windows\Shell\MuiCache` | 当前用户 |
| Live path | `HKU\<SID>_Classes` | `Local Settings\Software\Microsoft\Windows\Shell\MuiCache` | 指定 SID |
| Offline hive path | `UsrClass.dat` | `Local Settings\Software\Microsoft\Windows\Shell\MuiCache` | 用户 Classes hive |
| Legacy / variant | `NTUSER.DAT` | `Software\Microsoft\Windows\ShellNoRoam\MUICache` | 老版本常见，需按 OS 验证 |

## 原生注册表视图

在 live 系统中常见于 `HKCU\Software\Classes\Local Settings\Software\Microsoft\Windows\Shell\MuiCache`。由于 `HKCU\Software\Classes` 参与 `HKCR` 合并视图，离线时应优先定位目标用户的 `UsrClass.dat` 或 `HKU\<SID>_Classes`。

## 离线位置

主要对应 `C:\Users\<user>\AppData\Local\Microsoft\Windows\UsrClass.dat`。部分旧系统或历史路径可能位于用户 `NTUSER.DAT`。分析前先用 [ProfileList](../security/profilelist.md) 确认 SID 到 profile 的映射。

## 字段含义

| Field | Meaning |
|---|---|
| value name | 通常包含程序路径或资源引用，可能带 `FriendlyAppName` 等后缀 |
| value data | Shell 缓存的显示字符串，例如程序名、描述、资源名称 |
| key LastWrite | MuiCache 容器最近变化时间，不能直接等同某个 value 的首次出现 |

## 取证含义

MUICache 更适合证明“该用户 Shell 环境曾缓存过这个程序路径或显示名”。它常用于辅助定位程序存在、用户环境接触过某路径、或解释图形界面中显示的程序名。它的证据强度通常低于 Prefetch、UserAssist、BAM、进程日志。

## 可以证明

- 目标用户的 user hive 中存在某程序路径或显示名缓存。
- 程序路径、名称或资源字符串可用于线索扩展和时间线定位。
- 可辅助证明程序曾被 Shell 解析、展示或接触过。

## 不能证明

- 不能单独证明程序执行。
- 不能证明用户主动打开程序。
- 不能证明文件当前仍存在。
- 不能把显示字符串当成可信软件身份；它可能来自文件资源或被伪造。

## 时间戳说明

MUICache value 通常没有独立时间戳。key LastWrite 表示 MuiCache key 最近变化，可能由任意 value 新增、修改或删除触发。若工具输出“首次出现”或“最后出现”，应确认它是工具推断、hive 历史解析还是 key LastWrite。

## 系统版本差异

Windows 7、Windows 10、Windows 11 的 MUICache 路径和 value 命名存在差异。老系统常见 `ShellNoRoam\MUICache`，新系统常见 `UsrClass.dat` 下的 `Local Settings\Software\Microsoft\Windows\Shell\MuiCache`。Server 版本和禁用 Explorer 的系统上覆盖范围需待验证。

## 攻击滥用

攻击者通常不会依赖 MUICache 持久化，但可通过改写文件版本资源、伪装产品名或把工具命名为系统组件来污染显示信息。清理时可能删除 MuiCache key 或相关 value 以降低程序路径暴露。

## 检测思路

- 将 MUICache 作为低置信线索源，批量搜索已知恶意工具名、罕见路径和用户可写目录。
- 关注 value name 中的 `%Temp%`、`Downloads`、压缩包释放目录、远程同步目录。
- 与高置信执行源命中同一路径时提升评分，而不是仅凭 MUICache 告警。

## 常见误报

- 用户浏览目录、文件属性读取、应用安装卸载、开始菜单和 Shell 预览可能产生缓存。
- 合法便携软件、开发工具和内部工具常出现在用户可写目录。
- 显示名可能来自合法软件资源，不能只看名称相似度。

## 采集方式

=== "PowerShell"

    ```powershell
    Get-ItemProperty "HKCU:\Software\Classes\Local Settings\Software\Microsoft\Windows\Shell\MuiCache" -ErrorAction SilentlyContinue
    ```

=== "reg.exe"

    ```cmd
    reg query "HKCU\Software\Classes\Local Settings\Software\Microsoft\Windows\Shell\MuiCache"
    ```

=== "Offline"

    ```text
    Collect C:\Users\<user>\AppData\Local\Microsoft\Windows\UsrClass.dat and logs.
    Also check C:\Users\<user>\NTUSER.DAT for legacy MUICache paths.
    ```

## 解析工具

- Registry Explorer：适合人工检查 `UsrClass.dat` 与 value data。
- RECmd：适合批量导出用户 hive 的 MuiCache 相关路径。
- RegRipper：可用插件解析，覆盖范围取决于版本。
- KAPE：适合收集所有用户 `NTUSER.DAT`、`UsrClass.dat`。
- Velociraptor：适合跨主机按路径搜索 value name。

## 交叉验证

- Prefetch、BAM/DAM、UserAssist、Amcache、ShimCache。
- LNK、Jump Lists、RecentDocs、ShellBags。
- 文件系统 `$MFT`、`$UsnJrnl`、签名、哈希和下载来源。
- Sysmon Event ID 1、Security 4688、EDR process telemetry。

## 示例结论

- `UsrClass.dat` 中 MUICache 出现 `C:\Users\bob\Downloads\AnyDesk.exe.FriendlyAppName`，说明 bob 的 Shell 环境缓存过该路径和显示名；该记录不能单独证明 AnyDesk 执行，需结合 Prefetch 或进程日志。
- MUICache、BAM 和 Amcache 同时指向 `C:\Users\bob\AppData\Roaming\svhost.exe`，且文件资源显示名伪装为 `Windows Host Process`，可作为用户级可疑程序存在与执行链的交叉证据。

## 相关页面

- 场景：[程序执行](../../questions/execution.md)、[Shell / Explorer 用户行为](../../questions/shell-explorer.md)
- 注册表位置：[HKEY_CLASSES_ROOT](../../registry-tree/hkcr/index.md)、[UsrClass.dat](../../registry-tree/hku/usrclass.md)

## 参考资料

- [artefacts.help: MUICache](https://artefacts.help/windows_registry_muicache.html)
- [Eric Zimmerman tools](https://ericzimmerman.github.io/)
