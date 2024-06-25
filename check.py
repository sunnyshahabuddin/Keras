DECLARE
  -- Define a cursor to fetch data from flex_adj
  CURSOR cur_flex_adj IS
    SELECT irn, first_name
    FROM flex_adj;
  
  -- Variables to hold fetched data
  v_irn flex_adj.irn%TYPE;
  v_first_name flex_adj.first_name%TYPE;
  
  -- Custom exception for validation errors
  e_validation_error EXCEPTION;
  v_error_msg VARCHAR2(4000);
  
BEGIN
  -- Open the cursor and loop through each row
  OPEN cur_flex_adj;
  LOOP
    FETCH cur_flex_adj INTO v_irn, v_first_name;
    EXIT WHEN cur_flex_adj%NOTFOUND;
    
    -- Perform validations
    IF v_irn IS NULL THEN
      v_error_msg := 'Validation Error: IRN cannot be NULL';
      RAISE e_validation_error;
    ELSIF LENGTH(v_irn) != 10 THEN
      v_error_msg := 'Validation Error: IRN must be of length 10';
      RAISE e_validation_error;
    ELSIF v_first_name IS NULL THEN
      v_error_msg := 'Validation Error: First Name cannot be NULL';
      RAISE e_validation_error;
    END IF;
    
    -- Insert into flex table if validations pass
    INSERT INTO flex (irn, first_name)
    VALUES (v_irn, v_first_name);
  END LOOP;
  CLOSE cur_flex_adj;

  -- Commit the transaction
  COMMIT;
  
EXCEPTION
  WHEN e_validation_error THEN
    -- Handle the validation error
    DBMS_OUTPUT.PUT_LINE(v_error_msg);
    ROLLBACK; -- Rollback the transaction if any validation fails
  WHEN OTHERS THEN
    -- Handle any other errors
    DBMS_OUTPUT.PUT_LINE('An unexpected error occurred: ' || SQLERRM);
    ROLLBACK;
END;
/


BEGIN
    FOR rec IN (SELECT firstname, lastname, age FROM table1) LOOP
        -- Validation checks
        IF rec.firstname = rec.lastname THEN
            RAISE_APPLICATION_ERROR(-20001, 'firstname and lastname cannot be same');
        END IF;
        
        IF rec.age < 18 THEN
            RAISE_APPLICATION_ERROR(-20002, 'age cannot be less than 18');
        END IF;

        -- If validations pass, insert the data
        INSERT INTO table2 (firstname, lastname, age)
        VALUES (rec.firstname, rec.lastname, rec.age);
    END LOOP;
END;




