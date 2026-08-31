"""Carga de configuración desde entorno y YAML."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml
from dotenv import load_dotenv

from course_project.paths import project_root


class ConfigError(RuntimeError):
    """Error de configuración visible para el alumnado, sin secretos."""


@dataclass(frozen=True)
class DatabaseSettings:
    engine: str
    host: str
    port: int
    name: str
    user: str
    password: str
    sqlite_path: Path | None


def _load_env(root: Path) -> None:
    env_path = root / ".env"
    load_dotenv(env_path, override=False)


def load_course_config(root: Path | None = None) -> dict[str, Any]:
    """Carga course_config.yml o, si no existe, el ejemplo maestro."""
    root = root or project_root()
    preferred = root / "config" / "course_config.yml"
    fallback = root / "config" / "course_config.example.yml"
    path = preferred if preferred.exists() else fallback
    if not path.exists():
        raise ConfigError(
            "No se encontró config/course_config.example.yml. "
            "Comprueba que estás en la raíz del repositorio."
        )
    with path.open(encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}
    if not isinstance(data, dict):
        raise ConfigError(f"El archivo {path} no contiene un mapeo YAML válido.")
    return data


def load_database_settings(root: Path | None = None) -> DatabaseSettings:
    root = root or project_root()
    _load_env(root)
    engine = os.getenv("DB_ENGINE", "postgresql").strip().lower()
    missing: list[str] = []
    if engine == "sqlite":
        sqlite_raw = os.getenv("DB_SQLITE_PATH", "data/processed/ecommerce_course.sqlite")
        return DatabaseSettings(
            engine="sqlite",
            host="",
            port=0,
            name="",
            user="",
            password="",
            sqlite_path=(root / sqlite_raw).resolve()
            if not Path(sqlite_raw).is_absolute()
            else Path(sqlite_raw),
        )

    host = os.getenv("DB_HOST", "").strip()
    port_raw = os.getenv("DB_PORT", "").strip()
    name = os.getenv("DB_NAME", "").strip()
    user = os.getenv("DB_USER", "").strip()
    password = os.getenv("DB_PASSWORD", "")
    if not host:
        missing.append("DB_HOST")
    if not port_raw:
        missing.append("DB_PORT")
    if not name:
        missing.append("DB_NAME")
    if not user:
        missing.append("DB_USER")
    if password == "":
        missing.append("DB_PASSWORD")
    if missing:
        raise ConfigError(
            "Faltan variables de conexión a PostgreSQL: "
            + ", ".join(missing)
            + ". Copia .env.example a .env y completa los valores. "
            + "No compartas el archivo .env ni contraseñas."
        )
    try:
        port = int(port_raw)
    except ValueError as exc:
        raise ConfigError("DB_PORT debe ser un número entero, por ejemplo 5432.") from exc
    return DatabaseSettings(
        engine="postgresql",
        host=host,
        port=port,
        name=name,
        user=user,
        password=password,
        sqlite_path=None,
    )
