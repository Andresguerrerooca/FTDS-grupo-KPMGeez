# PostgreSQL y pgAdmin

PostgreSQL es el motor **obligatorio por defecto** del curso. pgAdmin es el entorno previsto para ejecutar cada script de `sql/` de forma aislada. Docker Compose es **opcional** y no sustituye a esta guía.

SQLite no es un equivalente: ved la política en [08_preguntas_frecuentes.md](08_preguntas_frecuentes.md) y en las rúbricas.

## 1. Instalación local (sin Docker)

1. Instalad PostgreSQL 16 (u otra 14+ estable) desde el sitio oficial o el empaquetado de vuestra distro.
2. Anotad puerto (5432 por defecto), usuario y contraseña **local**.
3. Instalad pgAdmin 4.
4. Cread la base `ecommerce_course` (o el nombre de vuestro `.env`).

En pgAdmin: clic derecho en *Databases* → *Create* → *Database*.

Conexión en `.env`:

```text
DB_HOST=localhost
DB_PORT=5432
DB_NAME=ecommerce_course
DB_USER=postgres
DB_PASSWORD=change_me
```

## 2. Opción Docker (conveniencia)

Requisitos: Docker Desktop o motor Docker + Compose. No es requisito académico.

```bash
docker compose up -d
```

Servicios del archivo [docker-compose.yml](../docker-compose.yml):

- PostgreSQL en el puerto `DB_PORT`
- pgAdmin en `PGADMIN_PORT` (por defecto 5050)

Credenciales de pgAdmin en `.env` (`PGADMIN_DEFAULT_EMAIL`, `PGADMIN_DEFAULT_PASSWORD`): son de **desarrollo**, no cuentas reales. Dentro de pgAdmin hay que **registrar el servidor** `postgres` (en Compose el hostname del servicio es `postgres`; desde el navegador del anfitrión el host de la base suele ser `localhost`).

Parar:

```bash
docker compose down
```

Los volúmenes `ftds_ecommerce_pgdata` y `ftds_ecommerce_pgadmin` persisten datos de desarrollo. No los subáis a Git.

## 3. Ejecutar scripts numerados en pgAdmin

Los archivos de [sql/](../sql/README.md) están pensados para el Query Tool:

1. Conectad a `ecommerce_course`.
2. *Tools* → *Query Tool*.
3. Abrid `sql/01_create_schemas.sql` (ejemplo).
4. Execute (icono de play).
5. Leed mensajes y rejilla de resultados.

**No** incrustéis `\i` ni `\copy` en esos archivos: no funcionan igual en pgAdmin y rompen el ejecutor Python.

Orden propuesto: `00` → `01` → `02` → importar datos → calidad → `03` → `05` / `04` (justificad) → `06` → `07` → `08`.

## 4. Importar CSV y Excel a staging

Dos vías válidas:

### A. Asistente de pgAdmin

1. Cread las tablas staging (`02_create_staging_tables.sql`) alineadas con las cabeceras.
2. Clic derecho en la tabla → *Import/Export Data*.
3. CSV: UTF-8, delimitador coma, header *yes*.
4. Excel: pgAdmin no siempre importa `.xlsx` de forma fiable. En ese caso, exportad a CSV **localmente** (sin subir el CSV) o usad la vía B.

### B. Python

Cuando las tablas existan y coincidan las columnas:

```bash
python scripts/load_raw_data.py --input data/raw
```

Este script no transforma reglas de negocio; solo carga. Si falla, el mensaje debe indicar si faltan tablas o si COPY no está disponible.

## 5. Automatizar el pipeline SQL

```bash
python scripts/run_sql_pipeline.py
```

Ejecuta `sql/NN_*.sql` en orden, **una transacción por archivo**, y se detiene indicando el archivo que falló. Seguid teniendo los scripts ejecutables a mano en pgAdmin: eso es lo que se evalúa en reproducibilidad de aula.

## 6. Buenas prácticas

- Un script = un propósito (el encabezado de cada archivo ya pide objetivo, dependencias, entradas, salidas, autoría).
- No guardéis copias `final2.sql` sueltas en el escritorio: el repo es la fuente.
- No pegues la contraseña en un script `CONNECT`.
- Tras un error de FK, no desactivéis todas las restricciones «para que cargue»: documentad el problema de calidad.

## 7. Comprobación rápida de conexión

Si el entorno Python está instalado:

```bash
python -c "from course_project.db import ping; ping(); print('ok')"
```

Debe leer `.env`. Si falta configuración, el error lista variables **sin** imprimir la contraseña.
