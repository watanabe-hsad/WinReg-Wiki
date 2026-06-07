# HKLM\SYSTEM\ControlSet00x\Enum\USBSTOR

`USBSTOR` 保存 USB Mass Storage 设备枚举信息。

<div class="ww-fact-card" markdown>
<div class="ww-fact-card__top">
<div><span class="ww-card-kicker">Registry Fact Card</span><strong>HKLM\SYSTEM\ControlSet00x\Enum\USBSTOR</strong></div>
<span class="ww-badge ww-badge--status">reviewed / medium</span>
</div>
<div class="ww-fact-grid" markdown>
<div><span>Root</span><span class="ww-badge ww-badge--hive">HKLM</span></div>
<div><span>Hive</span><span class="ww-badge ww-badge--hive">SYSTEM</span></div>
<div><span>Offline file</span><strong>C:\Windows\System32\Config\SYSTEM</strong></div>
<div class="ww-fact-wide"><span>Native path</span><div class="ww-path-stack"><span class="ww-path-pill">HKLM\SYSTEM\CurrentControlSet\Enum\USBSTOR</span><span class="ww-path-pill">HKLM\SYSTEM\ControlSet00x\Enum\USBSTOR</span></div></div>
</div>
<div class="ww-fact-footer">
<div><span>Topics</span><span class="ww-chip ww-chip--topic">设备</span></div>
<div><span>Scenarios</span><span class="ww-chip ww-chip--scenario">USB 与外接设备</span><span class="ww-chip ww-chip--scenario">常规注册表检查</span></div>
<div><span>Related data</span><span class="ww-chip ww-chip--data">data/registry: hklm-system-enum-usbstor</span><span class="ww-chip ww-chip--data">artifact: usbstor</span><span class="ww-chip ww-chip--data">artifact: usb</span><span class="ww-chip ww-chip--data">artifact: mounteddevices</span></div>
</div>
</div>

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SYSTEM\CurrentControlSet\Enum\USBSTOR` |
| 离线 | `SYSTEM\ControlSet00x\Enum\USBSTOR` |

## 离线位置

`C:\Windows\System32\Config\SYSTEM`

## 作用

记录系统识别过的 USB 存储设备。子键通常可反映设备类型、厂商、产品、版本和序列号。

## 常见子键 / 值

| 名称 | 类型 | 含义 |
|---|---|---|
| `<DeviceType&Vendor&Product&Revision>` | Key | 设备类别、厂商、产品和版本组合。 |
| `<SerialOrInstanceId>` | Key | 设备序列号或实例 ID。 |
| `FriendlyName` | `REG_SZ` | 设备友好名称。 |
| `ParentIdPrefix` | `REG_SZ` | 与设备实例关联的前缀，部分设备存在。 |
| `ContainerID` | `REG_SZ` | 设备容器 ID，可用于关联同一物理设备的接口。 |

## 默认状态 / 常见状态

没有接入过 USB 存储设备的系统可能为空。正常 U 盘、移动硬盘、读卡器、手机 USB 存储模式和企业加密盘都可能留下记录。

## 版本差异

不同设备是否暴露稳定序列号取决于硬件和驱动。无唯一序列号的设备可能使用 Windows 生成的实例标识。

## 取证提示

该位置说明系统枚举过 USB 存储设备，不等于用户访问过文件，也不等于发生复制。连接时间和盘符关系需要结合 SetupAPI.dev.log、Partition/Diagnostic、MountedDevices、MountPoints2、LNK 和 Jump Lists。

## 相关场景

- [USB 与外接设备](../../../../../questions/usb.md)
- [常规注册表检查](../../../../../questions/registry-checklist.md)

## 相关位置

- [HKLM Enum](index.md)
- [HKLM Enum USB](usb.md)
- [HKLM MountedDevices](../../mounteddevices.md)
- [HKCU MountPoints2](../../../../hkcu/software/microsoft/windows/currentversion/mountpoints2.md)
