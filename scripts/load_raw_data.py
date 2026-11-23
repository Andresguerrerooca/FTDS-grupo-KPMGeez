#!/usr/bin/env python3
"""Carga los ficheros fuente a las tablas de staging en PostgreSQL."""

from __future__ import annotations

import argparse
import sys
from io import StringIO
from pathlib import Path

import pandas as pd
from sqlalchemy import inspect, text

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from course_project.db import create_db_engine  # noqa: E402

EXCEL_TABLES = {"shipments", "suppliers"}
TABLE_ORDER = [
    "geography",
    "categories",
    "suppliers",
    "customers",
    "products",
    "orders",
    "order_items",
    "payments",
    "shipments",
    "returns",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Carga CSV/Excel de data/raw en el esquema staging."
    )
    parser.add_argument("--input", default="data/raw", help="Directorio de ficheros fuente.")
    parser.add_argument("--schema", default="staging", help="Esquema de destino.")
    parser.add_argument(
        "--if-exists",
        default="replace",
        choices=["replace", "append", "fail"],
        help="Comportamiento si la tabla ya tiene datos en pandas.to_sql (fallback).",
    )
    return parser.parse_args()


def _read_table(input_dir: Path, name: str) -> pd.DataFrame:
    if name in EXCEL_TABLES:
        path = input_dir / f"{name}.xlsx"
        if not path.exists():
            raise FileNotFoundError(f"No se encuentra {path}. Coloca los ficheros fuente en {input_dir}.")
        return pd.read_excel(path, sheet_name=name, engine="openpyxl", dtype=str)
    path = input_dir / f"{name}.csv"
    if not path.exists():
        raise FileNotFoundError(f"No se encuentra {path}. Coloca los ficheros fuente en {input_dir}.")
    return pd.read_csv(path, encoding="utf-8", dtype=str, keep_default_na=False)


def _copy_frame(engine, schema: str, table: str, frame: pd.DataFrame) -> None:
    columns = list(frame.columns)
    col_sql = ", ".join(f'"{c}"' for c in columns)
    buf = StringIO()
    frame.to_csv(buf, index=False, header=False, lineterminator="\n")
    buf.seek(0)
    raw = engine.raw_connection()
    try:
        cursor = raw.cursor()
        copy_sql = (
            f'COPY {schema}.{table} ({col_sql}) FROM STDIN WITH (FORMAT CSV, NULL \'\')'
        )
        try:
            with cursor.copy(copy_sql) as copy:
                copy.write(buf.getvalue())
        except Exception:
            # Fallback si las tablas staging aún no existen o COPY no está disponible.
            raise
        raw.commit()
    finally:
        raw.close()


def main() -> int:
    args = parse_args()
    input_dir = Path(args.input)
    if not input_dir.is_absolute():
        input_dir = ROOT / input_dir
    engine = create_db_engine()
    if engine.dialect.name != "postgresql":
        print(
            "Aviso: este cargador está pensado para PostgreSQL. "
            "SQLite solo se admite con justificación técnica documentada."
        )
    inspector = inspect(engine)
    existing = set(inspector.get_table_names(schema=args.schema)) if engine.dialect.name == "postgresql" else set()

    for name in TABLE_ORDER:
        frame = _read_table(input_dir, name)
        print(f"Cargando {name} ({len(frame)} filas)...")
        if engine.dialect.name == "postgresql" and name in existing:
            with engine.begin() as connection:
                connection.execute(text(f'TRUNCATE TABLE {args.schema}.{name}'))
            try:
                _copy_frame(engine, args.schema, name, frame)
                continue
            except Exception as exc:  # noqa: BLE001
                print(
                    f"COPY no disponible para {name} ({exc.__class__.__name__}). "
                    "Se usa un fallback más lento. ¿Existen las tablas staging y coinciden las columnas?"
                )
        frame.to_sql(
            name,
            engine,
            schema=args.schema if engine.dialect.name == "postgresql" else None,
            if_exists=args.if_exists,
            index=False,
            method="multi",
            chunksize=1000,
        )
    print("Carga de staging finalizada.")
    print("Siguiente paso: ejecutar las transformaciones SQL hacia core.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())