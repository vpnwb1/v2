# Define the input and output file paths
input_file_path = 'vmess.txt'
output_file_path = 'vmess1.txt'

# Open the input file in read mode and the output file in write mode
with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    # Iterate through each line in the input file
    for line in input_file:
        # Remove "vmess://" prefix and any leading/trailing whitespace
        encoded_data = line.strip()[8:]
        # Write the modified line to the output file
        output_file.write(encoded_data + '\n')

# Print a message to indicate the process is complete
print(f"Conversion complete. Modified data saved to '{output_file_path}'.")