import pandas as pd

file_path = r'C:\user\initial_data.xlsx'

df = pd.read_excel(file_path, dtype=str, parse_dates=[0])

table_name = 'YourTable'

insert_statements = []

for index, row in df.iterrows():
    if isinstance(row[0], pd.Timestamp):
        date_value = row[0].strftime('%d/%m/%Y')
    else:
        date_value = str(row[0]).replace("'", "''")
    
    other_values = []
    for i, value in enumerate(row[1:]):
        if i == len(row[1:]) - 1:
            if value.isnumeric():
                other_values.append(str(int(value)))
            else:
                other_values.append(f"'{str(value).replace("'", "''")}'")
        else:
            other_values.append(f"'{str(value).replace("'", "''")}'")
    
    other_values_str = ', '.join(other_values)
    
    insert_statement = f"INSERT INTO {table_name} VALUES ('{date_value}', {other_values_str});"
    insert_statements.append(insert_statement)

output_file_path = r'C:\user\insert_statements.sql'
with open(output_file_path, 'w') as file:
    file.write('\n'.join(insert_statements))

print(f"SQL insert statements saved to {output_file_path}")
