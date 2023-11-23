DELETE FROM your_table
WHERE ROWID NOT IN (
    SELECT MAX(ROWID) AS max_rowid
    FROM your_table
    GROUP BY a, b, c
    HAVING COUNT(*) > 1
);
