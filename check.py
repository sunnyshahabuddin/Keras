DECLARE
  input_number NUMBER := 78455.1155; -- Replace this with your input number
  output_number NUMBER;
BEGIN
  output_number := TO_NUMBER(CASE WHEN input_number >= 1000 THEN SUBSTR(TO_CHAR(input_number), 1, LENGTH(TO_CHAR(TRUNC(input_number))) - 3) ELSE '0' END);
  DBMS_OUTPUT.PUT_LINE('Output: ' || output_number);
END;
/
