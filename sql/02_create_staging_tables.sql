-- Objetivo:
--   Definir tablas de staging que reciban los ficheros fuente con tipos
--   tolerantes (TEXT en todas las columnas para no rechazar filas sucias).
-- Dependencias:
--   01_create_schemas.sql
-- Entradas:
--   Ficheros CSV/Excel en data/raw/ según contrato de data_dictionary.xlsx.
-- Salidas:
--   10 tablas en el esquema staging.* listas para la importación inicial.
-- Autoría / equipo:
--   TODO: indicar nombres, apellidos y repositorio del equipo.

CREATE TABLE IF NOT EXISTS staging.geography (
    geo_id TEXT,
    country_code TEXT,
    country_name TEXT,
    region_code TEXT,
    region_name TEXT,
    city_name TEXT,
    postal_code TEXT,
    is_island TEXT
);

CREATE TABLE IF NOT EXISTS staging.customers (
    customer_id TEXT,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    phone TEXT,
    customer_segment TEXT,
    registration_date TEXT,
    geo_id TEXT,
    is_active TEXT,
    preferred_channel TEXT
);

CREATE TABLE IF NOT EXISTS staging.suppliers (
    supplier_id TEXT,
    supplier_name TEXT,
    country_code TEXT,
    contact_email TEXT,
    lead_time_days TEXT,
    reliability_score TEXT,
    is_active TEXT
);

CREATE TABLE IF NOT EXISTS staging.categories (
    category_id TEXT,
    category_name TEXT,
    parent_category_id TEXT,
    target_margin_pct TEXT
);

CREATE TABLE IF NOT EXISTS staging.products (
    product_id TEXT,
    product_name TEXT,
    sku TEXT,
    category_id TEXT,
    supplier_id TEXT,
    unit_cost TEXT,
    list_price TEXT,
    is_active TEXT,
    created_date TEXT
);

CREATE TABLE IF NOT EXISTS staging.orders (
    order_id TEXT,
    customer_id TEXT,
    order_date TEXT,
    order_status TEXT,
    channel TEXT,
    geo_id TEXT,
    discount_pct TEXT,
    shipping_fee TEXT,
    order_total TEXT
);

CREATE TABLE IF NOT EXISTS staging.order_items (
    order_item_id TEXT,
    order_id TEXT,
    product_id TEXT,
    quantity TEXT,
    unit_price TEXT,
    line_discount_pct TEXT,
    line_total TEXT
);

CREATE TABLE IF NOT EXISTS staging.payments (
    payment_id TEXT,
    order_id TEXT,
    payment_date TEXT,
    payment_method TEXT,
    payment_status TEXT,
    amount TEXT,
    currency TEXT
);

CREATE TABLE IF NOT EXISTS staging.shipments (
    shipment_id TEXT,
    order_id TEXT,
    shipped_date TEXT,
    delivered_date TEXT,
    carrier TEXT,
    shipment_status TEXT,
    tracking_code TEXT
);

CREATE TABLE IF NOT EXISTS staging.returns (
    return_id TEXT,
    order_id TEXT,
    order_item_id TEXT,
    return_date TEXT,
    return_reason TEXT,
    return_status TEXT,
    refund_amount TEXT
);