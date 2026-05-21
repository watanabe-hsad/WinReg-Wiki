# HKLM\SYSTEM\ControlSet00x\Control\Lsa\Security Packages

`Security Packages` 是 `Control\Lsa` 下的 LSA 安全支持包列表 value。

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SYSTEM\CurrentControlSet\Control\Lsa` |
| 离线 | `SYSTEM\ControlSet00x\Control\Lsa` |

## 常见子键 / value

| 名称 | 类型 | 含义 |
|---|---|---|
| `Security Packages` | `REG_MULTI_SZ` | LSA 可使用的安全支持包列表。 |
| `OSConfig\Security Packages` | `REG_MULTI_SZ` | 系统受限配置位置；版本语义需结合系统确认。 |
| `Authentication Packages` | `REG_MULTI_SZ` | 相关但不同的认证包列表。 |
| `RunAsPPL` | `REG_DWORD` | LSA protection 配置。 |

## 说明

| 项 | 内容 |
|---|---|
| 数据来源 | `SYSTEM` hive。 |
| 常见写入者 | Windows、身份认证组件、安全产品、VPN/MFA/智能卡组件。 |
| 注意 | value 存在表示配置状态，不等同包已被 LSASS 加载。 |

## 相关 Artifact

- [LSA Security Packages](../../../../../../artifacts/persistence/lsa-security-packages.md)
- [LSA Authentication Packages](../../../../../../artifacts/persistence/lsa-authentication-packages.md)

