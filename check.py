import pandas as pd

file_path = 'test.xlsx'
output_file_path = 'insert_statement.sql'

df = pd.read_excel(file_path, dtype=str, parse_dates=[0])

table_name = 'YourTable'

insert_statements = []

for index, row in df.iterrows():
    if isinstance(row[0], pd.Timestamp):
        date_value = row[0].strftime('%d/%m/%Y')
    else:
        date_value = str(row[0]).replace("'", "''")
    
    other_values = "', '".join(str(value).replace("'", "''") for value in row[1:])
    
    insert_statement = f"INSERT INTO {table_name} VALUES ('{date_value}', '{other_values}');"
    insert_statements.append(insert_statement)

with open(output_file_path, 'w') as file:
    file.write('\n'.join(insert_statements))

print(f"SQL insert statements saved to {output_file_path}")
