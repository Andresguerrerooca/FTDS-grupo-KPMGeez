"""Resolución de rutas del repositorio."""

from __future__ import annotations

from pathlib import Path


def project_root(start: Path | None = None) -> Path:
    """Devuelve la raíz del proyecto (directorio que contiene pyproject.toml)."""
    here = (start or Path(__file__).resolve()).absolute()
    candidates = [here, *here.parents] if here.is_file() or here.suffix else [here, *here.parents]
    if here.is_dir():
        candidates = [here, *here.parents]
    else:
        candidates = [here.parent, *here.parent.parents]
    for candidate in candidates:
        if (candidate / "pyproject.toml").exists():
            return candidate
    return Path.cwd()
