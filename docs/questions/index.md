<section class="ww-shell">
  <div class="ww-page-header ww-page-header--scenario">
    <p class="ww-hero-eyebrow">Scenario Playbooks</p>
    <h1>Investigate by scenario</h1>
    <p>按调查问题进入检查清单。场景页负责组织路径组合和交叉验证来源，主链接优先指向注册表位置页面。</p>
  </div>

  <a class="ww-start-card ww-start-card--wide" href="registry-checklist/">
    <span class="ww-card-mark">START</span>
    <span class="ww-card-kicker">Start here</span>
    <strong>常规注册表检查</strong>
    <span>第一次查看注册表时，从自启动、服务、设备、账户、策略和网络配置快速扫一遍。</span>
    <em>Open checklist →</em>
  </a>

  <div class="ww-chip-row ww-chip-row--filters">
    <a class="ww-chip ww-chip--scenario" href="execution/">Program Execution</a>
    <a class="ww-chip ww-chip--scenario" href="persistence/">Persistence</a>
    <a class="ww-chip ww-chip--scenario" href="shell-explorer/">User Activity</a>
    <a class="ww-chip ww-chip--scenario" href="usb/">USB</a>
    <a class="ww-chip ww-chip--scenario" href="rdp/">RDP</a>
    <a class="ww-chip ww-chip--scenario" href="accounts-security/">Accounts</a>
    <a class="ww-chip ww-chip--scenario" href="policy-security/">Security Policy</a>
    <a class="ww-chip ww-chip--scenario" href="network/">Network</a>
    <a class="ww-chip ww-chip--scenario" href="software-install/">Software</a>
    <a class="ww-chip ww-chip--scenario" href="anti-forensics/">Anti-forensics</a>
  </div>
</section>

<section class="ww-section">
  <div class="ww-card-grid ww-card-grid--scenarios">
    <a class="ww-scenario-card" href="execution/">
      <span class="ww-card-kicker">Program Execution</span>
      <strong>程序执行</strong>
      <span>确认哪些注册表线索可能说明程序存在、交互或执行。</span>
      <div class="ww-card-chips"><span class="ww-path-pill">UserAssist</span><span class="ww-path-pill">App Paths</span><span class="ww-path-pill">IFEO</span></div>
      <em>Open checklist →</em>
    </a>

    <a class="ww-scenario-card" href="shell-explorer/">
      <span class="ww-card-kicker">User Activity</span>
      <strong>Shell / Explorer 用户行为</strong>
      <span>查看 Explorer、文件对话框、运行框和最近文档相关痕迹。</span>
      <div class="ww-card-chips"><span class="ww-path-pill">RunMRU</span><span class="ww-path-pill">RecentDocs</span><span class="ww-path-pill">ComDlg32</span></div>
      <em>Open checklist →</em>
    </a>

    <a class="ww-scenario-card" href="persistence/">
      <span class="ww-card-kicker">Persistence</span>
      <strong>自启动与持久化</strong>
      <span>检查登录启动、服务、登录链和系统初始化配置。</span>
      <div class="ww-card-chips"><span class="ww-path-pill">Run Keys</span><span class="ww-path-pill">Services</span><span class="ww-path-pill">Winlogon</span></div>
      <em>Open checklist →</em>
    </a>

    <a class="ww-scenario-card" href="usb/">
      <span class="ww-card-kicker">Devices</span>
      <strong>USB 与外接设备</strong>
      <span>区分设备枚举、卷映射、用户见过卷和文件访问证据。</span>
      <div class="ww-card-chips"><span class="ww-path-pill">USBSTOR</span><span class="ww-path-pill">MountedDevices</span><span class="ww-path-pill">MountPoints2</span></div>
      <em>Open checklist →</em>
    </a>

    <a class="ww-scenario-card" href="rdp/">
      <span class="ww-card-kicker">Remote Access</span>
      <strong>RDP 与远程访问</strong>
      <span>检查 RDP 服务端配置、客户端历史、NLA 和防火墙线索。</span>
      <div class="ww-card-chips"><span class="ww-path-pill">Terminal Server</span><span class="ww-path-pill">RDP-Tcp</span><span class="ww-path-pill">CredSSP</span></div>
      <em>Open checklist →</em>
    </a>

    <a class="ww-scenario-card" href="accounts-security/">
      <span class="ww-card-kicker">Accounts</span>
      <strong>账户与安全</strong>
      <span>建立 SID / profile 映射，再检查登录界面、账户显示和凭据组件。</span>
      <div class="ww-card-chips"><span class="ww-path-pill">ProfileList</span><span class="ww-path-pill">SAM</span><span class="ww-path-pill">LogonUI</span></div>
      <em>Open checklist →</em>
    </a>

    <a class="ww-scenario-card" href="policy-security/">
      <span class="ww-card-kicker">Security Policy</span>
      <strong>安全策略与防护配置</strong>
      <span>区分注册表策略值、策略来源和实际生效状态。</span>
      <div class="ww-card-chips"><span class="ww-path-pill">Defender</span><span class="ww-path-pill">FirewallPolicy</span><span class="ww-path-pill">EventLog</span></div>
      <em>Open checklist →</em>
    </a>

    <a class="ww-scenario-card" href="network/">
      <span class="ww-card-kicker">Network</span>
      <strong>网络与系统环境</strong>
      <span>查看接口 IP/DNS/DHCP、网络 profile、代理、区域和时区线索。</span>
      <div class="ww-card-chips"><span class="ww-path-pill">Tcpip</span><span class="ww-path-pill">NetworkList</span><span class="ww-path-pill">ZoneMap</span></div>
      <em>Open checklist →</em>
    </a>

    <a class="ww-scenario-card" href="software-install/">
      <span class="ww-card-kicker">Software</span>
      <strong>软件安装与卸载</strong>
      <span>确认软件登记、应用路径、兼容性配置和用户侧交互线索。</span>
      <div class="ww-card-chips"><span class="ww-path-pill">Uninstall</span><span class="ww-path-pill">App Paths</span><span class="ww-path-pill">AppCompatFlags</span></div>
      <em>Open checklist →</em>
    </a>

    <a class="ww-scenario-card" href="anti-forensics/">
      <span class="ww-card-kicker">Anti-forensics</span>
      <strong>反取证与清理痕迹</strong>
      <span>检查防护策略、日志配置、删除队列和安全 hive 线索。</span>
      <div class="ww-card-chips"><span class="ww-path-pill">Defender</span><span class="ww-path-pill">EventLog</span><span class="ww-path-pill">PendingFileRename</span></div>
      <em>Open checklist →</em>
    </a>
  </div>
</section>

<section class="ww-supplemental">
  <div class="ww-section-header">
    <span>Supplemental</span>
    <h2>补充入口</h2>
  </div>

  <div class="ww-card-grid ww-card-grid--compact">
    <a class="ww-feature-card" href="../artifacts/"><strong>Artifact 补充索引</strong><span>字段语义、采集、误判和工具说明。</span><em>Open →</em></a>
    <a class="ww-feature-card" href="../registry-tree/generated-index/"><strong>结构化数据索引</strong><span>从 data/registry 生成的 registry entry 表。</span><em>Open →</em></a>
    <a class="ww-feature-card" href="../detection/"><strong>检测工程</strong><span>注册表路径组合、误报和验证思路。</span><em>Open →</em></a>
  </div>
</section>
