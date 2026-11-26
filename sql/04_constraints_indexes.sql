-- Archivo: sql/04_constraints_indexes.sql
-- Objetivo:
--   Añadir las reglas de seguridad (claves primarias, claves foráneas y reglas
--   CHECK) e índices a las tablas del esquema core para evitar datos repetidos,
--   incoherentes o sin relación.
-- Dependencias:
--   03_create_core_tables.sql (las tablas de core deben existir antes).
--   ¿Por qué ejecutamos el 04 antes del 05?: Aplicamos estas reglas ahora que
--   las tablas de core están vacías. Así, cuando carguemos los datos limpios
--   en el paso 05, la propia base de datos nos avisará al momento si se cuela
--   algún error, duplicado o dato huérfano.
-- Entradas:
--   Las 10 tablas vacías del esquema core.
-- Salidas:
--   Las mismas 10 tablas de core ya protegidas con sus relaciones entre tablas
--   e índices para que las consultas futuras vayan más rápido.
-- Autoría / equipo:
--   Grupo KPMGeez — [Pablo Sepúlveda, Mohammed Ghaith, Meysem Bentahar, Andres Guerrero, Martín Larrea]
--   Repositorio: https://github.com/Andresguerrerooca/FTDS-grupo-KPMGeez

-- 1. CLAVES PRIMARIAS (PRIMARY KEY)

ALTER TABLE core.geography
    ADD CONSTRAINT pk_geography PRIMARY KEY (geo_id);

ALTER TABLE core.customers
    ADD CONSTRAINT pk_customers PRIMARY KEY (customer_id);

ALTER TABLE core.suppliers
    ADD CONSTRAINT pk_suppliers PRIMARY KEY (supplier_id);

ALTER TABLE core.categories
    ADD CONSTRAINT pk_categories PRIMARY KEY (category_id);

ALTER TABLE core.products
    ADD CONSTRAINT pk_products PRIMARY KEY (product_id);

ALTER TABLE core.orders
    ADD CONSTRAINT pk_orders PRIMARY KEY (order_id);

ALTER TABLE core.order_items
    ADD CONSTRAINT pk_order_items PRIMARY KEY (order_item_id);

ALTER TABLE core.payments
    ADD CONSTRAINT pk_payments PRIMARY KEY (payment_id);

ALTER TABLE core.shipments
    ADD CONSTRAINT pk_shipments PRIMARY KEY (shipment_id);

ALTER TABLE core.returns
    ADD CONSTRAINT pk_returns PRIMARY KEY (return_id);

-- 2. CLAVES FORÁNEAS (FOREIGN KEY)

-- Tablas maestras y dimensiones
ALTER TABLE core.customers
    ADD CONSTRAINT fk_customers_geo
    FOREIGN KEY (geo_id) REFERENCES core.geography (geo_id);

ALTER TABLE core.categories
    ADD CONSTRAINT fk_categories_parent
    FOREIGN KEY (parent_category_id) REFERENCES core.categories (category_id);

ALTER TABLE core.products
    ADD CONSTRAINT fk_products_category
    FOREIGN KEY (category_id) REFERENCES core.categories (category_id);

ALTER TABLE core.products
    ADD CONSTRAINT fk_products_supplier
    FOREIGN KEY (supplier_id) REFERENCES core.suppliers (supplier_id);

-- Tablas transaccionales y de eventos
ALTER TABLE core.orders
    ADD CONSTRAINT fk_orders_customer
    FOREIGN KEY (customer_id) REFERENCES core.customers (customer_id);

ALTER TABLE core.orders
    ADD CONSTRAINT fk_orders_geo
    FOREIGN KEY (geo_id) REFERENCES core.geography (geo_id);

ALTER TABLE core.order_items
    ADD CONSTRAINT fk_order_items_order
    FOREIGN KEY (order_id) REFERENCES core.orders (order_id);

ALTER TABLE core.order_items
    ADD CONSTRAINT fk_order_items_product
    FOREIGN KEY (product_id) REFERENCES core.products (product_id);

ALTER TABLE core.payments
    ADD CONSTRAINT fk_payments_order
    FOREIGN KEY (order_id) REFERENCES core.orders (order_id);

ALTER TABLE core.shipments
    ADD CONSTRAINT fk_shipments_order
    FOREIGN KEY (order_id) REFERENCES core.orders (order_id);

ALTER TABLE core.returns
    ADD CONSTRAINT fk_returns_order
    FOREIGN KEY (order_id) REFERENCES core.orders (order_id);

ALTER TABLE core.returns
    ADD CONSTRAINT fk_returns_order_item
    FOREIGN KEY (order_item_id) REFERENCES core.order_items (order_item_id);

-- 3. REGLAS DE NEGOCIO Y DOMINIO (CHECK)

-- Geography: prefijo
ALTER TABLE core.geography
    ADD CONSTRAINT chk_geography_id_prefix CHECK (geo_id LIKE 'GEO-%');

-- Suppliers: prefijo, plazos no negativos y fiabilidad entre 0 y 1
ALTER TABLE core.suppliers
    ADD CONSTRAINT chk_suppliers_id_prefix CHECK (supplier_id LIKE 'SUP-%'),
    ADD CONSTRAINT chk_suppliers_lead_time CHECK (lead_time_days >= 0),
    ADD CONSTRAINT chk_suppliers_reliability CHECK (reliability_score BETWEEN 0 AND 1);

-- Categories: prefijo y margen objetivo entre 0 y 1
ALTER TABLE core.categories
    ADD CONSTRAINT chk_categories_id_prefix CHECK (category_id LIKE 'CAT-%'),
    ADD CONSTRAINT chk_categories_target_margin CHECK (target_margin_pct BETWEEN 0 AND 1);

