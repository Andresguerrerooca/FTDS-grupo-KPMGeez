-- Objetivo:
--   Crear las tablas del modelo core, ya tipadas, que representen las
--   entidades de negocio. En este paso se definen columnas y tipos; las
--   restricciones fuertes pueden ir aquí o en 04, según vuestra decisión.
-- Dependencias:
--   01_create_schemas.sql
-- Entradas:
--   Diseño del modelo (informe de arquitectura). Aún no se copian datos.
-- Salidas:
--   Tablas core.* vacías, preparadas para la carga transformada.
-- Autoría / equipo:
--   TODO: indicar nombres, apellidos y repositorio del equipo.

-- TODO: definid entidades (cliente, producto, pedido, línea, pago, envío,
-- devolución, geografía, categoría, proveedor, etc.) con tipos PostgreSQL
-- adecuados: DATE, NUMERIC, BOOLEAN, VARCHAR, TEXT.

-- Ejemplo neutro:
CREATE TABLE IF NOT EXISTS core._plantilla_ejemplo (
    example_id VARCHAR(32),
    example_name TEXT,
    created_on DATE
);

-- DROP TABLE IF EXISTS core._plantilla_ejemplo;

-- TODO: no copiéis staging tal cual. Core debe reflejar decisiones de modelo
-- (nombres, granularidad, claves candidatas). Documentad cardinalidades en el
-- informe y en el diagrama ER.
