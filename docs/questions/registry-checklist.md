# 常规注册表检查

<section class="ww-page-header ww-page-header--checklist">
  <p class="ww-hero-eyebrow">Registry Checklist</p>
  <h1>第一次检查注册表时看哪里</h1>
  <p>按主题扫关键路径。每一项只说明检查目标、注册表位置、关注字段和交叉验证来源。</p>
</section>

<div class="ww-chip-row ww-chip-row--filters">
  <a class="ww-chip ww-chip--topic" href="#persistence">启动与持久化</a>
  <a class="ww-chip ww-chip--topic" href="#execution">程序执行</a>
  <a class="ww-chip ww-chip--topic" href="#user-activity">用户行为</a>
  <a class="ww-chip ww-chip--topic" href="#devices">USB / 设备</a>
  <a class="ww-chip ww-chip--topic" href="#rdp">RDP / 远程访问</a>
  <a class="ww-chip ww-chip--topic" href="#accounts">账户 / 登录</a>
  <a class="ww-chip ww-chip--topic" href="#security-policy">安全策略</a>
  <a class="ww-chip ww-chip--topic" href="#network">网络</a>
</div>

<section class="ww-check-section" id="persistence">
  <div class="ww-section-header"><span>Persistence</span><h2>启动与持久化</h2></div>
  <div class="ww-check-grid">
    <article class="ww-check-card"><strong>机器级登录启动</strong><a class="ww-path-pill" href="../registry-tree/hklm/software/microsoft/windows/currentversion/run/">HKLM Run / RunOnce</a><dl><div><dt>关注字段</dt><dd>value name、value data、WOW6432Node</dd></div><div><dt>交叉验证</dt><dd>登录事件、进程创建、Prefetch、BAM / DAM、EDR</dd></div></dl></article>
    <article class="ww-check-card"><strong>用户级登录启动</strong><a class="ww-path-pill" href="../registry-tree/hkcu/software/microsoft/windows/currentversion/run/">HKCU Run / RunOnce</a><dl><div><dt>关注字段</dt><dd>value name、value data、用户 SID</dd></div><div><dt>交叉验证</dt><dd>用户登录事件、StartupApproved、Prefetch、EDR</dd></div></dl></article>
    <article class="ww-check-card"><strong>服务和驱动</strong><a class="ww-path-pill" href="../registry-tree/hklm/system/controlset/services/">Services</a><dl><div><dt>关注字段</dt><dd>ImagePath、Type、Start、ObjectName</dd></div><div><dt>交叉验证</dt><dd>System.evtx、Service Control Manager、Autoruns、签名</dd></div></dl></article>
    <article class="ww-check-card"><strong>登录链</strong><a class="ww-path-pill" href="../registry-tree/hklm/software/microsoft/windows-nt/currentversion/winlogon/">Winlogon</a><dl><div><dt>关注字段</dt><dd>Userinit、Shell、AutoAdminLogon、Notify</dd></div><div><dt>交叉验证</dt><dd>Security.evtx、SAM、ProfileList、Autoruns</dd></div></dl></article>
    <article class="ww-check-card"><strong>Session Manager</strong><a class="ww-path-pill" href="../registry-tree/hklm/system/controlset/control/session-manager/">Session Manager</a><dl><div><dt>关注字段</dt><dd>BootExecute、AppCertDlls、SubSystems</dd></div><div><dt>交叉验证</dt><dd>重启时间线、模块加载、同版本基线</dd></div></dl></article>
    <article class="ww-check-card"><strong>文件删除队列</strong><a class="ww-path-pill" href="../registry-tree/hklm/system/controlset/control/session-manager/pending-file-rename-operations/">PendingFileRenameOperations</a><dl><div><dt>关注字段</dt><dd>待重命名 / 删除路径</dd></div><div><dt>交叉验证</dt><dd>重启记录、文件系统时间线、$UsnJrnl</dd></div></dl></article>
  </div>
</section>

