-- Check if the adjustment table exists for the specified data source
IF EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = {{sourceAdjustmentTable('ds_enrich_missing', @EXEC_DATE)}})
BEGIN
    -- If the adjustment table exists, then execute the DELETE statement
    DELETE FROM {{sourceAdjustmentTable('ds_enrich_missing', @EXEC_DATE)}};
END
