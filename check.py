import pyodbc

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=your_server;DATABASE=your_database;UID=your_user;PWD=your_password')
cursor = conn.cursor()

with open('insert_statements.sql', 'r') as file:
    sql = file.read()

statements = sql.split(';')

batch_size = 1000
batch = []
error_log = []

for statement in statements:
    statement = statement.strip()
    if statement:
        batch.append(statement)
        if len(batch) >= batch_size:
            try:
                for stmt in batch:
                    cursor.execute(stmt)
                conn.commit()
            except Exception as e:
                error_log.append(f"Batch error: {e}")
                conn.rollback()
            batch = []

if batch:
    try:
        for stmt in batch:
            cursor.execute(stmt)
        conn.commit()
    except Exception as e:
        error_log.append(f"Batch error: {e}")
        conn.rollback()

cursor.close()
conn.close()

with open('error_log.txt', 'w') as log_file:
    for error in error_log:
        log_file.write(f"{error}\n")
