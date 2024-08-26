import pandas as pd

# Path to the Excel file
file_path = r'C:\user\initial_data.xlsx'

# Load the Excel file and ensure the first column is treated as a date
df = pd.read_excel(file_path, parse_dates=[0])

# Define the name of the table where data will be inserted
table_name = 'YourTable'

# List to store the SQL insert statements
insert_statements = []

# Loop through each row in the dataframe and create an INSERT statement
for index, row in df.iterrows():
    # Ensure the first column (date) is formatted as DD/MM/YYYY
    if isinstance(row[0], pd.Timestamp):
        date_value = row[0].strftime('%d/%m/%Y')
    else:
        date_value = str(row[0]).replace("'", "''")
    
    # Convert the remaining columns to strings and handle special cases (like quotes)
    other_values = "', '".join(str(value).replace("'", "''") for value in row[1:])
    
    # Construct the INSERT statement
    insert_statement = f"INSERT INTO {table_name} VALUES ('{date_value}', '{other_values}');"
    insert_statements.append(insert_statement)

# Save the insert statements to a file
output_file_path = r'C:\user\insert_statements.sql'
with open(output_file_path, 'w') as file:
    file.write('\n'.join(insert_statements))

print(f"SQL insert statements saved to {output_file_path}")
