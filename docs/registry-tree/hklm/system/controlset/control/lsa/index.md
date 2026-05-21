# HKLM\SYSTEM\ControlSet00x\Control\Lsa

`Control\Lsa` 保存 Local Security Authority 的部分运行配置。

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SYSTEM\CurrentControlSet\Control\Lsa` |
| 离线 | `SYSTEM\ControlSet00x\Control\Lsa` |

## 常见子键 / value

| 名称 | 类型 | 含义 |
|---|---|---|
| `Authentication Packages` | `REG_MULTI_SZ` | LSA 认证包列表。 |
| `Security Packages` | `REG_MULTI_SZ` | 安全包列表。 |
| `Notification Packages` | `REG_MULTI_SZ` | 通知包列表，常见值需结合系统版本确认。 |
| `RunAsPPL` | `REG_DWORD` | LSASS Protected Process Light 相关配置。 |

## 说明

| 项 | 内容 |
|---|---|
| 数据来源 | `SYSTEM` hive。 |
| 常见写入者 | Windows 安全组件、认证包安装程序、策略或安全软件。 |
| 注意 | value 语义与系统版本、安全产品和域环境有关；未知条目需要文件和签名验证。 |

## 相关场景

- [账户与安全](../../../../../../questions/accounts-security.md)
- [安全策略与防护配置](../../../../../../questions/policy-security.md)
- [自启动与持久化](../../../../../../questions/persistence.md)
- [常规注册表检查](../../../../../../questions/registry-checklist.md)

## 补充阅读

- [LSA Authentication Packages](../../../../../../artifacts/persistence/lsa-authentication-packages.md)
- [LSA Security Packages](../../../../../../artifacts/persistence/lsa-security-packages.md)
- [UAC Policies](../../../../../../artifacts/security/uac-policies.md)
- [Audit Policy](../../../../../../artifacts/security/audit-policy.md)
