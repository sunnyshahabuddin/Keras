input_file = "input.txt"
output_file = "output.txt"

with open(input_file, "r") as f_input, open(output_file, "w") as f_output:
    for line in f_input:
        # Split the line using '|' as the delimiter
        parts = line.strip().split('|')
        
        if len(parts) >= 7:
            # Remove the 7th '|' from the list of parts
            parts.pop(6)
            
            # Join the modified parts back together with '|' and write to the output file
            modified_line = '|'.join(parts) + '\n'
            f_output.write(modified_line)

print("Task completed. The modified data has been written to output.txt.")