<section class="ww-check-section" id="execution">
  <div class="ww-section-header"><span>Execution</span><h2>程序执行</h2></div>
  <div class="ww-check-grid">
    <article class="ww-check-card"><strong>Explorer 交互</strong><a class="ww-path-pill" href="../registry-tree/hkcu/software/microsoft/windows/currentversion/userassist/">UserAssist</a><dl><div><dt>关注字段</dt><dd>ROT13 条目、计数、时间字段</dd></div><div><dt>交叉验证</dt><dd>Prefetch、Amcache、BAM / DAM、LNK、EDR</dd></div></dl></article>
    <article class="ww-check-card"><strong>应用路径注册</strong><a class="ww-path-pill" href="../registry-tree/hklm/software/microsoft/windows/currentversion/app-paths/">App Paths</a><dl><div><dt>关注字段</dt><dd>可执行文件名、默认路径、Path</dd></div><div><dt>交叉验证</dt><dd>文件系统、安装记录、进程创建</dd></div></dl></article>
    <article class="ww-check-card"><strong>命令处理器</strong><a class="ww-path-pill" href="../registry-tree/hkcu/software/microsoft/command-processor/">Command Processor</a><dl><div><dt>关注字段</dt><dd>AutoRun、扩展、补全配置</dd></div><div><dt>交叉验证</dt><dd>进程创建、命令行日志、PowerShell / Sysmon</dd></div></dl></article>
    <article class="ww-check-card"><strong>IFEO</strong><a class="ww-path-pill" href="../registry-tree/hklm/software/microsoft/windows-nt/currentversion/ifeo/">Image File Execution Options</a><dl><div><dt>关注字段</dt><dd>Debugger、SilentProcessExit 相关值</dd></div><div><dt>交叉验证</dt><dd>进程创建、调试器路径、开发工具和 EDR 基线</dd></div></dl></article>
  </div>
</section>

<section class="ww-check-section" id="user-activity">
  <div class="ww-section-header"><span>User Activity</span><h2>用户行为</h2></div>
  <div class="ww-check-grid">
    <article class="ww-check-card"><strong>运行框输入</strong><a class="ww-path-pill" href="../registry-tree/hkcu/software/microsoft/windows/currentversion/runmru/">RunMRU</a><dl><div><dt>关注字段</dt><dd>MRUList、命令字符串</dd></div><div><dt>交叉验证</dt><dd>进程创建、Shell 事件、用户上下文</dd></div></dl></article>
    <article class="ww-check-card"><strong>最近文档</strong><a class="ww-path-pill" href="../registry-tree/hkcu/software/microsoft/windows/currentversion/recentdocs/">RecentDocs</a><dl><div><dt>关注字段</dt><dd>MRU 顺序、文件名</dd></div><div><dt>交叉验证</dt><dd>LNK、Jump Lists、文件系统</dd></div></dl></article>
    <article class="ww-check-card"><strong>文件对话框</strong><a class="ww-path-pill" href="../registry-tree/hkcu/software/microsoft/windows/currentversion/comdlg32/">ComDlg32</a><dl><div><dt>关注字段</dt><dd>OpenSavePidlMRU、LastVisitedPidlMRU</dd></div><div><dt>交叉验证</dt><dd>LNK、Jump Lists、ShellBags</dd></div></dl></article>
    <article class="ww-check-card"><strong>用户级策略</strong><a class="ww-path-pill" href="../registry-tree/hkcu/software/microsoft/windows/currentversion/policies/">HKCU Policies</a><dl><div><dt>关注字段</dt><dd>Explorer 限制、驱动器显示、控制面板限制</dd></div><div><dt>交叉验证</dt><dd>GPO / MDM、用户 SID、Shell 行为</dd></div></dl></article>
  </div>
</section>

<section class="ww-check-section" id="devices">
  <div class="ww-section-header"><span>Devices</span><h2>USB / 设备</h2></div>
  <div class="ww-check-grid">
    <article class="ww-check-card"><strong>USB 存储</strong><a class="ww-path-pill" href="../registry-tree/hklm/system/controlset/enum/usbstor/">USBSTOR</a><dl><div><dt>关注字段</dt><dd>设备类型、厂商、产品、实例 ID、FriendlyName</dd></div><div><dt>交叉验证</dt><dd>SetupAPI.dev.log、Partition/Diagnostic、LNK、Jump Lists</dd></div></dl></article>
    <article class="ww-check-card"><strong>USB 总线</strong><a class="ww-path-pill" href="../registry-tree/hklm/system/controlset/enum/usb/">USB</a><dl><div><dt>关注字段</dt><dd>VID/PID、实例 ID、ContainerID</dd></div><div><dt>交叉验证</dt><dd>USBSTOR、DeviceClasses、SetupAPI.dev.log</dd></div></dl></article>
    <article class="ww-check-card"><strong>卷和盘符</strong><a class="ww-path-pill" href="../registry-tree/hklm/system/mounteddevices/">MountedDevices</a><dl><div><dt>关注字段</dt><dd>\DosDevices\&lt;letter&gt;:、Volume GUID</dd></div><div><dt>交叉验证</dt><dd>USBSTOR、MountPoints2、卷 GUID、文件系统</dd></div></dl></article>
    <article class="ww-check-card"><strong>用户见过的卷</strong><a class="ww-path-pill" href="../registry-tree/hkcu/software/microsoft/windows/currentversion/mountpoints2/">MountPoints2</a><dl><div><dt>关注字段</dt><dd>Volume GUID、网络共享、用户 SID</dd></div><div><dt>交叉验证</dt><dd>LNK、Jump Lists、ShellBags、文件访问记录</dd></div></dl></article>
  </div>
