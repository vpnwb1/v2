import json

# Define a function to process the VMess configuration
def process_vmess_config(config_str):
    try:
        config = json.loads(config_str)
        if 'ps' in config:
            del config['ps']
        return json.dumps(config)
    except json.JSONDecodeError:
        # Handle invalid JSON if necessary
        return None

# Input and output file paths
input_file_path = 'vmess4.txt'
output_file_path = 'vmess5.txt'

# Read the input file and process each line
with open(input_file_path, 'r') as input_file:
    lines = input_file.readlines()

# Process each line and write to the output file
with open(output_file_path, 'w') as output_file:
    for line in lines:
        processed_config = process_vmess_config(line)
        if processed_config:
            output_file.write(processed_config + '\n')

print(f"PS entries removed and saved to {output_file_path}")
