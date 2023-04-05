CREATE TABLE shops (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  address VARCHAR(50) NOT NULL,
  budget INTEGER NOT NULL,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO shops (name, address, budget)
VALUES 
  ('SAS Supermarket', 'Garni highway, Yerevan', 5000000),
  ('Yerevan City Supermarket', 'Teryan St, Yerevan', 3000000),
  ('Grand Candy', 'Arshakunyats Ave, Yerevan', 10000000);

CREATE TABLE suppliers (
  id SERIAL PRIMARY KEY,
  contact_name VARCHAR(50) NOT NULL,
  contact_surname VARCHAR(50) NOT NULL, 
  contact_email VARCHAR(70) NOT NULL CHECK(contact_email LIKE '%@%'),
  contact_phone VARCHAR(10) NOT NULL CHECK(contact_phone LIKE '%-%'),
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO suppliers(contact_name, contact_surname, contact_email, contact_phone)
VALUES
  ('Hayk', 'Antonyan' 'hayk.antonyan@gmail.com', '010-123456'),
  ('Melisa', 'Sahakyan' 'melisa.sahakyan@gmail.com', '077-123456'),
  ('Argishti', 'Movsisyan', 'argisht.movsisyan@gmail.com', '098-123456');

CREATE TABLE good_prices (
  id SERIAL PRIMARY KEY,
  good_id INTEGER NOT NULL REFERENCES goods(id),
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO prices(good_id, price) 
VALUES
(1,2000),
(2,2850), 
(1,3590), 
(2,4600);

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
  price_id INTEGER NOT NULL,
  supplier_id INTEGER NOT NULL REFERENCES suppliers(id),
  shop_id INTEGER NOT NULL REFERENCES shops(id),
  measurement_id INTEGER NOT NULL REFERENCES measurements(id)
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO goods (name, description, supplier_id, shop_id, price_id, measurement_id)
VALUES
  ('Westgold', 'Salted butter made with milk from grass fed cows', 2, 1, 1,1),
  ('Feta', 'Perfect cheese for any dish needing a creamy texture and a salty kick', 1, 3, 3,1);

CREATE TABLE customers (
  id SERIAL PRIMARY KEY,
  name VARCHAR(30) NOT NULL,
  surname VARCHAR(50) NOT NULL,
  account_balance DECIMAL(10, 2) NOT NULL,
  updated_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO customers (name, surname, account_balance)
VALUES
  ('Sahakyan', 'Anush', 15000),
  ('Vardanyan', 'Agapi', 5600),
  ('Sargsyan', 'Elen', 20000);

CREATE TABLE customer_shop (
  id SERIAL PRIMARY KEY,
  customer_id INTEGER NOT NULL REFERENCES customers(id),
  shop_id INTEGER NOT NULL REFERENCES shops(id),
  supplier_id INTEGER NOT NULL REFERENCES suppliers(id),
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO customer_shop (customer_id, shop_id)
VALUES
  (2, 1),
  (1, 3), 
  (2, 3);

CREATE TABLE order (
  id SERIAL PRIMARY KEY,
  order_id INTEGER NOT NULL REFERENCES customer_shop(id),
  good_id INTEGER NOT NULL REFERENCES goods(id),
  quantity INTEGER NOT NULL DEFAULT 1,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO order(order_id, good_id, quantity)
VALUES
(1,3,2,1),
(2,1,1,3);

-- function for storing year instead of age

CREATE OR REPLACE FUNCTION update_birth_year() RETURNS TRIGGER AS $$
BEGIN
  NEW.birthyear = DATE_TRUNC('year', CURRENT_DATE) - INTERVAL '1 year' * NEW.age;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;



