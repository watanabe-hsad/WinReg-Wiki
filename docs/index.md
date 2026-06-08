<section class="ww-shell ww-shell--landing">
  <div class="ww-compact-head">
    <p class="ww-hero-eyebrow">WINDOWS REGISTRY KNOWLEDGE BASE</p>
    <h1 class="ww-hero-title">WinReg Wiki</h1>
    <p class="ww-hero-subtitle">Windows 注册表键值速查与取证线索</p>
    <p class="ww-hero-text">按原生注册表路径查询 key / value，按取证场景交叉验证线索。</p>
  </div>

  <button class="ww-search-panel ww-search-panel--inline" type="button" data-ww-search-trigger>
    <span class="ww-search-icon">⌕</span>
    <span class="ww-search-placeholder">搜索路径、值名、场景，例如 Run Keys / USBSTOR / Winlogon</span>
    <span class="ww-command-group"><kbd class="ww-command-key">/</kbd><kbd class="ww-command-key">Ctrl K</kbd></span>
  </button>

  <div class="ww-chip-row ww-chip-row--filters">
    <a class="ww-chip ww-chip--hive" href="registry-tree/hklm/">HKLM</a>
    <a class="ww-chip ww-chip--hive" href="registry-tree/hkcu/">HKCU</a>
    <a class="ww-chip ww-chip--hive" href="registry-tree/hklm/system/">SYSTEM</a>
    <a class="ww-chip ww-chip--hive" href="registry-tree/hklm/software/">SOFTWARE</a>
    <a class="ww-chip ww-chip--scenario" href="registry-tree/hklm/software/microsoft/windows/currentversion/run/">Run Keys</a>
    <a class="ww-chip ww-chip--scenario" href="registry-tree/hklm/system/controlset/services/">Services</a>
    <a class="ww-chip ww-chip--scenario" href="registry-tree/hklm/system/controlset/enum/usbstor/">USBSTOR</a>
    <a class="ww-chip ww-chip--scenario" href="registry-tree/hkcu/software/microsoft/windows/currentversion/userassist/">UserAssist</a>
    <a class="ww-chip ww-chip--scenario" href="registry-tree/hklm/software/microsoft/windows-nt/currentversion/winlogon/">Winlogon</a>
    <a class="ww-chip ww-chip--scenario" href="registry-tree/hklm/software/microsoft/windows-nt/currentversion/profilelist/">ProfileList</a>
    <a class="ww-chip ww-chip--scenario" href="questions/rdp/">RDP</a>
    <a class="ww-chip ww-chip--scenario" href="registry-tree/hklm/software/policies/microsoft/windows-defender/">Defender</a>
  </div>

  <div class="ww-dashboard-grid ww-dashboard-grid--landing">
    <div class="ww-stat-card"><strong>98</strong><span>registry pages</span></div>
    <div class="ww-stat-card"><strong>30</strong><span>registry data</span></div>
    <div class="ww-stat-card"><strong>42</strong><span>artifacts</span></div>
    <div class="ww-stat-card"><strong>12</strong><span>scenarios</span></div>
  </div>

  <div class="ww-card-grid ww-card-grid--three ww-card-grid--entry">
    <a class="ww-feature-card" href="registry-tree/explorer/">
      <span class="ww-card-mark">REG</span>
      <strong>Registry Explorer</strong>
      <span>按路径、Hive、主题筛选。</span>
      <em>Open →</em>
    </a>

    <a class="ww-feature-card" href="questions/">
      <span class="ww-card-mark">SCN</span>
      <strong>Scenario Playbooks</strong>
      <span>场景检查清单入口。</span>
      <em>Open →</em>
    </a>

    <a class="ww-feature-card" href="registry-tree/generated-index/">
      <span class="ww-card-mark">IDX</span>
      <strong>Structured Index</strong>
      <span>data/registry 静态索引。</span>
      <em>Open →</em>
    </a>
  </div>
</section>

