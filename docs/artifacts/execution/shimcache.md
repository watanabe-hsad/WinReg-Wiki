---
tags:
  - Execution
  - ShimCache
  - SYSTEM
---

# ShimCache / AppCompatCache

<div class="rfh-meta" markdown>
<span class="rfh-badge medium">取证价值 中</span>
<span class="rfh-badge medium">检测价值 中</span>
<span class="rfh-badge">兼容性缓存</span>
</div>

ShimCache, also known as AppCompatCache, 是 Windows 应用兼容性机制的一部分。它常被用于发现系统上出现过的可执行文件路径。

## 注册表路径

| Hive | Path |
|---|---|
| `HKLM\SYSTEM` | `ControlSet00x\Control\Session Manager\AppCompatCache` |

## 取证含义

ShimCache 可以提供程序路径和缓存时间线线索，但执行语义在不同 Windows 版本上差异明显。

## 可以证明

- 系统缓存中存在某个程序路径。
- 可辅助发现已删除或不再明显存在的程序路径。

## 不能证明

- 程序一定执行。
- 缓存顺序一定是执行顺序。
- 时间戳一定表示执行时间。

## 时间戳说明

ShimCache 的时间语义高度依赖 Windows 版本和解析方法。报告中建议使用保守表述，并附解析工具名称。

## 交叉验证

- Amcache
- Prefetch
- UserAssist
- `$MFT` and `$UsnJrnl`
- EDR or Sysmon process logs

