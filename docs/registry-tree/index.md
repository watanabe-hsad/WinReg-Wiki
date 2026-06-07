<section class="ww-shell">
  <div class="ww-page-header ww-page-header--registry">
    <p class="ww-hero-eyebrow">Registry Tree</p>
    <h1>Browse by native registry tree</h1>
    <p>按 Windows 原生 root key 和 live/offline 映射浏览注册表位置。进入具体页面后再查看 key / value 含义、常见状态和注意事项。</p>
  </div>

  <div class="ww-card-grid ww-card-grid--three">
    <a class="ww-feature-card ww-feature-card--primary" href="explorer/">
      <span class="ww-card-mark">EXP</span>
      <span class="ww-card-kicker">Filter database</span>
      <strong>Open Registry Explorer</strong>
      <span>按关键词、Hive、主题和状态筛选结构化 registry entry。</span>
      <em>Browse →</em>
    </a>

    <a class="ww-feature-card" href="generated-index/">
      <span class="ww-card-mark">IDX</span>
      <span class="ww-card-kicker">Generated index</span>
      <strong>Structured Index</strong>
      <span>由 data/registry 生成的路径索引，适合快速扫当前已结构化条目。</span>
      <em>Open →</em>
    </a>

    <a class="ww-feature-card" href="coverage/">
      <span class="ww-card-mark">COV</span>
      <span class="ww-card-kicker">Maintenance</span>
      <strong>Coverage Matrix</strong>
      <span>查看当前覆盖范围、记录状态和下一阶段待补路径。</span>
      <em>Review →</em>
    </a>
  </div>
</section>

<section class="ww-section">
  <div class="ww-section-header">
    <span>Root keys</span>
    <h2>按原生根键进入</h2>
  </div>

  <div class="ww-card-grid ww-card-grid--roots">
    <a class="ww-root-card" href="hkcr/">
      <span class="ww-chip ww-chip--hive">HKCR</span>
      <strong>HKEY_CLASSES_ROOT</strong>
      <span>文件关联、COM、协议处理器的合并视图。</span>
      <small>Mapping: HKLM\Software\Classes + HKCU\Software\Classes</small>
      <em>软件 · Shell · COM</em>
    </a>

    <a class="ww-root-card" href="hkcu/">
      <span class="ww-chip ww-chip--hive">HKCU</span>
      <strong>HKEY_CURRENT_USER</strong>
      <span>当前用户配置视图。离线分析应定位具体用户 hive。</span>
      <small>Offline: C:\Users\&lt;User&gt;\NTUSER.DAT / UsrClass.dat</small>
      <em>用户行为 · 持久化 · 网络</em>
    </a>

    <a class="ww-root-card" href="hklm/">
      <span class="ww-chip ww-chip--hive">HKLM</span>
      <strong>HKEY_LOCAL_MACHINE</strong>
      <span>机器级配置入口，包含 SYSTEM、SOFTWARE、SAM、SECURITY 等 hive。</span>
      <small>Offline: SYSTEM / SOFTWARE / SAM / SECURITY</small>
      <em>系统配置 · 策略 · 设备</em>
    </a>

    <a class="ww-root-card" href="hku/">
      <span class="ww-chip ww-chip--hive">HKU</span>
      <strong>HKEY_USERS</strong>
      <span>已加载用户 hive、服务账户 hive 和默认账户 hive。</span>
      <small>Offline: NTUSER.DAT / UsrClass.dat，需确认 SID 语义</small>
      <em>账户 · 用户行为 · Shell</em>
    </a>

    <a class="ww-root-card" href="hkcc/">
      <span class="ww-chip ww-chip--hive">HKCC</span>
      <strong>HKEY_CURRENT_CONFIG</strong>
      <span>当前硬件配置映射，通常用于系统环境和硬件配置解释。</span>
      <small>Mapping: HKLM\SYSTEM\CurrentControlSet\Hardware Profiles\Current</small>
      <em>硬件配置 · 系统环境</em>
    </a>
  </div>
</section>

<section class="ww-section">
  <div class="ww-section-header">
    <span>Browse by topic</span>
    <h2>按主题快速定位</h2>
  </div>

  <div class="ww-chip-row ww-chip-row--filters">
    <span class="ww-chip ww-chip--topic">系统配置</span>
    <span class="ww-chip ww-chip--topic">用户行为</span>
    <span class="ww-chip ww-chip--topic">持久化</span>
    <span class="ww-chip ww-chip--topic">网络</span>
    <span class="ww-chip ww-chip--topic">账户</span>
    <span class="ww-chip ww-chip--topic">设备</span>
    <span class="ww-chip ww-chip--topic">策略</span>
    <span class="ww-chip ww-chip--topic">软件</span>
  </div>
</section>

<section class="ww-section">
  <div class="ww-section-header">
    <span>Common Registry Areas</span>
    <h2>常用注册表区域</h2>
  </div>

  <div class="ww-card-grid ww-card-grid--paths">
    <a class="ww-path-card" href="hklm/system/">
      <span class="ww-chip ww-chip--hive">HKLM</span>
      <strong>HKLM\SYSTEM</strong>
      <span>ControlSet、服务、设备枚举、网络接口和系统控制配置。</span>
      <em>SYSTEM hive</em>
    </a>

    <a class="ww-path-card" href="hklm/software/">
      <span class="ww-chip ww-chip--hive">HKLM</span>
      <strong>HKLM\SOFTWARE</strong>
      <span>机器级软件、策略、Windows CurrentVersion 和登录相关配置。</span>
      <em>SOFTWARE hive</em>
    </a>

    <a class="ww-path-card" href="hkcu/software/microsoft/windows/currentversion/explorer/">
      <span class="ww-chip ww-chip--hive">HKCU</span>
      <strong>HKCU\Software\Microsoft\Windows\CurrentVersion</strong>
      <span>用户级 Explorer、Run、RecentDocs、RunMRU、ComDlg32 等位置。</span>
      <em>NTUSER.DAT</em>
    </a>

    <a class="ww-path-card" href="hku/">
      <span class="ww-chip ww-chip--hive">HKU</span>
      <strong>HKU\&lt;SID&gt;</strong>
      <span>具体用户 hive 视图，解释前应确认 SID 是否代表真实交互用户。</span>
      <em>用户 hive</em>
    </a>

    <a class="ww-path-card" href="hklm/system/controlset/">
      <span class="ww-chip ww-chip--hive">SYSTEM</span>
      <strong>ControlSet00x</strong>
      <span>离线分析时应结合 HKLM\SYSTEM\Select 解析 CurrentControlSet。</span>
      <em>ControlSet 映射</em>
    </a>
  </div>
</section>
