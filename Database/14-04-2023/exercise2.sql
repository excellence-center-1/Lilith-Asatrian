CREATE TABLE Customers (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  email VARCHAR(100) NOT NULL,
  phone VARCHAR(50) NOT NULL
);

CREATE TABLE Products (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50) NOT NULL
);

CREATE TABLE ProductPrices (
  id SERIAL PRIMARY KEY,
  product_id INTEGER REFERENCES Products(id) NOT NULL,
  price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE Orders (
  id SERIAL PRIMARY KEY,
  customer_id INTEGER REFERENCES Customers(id) NOT NULL
);

CREATE TABLE OrderDetails (
  id SERIAL PRIMARY KEY,
  order_id INTEGER REFERENCES Orders(id) NOT NULL,
  product_price_id INTEGER REFERENCES ProductPrices(id) NOT NULL,
  quantity INTEGER NOT NULL
);

CREATE OR REPLACE FUNCTION GetProductRevenue(productId INTEGER)
RETURNS TABLE(product_name VARCHAR(50), revenue DECIMAL(10,2)) 
AS $$
BEGIN
    RETURN QUERY SELECT p.name, SUM(od.quantity * pp.price)
    FROM Products p
    JOIN ProductPrices pp ON p.id = pp.product_id
    JOIN OrderDetails od ON pp.id = od.product_price_id
    WHERE p.id = productId
    GROUP BY p.name;
END;
$$ LANGUAGE plpgsql;
