#!/usr/bin/env python3
"""Lightweight content style checks for WinReg Wiki."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class Rule:
    name: str
    needles: tuple[str, ...]
    paths: tuple[str, ...]
    allow: tuple[str, ...] = ()


RULES = (
    Rule(
        name="旧 artifact 主入口标题",
        needles=("相关 Artifact",),
        paths=("docs", "README.md", "PROJECT_STATUS.md", "ROADMAP.md", "CHANGELOG.md"),
    ),
    Rule(
        name="英文 artifact 模板标题",
        needles=(
            "What It Can Prove",
            "What It Cannot Prove",
            "Forensic Meaning",
            "Detection Ideas",
            "Attacker Usage",
        ),
        paths=("docs", "README.md", "PROJECT_STATUS.md", "ROADMAP.md", "CHANGELOG.md"),
    ),
    Rule(
        name="主观优先级措辞",
        needles=("高价值", "非常重要", "强烈建议", "重点关注"),
        paths=("docs", "README.md", "PROJECT_STATUS.md", "ROADMAP.md", "CHANGELOG.md"),
    ),
    Rule(
        name="旧项目显示名",
        needles=("Windows Registry Forensics Handbook",),
        paths=("docs", "README.md", "PROJECT_STATUS.md", "ROADMAP.md", "CHANGELOG.md", "mkdocs.yml"),
    ),
    Rule(
        name="旧仓库地址",
        needles=("watanabe-hsad/windows-registry-forensics-handbook",),
        paths=("docs", "README.md", "PROJECT_STATUS.md", "ROADMAP.md", "CHANGELOG.md", "mkdocs.yml"),
    ),
    Rule(
        name="旧仓库路径片段",
        needles=("windows-registry-forensics-handbook",),
        paths=("docs", "README.md", "PROJECT_STATUS.md", "ROADMAP.md", "CHANGELOG.md", "mkdocs.yml"),
        allow=(
            "README.md",
            "PROJECT_STATUS.md",
            "CHANGELOG.md",
            "mkdocs.yml",
        ),
    ),
)


TEXT_SUFFIXES = {".md", ".yml", ".yaml", ".py", ".txt"}


def iter_files(rule: Rule) -> list[Path]:
    files: list[Path] = []
    for raw in rule.paths:
        path = ROOT / raw
        if not path.exists():
            continue
        if path.is_file():
            files.append(path)
            continue
        for child in path.rglob("*"):
            if child.is_file() and child.suffix in TEXT_SUFFIXES:
                files.append(child)
    return sorted(set(files))


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def main() -> int:
    hits: list[str] = []

    for rule in RULES:
        for path in iter_files(rule):
            relative = rel(path)
            if relative in rule.allow:
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            for lineno, line in enumerate(text.splitlines(), start=1):
                for needle in rule.needles:
                    if needle in line:
                        hits.append(f"{relative}:{lineno}: {rule.name}: {needle}")

    if hits:
        print("Content style check failed:")
        for hit in hits:
            print(f"- {hit}")
        return 1

    print("Content style check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
