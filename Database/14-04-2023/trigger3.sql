CREATE TABLE employee_audit (
	employee_id INTEGER,
	old_salary NUMERIC,
	new_salary NUMERIC,
	change_date TIMESTAMP DEFAULT now()
);

CREATE FUNCTION employee_salary_change()
RETURN TRIGGER AS $$
BEGIN
	IF NEW.salary <> OLD.salary THEN
		INSERT INTO employee_audit(employee_id, old_salary, new_salary)
		VALUES (OLD.employee_id, OLD.salary, NEW.salary);
	END IF;
	RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER employee_salary_change_trigger
AFTER UPDATE ON employees
FOR EACH ROW
	EXECUTE FUNTION employee_salary_change();

