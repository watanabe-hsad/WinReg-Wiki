<section class="ww-page-header ww-page-header--scenario" markdown>
<p class="ww-hero-eyebrow">Scenario Directory</p>
<h1>按调查问题进入注册表线索</h1>
<p>场景页只组织检查顺序和证据边界。主链接仍优先指向注册表位置页面。</p>
</section>

<a class="ww-start-card" href="registry-checklist/">
  <span class="ww-card-kicker">Start here</span>
  <strong>常规注册表检查</strong>
  <span>第一次看注册表时，用一张清单扫自启动、服务、设备、账户、策略和网络配置。</span>
</a>

<div class="ww-card-grid ww-card-grid--scenarios" markdown>
<a class="ww-scenario-card" href="execution/">
  <strong>程序执行</strong>
  <span>确认哪些注册表线索可能说明程序存在、交互或执行。</span>
  <em>UserAssist · App Paths · Services · Command Processor</em>
</a>

<a class="ww-scenario-card" href="shell-explorer/">
  <strong>Shell / Explorer 用户行为</strong>
  <span>查看 Explorer、文件对话框、运行框和最近文档相关痕迹。</span>
  <em>UserAssist · RunMRU · RecentDocs · ComDlg32</em>
</a>

<a class="ww-scenario-card" href="persistence/">
  <strong>自启动与持久化</strong>
  <span>检查登录启动、服务、登录链和系统初始化配置。</span>
  <em>Run Keys · Services · Winlogon · Session Manager</em>
</a>

<a class="ww-scenario-card" href="usb/">
  <strong>USB 与外接设备</strong>
  <span>区分设备枚举、卷映射、用户见过卷和文件访问证据。</span>
  <em>USBSTOR · USB · MountedDevices · MountPoints2</em>
</a>

<a class="ww-scenario-card" href="rdp/">
  <strong>RDP 与远程访问</strong>
  <span>检查 RDP 服务端配置、客户端历史、NLA 和防火墙线索。</span>
  <em>Terminal Server · RDP-Tcp · CredSSP · MSTSC</em>
</a>

<a class="ww-scenario-card" href="accounts-security/">
  <strong>账户与安全</strong>
  <span>建立 SID / profile 映射，再检查登录界面、账户显示和凭据组件。</span>
  <em>ProfileList · SAM · HKU · Winlogon · LogonUI</em>
</a>

<a class="ww-scenario-card" href="policy-security/">
  <strong>安全策略与防护配置</strong>
  <span>区分注册表策略值、策略来源和实际生效状态。</span>
  <em>Policies · Defender · FirewallPolicy · EventLog</em>
</a>

<a class="ww-scenario-card" href="network/">
  <strong>网络与系统环境</strong>
  <span>查看接口 IP/DNS/DHCP、网络 profile、代理、区域和时区线索。</span>
  <em>Tcpip · NetworkList · Internet Settings · ZoneMap</em>
</a>

<a class="ww-scenario-card" href="software-install/">
  <strong>软件安装与卸载</strong>
  <span>确认软件登记、应用路径、兼容性配置和用户侧交互线索。</span>
  <em>Uninstall · App Paths · AppCompatFlags · UserAssist</em>
</a>

<a class="ww-scenario-card" href="anti-forensics/">
  <strong>反取证与清理痕迹</strong>
  <span>检查防护策略、日志配置、删除队列和安全 hive 线索。</span>
  <em>Defender · EventLog · SECURITY · PendingFileRename</em>
</a>
</div>

<section class="ww-supplemental" markdown>
<div class="ww-section-header" markdown>
<span>Supplemental</span>
<h2>补充入口</h2>
</div>

<div class="ww-card-grid ww-card-grid--compact" markdown>
<a class="ww-feature-card" href="../artifacts/"><strong>Artifact 补充索引</strong><span>字段语义、采集、误判和工具说明。</span></a>
<a class="ww-feature-card" href="../artifacts/generated-index/"><strong>结构化 artifact 数据</strong><span>从 `data/artifacts/*.yml` 生成的维护表格。</span></a>
<a class="ww-feature-card" href="../registry-tree/generated-index/"><strong>结构化注册表索引</strong><span>从 `data/registry/*.yml` 生成的 registry 入口。</span></a>
<a class="ww-feature-card" href="../detection/"><strong>检测工程</strong><span>注册表路径组合、误报和验证思路。</span></a>
</div>
</section>
