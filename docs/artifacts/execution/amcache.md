---
tags:
  - Execution
  - Amcache
  - ProgramMetadata
---

# Amcache

<div class="rfh-meta" markdown>
<span class="rfh-badge high">取证价值 高</span>
<span class="rfh-badge medium">检测价值 中</span>
<span class="rfh-badge">程序元数据</span>
</div>

Amcache 记录应用兼容性相关数据，常用于发现系统上出现过的可执行文件、路径、哈希和文件元数据。

## Registry Paths

| File | Common Path |
|---|---|
| `Amcache.hve` | `C:\Windows\AppCompat\Programs\Amcache.hve` |

## Forensic Meaning

Amcache 更适合证明“系统知道这个文件”或“该文件元数据曾被记录”，而不是单独证明执行。

## What It Can Prove

- 可执行文件路径、文件名、部分哈希或元数据。
- 文件首次被兼容性组件记录的线索。
- 程序清单、版本、发布者等辅助信息。

## What It Cannot Prove

- 程序一定执行。
- 记录时间一定等于首次执行时间。
- 文件仍然存在。

## Detection Ideas

- 用户可写目录中的可执行文件。
- 伪装系统路径或双扩展名。
- 低信誉发布者、无签名、异常时间线。

## Cross Validation

- Prefetch
- UserAssist
- ShimCache
- SRUM
- EDR process telemetry
- File system timeline

