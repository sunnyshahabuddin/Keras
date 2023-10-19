import pyodbc

# Define your SQL Server connection parameters
server = 'your_server_name'  # Replace with your SQL Server hostname
database = 'your_database_name'  # Replace with your database name
username = 'your_username'  # Replace with your username
password = 'your_password'  # Replace with your password

# Create a connection to the SQL Server
connection = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')

# Create a cursor to interact with the database
cursor = connection.cursor()

# Define your SQL SELECT statement
sql_query = 'SELECT * FROM your_table_name'  # Replace with your table name

# Execute the SELECT statement
cursor.execute(sql_query)

# Fetch the results
results = cursor.fetchall()

# Iterate through the results and print them
for row in results:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()
