# HKCU\Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKCU\Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags` |
| 离线 | `NTUSER.DAT\Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags` |

## 离线位置

`C:\Users\<User>\NTUSER.DAT`

## 作用

保存用户级应用兼容性相关配置和 Program Compatibility Assistant 记录。常见子路径可记录兼容性 shim、用户设置的兼容模式，或系统观察到的程序兼容性状态。

## 常见子键和值

| 名称 | 类型 | 含义 | 常见数据 / 状态 | 说明 |
|---|---|---|---|---|
| `Layers` | Key | 用户级兼容性层配置。 | value 名为程序路径 | value data 可含兼容性标记。 |
| `Compatibility Assistant\Store` | Key | Program Compatibility Assistant 记录。 | value 名为程序路径 | 表示程序被 PCA 记录过，不等于完整执行证明。 |
| `Compatibility Assistant\Persisted` | Key | PCA 持久化相关记录。 | 视版本而定 | 字段语义需工具验证。 |

## 默认状态与版本差异

不同 Windows 版本的 PCA 和兼容性子键表现不同。Server、精简系统或禁用 PCA 的环境可能缺少部分子键。

## 注意事项

- AppCompatFlags 更偏兼容性配置和程序存在 / 交互线索，不应单独写成执行定论。
- value 名通常是路径，需确认文件是否仍存在、路径是否被复用。
- HKLM 也可能存在机器级 AppCompatFlags，需按范围区分。

## 取证提示

- 可辅助确认某用户上下文中程序路径被兼容性系统记录或配置过。
- 与 UserAssist、Prefetch、Amcache、ShimCache、BAM / DAM 和文件系统时间线交叉验证。

## 相关场景

- [程序执行痕迹](../../../../../../questions/execution.md)
- [软件安装与卸载](../../../../../../questions/software-install.md)
- [常规注册表检查](../../../../../../questions/registry-checklist.md)

## 相关位置

- [HKCU NTUSER.DAT](../../../../../hku/ntuser.md)
- [HKLM AppCompatFlags](../../../../../hklm/software/microsoft/windows-nt/currentversion/appcompatflags.md)
- [UserAssist](../../windows/currentversion/userassist.md)
- [HKLM Uninstall](../../../../../hklm/software/microsoft/windows/currentversion/uninstall.md)

## 补充阅读

- [ShimCache artifact](../../../../../../artifacts/execution/shimcache.md)
