import mysql.connector

# Assuming you have the 'data' variable containing the JSON data
data = {
    "data": {
        "applicationProducViewData": [
            {
                "tc_id": "1",
                "tc_name": "测试用例1",
            },
            {
                "tc_id": "2",
                "tc_name": "测试用例2",
            },
            {
                "tc_id": "3",
                "tc_name": "测试用例3",
            }
        ]
    }
}

# MySQL database configuration
db_config = {
    "host": "localhost",
    "user": "your_username",
    "password": "your_password",
    "database": "test"
}

# Establish a connection to the MySQL server
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# Extract the test cases from the JSON data and insert into the table
test_cases = data["data"]["applicationProducViewData"]
for test_case in test_cases:
    tc_id = test_case["tc_id"]
    tc_name = test_case["tc_name"]
    
    insert_query = "INSERT INTO test_data_table (id, name) VALUES (%s, %s)"
    insert_data = (tc_id, tc_name)
    
    cursor.execute(insert_query, insert_data)
    connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()
