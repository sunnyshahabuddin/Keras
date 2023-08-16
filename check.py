import pandas as pd

# Load the Excel file
excel_file_path = 'path/to/your/excel/file.xlsx'
df = pd.read_excel(excel_file_path)

# Extract values from columns E and L
column_e_values = df['E'].tolist()
column_l_values = df['L'].tolist()

# Find values in column E but not in column L
e_not_in_l = [value for value in column_e_values if value not in column_l_values]

# Find values in column L but not in column E
l_not_in_e = [value for value in column_l_values if value not in column_e_values]

# Create a DataFrame to store the results
result_df = pd.DataFrame({
    'E_not_in_L': e_not_in_l,
    'L_not_in_E': l_not_in_e
})

# Save the DataFrame to a new Excel file
output_excel_path = 'output.xlsx'
result_df.to_excel(output_excel_path, index=False)

print("Results saved to", output_excel_path)
