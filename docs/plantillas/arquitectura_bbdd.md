# Plantilla · Informe de arquitectura de la base de datos

Usad este esquema en el documento de la [entrega 1](../entregables/entrega_1_bbdd_sql.md). Borrad los comentarios en cursiva.

## 1. Identificación

- Equipo:
- Integrantes:
- Repositorio:
- Motor: PostgreSQL (si SQLite, justificación técnica):
- Fecha de los scripts evaluados (commit o etiqueta `entrega-1`):

## 2. Capas o esquemas

| Esquema | Propósito | Qué entra | Qué sale |
| --- | --- | --- | --- |
| staging | *Recepción fiel* | | |
| core | *Modelo de negocio* | | |
| analytics | *Consumo* | | |

## 3. Tablas

| Tabla | Esquema | Grano (una fila es…) | Propósito |
| --- | --- | --- | --- |
| | | | |

## 4. Claves y cardinalidades

Describid PK, FK y relaciones (1:N, etc.). El diagrama ER debe coincidir con esta sección.

## 5. Diagrama entidad-relación

*Insertad una figura legible. Opcional: enlace a fuente editable en el repo, sin sustituir la figura del PDF.*

## 6. Limpieza y tipado

| Problema observado | Evidencia (query) | Decisión | Dónde se aplica |
| --- | --- | --- | --- |
| | | | |

## 7. Vistas

| Vista | Grano | Pregunta que responde | Usuarios previstos |
| --- | --- | --- | --- |
| | | | |

## 8. Índices, restricciones y otras decisiones

*Por qué ese índice, qué CHECK, qué se dejó fuera y por qué.*

## 9. Orden de ejecución y reproducibilidad

Lista numerada de scripts y del momento de importar ficheros. Si 04 va después de 05, explicadlo.

## 10. Limitaciones

Lo que el modelo aún no cubre y el impacto en la entrega 2.
