-- Objetivo:
--   Controles de calidad reproducibles sobre staging y/o core: nulos
--   inesperados, duplicados, huérfanos, rangos, coherencia de estados y fechas.
-- Dependencias:
--   Datos en staging (siempre) y en core (cuando exista la transformación).
-- Entradas:
--   staging.* y core.*.
-- Salidas:
--   Resultados de consultas de control. No es obligatorio persistir tablas de
--   calidad, pero sí documentar umbrales y hallazgos.
-- Autoría / equipo:
--   TODO: indicar nombres, apellidos y repositorio del equipo.

-- Ejecutad estos controles ANTES de dar por buena la transformación. El caso
-- está diseñado para que los ficheros fuente NO se asuman correctos.

-- Ejemplo neutro de conteo:
SELECT
    'staging._plantilla_ejemplo' AS tabla,
    COUNT(*) AS n_filas
FROM staging._plantilla_ejemplo;

-- TODO: nulos en campos que el diccionario marca como no nulos.
-- TODO: duplicados de claves de negocio (email, sku, order_id, etc.).
-- TODO: referencias huérfanas (cliente inexistente, producto inexistente, geo inexistente).
-- TODO: cantidades o importes negativos o desproporcionados.
-- TODO: fechas de pago/envío/devolución incompatibles con el pedido.
-- TODO: estados de pedido, pago y envío que no encajan entre sí.

-- Dejad las consultas que evidencian problemas. No las borréis al «limpiar».
