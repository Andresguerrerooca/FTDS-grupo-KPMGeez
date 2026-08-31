# Rúbrica de la entrega 2 (100 puntos)

Evaluación del **dashboard ejecutivo en Streamlit**. Instrucciones: [entrega_2_dashboard.md](entrega_2_dashboard.md). Fechas: [config/course_config.yml](../../config/course_config.yml).

Niveles: **Excelente**, **Adecuado**, **En desarrollo**, **Insuficiente**.

Suma: 40 + 20 + 20 + 20 = **100**.

## Distinción entre el 40 técnico y el 20 de código

- **Bloque T (40):** ¿La aplicación **funciona**? ¿Se **conecta** a la base? ¿Hay tabla y tres gráficos con consultas? ¿El manual permite arrancarla? ¿Se gestionan errores de conexión?
- **Bloque R (20):** ¿El código está **modular**, documentado, sin secretos, con dependencias claras e historial Git limpio, sin CSV ni `.venv`?

Un dashboard que funciona con un único archivo de 800 líneas puede puntuar alto en T y bajo en R. Un repo impecable que lee CSV y no conecta puede puntuar bajo en T aunque R esté cuidado.

## Cómo aplicar la rúbrica

- T, R y N sobre el producto grupal.
- P con evidencia de la defensa; matices individuales si el desequilibrio es claro.
- Ausencia o no presentación: **individual**, sin recortar de oficio al resto.
- Nota sobre 10 = puntos / 10, con el tope 8/10 si aplica la regla oral.

## Bloque T. Funcionamiento técnico del dashboard (40 puntos)

### T1. Conexión real a la base de datos y origen de los datos (12 puntos)

- **Excelente:** Conexión a PostgreSQL (o SQLite **justificado**) mediante entorno/secretos de ejemplo. Las vistas o tablas `core`/`analytics` son el origen. No hay lectura de CSV como fuente del tablero.
- **Adecuado:** Conecta y muestra datos de la base. Algún gráfico aún mezcla un apoyo local documentado, no como fuente principal.
- **En desarrollo:** Conexión inestable, credenciales en código, o parte material del tablero sale de ficheros.
- **Insuficiente:** No hay conexión. La app solo lee CSV/Excel. Este incumplimiento **impide una valoración satisfactoria (Excelente o Adecuado) de todo el bloque T**.

### T2. Requisitos mínimos de consulta, tabla y visualizaciones (12 puntos)

- **Excelente:** Una tabla y tres visualizaciones con SQL parametrizado, títulos, unidades y propósito. Filtros útiles si existen. Selección contenida (no un festín de widgets).
- **Adecuado:** Cumple el mínimo (1 tabla + 3 gráficos) con datos reales de la base. Filtros simples o alguno cosmético.
- **En desarrollo:** Falta alguno de los mínimos, o los gráficos no salen de una consulta, o son placeholders de la plantilla.
- **Insuficiente:** No hay producto más allá de la plantilla sin conectar.

### T3. Manejo de errores, parámetros y estabilidad (8 puntos)

- **Excelente:** Sin base, el mensaje es accionable (como la plantilla, o mejor). Los filtros no concatenan SQL. La app no revienta en excepción cruda ante un fallo típico.
- **Adecuado:** Errores de conexión controlados. Algún fallo menor no capturado.
- **En desarrollo:** Trazas largas sin guía, o SQL interpolado con el selectbox.
- **Insuficiente:** La app no arranca o cae al primer error sin información útil.

### T4. Reproducibilidad, manual de ejecución y entorno (8 puntos)

- **Excelente:** Manual de 2–4 páginas equivalentes: instalación, `.env`, `streamlit run app/Home.py`, tablas/vistas esperadas, limitaciones. Un tercero arranca con ese texto.
- **Adecuado:** Manual suficiente con un hueco menor (p. ej. versión de Python no citada).
- **En desarrollo:** README genérico sin comandos reales, o comandos que no coinciden con el repo.
- **Insuficiente:** No hay manual ni forma documentada de ejecutar.

## Bloque R. Calidad del código y limpieza del repositorio (20 puntos)

### R1. Modularidad, claridad y documentación del código (8 puntos)

- **Excelente:** Separación conexión / consultas / gráficos / UI. Nombres claros. Comentarios de decisión. Páginas extra solo si aportan.
- **Adecuado:** Estructura razonable a partir de la plantilla, con módulos o funciones propias.
- **En desarrollo:** Un único archivo masivo, nombres oscuros, plantilla apenas tocada en estructura.
- **Insuficiente:** Código incomprensible o no es Python/Streamlit del repo.

### R2. Gestión segura de la configuración y dependencias (6 puntos)

