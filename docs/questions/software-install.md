# 软件安装与卸载

软件安装调查要区分“安装记录”“程序文件存在”“程序执行”和“用户见过”。注册表 Uninstall 与 Amcache 常能提供软件和文件元数据，但卸载、清理和便携软件会留下不完整证据。

## 优先级

| 优先级 | Artifact / Path | 主要价值 |
|---|---|---|
| 高 | `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall` | 机器级软件安装/卸载记录 |
| 高 | `HKCU\Software\Microsoft\Windows\CurrentVersion\Uninstall` | 用户级安装记录 |
| 高 | [Amcache](../artifacts/execution/amcache.md) | 程序路径、哈希、版本和文件元数据 |
| 中 | [MUICache](../artifacts/execution/muicache.md) | Shell 缓存的程序路径和显示名 |
| 中 | [UserAssist](../artifacts/execution/userassist.md) | 用户交互执行线索 |

## 高信号特征

- 安装记录显示远控、隧道、压缩、加密或同步软件接近入侵窗口安装。
- `InstallLocation` 位于用户可写目录或临时路径。
- Uninstall 记录被删除但 Amcache、Prefetch、文件系统仍有残留。
- `DisplayName` 伪装系统组件，`Publisher` 缺失或签名不一致。

## 交叉验证

- MSI logs、Windows Installer events、Program Files、Start Menu、服务、计划任务。
- Amcache、ShimCache、Prefetch、BAM/DAM、UserAssist。
- `$MFT`、`$UsnJrnl`、下载记录、浏览器历史、软件自身日志。

## 结论写法

- Uninstall 记录可证明安装登记存在，不等于软件当前仍安装或执行过。
- Amcache 和 MUICache 更偏程序存在/元数据，执行要用 Prefetch、BAM、UserAssist 或进程日志加强。
