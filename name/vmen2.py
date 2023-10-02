import re

# Define the input and output file names
input_file_name = 'vmess1.txt'
output_file_name = 'vmess2.txt'

# Regular expressions to match the specified prefixes
prefixes = ['vmess://', 'vless://', 'ss://', 'ssr://', 'trojan://']
prefix_pattern = '|'.join(map(re.escape, prefixes))

# Open the input and output files
with open(input_file_name, 'r') as input_file, open(output_file_name, 'w') as output_file:
    # Process each line in the input file
    for line in input_file:
        # Remove the specified prefixes and everything after them
        filtered_line = re.sub(f'({prefix_pattern}).*$', '', line.strip())
        # Write the filtered line to the output file
        if filtered_line:
            output_file.write(filtered_line + '\n')

print(f'Filtered data saved to {output_file_name}')
