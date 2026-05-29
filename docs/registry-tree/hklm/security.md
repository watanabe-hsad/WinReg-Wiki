# HKLM\SECURITY

`HKLM\SECURITY` 保存本机安全策略、LSA Secrets、缓存登录相关数据和部分审计策略。

## 文件

| 项 | 路径 |
|---|---|
| Hive | `C:\Windows\System32\Config\SECURITY` |
| 常用配套 hive | `SYSTEM`、`SAM`、`SOFTWARE` |

## 常用路径

| 路径 | 含义 |
|---|---|
| `Policy\Secrets` | LSA Secrets。 |
| `Policy\PolAdtEv` | 审计策略底层数据。 |
| `Cache` | 缓存登录相关数据。 |
| `HKLM\SYSTEM\CurrentControlSet\Control\Lsa` | LSA 运行配置，位于 `SYSTEM` hive。 |

## 注意

| 项 | 说明 |
|---|---|
| 二进制结构 | 多数数据需要专门 parser。 |
| 敏感数据 | LSA Secrets 可能包含凭据材料，处理时应控制输出范围。 |
| 策略来源 | 本地策略、GPO、MDM 都可能写入相关配置。 |

## 补充阅读

[Audit Policy](../../artifacts/security/audit-policy.md),
[LSA Authentication Packages](../../artifacts/persistence/lsa-authentication-packages.md)
