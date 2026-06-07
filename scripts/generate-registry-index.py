#!/usr/bin/env python3
"""Generate registry-tree structured index pages from data/registry/*.yml."""

from __future__ import annotations

from collections import defaultdict
import json
import os
from pathlib import Path
import sys

try:
    import yaml
except ImportError:
    print("Install PyYAML to use this script: pip install pyyaml", file=sys.stderr)
    raise SystemExit(1)


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "registry"
DOCS_DIR = ROOT / "docs"
REGISTRY_TREE_DIR = DOCS_DIR / "registry-tree"
GENERATED_INDEX = REGISTRY_TREE_DIR / "generated-index.md"
COVERAGE = REGISTRY_TREE_DIR / "coverage.md"
REGISTRY_JSON = DOCS_DIR / "assets" / "registry-index.json"

REQUIRED_FIELDS = ("id", "title", "native_paths", "root", "hive")
STATUS_LABELS = {
    "draft": "草稿",
    "reviewed": "已审阅",
    "stable": "稳定",
}
CONFIDENCE_LABELS = {
    "low": "低",
    "medium": "中",
    "high": "高",
}


def as_list(value: object) -> list[object]:
    if value is None:
        return []
    if isinstance(value, list):
        return [item for item in value if item is not None]
    return [value]


def as_text_list(value: object) -> list[str]:
    return [str(item) for item in as_list(value)]


def md_escape(value: object) -> str:
    return str(value or "").replace("|", "\\|").replace("\n", " ")


def code(value: object) -> str:
    text = md_escape(value)
    if not text:
        return ""
    escaped = text.replace("`", "\\`")
    return f"`{escaped}`"


def badge(value: object, kind: str = "") -> str:
    label = md_escape(value)
    klass = f"ww-chip ww-chip--{kind}" if kind else "ww-chip"
    return f'<span class="{klass}">{label}</span>'


def path_pill(value: object) -> str:
    text = md_escape(value)
    return f'<span class="ww-path-pill">{text}</span>'


def rel_doc(path: str | object) -> str:
    return str(path or "").replace("\\", "/")


def link_to_doc(label: object, path: object, from_dir: Path = REGISTRY_TREE_DIR) -> str:
    text = md_escape(label)
    rel_path = rel_doc(path)
    if not rel_path:
        return text
    target = ROOT / rel_path
    href = os.path.relpath(target, start=from_dir).replace(os.sep, "/")
    return f"[{text}]({href})"


def site_path(path: object) -> str:
    rel_path = rel_doc(path)
    if rel_path.startswith("docs/"):
        rel_path = rel_path[5:]
    if rel_path.endswith("/index.md"):
        return rel_path[: -len("index.md")]
    if rel_path.endswith(".md"):
        return f"{rel_path[:-3]}/"
    return rel_path


def explorer_href(path: object) -> str:
    target = site_path(path)
    if not target:
        return ""
    if target.startswith("registry-tree/"):
        return f"../{target[len('registry-tree/'):]}"
    return f"../../{target}"


def first_path(item: dict[str, object]) -> str:
    paths = as_text_list(item.get("native_paths"))
    return paths[0] if paths else ""


def topics(item: dict[str, object]) -> str:
    return " ".join(badge(topic, "topic") for topic in as_text_list(item.get("topics")))


def roots(entries: list[dict[str, object]]) -> set[str]:
    return {str(item.get("root")) for item in entries if item.get("root")}


def all_topics(entries: list[dict[str, object]]) -> set[str]:
    values: set[str] = set()
    for item in entries:
        values.update(as_text_list(item.get("topics")))
    return values


def scenario_links(item: dict[str, object]) -> str:
    links: list[str] = []
    for scenario in as_list(item.get("related_scenarios")):
        if isinstance(scenario, dict):
            links.append(link_to_doc(scenario.get("title"), scenario.get("path")))
        else:
            links.append(md_escape(scenario))
    return "<br>".join(links)


def scenario_titles(item: dict[str, object]) -> list[str]:
    values: list[str] = []
    for scenario in as_list(item.get("related_scenarios")):
        if isinstance(scenario, dict):
            title = str(scenario.get("title") or "").strip()
            if title:
                values.append(title)
        else:
            text = str(scenario).strip()
            if text:
                values.append(text)
    return values


def summarize_values(item: dict[str, object]) -> list[str]:
    names: list[str] = []
    for value in as_list(item.get("values")):
        if isinstance(value, dict) and value.get("name"):
            names.append(str(value["name"]))
    return names[:8]


