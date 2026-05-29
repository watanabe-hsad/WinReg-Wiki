# HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags` |
| 32 位视图 | `HKLM\SOFTWARE\WOW6432Node\Microsoft\Windows NT\CurrentVersion\AppCompatFlags` |
| 离线 | `SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags` |

## 离线位置

`C:\Windows\System32\Config\SOFTWARE`

## 作用

保存机器级应用兼容性配置和兼容性数据库相关入口。它与用户级 `HKCU\...\AppCompatFlags` 分工不同：HKLM 更偏机器范围配置，HKCU 更偏单用户配置和 PCA 记录。

## 常见子键和值

| 名称 | 类型 | 含义 | 常见数据 / 状态 | 说明 |
|---|---|---|---|---|
| `Layers` | Key | 机器级兼容层配置。 | value 名为程序路径 | 影响所有用户或机器范围。 |
| `Custom` | Key | 自定义兼容性数据库相关入口。 | 视系统和安装软件而定 | 字段语义需结合工具。 |
| `InstalledSDB` | Key | 已安装 shim database 记录。 | 视系统和软件而定 | 可与兼容性数据库文件交叉验证。 |

## 默认状态与版本差异

AppCompatFlags 子键随 Windows 版本、兼容性组件、企业兼容性数据库和安装软件变化。Server、禁用兼容性组件或精简系统可能表现不同。

## 注意事项

- AppCompatFlags 配置存在不等于程序已经执行。
- 机器级 `Layers` 和用户级 `Layers` 需要分开解释。
- 32 位程序相关配置可能出现在 WOW6432Node 视图。

## 取证提示

- 可辅助解释程序兼容层、shim database 和机器范围兼容性配置。
- 需要与 Prefetch、Amcache、ShimCache、BAM / DAM、文件系统时间线和用户级 AppCompatFlags 验证。

## 相关场景

- [程序执行痕迹](../../../../../../questions/execution.md)
- [软件安装与卸载](../../../../../../questions/software-install.md)
- [常规注册表检查](../../../../../../questions/registry-checklist.md)

## 相关位置

- [HKLM AppCompatFlags\Layers](appcompatflags/layers.md)
- [HKCU AppCompatFlags](../../../../../hkcu/software/microsoft/windows-nt/currentversion/appcompatflags.md)
- [WOW6432Node](../../../wow6432node.md)

## 补充阅读

- [ShimCache artifact](../../../../../../artifacts/execution/shimcache.md)
