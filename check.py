import json

# Read the JSON data from the file
with open('data.json', 'r') as json_file:
    data = json.load(json_file)

# Extract the "sm_Business_Product_Name" values for objects with "sm_Buss_CDR" as "Jack Jones"
jack_jones_products = [item['sm_Business_Product_Name'] for item in data['applicationProductViewData'] if item['sm_Buss_CDR'] == 'Jack Jones']

# Print the list of products for Jack Jones
print(jack_jones_products)
