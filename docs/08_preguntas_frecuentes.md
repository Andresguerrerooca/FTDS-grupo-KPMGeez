# Preguntas frecuentes

## Entorno y Python

**`python` no se reconoce.** En Windows probad `py -3.12`. Aseguraos de tener Python 3.11, 3.12 o 3.13 en el PATH.

**El entorno virtual no se activa en PowerShell.** Política de ejecución: el profesorado o el servicio informático pueden orientar. Alternativa: `cmd` y `.venv\Scripts\activate.bat`. No desactivéis el antivirus a ciegas.

**`pip install -e ".[dev]"` falla.** Actualizad pip (`python -m pip install -U pip`). Comprobad que estáis en la raíz (donde está `pyproject.toml`).

## Git

**Git quiere añadir CSV enormes.** Cancelad. Deben estar ignorados. Ved [05_git_guia_practica.md](05_git_guia_practica.md).

**¿Puedo hacer `push --force`?** No forma parte del flujo de esta asignatura. Si el remoto rechaza el push, haced `git pull`, resolved conflictos y `git push` normal.

## PostgreSQL y pgAdmin

**No tengo Docker.** No hace falta. Instalar PostgreSQL y pgAdmin es la vía prevista.

**pgAdmin no ejecuta `\copy`.** Correcto: no lo uséis en los scripts del repo. Importad con el asistente o con `scripts/load_raw_data.py`.

**Error de clave foránea al cargar core.** Es una señal de calidad o de orden de inserción. No es un «bug de PostgreSQL». Documentad huérfanos y decidid regla.

**¿Puedo usar SQLite para ir más rápido?** No como atajo equivalente. PostgreSQL es el requisito. SQLite **solo** si existe un **problema técnico real** (instalación bloqueada, política del equipo, imposibilidad documentada de levantar Postgres) y el equipo lo **justifica por escrito** en el informe. La comodidad, el desconocimiento o «así abre Streamlit más fácil» **no** satisfacen el requisito. Las rúbricas lo recogen.

## Datos

**¿Subimos los CSV al repo para que el profesor pueda reproducir?** No. Los datos se distribuyen por otro canal. El código SQL y Python sí van al repo.

**El Excel de envíos es grande.** Trabajad en local. No lo versionéis. Para importar, usad el cargador Python o CSV temporal local.

**¿El diccionario garantiza que no hay nulos?** No. Es el contrato esperado. Ved [04_calidad_del_dato.md](04_calidad_del_dato.md).

## Streamlit

**La app arranca pero no hay gráficos del caso.** La plantilla es intencionadamente incompleta. La entrega 2 consiste en construirlos contra la base.

**Cambia el `.env` y no se nota.** Caché de Streamlit: *Clear cache* o reiniciar. Ved [07_streamlit.md](07_streamlit.md).

**¿Puedo leer los CSV en pandas y saltarme la base?** No. Incumple un requisito esencial de la entrega 2.

## Entregas

**¿Dónde están las fechas?** En [config/course_config.yml](../config/course_config.yml).

**Una persona del equipo no puede presentar.** La penalización oral es **individual** (máximos 7/10 y 8/10 según la entrega). No se rebaja automáticamente al resto. Avisad al profesorado.

**Subimos el código un día tarde.** Ved las rúbricas: en la entrega 1 la parte técnica puede ir a **0 puntos sobre 40** si el repo no está correcto como máximo el día posterior a la presentación.

## Cómo pedir ayuda

Incluid:

1. mensaje de error completo;
2. comando o botón de pgAdmin usado;
3. sistema operativo;
4. qué estabais haciendo.

No incluyáis contraseñas, `.env` ni pantallazos con secretos.
