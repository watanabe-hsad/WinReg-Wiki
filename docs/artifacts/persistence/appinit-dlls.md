---
tags:
  - Persistence
  - AppInit
  - DLL
  - SOFTWARE
  - HKLM
---

# AppInit_DLLs

<div class="rfh-meta" markdown>
<span class="rfh-badge high">取证价值 高</span>
<span class="rfh-badge high">检测价值 高</span>
<span class="rfh-badge">DLL 加载链</span>
</div>

## 摘要

`AppInit_DLLs` 可让加载 `User32.dll` 的进程额外加载指定 DLL，是旧式但仍需排查的用户态持久化和注入入口。

## 注册表路径

| 视图 | Hive / 文件 | 路径 | Value | 范围 |
|---|---|---|---|---|
| Live path | `HKLM\SOFTWARE` | `Microsoft\Windows NT\CurrentVersion\Windows` | `AppInit_DLLs` | 机器级 |
| Live path | `HKLM\SOFTWARE` | `Microsoft\Windows NT\CurrentVersion\Windows` | `LoadAppInit_DLLs` | 机器级 |
| Live path | `HKLM\SOFTWARE` | `Microsoft\Windows NT\CurrentVersion\Windows` | `RequireSignedAppInit_DLLs` | 机器级 |
| Live path | `HKLM\SOFTWARE\WOW6432Node` | `Microsoft\Windows NT\CurrentVersion\Windows` | 同上 | 32 位视图 |
| Offline hive path | `SOFTWARE` | `Microsoft\Windows NT\CurrentVersion\Windows` | 同上 | 机器级 |

## 原生注册表视图

在 `regedit.exe` 中展开 `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Windows`。64 位系统上还应检查 `HKLM\SOFTWARE\WOW6432Node\Microsoft\Windows NT\CurrentVersion\Windows`，因为 32 位进程可能读取重定向视图。

## 离线位置

离线文件为 `C:\Windows\System32\Config\SOFTWARE`。若分析 32 位重定向配置，仍在同一 SOFTWARE hive 内查看 `WOW6432Node`。

## 字段含义

| 字段 | 含义 |
|---|---|
| `AppInit_DLLs` | 待加载 DLL 列表或路径。 |
| `LoadAppInit_DLLs` | `REG_DWORD`，常见为 `1` 时启用加载，`0` 时禁用。 |
| `RequireSignedAppInit_DLLs` | `REG_DWORD`，要求签名 DLL 的策略开关，默认和版本有关。 |
| key LastWrite | 该 key 最近更新，不等同某个 DLL 首次加载时间。 |

## 取证含义

该位置可证明系统配置了 AppInit DLL 加载链。只有在 `LoadAppInit_DLLs` 启用、目标进程加载 `User32.dll` 且系统策略允许时，列表中的 DLL 才可能被加载。它适合和模块加载、文件签名和进程创建日志交叉验证。

## 可以证明

- 系统是否配置了 AppInit DLL 列表。
- AppInit 加载是否在配置层面被启用。
- 是否存在非基线 DLL、用户可写路径或无签名组件。

## 不能证明

- 不能单独证明 DLL 已被某进程加载。
- 不能单独证明 DLL 已执行恶意逻辑。
- 不能忽略 `LoadAppInit_DLLs`、签名要求、Secure Boot 和 WOW6432Node 差异。

## 时间戳说明

`Windows` key LastWrite 可能由多个 value 变化触发。DLL 实际加载时间应通过 Sysmon Event ID 7、EDR module telemetry、进程内存或文件访问证据确认。

## 系统版本差异

Windows 7 / Server 2008 R2 引入更严格的签名要求控制。Windows 8 及以后 AppInit_DLLs 默认行为和 Secure Boot 影响需按版本验证。未知环境中不要仅凭 value 存在判断必然生效。

## 攻击滥用

攻击者可写入恶意 DLL 路径并启用 `LoadAppInit_DLLs`，让 GUI 进程加载 DLL。该方式通常需要管理员权限，且容易受签名策略和安全产品拦截。

## 检测思路

- `LoadAppInit_DLLs` 从 `0` 变为 `1`。
- `AppInit_DLLs` 包含用户可写目录、UNC 路径、临时目录或异常 DLL。
- `RequireSignedAppInit_DLLs` 被降低，且同时出现新 DLL。
- 监控 registry set：`\Microsoft\Windows NT\CurrentVersion\Windows\AppInit_DLLs`。
- 关联 DLL 文件创建、签名、Sysmon 7 和进程启动。

## 常见误报

- 旧版安全软件、DLP、输入法、辅助功能、图形增强工具可能使用 AppInit。
- 老旧业务系统可能保留配置但未启用。
- 32 位和 64 位视图不一致可能造成误判。

## 采集方式

=== "PowerShell"

    ```powershell
    Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Windows" |
      Select-Object AppInit_DLLs, LoadAppInit_DLLs, RequireSignedAppInit_DLLs
    ```

=== "reg.exe"

    ```cmd
    reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Windows" /v AppInit_DLLs
    reg query "HKLM\SOFTWARE\WOW6432Node\Microsoft\Windows NT\CurrentVersion\Windows" /v AppInit_DLLs
    ```

=== "Offline"

    ```text
    Collect SOFTWARE hive and inspect both native and WOW6432Node Windows keys.
    ```

## 解析工具

- Autoruns / Autorunsc
- Registry Explorer
- RECmd
- KAPE
- Velociraptor

## 交叉验证

- Sysmon Event ID 7、EDR module telemetry。
- DLL 文件路径、签名、哈希、创建/修改时间。
- Sysmon Event ID 13 或 Security 4657 registry set。
- Prefetch、Amcache、进程树和内存取证。

## 示例结论

- `AppInit_DLLs` 包含 `C:\Users\Public\lib.dll` 且 `LoadAppInit_DLLs=1`，可证明系统配置了 AppInit DLL 加载链；是否已加载需结合模块加载或内存证据确认。
- `RequireSignedAppInit_DLLs` 被设置为 `0` 并与异常 DLL 写入时间接近，说明 AppInit 策略被调整为更容易加载未签名 DLL。

## 参考资料

- [Microsoft Learn: AppInit DLLs in Windows 7 and Windows Server 2008 R2](https://learn.microsoft.com/en-us/windows/win32/win7appqual/appinit-dlls-in-windows-7-and-windows-server-2008-r2)
- [MITRE ATT&CK: AppInit DLLs](https://attack.mitre.org/techniques/T1546/010/)
- [Microsoft Sysinternals: Autoruns](https://learn.microsoft.com/en-us/sysinternals/downloads/autoruns)

## 相关页面

- 场景：[自启动与持久化](../../questions/persistence.md)
- 注册表位置：[HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Windows](../../registry-tree/hklm/software/appinit-dlls.md)

