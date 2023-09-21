import sqlite3

# Replace 'your_database.db' with the actual path to your SQLite database file
db_file = 'your_database.db'

# Connect to the SQLite database
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Read SQL INSERT statements from the file
with open('insert_statements.txt', 'r') as file:
    insert_statements = file.read().split(';')

# Remove any empty statements
insert_statements = [statement.strip() for statement in insert_statements if statement.strip()]

# Start a transaction
conn.execute("BEGIN TRANSACTION;")

# Execute the INSERT statements
for statement in insert_statements:
    cursor.execute(statement)

# Commit the transaction to save changes to the database
conn.execute("COMMIT;")

# Close the database connection
conn.close()
