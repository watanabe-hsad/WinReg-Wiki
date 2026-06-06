<section class="ww-hero" markdown>
<div class="ww-hero-copy" markdown>
<p class="ww-hero-eyebrow">Registry Knowledge Base</p>
<h1 class="ww-hero-title">WinReg Wiki</h1>
<p class="ww-hero-subtitle">Windows 注册表键值速查与取证线索</p>
<p class="ww-hero-text">中文 Windows Registry knowledge base。按注册表路径查询 key / value 含义，再按取证场景交叉验证证据边界。</p>
</div>

<div class="ww-search-panel" markdown>
<span class="ww-search-label">Search registry paths</span>
<a class="ww-search-box" href="#__search">
  <span class="ww-search-placeholder">Search: Run Keys, USBSTOR, Winlogon, ProfileList...</span>
  <span class="ww-command-group"><kbd class="ww-command-key">/</kbd><kbd class="ww-command-key">Ctrl K</kbd></span>
</a>
<div class="ww-chip-row ww-chip-row--tight" markdown>
[HKLM](registry-tree/hklm/index.md){ .ww-chip .ww-chip--hive }
[HKCU](registry-tree/hkcu/index.md){ .ww-chip .ww-chip--hive }
[SYSTEM](registry-tree/hklm/system/index.md){ .ww-chip .ww-chip--hive }
[SOFTWARE](registry-tree/hklm/software/index.md){ .ww-chip .ww-chip--hive }
[Run Keys](registry-tree/hklm/software/microsoft/windows/currentversion/run.md){ .ww-chip }
[Services](registry-tree/hklm/system/controlset/services/index.md){ .ww-chip }
[USBSTOR](registry-tree/hklm/system/controlset/enum/usbstor.md){ .ww-chip }
[UserAssist](registry-tree/hkcu/software/microsoft/windows/currentversion/userassist.md){ .ww-chip }
[Winlogon](registry-tree/hklm/software/microsoft/windows-nt/currentversion/winlogon.md){ .ww-chip }
[ProfileList](registry-tree/hklm/software/microsoft/windows-nt/currentversion/profilelist.md){ .ww-chip }
[MountedDevices](registry-tree/hklm/system/mounteddevices.md){ .ww-chip }
[Defender](registry-tree/hklm/software/policies/microsoft/windows-defender.md){ .ww-chip }
[RDP](registry-tree/hklm/system/controlset/control/terminal-server.md){ .ww-chip }
</div>
</div>
</section>

<div class="ww-dashboard-grid" markdown>
<div class="ww-stat-card"><span>registry pages</span><strong>97</strong><em>含索引和覆盖矩阵</em></div>
<div class="ww-stat-card"><span>registry YAML</span><strong>10</strong><em>结构化试点</em></div>
<div class="ww-stat-card"><span>artifact supplements</span><strong>42</strong><em>补充细节层</em></div>
<div class="ww-stat-card"><span>scenarios</span><strong>12</strong><em>取证查询入口</em></div>
</div>

<div class="ww-card-grid ww-card-grid--three" markdown>
<a class="ww-feature-card" href="registry-tree/">
  <span class="ww-card-kicker">Registry Explorer</span>
  <strong>按注册表位置查</strong>
  <span>从 HKLM、HKCU、HKU、HKCR、HKCC 进入，查看路径、hive、value、默认状态和注意事项。</span>
</a>

<a class="ww-feature-card" href="questions/">
  <span class="ww-card-kicker">Scenario Playbooks</span>
  <strong>按取证场景查</strong>
  <span>按程序执行、自启动、USB、RDP、账户、安全策略和网络问题组织检查清单。</span>
</a>

<a class="ww-feature-card" href="registry-tree/generated-index/">
  <span class="ww-card-kicker">Structured Index</span>
  <strong>看结构化索引</strong>
  <span>由 data/registry 生成，按 root、hive、topic 和状态查看当前结构化路径。</span>
</a>
</div>

## Popular Registry Paths

