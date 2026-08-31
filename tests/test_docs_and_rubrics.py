"""Rúbricas equivalentes, enlaces y cobertura documental."""

from __future__ import annotations

import re
from pathlib import Path

import pytest

import validate_project

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def validator():
    return validate_project


def test_rubrics_match_and_sum_100(validator) -> None:
    result = validator.CheckResult()
    validator.check_rubrics(ROOT, result)
    assert result.errors == []


def test_special_rules_present(validator) -> None:
    result = validator.CheckResult()
    validator.check_special_rules(ROOT, result)
    assert result.errors == []


def test_markdown_links(validator) -> None:
    result = validator.CheckResult()
    validator.check_markdown_links(ROOT, result)
    assert result.errors == []


def test_git_guide_coverage(validator) -> None:
    result = validator.CheckResult()
    validator.check_git_guide(ROOT, result)
    assert result.errors == []


def test_sql_templates(validator) -> None:
    result = validator.CheckResult()
    validator.check_sql_templates(ROOT, result)
    assert result.errors == []


def test_readme_lists_main_docs() -> None:
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    for relative in [
        "docs/README.md",
        "docs/01_descripcion_del_caso.md",
        "docs/05_git_guia_practica.md",
        "docs/entregables/entrega_1_bbdd_sql.md",
        "docs/entregables/rubrica_entrega_1.md",
        "docs/entregables/entrega_2_dashboard.md",
        "docs/entregables/rubrica_entrega_2.md",
        "config/course_config.example.yml",
    ]:
        assert relative.replace("\\", "/") in text.replace("\\", "/")


def test_student_docs_do_not_link_private_logs() -> None:
    forbidden = re.compile(r"anomaly_log|instructor/generated|notas_privadas", re.I)
    for path in (ROOT / "docs").rglob("*"):
        if path.suffix.lower() not in {".md", ".html"}:
            continue
        text = path.read_text(encoding="utf-8")
        assert not forbidden.search(text), path
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "anomaly_log" not in readme
    assert "instructor/generated" not in readme
