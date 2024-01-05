import re

# Open the input and output files
input_filename = 'V2/ssr2.txt'
output_filename = 'V2/ssr3.txt'

with open(input_filename, 'r', encoding='utf-8') as input_file, open(output_filename, 'w', encoding='utf-8') as output_file:
    # Read each line from the input file
    for line in input_file:
        # Use regular expressions to remove the "remarks" parameter and its value
        modified_line = re.sub(r'remarks=[^&]*&?', '', line)

        # Write the modified line to the output file
        output_file.write(modified_line)

print(f'Removed "remarks" parameters and saved the result to {output_filename}')
