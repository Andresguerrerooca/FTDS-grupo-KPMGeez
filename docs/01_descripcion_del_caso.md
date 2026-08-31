# Descripción del caso AlbaMarket

AlbaMarket es una **plataforma ficticia de comercio electrónico**. El equipo de dirección quiere dejar de decidir con extractos sueltos de hojas de cálculo y pasar a una base de datos consolidada, con calidad conocida, y a un tablero ejecutivo.

Este documento describe el perímetro del caso. No adelanta hallazgos ni «la respuesta correcta»: esa parte es trabajo del equipo.

## Contexto de negocio

La compañía vende un catálogo diverso (electrónica, hogar, moda, belleza, etc.) a clientes en España y, en menor medida, en otros países europeos. Los pedidos llegan por web, aplicación móvil y marketplace. Hay proveedores, envíos con distintos transportistas, pagos con varios métodos y un flujo de devoluciones.

Preguntas típicas de dirección (orientativas, no un checklist cerrado):

- ¿Dónde se concentra la venta y con qué margen?
- ¿Qué canales y segmentos se comportan de forma distinta?
- ¿Cómo se relacionan descuentos, volumen y rentabilidad?
- ¿Qué fricciones hay en pago y logística?
- ¿Qué patrones de devolución merecen atención?

Debéis formular **vuestras** preguntas, responderlas con evidencia y declarar limitaciones.

## Ficheros fuente

El profesorado os entregará un paquete de datos **aparte de Git**. Colocadlo en `data/raw/`. Detalle de formatos: [data/README.md](../data/README.md).

Ficheros mínimos:

- `customers.csv` — clientes
- `suppliers.xlsx` — proveedores (una sola hoja)
- `categories.csv` — categorías
- `products.csv` — productos
- `orders.csv` — pedidos
- `order_items.csv` — líneas de pedido
- `payments.csv` — pagos
- `shipments.xlsx` — envíos (una sola hoja)
- `returns.csv` — devoluciones
- `geography.csv` — países, regiones y ciudades
- `data_dictionary.xlsx` — diccionario (una pestaña por fichero más `README`)

Los nombres técnicos están en `snake_case` e inglés. El significado en castellano está en el diccionario (`description_es`).

## Advertencia de calidad (obligatoria)

Los sistemas de origen de AlbaMarket **son propensos a errores**. Hay que tratar los ficheros como extraídos reales, no como un dataset de juguete impecable.

- No asumas que todos los registros son correctos.
- Analizad y documentad la calidad **antes** de transformar a `core`.
- El diccionario describe el **contrato esperado**, no el cumplimiento de cada fila.
- Una transformación que «hace que todo cargue» sin dejar rastro de problemas no es un buen trabajo.

Guía: [04_calidad_del_dato.md](04_calidad_del_dato.md).

## Arquitectura prevista (sin resolver el modelo)

Se espera una arquitectura por capas:

| Capa / esquema | Rol |
| --- | --- |
| `staging` | Recepción fiel. Tipos tolerantes. Debe poder importarse aunque haya suciedad. |
| `core` | Entidades limpiadas, tipadas y relacionadas. Aquí viven las decisiones de modelo. |
| `analytics` | Vistas y agregados para SQL analítico y para Streamlit. |

Python puede **cargar** staging y **orquestar** scripts SQL. No debe duplicar la lógica de transformación que pertenece a SQL.

Detalle de scripts: [sql/README.md](../sql/README.md). Flujo: [03_flujo_de_trabajo_del_proyecto.md](03_flujo_de_trabajo_del_proyecto.md).

## Identificadores y convenciones

- CSV en UTF-8, coma, una cabecera.
- Fechas ISO 8601 (`YYYY-MM-DD`).
- Decimales con punto.
- Prefijos de identificadores: `GEO-`, `CUST-`, `SUP-`, `CAT-`, `PRD-`, `ORD-`, `ITM-`, `PAY-`, `SHP-`, `RET-`.
- Divisa del caso: EUR.

## Datos sintéticos

Nombres, correos, teléfonos, empresas y pedidos son **ficticios**, generados para la asignatura. No intentéis contactar esas direcciones ni tratarlas como personas reales.

## Qué se evalúa a partir de este caso

- Entrega 1: base, arquitectura, calidad, insights SQL y defensa.  
  [entrega_1_bbdd_sql.md](entregables/entrega_1_bbdd_sql.md)
- Entrega 2: dashboard conectado a esa base, narrativa ejecutiva y defensa.  
  [entrega_2_dashboard.md](entregables/entrega_2_dashboard.md)
