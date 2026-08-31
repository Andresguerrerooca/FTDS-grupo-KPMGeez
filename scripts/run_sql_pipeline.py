#!/usr/bin/env python3
"""Ejecuta los scripts SQL numerados contra PostgreSQL."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from course_project.db import create_db_engine  # noqa: E402
from course_project.sql_runner import run_sql_pipeline  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Ejecuta sql/*.sql en orden. Detiene e informa del archivo que falle."
    )
    parser.add_argument("--sql-dir", default="sql", help="Directorio de scripts numerados.")
    parser.add_argument(
        "--continue-on-error",
        action="store_true",
        help="No detiene el pipeline al primer error (sigue registrando fallos).",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    sql_dir = Path(args.sql_dir)
    if not sql_dir.is_absolute():
        sql_dir = ROOT / sql_dir
    engine = create_db_engine()
    results = run_sql_pipeline(
        engine,
        sql_dir=sql_dir,
        stop_on_error=not args.continue_on_error,
    )
    exit_code = 0
    for item in results:
        if item.ok:
            print(f"OK   {item.path.name}")
        else:
            exit_code = 1
            print(f"FAIL {item.path.name}")
            print(f"     {item.error}")
    if not results:
        print("No se encontraron scripts SQL numerados.")
        return 1
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
