# Streamlit

La segunda entrega construye un **dashboard ejecutivo** sobre la base de la primera. Esta guía explica la plantilla, no el diseño final.

Instrucciones de evaluación: [entregables/entrega_2_dashboard.md](entregables/entrega_2_dashboard.md). Fecha y duración: [config/course_config.yml](../config/course_config.yml).

## Ejecutar la plantilla

Desde la raíz del repositorio, con el entorno activado:

```bash
streamlit run app/Home.py
```

Equivalente: `make streamlit`.

La app debe **arrancar aunque no haya credenciales**. En ese caso veréis un aviso con pasos de configuración, no un volcado críptico de excepción sin contexto.

## Estructura prevista

```text
app/
  Home.py                 ← punto de entrada
  pages/01_Plantilla.py   ← página extra opcional
  components/
    data.py               ← conexión y consultas parametrizadas
    charts.py             ← gráficos reutilizables
src/course_project/
  db.py                   ← motor SQLAlchemy desde el entorno
  config.py               ← lectura de .env
```

Podéis añadir páginas; no es obligatorio. Streamlit lista `app/pages/` automáticamente.

Separad, en la medida de lo posible:

1. **Conexión** (`cache_resource` / motor).
2. **Acceso a datos** (SQL parametrizado, `cache_data`).
3. **Transformación para visualización** (agregados ligeros en pandas si hace falta).
4. **Interfaz** (filtros, títulos, texto para dirección).

## Configuración segura

- Preferid `.env` (véase `.env.example`).
- Alternativa: copiad `.streamlit/secrets.toml.example` a `.streamlit/secrets.toml`.
- Nunca incrustéis usuario y contraseña en `Home.py`.
- Nunca subáis `.env` ni `secrets.toml`.

PostgreSQL es el destino por defecto. Una app que **solo lee CSV/Excel** y no se conecta a la base **no cumple** un requisito esencial de la rúbrica técnica.

## Caché (implicaciones)

La plantilla usa:

- `st.cache_resource` para el motor de base de datos (objeto de conexión reutilizable).
- `st.cache_data(ttl=300)` para resultados de consulta (cinco minutos).

Consecuencias:

- Cambiar `.env` con la app abierta puede no bastar: *Clear cache* o reiniciar.
- Actualizar datos en PostgreSQL puede no verse al instante.
- No cacheéis por error un DataFrame enorme a nivel de pedido individual si dirección no lo necesita.

## SQL seguro

Usad parámetros enlazados (`text("... WHERE zona = :zona")` + `params={"zona": valor}`). **No** construyáis consultas con `f"... {selectbox}"`. Un filtro de la interfaz es entrada de usuario.

## Contenido mínimo frente a exceso

Obligatorio: **una tabla** y **tres visualizaciones** desarrolladas en Python, con datos de la base, más una narrativa para alta gerencia.

Recomendación: no superar ~**10** elementos entre tablas, gráficos e indicadores principales. Más no implica mejor nota: se valora selección, coherencia y legibilidad.

Cada visual debe tener título, unidades, periodo o filtro aplicable y un propósito analítico. Evitad listar personas u pedidos concretos si un agregado basta.

## TODO de la plantilla

En `Home.py` hay huecos para tres gráficos y una tabla. El selector de «zona» opera sobre **datos ficticios mínimos de demostración**, no sobre el caso. Sustituidlo por controles que consulten la base cuando aporten valor.

## Manual de ejecución (entrega 2)

El equipo debe redactar un manual de 2–4 páginas equivalentes (puede vivir en `docs/` del repo del equipo) con:

- requisitos;
- instalación;
- variables de entorno;
- comando `streamlit run app/Home.py`;
- qué vistas o tablas espera en PostgreSQL;
- limitaciones conocidas.

Sin ese manual y sin código en el repositorio a tiempo, la rúbrica penaliza los criterios de reproducibilidad afectados.
