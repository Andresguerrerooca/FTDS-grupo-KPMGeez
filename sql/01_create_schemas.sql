-- Objetivo:
--   Crear los esquemas por capas: staging (recepción fiel), core (entidades
--   limpias y relacionadas) y analytics (vistas y agregados).
-- Dependencias:
--   00_reset.sql si se parte de un estado sucio; si no, puede ejecutarse sobre
--   una base vacía.
-- Entradas:
--   Ninguna tabla. Solo crea esquemas.
-- Salidas:
--   Esquemas staging, core y analytics disponibles para los scripts posteriores.
-- Autoría / equipo:
--   Grupo KPMGeez — [Pablo Sepúlveda, Mohammed Ghaith, Meysem Bentahar, Andres Guerrero, Martín Larrea]
--   Repositorio: https://github.com/Andresguerrerooca/FTDS-grupo-KPMGeez
-- Cómo ejecutarlo:
--   Query Tool de pgAdmin. Script autocontenido, sin \i ni \copy.

CREATE SCHEMA IF NOT EXISTS staging;
CREATE SCHEMA IF NOT EXISTS core;
CREATE SCHEMA IF NOT EXISTS analytics;

-- TODO: si el equipo necesita un esquema adicional, documentad el motivo en el
-- informe de arquitectura. No creéis esquemas «por si acaso».

COMMENT ON SCHEMA staging IS 'Recepción fiel de ficheros fuente; tipos tolerantes.';
COMMENT ON SCHEMA core IS 'Entidades limpiadas, tipadas y relacionadas.';
COMMENT ON SCHEMA analytics IS 'Vistas y agregados para análisis y dashboard.';
