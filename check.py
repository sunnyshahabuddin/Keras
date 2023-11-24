DECLARE
   table_name VARCHAR2(30) := 'YOUR_TABLE_NAME'; -- Replace with the actual table name

   table_count NUMBER;
BEGIN
   -- Check if the table exists
   SELECT COUNT(*)
   INTO table_count
   FROM USER_TABLES
   WHERE TABLE_NAME = table_name;

   -- If the table exists, delete it
   IF table_count > 0 THEN
      EXECUTE IMMEDIATE 'DROP TABLE ' || table_name;
      DBMS_OUTPUT.PUT_LINE('Table ' || table_name || ' has been deleted.');
   ELSE
      DBMS_OUTPUT.PUT_LINE('Table ' || table_name || ' does not exist.');
   END IF;
END;
/
