# HKLM\SECURITY

`HKLM\SECURITY` 保存本机安全策略、LSA Secrets、缓存登录配置和部分审计策略。它通常是高权限后门、凭据风险和策略异常调查的辅助入口。

## Windows 原生视图

Live 系统中为 `HKLM\SECURITY`，默认权限较高。直接查看时字段多为二进制结构，建议使用专门工具或脚本解析，并与事件日志交叉验证。

## 离线 hive 文件来源

| Hive | 文件 |
|---|---|
| `SECURITY` | `C:\Windows\System32\Config\SECURITY` |

取证采集时通常同时收集 `SYSTEM`、`SAM`、`SOFTWARE`，因为账户、LSA 配置、策略来源和 profile 映射分散在多个 hive。

## 典型取证价值

- 调查 LSA Secrets、服务账户凭据残留、缓存登录策略。
- 核对审计策略、登录策略和安全选项是否被削弱。
- 与 `SYSTEM\CurrentControlSet\Control\Lsa` 下的 LSA 包配置共同判断认证链风险。

## 典型检测价值

- 监控安全策略被关闭或审计策略被降级。
- 对 LSA 相关路径变更做高优先级告警，尤其是认证包、Security Packages 和通知包。

## 常见误判

- 域策略、基线工具和安全产品可能合法修改安全策略。
- 二进制字段需要可靠 parser，不能仅凭十六进制 diff 下结论。
- LSA 相关路径横跨 `SECURITY` 与 `SYSTEM`，不要只查一个 hive。

## 重点子路径

| 子路径 | 价值 |
|---|---|
| `Policy\Secrets` | LSA Secrets，需谨慎处理敏感数据 |
| `Policy\PolAdtEv` | 审计策略相关数据，见 [Audit Policy](../../artifacts/security/audit-policy.md) |
| `Cache` | 缓存登录相关数据，语义需结合 OS 版本和域环境 |
| `HKLM\SYSTEM\CurrentControlSet\Control\Lsa` | LSA 包配置，位于 SYSTEM hive |

## 关联 artifact 页面

- [LSA Authentication Packages](../../artifacts/persistence/lsa-authentication-packages.md)
- [Audit Policy](../../artifacts/security/audit-policy.md)

## References

- [Microsoft Learn: Registry hives](https://learn.microsoft.com/en-us/windows/win32/sysinfo/registry-hives)
- [Microsoft Learn: LSA Authentication](https://learn.microsoft.com/en-us/windows/win32/secauthn/lsa-authentication)