-- Products: prefijo, costes y precios no negativos
ALTER TABLE core.products
    ADD CONSTRAINT chk_products_id_prefix CHECK (product_id LIKE 'PRD-%'),
    ADD CONSTRAINT chk_products_unit_cost CHECK (unit_cost >= 0),
    ADD CONSTRAINT chk_products_list_price CHECK (list_price >= 0);

-- Customers: prefijo y valores válidos de segmento y canal
ALTER TABLE core.customers
    ADD CONSTRAINT chk_customers_id_prefix CHECK (customer_id LIKE 'CUST-%'),
    ADD CONSTRAINT chk_customers_segment
        CHECK (customer_segment IN ('premium', 'standard', 'occasional')),
    ADD CONSTRAINT chk_customers_channel
        CHECK (preferred_channel IN ('web', 'mobile_app', 'marketplace'));

-- Orders: prefijo, estados, canales, descuentos e importes no negativos
ALTER TABLE core.orders
    ADD CONSTRAINT chk_orders_id_prefix CHECK (order_id LIKE 'ORD-%'),
    ADD CONSTRAINT chk_orders_status
        CHECK (order_status IN ('pending', 'paid', 'shipped', 'delivered', 'cancelled', 'returned')),
    ADD CONSTRAINT chk_orders_channel
        CHECK (channel IN ('web', 'mobile_app', 'marketplace')),
    ADD CONSTRAINT chk_orders_discount CHECK (discount_pct BETWEEN 0 AND 1),
    ADD CONSTRAINT chk_orders_shipping_fee CHECK (shipping_fee >= 0),
    ADD CONSTRAINT chk_orders_total CHECK (order_total >= 0);

-- Order items: prefijo, cantidades positivas y precios/descuentos válidos
ALTER TABLE core.order_items
    ADD CONSTRAINT chk_order_items_id_prefix CHECK (order_item_id LIKE 'ITM-%'),
    ADD CONSTRAINT chk_order_items_quantity CHECK (quantity > 0),
    ADD CONSTRAINT chk_order_items_unit_price CHECK (unit_price >= 0),
    ADD CONSTRAINT chk_order_items_discount CHECK (line_discount_pct BETWEEN 0 AND 1),
    ADD CONSTRAINT chk_order_items_total CHECK (line_total >= 0);

-- Payments: prefijo, métodos, estados e importes no negativos
ALTER TABLE core.payments
    ADD CONSTRAINT chk_payments_id_prefix CHECK (payment_id LIKE 'PAY-%'),
    ADD CONSTRAINT chk_payments_method
        CHECK (payment_method IN ('card', 'paypal', 'transfer', 'bizum')),
    ADD CONSTRAINT chk_payments_status
        CHECK (payment_status IN ('pending', 'completed', 'failed', 'refunded')),
    ADD CONSTRAINT chk_payments_amount CHECK (amount >= 0);

-- Shipments: prefijo, transportistas, estados y entrega >= envío
ALTER TABLE core.shipments
    ADD CONSTRAINT chk_shipments_id_prefix CHECK (shipment_id LIKE 'SHP-%'),
    ADD CONSTRAINT chk_shipments_carrier
        CHECK (carrier IN ('rapidex', 'correosnube', 'lentolog')),
    ADD CONSTRAINT chk_shipments_status
        CHECK (shipment_status IN ('pending', 'in_transit', 'delivered', 'delayed', 'returned_to_sender')),
    ADD CONSTRAINT chk_shipments_dates
        CHECK (delivered_date IS NULL OR shipped_date IS NULL OR delivered_date >= shipped_date);

-- Returns: prefijo, motivos, estados y reembolso no negativo
ALTER TABLE core.returns
    ADD CONSTRAINT chk_returns_id_prefix CHECK (return_id LIKE 'RET-%'),
    ADD CONSTRAINT chk_returns_reason
        CHECK (return_reason IN ('size', 'damaged', 'delayed', 'not_as_described', 'other')),
    ADD CONSTRAINT chk_returns_status
        CHECK (return_status IN ('requested', 'approved', 'rejected', 'refunded')),
    ADD CONSTRAINT chk_returns_refund CHECK (refund_amount >= 0);

-- 4. ÍNDICES (CLAVES FORÁNEAS Y FILTROS FRECUENTES)

-- Dimensiones y maestras (cruces habituales)
CREATE INDEX IF NOT EXISTS idx_customers_geo_id ON core.customers (geo_id);
CREATE INDEX IF NOT EXISTS idx_products_category_id ON core.products (category_id);
CREATE INDEX IF NOT EXISTS idx_products_supplier_id ON core.products (supplier_id);

-- Tablas transaccionales y de eventos (JOINs y filtros analíticos)
CREATE INDEX IF NOT EXISTS idx_orders_customer_id ON core.orders (customer_id);
CREATE INDEX IF NOT EXISTS idx_orders_geo_id ON core.orders (geo_id);
CREATE INDEX IF NOT EXISTS idx_orders_order_date ON core.orders (order_date);
CREATE INDEX IF NOT EXISTS idx_orders_order_status ON core.orders (order_status);

CREATE INDEX IF NOT EXISTS idx_order_items_order_id ON core.order_items (order_id);
CREATE INDEX IF NOT EXISTS idx_order_items_product_id ON core.order_items (product_id);

CREATE INDEX IF NOT EXISTS idx_payments_order_id ON core.payments (order_id);
CREATE INDEX IF NOT EXISTS idx_shipments_order_id ON core.shipments (order_id);

CREATE INDEX IF NOT EXISTS idx_returns_order_id ON core.returns (order_id);
CREATE INDEX IF NOT EXISTS idx_returns_order_item_id ON core.returns (order_item_id);