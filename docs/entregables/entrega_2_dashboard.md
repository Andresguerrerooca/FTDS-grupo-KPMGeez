# Entrega 2 · Dashboard ejecutivo en Streamlit

Bloque de **Python, visualización y comunicación ejecutiva**. El producto es una aplicación que consulta la base de la entrega 1, más un manual y una defensa.

- Fecha: `deliveries.entrega_2.fecha` en [config/course_config.yml](../../config/course_config.yml).
- Duración orientativa: `deliveries.entrega_2.duracion_presentacion` en el mismo archivo.
- Rúbrica (100 puntos): [rubrica_entrega_2.md](rubrica_entrega_2.md).
- Etiqueta Git recomendada: `entrega-2`.
- Guía técnica: [../07_streamlit.md](../07_streamlit.md).

## 1. Contenido obligatorio

Cada equipo entrega:

1. Un dashboard desarrollado con **Streamlit**.
2. **Conexión real** a la base implementada en la primera fase.
3. **PostgreSQL** por defecto; SQLite solo con justificación técnica documentada.
4. Al menos **una tabla** y **tres visualizaciones** desarrolladas en Python.
5. Filtros o controles útiles **cuando aporten valor**.
6. Una **narrativa coherente** para alta gerencia / dirección.
7. Justificación de qué insights se muestran, por qué valen y qué decisiones podrían apoyar.
8. Código modular, comprensible y documentado (`app/` + reutilizables en `src/` si aplica).
9. Gestión segura de configuración y credenciales (`.env.example` o `secrets.toml.example`, nunca secretos reales).
10. Manual de instalación y ejecución reproducible.
11. Presentación y defensa oral del producto.

No hay un máximo rígido de widgets, pero se recomienda **no superar ~10 elementos** entre tablas, gráficos e indicadores principales. Más elementos no implica mejor evaluación: importan selección, coherencia y legibilidad.

El dashboard consulta la base o sus vistas. **No** debe funcionar leyendo los CSV/Excel originales como sustituto de la conexión.

## 2. Formato y extensión esperada

| Elemento | Expectativa |
| --- | --- |
| Código | `app/` (entrada `app/Home.py`) y módulos en `src/` |
| Dependencias | `requirements.txt` y/o `pyproject.toml` reproducible |
| Secretos | `.env.example` y/o `.streamlit/secrets.toml.example` |
| Manual | Markdown, unas **2–4 páginas** equivalentes |
| Memoria o presentación | **10–15 diapositivas** (o extensión equivalente): audiencia, insights, diseño, limitaciones |
| Defensa | `[DURACION_PRESENTACION_2]` |
| Git | Código y documentación subidos **como máximo el día posterior a la presentación**; etiqueta `entrega-2` |
| Ejecución documentada | `streamlit run app/Home.py` |

## 3. Qué no debe entregarse ni subirse

- CSV, Excel ni extractos completos de los datos.
- Bases SQLite ni archivos de base de datos.
- `.env`, `secrets.toml` con credenciales, usuarios o contraseñas.
- Credenciales incrustadas en el código.
- `.venv`, cachés, `__pycache__`, logs, temporales.
- Sustituir la conexión por lectura directa de ficheros.
- Entregar solo capturas o un vídeo **sin** código ejecutable.
- Gráficos sin título, unidades, contexto o propósito analítico.
- Datos innecesarios a nivel individual cuando una agregación basta.

## 4. Evaluación (resumen)

100 puntos:

- **40** funcionamiento técnico (conexión, consultas, errores, mínimos, reproducibilidad de *que arranque*);
- **20** calidad de código y limpieza del repositorio (modularidad, secretos, historial, artefactos);
- **20** estética y narrativa;
- **20** presentación y defensa.

El 40 técnico y el 20 de código **no puntúan lo mismo dos veces**: el primero pregunta *si funciona y se conecta*; el segundo pregunta *cómo está escrito y versionado*. Detalle y reglas (máximo **8/10** sin defensa oral, ficheros vs base, SQLite): [rubrica_entrega_2.md](rubrica_entrega_2.md).

## 5. Relación con la entrega 1

Podéis evolucionar vistas SQL si lo documentáis. No reescribáis el modelo en pandas para evitar SQL. Si la base de la entrega 1 era incompleta, la entrega 2 no «salva» aquel 40 técnico, pero sí puede mostrar un producto coherente sobre lo que sí exista, con limitaciones honestas.
