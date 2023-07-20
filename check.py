DECLARE
  input_number NUMBER := 957562782.22; -- Replace this with your input number
  output_number NUMBER;
BEGIN
  output_number := TO_NUMBER(SUBSTR(TO_CHAR(input_number), 1, CASE WHEN input_number >= 1000 THEN LENGTH(TO_CHAR(TRUNC(input_number))) - 3 ELSE LENGTH(TO_CHAR(TRUNC(input_number))) END));
  DBMS_OUTPUT.PUT_LINE('Output: ' || output_number);
END;
/
