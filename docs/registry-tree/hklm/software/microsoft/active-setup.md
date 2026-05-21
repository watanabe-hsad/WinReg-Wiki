# HKLM\SOFTWARE\Microsoft\Active Setup

`Active Setup` 保存机器级组件定义和每用户初始化相关配置。

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SOFTWARE\Microsoft\Active Setup\Installed Components` |
| Live 用户状态 | `HKCU\Software\Microsoft\Active Setup\Installed Components` |
| 离线机器级 | `SOFTWARE\Microsoft\Active Setup\Installed Components` |
| 离线用户级 | `NTUSER.DAT\Software\Microsoft\Active Setup\Installed Components` |

## 常见子键 / value

| 名称 | 类型 | 含义 |
|---|---|---|
| `<Component>` | Key | 组件 GUID 或名称。 |
| `StubPath` | `REG_SZ` / `REG_EXPAND_SZ` | 初始化命令。 |
| `Version` | `REG_SZ` | HKLM/HKCU 版本比较相关。 |
| `Locale` | `REG_SZ` | 区域设置比较相关。 |
| `IsInstalled` | `REG_DWORD` | 安装状态标记；具体语义需结合组件。 |

## 说明

| 项 | 内容 |
|---|---|
| 数据来源 | 机器级在 `SOFTWARE`；用户级在 `NTUSER.DAT`。 |
| 常见写入者 | Windows 组件、浏览器、Office、安装程序、企业软件。 |
| 注意 | HKLM 定义和 HKCU 镜像需要一起看；配置存在不等于命令已执行。 |

## 相关 Artifact

- [Active Setup](../../../../artifacts/persistence/active-setup.md)

