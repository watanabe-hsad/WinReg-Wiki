# 程序执行

程序执行不是单个 artifact 能完全证明的事情。注册表可以提供强线索，但最好和 Prefetch、SRUM、事件日志、EDR 或文件系统时间线一起看。

## 优先级

| 优先级 | Artifact | 主要价值 |
|---|---|---|
| 高 | [UserAssist](../artifacts/execution/userassist.md) | Explorer 相关用户交互痕迹 |
| 高 | [BAM / DAM](../artifacts/execution/bam-dam.md) | SID 维度的近期程序运行线索 |
| 高 | [Amcache](../artifacts/execution/amcache.md) | 程序存在、路径、哈希、元数据 |
| 中 | [ShimCache](../artifacts/execution/shimcache.md) | 程序路径与兼容性缓存 |
| 中 | [MUICache](../artifacts/execution/muicache.md) | Shell 缓存的程序路径和显示名 |

## 常见判断问题

- 这个程序是否存在过？
- 用户是否可能通过 Explorer 触发过它？
- BAM 是否把路径归属到某个 SID？
- 路径是否位于用户可写目录？
- 首次出现时间、最后修改时间、日志时间线是否一致？

## 结论写法

- `UserAssist`、`BAM / DAM`、Prefetch、进程日志互相印证时，可以较稳妥写“该程序在某用户上下文中执行过”。
- 只有 `MUICache` 或 `ShimCache` 时，优先写“程序路径存在或被系统组件记录过”，不要单独写成“已执行”。
