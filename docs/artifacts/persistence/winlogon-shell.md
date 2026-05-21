---
tags:
  - Persistence
  - Autoruns
  - Winlogon
  - HKLM
  - HKCU
---

# Winlogon\Shell

此页保留 `Winlogon\Shell` artifact 的补充细节。主入口请先查看注册表位置页和取证场景页。

## 对应注册表位置

| 位置 | 说明 |
|---|---|
| [HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon](../../registry-tree/hklm/software/microsoft/windows-nt/currentversion/winlogon.md) | 机器级登录 Shell 配置。 |
| `HKCU\Software\Microsoft\Windows NT\CurrentVersion\Winlogon` | 用户级 Shell 配置；离线位于对应用户 `NTUSER.DAT`。 |

## 字段语义

| Value | 类型 | 含义 |
|---|---|---|
| `Shell` | `REG_SZ` | 登录后启动的 Shell。 |
| 默认常见数据 | 字符串 | `explorer.exe`。 |

## 采集与工具

```cmd
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Shell
reg query "HKCU\Software\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Shell
```

- Autoruns / Autorunsc：查看 Winlogon Shell。
- Registry Explorer / RECmd：离线查看 SOFTWARE 和各用户 `NTUSER.DAT`。
- Velociraptor：跨主机搜索非默认 Shell。

## 常见误读

- `Shell` 非默认不必然恶意；kiosk、VDI、Shell Launcher 和设备管理软件可能合法修改。
- 配置存在不等于 Shell 已启动。
- 用户级 Shell 需要先映射 SID，不能只写 `HKCU`。

## 交叉验证

- Security 4624 登录事件、Shell 进程创建、Explorer Prefetch。
- Sysmon Event ID 13、Security 4657、EDR registry telemetry。
- Kiosk / VDI / MDM / GPO 基线。

## 相关场景

- [自启动与持久化](../../questions/persistence.md)
- [账户与安全](../../questions/accounts-security.md)
- [常规注册表检查](../../questions/registry-checklist.md)

## 参考资料

- [MITRE ATT&CK: Winlogon Helper DLL](https://attack.mitre.org/techniques/T1547/004/)
- [Microsoft Learn: Shell Launcher](https://learn.microsoft.com/en-us/windows/configuration/shell-launcher/)
