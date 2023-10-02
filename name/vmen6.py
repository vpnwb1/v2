import base64

# Define the input and output file names
input_file = "vmess5.txt"
output_file = "vmess6.txt"

# Open the input file for reading and the output file for writing
with open(input_file, "r") as f_in, open(output_file, "w") as f_out:
    # Read each line from the input file
    for line in f_in:
        # Remove leading and trailing whitespace
        line = line.strip()
        
        # Encode the line as base64
        encoded_line = base64.b64encode(line.encode()).decode()
        
        # Write the encoded line to the output file
        f_out.write(encoded_line + '\n')

print("Encoding complete. Output saved to", output_file)
