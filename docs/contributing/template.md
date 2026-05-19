# Artifact 页面模板

新增 artifact 时建议复制这个结构，避免页面越写越散。

```markdown
---
tags:
  - Category
  - Hive
---

# Artifact Name

<div class="rfh-meta" markdown>
<span class="rfh-badge high">取证价值 高</span>
<span class="rfh-badge medium">检测价值 中</span>
<span class="rfh-badge">证据类型</span>
</div>

一句话说明这个 artifact 的调查价值。

## 摘要

一句话说明这个 artifact 的核心价值。

## 注册表路径

| 视图 | Hive / 文件 | 路径 | Value | 范围 |
|---|---|---|---|---|
| Live path | `HKCU` | `Software\...` | `ValueName` | Current user |
| Offline hive path | `NTUSER.DAT` | `Software\...` | `ValueName` | User SID |

## 原生注册表视图

说明在 `regedit.exe` 中通常从哪里展开，以及 live 视图和真实 hive 的关系。

## 离线位置

说明离线镜像中对应哪个 hive 文件、是否需要 SID 映射或 ControlSet 解析。

## 字段含义

| 字段 | 含义 |
|---|---|
| value / subkey | 具体含义 |

## 取证含义

说明它通常记录什么。

## 可以证明

- ...

## 不能证明

- ...

## 时间戳说明

说明 LastWrite、value 时间戳、工具解析差异。

## 系统版本差异

说明 Windows 7 / 10 / 11 / Server 差异；未知就写“待验证”。

## 攻击滥用

说明攻击者如何滥用这个位置或如何清理痕迹。

## 检测思路

- ...

## 常见误报

- ...

## 采集方式

```powershell
Get-ItemProperty "HKCU:\..."
```

## 解析工具

- RECmd
- Registry Explorer
- RegRipper
- KAPE
- Velociraptor

## 交叉验证

- Event Log
- Prefetch
- Amcache
- File system timeline

## 示例结论

- 报告风格判断句，明确证据强度。

## 相关页面

- 场景：...
- 注册表位置：...

## 参考资料

- ...
```