</section>

<section class="ww-check-section" id="rdp">
  <div class="ww-section-header"><span>Remote Access</span><h2>RDP / 远程访问</h2></div>
  <div class="ww-check-grid">
    <article class="ww-check-card"><strong>RDP 服务端开关</strong><a class="ww-path-pill" href="../registry-tree/hklm/system/controlset/control/terminal-server/">Terminal Server</a><dl><div><dt>关注字段</dt><dd>fDenyTSConnections</dd></div><div><dt>交叉验证</dt><dd>TerminalServices 日志、防火墙、监听端口</dd></div></dl></article>
    <article class="ww-check-card"><strong>RDP listener</strong><a class="ww-path-pill" href="../registry-tree/hklm/system/controlset/control/terminal-server/rdp-tcp/">RDP-Tcp</a><dl><div><dt>关注字段</dt><dd>PortNumber、NLA、安全层</dd></div><div><dt>交叉验证</dt><dd>TerminalServices、Security.evtx、端口监听</dd></div></dl></article>
    <article class="ww-check-card"><strong>CredSSP</strong><a class="ww-path-pill" href="../registry-tree/hklm/system/controlset/control/terminal-server/credssp/">CredSSP</a><dl><div><dt>关注字段</dt><dd>NLA / 认证兼容性策略</dd></div><div><dt>交叉验证</dt><dd>组策略、连接事件、客户端配置</dd></div></dl></article>
    <article class="ww-check-card"><strong>RDP 客户端</strong><a class="ww-path-pill" href="../registry-tree/hkcu/software/microsoft/terminal-server-client/">Terminal Server Client</a><dl><div><dt>关注字段</dt><dd>Servers、Default、MRU 项</dd></div><div><dt>交叉验证</dt><dd>Jump Lists、LNK、RDP 缓存、用户上下文</dd></div></dl></article>
  </div>
</section>

<section class="ww-check-section" id="accounts">
  <div class="ww-section-header"><span>Accounts</span><h2>账户 / 登录</h2></div>
  <div class="ww-check-grid">
    <article class="ww-check-card"><strong>用户映射</strong><a class="ww-path-pill" href="../registry-tree/hklm/software/microsoft/windows-nt/currentversion/profilelist/">ProfileList</a><dl><div><dt>关注字段</dt><dd>SID、ProfileImagePath、.bak、State</dd></div><div><dt>交叉验证</dt><dd>SAM、域账户、Security.evtx、用户目录</dd></div></dl></article>
    <article class="ww-check-card"><strong>当前用户 hive</strong><a class="ww-path-pill" href="../registry-tree/hku/">HKEY_USERS</a><dl><div><dt>关注字段</dt><dd>SID、加载状态、用户 hive 文件</dd></div><div><dt>交叉验证</dt><dd>ProfileList、用户目录、登录事件</dd></div></dl></article>
    <article class="ww-check-card"><strong>登录界面</strong><a class="ww-path-pill" href="../registry-tree/hklm/software/microsoft/windows/currentversion/authentication/logonui/">LogonUI</a><dl><div><dt>关注字段</dt><dd>最近用户 / SID 显示线索</dd></div><div><dt>交叉验证</dt><dd>Security.evtx、ProfileList、域日志</dd></div></dl></article>
    <article class="ww-check-card"><strong>凭据组件</strong><a class="ww-path-pill" href="../registry-tree/hklm/software/microsoft/windows/currentversion/authentication/credential-providers/">Credential Providers</a><dl><div><dt>关注字段</dt><dd>Provider / Filter CLSID</dd></div><div><dt>交叉验证</dt><dd>安装软件、签名、LogonUI、EDR</dd></div></dl></article>
  </div>
