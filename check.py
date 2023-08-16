# Open the file in read mode
with open('reg.env', 'r') as file:
    # Read the lines from the file
    lines = file.readlines()

# Iterate through the lines and find the one containing "logPath"
for line in lines:
    if 'export logPath' in line:
        # Extract the value within single quotes
        value = line.split("'")[1]
        print(value)
        break
