CREATE TABLE shops (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  address VARCHAR(50) NOT NULL,
  budget INTEGER NOT NULL,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO shops (name, address, budget, created_at)
VALUES 
  ('SAS Supermarket', 'Garni highway, Yerevan', 5000000, NOW()),
  ('Yerevan City Supermarket', 'Teryan St, Yerevan', 3000000, NOW()),
  ('Grand Candy', 'Arshakunyats Ave, Yerevan', 10000000, NOW());

CREATE TABLE suppliers (
  id SERIAL PRIMARY KEY,
  contact_name VARCHAR(50) NOT NULL,
  contact_surname VARCHAR(50) NOT NULL, 
  contact_email VARCHAR(70) NOT NULL CHECK(contact_email LIKE '%@%'),
  contact_phone VARCHAR(10) NOT NULL CHECK(contact_phone LIKE '%-%'),
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO suppliers(contact_name, contact_surname, contact_email, contact_phone, created_at)
VALUES
  ('Hayk', 'Antonyan' 'hayk.antonyan@gmail.com', '010-123456', NOW()),
  ('Melisa', 'Sahakyan' 'melisa.sahakyan@gmail.com', '077-123456', NOW()),
  ('Argishti', 'Movsisyan', 'argisht.movsisyan@gmail.com', '098-123456', NOW());

CREATE TABLE prices (
  id SERIAL PRIMARY KEY,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO prices(price) 
VALUES
(2000),
(2850), 
(3590), 
(4600);

CREATE TABLE measurements(
  id SERIAL PRIMARY KEY,
  measure VARCHAR(20)
);

INSERT INTO measurements(measure)
VALUES
('kilo'),
('gram'),
('lbs');

CREATE TABLE goods (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  description TEXT CHECK(LENGTH(description)<=100),
  supplier_id INTEGER NOT NULL REFERENCES suppliers(id),
  shop_id INTEGER NOT NULL REFERENCES shops(id),
  price_id INTEGER NOT NULL REFERENCES prices(id),
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO goods (name, description, supplier_id, shop_id, price_id)
VALUES
  ('Westgold', 'Salted butter made with milk from grass fed cows', 2, 1, 1),
  ('Feta', 'Perfect cheese for any dish needing a creamy texture and a salty kick', 1, 3, 3);

CREATE TABLE customers (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  account_balance DECIMAL(10, 2) NOT NULL,
  updated_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO customers (name, surname, account_balance)
VALUES
  ('Sahakyan', 'Anush', 15000),
  ('Vardanyan', 'Agapi', 5600),
  ('Sargsyan', 'Elen', 20000);

CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  customer_id INTEGER NOT NULL REFERENCES customers(id),
  shop_id INTEGER NOT NULL REFERENCES shops(id),
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO orders (customer_id, shop_id, created_at)
VALUES
  (2, 1, NOW()),
  (1, 3, NOW()), 
  (2, 3, NOW());

CREATE TABLE order_items (
  id SERIAL PRIMARY KEY,
  order_id INTEGER NOT NULL REFERENCES orders(id),
  good_id INTEGER NOT NULL REFERENCES goods(id),
  quantity INTEGER NOT NULL DEFAULT 1,
  measurement_id INTEGER NOT NULL REFERENCES measurements(id),
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO order_items(order_id, good_id, quantity, measurement_id)
VALUES
(1,3,2,1),
(2,1,1,3);

