# HKLM\SYSTEM\ControlSet00x\Control\TimeZoneInformation

`TimeZoneInformation` 保存系统时区和 bias 配置。

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SYSTEM\CurrentControlSet\Control\TimeZoneInformation` |
| 离线 | `SYSTEM\ControlSet00x\Control\TimeZoneInformation` |

## 常见子键 / value

| 名称 | 类型 | 含义 |
|---|---|---|
| `TimeZoneKeyName` | `REG_SZ` | Windows 时区键名。 |
| `Bias` | `REG_DWORD` | 本地时间与 UTC 的偏移，单位为分钟。 |
| `ActiveTimeBias` | `REG_DWORD` | 当前生效偏移，通常考虑夏令时。 |
| `StandardName` | `REG_SZ` | 标准时间名称。 |
| `DaylightName` | `REG_SZ` | 夏令时名称。 |

## 说明

| 项 | 内容 |
|---|---|
| 数据来源 | `SYSTEM` hive。 |
| 常见写入者 | Windows 时间/区域设置、GPO、系统安装或配置流程。 |
| 注意 | 时间线归一化时应记录时区配置；注册表时间戳本身通常以 UTC 存储。 |

## 相关 Artifact

- 暂无专门 artifact 页面
- [ProfileList](../../../artifacts/security/profilelist.md)

