# HKLM\SOFTWARE\Microsoft\Windows Search\VolumeInfoCache

`VolumeInfoCache` 保存 Windows Search 记录的卷信息缓存。

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SOFTWARE\Microsoft\Windows Search\VolumeInfoCache` |
| 离线 | `SOFTWARE\Microsoft\Windows Search\VolumeInfoCache` |

## 常见子键 / value

| 名称 | 类型 | 含义 |
|---|---|---|
| `<volume key>` | Key | 缓存的卷记录。 |
| `DriveLetter` | `REG_SZ` / 待验证 | 驱动器号信息；字段名和类型需按系统验证。 |
| `VolumeLabel` | `REG_SZ` / 待验证 | 卷标信息；字段名和类型需按系统验证。 |
| `<metadata value>` | `REG_*` | Windows Search 使用的卷元数据。 |

## 说明

| 项 | 内容 |
|---|---|
| 数据来源 | `SOFTWARE` hive。 |
| 常见写入者 | Windows Search / 索引服务。 |
| 注意 | 该位置是否存在和是否填充受 Windows Search 配置影响；不能单独证明 USB 插入或文件访问。 |

## 补充阅读

- [VolumeInfoCache](../../../../../artifacts/usb/volumeinfocache.md)
- [MountedDevices](../../../../../artifacts/usb/mounteddevices.md)
- [MountPoints2](../../../../../artifacts/usb/mountpoints2.md)

