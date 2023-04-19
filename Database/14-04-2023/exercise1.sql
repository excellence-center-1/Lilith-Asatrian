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

INSERT INTO Customers (name, email, phone) VALUES
  ('John Doe', 'johndoe@example.com', '555-1234'),
  ('Jane Smith', 'janesmith@example.com', '555-5678');

INSERT INTO Products (name) VALUES
  ('Product A'),
  ('Product B'),
  ('Product C');

INSERT INTO ProductPrices (product_id, price) VALUES
  (1, 10.00),
  (2, 15.00),
  (3, 20.00);

INSERT INTO Orders (customer_id) VALUES
  (1),
  (2);

INSERT INTO OrderDetails (order_id, product_price_id, quantity) VALUES
  (1, 1, 2),
  (1, 2, 3),
  (2, 3, 1);

CREATE OR REPLACE FUNCTION GetCustomerOrders(customerId INTEGER)
RETURNS TABLE (
  CustomerName VARCHAR(50),
  CustomerEmail VARCHAR(100),
  CustomerPhone VARCHAR(50),
  TotalAmountSpent DECIMAL(10, 2)
)
AS $$
BEGIN
  RETURN QUERY
  SELECT
    c.name AS CustomerName,
    c.email AS CustomerEmail,
    c.phone AS CustomerPhone,
    SUM(p.price * od.quantity) AS TotalAmountSpent
  FROM Customers c
  JOIN Orders o ON c.id = o.customer_id
  JOIN OrderDetails od ON o.id = od.order_id
  JOIN ProductPrices p ON od.product_price_id = p.id
  WHERE c.id = customerId
  GROUP BY c.name, c.email, c.phone;
END;
$$ LANGUAGE plpgsql;