<section class="ww-section">
  <div class="ww-section-header">
    <span>Popular Registry Paths</span>
    <h2>常用路径入口</h2>
  </div>

  <div class="ww-card-grid ww-card-grid--paths">
    <a class="ww-path-card" href="registry-tree/hklm/software/microsoft/windows/currentversion/run/">
      <div class="ww-card-line"><strong>Run Keys</strong><span class="ww-chip ww-chip--hive">HKLM / HKCU</span></div>
      <span class="ww-path-pill">...\CurrentVersion\Run</span>
      <span>登录启动项配置。</span>
    </a>

    <a class="ww-path-card" href="registry-tree/hklm/system/controlset/services/">
      <div class="ww-card-line"><strong>Services</strong><span class="ww-chip ww-chip--hive">SYSTEM</span></div>
      <span class="ww-path-pill">ControlSet00x\Services</span>
      <span>服务与驱动配置。</span>
    </a>

    <a class="ww-path-card" href="registry-tree/hklm/system/controlset/enum/usbstor/">
      <div class="ww-card-line"><strong>USBSTOR</strong><span class="ww-chip ww-chip--hive">SYSTEM</span></div>
      <span class="ww-path-pill">Enum\USBSTOR</span>
      <span>USB 存储设备枚举。</span>
    </a>

    <a class="ww-path-card" href="registry-tree/hkcu/software/microsoft/windows/currentversion/userassist/">
      <div class="ww-card-line"><strong>UserAssist</strong><span class="ww-chip ww-chip--hive">HKCU</span></div>
      <span class="ww-path-pill">...\Explorer\UserAssist</span>
      <span>Explorer 用户交互线索。</span>
    </a>

    <a class="ww-path-card" href="registry-tree/hklm/software/microsoft/windows-nt/currentversion/winlogon/">
      <div class="ww-card-line"><strong>Winlogon</strong><span class="ww-chip ww-chip--hive">SOFTWARE</span></div>
      <span class="ww-path-pill">...\Winlogon</span>
      <span>登录初始化配置。</span>
    </a>

    <a class="ww-path-card" href="registry-tree/hklm/software/microsoft/windows-nt/currentversion/profilelist/">
      <div class="ww-card-line"><strong>ProfileList</strong><span class="ww-chip ww-chip--hive">SOFTWARE</span></div>
      <span class="ww-path-pill">...\ProfileList</span>
      <span>SID 与 profile 映射。</span>
    </a>

    <a class="ww-path-card" href="registry-tree/hklm/system/mounteddevices/">
      <div class="ww-card-line"><strong>MountedDevices</strong><span class="ww-chip ww-chip--hive">SYSTEM</span></div>
      <span class="ww-path-pill">MountedDevices</span>
      <span>卷 GUID 与盘符映射。</span>
    </a>

    <a class="ww-path-card" href="registry-tree/hklm/software/policies/microsoft/windows-defender/">
      <div class="ww-card-line"><strong>Defender Policies</strong><span class="ww-chip ww-chip--hive">Policies</span></div>
      <span class="ww-path-pill">Windows Defender</span>
      <span>防护策略配置。</span>
    </a>

    <a class="ww-path-card" href="registry-tree/hklm/system/controlset/control/terminal-server/rdp-tcp/">
      <div class="ww-card-line"><strong>RDP-Tcp</strong><span class="ww-chip ww-chip--hive">SYSTEM</span></div>
      <span class="ww-path-pill">WinStations\RDP-Tcp</span>
      <span>RDP listener 配置。</span>
    </a>

    <a class="ww-path-card" href="registry-tree/hklm/system/controlset/services/tcpip/parameters/interfaces/">
      <div class="ww-card-line"><strong>Tcpip Interfaces</strong><span class="ww-chip ww-chip--hive">SYSTEM</span></div>
      <span class="ww-path-pill">Parameters\Interfaces</span>
      <span>接口 IP / DNS / DHCP。</span>
    </a>
  </div>
</section>

<section class="ww-supplemental">
  <div class="ww-info-strip">
    <span><strong>Registry first</strong> 路径页面解释 key / value。</span>
    <span><strong>Scenario assisted</strong> 场景页组织交叉验证。</span>
    <span><strong>Artifact supplemental</strong> artifact 保留补充细节。</span>
  </div>
</section>
