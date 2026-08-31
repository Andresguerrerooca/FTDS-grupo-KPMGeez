# Puesta en marcha

Esta guía cubre el entorno local. Las fechas de entrega están en [config/course_config.yml](../config/course_config.yml).

## 1. Comprobar herramientas

En una terminal:

```bash
git --version
python --version
```

Hace falta **Python 3.11, 3.12 o 3.13** (se recomienda 3.12). PostgreSQL y pgAdmin se instalan aparte (véase [06_postgresql_y_pgadmin.md](06_postgresql_y_pgadmin.md)). Docker es opcional.

## 2. Clonar o copiar el proyecto

Si el profesorado os da un repositorio Git:

```bash
git clone <url-del-repositorio-del-equipo>
cd <carpeta>
```

Si os dan un ZIP del paquete estudiantil, descomprimidlo y `git init` según la [guía de Git](05_git_guia_practica.md).

## 3. Entorno virtual e instalación

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip
python -m pip install -e ".[dev]"
```

Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -e ".[dev]"
```

`.[dev]` instala el paquete local y pytest. Alternativa equivalente: `python -m pip install -r requirements.txt` y, además, `python -m pip install -e .`.

Si el profesorado publica más adelante un `requirements.lock.txt`, instáladlo con `python -m pip install -r requirements.lock.txt` y anotad la fecha en vuestro manual.

## 4. Variables de entorno

```bash
copy .env.example .env
```

(En Linux/macOS: `cp .env.example .env`.)

Valores mínimos:

```text
DB_HOST=localhost
DB_PORT=5432
DB_NAME=ecommerce_course
DB_USER=postgres
DB_PASSWORD=change_me
```

Sustituid `change_me` por la contraseña **local** de vuestro PostgreSQL. No la subáis a Git. No la peguéis en issues ni en el chat de la asignatura.

## 5. Datos

Colocad el paquete de ficheros que os entregue el profesorado en `data/raw/`. Esa carpeta **no se versiona** (salvo README y `.gitkeep`).

Un demo local, si os lo autorizan para probar scripts:

```bash
python scripts/generate_data.py --profile demo --seed 2026 --output data/raw
```

El perfil `full` es el volumen docente. Puede tardar y ocupar bastante disco; no se sube a Git.

```bash
python scripts/generate_data.py --profile full --seed 2026 --output data/raw
```

## 6. Comprobaciones

```bash
python -m pytest
python scripts/validate_project.py
```

Plantilla Streamlit (fallará de forma informativa si aún no hay base):

```bash
streamlit run app/Home.py
```

## 7. PostgreSQL opcional con Docker

Si no tenéis Postgres instalado y sí Docker:

```bash
docker compose up -d
```

pgAdmin suele quedar en `http://localhost:5050` (puerto `PGADMIN_PORT`). Seguid usando las mismas variables de `.env`. Esto **no** sustituye aprender pgAdmin ni justifica SQLite.

## 8. Carga y SQL (cuando el equipo tenga tablas)

```bash
python scripts/load_raw_data.py --input data/raw
python scripts/run_sql_pipeline.py
```

Los scripts de `sql/` deben funcionar también **uno a uno** en pgAdmin. Python solo orquesta; no mueve la lógica de negocio fuera de SQL.

## Si algo falla

Incluid error, comando, sistema operativo y contexto. Guía de incidencias: [08_preguntas_frecuentes.md](08_preguntas_frecuentes.md).
