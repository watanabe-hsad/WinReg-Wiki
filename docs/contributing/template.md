# 页面模板

本页提供常用页面骨架。新增内容时优先新增或补强 `注册表位置` 页面；只有确实需要 artifact 级字段、工具和采集细节时，再维护 artifact 补充页。

## 注册表位置页面

```markdown
# HKLM\...

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\...` |
| 离线 | `HIVE\...` |

## 离线位置

`C:\Windows\System32\Config\...`

## 作用

2 到 5 句话说明这个 key / value 在 Windows 中负责什么。

## 常见子键和值

| 名称 | 类型 | 含义 | 常见数据 / 状态 | 说明 |
|---|---|---|---|---|
| `ValueName` | `REG_*` | ... | ... | ... |

## 默认状态与版本差异

视 Windows 版本、角色和配置而定。

## 注意事项

- ...

## 取证提示

- ...

## 相关场景

- [常规注册表检查](../../questions/registry-checklist.md)

## 相关位置

- [...]

## 补充阅读

- [...]
```

## 取证场景页面

```markdown
# 场景名称

## 检查目标

一句话说明这个场景回答什么问题。

## 优先查看的注册表位置

| 注册表位置 | 用途 | 判断边界 |
|---|---|---|
| [路径名称](../registry-tree/...) | ... | ... |

## 判断要点

- ...

## 交叉验证

- 事件日志、文件系统、Prefetch、Amcache、ShimCache、SRUM、Defender 日志、EDR 等。

## 常见误判

- ...

## 相关场景

- [...]

## 补充阅读

- artifact 补充页，仅在需要字段或工具细节时添加。
```

## Artifact 补充页面

```markdown
---
tags:
  - Category
  - Hive
---

# Artifact Name

一句话说明该补充条目覆盖的字段或工具解析范围。

## 对应注册表位置

- [...]

## 字段语义

| 字段 | 含义 |
|---|---|
| `ValueName` | ... |

## 采集注意事项

- ...

## 解析工具

- Registry Explorer
- RECmd
- KAPE
- Velociraptor

## 常见误判

- ...

## 交叉验证

- ...

## 参考

- ...
```

## Registry YAML 示例

`data/registry/*.yml` 用于生成结构化索引和覆盖矩阵。正文页面仍需人工维护。

```yaml
id: hklm-example-path
title: HKLM\SOFTWARE\Example
page: docs/registry-tree/hklm/software/example.md
summary: 一句话说明该位置负责什么。
native_paths:
  - HKLM\SOFTWARE\Example
root: HKLM
hive: SOFTWARE
offline_files:
  - C:\Windows\System32\Config\SOFTWARE
topics:
  - 系统配置
category: 示例分类
evidence_types:
  - 配置项
values:
  - name: ValueName
    type: REG_SZ
    meaning: value 的含义。
    common_data: 常见数据。
    notes: 解释限制或注意事项。
subkeys: []
default_state: 视 Windows 版本、角色和配置而定。
version_notes: 视 Windows 版本和配置而定。
timestamp_notes: key LastWrite 是 key 级变化时间，不是单个 value 创建时间。
forensic_notes:
  - 只写短事实提示。
common_misreads:
  - 不要把配置存在直接写成行为发生。
related_scenarios:
  - title: 常规注册表检查
    path: docs/questions/registry-checklist.md
related_registry_pages:
  - title: HKLM\SOFTWARE
    path: docs/registry-tree/hklm/software/index.md
related_artifacts: []
tools:
  - Registry Explorer
references:
  - title: Microsoft Learn
    url: https://learn.microsoft.com/
status: draft
confidence: medium
```

生成命令：

```bash
.venv/bin/python scripts/generate-registry-index.py
```
