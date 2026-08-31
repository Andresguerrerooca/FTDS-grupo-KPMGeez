# Datos del caso AlbaMarket

Este directorio está pensado para trabajo **local**. Los ficheros fuente no deben subirse al repositorio del equipo.

## Dónde colocar los ficheros

- `raw/`: ficheros recibidos (CSV y Excel) exactamente como se os entreguen.
- `processed/`: salidas intermedias opcionales de vuestro trabajo local. Tampoco se suben.

El profesorado os proporcionará un paquete de datos por un canal distinto a Git. Copiadlo a `data/raw/` antes de importar a PostgreSQL.

## Advertencia de calidad

Los sistemas fuente de AlbaMarket son propensos a errores. **No asumas que todos los registros son correctos.** Analizad y documentad la calidad del dato **antes** de transformarlo. El diccionario de datos describe el contrato esperado, no una garantía de cumplimiento.

## Formato esperado de los ficheros fuente

| Fichero | Formato | Contenido orientativo |
| --- | --- | --- |
| `customers.csv` | CSV UTF-8, coma | Clientes |
| `suppliers.xlsx` | Excel, una sola hoja | Proveedores |
| `categories.csv` | CSV UTF-8, coma | Categorías de producto |
| `products.csv` | CSV UTF-8, coma | Productos |
| `orders.csv` | CSV UTF-8, coma | Pedidos |
| `order_items.csv` | CSV UTF-8, coma | Líneas de pedido |
| `payments.csv` | CSV UTF-8, coma | Pagos |
| `shipments.xlsx` | Excel, una sola hoja | Envíos |
| `returns.csv` | CSV UTF-8, coma | Devoluciones |
| `geography.csv` | CSV UTF-8, coma | Países, regiones y ciudades |
| `data_dictionary.xlsx` | Excel, varias pestañas | Diccionario de datos |

Convenciones de importación:

- CSV en UTF-8, delimitador coma, una sola fila de cabecera.
- Fechas en ISO 8601 (`YYYY-MM-DD`).
- Decimales con punto.
- Identificadores estables con prefijo (`CUST-`, `ORD-`, `PRD-`, etc.).

Todos los datos son **sintéticos y ficticios**. No contienen datos personales reales.

## Qué no subir a Git

No subáis CSV, Excel, bases `.db`/`.sqlite`, volcados SQL masivos ni copias «limpiadas» de los ficheros originales. El `.gitignore` del proyecto ya ignora `data/raw/*` y `data/processed/*`, salvo los `.gitkeep` y README.