- **Excelente:** `.env.example` o secrets de ejemplo; dependencias fijadas en rangos; ninguna contraseña en Git.
- **Adecuado:** Entorno reproducible y sin secretos reales. Alguna dependencia solo citada de palabra.
- **En desarrollo:** Dependencias incompletas o un secreto de ejemplo demasiado parecido a uno real pegado en un comentario.
- **Insuficiente:** Credenciales en el código o en archivos versionados.

### R3. Higiene del repositorio e historial de Git (6 puntos)

- **Excelente:** Sin CSV/Excel de datos, sin `.venv`, sin `.db`, commits con sentido, etiqueta o commit de entrega identificable.
- **Adecuado:** Repo usable; uno o dos archivos irrelevantes no sensibles.
- **En desarrollo:** Historial `final.zip` / `cambios`, o artefactos que el `.gitignore` debería haber evitado.
- **Insuficiente:** Entrega por fichero suelto fuera de Git, o datos/secretos en el repo.

## Bloque N. Calidad estética y narrativa (20 puntos)

### N1. Selección y propósito analítico de los elementos visuales (8 puntos)

- **Excelente:** Cada visual responde a una pregunta de dirección. No hay gráficos de relleno. Se nota por qué están esos insights y no otros.
- **Adecuado:** Selección razonable, algún gráfico débil pero no contradictorio.
- **En desarrollo:** Galería de plots sin tesis, o más de ~10 elementos que diluyen el mensaje.
- **Insuficiente:** Sin narrativa visual, o gráficos sin título/unidades/propósito.

### N2. Legibilidad, jerarquía visual y pulido estético (6 puntos)

- **Excelente:** Jerarquía clara (titular → KPI o tesis → apoyo). Contraste y no saturación. Ejes legibles.
- **Adecuado:** Se lee en una pantalla de aula. Algún solapamiento o color discutible.
- **En desarrollo:** Texto minúsculo, leyendas cortadas, plantilla cruda.
- **Insuficiente:** Ilegible o roto en la demostración.

### N3. Narrativa ejecutiva y apoyo a la toma de decisiones (6 puntos)

- **Excelente:** Audiencia de alta gerencia: contexto, hallazgo, implicación, limitación. Se entiende qué harían mañana.
- **Adecuado:** Relato de negocio presente, con alguna jerga técnica de más.
- **En desarrollo:** Narrativa de tutorial Streamlit, no de dirección.
- **Insuficiente:** No hay discurso ejecutivo.

## Bloque P. Presentación y defensa oral (20 puntos)

### P1. Claridad de la presentación del producto (10 puntos)

- **Excelente:** Demostración en vivo o guiada en `[DURACION_PRESENTACION_2]`, con recorrido consciente (no paseo aleatorio de menús).
- **Adecuado:** Se ve el producto y el hilo. Algún tropiezo técnico recuperado.
- **En desarrollo:** Solo diapositivas de capturas, o demo que no coincide con el repo.
- **Insuficiente:** No se presenta el producto.

### P2. Defensa, justificación de decisiones y respuestas (10 puntos)

- **Excelente:** Justifican conexión, elección de gráficos, agregación frente a detalle personal, y una limitación de datos.
- **Adecuado:** Responden lo central con apoyo del equipo.
- **En desarrollo:** No saben de dónde sale un número mostrado.
- **Insuficiente:** No hay defensa.

## Reglas especiales

1. Si el código y el manual **no están correctamente subidos al repositorio como máximo el día posterior a la presentación**, se aplican **ceros o el nivel Insuficiente** en los criterios **directamente afectados**, con trazabilidad:
   - T4 (manual/reproducibilidad) → 0 / Insuficiente;
   - R3 (higiene e historial) → 0 / Insuficiente;
   - T2 y R1 si no hay código evaluable en Git → 0 / Insuficiente.
   El acta debe citar el commit ausente o tardío. No se inventa un recorte opaco sobre los 100 puntos.
2. Un alumno que **no realice la presentación/defensa oral** podrá obtener como máximo **8/10** en esta entrega (`min(nota, 8.0)`). Regla **individual**.
3. La ausencia individual **no reduce automáticamente** la nota oral del resto del equipo.
4. Una aplicación que **solo lea ficheros y no se conecte a la base** incumple un requisito esencial: **no puede obtener una valoración satisfactoria (Excelente o Adecuado) en el bloque T (40 puntos)**.
5. **SQLite** requiere justificación documentada de un problema técnico real. Por comodidad, T1 no puede ser Excelente ni Adecuado.

## Observaciones del profesorado

- Equipo:
- Fecha de presentación:
- Commit/etiqueta:
- ¿Conexión a PostgreSQL verificada?:
- ¿SQLite justificado?:
- Criterios T afectados por retraso de repo:
- Comentarios T / R / N / P:
- Notas individuales (tope 8/10 si aplica):
- Nota numérica (0–100) y sobre 10:
