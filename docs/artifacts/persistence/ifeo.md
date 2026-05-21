---
tags:
  - Persistence
  - IFEO
  - Hijacking
---

# Image File Execution Options

此页保留 IFEO artifact 的补充细节。主入口请先查看注册表位置页和取证场景页。

## 对应注册表位置

| 位置 | 说明 |
|---|---|
| [HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options](../../registry-tree/hklm/software/microsoft/windows-nt/currentversion/ifeo.md) | 按映像名生效的调试、兼容性和启动相关配置。 |

## 字段语义

| Value / 子键 | 类型 | 含义 |
|---|---|---|
| `<ImageName>` | Key | 目标可执行文件名，例如 `notepad.exe`。 |
| `Debugger` | `REG_SZ` | 目标进程启动时调用的调试器命令。 |
| `GlobalFlag` | `REG_DWORD` | 调试 / 诊断标志。 |
| `SilentProcessExit` | Key | 进程退出监控相关配置。 |

## 采集与工具

```powershell
Get-ChildItem "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options" |
  ForEach-Object {
    $p = Get-ItemProperty $_.PsPath -ErrorAction SilentlyContinue
    if ($p.Debugger) { [pscustomobject]@{Image=$_.PSChildName; Debugger=$p.Debugger} }
  }
```

- Autoruns / Autorunsc：查看 IFEO 和调试器配置。
- Registry Explorer / RECmd：离线查看 SOFTWARE hive。
- KAPE / Velociraptor：跨主机枚举 `Debugger` 和相关键。

## 常见误读

- IFEO key 存在不等于目标程序已启动。
- `Debugger` 指向命令不等于命令成功执行。
- 开发工具、调试器、兼容性工具和 EDR 可能合法使用 IFEO。

## 交叉验证

- Sysmon Event ID 13、Security 4657、EDR registry telemetry。
- 目标程序启动记录、调试器进程创建、命令行和父子进程关系。
- 调试器二进制路径、签名、哈希和文件系统时间线。

## 相关场景

- [自启动与持久化](../../questions/persistence.md)
- [程序执行痕迹](../../questions/execution.md)
- [常规注册表检查](../../questions/registry-checklist.md)

## 参考资料

- [MITRE ATT&CK: Image File Execution Options Injection](https://attack.mitre.org/techniques/T1546/012/)
- [Microsoft Sysinternals: Autoruns](https://learn.microsoft.com/en-us/sysinternals/downloads/autoruns)
