# Fundamentos Tecnológicos en Data Science

Proyecto transversal de la asignatura **Fundamentos Tecnológicos en Data Science**. Este repositorio es la plantilla de trabajo de los equipos: guía, estructura de código y soporte de las dos entregas. El caso es **AlbaMarket**, una plataforma ficticia de comercio electrónico.

Los datos del caso son **sintéticos**. No contienen datos personales reales.

## Para qué sirve este repositorio

- Construir una base de datos reproducible en **PostgreSQL** a partir de ficheros fuente.
- Analizar la calidad del dato, modelar por capas y extraer insights con SQL.
- Construir después un **dashboard ejecutivo en Streamlit** conectado a esa base.
- Entregar y defender dos productos evaluables, con rúbricas públicas.

No es una solución resuelta: los scripts SQL y el dashboard son plantillas con `TODO`. El valor está en las decisiones del equipo.

## El caso (breve)

AlbaMarket opera un catálogo con clientes, productos, proveedores, pedidos, pagos, envíos y devoluciones. Los equipos reciben ficheros extraídos de sistemas fuente heterogéneos (CSV y Excel). La dirección quiere una base fiable y un tablero que apoye decisiones, no un almacén de capturas de pantalla.

**Los sistemas fuente son propensos a errores.** Debéis **analizar y documentar la calidad del dato antes de transformarlo**. No asumas que todos los registros recibidos son correctos, ni que el diccionario de datos garantiza el cumplimiento de cada fila.

Descripción completa: [docs/01_descripcion_del_caso.md](docs/01_descripcion_del_caso.md).

## Dos bloques y dos entregas

1. **SQL y bases de datos.** Consolidación, control de calidad, modelo por capas e insights.  
   Instrucciones: [docs/entregables/entrega_1_bbdd_sql.md](docs/entregables/entrega_1_bbdd_sql.md) · Rúbrica: [docs/entregables/rubrica_entrega_1.md](docs/entregables/rubrica_entrega_1.md)
2. **Python y dashboard.** Streamlit conectado a la base, narrativa ejecutiva y defensa del producto.  
   Instrucciones: [docs/entregables/entrega_2_dashboard.md](docs/entregables/entrega_2_dashboard.md) · Rúbrica: [docs/entregables/rubrica_entrega_2.md](docs/entregables/rubrica_entrega_2.md)

Las fechas y duraciones de exposición están en el archivo maestro [config/course_config.yml](config/course_config.yml). Si ese archivo no está en vuestra copia, usad [config/course_config.example.yml](config/course_config.example.yml).

## Resultados de aprendizaje

Al terminar el proyecto, el equipo será capaz de:

- Diseñar un flujo reproducible de carga desde ficheros hacia PostgreSQL.
- Separar recepción (`staging`), modelo de negocio (`core`) y consumo analítico (`analytics`).
- Detectar, documentar y tratar problemas de calidad sin destruir evidencia.
- Formular preguntas de negocio y responderlas con SQL reproducible.
- Construir un dashboard Streamlit conectado a la base, con configuración segura.
- Trabajar en equipo con Git, commits trazables y un repositorio limpio.

## Recorrido recomendado (fases, no calendario cerrado)

Las fechas concretas las fija el profesorado en el [archivo maestro](config/course_config.yml). El orden de trabajo sí es estable:

1. Lectura del caso, diccionario y [puesta en marcha](docs/02_puesta_en_marcha.md).
2. Git: clonar, ramas cortas, convenciones ([guía práctica](docs/05_git_guia_practica.md)).
3. PostgreSQL y pgAdmin ([guía](docs/06_postgresql_y_pgadmin.md)). Importar a `staging`.
4. Calidad del dato **antes** de transformar ([guía](docs/04_calidad_del_dato.md)).
5. Modelo core, restricciones, índices y vistas.
6. Insights SQL, informe, diagrama ER y defensa de la entrega 1.
7. Plantilla Streamlit, conexión, consultas y narrativa ejecutiva ([guía](docs/07_streamlit.md)).
8. Manual de ejecución, higiene del repo y defensa de la entrega 2.

Flujo detallado: [docs/03_flujo_de_trabajo_del_proyecto.md](docs/03_flujo_de_trabajo_del_proyecto.md).

## Requisitos

| Herramienta | ¿Obligatorio? | Notas |
| --- | --- | --- |
| Git | Sí | Trabajo en equipo y entregas |
| Python 3.11–3.13 | Sí | Entorno virtual. Se recomienda 3.12. |
| PostgreSQL | Sí (por defecto) | Motor académico del curso |
| pgAdmin | Sí | Ejecución individual de scripts SQL |
| Docker / Docker Compose | No | Solo conveniencia para levantar Postgres+pgAdmin |
| SQLite | No | Solo ante un problema técnico real, documentado y justificado |

