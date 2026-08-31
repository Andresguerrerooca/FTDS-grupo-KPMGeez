# Scripts SQL del proyecto

Los archivos de esta carpeta están **numerados** para ejecutarse en orden. Cada uno debe poder abrirse y ejecutarse **individualmente** en el Query Tool de pgAdmin. No uses metacomandos de `psql` (`\i`, `\copy`) dentro de estos scripts.

## Orden propuesto

| Archivo | Qué hace | Qué no hace |
| --- | --- | --- |
| `00_reset.sql` | Elimina esquemas para empezar de cero | No borra la instancia de PostgreSQL |
| `01_create_schemas.sql` | Crea `staging`, `core` y `analytics` | No crea tablas de negocio |
| `02_create_staging_tables.sql` | Tablas de recepción, tipos tolerantes | No limpia ni tipa como core |
| `03_create_core_tables.sql` | Entidades tipadas del modelo | No implica que los datos ya estén limpios |
| `04_constraints_indexes.sql` | PK, FK, checks, índices | Puede fallar si se aplica sobre datos sucios |
| `05_transform_load.sql` | Limpieza y carga staging → core | No debe duplicarse esa lógica en Python |
| `06_views.sql` | Vistas analíticas | No sustituye a las tablas core |
| `07_quality_checks.sql` | Controles de calidad reproducibles | No «arregla» automáticamente |
| `08_eda_insights.sql` | Consultas de los insights | No reemplaza al informe |

El orden de `04` y `05` es una **propuesta**. Si aplicáis claves foráneas antes de limpiar, la carga puede fallar. Documentad y justificad el orden real.

## Cómo ejecutarlos en pgAdmin

1. Conectaos a la base `ecommerce_course` (o el nombre de vuestro `.env`).
2. Query Tool → abrir el archivo → Execute.
3. Si hay error, leed el mensaje, corregid el script y volved a ejecutarlo. No sigáis «a ciegas».
4. La importación de CSV/Excel a `staging` se hace con el asistente de pgAdmin **o** con `python scripts/load_raw_data.py`. Eso no va dentro de estos `.sql`.

## Automatización posterior

`python scripts/run_sql_pipeline.py` ejecutará estos archivos en orden y detendrá el proceso indicando **qué archivo falló**. Por eso los nombres deben seguir el patrón `NN_descripcion.sql`.

## Encabezado obligatorio

Cada script ya incluye objetivo, dependencias, entradas, salidas y autoría. Completad la autoría. Sustituid los `TODO` por SQL real de vuestro equipo. Los ejemplos `_plantilla_ejemplo` son neutros: no son el modelo del caso.

## Qué no debe aparecer aquí

- Soluciones copiadas de otros equipos.
- Contraseñas o cadenas de conexión.
- `\copy` o rutas locales absolutas a CSV.
- Insights «mágicos» sin consulta reproducible.
