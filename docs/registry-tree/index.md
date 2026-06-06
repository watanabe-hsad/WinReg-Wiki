# 注册表位置

<p class="ww-lede">按 Windows 原生 root key 浏览注册表路径。这个入口只解释 key / value 是什么、来自哪里，以及解释时需要注意什么。</p>

<div class="ww-entry-grid ww-entry-grid--registry" markdown>

<a class="ww-entry-card" href="hkcr/">
  <span class="ww-entry-kicker">HKCR</span>
  <strong>HKEY_CLASSES_ROOT</strong>
  <span>文件关联、COM、协议处理器的合并视图。</span>
</a>

<a class="ww-entry-card" href="hkcu/">
  <span class="ww-entry-kicker">HKCU</span>
  <strong>HKEY_CURRENT_USER</strong>
  <span>当前用户配置，离线通常对应目标用户的 NTUSER.DAT。</span>
</a>

<a class="ww-entry-card" href="hklm/">
  <span class="ww-entry-kicker">HKLM</span>
  <strong>HKEY_LOCAL_MACHINE</strong>
  <span>机器级配置：SYSTEM、SOFTWARE、SAM、SECURITY、BCD。</span>
</a>

<a class="ww-entry-card" href="hku/">
  <span class="ww-entry-kicker">HKU</span>
  <strong>HKEY_USERS</strong>
  <span>已加载用户 hive、服务账户 hive 和默认账户 hive。</span>
</a>

<a class="ww-entry-card" href="hkcc/">
  <span class="ww-entry-kicker">HKCC</span>
  <strong>HKEY_CURRENT_CONFIG</strong>
  <span>当前硬件配置映射，来源于 SYSTEM 中的 Hardware Profiles。</span>
</a>

</div>

## 数据索引

<div class="ww-index-links" markdown>

- [结构化注册表索引](generated-index.md)：由 `data/registry/*.yml` 生成，按 hive 和主题查看试点路径。
- [覆盖矩阵](coverage.md)：由 `data/registry/*.yml` 生成，维护当前结构化覆盖状态和下一阶段候选。

</div>

## 高频路径

| 路径 | 内容 |
|---|---|
| [HKLM\SYSTEM\Select](hklm/system/select.md) | `CurrentControlSet` 到 `ControlSet00x` 的映射。 |
| [HKLM\SYSTEM\ControlSet00x](hklm/system/controlset/index.md) | 真实控制集。 |
| [HKLM\SYSTEM\ControlSet00x\Services](hklm/system/controlset/services/index.md) | 服务、驱动和网络组件配置。 |
| [HKLM\SYSTEM\ControlSet00x\Services\Tcpip\Parameters\Interfaces](hklm/system/controlset/services/tcpip/parameters/interfaces.md) | 网卡 IP、DNS、DHCP、网关。 |
| [HKLM\SYSTEM\ControlSet00x\Enum\USBSTOR](hklm/system/controlset/enum/usbstor.md) | USB 存储设备枚举。 |
| [HKLM\SYSTEM\MountedDevices](hklm/system/mounteddevices.md) | 卷、盘符和设备映射。 |
| [HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList](hklm/software/microsoft/windows-nt/currentversion/profilelist.md) | SID 到 profile 路径映射。 |
| [HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon](hklm/software/microsoft/windows-nt/currentversion/winlogon.md) | 交互式登录配置。 |
| [HKLM Run / RunOnce](hklm/software/microsoft/windows/currentversion/run.md) | 机器级登录启动项。 |
| [HKCU Run / RunOnce](hkcu/software/microsoft/windows/currentversion/run.md) | 用户级登录启动项。 |

## 映射关系速查

| 映射 | 说明 |
|---|---|
| `HKCU` -> `HKU\<SID>` | live 环境下取决于当前进程上下文。 |
| `HKCR` -> `HKLM\Software\Classes` + `HKCU\Software\Classes` | 合并视图，离线时不要当成单独 hive。 |
| `HKCC` -> `HKLM\SYSTEM\CurrentControlSet\Hardware Profiles\Current` | 当前硬件 profile 映射。 |
| `CurrentControlSet` -> `ControlSet00x` | 由 `HKLM\SYSTEM\Select\Current` 决定。 |