def build_registry_json(entries: list[dict[str, object]]) -> dict[str, object]:
    root_values = sorted(roots(entries))
    topic_values = sorted(all_topics(entries))
    scenario_values: set[str] = set()
    status_counts: dict[str, int] = defaultdict(int)

    json_entries: list[dict[str, object]] = []
    for item in entries:
        scenarios = scenario_titles(item)
        scenario_values.update(scenarios)
        status = str(item.get("status") or "draft")
        status_counts[status] += 1

        related_pages = []
        for page in as_list(item.get("related_registry_pages")):
            if isinstance(page, dict):
                related_pages.append(
                    {
                        "title": str(page.get("title") or ""),
                        "url": explorer_href(page.get("path")),
                    }
                )

        references = []
        for ref in as_list(item.get("references")):
            if isinstance(ref, dict):
                references.append(
                    {
                        "title": str(ref.get("title") or ""),
                        "url": str(ref.get("url") or ""),
                    }
                )

        json_entries.append(
            {
                "id": str(item.get("id") or ""),
                "title": str(item.get("title") or ""),
                "summary": str(item.get("summary") or ""),
                "native_paths": as_text_list(item.get("native_paths")),
                "root": str(item.get("root") or ""),
                "hive": str(item.get("hive") or ""),
                "offline_files": as_text_list(item.get("offline_files")),
                "topics": as_text_list(item.get("topics")),
                "category": str(item.get("category") or ""),
                "evidence_types": as_text_list(item.get("evidence_types")),
                "values": summarize_values(item),
                "related_scenarios": scenarios,
                "related_registry_pages": related_pages,
                "related_artifacts": as_text_list(item.get("related_artifacts")),
                "tools": as_text_list(item.get("tools")),
                "references": references,
                "status": status,
                "confidence": str(item.get("confidence") or ""),
                "page_url": explorer_href(item.get("page")),
                "site_path": site_path(item.get("page")),
            }
        )

    return {
        "meta": {
            "generated_by": "scripts/generate-registry-index.py",
            "entries": len(entries),
            "roots": root_values,
            "topics": topic_values,
            "scenarios": sorted(scenario_values),
            "statuses": dict(sorted(status_counts.items())),
        },
        "entries": json_entries,
    }


