# WinReg Wiki

Windows 注册表键值速查与取证线索知识库。

## 怎么查

| 需求 | 入口 |
|---|---|
| 查某个注册表路径、key 或 value 是什么 | [注册表位置](registry-tree/index.md) |
| 按调查问题查相关线索 | [取证场景](questions/index.md) |
| 查 artifact 的补充细节 | [取证场景 -> Artifact 补充索引](artifacts/index.md) |
| 查基础概念 | [注册表基础](getting-started/registry-basics.md)、[时间戳语义](getting-started/timestamps.md) |

## 注册表基础

| 名称 | 简要说明 |
|---|---|
| `HKLM` | 机器级配置入口，离线主要来自 `SYSTEM`、`SOFTWARE`、`SAM`、`SECURITY` 等 hive。 |
| `HKCU` | 当前用户视图，实际映射到 `HKU\<SID>`。离线通常对应目标用户的 `NTUSER.DAT`。 |
| `HKU` | 已加载用户 hive 集合，包括普通用户、服务账户和 `.DEFAULT`。 |
| `HKCR` | Classes 合并视图，来自 `HKLM\Software\Classes` 与 `HKCU\Software\Classes`。 |
| `HKCC` | 当前硬件配置映射，通常指向 `HKLM\SYSTEM\CurrentControlSet\Hardware Profiles\Current`。 |
| `SYSTEM` | 控制集、服务、驱动、设备、网络、RDP 服务端等机器级配置。 |
| `SOFTWARE` | 软件、策略、Winlogon、ProfileList、Defender、COM / Classes 等机器级配置。 |
| `SAM` | 本地账户和组数据库。 |
| `SECURITY` | LSA、安全策略、审计策略等。 |
| `NTUSER.DAT` | 单个用户的用户级注册表 hive。 |
| `UsrClass.dat` | 用户级 Classes / Shell 相关 hive。 |
| `BCD` | 启动配置数据库，可映射为 `HKLM\BCD00000000`。 |
| live view | 正在运行系统中的注册表视图，包含 `HKCU`、`HKCR`、`HKCC`、`CurrentControlSet` 等映射。 |
| offline hive | 离线镜像中的 hive 文件，需要手动加载并解析 SID、ControlSet 和用户目录。 |
| `CurrentControlSet` | live 映射；离线时用 `HKLM\SYSTEM\Select\Current` 解析到 `ControlSet00x`。 |
| key LastWrite | key 级更新时间，不等同某个 value 的创建时间。 |

## 内容边界

| 区域 | 放什么 |
|---|---|
| [注册表位置](registry-tree/index.md) | key / value 是什么、在哪里、来自哪个 hive、基本注意事项。 |
| [取证场景](questions/index.md) | 按调查问题组织证据语义、交叉验证和检测思路。 |
| [Artifact 补充索引](artifacts/index.md) | 具体 artifact 的字段、证据边界、误报、采集和工具；不是主要阅读入口。 |
