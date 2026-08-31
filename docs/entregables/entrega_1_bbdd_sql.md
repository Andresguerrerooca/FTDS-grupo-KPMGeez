# Entrega 1 · Base de datos, arquitectura e insights SQL

Bloque de **SQL y bases de datos**. El producto es un repositorio reproducible más un informe y una defensa oral.

- Fecha: `deliveries.entrega_1.fecha` en [config/course_config.yml](../../config/course_config.yml).
- Duración orientativa de la defensa: `deliveries.entrega_1.duracion_presentacion` en el mismo archivo.
- Rúbrica (100 puntos): [rubrica_entrega_1.md](rubrica_entrega_1.md).
- Etiqueta Git recomendada: `entrega-1`.

## 1. Contenido obligatorio

### 1.1 Repositorio de código

Scripts SQL necesarios para **recrear la base desde cero** a partir de los ficheros fuente (que **no** se suben):

- ordenados y numerados;
- documentados (objetivo, dependencias, entradas, salidas, autoría);
- ejecutables **individualmente** en el Query Tool de pgAdmin;
- sin `\i` ni `\copy`;
- compatibles con `python scripts/run_sql_pipeline.py`.

Estructura de partida: [sql/README.md](../../sql/README.md). Podéis añadir archivos numerados si lo justificáis, no eliminar la disciplina de orden.

### 1.2 Informe de arquitectura

Debe describir:

- capas o esquemas (`staging`, `core`, `analytics` u otros justificados);
- tablas y propósito de cada una;
- claves primarias y foráneas;
- cardinalidades y relaciones;
- decisiones de limpieza y tipado;
- vistas, en especial las agregadas, y qué representa cada una;
- índices, restricciones y decisiones técnicas relevantes;
- diagrama entidad-relación **legible** (integrado en el informe; opcionalmente, fuente editable adicional en el repo, por ejemplo `.drawio` o `.md` con mermaid, sin sustituir la imagen/exportación del PDF).

Plantilla: [../plantillas/arquitectura_bbdd.md](../plantillas/arquitectura_bbdd.md).

### 1.3 Reporte de análisis exploratorio SQL

Entre **5 y 10 insights** relevantes. Cada uno incluye:

1. pregunta de negocio;
2. query SQL reproducible (en el repo, no solo captura);
3. resultado o evidencia (tabla resumen o métrica; no hace falta pegar 10.000 filas);
4. interpretación;
5. relevancia para el negocio;
6. limitaciones o cautelas de calidad cuando proceda.

Plantilla: [../plantillas/registro_insights.md](../plantillas/registro_insights.md). Consultas: `sql/08_eda_insights.sql` y/o archivos adicionales claramente nombrados.

### 1.4 Presentación y defensa oral

En clase, con **participación identificable** de quienes integran el equipo. Guion orientativo: [../plantillas/guion_presentacion.md](../plantillas/guion_presentacion.md).

## 2. Formato y extensión esperada

Son expectativas razonables, no un límite punitivo por una página de más o de menos si el contenido es sólido.

| Elemento | Expectativa |
| --- | --- |
| Informe de arquitectura + análisis | Un único documento de **8–15 páginas**, o presentación equivalente de **12–20 diapositivas** |
| Formato del informe | PDF, DOCX o PPTX. **Se recomienda PDF** para preservar el formato |
| Diagrama ER | Integrado en el informe; fuente editable opcional en el repo |
| Queries | Archivos `.sql` en el repositorio |
| Defensa oral | Duración `[DURACION_PRESENTACION_1]` |
| Nombres de archivo | `entrega1_informe_equipoXX.pdf` (o `.docx`/`.pptx`) en, por ejemplo, `docs/entregas/` del **repo del equipo** (esa carpeta la podéis crear vosotros). No subáis datos. |
| Código | Rama principal actualizada; etiqueta `entrega-1` recomendada |
| Plazo del repo | Código y scripts correctamente subidos **como máximo el día posterior a la presentación** |

El informe puede entregarse por el canal que indique el profesorado (Canvas, etc.). El código **siempre** vive en Git.

## 3. Reproducibilidad

Una persona externa (profesorado) debe poder:

1. crear la base vacía;
2. colocar los ficheros fuente en `data/raw/` (obtenidos por el canal de datos, no por Git);
3. ejecutar los scripts en orden (pgAdmin o pipeline);
4. obtener el mismo modelo y poder lanzar las queries de insights.

Documentad el orden real si se aparta de `00`–`08`.

## 4. Qué no debe entregarse ni subirse

- CSV o Excel de origen, ni copias modificadas.
- Bases SQLite ni archivos `.db`, `.sqlite`, `.sqlite3`.
- Volcados completos de PostgreSQL salvo petición expresa del profesorado.
- `.env`, contraseñas, secretos.
- `.venv`, cachés, logs, temporales, exportaciones masivas.
- Sustituir las queries por capturas de pantalla (las capturas pueden **ilustrar** el informe, no reemplazar el `.sql`).
- Entregar **solo** un informe sin scripts reproducibles.
- Datos personales reales (el caso es sintético; no añadáis los vuestros).

## 5. Evaluación (resumen)

Peso total 100 puntos: **40** implementación SQL y reproducibilidad, **30** insights y evidencia, **30** presentación y defensa. Detalle y reglas especiales (0 sobre 40 técnico, máximo **7/10** si no hay defensa oral individual, SQLite justificado): [rubrica_entrega_1.md](rubrica_entrega_1.md).

Motor: PostgreSQL. SQLite solo con problema técnico real documentado; la mera comodidad no sirve.
