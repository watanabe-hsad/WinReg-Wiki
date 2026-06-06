# WinReg Wiki

<p class="ww-lede">Windows 注册表键值速查与取证线索。</p>

WinReg Wiki 是中文优先的 Windows 注册表知识库。主路径是按注册表位置查询 key / value 的含义；取证场景用于把路径组合成检查清单；artifact 页面保留为补充细节层。

<div class="ww-entry-grid" markdown>

<a class="ww-entry-card" href="registry-tree/">
  <span class="ww-entry-kicker">Registry Tree</span>
  <strong>按注册表位置查</strong>
  <span>从 HKLM、HKCU、HKU、HKCR、HKCC 进入，查看路径、hive、value 和注意事项。</span>
</a>

<a class="ww-entry-card" href="questions/">
  <span class="ww-entry-kicker">Scenarios</span>
  <strong>按取证场景查</strong>
  <span>从程序执行、自启动、USB、RDP、账户、安全策略和网络问题进入。</span>
</a>

<a class="ww-entry-card" href="registry-tree/generated-index/">
  <span class="ww-entry-kicker">Structured Data</span>
  <strong>看结构化索引</strong>
  <span>由 data/registry 生成，按 hive 和主题查看当前结构化试点路径。</span>
</a>

</div>

## 当前覆盖

<div class="ww-stat-grid" markdown>

<div class="ww-stat"><strong>97</strong><span>registry-tree Markdown</span></div>
<div class="ww-stat"><strong>42</strong><span>artifact 补充页</span></div>
<div class="ww-stat"><strong>42</strong><span>artifact YAML</span></div>
<div class="ww-stat"><strong>10</strong><span>registry YAML 试点</span></div>

</div>

## 常用路径

<div class="ww-chip-row" markdown>

[Run Keys](registry-tree/hklm/software/microsoft/windows/currentversion/run.md){ .ww-path-chip }
[Services](registry-tree/hklm/system/controlset/services/index.md){ .ww-path-chip }
[USBSTOR](registry-tree/hklm/system/controlset/enum/usbstor.md){ .ww-path-chip }
[UserAssist](registry-tree/hkcu/software/microsoft/windows/currentversion/userassist.md){ .ww-path-chip }
[Winlogon](registry-tree/hklm/software/microsoft/windows-nt/currentversion/winlogon.md){ .ww-path-chip }
[ProfileList](registry-tree/hklm/software/microsoft/windows-nt/currentversion/profilelist.md){ .ww-path-chip }
[MountedDevices](registry-tree/hklm/system/mounteddevices.md){ .ww-path-chip }
[Defender](registry-tree/hklm/software/policies/microsoft/windows-defender.md){ .ww-path-chip }
[RDP](registry-tree/hklm/system/controlset/control/terminal-server.md){ .ww-path-chip }

</div>

## 注册表基础

| 名称 | 简要说明 |
|---|---|
| `HKLM` | 机器级配置入口，离线主要来自 `SYSTEM`、`SOFTWARE`、`SAM`、`SECURITY` 等 hive。 |
| `HKCU` | 当前用户视图，实际映射到 `HKU\<SID>`；离线通常对应目标用户的 `NTUSER.DAT`。 |
| `HKU` | 已加载用户 hive 集合，包括普通用户、服务账户和 `.DEFAULT`。 |
| `HKCR` | Classes 合并视图，来自 `HKLM\Software\Classes` 与 `HKCU\Software\Classes`。 |
| `HKCC` | 当前硬件配置映射，通常指向 `HKLM\SYSTEM\CurrentControlSet\Hardware Profiles\Current`。 |
| `CurrentControlSet` | live 映射；离线时用 `HKLM\SYSTEM\Select\Current` 解析到 `ControlSet00x`。 |
| key LastWrite | key 级更新时间，不等同某个 value 的创建时间。 |

## 内容边界

| 区域 | 放什么 |
|---|---|
| [注册表位置](registry-tree/index.md) | key / value 是什么、在哪里、来自哪个 hive、基本注意事项。 |
| [取证场景](questions/index.md) | 按调查问题组织证据语义、交叉验证和检测思路。 |
| [Artifact 补充索引](artifacts/index.md) | 具体 artifact 的字段、证据边界、误报、采集和工具；不是主要阅读入口。 |
