# Rúbrica de la entrega 1 (100 puntos)

Evaluación de **base de datos, arquitectura e insights SQL**. Instrucciones: [entrega_1_bbdd_sql.md](entrega_1_bbdd_sql.md). Fechas: [config/course_config.yml](../../config/course_config.yml).

Niveles: **Excelente**, **Adecuado**, **En desarrollo**, **Insuficiente**. Cada nivel indica evidencia observable.

Suma de pesos: 40 + 30 + 30 = **100**.

## Cómo aplicar la rúbrica (equipo e individuos)

- Los bloques A y B se califican sobre el **producto grupal** (repo e informe).
- El bloque C se califica con evidencia de la **defensa**. Puede haber matices individuales si la participación es muy desigual; hay que argumentarlo en observaciones.
- Una ausencia o no presentación se aplica a la **persona afectada**, no al resto del equipo de forma automática.
- Tras sumar puntos (0–100), la nota sobre 10 es `puntos / 10`.

## Bloque A. Implementación técnica de SQL y reproducibilidad (40 puntos)

### A1. Reproducibilidad y ejecución de los scripts (12 puntos)

- **Excelente:** Los scripts numerados recrean la base desde cero en pgAdmin, uno a uno, y también con el pipeline Python. El orden está documentado. Un tercero reproduce sin mensajes privados del equipo.
- **Adecuado:** Los scripts funcionan en orden con indicaciones menores (un paso manual documentado, por ejemplo la importación a staging). Se puede reproducir en un tiempo razonable.
- **En desarrollo:** Faltan pasos, hay rutas locales o el orden solo lo conoce quien lo escribió. La reproducción requiere adivinar.
- **Insuficiente:** No hay scripts ejecutables, dependen de `\i`/`\copy`, o el repositorio no permite reconstruir la base.

### A2. Arquitectura por capas, modelo de datos y relaciones (12 puntos)

- **Excelente:** `staging`, `core` y `analytics` (o equivalente justificado) están separados con propósito claro. El ER es legible. PK/FK y cardinalidades coinciden con el código y el informe.
- **Adecuado:** Hay capas y un modelo relacional usable. El ER existe y es comprensible, con fallos menores de nomenclatura o de una cardinalidad.
- **En desarrollo:** Tablas planas o staging copiado a core sin diseño. ER incompleto o contradictorio con las FK.
- **Insuficiente:** No hay modelo reconocible, ni esquemas, ni relaciones documentadas ni implementadas.

### A3. Transformaciones, restricciones, índices y vistas (10 puntos)

- **Excelente:** La limpieza está en SQL, con reglas explícitas. Restricciones e índices justificados. Vistas con propósito de negocio, incluidas agregadas. El orden 04/05 está razonado.
- **Adecuado:** Hay transformación a tipos correctos, algunas FK/índices y al menos una vista útil. Justificación breve pero presente.
- **En desarrollo:** Casi no hay limpieza, o las vistas son `SELECT *`. Índices decorativos o restricciones que se desactivan sin análisis.
- **Insuficiente:** No hay transformación documentada, ni vistas, ni integridad más allá de cargar texto.

### A4. Documentación técnica de los scripts (6 puntos)

- **Excelente:** Encabezados completos (objetivo, dependencias, entradas, salidas, autoría). Comentarios que explican decisiones, no el SQL obvio.
- **Adecuado:** Encabezados presentes y autoría del equipo. Algún comentario desigual entre archivos.
- **En desarrollo:** Plantillas `TODO` apenas tocadas o autoría ausente.
- **Insuficiente:** Scripts opacos, sin encabezado ni forma de saber qué ejecutar.

## Bloque B. Calidad de los insights y de sus queries o evidencias (30 puntos)

### B1. Cobertura y relevancia de los insights de negocio (10 puntos)

- **Excelente:** Entre 5 y 10 hallazgos no triviales, conectados con decisiones de AlbaMarket (margen, canal, logística, etc.), sin repetir el mismo recuento disfrazado.
- **Adecuado:** 5 o más insights pertinentes, alguno descriptivo. Cubren más de una perspectiva (p. ej. venta y calidad, o venta y logística).
- **En desarrollo:** Menos de 5, o todos son conteos `COUNT(*)` sin pregunta de negocio.
- **Insuficiente:** No hay insights, o son irrelevantes / copiados sin relación con los datos.

