#!/usr/bin/env python3
"""Construye un paquete de distribución para el alumnado, sin material privado."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

EXCLUDE_DIR_NAMES = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    "dist",
    "build",
    "htmlcov",
    "instructor",
    "data_generation",
}
EXCLUDE_FILE_NAMES = {
    ".env",
    "secrets.toml",
    "generate_data.py",
}
EXCLUDE_SUFFIXES = {
    ".pyc",
    ".pyo",
    ".db",
    ".sqlite",
    ".sqlite3",
    ".dump",
    ".log",
}
PRIVATE_PATHS = {
    Path("src/course_project/data_generation"),
    Path("scripts/generate_data.py"),
    Path("tests/test_data_generation.py"),
    Path("tests/test_data_dictionary.py"),
    Path("instructor"),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Copia el material estudiantil a dist/, sin datos ni material del profesorado."
    )
    parser.add_argument("--output", default="dist", help="Directorio padre del paquete.")
    parser.add_argument(
        "--name",
        default="ftds_proyecto_alumnado",
        help="Nombre de la carpeta/zip generada.",
    )
    parser.add_argument(
        "--with-data",
        action="store_true",
        help="Incluye data/raw (ficheros fuente). Nunca incluye registros internos del profesorado.",
    )
    parser.add_argument("--zip", dest="make_zip", action="store_true", help="Además crea un archivo ZIP.")
    return parser.parse_args()


def _is_excluded(path: Path, root: Path, with_data: bool) -> bool:
    rel = path.relative_to(root)
    parts = set(rel.parts)
    if parts & EXCLUDE_DIR_NAMES:
        return True
    if rel.as_posix() in {p.as_posix() for p in PRIVATE_PATHS}:
        return True
    for private in PRIVATE_PATHS:
        try:
            rel.relative_to(private)
            return True
        except ValueError:
            pass
    if path.name in EXCLUDE_FILE_NAMES:
        return True
    if path.suffix in EXCLUDE_SUFFIXES:
        return True
    if any(part.endswith(".egg-info") for part in rel.parts):
        return True
    if path.name.endswith(".egg-info"):
        return True
    if not with_data and rel.parts[:2] == ("data", "raw") and path.name not in {".gitkeep", "README.md"}:
        return True
    if rel.parts[:2] == ("data", "processed") and path.name not in {".gitkeep", "README.md"}:
        return True
    if rel.parts[:2] == ("instructor", "generated"):
        return True
    return False


def main() -> int:
    args = parse_args()
    output_parent = Path(args.output)
    if not output_parent.is_absolute():
        output_parent = ROOT / output_parent
    target = output_parent / args.name
    if target.exists():
        shutil.rmtree(target)
    target.mkdir(parents=True)

    for path in ROOT.rglob("*"):
        if path.is_dir():
            continue
        if _is_excluded(path, ROOT, with_data=args.with_data):
            continue
        rel = path.relative_to(ROOT)
        dest = target / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, dest)

    # El alumnado no recibe el generador interno; se deja un marcador en src.
    pkg = target / "src" / "course_project"
    pkg.mkdir(parents=True, exist_ok=True)

    note = target / "DISTRIBUCION.md"
    note.write_text(
        (
            "Paquete de distribución para el alumnado.\n\n"
            "Este archivo se genera automáticamente. No incluye material privado del "
            "profesorado, registros internos, el generador de datos ni, salvo que se "
            "indique lo contrario, los ficheros de datos. Los CSV/Excel del caso se "
            "entregan por un canal separado. Colocadlos en data/raw/.\n"
        ),
        encoding="utf-8",
    )

    forbidden = []
    for path in target.rglob("*"):
        name = path.name.lower()
        if "anomaly_log" in name or "anomaly_summary" in name:
            forbidden.append(path)
        if "instructor" in path.relative_to(target).parts:
            forbidden.append(path)
        if "data_generation" in path.relative_to(target).parts:
            forbidden.append(path)
    if forbidden:
        raise SystemExit(
            "El paquete estudiantil contiene rutas privadas: "
            + ", ".join(str(p) for p in forbidden[:8])
        )

    print(f"Paquete creado en {target}")
    if args.make_zip:
        archive = shutil.make_archive(str(target), "zip", root_dir=target)
        print(f"ZIP: {archive}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
