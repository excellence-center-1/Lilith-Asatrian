CREATE OR REPLACE FUNCTION get_total_revenue(start_date DATE, end_date DATE)
RETURNS NUMERIC AS $$
DECLARE
  total_revenue NUMERIC;
BEGIN
  SELECT SUM(p.price * od.quantity)
  INTO total_revenue
  FROM Orders o
  JOIN OrderDetails od ON o.id = od.order_id
  JOIN ProductPrices p ON od.product_price_id = p.id
  WHERE o.order_date BETWEEN start_date AND end_date;
  
  RETURN total_revenue;
END;
$$ LANGUAGE plpgsql;
