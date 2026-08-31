-- Objetivo:
--   Vaciar de forma controlada los esquemas del caso para poder recrear la base
--   desde cero. Ejecutar este script implica perder los datos cargados.
-- Dependencias:
--   Ninguna. Es el primer paso de un reseteo completo.
-- Entradas:
--   No lee tablas. Opera sobre los esquemas staging, core y analytics si existen.
-- Salidas:
--   Esquemas eliminados (CASCADE). La base de datos en sí no se borra.
-- Autoría / equipo:
--   TODO: indicar nombres, apellidos y repositorio del equipo.
-- Cómo ejecutarlo:
--   Query Tool de pgAdmin, sobre la base ecommerce_course (o el nombre acordado).
--   No uses metacomandos de psql (\i, \copy) en este archivo.

-- TODO: confirmad que estáis conectados a la base de trabajo y no a otra instancia.
-- DROP SCHEMA IF EXISTS staging CASCADE;
-- DROP SCHEMA IF EXISTS core CASCADE;
-- DROP SCHEMA IF EXISTS analytics CASCADE;

-- Ejemplo neutro (no asume nombres de tablas de negocio):
-- CREATE SCHEMA IF EXISTS sandbox_reset_example;
-- DROP SCHEMA IF EXISTS sandbox_reset_example CASCADE;

SELECT 'TODO: descomentar los DROP SCHEMA cuando el equipo decida resetear' AS aviso;
