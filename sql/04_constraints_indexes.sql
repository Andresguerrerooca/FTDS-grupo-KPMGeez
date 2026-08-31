-- Objetivo:
--   Aplicar claves primarias, foráneas, checks e índices. Este paso puede
--   fallar si se ejecuta sobre datos sucios: es una decisión de diseño.
-- Dependencias:
--   03_create_core_tables.sql. Si las restricciones se aplican DESPUÉS de la
--   carga, este script podría ejecutarse tras 05. Justificad el orden.
-- Entradas:
--   Tablas core.* (vacías o ya cargadas, según el orden que elijáis).
-- Salidas:
--   Integridad referencial e índices que soporten las consultas analíticas.
-- Autoría / equipo:
--   TODO: indicar nombres, apellidos y repositorio del equipo.

-- Atención pedagógica:
-- Si aplicáis FOREIGN KEY antes de limpiar, la carga de core fallará al
-- encontrar huérfanos o duplicados. Muchos equipos cargan, limpian y DESPUÉS
-- refuerzan restricciones. Otros limpian en el SELECT de 05 y aplican FK al
-- final de esa carga. Lo importante es que el orden sea reproducible y esté
-- documentado.

-- Ejemplo neutro:
-- ALTER TABLE core._plantilla_ejemplo
--     ADD CONSTRAINT pk_plantilla_ejemplo PRIMARY KEY (example_id);

-- TODO: PRIMARY KEY en cada entidad core.
-- TODO: FOREIGN KEY con las cardinalidades del diagrama ER.
-- TODO: CHECK solo cuando la regla sea estable (por ejemplo, cantidades > 0
-- en la tabla limpia, no en staging).
-- TODO: índices en claves foráneas y en columnas de filtro frecuentes
-- (fechas, estados, geografía). No indexéis «por si acaso».
