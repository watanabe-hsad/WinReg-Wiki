# Registry 数据模型

`data/registry/*.yml` 是注册表位置的结构化事实层。它服务于 Registry Explorer、结构化索引、覆盖矩阵和后续互链，不直接生成注册表位置正文。

## 基本原则

- Markdown 正文仍由人工维护。
- YAML 只保存可复用事实：路径、hive、value、主题、场景、artifact、工具和参考。
- 每条记录对应一个稳定 registry entry，不要求一个文件覆盖整个 hive。
- 不确定的信息写入 `version_notes`、`timestamp_notes` 或 `confidence`，不要猜默认值。

## 字段

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `id` | string | 是 | 稳定 ID，小写短横线，例如 `hklm-system-select`。 |
| `title` | string | 是 | 页面展示标题，通常是真实注册表路径。 |
| `page` | string | 建议 | 对应 Markdown 页面路径，例如 `docs/registry-tree/hklm/system/select.md`。 |
| `summary` | string | 建议 | 一句话说明该位置负责什么。 |
| `native_paths` | list | 是 | 真实注册表路径，可以有多个 live/offline 视图。 |
| `root` | string | 是 | `HKLM`、`HKCU`、`HKU`、`HKCR`、`HKCC` 等。 |
| `hive` | string | 是 | 离线 hive，例如 `SYSTEM`、`SOFTWARE`、`NTUSER.DAT`。 |
| `offline_files` | list | 建议 | 离线文件路径示例。 |
| `topics` | list | 建议 | 中文主题，例如 `系统配置`、`持久化`、`网络`、`账户`、`设备`。 |
| `category` | string | 建议 | 更具体的中文分类。 |
| `evidence_types` | list | 建议 | 证据类型，例如 `服务配置`、`卷映射`、`SID 映射`。 |
| `values` | list | 建议 | value name、type、meaning、common_data、notes。 |
| `subkeys` | list | 可选 | 常见子键名称和含义。 |
| `default_state` | string | 可选 | 默认状态或常见状态；不确定时写版本相关。 |
| `version_notes` | string | 可选 | 明确版本差异或“视版本而定”。 |
| `timestamp_notes` | string | 建议 | 时间戳语义，避免把 key LastWrite 写成某个 value 的修改时间。 |
| `forensic_notes` | list | 建议 | 2 到 4 条短事实提示。 |
| `common_misreads` | list | 建议 | 常见误读。 |
| `related_scenarios` | list | 建议 | 相关取证场景，使用 `title` 和 `path`。 |
| `related_registry_pages` | list | 建议 | 上下游或同类注册表位置。 |
| `related_artifacts` | list | 可选 | 相关 artifact YAML 的 `id`。 |
| `tools` | list | 可选 | Registry Explorer、RECmd、KAPE、Velociraptor 等。 |
| `references` | list | 建议 | `title` + `url`，优先官方和成熟 DFIR 资料。 |
| `status` | string | 是 | `draft`、`reviewed`、`stable`。 |
| `confidence` | string | 是 | `low`、`medium`、`high`，表示资料把握程度，不表示取证价值。 |

## values 示例

```yaml
values:
  - name: Current
    type: REG_DWORD
    meaning: 当前启动后映射为 CurrentControlSet 的控制集编号。
    common_data: 控制集编号
    notes: 离线分析时优先读取。
```

## 场景链接示例

```yaml
related_scenarios:
  - title: 常规注册表检查
    path: docs/questions/registry-checklist.md
```

## Artifact 关系

artifact YAML 保留在 `data/artifacts/*.yml`。当 artifact 与 registry entry 有明确关系时，在 artifact YAML 中增加：

```yaml
registry_entry_ids:
  - hklm-system-controlset-services
```

规则：

- 不删除 artifact 旧字段。
- 不把 artifact 页面重新变成主入口。
- registry entry 解释 key / value 是什么；artifact 补充采集、解析工具、误判和交叉验证。

## 生成命令

```bash
.venv/bin/python scripts/generate-registry-index.py
```

输出：

- `docs/registry-tree/generated-index.md`
- `docs/registry-tree/coverage.md`
- `docs/assets/registry-index.json`

`generated-index.md`、`coverage.md` 和 `registry-index.json` 都是生成文件，不要手工编辑。`docs/registry-tree/explorer.md` 是人工维护页面，通过 `docs/javascripts/registry-explorer.js` 读取 JSON 并渲染筛选卡片。
