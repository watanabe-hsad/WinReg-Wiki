<section class="ww-page-header" markdown>
<p class="ww-hero-eyebrow">Registry Explorer</p>
<h1>按 Windows 原生 root key 浏览</h1>
<p>这个入口解释 key / value 是什么、来自哪个 hive、离线文件在哪里，以及解释时有哪些边界。</p>
</section>

<div class="ww-card-grid ww-card-grid--roots" markdown>
<a class="ww-root-card" href="hkcr/">
  <span class="ww-chip ww-chip--hive">HKCR</span>
  <strong>HKEY_CLASSES_ROOT</strong>
  <span>文件关联、COM、协议处理器的合并视图。</span>
  <em>Mapping: HKLM Classes + HKCU Classes</em>
  <small>软件 · Shell · COM</small>
</a>

<a class="ww-root-card" href="hkcu/">
  <span class="ww-chip ww-chip--hive">HKCU</span>
  <strong>HKEY_CURRENT_USER</strong>
  <span>当前用户配置视图。</span>
  <em>Offline: C:\Users\&lt;User&gt;\NTUSER.DAT</em>
  <small>用户行为 · 持久化 · 网络</small>
</a>

<a class="ww-root-card" href="hklm/">
  <span class="ww-chip ww-chip--hive">HKLM</span>
  <strong>HKEY_LOCAL_MACHINE</strong>
  <span>机器级配置入口。</span>
  <em>Offline: SYSTEM / SOFTWARE / SAM / SECURITY</em>
  <small>系统配置 · 策略 · 设备</small>
</a>

<a class="ww-root-card" href="hku/">
  <span class="ww-chip ww-chip--hive">HKU</span>
  <strong>HKEY_USERS</strong>
  <span>已加载用户 hive、服务账户 hive 和默认账户 hive。</span>
  <em>Offline: NTUSER.DAT / UsrClass.dat</em>
  <small>账户 · 用户行为 · Shell</small>
</a>

<a class="ww-root-card" href="hkcc/">
  <span class="ww-chip ww-chip--hive">HKCC</span>
  <strong>HKEY_CURRENT_CONFIG</strong>
  <span>当前硬件配置映射。</span>
  <em>Mapping: SYSTEM Hardware Profiles</em>
  <small>硬件配置 · 系统环境</small>
</a>
</div>

<div class="ww-card-grid ww-card-grid--two" markdown>
<a class="ww-feature-card ww-feature-card--index" href="generated-index/">
  <span class="ww-card-kicker">Generated from data/registry</span>
  <strong>结构化索引</strong>
  <span>按 root、hive、topic 和状态浏览当前 registry YAML 试点路径。</span>
</a>

<a class="ww-feature-card ww-feature-card--index" href="coverage/">
  <span class="ww-card-kicker">Coverage matrix</span>
  <strong>覆盖矩阵</strong>
  <span>维护当前结构化覆盖范围和下一阶段候选注册表路径。</span>
</a>
</div>

## Browse by topic

<div class="ww-chip-row" markdown>
<span class="ww-chip ww-chip--topic">系统配置</span>
<span class="ww-chip ww-chip--topic">用户行为</span>
<span class="ww-chip ww-chip--topic">持久化</span>
<span class="ww-chip ww-chip--topic">网络</span>
<span class="ww-chip ww-chip--topic">账户</span>
<span class="ww-chip ww-chip--topic">设备</span>
<span class="ww-chip ww-chip--topic">策略</span>
<span class="ww-chip ww-chip--topic">软件</span>
</div>

## High-frequency paths

<div class="ww-card-grid ww-card-grid--paths" markdown>
<a class="ww-path-card" href="hklm/system/select/"><span class="ww-chip ww-chip--hive">SYSTEM</span><strong>HKLM\SYSTEM\Select</strong><span>CurrentControlSet 映射。</span><em>系统配置</em></a>
<a class="ww-path-card" href="hklm/system/controlset/services/"><span class="ww-chip ww-chip--hive">SYSTEM</span><strong>Services</strong><span>服务和驱动配置。</span><em>持久化</em></a>
<a class="ww-path-card" href="hklm/system/controlset/enum/usbstor/"><span class="ww-chip ww-chip--hive">SYSTEM</span><strong>USBSTOR</strong><span>USB 存储设备枚举。</span><em>设备</em></a>
<a class="ww-path-card" href="hklm/software/microsoft/windows-nt/currentversion/profilelist/"><span class="ww-chip ww-chip--hive">SOFTWARE</span><strong>ProfileList</strong><span>SID 到 profile 路径映射。</span><em>账户</em></a>
<a class="ww-path-card" href="hklm/software/microsoft/windows-nt/currentversion/winlogon/"><span class="ww-chip ww-chip--hive">SOFTWARE</span><strong>Winlogon</strong><span>交互式登录配置。</span><em>登录</em></a>
<a class="ww-path-card" href="hkcu/software/microsoft/windows/currentversion/userassist/"><span class="ww-chip ww-chip--hive">NTUSER.DAT</span><strong>UserAssist</strong><span>Explorer 用户交互线索。</span><em>用户行为</em></a>
</div>
