import pandas as pd

file_path = r'C:\user\initial_data.xlsx'
df = pd.read_excel(file_path)
table_name = 'YourTable'

insert_statements = []

for index, row in df.iterrows():
    if pd.api.types.is_datetime64_any_dtype(row[0]):
        row[0] = row[0].strftime('%d/%m/%Y')
    values = "', '".join(str(value).replace("'", "''") for value in row)
    insert_statement = f"INSERT INTO {table_name} VALUES ('{values}');"
    insert_statements.append(insert_statement)

output_file_path = r'C:\user\insert_statements.sql'
with open(output_file_path, 'w') as file:
    file.write('\n'.join(insert_statements))

print(f"SQL insert statements saved to {output_file_path}")
