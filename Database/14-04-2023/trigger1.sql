CREATE OR REPLACE FUNCTION update_customer_total_orders()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE customer
    SET total_orders = total_orders + 1
    WHERE id = NEW.customer_id;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_customer_total_orders_trigger
AFTET INSERT ON orders
FOR EACH ROW 
EXECUTE FUNCTION update_customer_total_orders();