</section>

<section class="ww-check-section" id="security-policy">
  <div class="ww-section-header"><span>Policy</span><h2>安全策略</h2></div>
  <div class="ww-check-grid">
    <article class="ww-check-card"><strong>Defender 策略</strong><a class="ww-path-pill" href="../registry-tree/hklm/software/policies/microsoft/windows-defender/">Defender Policies</a><dl><div><dt>关注字段</dt><dd>Disable*、排除项、实时防护相关值</dd></div><div><dt>交叉验证</dt><dd>Defender Operational、Tamper Protection、GPO / MDM</dd></div></dl></article>
    <article class="ww-check-card"><strong>防火墙配置</strong><a class="ww-path-pill" href="../registry-tree/hklm/system/controlset/services/sharedaccess/firewallpolicy/">FirewallPolicy</a><dl><div><dt>关注字段</dt><dd>profile、规则、默认入站 / 出站动作</dd></div><div><dt>交叉验证</dt><dd>Firewall 日志、ActiveStore、GPO / MDM、网络流量</dd></div></dl></article>
    <article class="ww-check-card"><strong>事件日志配置</strong><a class="ww-path-pill" href="../registry-tree/hklm/system/controlset/services/eventlog/">EventLog</a><dl><div><dt>关注字段</dt><dd>File、MaxSize、Retention、AutoBackupLogFiles</dd></div><div><dt>交叉验证</dt><dd>实际 .evtx 文件、EventLog 服务、日志截断线索</dd></div></dl></article>
    <article class="ww-check-card"><strong>LSA</strong><a class="ww-path-pill" href="../registry-tree/hklm/system/controlset/control/lsa/">LSA</a><dl><div><dt>关注字段</dt><dd>认证包、安全包、LSASS 保护相关值</dd></div><div><dt>交叉验证</dt><dd>LSASS 模块、签名、Security.evtx、EDR</dd></div></dl></article>
  </div>
</section>

<section class="ww-check-section" id="network">
  <div class="ww-section-header"><span>Network</span><h2>网络</h2></div>
  <div class="ww-check-grid">
    <article class="ww-check-card"><strong>网络接口</strong><a class="ww-path-pill" href="../registry-tree/hklm/system/controlset/services/tcpip/parameters/interfaces/">Tcpip Interfaces</a><dl><div><dt>关注字段</dt><dd>EnableDHCP、IP、DNS、网关、租约时间</dd></div><div><dt>交叉验证</dt><dd>NetworkList、DHCP / DNS 日志、防火墙、EDR 网络</dd></div></dl></article>
    <article class="ww-check-card"><strong>网络配置文件</strong><a class="ww-path-pill" href="../registry-tree/hklm/software/microsoft/windows-nt/currentversion/networklist/profiles/">NetworkList Profiles</a><dl><div><dt>关注字段</dt><dd>ProfileName、Category、DateCreated、DateLastConnected</dd></div><div><dt>交叉验证</dt><dd>WLAN / DHCP 日志、网络连接时间线</dd></div></dl></article>
    <article class="ww-check-card"><strong>代理配置</strong><a class="ww-path-pill" href="../registry-tree/hkcu/software/microsoft/windows/currentversion/internet-settings/">Internet Settings</a><dl><div><dt>关注字段</dt><dd>ProxyEnable、ProxyServer、AutoConfigURL</dd></div><div><dt>交叉验证</dt><dd>浏览器设置、WinINet 程序、代理日志、EDR 网络</dd></div></dl></article>
    <article class="ww-check-card"><strong>安全区域</strong><a class="ww-path-pill" href="../registry-tree/hkcu/software/microsoft/windows/currentversion/internet-settings/zonemap/">ZoneMap</a><dl><div><dt>关注字段</dt><dd>Domains、Ranges、区域编号</dd></div><div><dt>交叉验证</dt><dd>浏览器策略、GPO / MDM、访问日志</dd></div></dl></article>
  </div>
</section>

## 常见误读

- Run key、Services、Winlogon、LSA 只能先证明配置存在；是否执行或加载要另证。
- `USBSTOR`、`MountedDevices`、`MountPoints2` 分别回答不同层面的问题，不能互相替代。
- Defender、Firewall、Audit Policy 注册表值可能来自 GPO、MDM、安全产品或本地管理操作。
- key LastWrite 是 key 级变化时间，不是某个 value 的独立创建时间。
