# HKLM\SYSTEM\MountedDevices

`MountedDevices` 保存卷标识、卷 GUID 和 DOS 盘符之间的映射。

<div class="ww-fact-card" markdown>
<div class="ww-fact-card__head"><span class="ww-card-kicker">Registry Fact Card</span><strong>卷和盘符映射</strong></div>
<div class="ww-fact-grid" markdown>
<div><span>Root</span><strong>HKLM</strong></div>
<div><span>Hive</span><strong>SYSTEM</strong></div>
<div><span>Offline file</span><strong>C:\Windows\System32\Config\SYSTEM</strong></div>
<div class="ww-fact-wide"><span>Native path</span><code>HKLM\SYSTEM\MountedDevices</code></div>
<div><span>Topics</span><span class="ww-chip ww-chip--topic">设备</span></div>
<div><span>Related scenarios</span><span class="ww-chip ww-chip--scenario">USB 与外接设备</span><span class="ww-chip ww-chip--scenario">Shell / Explorer</span></div>
<div><span>Data status</span><strong>reviewed / medium</strong></div>
</div>
</div>

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SYSTEM\MountedDevices` |
| 离线 | `SYSTEM\MountedDevices` |

## 离线位置

`C:\Windows\System32\Config\SYSTEM`

## 作用

Mount Manager 使用该位置维护卷 GUID、DOS 盘符和底层设备标识之间的关系。它能辅助解释某个卷曾被分配过什么盘符，但不保存文件访问或复制行为。

## 常见子键和值

| 名称 | 类型 | 含义 |
|---|---|---|
| `\DosDevices\C:` | `REG_BINARY` | DOS 盘符到卷或设备的二进制映射。 |
| `\??\Volume{GUID}` | `REG_BINARY` | 卷 GUID 到设备标识的映射。 |
| `\DosDevices\<letter>:` | `REG_BINARY` | 其他盘符映射。 |

## 默认状态与版本差异

系统盘和已挂载卷通常会产生记录。盘符、卷 GUID 和二进制数据含义受磁盘类型、分区、可移动设备、虚拟磁盘和系统版本影响。

## 注意事项

- 盘符可复用；不能只凭 `\DosDevices\<letter>:` 判断同一个设备。
- 二进制数据需要结合卷 GUID、设备实例、磁盘签名或工具解析。
- 该位置是机器级卷映射，不说明哪个用户访问过该卷。

## 取证提示

- 与 USBSTOR、USB、SWD\WPDBUSENUM、MountPoints2、LNK 和 Jump Lists 关联时，可帮助还原设备、卷和用户视角。
- 报告中应同时保留盘符、卷 GUID、设备序列或实例 ID，避免只写盘符。

## 相关场景

- [USB 与外接设备](../../../questions/usb.md)
- [Shell / Explorer 用户行为](../../../questions/shell-explorer.md)
- [常规注册表检查](../../../questions/registry-checklist.md)

## 相关位置

- [USBSTOR](controlset/enum/usbstor.md)
- [USB](controlset/enum/usb.md)
- [SWD\WPDBUSENUM](controlset/enum/swd-wpdbusenum.md)
- [MountPoints2](../../hkcu/software/microsoft/windows/currentversion/mountpoints2.md)

## 补充阅读

- [MountedDevices](../../../artifacts/usb/mounteddevices.md)
- [USBSTOR](../../../artifacts/usb/usbstor.md)
- [MountPoints2](../../../artifacts/usb/mountpoints2.md)
