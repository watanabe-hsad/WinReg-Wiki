# HKCU\Software\Microsoft\Terminal Server Client

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKCU\Software\Microsoft\Terminal Server Client` |
| HKU | `HKU\<SID>\Software\Microsoft\Terminal Server Client` |
| 离线 | `NTUSER.DAT\Software\Microsoft\Terminal Server Client` |

## 离线位置

`C:\Users\<User>\NTUSER.DAT`

## 作用

保存当前用户使用 Microsoft Remote Desktop Client / `mstsc.exe` 时产生的客户端侧目标历史。它说明用户 hive 中存在 RDP 客户端配置或历史线索，不说明本机作为 RDP 服务端被登录。

## 常见子键和值

| 名称 | 类型 | 含义 | 常见数据 / 状态 | 说明 |
|---|---|---|---|---|
| `Default` | Key | MRU 目标列表。 | `MRU0`、`MRU1` ... | 目标可能是主机名、IP 或完整目标字符串。 |
| `Default\MRU*` | `REG_SZ` | 最近输入或选择的连接目标。 | `server01`、`10.0.0.5` | MRU 顺序不等于连接成功顺序。 |
| `Servers\<host>` | Key | 单个目标主机记录。 | 主机名或 IP 子键 | 由客户端使用或保存连接产生。 |
| `Servers\<host>\UsernameHint` | `REG_SZ` | UI 保存的用户名提示。 | `DOMAIN\user`、`user` | 不等于凭据仍存在或登录成功。 |

## 默认状态与版本差异

未使用 MSTSC 的用户 hive 中该 key 可能不存在。Windows 版本、Remote Desktop Client 版本、保存连接方式和企业策略会影响子键和值的出现。

## 注意事项

- 这是客户端侧记录，不能证明目标主机登录成功。
- 目标字符串可能来自手工输入、旧缓存或保存连接。
- 离线分析时需先用 ProfileList / HKU 映射确认用户归属。

## 取证提示

- 可辅助回答某用户是否配置或尝试连接过特定 RDP 目标。
- 需要与 Security.evtx、TerminalServices 日志、Jump Lists、Credential Manager 和目标主机日志交叉验证。

## 相关场景

- [RDP 与远程访问](../../../../questions/rdp.md)
- [账户与安全](../../../../questions/accounts-security.md)
- [网络与系统环境](../../../../questions/network.md)
- [常规注册表检查](../../../../questions/registry-checklist.md)

## 相关位置

- [HKLM Terminal Server](../../../hklm/system/controlset/control/terminal-server.md)
- [ProfileList](../../../hklm/software/microsoft/windows-nt/currentversion/profilelist.md)
- [HKEY_USERS](../../../hku/index.md)

## 补充阅读

- [Terminal Server Client artifact](../../../../artifacts/rdp/terminal-server-client.md)
