---
tags:
  - Persistence
  - Autoruns
  - HKCU
  - HKLM
---

# Command Processor\AutoRun

此页保留 `Command Processor\AutoRun` 的补充细节。主入口请先查看注册表位置页和取证场景页。

## 对应注册表位置

| 范围 | 位置 | 说明 |
|---|---|---|
| 用户级 | [HKCU\Software\Microsoft\Command Processor](../../registry-tree/hkcu/software/microsoft/command-processor.md) | 当前用户 `cmd.exe` 配置。 |
| 机器级 | [HKLM\SOFTWARE](../../registry-tree/hklm/software/index.md) | `HKLM\SOFTWARE\Microsoft\Command Processor`，影响机器级命令处理器配置。 |

## 字段语义

| Value | 类型 | 含义 |
|---|---|---|
| `AutoRun` | `REG_SZ` / `REG_EXPAND_SZ` | `cmd.exe` 启动且未使用 `/D` 时执行的命令。 |
| `CompletionChar` | `REG_DWORD` | 命令补全字符配置。 |
| `DefaultColor` | `REG_DWORD` | 默认控制台颜色。 |
| `EnableExtensions` | `REG_DWORD` | 命令扩展配置。 |

## 采集与工具

```cmd
reg query "HKCU\Software\Microsoft\Command Processor" /v AutoRun
reg query "HKLM\Software\Microsoft\Command Processor" /v AutoRun
```

- Registry Explorer / RECmd：查看 value data 和 key LastWrite。
- KAPE / Velociraptor：跨用户或跨主机枚举非空 `AutoRun`。
- live 系统可用 `cmd /?` 核对 `/D` 对 AutoRun 的影响。

## 常见误读

- `AutoRun` 存在不等于已经触发；需要进程创建日志证明有未加 `/D` 的 `cmd.exe` 启动。
- key LastWrite 是 key 级时间，不是 `AutoRun` value 的精确创建时间。
- 开发环境、终端增强、运维初始化脚本可能设置合法 AutoRun。

## 交叉验证

- Sysmon Event ID 13、Security 4657、EDR registry telemetry。
- Sysmon Event ID 1 / Security 4688：`cmd.exe` 启动后的子进程或命令行。
- PowerShell 日志、脚本日志、网络连接日志、文件系统时间线。

## 相关场景

- [自启动与持久化](../../questions/persistence.md)
- [程序执行痕迹](../../questions/execution.md)
- [反取证与清理痕迹](../../questions/anti-forensics.md)
- [常规注册表检查](../../questions/registry-checklist.md)

## 参考资料

- [Microsoft Learn: cmd](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/cmd)
- [MITRE ATT&CK: Command and Scripting Interpreter: Windows Command Shell](https://attack.mitre.org/techniques/T1059/003/)
