<section class="ww-shell">
  <div class="ww-compact-head">
    <p class="ww-hero-eyebrow">Registry Tree</p>
    <h1>按原生注册表树浏览</h1>
    <p>按 Windows 原生 root key 和 ControlSet / HKCU-HKU 映射查询注册表位置。</p>
  </div>

  <div class="ww-card-grid ww-card-grid--three ww-card-grid--entry">
    <a class="ww-feature-card" href="explorer/">
      <span class="ww-card-mark">EXP</span>
      <strong>Explorer</strong>
      <span>按关键词、Hive、主题和状态筛选结构化路径。</span>
      <em>Open →</em>
    </a>

    <a class="ww-feature-card" href="generated-index/">
      <span class="ww-card-mark">IDX</span>
      <strong>结构化索引</strong>
      <span>静态表格查看 data/registry 当前记录。</span>
      <em>Open →</em>
    </a>

    <a class="ww-feature-card" href="coverage/">
      <span class="ww-card-mark">COV</span>
      <strong>覆盖矩阵</strong>
      <span>维护用覆盖状态和下一阶段候选路径。</span>
      <em>Open →</em>
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
      <div class="ww-card-line"><strong>HKCR</strong><span class="ww-chip ww-chip--hive">classes</span></div>
      <span>文件关联、COM、协议处理器合并视图。</span>
      <small>Mapping: HKLM\Software\Classes + HKCU\Software\Classes</small>
      <div class="ww-card-chips"><span class="ww-chip ww-chip--topic">软件</span><span class="ww-chip ww-chip--topic">Shell</span><span class="ww-chip ww-chip--topic">COM</span></div>
    </a>

    <a class="ww-root-card" href="hkcu/">
      <div class="ww-card-line"><strong>HKCU</strong><span class="ww-chip ww-chip--hive">user</span></div>
      <span>当前用户配置视图，离线分析应定位具体用户 hive。</span>
      <small>Offline: NTUSER.DAT / UsrClass.dat</small>
      <div class="ww-card-chips"><span class="ww-chip ww-chip--topic">用户行为</span><span class="ww-chip ww-chip--topic">持久化</span><span class="ww-chip ww-chip--topic">网络</span></div>
    </a>

    <a class="ww-root-card" href="hklm/">
      <div class="ww-card-line"><strong>HKLM</strong><span class="ww-chip ww-chip--hive">machine</span></div>
      <span>机器级配置入口，包含 SYSTEM、SOFTWARE、SAM、SECURITY。</span>
      <small>Offline: SYSTEM / SOFTWARE / SAM / SECURITY</small>
      <div class="ww-card-chips"><span class="ww-chip ww-chip--topic">系统配置</span><span class="ww-chip ww-chip--topic">设备</span><span class="ww-chip ww-chip--topic">策略</span></div>
    </a>

    <a class="ww-root-card" href="hku/">
      <div class="ww-card-line"><strong>HKU</strong><span class="ww-chip ww-chip--hive">sid</span></div>
      <span>已加载用户 hive、服务账户 hive 和默认账户 hive。</span>
      <small>Offline: 需结合 SID 与用户目录解释</small>
      <div class="ww-card-chips"><span class="ww-chip ww-chip--topic">账户</span><span class="ww-chip ww-chip--topic">用户行为</span><span class="ww-chip ww-chip--topic">Shell</span></div>
    </a>

    <a class="ww-root-card" href="hkcc/">
      <div class="ww-card-line"><strong>HKCC</strong><span class="ww-chip ww-chip--hive">profile</span></div>
      <span>当前硬件配置映射，常用于系统环境解释。</span>
      <small>Mapping: HKLM\SYSTEM\...\Hardware Profiles\Current</small>
      <div class="ww-card-chips"><span class="ww-chip ww-chip--topic">硬件配置</span><span class="ww-chip ww-chip--topic">系统环境</span></div>
    </a>
  </div>
</section>

<section class="ww-section">
  <div class="ww-section-header">
    <span>Common Registry Areas</span>
    <h2>常用注册表区域</h2>
  </div>

  <div class="ww-card-grid ww-card-grid--paths">
    <a class="ww-path-card" href="hklm/system/">
      <div class="ww-card-line"><strong>HKLM\SYSTEM</strong><span class="ww-chip ww-chip--hive">SYSTEM</span></div>
      <span class="ww-path-pill">HKLM\SYSTEM</span>
      <span>ControlSet、服务、设备枚举、网络接口。</span>
    </a>

    <a class="ww-path-card" href="hklm/software/">
      <div class="ww-card-line"><strong>HKLM\SOFTWARE</strong><span class="ww-chip ww-chip--hive">SOFTWARE</span></div>
      <span class="ww-path-pill">HKLM\SOFTWARE</span>
      <span>机器级软件、策略和 Windows 配置。</span>
    </a>

    <a class="ww-path-card" href="hkcu/software/microsoft/windows/currentversion/explorer/">
      <div class="ww-card-line"><strong>HKCU CurrentVersion</strong><span class="ww-chip ww-chip--hive">HKCU</span></div>
      <span class="ww-path-pill">...\Windows\CurrentVersion</span>
      <span>Explorer、Run、RecentDocs、RunMRU。</span>
    </a>

    <a class="ww-path-card" href="hku/">
      <div class="ww-card-line"><strong>HKU\&lt;SID&gt;</strong><span class="ww-chip ww-chip--hive">HKU</span></div>
      <span class="ww-path-pill">HKEY_USERS\&lt;SID&gt;</span>
      <span>具体用户 hive 视图与 SID 语义。</span>
    </a>

    <a class="ww-path-card" href="hklm/system/controlset/">
      <div class="ww-card-line"><strong>ControlSet00x</strong><span class="ww-chip ww-chip--hive">SYSTEM</span></div>
      <span class="ww-path-pill">ControlSet00x</span>
      <span>结合 Select 解析 CurrentControlSet。</span>
    </a>
  </div>
</section>
