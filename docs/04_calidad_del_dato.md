# Calidad del dato

Este caso **no** se puede resolver importando y cruzando tablas como si el origen fuera perfecto. Los sistemas fuente de AlbaMarket son propensos a errores. Debéis **analizar y documentar la calidad antes de transformar**.

No se os indica aquí qué anomalías concretas hay, ni en qué proporción, ni en qué tabla «está el truco». Eso forma parte del trabajo.

## Principio

El diccionario de datos (`data_dictionary.xlsx`) explica el **contrato esperado**: nombres de columna, nulos previstos, reglas de negocio. Una fila que viola el contrato es un hallazgo, no un detalle molesto que borrar en silencio.

Staging debe poder **recibir** el fichero. Core debe representar **decisiones conscientes** sobre ese fichero.

## Qué revisar (lista de trabajo, no de soluciones)

Trabajad con consultas reproducibles en `sql/07_quality_checks.sql` (y las que añadais):

1. **Completitud.** Nulos o cadenas vacías en campos que el diccionario marca como no nulos.
2. **Unicidad.** Duplicados de identificadores y de claves de negocio (correo, SKU, pedido…).
3. **Validez de rangos.** Cantidades, precios, descuentos, plazos e importes imposibles o desproporcionados.
4. **Consistencia interna.** `line_total` frente a cantidad y precio; total de pedido frente a líneas, descuento y envío.
5. **Consistencia temporal.** Fechas de alta, pedido, pago, envío, entrega y devolución que no encajan.
6. **Consistencia de estados.** Pedido, pago y envío que se contradicen.
7. **Integridad referencial.** Claves que no existen en la tabla padre (huérfanos) o geografías desconocidas.
8. **Formato.** Mayúsculas, espacios, sinónimos de un mismo estado o canal.
9. **Extremos operativos.** Tiempos de entrega u otras magnitudes que, aun siendo numéricas, no son creíbles.

Un mismo registro puede tener más de un problema. Contad **filas afectadas** y **tipos de incidencia** por separado cuando os sea útil.

## Cómo documentar

Para cada hallazgo relevante:

- pregunta o control («¿hay pedidos sin cliente existente?»);
- consulta SQL;
- magnitud (conteo, porcentaje, ejemplos **anonimizados / sintéticos**, sin volcar el fichero);
- decisión (corregir con regla, aislar, descartar, conservar con marca);
- impacto en los insights posteriores.

Usad la plantilla [plantillas/registro_insights.md](plantillas/registro_insights.md) también para hallazgos de calidad si los convertís en insight.

## Qué no hacer

- No «arreglar a mano» el CSV en Excel y entregar esa copia como si fuera el origen.
- No subir los ficheros, ni las versiones limpiadas, al repositorio.
- No aplicar `DELETE` masivos en core sin dejar constancia de la regla.
- No ignorar un problema porque dificulta una clave foránea: ese es precisamente el momento de decidir.
- No asumir que un porcentaje bajo de errores hace innecesario el control.

## Relación con las entregas

En la entrega 1, la calidad aparece en la arquitectura (decisiones de limpieza y tipado), en los scripts y, cuando proceda, en las **cautelas** de cada insight. En la entrega 2, el dashboard no debe vender como verdad operativa un indicador construido sobre datos no gobernados.
