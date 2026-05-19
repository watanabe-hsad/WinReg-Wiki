---
tags:
  - Execution
  - UserActivity
  - NTUSER.DAT
---

# UserAssist

<div class="rfh-meta" markdown>
<span class="rfh-badge high">取证价值 高</span>
<span class="rfh-badge medium">检测价值 中</span>
<span class="rfh-badge">用户交互</span>
</div>

UserAssist 记录 Explorer 相关用户交互触发的程序执行痕迹。条目名称通常经过 ROT13 编码。

## 注册表路径

| Hive | Path |
|---|---|
| `NTUSER.DAT` | `Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist\{GUID}\Count` |

## 取证含义

UserAssist 可提示用户通过 Explorer、开始菜单、快捷方式等方式触发过某些程序。它比“程序存在”更接近用户交互，但仍然不是所有执行行为的完整记录。

## 可以证明

- 某用户 profile 中存在与程序交互相关的记录。
- 条目可能包含运行次数、最后运行时间等解析字段。
- 路径或名称经 ROT13 还原后可用于定位程序。

## 不能证明

- 程序一定由用户双击启动。
- 所有程序执行都会进入 UserAssist。
- 运行次数一定等于真实执行次数。

## 时间戳说明

不同 Windows 版本和解析工具对字段解释可能不同。报告中应标注解析工具和版本。

## 采集方式

```text
RECmd.exe -f NTUSER.DAT --bn BatchExamples\UserAssist.reb
```

## 交叉验证

- Prefetch
- Amcache
- Jump Lists
- LNK
- ShellBags
- Security and Sysmon process creation logs

