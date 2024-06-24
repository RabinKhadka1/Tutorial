CREATE DATABASE ecommerce;

\c ecommerce;

CREATE TABLE product (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    price FLOAT NOT NULL
);

INSERT INTO product (name, price) VALUES 
('Product A', 10),
('Product B', 20),
('Product C', 30);
