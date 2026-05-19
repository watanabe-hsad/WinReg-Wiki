---
tags:
  - RDP
  - RemoteAccess
  - SYSTEM
  - HKLM
---

# RDP-Tcp PortNumber

<div class="rfh-meta" markdown>
<span class="rfh-badge high">取证价值 高</span>
<span class="rfh-badge high">检测价值 高</span>
<span class="rfh-badge">RDP 监听端口配置</span>
</div>

## Summary

`WinStations\RDP-Tcp\PortNumber` 记录 RDP 服务端监听端口配置，默认通常为 `3389`，但显示时要注意十六进制和十进制差异。

## Registry Paths

| View | Hive / File | Path | Value | Scope |
|---|---|---|---|---|
| Live path | `HKLM\SYSTEM` | `CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp` | `PortNumber` | 机器级 |
| Offline hive path | `SYSTEM` | `ControlSet00x\Control\Terminal Server\WinStations\RDP-Tcp` | `PortNumber` | 机器级 |

## Native Registry View

在 `regedit.exe` 中展开 `HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp`。`PortNumber` 是 DWORD，Regedit 可按十六进制或十进制显示。

## Offline Location

`C:\Windows\System32\Config\SYSTEM`。离线分析先解析 `SYSTEM\Select`，再读取当前 control set 的 `RDP-Tcp`。

## Data Meaning

| Field | Meaning |
|---|---|
| `PortNumber` | RDP-Tcp listener 端口，默认常见为 decimal `3389` / hex `0x00000d3d` |
| key LastWrite | `RDP-Tcp` 配置 key 最近变化时间，不等于服务监听开始时间 |

## Forensic Meaning

该值可证明 RDP 服务端被配置为使用哪个端口。非默认端口可能是管理员基线、暴露面管理，也可能是攻击者试图绕过简单扫描或安全策略。是否实际监听需用服务状态、网络连接和防火墙验证。

## What It Can Prove

- RDP-Tcp listener 的注册表端口配置。
- 端口是否偏离默认 `3389`。
- RDP 服务端调查应查询哪个端口的网络和防火墙日志。

## What It Cannot Prove

- 端口正在监听。
- 防火墙允许该端口入站。
- 有 RDP 登录或连接尝试。
- 非默认端口一定恶意。

## Timestamp Notes

`RDP-Tcp` key LastWrite 只能提示该 key 变化。`PortNumber` value 无独立时间戳。实际监听时间应结合 `TermService` 重启、系统重启、TerminalServices logs、netstat/EDR 网络 telemetry。

## OS Version Notes

Windows 客户端和 Server 通常使用该路径。远程桌面服务角色、RD Gateway、第三方远控或策略可能改变暴露面。默认端口和字段语义稳定，但生效需要服务重启或系统状态验证。

## Attacker Usage

攻击者可能把 RDP 改到非默认端口以规避粗糙扫描、与防火墙规则配套开放，或临时开启远程访问。也可能将端口改回默认掩盖变更。

## Detection Ideas

- `PortNumber` 被修改为非 `3389`。
- 端口修改后出现防火墙放行、`TermService` 重启或外部连接。
- 非 IT 工具或脚本修改 `WinStations\RDP-Tcp\PortNumber`。
- 监听端口与资产基线不一致。

## False Positives

- 合法安全基线要求更改 RDP 端口。
- 跳板机、实验环境、托管服务和特殊运维策略。
- 迁移、加固脚本或 GPO/MDM 统一下发。

## Collection

=== "PowerShell"

    ```powershell
    Get-ItemProperty "HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" |
      Select-Object PortNumber
    ```

=== "reg.exe"

    ```cmd
    reg query "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v PortNumber
    ```

=== "Offline"

    ```text
    Load SYSTEM, resolve Select\Current, inspect ControlSet00x\Control\Terminal Server\WinStations\RDP-Tcp\PortNumber.
    ```

## Parsing Tools

- Registry Explorer
- RECmd
- KAPE
- Velociraptor
- RegRipper

## Cross Validation

- `fDenyTSConnections`
- Windows Firewall rules
- `TermService` service state
- `netstat` / EDR network telemetry
- TerminalServices logs
- Security.evtx LogonType `10`

## Example Findings

- `PortNumber` is `0x00001389`, which converts to decimal `5001`; this proves RDP-Tcp was configured for port `5001`, but does not prove the port was reachable or used.
- RDP port changed from default, firewall rule opened the same port, and external connection telemetry followed within 10 minutes; together these support RDP exposure change during the incident window.

## References

- [Microsoft Learn: Change the listening port for Remote Desktop](https://learn.microsoft.com/en-us/troubleshoot/windows-server/remote/change-listening-port-remote-desktop)
- [MITRE ATT&CK: Remote Services - RDP](https://attack.mitre.org/techniques/T1021/001/)

## Related Pages

- 场景：[RDP 与远程访问](../../questions/rdp.md)
- 注册表位置：[HKLM\SYSTEM](../../registry-tree/hklm/system.md)
