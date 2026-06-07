<section class="ww-shell ww-shell--landing">
  <div class="ww-hero ww-hero--database">
    <div class="ww-hero-copy">
      <p class="ww-hero-eyebrow">WINDOWS REGISTRY KNOWLEDGE BASE</p>
      <h1 class="ww-hero-title">快速查询 Windows 注册表键值含义</h1>
      <p class="ww-hero-subtitle">按原生注册表路径查询 key / value，按取证场景交叉验证线索。</p>
      <p class="ww-hero-text">WinReg Wiki 是中文优先的 Windows Registry reference。主入口是注册表位置，场景页用于组织检查清单，artifact 仅作为补充层。</p>
    </div>

    <button class="ww-search-panel ww-search-panel--hero" type="button" data-ww-search-trigger>
      <span class="ww-search-label">Search</span>
      <span class="ww-search-box">
        <span class="ww-search-icon">⌕</span>
        <span class="ww-search-placeholder">搜索路径、值名、场景，例如 Run Keys / USBSTOR / Winlogon</span>
        <span class="ww-command-group"><kbd class="ww-command-key">/</kbd><kbd class="ww-command-key">Ctrl K</kbd></span>
      </span>
      <span class="ww-search-note">点击打开 MkDocs 全站搜索。支持中文标题、路径片段和值名。</span>
    </button>
  </div>

  <div class="ww-chip-row ww-chip-row--filters">
    <a class="ww-chip ww-chip--hive" href="registry-tree/hklm/">HKLM</a>
    <a class="ww-chip ww-chip--hive" href="registry-tree/hkcu/">HKCU</a>
    <a class="ww-chip ww-chip--hive" href="registry-tree/hklm/system/">SYSTEM</a>
    <a class="ww-chip ww-chip--hive" href="registry-tree/hklm/software/">SOFTWARE</a>
    <a class="ww-chip ww-chip--scenario" href="questions/shell-explorer/">User Activity</a>
    <a class="ww-chip ww-chip--scenario" href="questions/persistence/">Persistence</a>
    <a class="ww-chip ww-chip--scenario" href="questions/execution/">Program Execution</a>
    <a class="ww-chip ww-chip--scenario" href="questions/usb/">USB</a>
    <a class="ww-chip ww-chip--scenario" href="questions/rdp/">RDP</a>
    <a class="ww-chip ww-chip--scenario" href="questions/policy-security/">Security Policy</a>
    <a class="ww-chip ww-chip--scenario" href="questions/network/">Network</a>
  </div>

  <div class="ww-dashboard-grid ww-dashboard-grid--landing">
    <div class="ww-stat-card"><span>Registry Pages</span><strong>98</strong><em>按原生树组织</em></div>
    <div class="ww-stat-card"><span>Registry Data Records</span><strong>10</strong><em>结构化试点</em></div>
    <div class="ww-stat-card"><span>Artifact Supplements</span><strong>42</strong><em>补充细节层</em></div>
    <div class="ww-stat-card"><span>Scenarios</span><strong>12</strong><em>检查清单入口</em></div>
  </div>

  <div class="ww-card-grid ww-card-grid--three">
    <a class="ww-feature-card ww-feature-card--primary" href="registry-tree/explorer/">
      <span class="ww-card-mark">REG</span>
      <span class="ww-card-kicker">Registry Explorer</span>
      <strong>按注册表位置查</strong>
      <span>用关键词、Hive、主题和状态筛选结构化 registry entry，再进入人工维护的路径页面。</span>
      <em>Explore →</em>
    </a>

    <a class="ww-feature-card" href="questions/">
      <span class="ww-card-mark">SCN</span>
      <span class="ww-card-kicker">Scenario Playbooks</span>
      <strong>按取证场景查</strong>
      <span>程序执行、自启动、USB、RDP、账户、安全策略和网络配置的检查入口。</span>
      <em>Explore →</em>
    </a>

    <a class="ww-feature-card" href="registry-tree/generated-index/">
      <span class="ww-card-mark">IDX</span>
      <span class="ww-card-kicker">Structured Registry Index</span>
      <strong>看结构化索引</strong>
      <span>由 data/registry 生成的路径索引，适合快速扫当前结构化覆盖范围。</span>
      <em>Explore →</em>
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
      <span class="ww-chip ww-chip--hive">HKLM</span>
      <strong>Run Keys</strong>
      <span>机器级登录启动项和 RunOnce 配置。</span>
      <em>持久化</em>
    </a>

    <a class="ww-path-card" href="registry-tree/hklm/system/controlset/services/">
      <span class="ww-chip ww-chip--hive">SYSTEM</span>
      <strong>Services</strong>
      <span>服务、驱动、网络组件和系统组件配置。</span>
      <em>系统配置</em>
    </a>

    <a class="ww-path-card" href="registry-tree/hklm/system/controlset/enum/usbstor/">
      <span class="ww-chip ww-chip--hive">SYSTEM</span>
      <strong>USBSTOR</strong>
      <span>USB Mass Storage 设备枚举信息。</span>
      <em>设备</em>
    </a>

    <a class="ww-path-card" href="registry-tree/hkcu/software/microsoft/windows/currentversion/userassist/">
      <span class="ww-chip ww-chip--hive">HKCU</span>
      <strong>UserAssist</strong>
      <span>Explorer 相关用户交互线索。</span>
      <em>用户行为</em>
    </a>

    <a class="ww-path-card" href="registry-tree/hklm/software/microsoft/windows-nt/currentversion/winlogon/">
      <span class="ww-chip ww-chip--hive">SOFTWARE</span>
      <strong>Winlogon</strong>
      <span>登录初始化、Shell、Userinit 和自动登录配置。</span>
      <em>账户</em>
    </a>

    <a class="ww-path-card" href="registry-tree/hklm/software/microsoft/windows-nt/currentversion/profilelist/">
      <span class="ww-chip ww-chip--hive">SOFTWARE</span>
      <strong>ProfileList</strong>
      <span>SID 到用户 profile 目录的映射。</span>
      <em>账户</em>
    </a>

    <a class="ww-path-card" href="registry-tree/hklm/system/mounteddevices/">
      <span class="ww-chip ww-chip--hive">SYSTEM</span>
      <strong>MountedDevices</strong>
      <span>卷 GUID、DOS 盘符和设备标识映射。</span>
      <em>设备</em>
    </a>

    <a class="ww-path-card" href="registry-tree/hklm/software/policies/microsoft/windows-defender/">
      <span class="ww-chip ww-chip--hive">Policies</span>
      <strong>Defender Policies</strong>
      <span>Microsoft Defender 策略值和排除项线索。</span>
      <em>策略</em>
    </a>

    <a class="ww-path-card" href="registry-tree/hklm/system/controlset/control/terminal-server/rdp-tcp/">
      <span class="ww-chip ww-chip--hive">SYSTEM</span>
      <strong>RDP-Tcp</strong>
      <span>RDP listener 端口、安全层和 NLA 相关配置。</span>
      <em>RDP</em>
    </a>

    <a class="ww-path-card" href="registry-tree/hklm/system/controlset/services/tcpip/parameters/interfaces/">
      <span class="ww-chip ww-chip--hive">SYSTEM</span>
      <strong>Tcpip Interfaces</strong>
      <span>接口 IP、DNS、网关和 DHCP 租约信息。</span>
      <em>网络</em>
    </a>
  </div>
</section>

<section class="ww-supplemental">
  <div class="ww-card-grid ww-card-grid--compact">
    <div class="ww-info-card"><strong>Registry first</strong><span>路径页面解释 key / value 的位置、作用、常见值和边界。</span></div>
    <div class="ww-info-card"><strong>Scenario assisted</strong><span>场景页组织检查顺序和交叉验证来源。</span></div>
    <div class="ww-info-card"><strong>Artifact supplemental</strong><span>artifact 页面保留采集、解析工具和误读补充，不作为主入口。</span></div>
  </div>
</section>
