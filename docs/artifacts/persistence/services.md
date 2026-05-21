---
tags:
  - Persistence
  - Services
  - SYSTEM
---

# Services

此页保留 Windows Services artifact 的补充细节。主入口请先查看注册表位置页和取证场景页。

## 对应注册表位置

| 位置 | 说明 |
|---|---|
| [HKLM\SYSTEM\CurrentControlSet\Services](../../registry-tree/hklm/system/controlset/services/index.md) | 服务、驱动和相关服务配置根位置。 |
| `Services\<DriverName>` | 驱动也保存在 Services 子树下，通常通过 `Type`、`Start`、`Group` 等 value 区分。 |

## 字段语义

| Value | 类型 | 含义 |
|---|---|---|
| `ImagePath` | `REG_EXPAND_SZ` / `REG_SZ` | 服务二进制或命令行。 |
| `Start` | `REG_DWORD` | 启动类型。 |
| `Type` | `REG_DWORD` | 服务或驱动类型。 |
| `DisplayName` | `REG_SZ` | 显示名称。 |
| `ObjectName` | `REG_SZ` | 服务运行账户。 |
| `FailureActions` | `REG_BINARY` | 失败恢复动作。 |
| `ServiceDll` | `REG_EXPAND_SZ` / `REG_SZ` | `svchost.exe` 托管服务常见 DLL 路径。 |

## 采集与工具

```powershell
Get-ChildItem "HKLM:\SYSTEM\CurrentControlSet\Services" |
  ForEach-Object { Get-ItemProperty $_.PsPath }
```

- Registry Explorer / RECmd：查看 service key、value 和 LastWrite。
- Autoruns：快速查看 services 和 drivers。
- KAPE / Velociraptor：采集 SYSTEM、System.evtx、服务二进制和执行痕迹。

## 常见误读

- service key 存在不等于服务成功启动。
- `ImagePath` 指向的文件可能已删除或被替换。
- 服务名和显示名可以伪装，不能单独作为可信来源。
- 离线分析需根据 `SYSTEM\Select` 判断当前控制集。

## 交叉验证

- System.evtx Service Control Manager events。
- Sysmon Event ID 1、6、12、13。
- 服务二进制文件时间线、签名、哈希、路径权限。
- Prefetch、Amcache、Shimcache、BAM/DAM。

## 相关场景

- [自启动与持久化](../../questions/persistence.md)
- [程序执行痕迹](../../questions/execution.md)
- [常规注册表检查](../../questions/registry-checklist.md)

## 参考资料

- [Microsoft Learn: Services registry tree](https://learn.microsoft.com/en-us/windows-hardware/drivers/install/hklm-system-currentcontrolset-services-registry-tree)
- [Microsoft Sysinternals: Autoruns](https://learn.microsoft.com/en-us/sysinternals/downloads/autoruns)
