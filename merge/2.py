# List of input file names
input_files = ['fromtele/juicity.txt', 'fromtele/ss.txt', 'fromtele/ssr.txt', 'fromtele/vmess.txt', 'fromtele/vless.txt', 'fromtele/trojan.txt', 'fromtele/tuic.txt', 'fromtele/hy2.txt', 'fromtele/hysteria.txt']

# Output file name
output_file = 'merged_file.txt'

# Open the output file in write mode
with open(output_file, 'w') as outfile:
    # Iterate through each input file
    for file_name in input_files:
        # Open each input file in read mode
        with open(file_name, 'r') as infile:
            # Read the content of the input file
            content = infile.read()
            
            # Write the content to the output file
            outfile.write(content)
            
            # Add a newline between the contents of different files
            outfile.write('\n')
