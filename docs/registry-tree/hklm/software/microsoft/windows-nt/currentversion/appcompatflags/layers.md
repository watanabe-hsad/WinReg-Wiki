# HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Layers

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Layers` |
| 32 位视图 | `HKLM\SOFTWARE\WOW6432Node\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Layers` |
| 离线 | `SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Layers` |

## 离线位置

`C:\Windows\System32\Config\SOFTWARE`

## 作用

保存机器级应用兼容层配置。value name 通常是程序路径，value data 是兼容层标记，用于让 Windows 对指定程序应用兼容性选项。

## 常见子键和值

| 名称 | 类型 | 含义 | 常见数据 / 状态 | 说明 |
|---|---|---|---|---|
| `<Executable path>` | `REG_SZ` | 指定程序路径的兼容层配置。 | `RUNASADMIN`、`WINXPSP3` 等标记可能出现 | 标记组合随版本和 UI 设置变化。 |

## 默认状态与版本差异

该 key 在没有机器级兼容层配置时可能不存在或为空。可用兼容层标记随 Windows 版本、兼容性组件和应用程序兼容性数据库变化。

## 注意事项

- 兼容层记录不等于程序成功执行。
- value name 路径可能指向已删除文件或被路径复用。
- 机器级配置影响范围不同于 HKCU 用户级配置。

## 取证提示

- `RUNASADMIN` 等标记可辅助解释程序启动环境或权限提示配置。
- 应与用户级 `Layers`、Prefetch、Amcache、ShimCache、BAM / DAM 和进程日志交叉验证。

## 相关场景

- [程序执行痕迹](../../../../../../../questions/execution.md)
- [自启动与持久化](../../../../../../../questions/persistence.md)
- [软件安装与卸载](../../../../../../../questions/software-install.md)
- [常规注册表检查](../../../../../../../questions/registry-checklist.md)

## 相关位置

- [HKLM AppCompatFlags](../appcompatflags.md)
- [HKCU AppCompatFlags](../../../../../../hkcu/software/microsoft/windows-nt/currentversion/appcompatflags.md)
- [IFEO](../ifeo.md)

## 补充阅读

- [ShimCache artifact](../../../../../../../artifacts/execution/shimcache.md)