<div class="ww-card-grid ww-card-grid--paths" markdown>
<a class="ww-path-card" href="registry-tree/hklm/system/select/">
  <span class="ww-chip ww-chip--hive">SYSTEM</span>
  <strong>HKLM\SYSTEM\Select</strong>
  <span>解析 CurrentControlSet 到真实 ControlSet00x。</span>
  <em>常规注册表检查</em>
</a>

<a class="ww-path-card" href="registry-tree/hklm/system/controlset/services/">
  <span class="ww-chip ww-chip--hive">SYSTEM</span>
  <strong>Services</strong>
  <span>服务、驱动、网络组件和系统组件配置。</span>
  <em>自启动与持久化</em>
</a>

<a class="ww-path-card" href="registry-tree/hklm/system/controlset/enum/usbstor/">
  <span class="ww-chip ww-chip--hive">SYSTEM</span>
  <strong>USBSTOR</strong>
  <span>USB Mass Storage 设备枚举信息。</span>
  <em>USB 与外接设备</em>
</a>

<a class="ww-path-card" href="registry-tree/hklm/system/mounteddevices/">
  <span class="ww-chip ww-chip--hive">SYSTEM</span>
  <strong>MountedDevices</strong>
  <span>卷 GUID、DOS 盘符和设备标识映射。</span>
  <em>USB 与外接设备</em>
</a>

<a class="ww-path-card" href="registry-tree/hklm/software/microsoft/windows/currentversion/run/">
  <span class="ww-chip ww-chip--hive">SOFTWARE</span>
  <strong>HKLM Run / RunOnce</strong>
  <span>机器级登录启动项。</span>
  <em>自启动与持久化</em>
</a>

<a class="ww-path-card" href="registry-tree/hkcu/software/microsoft/windows/currentversion/run/">
  <span class="ww-chip ww-chip--hive">NTUSER.DAT</span>
  <strong>HKCU Run / RunOnce</strong>
  <span>用户级登录启动项，归属到具体用户 hive。</span>
  <em>自启动与持久化</em>
</a>

<a class="ww-path-card" href="registry-tree/hkcu/software/microsoft/windows/currentversion/userassist/">
  <span class="ww-chip ww-chip--hive">NTUSER.DAT</span>
  <strong>UserAssist</strong>
  <span>Explorer 相关用户交互和程序线索。</span>
  <em>程序执行</em>
</a>

<a class="ww-path-card" href="registry-tree/hklm/software/microsoft/windows-nt/currentversion/winlogon/">
  <span class="ww-chip ww-chip--hive">SOFTWARE</span>
  <strong>Winlogon</strong>
  <span>登录初始化、Shell、自动登录和登录链配置。</span>
  <em>账户与安全</em>
</a>

<a class="ww-path-card" href="registry-tree/hklm/software/microsoft/windows-nt/currentversion/profilelist/">
  <span class="ww-chip ww-chip--hive">SOFTWARE</span>
  <strong>ProfileList</strong>
  <span>SID 到用户 profile 目录的映射。</span>
  <em>账户与安全</em>
</a>
</div>

## Registry Basics

<div class="ww-card-grid ww-card-grid--compact" markdown>
<div class="ww-info-card"><strong>Hive</strong><span>离线文件，例如 <code>SYSTEM</code>、<code>SOFTWARE</code>、<code>NTUSER.DAT</code>、<code>UsrClass.dat</code>。</span></div>
<div class="ww-info-card"><strong>CurrentControlSet</strong><span>live 视图；离线时用 <code>HKLM\SYSTEM\Select\Current</code> 解析到 <code>ControlSet00x</code>。</span></div>
<div class="ww-info-card"><strong>HKCU / HKU</strong><span><code>HKCU</code> 是当前用户视图；离线分析应定位具体 <code>HKU\&lt;SID&gt;</code> hive。</span></div>
<div class="ww-info-card"><strong>Artifact</strong><span>artifact 页面是字段、工具和误判补充，不是主要阅读入口。</span></div>
</div>
