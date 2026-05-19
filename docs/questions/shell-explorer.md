# Shell / Explorer 用户行为

Shell / Explorer artifact 用来回答用户是否见过程序、文件、目录、卷或共享。它们很适合还原用户行为路径，但多数不能单独证明文件内容被读取或程序完整执行。

## 优先级

| 优先级 | Artifact / Path | 主要价值 |
|---|---|---|
| 高 | [UserAssist](../artifacts/execution/userassist.md) | Explorer 相关用户交互执行线索 |
| 高 | [MountPoints2](../artifacts/usb/mountpoints2.md) | 用户见过的卷、盘符或网络共享 |
| 中 | [MUICache](../artifacts/execution/muicache.md) | Shell 缓存的程序路径和显示名 |
| 中 | [RunMRU](../artifacts/user-activity/runmru.md) | Win+R / Run 对话框输入历史 |
| 中 | [RecentDocs](../artifacts/user-activity/recentdocs.md) | 最近文档名称和扩展名线索 |
| 中 | [OpenSavePidlMRU](../artifacts/user-activity/opensavepidlmru.md) / [LastVisitedPidlMRU](../artifacts/user-activity/lastvisitedpidlmru.md) | 文件对话框访问路径和应用关联 |

## 高信号特征

- UserAssist 与 Prefetch/BAM 同时指向用户目录中的可疑程序。
- MountPoints2 出现未知 USB 卷或敏感 SMB 共享，随后有 LNK/Jump Lists 文件访问。
- RecentDocs、OpenSavePidlMRU 和 `$MFT` 同时指向敏感文件名。
- RunMRU 出现 `cmd`、`powershell`、UNC 路径或内部工具命令。

## 交叉验证

- LNK、Jump Lists、ShellBags、RecentDocs、文件对话框 MRU。
- Prefetch、BAM/DAM、Amcache、ShimCache。
- `$MFT`、`$UsnJrnl`、文件访问审计、EDR process/file telemetry。
- 用户登录会话和屏幕锁定/解锁事件。

## 结论写法

- Shell artifact 常说明“用户环境中出现过/交互过/浏览过”，不要直接写“文件被阅读”或“程序由用户双击执行”。
- 多个独立 artifact 指向同一路径、同一 SID 和接近时间时，才提高到更强的用户行为判断。
