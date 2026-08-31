-- Objetivo:
--   Definir tablas de staging que reciban los ficheros fuente con tipos
--   tolerantes (texto cuando el origen pueda venir sucio).
-- Dependencias:
--   01_create_schemas.sql
-- Entradas:
--   Contrato de columnas descrito en data/raw/data_dictionary.xlsx (cuando lo
--   tengáis) y en docs/01_descripcion_del_caso.md.
-- Salidas:
--   Tablas staging.* listas para importar CSV/Excel vía pgAdmin o
--   scripts/load_raw_data.py. Aún no hay claves ni transformaciones.
-- Autoría / equipo:
--   TODO: indicar nombres, apellidos y repositorio del equipo.

-- TODO: cread una tabla staging por fichero fuente. Usad TEXT o VARCHAR para
-- campos que puedan llegar con formatos inconsistentes. No apliquéis todavía
-- claves foráneas: staging debe poder cargar el fichero aunque haya suciedad.

-- Ejemplo neutro de patrón (sustituid por las tablas reales del caso):
CREATE TABLE IF NOT EXISTS staging._plantilla_ejemplo (
    row_num TEXT,
    source_file TEXT,
    loaded_at TEXT
);

-- DROP TABLE IF EXISTS staging._plantilla_ejemplo;

-- TODO: customers, suppliers, categories, products, orders, order_items,
-- payments, shipments, returns, geography.
-- Alinead los nombres de columna con el diccionario de datos.
