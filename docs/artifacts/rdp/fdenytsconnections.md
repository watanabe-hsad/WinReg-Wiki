---
tags:
  - RDP
  - RemoteAccess
  - SYSTEM
  - HKLM
---

# fDenyTSConnections

<div class="rfh-meta" markdown>
<span class="rfh-badge high">取证价值 高</span>
<span class="rfh-badge high">检测价值 高</span>
<span class="rfh-badge">RDP 服务端允许状态</span>
</div>

## Summary

`fDenyTSConnections` 表示本机是否拒绝远程桌面连接；`0` 通常表示允许 RDP 连接，`1` 通常表示拒绝，但它不能单独证明发生过 RDP 登录。

## Registry Paths

| View | Hive / File | Path | Value | Scope |
|---|---|---|---|---|
| Live path | `HKLM\SYSTEM` | `CurrentControlSet\Control\Terminal Server` | `fDenyTSConnections` | 机器级 |
| Offline hive path | `SYSTEM` | `ControlSet00x\Control\Terminal Server` | `fDenyTSConnections` | 机器级 |

## Native Registry View

在 `regedit.exe` 中展开 `HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server`。离线时先通过 `HKLM\SYSTEM\Select` 映射当前 `ControlSet00x`。

## Offline Location

`C:\Windows\System32\Config\SYSTEM`。采集时保留 `SYSTEM.LOG1`、`SYSTEM.LOG2`，并记录当前 control set。

## Data Meaning

| Field | Meaning |
|---|---|
| `fDenyTSConnections=1` | 通常表示拒绝远程桌面连接 |
| `fDenyTSConnections=0` | 通常表示允许远程桌面连接 |
| key LastWrite | Terminal Server key 最近变化时间，不等于实际连接时间 |

## Forensic Meaning

该值用于判断 RDP 服务端功能是否处于允许连接状态。它是远程访问调查中的配置证据，不是登录证据。若该值在入侵窗口内由 `1` 变为 `0`，应重点交叉验证防火墙、TerminalServices、Security.evtx 和服务状态。

## What It Can Prove

- 采集时或某个 control set 中存在 RDP 允许/拒绝配置。
- 可辅助证明机器被配置为允许或禁止远程桌面连接。
- key LastWrite 可提示 Terminal Server 配置区域最近变化。

## What It Cannot Prove

- RDP 登录发生过。
- RDP 服务正在监听或防火墙已放行。
- 具体是谁修改了配置。
- RDP 连接成功、失败或持续时长。

## Timestamp Notes

`Terminal Server` key LastWrite 可能由多个 value 或子键变化触发，不能直接视为 `fDenyTSConnections` 修改时间。应结合 Sysmon Event ID 13、Security 4657、Group Policy、Remote Desktop Services logs 或 EDR registry telemetry。

## OS Version Notes

Windows 7/10/11/Server 都常见该配置，但策略、GPO、MDM、服务器角色和远程管理工具会影响实际状态。Server Core 和企业基线行为需按环境验证。

## Attacker Usage

攻击者可通过注册表、PowerShell、`SystemPropertiesRemote.exe`、WMI 或组策略开启 RDP，以便交互式登录或横向移动。也可能临时开启后再关闭以减少暴露。

## Detection Ideas

- `fDenyTSConnections` 从 `1` 改为 `0`。
- RDP 开启后短时间内新增防火墙规则、`TermService` 启动、`4624 LogonType 10` 或外部网络连接。
- 非 IT 管理工具写入 `Control\Terminal Server\fDenyTSConnections`。

## False Positives

- IT 运维开启远程桌面、服务器部署、GPO/MDM 策略、远程支持工具、实验室配置。

## Collection

=== "PowerShell"

    ```powershell
    Get-ItemProperty "HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server" |
      Select-Object fDenyTSConnections
    ```

=== "reg.exe"

    ```cmd
    reg query "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections
    ```

=== "Offline"

    ```text
    Load SYSTEM, resolve Select\Current, inspect ControlSet00x\Control\Terminal Server\fDenyTSConnections.
    ```

## Parsing Tools

- Registry Explorer
- RECmd
- KAPE
- Velociraptor
- RegRipper

## Cross Validation

- Security.evtx `4624` LogonType `10`, `4778`, `4779`
- TerminalServices-RemoteConnectionManager
- TerminalServices-LocalSessionManager
- Windows Firewall rules and logs
- `TermService` service state
- Network telemetry for TCP 3389 or configured RDP port

## Example Findings

- `fDenyTSConnections=0` in the current control set proves RDP was configured to allow connections at collection time; no conclusion about successful RDP logon should be made without Security.evtx or TerminalServices evidence.
- Sysmon Event ID 13 shows `fDenyTSConnections` changed to `0` at `2026-05-18 03:14 UTC`, followed by firewall rule changes and `4624` LogonType `10`; together these support an RDP enablement and login timeline.

## References

- [Microsoft Learn: Enable Remote Desktop using Settings or PowerShell](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/clients/remote-desktop-allow-access)
- [MITRE ATT&CK: Remote Services - RDP](https://attack.mitre.org/techniques/T1021/001/)

## Related Pages

- 场景：[RDP 与远程访问](../../questions/rdp.md)
- 注册表位置：[HKLM\SYSTEM](../../registry-tree/hklm/system.md)
