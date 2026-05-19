---
tags:
  - Persistence
  - IFEO
  - Hijacking
---

# Image File Execution Options

<div class="rfh-meta" markdown>
<span class="rfh-badge high">取证价值 高</span>
<span class="rfh-badge high">检测价值 高</span>
<span class="rfh-badge">劫持</span>
</div>

Image File Execution Options, commonly IFEO, 原本用于调试和兼容性配置。攻击者常滥用 `Debugger` value 劫持目标进程启动。

## 注册表路径

| Hive | Path |
|---|---|
| `HKLM\SOFTWARE` | `Microsoft\Windows NT\CurrentVersion\Image File Execution Options\<ImageName>` |

## 取证含义

当 `<ImageName>` 下存在 `Debugger` value 时，系统可能在目标可执行文件启动时先启动指定调试器命令。

## 可以证明

- 某个可执行文件存在 IFEO 配置。
- `Debugger` 指向的命令可能被用于进程启动劫持。

## 不能证明

- 目标进程一定被启动过。
- `Debugger` 命令一定成功执行。
- 所有 IFEO 配置都是恶意，开发工具也会使用。

## 检测思路

- 非开发环境中出现 `Debugger` value。
- `Debugger` 指向用户可写目录或脚本解释器。
- 针对安全工具、浏览器、办公软件、系统工具的 IFEO 配置。
- `sethc.exe`、`utilman.exe` 等辅助功能程序相关劫持。

## 采集方式

```powershell
Get-ChildItem "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options" |
  ForEach-Object {
    $p = Get-ItemProperty $_.PsPath -ErrorAction SilentlyContinue
    if ($p.Debugger) { $p }
  }
```

## 交叉验证

- Sysmon Registry Set events
- Process creation logs
- Security tool tampering alerts
- File system timeline for debugger binary

