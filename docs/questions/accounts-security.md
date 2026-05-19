# 账户与安全

账户调查要区分账户对象、profile、登录行为和权限变化。注册表可以帮助映射 SID、发现隐藏账户线索和 LSA 风险，但权限授予和登录事实通常要靠事件日志确认。

## 优先级

| 优先级 | Artifact / Path | 主要价值 |
|---|---|---|
| 高 | [ProfileList](../artifacts/security/profilelist.md) | SID 到用户目录映射，用户级 artifact 归属基础 |
| 高 | `HKLM\SAM\SAM\Domains\Account\Users` | 本地账户 RID、状态和二进制账户记录 |
| 高 | [SpecialAccounts\UserList](../artifacts/security/specialaccounts-userlist.md) | 登录界面隐藏账户线索 |
| 高 | [LSA Authentication Packages](../artifacts/persistence/lsa-authentication-packages.md) | 认证包持久化和凭据访问风险 |
| 中 | `HKLM\SECURITY\Policy` | 安全策略、LSA Secrets、审计相关数据 |

## 高信号特征

- 新 SID 出现在 ProfileList 后，短时间内出现本地管理员组变化或用户级持久化。
- `SpecialAccounts\UserList` 隐藏某个新建本地账户。
- LSA 包新增非基线条目，且对应 DLL 无签名或创建时间接近入侵窗口。
- Profile 路径指向非标准目录、临时目录或可移动卷。

## 交叉验证

- Security.evtx：`4720`、`4722`、`4726`、`4732`、`4733`、`4738`、`4672`、`4624`。
- SAM hive、本地域控制器日志、本地组成员列表。
- User Profile Service operational log。
- 用户 `NTUSER.DAT`、`UsrClass.dat`、文件系统时间线。

## 结论写法

- ProfileList 可证明 SID 与 profile 的映射存在，不能单独证明账户仍存在或近期登录。
- SAM 可证明本地账户数据库状态，域账户行为仍需域控制器和本机登录日志。
