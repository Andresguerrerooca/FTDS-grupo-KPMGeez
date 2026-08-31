"""Conexión a la base de datos a partir de variables de entorno."""

from __future__ import annotations

import warnings
from urllib.parse import quote_plus

from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine

from course_project.config import ConfigError, DatabaseSettings, load_database_settings


SQLITE_WARNING = (
    "SQLite es una alternativa excepcional y no equivalente a PostgreSQL. "
    "Solo debe usarse si existe un problema técnico real, documentado y justificado."
)


def sqlalchemy_url(settings: DatabaseSettings | None = None) -> str:
    settings = settings or load_database_settings()
    if settings.engine == "sqlite":
        warnings.warn(SQLITE_WARNING, UserWarning, stacklevel=2)
        if settings.sqlite_path is None:
            raise ConfigError("DB_SQLITE_PATH no está definido.")
        settings.sqlite_path.parent.mkdir(parents=True, exist_ok=True)
        return f"sqlite:///{settings.sqlite_path.as_posix()}"
    password = quote_plus(settings.password)
    user = quote_plus(settings.user)
    return (
        f"postgresql+psycopg://{user}:{password}"
        f"@{settings.host}:{settings.port}/{settings.name}"
    )


def create_db_engine(settings: DatabaseSettings | None = None) -> Engine:
    settings = settings or load_database_settings()
    url = sqlalchemy_url(settings)
    if settings.engine == "sqlite":
        return create_engine(url, future=True)
    return create_engine(url, future=True, pool_pre_ping=True)


def ping(engine: Engine | None = None) -> None:
    """Comprueba la conexión. No imprime credenciales."""
    engine = engine or create_db_engine()
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
