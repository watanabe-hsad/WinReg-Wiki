---
tags:
  - Persistence
  - Explorer
  - Shell
  - COM
  - SOFTWARE
  - HKLM
---

# ShellServiceObjectDelayLoad

<div class="rfh-meta" markdown>
<span class="rfh-badge high">取证价值 高</span>
<span class="rfh-badge medium">检测价值 中</span>
<span class="rfh-badge">Explorer COM 加载</span>
</div>

## 摘要

`ShellServiceObjectDelayLoad` 通过 Explorer Shell 加载指定 COM 对象，异常 CLSID 可用于登录后持久化或 Shell 扩展加载。

## 注册表路径

| 视图 | Hive / 文件 | 路径 | Value | 范围 |
|---|---|---|---|---|
| Live path | `HKLM\SOFTWARE` | `Microsoft\Windows\CurrentVersion\ShellServiceObjectDelayLoad` | `<Name>` | 机器级 |
| Live path | `HKCR` | `CLSID\{GUID}\InprocServer32` | `(Default)` | 合并视图 |
| Offline hive path | `SOFTWARE` | `Microsoft\Windows\CurrentVersion\ShellServiceObjectDelayLoad` | `<Name>` | 机器级 |
| Offline hive path | `SOFTWARE` | `Classes\CLSID\{GUID}\InprocServer32` | `(Default)` | 机器级 COM 注册 |

## 原生注册表视图

在 `regedit.exe` 中查看 `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\ShellServiceObjectDelayLoad`，再用 value 中的 CLSID 到 `HKCR\CLSID\{GUID}` 或 `HKLM\SOFTWARE\Classes\CLSID\{GUID}` 解析 DLL。

## 离线位置

离线文件主要是 `C:\Windows\System32\Config\SOFTWARE`。注意 `HKCR` 是 `HKLM\Software\Classes` 和 `HKCU\Software\Classes` 的合并视图，离线分析不要把 HKCR 当作单独 hive。

## 字段含义

| 字段 | 含义 |
|---|---|
| `<Name>` | Shell service object 名称，可被伪装成系统组件。 |
| value data | CLSID，例如 `{GUID}`。 |
| `CLSID\{GUID}\InprocServer32\(Default)` | COM DLL 路径。 |
| `ThreadingModel` | COM 线程模型，辅助判断注册完整性。 |

## 取证含义

该位置证明 Explorer Shell 配置了延迟加载的 COM 对象。调查重点不是 value 名本身，而是 CLSID 解析到的 DLL 路径、签名、时间线和是否符合系统基线。

## 可以证明

- 系统配置了特定 Shell service object。
- 可解析出对应 CLSID 和 COM DLL 路径。
- 异常对象具备 Explorer 登录会话加载潜力。

## 不能证明

- 不能单独证明 DLL 已被 Explorer 加载。
- 不能只凭 CLSID 判断恶意。
- 不能忽略 HKCU `Software\Classes` 对 COM 解析的可能影响。

## 时间戳说明

`ShellServiceObjectDelayLoad` key LastWrite 和 CLSID key LastWrite 分别反映各自 key 最近变化。DLL 创建/修改时间与实际加载时间需要单独验证。

## 系统版本差异

该位置在旧版 Windows 和部分兼容环境中更常见。Windows 10 / 11 上是否存在、默认项和加载行为需按系统基线验证；未知项应先解析 COM 注册和签名。

## 攻击滥用

攻击者可注册恶意 COM DLL，并在 `ShellServiceObjectDelayLoad` 中指向该 CLSID，使 Explorer 触发加载。该方式通常依赖管理员权限或可写 COM 注册位置。

## 检测思路

- 新增或修改 `ShellServiceObjectDelayLoad` value。
- CLSID 的 `InprocServer32` 指向用户可写目录、临时目录或无签名 DLL。
- Explorer 启动后加载非基线 DLL。
- 关联 Sysmon 13 registry set、Sysmon 7 image loaded 和 DLL 文件创建。

## 常见误报

- 旧版 Shell 扩展、同步盘、压缩软件、云盘、DLP、输入法和企业桌面组件。
- 系统升级或软件卸载后可能残留 CLSID。
- COM 注册存在但目标 DLL 已不存在。

## 采集方式

=== "PowerShell"

    ```powershell
    Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\ShellServiceObjectDelayLoad"
    ```

=== "reg.exe"

    ```cmd
    reg query "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\ShellServiceObjectDelayLoad" /s
    reg query "HKLM\SOFTWARE\Classes\CLSID" /s
    ```

=== "Offline"

    ```text
    Collect SOFTWARE and relevant user UsrClass.dat / NTUSER.DAT if HKCU Classes override is suspected.
    ```

## 解析工具

- Autoruns / Autorunsc
- Registry Explorer
- RECmd
- KAPE
- Velociraptor

## 交叉验证

- Explorer 进程模块加载、Sysmon Event ID 7。
- COM CLSID 注册、DLL 文件签名和哈希。
- Sysmon Event ID 13、Security 4657。
- UserAssist、ShellBags、登录事件和文件系统时间线。

## 示例结论

- `ShellServiceObjectDelayLoad` 新增 `UpdateHelper={GUID}`，该 CLSID 的 `InprocServer32` 指向 `%AppData%\helper.dll`；该证据可证明 Explorer Shell 加载链被配置为包含非基线 COM 对象。
- 目标 DLL 已缺失且无模块加载证据，因此当前只能证明配置残留，不能证明最近一次登录时成功加载。

## 参考资料

- [Microsoft Sysinternals: Autoruns](https://learn.microsoft.com/en-us/sysinternals/downloads/autoruns)
- [MITRE ATT&CK: Boot or Logon Autostart Execution](https://attack.mitre.org/techniques/T1547/)

## 相关页面

- 场景：[自启动与持久化](../../questions/persistence.md)、[Shell / Explorer 用户行为](../../questions/shell-explorer.md)
- 注册表位置：[HKLM\SOFTWARE\...\ShellServiceObjectDelayLoad](../../registry-tree/hklm/software/shellserviceobjectdelayload.md)

