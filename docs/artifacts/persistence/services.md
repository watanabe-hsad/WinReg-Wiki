---
tags:
  - Persistence
  - Services
  - SYSTEM
---

# Services

<div class="rfh-meta" markdown>
<span class="rfh-badge high">取证价值 高</span>
<span class="rfh-badge high">检测价值 高</span>
<span class="rfh-badge">系统级</span>
</div>

Windows 服务和驱动配置位于 `SYSTEM` hive，是高权限持久化和横向移动后落地的常见位置。

## Registry Paths

| Hive | Path |
|---|---|
| `HKLM\SYSTEM` | `ControlSet00x\Services\<ServiceName>` |

## Forensic Meaning

每个子键代表一个服务或驱动。关键 value 包括：

| Value | 含义 |
|---|---|
| `ImagePath` | 服务二进制或命令 |
| `Start` | 启动类型 |
| `Type` | 服务或驱动类型 |
| `DisplayName` | 显示名称 |
| `ObjectName` | 运行账户 |

## What It Can Prove

- 系统中配置过某个服务或驱动。
- 服务二进制路径、启动类型和运行账户。
- key LastWrite 可提示服务配置变化时间。

## What It Cannot Prove

- 服务一定成功启动。
- `ImagePath` 指向的文件仍然存在。
- 服务名称可信或属于合法软件。

## Detection Ideas

- 服务路径位于用户可写目录。
- `ImagePath` 使用脚本解释器或 LOLBin。
- 服务名伪装成 Microsoft、Windows Update、驱动组件。
- `Start=2` 的自动启动服务突然出现。
- 服务账户异常，例如不必要的高权限账户。

## Collection

```powershell
Get-ChildItem "HKLM:\SYSTEM\CurrentControlSet\Services" |
  ForEach-Object { Get-ItemProperty $_.PsPath }
```

## Cross Validation

- System.evtx Service Control Manager events
- Sysmon Event ID 6, 12, 13
- 服务二进制文件时间线
- Prefetch and Amcache