### B2. Calidad de las consultas SQL y de la evidencia (12 puntos)

- **Excelente:** Cada insight cita un `.sql` ejecutable. La evidencia es una agregación o muestra controlada. Las queries son legibles y usan el modelo (joins, filtros, fechas) de forma correcta.
- **Adecuado:** Queries en el repo y resultado en el informe. Fallos menores (un join de más, un redondeo).
- **En desarrollo:** Queries solo como captura, o no se pueden ejecutar, o no coinciden con el texto.
- **Insuficiente:** No hay SQL de insights en el repositorio.

### B3. Interpretación, implicación de negocio y cautelas de calidad (8 puntos)

- **Excelente:** Interpretación ligada a la evidencia, implicación accionable y cautela cuando la calidad del dato limita la afirmación.
- **Adecuado:** Hay interpretación y alguna limitación. La recomendación es plausible.
- **En desarrollo:** Se describe la tabla de resultado sin decir qué significa para dirección, o se afirma de más.
- **Insuficiente:** No hay interpretación, o se ignoran problemas de calidad evidentes para inflar el hallazgo.

## Bloque C. Presentación y defensa oral (30 puntos)

### C1. Estructura, claridad y adecuación del discurso (10 puntos)

- **Excelente:** Guion claro en el tiempo `[DURACION_PRESENTACION_1]`, lenguaje para clase y para un perfil de dirección, apoyo visual legible.
- **Adecuado:** Se entiende el relato (problema → modelo → hallazgos). Desajustes leves de tiempo o de diapositivas densas.
- **En desarrollo:** Lectura continua de diapositivas, sin hilo, o fuera de tiempo de forma notable.
- **Insuficiente:** No hay presentación usable, o no se expone el trabajo.

### C2. Dominio técnico y capacidad de defensa (12 puntos)

- **Excelente:** Responden a preguntas sobre orden de carga, una FK, una regla de limpieza y un insight con la query en mente.
- **Adecuado:** Defienden lo esencial con alguna imprecisión que corrigen al repreguntar.
- **En desarrollo:** Solo quien escribió el SQL puede responder; el resto no distingue staging de core.
- **Insuficiente:** No hay defensa técnica, o contradice de forma grave el repositorio.

### C3. Participación identificable y trabajo en equipo (8 puntos)

- **Excelente:** Todas las personas del equipo intervienen de forma reconocible (parte del discurso o respuestas).
- **Adecuado:** Intervienen todas, aunque el reparto sea desigual pero declarado.
- **En desarrollo:** Una persona monopoliza; el resto saluda o lee una diapositiva ajena sin criterio.
- **Insuficiente:** No se puede identificar la participación, o hay integrantes de la matrícula que no aparecen ni en repo ni en sala sin justificación.

## Reglas especiales (no alteran los pesos; sí el recorte de nota)

1. Si el código y los scripts **no están correctamente subidos al repositorio como máximo el día posterior a la presentación**, la parte técnica completa se califica con **0 puntos sobre 40** (bloque A entero). Los bloques B y C pueden evaluarse con la evidencia disponible ese día (presentación e informe), pero B2 no puede ser Excelente ni Adecuado si las queries no están en el repo.
2. Un alumno que **no realice la presentación/defensa oral** podrá obtener como máximo **7/10** en esta entrega (es decir, `min(nota, 7.0)` sobre 10). La regla es **individual**.
3. La ausencia individual **no rebaja automáticamente** al resto del equipo.
4. Cualquier uso de **SQLite** debe estar debidamente justificado por un problema técnico real. Una elección por mera comodidad **no satisface** el requisito tecnológico: el bloque A no puede situarse en Excelente y, salvo fuerza mayor documentada, permanece en En desarrollo o Insuficiente en A1 y A2.

## Observaciones del profesorado

- Equipo:
- Fecha de presentación:
- Fecha del commit/etiqueta evaluado:
- SQLite / incidencias técnicas:
- Comentarios bloque A:
- Comentarios bloque B:
- Comentarios bloque C (individuales si aplica):
- Nota numérica (0–100) y sobre 10:
