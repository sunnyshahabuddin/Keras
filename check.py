DECLARE
  v_close NUMBER := 482303.4356; -- Replace this with your actual number
BEGIN
  DBMS_OUTPUT.PUT_LINE(CASE WHEN v_close >= 1000 THEN SUBSTR(v_close, -6, 3) || '.' || TO_CHAR(MOD(v_close, 1), '00')
                            ELSE TO_CHAR(v_close, '999.00') END);
END;
