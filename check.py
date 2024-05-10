UPDATE your_table_name
SET date_insight = REGEXP_REPLACE(date_insight, '\\s+', '');
