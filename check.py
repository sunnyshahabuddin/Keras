import pandas as pd

# Path to the Excel file
file_path = r'C:\user\initial_data.xlsx'

# Load the Excel file
df = pd.read_excel(file_path)

# Define the name of the table where data will be inserted
table_name = 'YourTable'  # Replace with your actual table name

# List to store the SQL insert statements
insert_statements = []

# Loop through each row in the dataframe and create an INSERT statement
for index, row in df.iterrows():
    # Convert each value to string and handle special cases (like quotes)
    values = "', '".join(str(value).replace("'", "''") for value in row)
    # Construct the INSERT statement
    insert_statement = f"INSERT INTO {table_name} VALUES ('{values}');"
    insert_statements.append(insert_statement)

# Save the insert statements to a file
output_file_path = r'C:\user\insert_statements.sql'
with open(output_file_path, 'w') as file:
    file.write('\n'.join(insert_statements))

print(f"SQL insert statements saved to {output_file_path}")
