<section class="ww-shell ww-shell--landing">
  <div class="ww-landing-head">
    <p class="ww-hero-eyebrow">WINDOWS 注册表知识库</p>
    <h1 class="ww-hero-title">WinReg Wiki</h1>
    <span class="ww-title-underline" aria-hidden="true"></span>
    <p class="ww-hero-subtitle">Windows 注册表键值速查与取证线索</p>
    <p class="ww-hero-text">按原生注册表路径查询 key / value，按取证场景交叉验证线索。</p>
  </div>

  <button class="ww-search-panel ww-search-panel--landing" type="button" data-ww-search-trigger>
    <span class="ww-search-icon">⌕</span>
    <span class="ww-search-placeholder">搜索注册表路径、值名、场景，例如 Run Keys / USBSTOR / Winlogon</span>
    <span class="ww-command-group"><kbd class="ww-command-key">/</kbd><kbd class="ww-command-key">Ctrl K</kbd></span>
  </button>

  <div class="ww-chip-row ww-chip-row--filters ww-chip-row--center">
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
    <div class="ww-stat-card">
      <span class="ww-stat-icon">REG</span>
      <strong>98</strong>
      <span>注册表页面</span>
      <em>按原生路径整理</em>
    </div>
    <div class="ww-stat-card">
      <span class="ww-stat-icon">YML</span>
      <strong>30</strong>
      <span>结构化记录</span>
      <em>data/registry</em>
    </div>
    <div class="ww-stat-card">
      <span class="ww-stat-icon">ART</span>
      <strong>42</strong>
      <span>补充条目</span>
      <em>artifact YAML</em>
    </div>
    <div class="ww-stat-card">
      <span class="ww-stat-icon">SCN</span>
      <strong>12</strong>
      <span>取证场景</span>
      <em>检查入口</em>
    </div>
  </div>

  <div class="ww-card-grid ww-card-grid--three ww-card-grid--entry ww-card-grid--landing-entry">
    <a class="ww-feature-card" href="registry-tree/explorer/">
      <span class="ww-card-mark">REG</span>
      <strong>注册表位置</strong>
      <span>按 HKLM / HKCU / HKU / HKCR / HKCC 浏览原生注册表树，并使用 Explorer 筛选结构化记录。</span>
      <em>打开 →</em>
    </a>

    <a class="ww-feature-card" href="questions/">
      <span class="ww-card-mark">SCN</span>
      <strong>取证场景</strong>
      <span>从程序执行、自启动、USB、RDP、账户、安全策略等问题进入检查清单。</span>
      <em>打开 →</em>
    </a>

    <a class="ww-feature-card" href="registry-tree/generated-index/">
      <span class="ww-card-mark">IDX</span>
      <strong>结构化索引</strong>
      <span>查看由 data/registry 生成的路径、Hive、主题、状态和相关场景索引。</span>
      <em>打开 →</em>
    </a>
  </div>
</section>

<section class="ww-section ww-section--landing-paths">
  <div class="ww-section-header ww-section-header--centerline">
    <span>常用注册表路径</span>
  </div>

  <div class="ww-card-grid ww-card-grid--paths ww-card-grid--common-paths">
    <a class="ww-path-card" href="registry-tree/hklm/software/microsoft/windows/currentversion/run/">
      <div class="ww-card-line"><strong>Run Keys</strong><span class="ww-chip ww-chip--topic">启动项</span></div>
      <span class="ww-path-pill">HKCU\Software\Microsoft\Windows\CurrentVersion\Run</span>
      <span>用户登录时加载的启动项配置。</span>
    </a>

    <a class="ww-path-card" href="registry-tree/hklm/system/controlset/services/">
      <div class="ww-card-line"><strong>Services</strong><span class="ww-chip ww-chip--topic">服务</span></div>
      <span class="ww-path-pill">HKLM\SYSTEM\ControlSet00x\Services</span>
      <span>服务与驱动的启动类型、镜像路径和账户配置。</span>
    </a>

    <a class="ww-path-card" href="registry-tree/hkcu/software/microsoft/windows/currentversion/userassist/">
      <div class="ww-card-line"><strong>UserAssist</strong><span class="ww-chip ww-chip--scenario">用户行为</span></div>
      <span class="ww-path-pill">HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist</span>
      <span>Explorer 介导的程序交互线索。</span>
    </a>

    <a class="ww-path-card" href="registry-tree/hkcu/software/microsoft/windows/currentversion/runmru/">
      <div class="ww-card-line"><strong>RunMRU</strong><span class="ww-chip ww-chip--scenario">用户行为</span></div>
      <span class="ww-path-pill">HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU</span>
      <span>运行对话框输入历史。</span>
    </a>

    <a class="ww-path-card" href="registry-tree/hklm/system/mounteddevices/">
      <div class="ww-card-line"><strong>MountedDevices</strong><span class="ww-chip ww-chip--hive">SYSTEM</span></div>
      <span class="ww-path-pill">HKLM\SYSTEM\MountedDevices</span>
      <span>卷 GUID、盘符和二进制设备标识映射。</span>
    </a>

    <a class="ww-path-card" href="registry-tree/hklm/system/controlset/control/session-manager/">
      <div class="ww-card-line"><strong>Session Manager</strong><span class="ww-chip ww-chip--hive">SYSTEM</span></div>
      <span class="ww-path-pill">HKLM\SYSTEM\ControlSet00x\Control\Session Manager</span>
      <span>启动阶段、兼容性缓存和会话初始化相关配置。</span>
    </a>

    <a class="ww-path-card" href="registry-tree/hklm/system/controlset/enum/usbstor/">
      <div class="ww-card-line"><strong>USBSTOR</strong><span class="ww-chip ww-chip--topic">设备</span></div>
      <span class="ww-path-pill">HKLM\SYSTEM\ControlSet00x\Enum\USBSTOR</span>
      <span>USB 存储设备枚举和实例线索。</span>
    </a>

    <a class="ww-path-card" href="registry-tree/hklm/system/controlset/control/timezone/">
      <div class="ww-card-line"><strong>TimeZoneInformation</strong><span class="ww-chip ww-chip--hive">SYSTEM</span></div>
      <span class="ww-path-pill">HKLM\SYSTEM\ControlSet00x\Control\TimeZoneInformation</span>
      <span>系统时区配置，适合与时间线解释交叉核对。</span>
    </a>
  </div>
</section>

<section class="ww-supplemental">
  <div class="ww-info-strip">
    <span><strong>注册表优先</strong> 路径页面解释 key / value。</span>
    <span><strong>场景辅助</strong> 取证场景页组织交叉验证。</span>
    <span><strong>补充层</strong> artifact 保留字段和工具细节。</span>
  </div>
</section>
