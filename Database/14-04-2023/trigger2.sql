CREATE FUNCTION prevent_stock_quantity_negative()
RETURNS TRIGGER AS $$
BEGIN
	IF NEW.stock_quantity < 0 THEN
		RAISE EXCEPTION 'stock qunatity can not be negative';
	ENDIF
	RETURN NEW
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER prevent_stock_squantity_negative_trigger
BEFORE UPDATE ON products
FOR EACH ROW 
	EXECUTE FUNCTION prevent_stock_quantity_negative();

