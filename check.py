import pandas as pd
import sqlite3

# Define the Excel file and SQLite database file names
excel_file = 'your_excel_file.xlsx'
db_file = 'timeseries.db'

# Read the Excel data into a DataFrame
df = pd.read_excel(excel_file, sheet_name='Sheet1')

# Create a SQLite connection and cursor
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Define the table name and create the table with auto-increment primary key
table_name = 'timeseries_data'
create_table_query = f'''
CREATE TABLE IF NOT EXISTS {table_name} (
    tab_id INTEGER PRIMARY KEY AUTOINCREMENT,
    {", ".join([f"{col_name} TEXT" for col_name in df.columns])}
);
'''
cursor.execute(create_table_query)

# Insert data from the DataFrame into the SQLite table
for index, row in df.iterrows():
    insert_query = f'''
    INSERT INTO {table_name} ({", ".join(df.columns)})
    VALUES ({", ".join(["?" for _ in df.columns])});
    '''
    cursor.execute(insert_query, tuple(row))

# Commit the changes and close the database connection
conn.commit()
conn.close()

print(f'Data from {excel_file} has been successfully imported into {db_file}.')
