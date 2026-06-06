# 取证场景

<p class="ww-lede">按调查问题进入，但主路径仍是“场景 -> 注册表位置”。先确认 key / value 是什么，再用日志、文件系统和工具输出交叉验证。</p>

<div class="ww-entry-grid ww-entry-grid--scenarios" markdown>

<a class="ww-entry-card ww-entry-card--accent" href="registry-checklist/">
  <span class="ww-entry-kicker">Start Here</span>
  <strong>常规注册表检查</strong>
  <span>第一次看注册表时优先检查的自启动、服务、设备、账户和策略路径。</span>
</a>

<a class="ww-entry-card" href="execution/">
  <strong>程序执行</strong>
  <span>UserAssist、Command Processor、App Paths、Services/BAM、Drivers 等。</span>
</a>

<a class="ww-entry-card" href="persistence/">
  <strong>自启动与持久化</strong>
  <span>Run Keys、Services、Winlogon、LSA、Session Manager、IFEO。</span>
</a>

<a class="ww-entry-card" href="usb/">
  <strong>USB 与外接设备</strong>
  <span>USBSTOR、USB、SWD\WPDBUSENUM、MountedDevices、MountPoints2。</span>
</a>

<a class="ww-entry-card" href="shell-explorer/">
  <strong>Shell / Explorer 用户行为</strong>
  <span>UserAssist、RunMRU、RecentDocs、ComDlg32、MountPoints2。</span>
</a>

<a class="ww-entry-card" href="rdp/">
  <strong>RDP 与远程访问</strong>
  <span>Terminal Server Client、Terminal Server、RDP-Tcp、CredSSP、防火墙。</span>
</a>

<a class="ww-entry-card" href="accounts-security/">
  <strong>账户与安全</strong>
  <span>ProfileList、SAM、HKEY_USERS、Winlogon、LogonUI、Credential Providers。</span>
</a>

<a class="ww-entry-card" href="policy-security/">
  <strong>安全策略与防护配置</strong>
  <span>Policies、Defender、FirewallPolicy、EventLog、LSA、UAC。</span>
</a>

<a class="ww-entry-card" href="network/">
  <strong>网络与系统环境</strong>
  <span>Tcpip Interfaces、NetworkList、Internet Settings、ZoneMap、TimeZone。</span>
</a>

<a class="ww-entry-card" href="software-install/">
  <strong>软件安装与卸载</strong>
  <span>Uninstall、App Paths、AppCompatFlags、SOFTWARE、UserAssist。</span>
</a>

<a class="ww-entry-card" href="anti-forensics/">
  <strong>反取证与清理痕迹</strong>
  <span>Defender Policies、EventLog、SECURITY、PendingFileRenameOperations。</span>
</a>

</div>

## 补充入口

| 入口 | 内容 |
|---|---|
| [Artifact 补充索引](../artifacts/index.md) | artifact 级字段语义、采集、误报和工具说明；不是主要阅读入口。 |
| [结构化 artifact 数据索引](../artifacts/generated-index.md) | 从 `data/artifacts/*.yml` 生成的内部数据表格。 |
| [结构化注册表索引](../registry-tree/generated-index.md) | 从 `data/registry/*.yml` 生成的 registry 试点索引。 |
| [检测工程](../detection/index.md) | 注册表检测规则的路径组合、误报和验证思路。 |

## 判断顺序

1. 先确认路径归属：root key、hive、SID、ControlSet、32/64 位视图。
2. 再解释证据语义：配置存在、设备枚举、用户交互、程序存在或策略值存在。
3. 然后用日志、文件系统、工具输出和时间线交叉验证。
4. 最后写清楚证据边界，避免把弱线索写成定案。
