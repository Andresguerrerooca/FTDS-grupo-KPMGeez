# Flujo de trabajo del proyecto

El proyecto tiene **dos bloques consecutivos**. No empecéis el dashboard «contra CSV» mientras la base no exista: la entrega 2 se apoya en la 1.

Fechas: [config/course_config.yml](../config/course_config.yml).

## Vista de conjunto

```text
ficheros fuente (data/raw)
        │
        ▼
  importar a staging     ← pgAdmin o scripts/load_raw_data.py
        │
        ▼
  controles de calidad   ← sql/07_quality_checks.sql (y más que añadais)
        │
        ▼
  transformar a core     ← sql/05_transform_load.sql
        │
        ▼
  restricciones/índices  ← sql/04_constraints_indexes.sql (el orden se justifica)
        │
        ▼
  vistas analytics       ← sql/06_views.sql
        │
        ├─ insights SQL  ← entrega 1
        │
        └─ Streamlit     ← entrega 2 (consulta la base, no los ficheros)
```

## Diferencia entre pasos (importante)

| Paso | Qué significa | Herramienta típica |
| --- | --- | --- |
| Crear estructuras | Esquemas y tablas vacías | `01`–`03` en pgAdmin |
| Importar a staging | Copiar ficheros tal cual, con tipos tolerantes | Asistente de pgAdmin o Python |
| Limpiar y transformar | Decidir qué se corrige, se descarta o se marca | `05_transform_load.sql` |
| Aplicar claves y restricciones | PK, FK, CHECK | `04` (antes o después de cargar: justificado) |
| Crear índices | Acelerar filtros y joins reales | `04` |
| Crear vistas | Contratos estables para análisis y dashboard | `06` |
| Controles de calidad | Medir nulos, duplicados, huérfanos, incoherencias | `07` |
| Consultas de análisis | Responder preguntas de negocio | `08` e informe |

Python **no** debe reimplementar la transformación de `05`. Sí puede crear el motor de conexión, cargar staging y lanzar los `.sql` numerados, indicando qué archivo falló (`scripts/run_sql_pipeline.py`).

## Bloque 1 — SQL

1. Leer caso, diccionario y esta guía.
2. Acordar ramas y mensajes de commit ([Git](05_git_guia_practica.md)).
3. Crear la base y esquemas.
4. Definir staging alineado con las cabeceras reales.
5. Importar.
6. **Calidad primero** ([04_calidad_del_dato.md](04_calidad_del_dato.md)).
7. Diseñar core y el ER.
8. Transformar, restringir, indexar, crear vistas.
9. 5–10 insights con SQL en el repositorio.
10. Informe, presentación, etiqueta `entrega-1`.

Detalle de entrega: [entregables/entrega_1_bbdd_sql.md](entregables/entrega_1_bbdd_sql.md).

## Bloque 2 — Python / Streamlit

1. Partir de la base ya defendida (o de su evolución documentada).
2. Conectar Streamlit con variables de entorno.
3. Consultar `core` o `analytics` con SQL parametrizado.
4. Una tabla + tres visualizaciones como mínimo, narrativa ejecutiva.
5. Manual de instalación y ejecución.
6. Presentación y etiqueta `entrega-2`.

Detalle: [entregables/entrega_2_dashboard.md](entregables/entrega_2_dashboard.md) y [07_streamlit.md](07_streamlit.md).

## Trabajo en equipo (mínimo viable)

- Tablero sencillo de tareas (issues, hoja compartida o similar).
- Una persona no acumula todo el SQL ni todo el Python: la defensa es individualizable.
- Cada sesión: `git pull` / `git switch` a vuestra rama, trabajo, commit, push.
- Antes de entregar: README del equipo (si lo añadís), scripts ejecutables, sin artefactos prohibidos.

## SQLite

PostgreSQL es el motor del curso. SQLite **no** es un atajo equivalente. Solo si hay un bloqueo técnico real (y está documentado) se admite como excepción. Ver rúbricas y [preguntas frecuentes](08_preguntas_frecuentes.md).
