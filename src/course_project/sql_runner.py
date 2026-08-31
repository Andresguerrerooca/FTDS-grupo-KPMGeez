"""Ejecución ordenada de scripts SQL numerados."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from sqlalchemy import text
from sqlalchemy.engine import Engine

from course_project.paths import project_root


@dataclass
class SqlScriptResult:
    path: Path
    ok: bool
    error: str | None = None


def list_sql_scripts(sql_dir: Path | None = None) -> list[Path]:
    root = project_root()
    sql_dir = sql_dir or (root / "sql")
    scripts = sorted(
        path
        for path in sql_dir.glob("*.sql")
        if path.is_file() and path.name[0:2].isdigit()
    )
    return scripts


def split_sql_statements(sql_text: str) -> list[str]:
    """Separa sentencias por ';' sin pretender ser un parser SQL completo.

    Es suficiente para los scripts docentes del curso. Evita metacomandos de psql.
    """
    statements: list[str] = []
    current: list[str] = []
    for line in sql_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("--"):
            current.append(line)
            continue
        current.append(line)
        if stripped.endswith(";"):
            statement = "\n".join(current).strip()
            if statement and statement != ";":
                statements.append(statement)
            current = []
    tail = "\n".join(current).strip()
    if tail:
        statements.append(tail)
    return statements


def run_sql_file(engine: Engine, path: Path) -> None:
    sql_text = path.read_text(encoding="utf-8")
    lowered = sql_text.lower()
    if "\\copy" in lowered or "\\i " in lowered or lowered.strip().startswith("\\i"):
        raise RuntimeError(
            f"{path.name} contiene metacomandos de psql (\\i o \\copy), "
            "incompatibles con pgAdmin y con este ejecutor."
        )
    statements = split_sql_statements(sql_text)
    with engine.begin() as connection:
        for statement in statements:
            body = "\n".join(
                line
                for line in statement.splitlines()
                if not line.strip().startswith("--")
            ).strip()
            if not body or body == ";":
                continue
            connection.execute(text(statement))


def run_sql_pipeline(
    engine: Engine,
    sql_dir: Path | None = None,
    stop_on_error: bool = True,
) -> list[SqlScriptResult]:
    results: list[SqlScriptResult] = []
    for path in list_sql_scripts(sql_dir):
        try:
            run_sql_file(engine, path)
            results.append(SqlScriptResult(path=path, ok=True))
        except Exception as exc:  # noqa: BLE001 - queremos el archivo concreto
            results.append(SqlScriptResult(path=path, ok=False, error=str(exc)))
            if stop_on_error:
                break
    return results
