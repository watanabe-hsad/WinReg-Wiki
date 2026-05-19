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

## Summary

一句话说明这个 artifact 的核心价值。

## Registry Paths

| View | Hive / File | Path | Value | Scope |
|---|---|---|---|---|
| Live path | `HKCU` | `Software\...` | `ValueName` | Current user |
| Offline hive path | `NTUSER.DAT` | `Software\...` | `ValueName` | User SID |

## Native Registry View

说明在 `regedit.exe` 中通常从哪里展开，以及 live 视图和真实 hive 的关系。

## Offline Location

说明离线镜像中对应哪个 hive 文件、是否需要 SID 映射或 ControlSet 解析。

## Data Meaning

| Field | Meaning |
|---|---|
| value / subkey | 具体含义 |

## Forensic Meaning

说明它通常记录什么。

## What It Can Prove

- ...

## What It Cannot Prove

- ...

## Timestamp Notes

说明 LastWrite、value 时间戳、工具解析差异。

## OS Version Notes

说明 Windows 7 / 10 / 11 / Server 差异；未知就写“待验证”。

## Attacker Usage

说明攻击者如何滥用这个位置或如何清理痕迹。

## Detection Ideas

- ...

## False Positives

- ...

## Collection

```powershell
Get-ItemProperty "HKCU:\..."
```

## Parsing Tools

- RECmd
- Registry Explorer
- RegRipper
- KAPE
- Velociraptor

## Cross Validation

- Event Log
- Prefetch
- Amcache
- File system timeline

## Example Findings

- 报告风格判断句，明确证据强度。

## Related Pages

- 场景：...
- 注册表位置：...

## References

- ...
```
