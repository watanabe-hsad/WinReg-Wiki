# HKLM\SYSTEM\ControlSet00x\Services\<DriverName>

驱动服务与普通服务同在 `Services` 树下，通过 `Type`、`Start`、`ImagePath` 等 value 描述加载配置。

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SYSTEM\CurrentControlSet\Services\<DriverName>` |
| 离线 | `SYSTEM\ControlSet00x\Services\<DriverName>` |

## 常见子键 / value

| 名称 | 类型 | 含义 |
|---|---|---|
| `Type` | `REG_DWORD` | 服务类型；常见 `1` kernel driver、`2` file system driver。 |
| `Start` | `REG_DWORD` | 启动类型；常见 `0` boot、`1` system、`2` auto、`3` demand、`4` disabled。 |
| `ImagePath` | `REG_EXPAND_SZ` / `REG_SZ` | 驱动镜像路径。 |
| `Group` | `REG_SZ` | 加载组。 |
| `ErrorControl` | `REG_DWORD` | 加载失败处理策略。 |
| `Parameters` | Key | 驱动私有参数。 |

## 说明

| 项 | 内容 |
|---|---|
| 数据来源 | `SYSTEM` hive。 |
| 常见写入者 | 驱动安装器、PnP、Service Control Manager、系统组件。 |
| 注意 | 驱动配置存在不等于驱动已加载；需结合 System.evtx、Sysmon 6、Code Integrity 或内存证据。 |

## 相关 Artifact

- [Drivers](../../../artifacts/persistence/drivers.md)
- [Services](../../../artifacts/persistence/services.md)

