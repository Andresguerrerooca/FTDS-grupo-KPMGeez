-- Objetivo:
--   Crear las tablas del modelo core, ya tipadas, que representen las
--   entidades de negocio. En este paso se definen columnas y tipos; las
--   restricciones fuertes pueden ir aquí o en 04, según vuestra decisión.
-- Dependencias:
--   01_create_schemas.sql
-- Entradas:
--   Diseño del modelo (informe de arquitectura). Aún no se copian datos.
-- Salidas:
--   Tablas core.* vacías, preparadas para la carga transformada.
-- Autoría / equipo:
--   Grupo KPMGeez — [Pablo Sepúlveda, Mohammed Ghaith, Meysem Bentahar, Andres Guerrero, Martín Larrea]
--   Repositorio: https://github.com/Andresguerrerooca/FTDS-grupo-KPMGeez

-- TABLAS MAESTRAS Y DIMENSIONES

-- 1. Ubicaciones geográficas
CREATE TABLE IF NOT EXISTS core.geography (
    geo_id VARCHAR(10) NOT NULL,
    country_code CHAR(2) NOT NULL,
    country_name VARCHAR(60) NOT NULL,
    region_code VARCHAR(10) NOT NULL,
    region_name VARCHAR(60) NOT NULL,
    city_name VARCHAR(60) NOT NULL,
    postal_code VARCHAR(12) NOT NULL,
    is_island BOOLEAN NOT NULL
);

-- 2. Clientes registrados
CREATE TABLE IF NOT EXISTS core.customers (
    customer_id VARCHAR(20) NOT NULL,
    first_name VARCHAR(40) NOT NULL,
    last_name VARCHAR(40) NOT NULL,
    email VARCHAR(120) NOT NULL,
    phone VARCHAR(24),
    customer_segment VARCHAR(20) NOT NULL,
    registration_date DATE NOT NULL,
    geo_id VARCHAR(10) NOT NULL,
    is_active BOOLEAN NOT NULL,
    preferred_channel VARCHAR(30) NOT NULL
);

-- 3. Proveedores
CREATE TABLE IF NOT EXISTS core.suppliers (
    supplier_id VARCHAR(30) NOT NULL,
    supplier_name VARCHAR(100) NOT NULL,
    country_code CHAR(2) NOT NULL,
    contact_email VARCHAR(120) NOT NULL,
    lead_time_days INTEGER NOT NULL,
    reliability_score NUMERIC(5, 4) NOT NULL,
    is_active BOOLEAN NOT NULL
);

-- 4. Categorías de producto
CREATE TABLE IF NOT EXISTS core.categories (
    category_id VARCHAR(20) NOT NULL,
    category_name VARCHAR(50) NOT NULL,
    parent_category_id VARCHAR(20),
    target_margin_pct NUMERIC(5, 4) NOT NULL
);

-- 5. Catálogo de productos
CREATE TABLE IF NOT EXISTS core.products (
    product_id VARCHAR(20) NOT NULL,
    product_name VARCHAR(120) NOT NULL,
    sku VARCHAR(30) NOT NULL,
    category_id VARCHAR(20) NOT NULL,
    supplier_id VARCHAR(30) NOT NULL,
    unit_cost NUMERIC(10, 2) NOT NULL,
    list_price NUMERIC(10, 2) NOT NULL,
    is_active BOOLEAN NOT NULL,
    created_date DATE NOT NULL
);

-- TABLAS TRANSACCIONALES Y DE EVENTOS

-- 6. Cabecera de pedidos
CREATE TABLE IF NOT EXISTS core.orders (
    order_id VARCHAR(30) NOT NULL,
    customer_id VARCHAR(20) NOT NULL,
    order_date DATE NOT NULL,
    order_status VARCHAR(20) NOT NULL,
    channel VARCHAR(20) NOT NULL,
    geo_id VARCHAR(10) NOT NULL,
    discount_pct NUMERIC(5, 4) NOT NULL,
    shipping_fee NUMERIC(10, 2) NOT NULL,
    order_total NUMERIC(12, 2) NOT NULL
);

-- 7. Líneas de detalle de cada pedido
CREATE TABLE IF NOT EXISTS core.order_items (
    order_item_id VARCHAR(20) NOT NULL,
    order_id VARCHAR(30) NOT NULL,
    product_id VARCHAR(20) NOT NULL,
    quantity INTEGER NOT NULL,
    unit_price NUMERIC(10, 2) NOT NULL,
    line_discount_pct NUMERIC(5, 4) NOT NULL,
    line_total NUMERIC(12, 2) NOT NULL
);

-- 8. Pagos asociados a pedidos
CREATE TABLE IF NOT EXISTS core.payments (
    payment_id VARCHAR(30) NOT NULL,
    order_id VARCHAR(30) NOT NULL,
    payment_date DATE NOT NULL,
    payment_method VARCHAR(30) NOT NULL,
    payment_status VARCHAR(30) NOT NULL,
    amount NUMERIC(12, 2) NOT NULL,
    currency CHAR(3) NOT NULL
);

-- 9. Envíos y seguimiento logístico
CREATE TABLE IF NOT EXISTS core.shipments (
    shipment_id VARCHAR(30) NOT NULL,
    order_id VARCHAR(30) NOT NULL,
    shipped_date DATE,
    delivered_date DATE,
    carrier VARCHAR(30) NOT NULL,
    shipment_status VARCHAR(30) NOT NULL,
    tracking_code VARCHAR(30)
);

-- 10. Devoluciones sobre líneas de pedido
CREATE TABLE IF NOT EXISTS core.returns (
    return_id VARCHAR(30) NOT NULL,
    order_id VARCHAR(30) NOT NULL,
    order_item_id VARCHAR(20) NOT NULL,
    return_date DATE NOT NULL,
    return_reason VARCHAR(40) NOT NULL,
    return_status VARCHAR(30) NOT NULL,
    refund_amount NUMERIC(10, 2) NOT NULL
);