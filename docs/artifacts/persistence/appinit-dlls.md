---
tags:
  - Persistence
  - AppInit
  - DLL
  - SOFTWARE
  - HKLM
---

# AppInit_DLLs

此页保留 AppInit_DLLs artifact 的补充细节。主入口请先查看注册表位置页和取证场景页。

## 对应注册表位置

| 位置 | 说明 |
|---|---|
| [HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Windows](../../registry-tree/hklm/software/microsoft/windows-nt/currentversion/appinit-dlls.md) | `AppInit_DLLs`、`LoadAppInit_DLLs`、`RequireSignedAppInit_DLLs`。 |
| [WOW6432Node](../../registry-tree/hklm/software/wow6432node.md) | 32 位进程相关重定向视图。 |

## 字段语义

| Value | 类型 | 含义 |
|---|---|---|
| `AppInit_DLLs` | `REG_SZ` / `REG_EXPAND_SZ` | 待加载 DLL 列表或路径。 |
| `LoadAppInit_DLLs` | `REG_DWORD` | AppInit 加载开关。 |
| `RequireSignedAppInit_DLLs` | `REG_DWORD` | 签名要求相关开关，语义随版本变化。 |

## 采集与工具

```cmd
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Windows" /v AppInit_DLLs
reg query "HKLM\SOFTWARE\WOW6432Node\Microsoft\Windows NT\CurrentVersion\Windows" /v AppInit_DLLs
```

- Autoruns / Autorunsc：查看 AppInit DLLs。
- Registry Explorer / RECmd：离线查看 SOFTWARE hive 和 key LastWrite。
- KAPE / Velociraptor：采集 registry、模块加载日志和 DLL 文件。

## 常见误读

- `AppInit_DLLs` 存在不等于 DLL 已被加载。
- 是否加载受 `LoadAppInit_DLLs`、签名要求、Secure Boot、进程类型和 WOW6432Node 影响。
- 旧版安全软件、DLP、输入法、辅助功能和图形工具可能留下合法配置。

## 交叉验证

- Sysmon Event ID 7、EDR module telemetry、进程内存。
- Sysmon Event ID 13、Security 4657、EDR registry telemetry。
- DLL 文件路径、签名、哈希、创建 / 修改时间。

## 相关场景

- [自启动与持久化](../../questions/persistence.md)
- [程序执行痕迹](../../questions/execution.md)
- [常规注册表检查](../../questions/registry-checklist.md)

## 参考资料

- [Microsoft Learn: AppInit DLLs in Windows 7 and Windows Server 2008 R2](https://learn.microsoft.com/en-us/windows/win32/win7appqual/appinit-dlls-in-windows-7-and-windows-server-2008-r2)
- [MITRE ATT&CK: AppInit DLLs](https://attack.mitre.org/techniques/T1546/010/)
- [Microsoft Sysinternals: Autoruns](https://learn.microsoft.com/en-us/sysinternals/downloads/autoruns)
