import json
from openpyxl import Workbook

var = b'{"@data.context": "http://schema.org", "@data.type": "Person", "@data.id": "http://www.example.com", "@data.name": "John Doe", "value":[{"data": "test", "data2": "test2"}, {"data": "test3", "data2": "test4"}]}'

# Convert bytes to string and then parse JSON
var_str = var.decode('utf-8')
data = json.loads(var_str)

# Extract value
value = data.get('value')

# Extract headers dynamically
headers = set()
for item in value:
    headers.update(item.keys())

# Create a new Excel workbook
wb = Workbook()
ws = wb.active

# Write headers
ws.append(list(headers))

# Write value
for item in value:
    ws.append([item.get(key, '') for key in headers])

# Save workbook
wb.save('value.xlsx')
