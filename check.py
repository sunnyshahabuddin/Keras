import openpyxl

def replace_newlines_in_excel(file_path, output_path):
    # Load the workbook and select the active worksheet
    wb = openpyxl.load_workbook(file_path)
    ws = wb.active

    # Iterate through all cells in the worksheet
    for row in ws.iter_rows():
        for cell in row:
            if cell.value and isinstance(cell.value, str):
                # Replace newlines with spaces
                cell.value = cell.value.replace('\n', ' ')

    # Save the modified workbook
    wb.save(output_path)

# Example usage
input_file = 'input.xlsx'  # Path to your input Excel file
output_file = 'output.xlsx'  # Path to save the modified Excel file
replace_newlines_in_excel(input_file, output_file)
