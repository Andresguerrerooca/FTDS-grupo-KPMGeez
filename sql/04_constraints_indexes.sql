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


-- Primero voy a definir las PRIMARY KEYS de cada tabla

Alter Table core.categories
add constraint pk_categories PRIMARY KEY (category_id);

Alter Table core.customers
add constraint pk_customers PRIMARY KEY (customer_id);

Alter Table core.geography
add constraint pk_geography PRIMARY KEY (geo_id);

Alter Table core.order_items
add constraint pk_order_items PRIMARY KEY (order_item_id);

Alter Table core.orders
add constraint pk_orders PRIMARY KEY (order_id);

ALTER TABLE core.payments
ADD CONSTRAINT pk_payments
PRIMARY KEY (payment_id);

Alter Table core.products
add constraint pk_products PRIMARY KEY (product_id);

Alter Table core.returns
add constraint pk_returns PRIMARY KEY (return_id);

Alter Table core.shipments
add constraint pk_shipments PRIMARY KEY (shipment_id);

Alter Table core.suppliers
add constraint pk_suppliers PRIMARY KEY (supplier_id);

-- Ahora las FOREIGN KEYS

Alter table core.customers
add constraint fk_customers FOREIGN KEY (geo_id)
References core.geography (geo_id);

ALTER TABLE core.products
ADD CONSTRAINT fk_products_categories
FOREIGN KEY (category_id)
REFERENCES core.categories (category_id);

ALTER TABLE core.products
ADD CONSTRAINT fk_products_suppliers
FOREIGN KEY (supplier_id)
REFERENCES core.suppliers (supplier_id);

ALTER TABLE core.categories
ADD CONSTRAINT fk_categories_parent
FOREIGN KEY (parent_category_id)
REFERENCES core.categories (category_id);

ALTER TABLE core.orders
ADD CONSTRAINT fk_orders_customers
FOREIGN KEY (customer_id)
REFERENCES core.customers (customer_id);

ALTER TABLE core.orders
ADD CONSTRAINT fk_orders_geography
FOREIGN KEY (geo_id)
REFERENCES core.geography (geo_id);

ALTER TABLE core.order_items
ADD CONSTRAINT fk_order_items_orders
FOREIGN KEY (order_id)
REFERENCES core.orders (order_id);

ALTER TABLE core.order_items
ADD CONSTRAINT fk_order_items_products
FOREIGN KEY (product_id)
REFERENCES core.products (product_id);

ALTER TABLE core.payments
ADD CONSTRAINT fk_payments_orders
FOREIGN KEY (order_id)
REFERENCES core.orders (order_id);

ALTER TABLE core.shipments
ADD CONSTRAINT fk_shipments_orders
FOREIGN KEY (order_id)
REFERENCES core.orders (order_id);

ALTER TABLE core.returns
ADD CONSTRAINT fk_returns_orders
FOREIGN KEY (order_id)
REFERENCES core.orders (order_id);

ALTER TABLE core.returns
ADD CONSTRAINT fk_returns_order_items
FOREIGN KEY (order_item_id)
REFERENCES core.order_items (order_item_id);

-- Se definen los CHECK para asegurar que los datos esten en el resultado vaido

ALTER TABLE core.suppliers
ADD CONSTRAINT chk_suppliers_lead_time
CHECK (lead_time_days >= 0);

ALTER TABLE core.products
ADD CONSTRAINT chk_products_unit_cost
CHECK (unit_cost >= 0);

ALTER TABLE core.products
ADD CONSTRAINT chk_products_list_price
CHECK (list_price >= 0);

ALTER TABLE core.orders
ADD CONSTRAINT chk_orders_shipping_fee
CHECK (shipping_fee >= 0);

ALTER TABLE core.orders
ADD CONSTRAINT chk_orders_total
CHECK (order_total >= 0);

ALTER TABLE core.order_items
ADD CONSTRAINT chk_order_items_quantity
CHECK (quantity > 0);

ALTER TABLE core.order_items
ADD CONSTRAINT chk_order_items_unit_price
CHECK (unit_price >= 0);

ALTER TABLE core.payments
ADD CONSTRAINT chk_payments_amount
CHECK (amount >= 0);

ALTER TABLE core.shipments
ADD CONSTRAINT chk_shipments_dates
CHECK (delivered_date IS NULL OR (shipped_date IS NOT NULL AND delivered_date >= shipped_date));

ALTER TABLE core.returns
ADD CONSTRAINT chk_returns_refund
CHECK (refund_amount >= 0);

-- Index 

CREATE INDEX idx_customers_geo
ON core.customers (geo_id);

CREATE INDEX idx_categories_parent
ON core.categories (parent_category_id);

CREATE INDEX idx_products_category
ON core.products (category_id);

CREATE INDEX idx_products_supplier
ON core.products (supplier_id);

CREATE INDEX idx_orders_customer
ON core.orders (customer_id);

CREATE INDEX idx_orders_geo
ON core.orders (geo_id);

CREATE INDEX idx_orders_date
ON core.orders (order_date);

CREATE INDEX idx_orders_status
ON core.orders (order_status);

CREATE INDEX idx_order_items_order
ON core.order_items (order_id);

CREATE INDEX idx_order_items_product
ON core.order_items (product_id);

CREATE INDEX idx_payments_order
ON core.payments (order_id);

CREATE INDEX idx_shipments_order
ON core.shipments (order_id);

CREATE INDEX idx_returns_order
ON core.returns (order_id);

CREATE INDEX idx_returns_order_item
ON core.returns (order_item_id);

