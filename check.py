import pandas as pd
import mysql.connector
from mysql.connector import errorcode

# Configuration for MySQL connection
config = {
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',
    'database': 'your_database'
}

# Path to your Excel file
excel_file_path = 'path_to_your_excel_file.xlsx'

# Read Excel file into DataFrame
df = pd.read_excel(excel_file_path)

# Establish MySQL connection
try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    
    # Insert data into table
    insert_query = f"""
    INSERT INTO inc_data ({', '.join(df.columns)}) VALUES ({', '.join(['%s'] * len(df.columns))})
    """
    
    for row in df.itertuples(index=False):
        cursor.execute(insert_query, tuple(row))
    
    # Commit the transaction
    conn.commit()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection is closed")