def load_entries() -> tuple[list[dict[str, object]], list[str]]:
    entries: list[dict[str, object]] = []
    warnings: list[str] = []
    seen_ids: set[str] = set()

    for path in sorted(DATA_DIR.glob("*.yml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        if not isinstance(data, dict):
            raise ValueError(f"{path} does not contain a YAML mapping")

        for field in REQUIRED_FIELDS:
            if not data.get(field):
                raise ValueError(f"{path.relative_to(ROOT)} missing required field: {field}")

        entry_id = str(data["id"])
        if entry_id in seen_ids:
            raise ValueError(f"Duplicate registry entry id: {entry_id}")
        seen_ids.add(entry_id)

        page = data.get("page")
        if page:
            page_path = ROOT / rel_doc(page)
            if not page_path.exists():
                raise ValueError(f"{path.relative_to(ROOT)} references missing page: {page}")

        for scenario in as_list(data.get("related_scenarios")):
            if isinstance(scenario, dict) and scenario.get("path"):
                scenario_path = ROOT / rel_doc(scenario["path"])
                if not scenario_path.exists():
                    warnings.append(f"{path.relative_to(ROOT)} references missing scenario: {scenario['path']}")

        entries.append(data)

    return sorted(entries, key=lambda item: (str(item.get("root")), str(item.get("hive")), first_path(item))), warnings


def build_generated_index(entries: list[dict[str, object]]) -> str:
    root_values = roots(entries)
    topic_values = all_topics(entries)
    status_counts = {key: 0 for key in STATUS_LABELS}
    for item in entries:
        status_counts[str(item.get("status"))] = status_counts.get(str(item.get("status")), 0) + 1

    lines = [
        "<!-- This file is generated by scripts/generate-registry-index.py. Do not edit manually. -->",
        "",
        '<section class="ww-index-hero" markdown>',
        '<p class="ww-hero-eyebrow">Structured Registry Index</p>',
        '<h1>结构化注册表索引</h1>',
        '<p>本页由 <code>data/registry/*.yml</code> 生成，面向读者提供稳定的路径索引。需要搜索和筛选时，优先使用 <a href="../explorer/">Registry Explorer</a>。</p>',
        '</section>',
        "",
        '<div class="ww-dashboard-grid" markdown>',
        f'<div class="ww-stat-card"><span>registry entries</span><strong>{len(entries)}</strong><em>data/registry</em></div>',
        f'<div class="ww-stat-card"><span>root hives</span><strong>{len(root_values)}</strong><em>{", ".join(sorted(root_values))}</em></div>',
        f'<div class="ww-stat-card"><span>topics</span><strong>{len(topic_values)}</strong><em>结构化主题</em></div>',
        f'<div class="ww-stat-card"><span>status</span><strong>{status_counts.get("stable", 0)} / {status_counts.get("reviewed", 0)} / {status_counts.get("draft", 0)}</strong><em>stable / reviewed / draft</em></div>',
        "</div>",
        "",
        '<div class="ww-card-grid ww-card-grid--three" markdown>',
        '<a class="ww-feature-card ww-feature-card--index" href="../explorer/"><span class="ww-card-kicker">Filter view</span><strong>Open Registry Explorer</strong><span>按关键词、Hive、主题和状态筛选结构化 registry entry。</span></a>',
        '<a class="ww-feature-card ww-feature-card--index" href="../coverage/"><span class="ww-card-kicker">Maintenance</span><strong>Coverage Matrix</strong><span>查看结构化覆盖范围、状态和下一阶段候选路径。</span></a>',
        '<a class="ww-feature-card ww-feature-card--index" href="../"><span class="ww-card-kicker">Native tree</span><strong>Registry Tree</strong><span>回到 HKLM / HKCU / HKU / HKCR / HKCC 原生层级浏览。</span></a>',
        "</div>",
        "",
        '<div class="ww-chip-row" markdown>',
        " ".join(badge(topic, "topic") for topic in sorted(topic_values)),
        "</div>",
        "",
    ]

    by_root: dict[str, list[dict[str, object]]] = defaultdict(list)
    for item in entries:
        by_root[str(item.get("root"))].append(item)

    for root in sorted(by_root):
        lines.extend([f"## {md_escape(root)}", ""])
        lines.extend([
            "| 路径 | Hive | 主题 | 状态 | 页面 | 相关场景 |",
            "|---|---|---|---|---|---|",
        ])
        for item in by_root[root]:
            path_text = "<br>".join(path_pill(path) for path in as_text_list(item.get("native_paths"))[:2])
            summary = md_escape(item.get("summary"))
            page = link_to_doc(item.get("title"), item.get("page"))
            status = STATUS_LABELS.get(str(item.get("status")), md_escape(item.get("status")))
            lines.append(
                f"| {path_text}<br><span class=\"ww-table-note\">{summary}</span> | "
                f"{badge(item.get('hive'), 'hive')} | {topics(item)} | {badge(status, 'status')} | {page} | {scenario_links(item)} |"
            )
        lines.append("")

    by_topic: dict[str, list[dict[str, object]]] = defaultdict(list)
    for item in entries:
        for topic in as_text_list(item.get("topics")):
            by_topic[topic].append(item)

    lines.extend(["## 按主题", ""])
    lines.extend(["| 主题 | 路径 | Hive | 页面 |", "|---|---|---|---|"])
    for topic in sorted(by_topic):
        paths = "<br>".join(path_pill(first_path(item)) for item in by_topic[topic])
        pages = "<br>".join(link_to_doc(item.get("title"), item.get("page")) for item in by_topic[topic])
        hives = "<br>".join(badge(item.get("hive"), "hive") for item in by_topic[topic])
        lines.append(f"| {badge(topic, 'topic')} | {paths} | {hives} | {pages} |")

    lines.append("")
    return "\n".join(lines)


def build_coverage(entries: list[dict[str, object]]) -> str:
    status_counts: dict[str, int] = defaultdict(int)
    for item in entries:
        status_counts[str(item.get("status"))] += 1

    lines = [
        "<!-- This file is generated by scripts/generate-registry-index.py. Do not edit manually. -->",
        "",
        '<section class="ww-index-hero ww-index-hero--maintenance" markdown>',
        '<p class="ww-hero-eyebrow">Maintenance Matrix</p>',
        '<h1>注册表位置覆盖矩阵</h1>',
        '<p>本页由 <code>data/registry/*.yml</code> 生成，用于维护当前结构化覆盖范围。它不是完整 Windows 注册表清单。</p>',
        '</section>',
        "",
        '<div class="ww-dashboard-grid" markdown>',
        f'<div class="ww-stat-card"><span>entries</span><strong>{len(entries)}</strong><em>当前结构化覆盖</em></div>',
        f'<div class="ww-stat-card"><span>stable</span><strong>{status_counts.get("stable", 0)}</strong><em>可作为索引基础</em></div>',
        f'<div class="ww-stat-card"><span>reviewed</span><strong>{status_counts.get("reviewed", 0)}</strong><em>主要字段已核对</em></div>',
        f'<div class="ww-stat-card"><span>draft</span><strong>{status_counts.get("draft", 0)}</strong><em>仍需审阅</em></div>',
        "</div>",
        "",
        "## 状态说明",
        "",
        "| 状态 | 含义 |",
        "|---|---|",
        f"| {badge('草稿', 'status')} | 已有数据，但字段、引用或页面结构仍需审阅。 |",
        f"| {badge('已审阅', 'status')} | 主要字段已核对，仍可能继续补参考或版本差异。 |",
        f"| {badge('稳定', 'status')} | 当前事实层可作为后续索引和互链基础。 |",
        "",
    ]

    by_root_hive: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for item in entries:
        by_root_hive[(str(item.get("root")), str(item.get("hive")))].append(item)

    for root, hive in sorted(by_root_hive):
        lines.extend([f"## {md_escape(root)} / {md_escape(hive)}", ""])
        lines.extend([
            "| 注册表路径 | 页面 | Root | Hive | 主题 | 相关场景 | 状态 | 备注 |",
            "|---|---|---|---|---|---|---|---|",
        ])
        for item in by_root_hive[(root, hive)]:
            status = STATUS_LABELS.get(str(item.get("status")), md_escape(item.get("status")))
            confidence = CONFIDENCE_LABELS.get(str(item.get("confidence")), md_escape(item.get("confidence")))
            page = link_to_doc(item.get("title"), item.get("page"))
            note = f"资料把握：{confidence}"
            lines.append(
                f"| {path_pill(first_path(item))} | {page} | {badge(root, 'hive')} | {badge(hive, 'hive')} | "
                f"{topics(item)} | {scenario_links(item)} | {badge(status, 'status')} | {md_escape(note)} |"
            )
        lines.append("")

    lines.extend([
        "## 下一阶段候选",
        "",
        "| 注册表路径 | 状态 | 主题 | 相关场景 | 备注 |",
        "|---|---|---|---|---|",
        "| `HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System` | 待新增 | 策略 | 安全策略与防护配置 | 用户级系统策略。 |",
        "| `HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Attachments` | 待新增 | 策略 / 用户行为 | 反取证与清理痕迹 | Attachment Manager。 |",
        "| `HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Associations` | 待新增 | 策略 / Shell | Shell / Explorer 用户行为 | 文件关联策略。 |",
        "| `HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced` | 待新增 | 用户行为 / Shell | Shell / Explorer 用户行为 | Explorer 显示和行为偏好。 |",
        "| `HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\TypedPaths` | 待新增 | 用户行为 | Shell / Explorer 用户行为 | Explorer 地址栏输入历史。 |",
        "| `HKCU\\Software\\Microsoft\\Windows\\Shell\\BagMRU` | 待新增 | 用户行为 | Shell / Explorer 用户行为 | ShellBags。 |",
        "| `HKLM\\SYSTEM\\ControlSet00x\\Enum\\STORAGE` | 待新增 | 设备 | USB 与外接设备 | 存储设备枚举。 |",
        "| `HKLM\\SYSTEM\\ControlSet00x\\Control\\DeviceContainers` | 待新增 | 设备 | USB 与外接设备 | 设备容器关联。 |",
        "",
    ])
    return "\n".join(lines)


def main() -> None:
    entries, warnings = load_entries()
    GENERATED_INDEX.write_text(build_generated_index(entries), encoding="utf-8")
    COVERAGE.write_text(build_coverage(entries), encoding="utf-8")
    REGISTRY_JSON.parent.mkdir(parents=True, exist_ok=True)
    REGISTRY_JSON.write_text(
        json.dumps(build_registry_json(entries), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    for warning in warnings:
        print(f"warning: {warning}", file=sys.stderr)

    print(
        f"Generated {len(entries)} registry entries into "
        f"{GENERATED_INDEX.relative_to(ROOT)}, {COVERAGE.relative_to(ROOT)}, "
        f"and {REGISTRY_JSON.relative_to(ROOT)}"
    )


if __name__ == "__main__":
    main()
