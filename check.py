CREATE OR REPLACE TRIGGER validate_load
BEFORE INSERT OR UPDATE ON your_table_name
FOR EACH ROW
BEGIN
  IF :NEW.id_number IS NULL THEN
    RAISE_APPLICATION_ERROR(-20001, 'id_number cannot be NULL');
  END IF;
  IF :NEW.first_name != 'Testering' THEN
    RAISE_APPLICATION_ERROR(-20002, 'first_name must be Testering');
  END IF;
END;
/
