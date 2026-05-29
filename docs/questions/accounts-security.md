# 账户与安全

## 检查目标

确认本地账户、SID 到 profile 的映射、隐藏账户配置、LSA 相关配置和登录/权限事实之间的边界。

## 优先查看的注册表位置

| 注册表位置 | 用途 | 判断边界 |
|---|---|---|
| [ProfileList](../registry-tree/hklm/software/microsoft/windows-nt/currentversion/profilelist.md) | SID 到 profile 路径映射。 | 不证明账户仍存在或近期登录。 |
| [SAM](../registry-tree/hklm/sam.md) | 本地账户和组数据库。 | 二进制字段需专门工具解析。 |
| [HKEY_USERS](../registry-tree/hku/index.md) | 已加载用户 hive 集合。 | live 树只显示已加载 hive。 |
| [NTUSER.DAT](../registry-tree/hku/ntuser.md) | 用户级配置和行为线索来源。 | 需要先映射 SID。 |
| [Winlogon](../registry-tree/hklm/software/microsoft/windows-nt/currentversion/winlogon.md) | `SpecialAccounts\UserList`、自动登录等。 | 隐藏登录界面不等于账户不存在。 |
| [CachedLogonsCount](../registry-tree/hklm/software/microsoft/windows-nt/currentversion/winlogon/cachedlogonscount.md) | 域登录缓存数量配置。 | 不保存缓存凭据内容。 |
| [SpecialAccounts\UserList](../registry-tree/hklm/software/microsoft/windows-nt/currentversion/winlogon/specialaccounts-userlist.md) | 登录界面账户显示控制。 | 不启用、不禁用、不创建账户。 |
| [LogonUI](../registry-tree/hklm/software/microsoft/windows/currentversion/authentication/logonui.md) | 登录界面最近用户、显示名和选中 SID。 | 不证明登录成功。 |
| [Credential Providers](../registry-tree/hklm/software/microsoft/windows/currentversion/authentication/credential-providers.md) | 登录界面凭据提供器注册。 | 注册存在不等于登录中使用。 |
| [Policies\System](../registry-tree/hklm/software/microsoft/windows/currentversion/policies/system.md) | UAC、远程本地账户过滤和登录提示相关策略。 | 需结合策略来源和登录事实。 |
| [LSA](../registry-tree/hklm/system/controlset/control/lsa/index.md) | LSA 包、RunAsPPL 和认证相关配置。 | 未知包需验证文件、签名和模块加载。 |
| [SECURITY](../registry-tree/hklm/security.md) | 安全策略、LSA Secrets、审计相关数据。 | 需要谨慎解析，避免直接手工解释二进制数据。 |

## 判断要点

- 先用 ProfileList 建立 SID、用户名目录、用户 hive 的对应关系。
- 新 SID、临时 profile、`.bak` profile、异常 profile 路径需要和登录日志、文件系统时间线关联。
- `SpecialAccounts\UserList` 和 LogonUI 值可解释登录界面显示状态，但不等于账户启用状态或登录成功。
- LSA 包新增条目时，记录 DLL 名称、路径来源、签名和是否存在模块加载证据。

## 交叉验证

- Security.evtx：`4624`、`4625`、`4672`、`4720`、`4722`、`4726`、`4732`、`4733`、`4738`。
- SAM hive、本地组成员、域控制器日志、User Profile Service operational log。
- 用户 `NTUSER.DAT`、`UsrClass.dat`、profile 目录、文件系统时间线。
- LSASS 模块、Code Integrity、EDR credential access telemetry。

## 常见误判

- ProfileList 中存在 SID 映射不等于账户仍启用。
- live `HKU` 中没有某用户 hive，不等于该用户不存在。
- 隐藏账户配置可能来自管理需求、VDI、实验环境或 OEM 配置。

## 相关场景

- [RDP 与远程访问](rdp.md)
- [安全策略与防护配置](policy-security.md)
- [常规注册表检查](registry-checklist.md)

## 补充阅读

- [ProfileList artifact](../artifacts/security/profilelist.md)
- [SpecialAccounts\UserList artifact](../artifacts/security/specialaccounts-userlist.md)
- [LSA Authentication Packages artifact](../artifacts/persistence/lsa-authentication-packages.md)
