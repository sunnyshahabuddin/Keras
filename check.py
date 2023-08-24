import pandas as pd

# Read the Excel file
xlsx_file_path = 'input.xlsx'
data = pd.read_excel(xlsx_file_path)

# Hardcoded values
reporting_period = '20230731'
user_id = 'G025555'

# Add hardcoded columns
data['Reporting_Period'] = reporting_period
data['User_id'] = user_id

# Process columns with date values
date_columns = [col for col in data.columns if 'date' in col.lower()]
for col in date_columns:
    data[col] = data[col].apply(lambda x: x.strftime('%d/%m/%Y') if pd.notnull(x) else '')

# Format columns with leading zeros
columns_with_zeros = ['Column1', 'Column2']  # Add column names here
for col in columns_with_zeros:
    data[col] = data[col].apply(lambda x: f'{x:0>7}' if pd.notnull(x) else '')

# Replace NaN with blank
data = data.where(pd.notna(data), '')

# Create a pipe-separated .dat file
dat_file_path = 'output.dat'
data.to_csv(dat_file_path, sep='|', index=False, na_rep='', date_format='%d/%m/%Y')

print(f'{xlsx_file_path} has been converted to {dat_file_path}')