Docker **no** es un requisito académico. Si ya tenéis PostgreSQL y pgAdmin, no hace falta Compose.

## Inicio rápido

```bash
python -m venv .venv
```

Activación:

- Windows (PowerShell): `.\.venv\Scripts\Activate.ps1`
- Linux/macOS: `source .venv/bin/activate`

```bash
python -m pip install -U pip
python -m pip install -e ".[dev]"
copy .env.example .env
```

En Linux/macOS usad `cp .env.example .env`. Editad `.env` con vuestra conexión. **No subáis `.env`.**

Generar un juego de datos de prueba (si el profesorado os pide generaros un demo local; el caso completo os llegará por otro canal):

```bash
python scripts/generate_data.py --profile demo --seed 2026 --output data/raw
python scripts/generate_data.py --profile full --seed 2026 --output data/raw
```

Pruebas y validación del repositorio:

```bash
python -m pytest
python scripts/validate_project.py
```

Dashboard (plantilla):

```bash
streamlit run app/Home.py
```

PostgreSQL opcional con Docker:

```bash
docker compose up -d
```

Carga a staging y pipeline SQL (cuando existan tablas y scripts reales del equipo):

```bash
python scripts/load_raw_data.py --input data/raw
python scripts/run_sql_pipeline.py
```

Paquete de distribución (uso del profesorado):

```bash
python scripts/build_student_release.py --output dist/
```

Equivalentes `make`: `make install`, `make demo-data`, `make full-data`, `make test`, `make validate`, `make streamlit`, `make docker-up`, `make load-staging`, `make sql-pipeline`, `make release`.

## Estructura resumida

```text
.
├── README.md                 ← este archivo
├── config/                   ← fechas y parámetros maestros
├── data/                     ← datos locales (no se suben)
├── docs/                     ← guías y entregas
├── sql/                      ← scripts numerados (pgAdmin)
├── src/course_project/       ← utilidades Python
├── app/                      ← plantilla Streamlit
├── scripts/                  ← generación, carga, validación
└── tests/                    ← pruebas automatizadas
```

Detalle: [docs/README.md](docs/README.md) e índice de SQL en [sql/README.md](sql/README.md).

## Documentación

Índice: [docs/README.md](docs/README.md)

- [Descripción del caso](docs/01_descripcion_del_caso.md)
- [Puesta en marcha](docs/02_puesta_en_marcha.md)
- [Flujo de trabajo del proyecto](docs/03_flujo_de_trabajo_del_proyecto.md)
- [Calidad del dato](docs/04_calidad_del_dato.md)
- [Git, guía práctica](docs/05_git_guia_practica.md)
- [PostgreSQL y pgAdmin](docs/06_postgresql_y_pgadmin.md)
- [Streamlit](docs/07_streamlit.md)
- [Preguntas frecuentes](docs/08_preguntas_frecuentes.md)
- [Entrega 1](docs/entregables/entrega_1_bbdd_sql.md) · [Rúbrica 1](docs/entregables/rubrica_entrega_1.md) · [HTML Canvas 1](docs/entregables/rubrica_entrega_1_canvas.html)
- [Entrega 2](docs/entregables/entrega_2_dashboard.md) · [Rúbrica 2](docs/entregables/rubrica_entrega_2.md) · [HTML Canvas 2](docs/entregables/rubrica_entrega_2_canvas.html)
- Plantillas: [arquitectura](docs/plantillas/arquitectura_bbdd.md), [insights](docs/plantillas/registro_insights.md), [guion](docs/plantillas/guion_presentacion.md)

## Trabajo en equipo y Git

- Una rama corta por tarea; commits pequeños y mensajes descriptivos.
- Cada integrante debe dejar **trazabilidad** (autoría de commits, participación en la defensa).
- Revisad antes de integrar en la rama principal del equipo.
- Guía: [docs/05_git_guia_practica.md](docs/05_git_guia_practica.md).

## Archivos que nunca deben subirse

- `.env`, `secrets.toml`, contraseñas, tokens.
- Ficheros de `data/raw/` y `data/processed/` (CSV, Excel, copias «limpias»).
- Bases `.db`, `.sqlite`, `.sqlite3`, volcados masivos.
- `.venv/`, `__pycache__/`, logs, temporales, exportaciones grandes.

El `.gitignore` ya cubre estos casos. Si Git propone añadirlos, cancelad y revisad.

## Cómo pedir ayuda

Enviad **el error completo**, **el comando ejecutado**, **sistema operativo** y **contexto** (qué estabais haciendo, archivo SQL o script). No envieis contraseñas, `.env` ni capturas con credenciales visibles.

Más ayuda: [docs/08_preguntas_frecuentes.md](docs/08_preguntas_frecuentes.md).

## Licencia

[MIT](LICENSE). Material para uso académico. Caso y datos ficticios.
