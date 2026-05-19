# HKLM\SAM

`HKLM\SAM` 对应本地 Security Account Manager 数据库，主要记录本地用户、组、RID 和账户状态。它通常需要 SYSTEM 权限或离线加载才能完整读取。

## Windows 原生视图

Live 系统中路径为 `HKLM\SAM\SAM\Domains\Account`。常规 `regedit.exe` 可能看不到完整内容，取证工具或离线挂载更可靠。

## 离线 hive 文件来源

| Hive | 文件 |
|---|---|
| `SAM` | `C:\Windows\System32\Config\SAM` |

采集时同时保留 `SYSTEM` hive，因为解析本地账户散列、LSA 相关数据或时间线时经常需要 SYSTEM boot key 及上下文。

## 典型取证价值

- 确认本地账户是否存在、RID 是否异常、账户是否禁用。
- 与 [ProfileList](../../artifacts/security/profilelist.md) 对比，判断账户对象、用户 profile 和登录痕迹是否一致。
- 辅助调查隐藏账户、影子管理员、RID 异常或本地组权限变化。

## 典型检测价值

- 监控本地账户新增、RID 500 以外管理员行为、本地 Administrators 组变化。
- 结合 Security.evtx `4720`、`4722`、`4732`、`4733`、`4738` 捕捉账户生命周期。

## 常见误判

- Profile 目录存在不等于 SAM 账户仍然存在。
- 域账户登录过的机器可能有 profile，但不一定有对应本地 SAM 账户。
- 离线解析工具输出字段名差异较大，报告应说明工具和版本。

## 重点子路径

| 子路径 | 价值 |
|---|---|
| `SAM\SAM\Domains\Account\Users` | 本地用户 RID 与二进制账户记录 |
| `SAM\SAM\Domains\Builtin\Aliases` | 内置组和成员关系 |
| `SAM\SAM\Domains\Account\Aliases` | 本地组 |

## 关联 artifact 页面

- [ProfileList](../../artifacts/security/profilelist.md)

## References

- [Microsoft Learn: Registry hives](https://learn.microsoft.com/en-us/windows/win32/sysinfo/registry-hives)
