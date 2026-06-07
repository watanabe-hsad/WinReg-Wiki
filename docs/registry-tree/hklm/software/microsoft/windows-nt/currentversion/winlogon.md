# HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon

<div class="ww-fact-card" markdown>
<div class="ww-fact-card__top">
<div><span class="ww-card-kicker">Registry Fact Card</span><strong>HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon</strong></div>
<span class="ww-badge ww-badge--status">stable / high</span>
</div>
<div class="ww-fact-grid" markdown>
<div><span>Root</span><span class="ww-badge ww-badge--hive">HKLM</span></div>
<div><span>Hive</span><span class="ww-badge ww-badge--hive">SOFTWARE</span></div>
<div><span>Offline file</span><strong>C:\Windows\System32\Config\SOFTWARE</strong></div>
<div class="ww-fact-wide"><span>Native path</span><div class="ww-path-stack"><span class="ww-path-pill">HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon</span></div></div>
</div>
<div class="ww-fact-footer">
<div><span>Topics</span><span class="ww-chip ww-chip--topic">持久化</span><span class="ww-chip ww-chip--topic">账户</span></div>
<div><span>Scenarios</span><span class="ww-chip ww-chip--scenario">自启动与持久化</span><span class="ww-chip ww-chip--scenario">账户与安全</span><span class="ww-chip ww-chip--scenario">常规注册表检查</span></div>
<div><span>Related data</span><span class="ww-chip ww-chip--data">data/registry: hklm-software-winlogon</span><span class="ww-chip ww-chip--data">artifact: winlogon-userinit</span><span class="ww-chip ww-chip--data">artifact: winlogon-shell</span><span class="ww-chip ww-chip--data">artifact: specialaccounts-userlist</span></div>
</div>
</div>

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon` |
| 离线 | `SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon` |

## 离线位置

`C:\Windows\System32\Config\SOFTWARE`

## 作用

保存交互式登录流程相关配置，包括登录初始化程序、Shell、自动登录、特殊账户显示控制和部分旧式 Winlogon 扩展点。这里是登录配置，不是登录事件日志。

## 常见子键和值

| 名称 | 类型 | 含义 | 常见数据 / 状态 | 说明 |
|---|---|---|---|---|
| `Userinit` | `REG_SZ` | 登录初始化程序列表。 | `C:\Windows\system32\userinit.exe,` 常见 | 额外命令需验证来源。 |
| `Shell` | `REG_SZ` | 用户 Shell。 | `explorer.exe` 常见 | 可被策略或环境修改。 |
| `AutoAdminLogon` | `REG_SZ` | 自动登录开关。 | `0` / `1` | 需结合凭据存储和值。 |
| `DefaultUserName` | `REG_SZ` | 自动登录或登录界面相关用户名。 | 用户名 | 不证明登录成功。 |
| `DefaultDomainName` | `REG_SZ` | 默认域或主机名。 | 域名 / 主机名 | 与环境有关。 |
| `CachedLogonsCount` | `REG_SZ` | 可缓存的域登录凭据数量。 | `0` 到 `50` | 不保存缓存凭据本体。 |
| `SpecialAccounts\UserList` | Key | 登录界面账户显示控制。 | 用户名 -> `0` / `1` | 可隐藏登录 UI 显示。 |
| `Notify` | Key | Winlogon notification package。 | 子键列表 | 旧式扩展点，需谨慎验证。 |

## 默认状态与版本差异

默认值随 Windows 版本、域加入状态、自动登录配置和安全基线变化。`Userinit` 和 `Shell` 的常见默认值可作为线索，但仍应按系统版本和组织基线核对。

## 注意事项

- `Userinit`、`Shell`、`Notify` 配置存在不等于命令或 DLL 已执行。
- `DefaultUserName`、`AutoAdminLogon` 是配置线索，不是登录成功证据。
- `SpecialAccounts\UserList` 影响登录 UI 显示，不等于账户不存在。

## 取证提示

- 关注 `Userinit` / `Shell` 中追加的命令、非系统路径、脚本解释器或网络路径。
- 账户隐藏、自动登录和 LogonUI 最近用户线索应与 Security.evtx、SAM、ProfileList、域日志交叉验证。

## 相关场景

- [自启动与持久化](../../../../../../questions/persistence.md)
- [账户与安全](../../../../../../questions/accounts-security.md)
- [RDP 与远程访问](../../../../../../questions/rdp.md)
- [常规注册表检查](../../../../../../questions/registry-checklist.md)

## 相关位置

- [Winlogon\Notify](winlogon/notify.md)
- [Winlogon\SpecialAccounts\UserList](winlogon/specialaccounts-userlist.md)
- [CachedLogonsCount](winlogon/cachedlogonscount.md)
- [LogonUI](../../windows/currentversion/authentication/logonui.md)
- [Policies\System](../../windows/currentversion/policies/system.md)
- [ProfileList](profilelist.md)

## 补充阅读

- [Winlogon Userinit artifact](../../../../../../artifacts/persistence/winlogon-userinit.md)
- [Winlogon Shell artifact](../../../../../../artifacts/persistence/winlogon-shell.md)
- [SpecialAccounts\UserList artifact](../../../../../../artifacts/security/specialaccounts-userlist.md)
- [Microsoft Learn: Winlogon and Credential Providers](https://learn.microsoft.com/en-us/windows/win32/secauthn/winlogon-and-credential-providers)
- [Microsoft Sysinternals: Autoruns](https://learn.microsoft.com/en-us/sysinternals/downloads/autoruns)
