---
tags:
  - Persistence
  - Autoruns
  - Winlogon
  - HKLM
---

# Winlogon\Userinit

此页保留 `Winlogon\Userinit` artifact 的补充细节。主入口请先查看注册表位置页和取证场景页。

## 对应注册表位置

| 位置 | 说明 |
|---|---|
| [HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon](../../registry-tree/hklm/software/microsoft/windows-nt/currentversion/winlogon.md) | 登录初始化程序、Shell、自动登录和特殊账户显示控制。 |

## 字段语义

| Value | 类型 | 含义 |
|---|---|---|
| `Userinit` | `REG_SZ` | 登录后执行的用户初始化程序列表。 |
| 默认常见数据 | 字符串 | `C:\Windows\system32\userinit.exe,` 或等价路径形式。 |

## 采集与工具

```cmd
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Userinit
```

- Autoruns / Autorunsc：查看 Winlogon autoruns。
- Registry Explorer / RECmd：离线查看 SOFTWARE hive 和 key LastWrite。
- KAPE / Velociraptor：采集 Winlogon 配置、登录事件和进程证据。

## 常见误读

- `Userinit` 配置存在不等于追加命令已经执行。
- key LastWrite 不是 `Userinit` value 的精确创建时间。
- Kiosk、VDI、Shell 替换、登录加固或企业管理软件可能合法修改登录链。

## 交叉验证

- Sysmon Event ID 13、Security 4657、EDR registry telemetry。
- Security 4624 / 4634 登录时间线。
- 追加程序的 Prefetch、Amcache、BAM / DAM、文件签名和文件系统时间线。

## 相关场景

- [自启动与持久化](../../questions/persistence.md)
- [账户与安全](../../questions/accounts-security.md)
- [常规注册表检查](../../questions/registry-checklist.md)

## 参考资料

- [MITRE ATT&CK: Winlogon Helper DLL](https://attack.mitre.org/techniques/T1547/004/)
- [Microsoft Learn: Winlogon and credential providers](https://learn.microsoft.com/en-us/windows/win32/secauthn/winlogon-and-credential-providers)
