# HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options

`Image File Execution Options` 保存按可执行文件名生效的进程启动配置。

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options` |
| 离线 | `SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options` |

## 常见子键 / value

| 名称 | 类型 | 含义 |
|---|---|---|
| `<ImageName>` | Key | 以可执行文件名命名，例如 `notepad.exe`。 |
| `Debugger` | `REG_SZ` | 调试器路径；会影响目标进程启动流程。 |
| `GlobalFlag` | `REG_DWORD` | 调试/诊断相关标志。 |
| `SilentProcessExit` | Key | 静默进程退出监控相关配置。 |

## 说明

| 项 | 内容 |
|---|---|
| 数据来源 | `SOFTWARE` hive。 |
| 常见写入者 | 调试工具、开发工具、诊断工具、应用兼容性配置。 |
| 注意 | IFEO 配置可能是开发或诊断用途；判断时需核对路径、签名和环境背景。 |

## 相关 Artifact

- [IFEO](../../../artifacts/persistence/ifeo.md)
- [Run / RunOnce](../../../artifacts/persistence/run-keys.md)
- [Services](../../../artifacts/persistence/services.md)

