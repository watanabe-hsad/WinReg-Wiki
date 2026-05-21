---
tags:
  - Persistence
  - Drivers
  - Services
  - SYSTEM
  - HKLM
---

# Drivers

此页保留驱动服务 artifact 的补充细节。主入口请先查看注册表位置页和取证场景页。

## 对应注册表位置

| 位置 | 说明 |
|---|---|
| [HKLM\SYSTEM\ControlSet00x\Services\Drivers](../../registry-tree/hklm/system/controlset/services/drivers.md) | kernel / file system driver 服务配置。 |
| [HKLM\SYSTEM\ControlSet00x\Services](../../registry-tree/hklm/system/controlset/services/index.md) | 服务和驱动共享的配置树。 |

## 字段语义

| Value | 类型 | 含义 |
|---|---|---|
| `Type` | `REG_DWORD` | `1` 常见为 kernel driver，`2` 常见为 file system driver，`0x10/0x20` 为 Win32 service。 |
| `Start` | `REG_DWORD` | `0` boot、`1` system、`2` auto、`3` demand、`4` disabled 常见。 |
| `ImagePath` | `REG_EXPAND_SZ` / `REG_SZ` | 驱动文件路径。 |
| `Group` | `REG_SZ` | 加载组，影响启动阶段顺序。 |
| `ErrorControl` | `REG_DWORD` | 加载失败处理策略。 |
| `Parameters` | Key | 驱动私有参数，含义由驱动决定。 |

## 采集与工具

```cmd
reg query "HKLM\SYSTEM\CurrentControlSet\Services" /s /v ImagePath
```

- Autoruns / Autorunsc：查看 drivers 和 services。
- Registry Explorer / RECmd：离线查看 SYSTEM hive 和 key LastWrite。
- KAPE / Velociraptor：采集 SYSTEM、System.evtx、CodeIntegrity 日志和驱动文件。
- Sigcheck：核对驱动签名和哈希。

## 常见误读

- 驱动服务 key 存在不等于驱动已成功加载。
- `Start=3` 不等于无风险；按需加载驱动仍可能被触发。
- EDR、VPN、备份、磁盘加密、虚拟化和硬件厂商工具会创建大量合法驱动项。
- 离线分析需先用 `SYSTEM\Select` 判断当前控制集。

## 交叉验证

- Sysmon Event ID 6、7、11、13。
- System.evtx Service Control Manager events。
- Microsoft-Windows-CodeIntegrity/Operational。
- 驱动文件签名、哈希、创建 / 修改时间、EDR telemetry。

## 相关场景

- [自启动与持久化](../../questions/persistence.md)
- [程序执行痕迹](../../questions/execution.md)
- [安全策略与防护配置](../../questions/policy-security.md)
- [常规注册表检查](../../questions/registry-checklist.md)

## 参考资料

- [Microsoft Learn: HKLM\SYSTEM\CurrentControlSet\Services Registry Tree](https://learn.microsoft.com/en-us/windows-hardware/drivers/install/hklm-system-currentcontrolset-services-registry-tree)
- [MITRE ATT&CK: Kernel Modules and Extensions](https://attack.mitre.org/techniques/T1547/006/)
- [Microsoft Sysinternals: Autoruns](https://learn.microsoft.com/en-us/sysinternals/downloads/autoruns)
