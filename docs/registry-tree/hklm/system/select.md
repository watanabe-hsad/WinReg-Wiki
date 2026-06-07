# HKLM\SYSTEM\Select

`HKLM\SYSTEM\Select` 记录 `CurrentControlSet` 与真实 `ControlSet00x` 的映射关系。

<div class="ww-fact-card" markdown>
<div class="ww-fact-card__top">
<div><span class="ww-card-kicker">Registry Fact Card</span><strong>HKLM\SYSTEM\Select</strong></div>
<span class="ww-badge ww-badge--status">stable / high</span>
</div>
<div class="ww-fact-grid" markdown>
<div><span>Root</span><span class="ww-badge ww-badge--hive">HKLM</span></div>
<div><span>Hive</span><span class="ww-badge ww-badge--hive">SYSTEM</span></div>
<div><span>Offline file</span><strong>C:\Windows\System32\Config\SYSTEM</strong></div>
<div class="ww-fact-wide"><span>Native path</span><div class="ww-path-stack"><span class="ww-path-pill">HKLM\SYSTEM\Select</span></div></div>
</div>
<div class="ww-fact-footer">
<div><span>Topics</span><span class="ww-chip ww-chip--topic">系统配置</span></div>
<div><span>Scenarios</span><span class="ww-chip ww-chip--scenario">常规注册表检查</span><span class="ww-chip ww-chip--scenario">自启动与持久化</span><span class="ww-chip ww-chip--scenario">USB 与外接设备</span></div>
<div><span>Related data</span><span class="ww-chip ww-chip--data">data/registry: hklm-system-select</span><span class="ww-chip ww-chip--data">artifact: services</span><span class="ww-chip ww-chip--data">artifact: bam-dam</span><span class="ww-chip ww-chip--data">artifact: usbstor</span></div>
</div>
</div>

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SYSTEM\Select` |
| 离线 | `SYSTEM\Select` |

## 常见子键 / value

| 名称 | 类型 | 含义 |
|---|---|---|
| `Current` | `REG_DWORD` | 当前启动后映射为 `CurrentControlSet` 的控制集编号。 |
| `Default` | `REG_DWORD` | 下次启动默认使用的控制集编号。 |
| `Failed` | `REG_DWORD` | 最近一次失败启动相关控制集；为 `0` 时通常表示无记录。 |
| `LastKnownGood` | `REG_DWORD` | 上一次已知良好配置对应的控制集编号。 |

## 说明

| 项 | 内容 |
|---|---|
| 数据来源 | `SYSTEM` hive。 |
| 常见写入者 | Windows 启动过程。 |
| 注意 | 离线分析时不要直接假设 `ControlSet001` 是当前配置，应先读取 `Select\Current`。 |

## 取证提示

- 离线解释 `Services`、`Enum`、`Control` 等路径前，先确认当前控制集编号。
- 比较多个 `ControlSet00x` 时，应记录每个控制集来源和是否为当前配置。

## 相关场景

- [常规注册表检查](../../../questions/registry-checklist.md)
- [自启动与持久化](../../../questions/persistence.md)
- [USB 与外接设备](../../../questions/usb.md)

## 相关位置

- [HKLM\SYSTEM](index.md)
- [ControlSet00x](controlset/index.md)

## 补充阅读

- [Services](../../../artifacts/persistence/services.md)
- [BAM / DAM](../../../artifacts/execution/bam-dam.md)
- [USBSTOR](../../../artifacts/usb/usbstor.md)
