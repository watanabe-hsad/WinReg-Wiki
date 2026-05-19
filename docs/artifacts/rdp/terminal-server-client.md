---
tags:
  - RDP
  - RemoteAccess
  - NTUSER.DAT
---

# Terminal Server Client

<div class="rfh-meta" markdown>
<span class="rfh-badge high">取证价值 高</span>
<span class="rfh-badge medium">检测价值 中</span>
<span class="rfh-badge">客户端连接</span>
</div>

`Terminal Server Client` 记录 MSTSC 客户端连接目标和部分用户提示信息。它更适合回答“这个用户是否从本机连接过某些远程主机”。

## Registry Paths

| Hive | Path | Meaning |
|---|---|---|
| `NTUSER.DAT` | `Software\Microsoft\Terminal Server Client\Default` | MRU 连接目标 |
| `NTUSER.DAT` | `Software\Microsoft\Terminal Server Client\Servers` | 服务器条目和用户名提示 |

## What It Can Prove

- 某用户配置或使用过 MSTSC 连接目标。
- 可发现目标主机名、IP 或用户名提示。

## What It Cannot Prove

- RDP 登录一定成功。
- 目标主机一定被攻陷。
- 当前主机一定作为服务端被远程登录。

## Detection Ideas

- 普通办公终端连接服务器网段。
- 用户连接异常资产或跳板机。
- RDP 目标出现外网 IP 或云主机。
- 时间线与凭据转储、横向移动工具执行接近。

## Collection

```powershell
Get-ItemProperty "HKCU:\Software\Microsoft\Terminal Server Client\Default"
Get-ChildItem "HKCU:\Software\Microsoft\Terminal Server Client\Servers"
```

## Cross Validation

- Security.evtx logon events
- TerminalServices-LocalSessionManager
- TerminalServices-RemoteConnectionManager
- Firewall logs
- Jump Lists
- Credential Manager artifacts

