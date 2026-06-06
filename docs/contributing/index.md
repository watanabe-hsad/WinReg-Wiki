# 贡献指南

WinReg Wiki 的目标是提供 Windows 注册表 key / value 的速查说明和注册表相关取证线索。新增内容应保持查询导向，避免写成博客、课程、应急响应手册或攻击手法说明。

## 内容定位

| 内容类型 | 作用 |
|---|---|
| 注册表位置 | 主入口。解释 key / value 的路径、来源 hive、作用、常见值、注意事项和相关场景。 |
| 取证场景 | 辅助入口。按调查问题组织检查清单，主链接应指向注册表位置页面。 |
| Artifact 补充 | 内部 / 补充层。保留字段语义、采集、解析工具、误判和结构化 YAML 数据。 |
| Registry YAML | 结构化事实层。为注册表位置生成索引、覆盖矩阵和后续互链，不直接生成正文。 |

## 写作风格

- 中文为主，技术名、路径、value name、工具名保留英文。
- 页面像字段说明，不写长篇叙事。
- 优先写事实：路径、value 名称、类型、含义、离线 hive、常见状态、版本差异、注意事项。
- 避免主观优先级措辞。具体禁用词由 `scripts/check-content-style.py` 检查。
- 不确定的信息写“视 Windows 版本、角色和配置而定”，不要猜默认值。

## 注册表位置页面

建议结构：

```markdown
# HKLM\...

## 位置

## 离线位置

## 作用

## 常见子键和值

## 默认状态与版本差异

## 注意事项

## 取证提示

## 相关场景

## 相关位置

## 补充阅读
```

要求：

- `## 位置` 写 live path 或 native registry path。
- `## 离线位置` 写 hive 文件，例如 `SYSTEM`、`SOFTWARE`、`NTUSER.DAT`、`UsrClass.dat`。
- `## 常见子键和值` 尽量使用表格，列出 `名称`、`类型`、`含义`、`常见数据 / 状态`、`说明`。
- `## 取证提示` 保持 2 到 4 条短句，只说明关联问题，不展开完整分析。
- artifact 链接只放在 `## 补充阅读`，不要作为页面主路径。

## 取证场景页面

建议结构：

```markdown
# 场景名称

## 检查目标

## 优先查看的注册表位置

## 判断要点

## 交叉验证

## 常见误判

## 相关场景

## 补充阅读
```

要求：

- “优先查看的注册表位置”表格主链接指向 `docs/registry-tree/`。
- artifact 只放在 `补充阅读`，用于字段细节、工具解析和采集注意。
- 不把取证结论写过头：配置存在、程序存在、用户交互、执行成功、设备接入、文件复制是不同强度的说法。

## 来源质量

优先级：

| 优先级 | 来源 |
|---|---|
| 1 | Microsoft Learn、Microsoft Sysinternals、Windows 官方文档。 |
| 2 | SANS DFIR 速查表、Eric Zimmerman 工具文档、成熟 DFIR 工具文档。 |
| 3 | artefacts.help 等可核验 artifact 资料。 |
| 4 | 个人博客或厂商文章，只能作为辅助线索，不应作为唯一来源。 |

引用原则：

- 不大段复制资料，只提炼字段事实并给链接。
- 如果行为和版本有关，应写明版本；无法确认时写“视版本而定”。
- 如果结论来自工具解析经验，应标注工具名，例如 Registry Explorer、RECmd、KAPE、Velociraptor。

## 时间戳原则

- key LastWrite 是 key 级变化时间，不是某个 value 的独立创建时间。
- 多个 value 共用同一个 key LastWrite 时，不能把它直接归因给其中一个 value。
- 工具解析出的时间字段需要说明格式和来源，例如 FILETIME、Unix epoch、DHCP 租约字段。
- 报告中应记录解析工具和版本，尤其是 UserAssist、ComDlg32、ShellBags、Amcache、ShimCache 等结构化 artifact。

## 文件命名

- 文件名和 URL 使用英文 kebab-case。
- 页面标题和导航展示中文为主，路径和技术名保留英文。
- 注册表路径层级尽量贴近 Windows 原生树，例如 `hklm/system/controlset/services/`。
- 有 `index.md` 的目录应作为可点击 section index，不使用“概览”作为子项标题。

## Artifact 与 YAML

- 不新增 artifact 主入口。
- 如果新增或修改 artifact 页面，尽量同步 `data/artifacts/*.yml`。
- `docs/artifacts/generated-index.md` 由 `scripts/generate-artifact-index.py` 生成，不要手工改生成表格。
- 如果 artifact 内容已经迁移到注册表位置或取证场景，artifact 页面应压缩为补充条目。

## Registry 数据模型

- `data/registry/*.yml` 保存注册表位置的结构化事实，字段说明见 [Registry 数据模型](registry-data-schema.md)。
- `docs/registry-tree/generated-index.md` 和 `docs/registry-tree/coverage.md` 由 `scripts/generate-registry-index.py` 生成，不要手工编辑生成内容。
- Markdown 正文仍由人工维护；YAML 只补路径、hive、主题、字段、关联场景、关联 artifact、工具和参考。
- artifact YAML 可以通过 `registry_entry_ids` 关联 registry entry。这个字段用于索引和维护关系，不改变 artifact 页面补充层定位。

## 提交前检查

```bash
.venv/bin/python scripts/generate-artifact-index.py
.venv/bin/python scripts/generate-registry-index.py
.venv/bin/python scripts/check-content-style.py
.venv/bin/mkdocs build --strict
```

如果 `mkdocs build --strict` 只出现 Material for MkDocs 关于上游 MkDocs 2.0 的提示，且构建成功，可以视为非项目错误。

## License 状态

当前 License 仍为 `TBD`，等待维护者确认。可选方向：

- 文档内容使用 `CC BY 4.0`，脚本和站点工程使用 `MIT`。
- 如果希望简单，也可以全仓库先使用 `MIT`。

在维护者明确选择前，不新增 `LICENSE` 文件。
