import pandas as pd

# Read the Excel file
df = pd.read_excel('country.xlsx', sheet_name='Sheet1')

# Extract values from the third column (RES_0300)
values = df['RES_0300'].tolist()

# Format the values as 'value1', 'value2', 'value3', ...
formatted_values = ', '.join([f"'{value}'" for value in values])

# Write the formatted values to a .txt file
with open('output.txt', 'w') as file:
    file.write(formatted_values)
