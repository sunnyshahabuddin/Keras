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

# Reorder columns to have the hardcoded ones first
data = data[['Reporting_Period', 'User_id'] + [col for col in data.columns if col not in ['Reporting_Period', 'User_id']]]

# Create a pipe-separated .dat file
dat_file_path = 'output.dat'
data.to_csv(dat_file_path, sep='|', index=False)

print(f'{xlsx_file_path} has been converted to {dat_file_path}')
