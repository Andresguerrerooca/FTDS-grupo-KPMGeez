#!/usr/bin/env python3
"""Valida enlaces, rúbricas, higiene, SQL y coherencia documental del proyecto."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

MD_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
CRITERION_MD_RE = re.compile(
    r"^###\s+([A-Z]\d+)\.\s+(.+?)\s+\((\d+)\s+puntos?\)\s*$",
    re.MULTILINE,
)
CRITERION_HTML_RE = re.compile(
    r'<th\s+scope="row">([A-Z]\d+)\.\s+([^<]+)</th>\s*<td[^>]*>\s*(\d+)\s*</td>',
    re.IGNORECASE,
)


class CheckResult:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)

    @property
    def ok(self) -> bool:
        return not self.errors


def _skip_link(target: str) -> bool:
    t = target.strip()
    if t.startswith(("http://", "https://", "mailto:", "#")):
        return True
    if t.startswith("git@") or t.startswith("ssh://"):
        return True
    return False


def check_markdown_links(root: Path, result: CheckResult) -> None:
    for path in root.rglob("*.md"):
        rel = path.relative_to(root)
        if any(part in {".venv", "dist", "build", ".git"} for part in rel.parts):
            continue
        text = path.read_text(encoding="utf-8")
        for match in MD_LINK_RE.finditer(text):
            target = match.group(1).split()[0].strip("<>")
            if _skip_link(target):
                continue
            target_path = target.split("#", 1)[0]
            if not target_path:
                continue
            resolved = (path.parent / target_path).resolve()
            try:
                resolved.relative_to(root.resolve())
            except ValueError:
                # enlace fuera del repo; solo se comprueba existencia
                pass
            if not resolved.exists():
                result.error(f"Enlace roto en {rel}: {target}")


def _parse_md_criteria(path: Path) -> list[tuple[str, str, int]]:
    text = path.read_text(encoding="utf-8")
    found = CRITERION_MD_RE.findall(text)
    return [(cid, name.strip(), int(weight)) for cid, name, weight in found]


def _parse_html_criteria(path: Path) -> list[tuple[str, str, int]]:
    text = path.read_text(encoding="utf-8")
    found = CRITERION_HTML_RE.findall(text)
    return [(cid, name.strip(), int(weight)) for cid, name, weight in found]


def check_rubrics(root: Path, result: CheckResult) -> None:
    pairs = [
        (
            root / "docs/entregables/rubrica_entrega_1.md",
            root / "docs/entregables/rubrica_entrega_1_canvas.html",
        ),
        (
            root / "docs/entregables/rubrica_entrega_2.md",
            root / "docs/entregables/rubrica_entrega_2_canvas.html",
        ),
    ]
    for md_path, html_path in pairs:
        if not md_path.exists():
            result.error(f"Falta {md_path.relative_to(root)}")
            continue
        if not html_path.exists():
            result.error(f"Falta {html_path.relative_to(root)}")
            continue
        md_items = _parse_md_criteria(md_path)
        html_items = _parse_html_criteria(html_path)
        if not md_items:
            result.error(f"No se leyeron criterios en {md_path.name}")
        md_sum = sum(item[2] for item in md_items)
        html_sum = sum(item[2] for item in html_items)
        if md_sum != 100:
            result.error(f"{md_path.name} suma {md_sum} puntos, no 100.")
        if html_sum != 100:
            result.error(f"{html_path.name} suma {html_sum} puntos, no 100.")
        md_pairs = [(i[0], i[1], i[2]) for i in md_items]
        html_pairs = [(i[0], i[1], i[2]) for i in html_items]
        if md_pairs != html_pairs:
            result.error(
                f"Criterios o pesos distintos entre {md_path.name} y {html_path.name}: "
                f"MD={md_pairs} HTML={html_pairs}"
            )


def check_special_rules(root: Path, result: CheckResult) -> None:
    e1 = (root / "docs/entregables/rubrica_entrega_1.md").read_text(encoding="utf-8")
    e1h = (root / "docs/entregables/rubrica_entrega_1_canvas.html").read_text(encoding="utf-8")
    e2 = (root / "docs/entregables/rubrica_entrega_2.md").read_text(encoding="utf-8")
    e2h = (root / "docs/entregables/rubrica_entrega_2_canvas.html").read_text(encoding="utf-8")
    for label, text in [("rúbrica 1 MD", e1), ("rúbrica 1 HTML", e1h)]:
        if "0 puntos sobre 40" not in text and "0/40" not in text:
            result.error(f"{label}: falta la regla de 0 sobre 40 de la parte técnica.")
        if "7/10" not in text:
            result.error(f"{label}: falta el máximo 7/10 por no defender oralmente.")
        if "SQLite" not in text:
            result.error(f"{label}: falta la regla sobre SQLite justificado.")
    for label, text in [("rúbrica 2 MD", e2), ("rúbrica 2 HTML", e2h)]:
        if "8/10" not in text:
            result.error(f"{label}: falta el máximo 8/10 por no defender oralmente.")
        if "SQLite" not in text:
            result.error(f"{label}: falta la regla sobre SQLite justificado.")
        if "CSV" not in text and "ficheros" not in text.lower():
            result.error(f"{label}: falta la regla sobre no sustituir la conexión por ficheros.")


def check_sql_templates(root: Path, result: CheckResult) -> None:
    sql_dir = root / "sql"
    for path in sorted(sql_dir.glob("*.sql")):
        original = path.read_text(encoding="utf-8")
        code_only = "\n".join(
            line
            for line in original.splitlines()
            if not line.strip().startswith("--")
        )
        lowered = code_only.lower()
        if "\\copy" in lowered or re.search(r"(^|\s)\\i\b", lowered):
            result.error(f"{path.name} usa metacomandos de psql (\\i o \\copy).")
        for marker in ["objetivo", "dependencias", "todo"]:
            if marker not in original.lower():
                result.error(f"{path.name} no incluye el marcador pedagógico '{marker}'.")


def check_gitignore(root: Path, result: CheckResult) -> None:
    text = (root / ".gitignore").read_text(encoding="utf-8")
    required = [
        ".env",
        "data/raw/*",
        "data/processed/*",
        "instructor/generated/",
        "dist/",
        ".venv/",
        "__pycache__/",
        ".sqlite",
        "secrets.toml",
    ]
    for item in required:
        if item not in text:
            result.error(f".gitignore no contiene el patrón esperado: {item}")


def check_hygiene(root: Path, result: CheckResult) -> None:
    secret_re = re.compile(
        r"(password\s*=\s*['\"](?!change_me|your_password|postgres|dev@)[^'\"]{8,}['\"])"
        r"|(api[_-]?key\s*=\s*['\"][A-Za-z0-9_\-]{16,}['\"])",
        re.IGNORECASE,
    )
    skip_dirs = {".git", ".venv", "dist", "build", "instructor", "__pycache__", "data"}
    forbidden_suffix = {".db", ".sqlite", ".sqlite3", ".dump"}
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(root)
        if any(part in skip_dirs for part in rel.parts):
            continue
        if path.suffix in forbidden_suffix:
            result.error(f"Archivo de base de datos en material visible: {rel}")
        if path.name == ".env":
            result.error("Existe un archivo .env en el repositorio de trabajo.")
        if path.suffix in {".md", ".py", ".yml", ".yaml", ".html", ".toml", ".txt", ".sql"}:
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            if secret_re.search(text) and path.name not in {"validate_project.py", "test_repository_hygiene.py"}:
                result.error(f"Posible secreto en {rel}")


def check_config_placeholders(root: Path, result: CheckResult) -> None:
    path = root / "config" / "course_config.example.yml"
    text = path.read_text(encoding="utf-8")
    for token in (
        "[FECHA_ENTREGA_1]",
        "[FECHA_ENTREGA_2]",
        "[DURACION_PRESENTACION_1]",
        "[DURACION_PRESENTACION_2]",
    ):
        if token not in text:
            result.error(f"Falta el marcador {token} en {path.name}")


def check_git_guide(root: Path, result: CheckResult) -> None:
    text = (root / "docs" / "05_git_guia_practica.md").read_text(encoding="utf-8")
    commands = [
        "git status",
        "git add",
        "git commit",
        "git log",
        "git diff",
        "git pull",
        "git push",
        "git branch",
        "git switch",
        "git merge",
        "git restore",
    ]
    for cmd in commands:
        if cmd not in text:
            result.error(f"La guía de Git no menciona {cmd}.")
    if "git push --force" not in text and "git push --force" not in text.lower():
        # Debe advertir, no recomendar. Comprobamos que aparece la advertencia.
        if "force" not in text.lower() or "reset --hard" not in text:
            result.error("La guía de Git debe advertir contra push --force y reset --hard.")
    if ".env" not in text or ".venv" not in text:
        result.error("La guía de Git debe prohibir subir .env y .venv.")


def check_data_if_present(root: Path, result: CheckResult) -> None:
    raw = root / "data" / "raw"
    csv_files = list(raw.glob("*.csv"))
    xlsx_files = [p for p in raw.glob("*.xlsx") if p.name != "data_dictionary.xlsx"]
    if not csv_files:
        result.warn("No hay datos en data/raw; se omite la validación de diccionario y relectura.")
        return
    try:
        import pandas as pd
        from course_project.data_generation.schema import EXCEL_TABLES, SCHEMAS, TABLE_ORDER
    except Exception as exc:  # noqa: BLE001
        result.warn(f"No se pudo importar pandas/schema para validar datos: {exc}")
        return
    dict_path = raw / "data_dictionary.xlsx"
    if not dict_path.exists():
        result.error("Existen ficheros en data/raw pero falta data_dictionary.xlsx.")
        return
    try:
        sheets = pd.ExcelFile(dict_path, engine="openpyxl").sheet_names
    except Exception as exc:  # noqa: BLE001
        result.error(f"No se pudo leer el diccionario: {exc}")
        return
    if "README" not in sheets:
        result.error("El diccionario no tiene pestaña README.")
    for table in TABLE_ORDER:
        source = raw / (f"{table}.xlsx" if table in EXCEL_TABLES else f"{table}.csv")
        if not source.exists():
            result.error(f"Falta el fichero fuente {source.name}.")
            continue
        try:
            if table in EXCEL_TABLES:
                frame = pd.read_excel(source, sheet_name=table, engine="openpyxl")
            else:
                frame = pd.read_csv(source, encoding="utf-8")
        except Exception as exc:  # noqa: BLE001
            result.error(f"No se pudo releer {source.name}: {exc}")
            continue
        expected = [col.column_name for col in SCHEMAS[table]]
        actual = list(frame.columns)
        if actual != expected:
            result.error(f"Cabeceras de {source.name} distintas del esquema: {actual} vs {expected}")
        if table not in sheets:
            result.error(f"El diccionario no tiene pestaña {table}.")
        else:
            dict_cols = list(pd.read_excel(dict_path, sheet_name=table, engine="openpyxl")["column_name"])
            if dict_cols != actual:
                result.error(f"Diccionario de {table} no coincide con el fichero.")


def check_commands(root: Path, result: CheckResult) -> None:
    readme = (root / "README.md").read_text(encoding="utf-8")
    required_snippets = [
        "scripts/generate_data.py --profile demo",
        "scripts/generate_data.py --profile full",
        "scripts/build_student_release.py",
        "scripts/validate_project.py",
        "streamlit run app/Home.py",
        "pytest",
    ]
    for snippet in required_snippets:
        if snippet not in readme:
            result.error(f"README no documenta el comando esperado: {snippet}")
    makefile = (root / "Makefile").read_text(encoding="utf-8")
    for target in ["install", "demo-data", "full-data", "test", "validate", "release", "streamlit"]:
        if target not in makefile:
            result.error(f"Makefile no contiene el objetivo {target}.")


def run_checks(root: Path) -> CheckResult:
    result = CheckResult()
    check_markdown_links(root, result)
    check_rubrics(root, result)
    check_special_rules(root, result)
    check_sql_templates(root, result)
    check_gitignore(root, result)
    check_hygiene(root, result)
    check_config_placeholders(root, result)
    check_git_guide(root, result)
    check_data_if_present(root, result)
    check_commands(root, result)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Valida el repositorio docente FTDS.")
    parser.add_argument("--root", default=str(ROOT), help="Raíz del proyecto.")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    result = run_checks(root)
    for warning in result.warnings:
        print(f"AVISO  {warning}")
    for error in result.errors:
        print(f"ERROR  {error}")
    if result.ok:
        print("Validación correcta.")
        return 0
    print(f"Validación con {len(result.errors)} error(es).")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
