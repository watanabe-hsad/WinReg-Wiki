# HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall

`Uninstall` 保存机器级软件安装登记和卸载信息。

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall` |
| 离线 | `SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall` |

## 常见子键 / value

| 名称 | 类型 | 含义 |
|---|---|---|
| `<ProductKey>` | Key | 单个软件登记项，可能是 GUID 或产品名。 |
| `DisplayName` | `REG_SZ` | 显示名称。 |
| `DisplayVersion` | `REG_SZ` | 显示版本。 |
| `InstallLocation` | `REG_SZ` | 安装目录。 |
| `InstallDate` | `REG_SZ` | 安装日期字符串；格式和可靠性取决于安装器。 |
| `UninstallString` | `REG_SZ` | 卸载命令。 |
| `Publisher` | `REG_SZ` | 发布者。 |

## 说明

| 项 | 内容 |
|---|---|
| 数据来源 | `SOFTWARE` hive；32 位软件可能在 `WOW6432Node` 视图。 |
| 常见写入者 | MSI、安装器、应用更新器。 |
| 注意 | 登记项存在说明安装登记存在，不等于程序近期运行。 |

## 补充阅读

- [Amcache](../../../../../../artifacts/execution/amcache.md)
- [MUICache](../../../../../../artifacts/execution/muicache.md)
- [Run / RunOnce](../../../../../../artifacts/persistence/run-keys.md)

