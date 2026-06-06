# HKCU\Software\Microsoft\Windows\CurrentVersion\Run

用户级登录启动项位置，只作用于对应用户 SID 的登录会话。

<div class="ww-fact-card" markdown>
<div class="ww-fact-card__head"><span class="ww-card-kicker">Registry Fact Card</span><strong>用户级登录启动项</strong></div>
<div class="ww-fact-grid" markdown>
<div><span>Root</span><strong>HKCU / HKU&lt;SID&gt;</strong></div>
<div><span>Hive</span><strong>NTUSER.DAT</strong></div>
<div><span>Offline file</span><strong>C:\Users\&lt;user&gt;\NTUSER.DAT</strong></div>
<div class="ww-fact-wide"><span>Native path</span><code>HKCU\Software\Microsoft\Windows\CurrentVersion\Run</code><code>HKU\&lt;SID&gt;\Software\Microsoft\Windows\CurrentVersion\Run</code></div>
<div><span>Topics</span><span class="ww-chip ww-chip--topic">持久化</span></div>
<div><span>Related scenarios</span><span class="ww-chip ww-chip--scenario">自启动与持久化</span><span class="ww-chip ww-chip--scenario">常规注册表检查</span></div>
<div><span>Data status</span><strong>stable / high</strong></div>
</div>
</div>

## 位置

| 视图 | 路径 |
|---|---|
| Live | `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` |
| Live | `HKCU\Software\Microsoft\Windows\CurrentVersion\RunOnce` |
| 用户 SID | `HKU\<SID>\Software\Microsoft\Windows\CurrentVersion\Run` |
| 离线 | `NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Run` |

## 离线位置

`C:\Users\<user>\NTUSER.DAT`

## 作用

`Run` 保存该用户登录后自动运行的命令。`RunOnce` 保存该用户的一次性登录启动项。value name 通常是启动项名称，value data 是命令或程序路径。

## 常见子键 / 值

| 名称 | 类型 | 含义 |
|---|---|---|
| `<value name>` | `REG_SZ` | 启动项名称。 |
| `<value data>` | `REG_SZ` / `REG_EXPAND_SZ` | 启动命令、程序路径或带参数命令行。 |
| `RunOnce` | Key | 用户级一次性登录启动项。 |

## 默认状态 / 常见状态

默认可以为空。浏览器更新器、同步盘、输入法、聊天软件、企业代理和正常应用都可能写入该位置。

## 版本差异

该位置按用户 hive 分开保存。live 查询 `HKCU` 时必须确认命令运行上下文，否则可能读到管理员、服务账户或当前 shell 用户的 hive。

## 取证提示

该位置能把自启动配置归属到具体用户。配置存在不等于执行成功，需要结合该用户登录、进程创建、StartupApproved、Prefetch、BAM / DAM 或 EDR 记录。

## 相关场景

- [自启动与持久化](../../../../../../questions/persistence.md)
- [常规注册表检查](../../../../../../questions/registry-checklist.md)

## 相关位置

- [HKLM Run / RunOnce](../../../../../hklm/software/microsoft/windows/currentversion/run.md)
- [HKCU Explorer](explorer.md)
- [NTUSER.DAT](../../../../../hku/ntuser.md)

## 补充阅读

- [Run / RunOnce artifact](../../../../../../artifacts/persistence/run-keys.md)
- [Microsoft Learn: Run and RunOnce registry keys](https://learn.microsoft.com/en-us/windows/win32/setupapi/run-and-runonce-registry-keys)
- [Microsoft Sysinternals: Autoruns](https://learn.microsoft.com/en-us/sysinternals/downloads/autoruns)
