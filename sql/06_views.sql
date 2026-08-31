-- Objetivo:
--   Crear vistas en analytics para análisis SQL y para el dashboard de la
--   segunda entrega. Las vistas no sustituyen a core: lo consumen.
-- Dependencias:
--   core.* poblado y, si aplica, restricciones de 04.
-- Entradas:
--   Tablas core.
-- Salidas:
--   Vistas (y, si se justifican, vistas materializadas) en analytics.
-- Autoría / equipo:
--   TODO: indicar nombres, apellidos y repositorio del equipo.

-- TODO: definid vistas de grano fino (p. ej. líneas enriquecidas) y vistas
-- agregadas (p. ej. ventas por mes, por región, por categoría, por canal).
-- Cada vista debe tener un propósito de negocio que podáis explicar.

-- Ejemplo neutro:
CREATE OR REPLACE VIEW analytics._plantilla_ejemplo AS
SELECT
    CURRENT_DATE AS generated_on,
    'TODO: sustituir por una vista real del equipo' AS nota;

-- TODO: no incrustéis aquí los insights finales como consultas opacas.
-- Las vistas deben ser reutilizables. Los insights viven en 08_eda_insights.sql
-- y en el informe, citando las vistas o las consultas completas.
