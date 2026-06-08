<section class="ww-shell">
  <div class="ww-compact-head">
    <p class="ww-hero-eyebrow">SCENARIO PLAYBOOKS</p>
    <h1>按取证场景查询</h1>
    <p>按调查问题进入检查清单；主链接优先指向注册表位置页面。</p>
  </div>

  <a class="ww-start-card ww-start-card--wide" href="registry-checklist/">
    <span class="ww-card-mark">START</span>
    <strong>常规注册表检查</strong>
    <span>从自启动、服务、设备、账户、策略和网络配置快速扫一遍。</span>
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
      <div class="ww-card-line"><strong>程序执行</strong><span>Program Execution</span></div>
      <p>程序存在、交互或执行相关线索。</p>
      <div class="ww-card-chips"><span class="ww-path-pill">UserAssist</span><span class="ww-path-pill">App Paths</span><span class="ww-path-pill">IFEO</span></div>
      <em>Open checklist →</em>
    </a>

    <a class="ww-scenario-card" href="shell-explorer/">
      <div class="ww-card-line"><strong>Shell / Explorer 用户行为</strong><span>User Activity</span></div>
      <p>Explorer、运行框、最近文档和文件对话框。</p>
      <div class="ww-card-chips"><span class="ww-path-pill">RunMRU</span><span class="ww-path-pill">RecentDocs</span><span class="ww-path-pill">ComDlg32</span></div>
      <em>Open checklist →</em>
    </a>

    <a class="ww-scenario-card" href="persistence/">
      <div class="ww-card-line"><strong>自启动与持久化</strong><span>Persistence</span></div>
      <p>登录启动、服务、登录链和系统初始化配置。</p>
      <div class="ww-card-chips"><span class="ww-path-pill">Run Keys</span><span class="ww-path-pill">Services</span><span class="ww-path-pill">Winlogon</span></div>
      <em>Open checklist →</em>
    </a>

    <a class="ww-scenario-card" href="usb/">
      <div class="ww-card-line"><strong>USB 与外接设备</strong><span>Devices</span></div>
      <p>设备枚举、卷映射和用户见过的卷。</p>
      <div class="ww-card-chips"><span class="ww-path-pill">USBSTOR</span><span class="ww-path-pill">MountedDevices</span><span class="ww-path-pill">MountPoints2</span></div>
      <em>Open checklist →</em>
    </a>

    <a class="ww-scenario-card" href="rdp/">
      <div class="ww-card-line"><strong>RDP 与远程访问</strong><span>Remote Access</span></div>
      <p>RDP 服务端、客户端历史、NLA 和防火墙线索。</p>
      <div class="ww-card-chips"><span class="ww-path-pill">Terminal Server</span><span class="ww-path-pill">RDP-Tcp</span><span class="ww-path-pill">CredSSP</span></div>
      <em>Open checklist →</em>
    </a>

    <a class="ww-scenario-card" href="accounts-security/">
      <div class="ww-card-line"><strong>账户与安全</strong><span>Accounts</span></div>
      <p>SID / profile 映射、登录界面和凭据组件。</p>
      <div class="ww-card-chips"><span class="ww-path-pill">ProfileList</span><span class="ww-path-pill">SAM</span><span class="ww-path-pill">LogonUI</span></div>
      <em>Open checklist →</em>
    </a>

    <a class="ww-scenario-card" href="policy-security/">
      <div class="ww-card-line"><strong>安全策略与防护配置</strong><span>Security Policy</span></div>
      <p>策略值、策略来源和实际生效状态。</p>
      <div class="ww-card-chips"><span class="ww-path-pill">Defender</span><span class="ww-path-pill">FirewallPolicy</span><span class="ww-path-pill">EventLog</span></div>
      <em>Open checklist →</em>
    </a>

    <a class="ww-scenario-card" href="network/">
      <div class="ww-card-line"><strong>网络与系统环境</strong><span>Network</span></div>
      <p>接口 IP / DNS / DHCP、网络 profile、代理和区域。</p>
      <div class="ww-card-chips"><span class="ww-path-pill">Tcpip</span><span class="ww-path-pill">NetworkList</span><span class="ww-path-pill">ZoneMap</span></div>
      <em>Open checklist →</em>
    </a>

    <a class="ww-scenario-card" href="software-install/">
      <div class="ww-card-line"><strong>软件安装与卸载</strong><span>Software</span></div>
      <p>软件登记、应用路径、兼容性配置和用户侧交互。</p>
      <div class="ww-card-chips"><span class="ww-path-pill">Uninstall</span><span class="ww-path-pill">App Paths</span><span class="ww-path-pill">AppCompatFlags</span></div>
      <em>Open checklist →</em>
    </a>

    <a class="ww-scenario-card" href="anti-forensics/">
      <div class="ww-card-line"><strong>反取证与清理痕迹</strong><span>Anti-forensics</span></div>
      <p>防护策略、日志配置、删除队列和安全 hive 线索。</p>
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

  <div class="ww-info-strip">
    <a href="../artifacts/"><strong>Artifact 补充索引</strong><span>字段语义、采集、误读和工具说明。</span></a>
    <a href="../registry-tree/generated-index/"><strong>结构化数据索引</strong><span>data/registry 生成的 registry entry 表。</span></a>
    <a href="../detection/"><strong>检测工程</strong><span>路径组合、误报和验证思路。</span></a>
  </div>
</section>
