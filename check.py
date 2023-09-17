import pandas as pd

# Replace 'your_file.xlsx' with the path to your Excel file
file_path = 'your_file.xlsx'

# Load the Excel file into a DataFrame
df = pd.read_excel(file_path)

# Replace 'A' with the column name you want to read
column_name = 'A'

# Extract the column as a list
column_data = df[column_name].tolist()

# Create a list of JSON objects
json_data = [{"id": i+1, "name": name} for i, name in enumerate(column_data)]

# Print the JSON objects
for obj in json_data:
    print(obj)
