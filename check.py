import json
import mysql.connector

# JSON data
json_data = '''
{
  "data": {
    "applicationProductView": [
      {
        "attr1": 123,
        "attr2": null,
        "attr3": 43
      },
      {
        "attr1": null,
        "attr2": null,
        "attr3": 1113
      },
      {
        "attr1": 12121,
        "attr2": null,
        "attr3": 43
      }
    ]
  }
}
'''

# Load JSON data
data = json.loads(json_data)

# Extract column names dynamically
columns = list(data['data']['applicationProductView'][0].keys())

# MySQL connection setup
db_config = {
    "host": "your_host",
    "user": "your_username",
    "password": "your_password",
    "database": "your_database",
}

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Loop through the JSON array and insert data into the database
for item in data['data']['applicationProductView']:
    # Create the SQL INSERT statement dynamically
    placeholders = ', '.join(['%s'] * len(columns))
    column_names = ', '.join(columns)
    sql = f"INSERT INTO your_table_name ({column_names}) VALUES ({placeholders})"

    # Convert 'None' to None for NULL values
    values = [item[column] if item[column] is not None else None for column in columns]

    # Execute the SQL statement
    cursor.execute(sql, values)
    conn.commit()

# Close the database connection
conn.close()
