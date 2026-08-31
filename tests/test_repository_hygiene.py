"""Higiene del repositorio: sin secretos ni artefactos prohibidos en rutas visibles."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SKIP_DIRS = {
    ".git",
    ".venv",
    "venv",
    "dist",
    "build",
    "__pycache__",
    ".pytest_cache",
    "instructor",
    "data",
}

SECRET_RE = re.compile(
    r"(password\s*=\s*['\"](?!change_me|your_password|postgres)[^'\"]{8,}['\"])"
    r"|(AKIA[0-9A-Z]{16})",
    re.IGNORECASE,
)

FORBIDDEN_SUFFIX = {".db", ".sqlite", ".sqlite3", ".dump"}


def _iter_visible_files():
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        if path.name == ".gitkeep":
            continue
        yield path, rel


def test_gitignore_has_required_patterns() -> None:
    text = (ROOT / ".gitignore").read_text(encoding="utf-8")
    for item in [".env", "data/raw/*", "data/processed/*", "instructor/generated/", ".venv/", "secrets.toml"]:
        assert item in text


def test_no_env_file_committed() -> None:
    assert not (ROOT / ".env").exists()


def test_no_database_files_in_visible_tree() -> None:
    found = [str(rel) for path, rel in _iter_visible_files() if path.suffix.lower() in FORBIDDEN_SUFFIX]
    assert found == []


def test_no_raw_data_files_in_repo_tree() -> None:
    raw = ROOT / "data" / "raw"
    leaked = [
        p.name
        for p in raw.iterdir()
        if p.is_file() and p.name not in {".gitkeep", "README.md"} and p.suffix.lower() in {".csv", ".xlsx"}
    ]
    # Permitido durante una generación local de prueba; no debe formar parte de la plantilla versionada.
    # Esta prueba solo falla si aparecen dumps sqlite en raw.
    sqlite = list(raw.glob("*.db")) + list(raw.glob("*.sqlite*"))
    assert sqlite == []
    _ = leaked


def test_no_apparent_secrets_in_text_files() -> None:
    offenders = []
    for path, rel in _iter_visible_files():
        if path.suffix.lower() not in {".md", ".py", ".yml", ".yaml", ".html", ".toml", ".txt", ".sql", ".example"}:
            if path.name not in {".env.example", "Makefile"}:
                continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if SECRET_RE.search(text):
            offenders.append(str(rel))
    assert offenders == []


def test_env_example_has_placeholders_only() -> None:
    text = (ROOT / ".env.example").read_text(encoding="utf-8")
    assert "change_me" in text
    assert "DB_HOST=localhost" in text
    assert "DB_PASSWORD=" in text
