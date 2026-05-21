# HKLM\SYSTEM\ControlSet00x\Control\Session Manager\AppCertDlls

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\AppCertDlls` |
| 离线 | `SYSTEM\ControlSet00x\Control\Session Manager\AppCertDlls` |

## 离线位置

`C:\Windows\System32\Config\SYSTEM`

## 作用

保存 AppCert DLL 配置。该机制可让进程创建路径上加载指定 DLL 进行应用证书相关处理；在现代系统中不常见，出现非空配置时应核对来源。

## 常见子键和值

| 名称 | 类型 | 含义 | 常见数据 / 状态 | 说明 |
|---|---|---|---|---|
| `<value name>` | `REG_SZ` / `REG_EXPAND_SZ` | AppCert DLL 路径或名称。 | 默认通常为空或不存在 | 名称和数据由组件决定。 |

## 默认状态与版本差异

多数普通客户端系统上该 key 可能不存在或为空。具体行为随 Windows 版本和兼容性机制变化，未知环境应标注待验证并与基线比较。

## 注意事项

- 配置存在不等于 DLL 已被加载。
- 该机制需要结合进程创建、模块加载和文件证据验证。
- 合法旧组件、兼容性组件或安全产品可能使用类似加载点。

## 取证提示

- 非空 AppCertDlls 指向用户可写目录、临时目录、网络路径或无签名 DLL 时，应进入持久化和进程创建排查。
- 与 Sysmon Event ID 7、EDR module telemetry、文件签名和 key LastWrite 一起看。

## 相关场景

- [自启动与持久化](../../../../../../questions/persistence.md)
- [程序执行痕迹](../../../../../../questions/execution.md)
- [常规注册表检查](../../../../../../questions/registry-checklist.md)

## 相关位置

- [Session Manager](index.md)
- [KnownDLLs](knowndlls.md)
- [AppInit_DLLs](../../../../software/microsoft/windows-nt/currentversion/appinit-dlls.md)

## 补充阅读

- [MITRE ATT&CK: AppCert DLLs](https://attack.mitre.org/techniques/T1546/009/)
