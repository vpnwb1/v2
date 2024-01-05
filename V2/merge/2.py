# List of input file names
input_files = ['V2/fromtele/juicity.txt', 'V2/fromtele/ss.txt', 'V2/fromtele/ssr.txt', 'V2/fromtele/vmess.txt', 'V2/fromtele/vless.txt', 'V2/fromtele/trojan.txt', 'V2/fromtele/tuic.txt', 'V2/fromtele/hy2.txt', 'V2/fromtele/hysteria.txt']

# Output file name
output_file = 'V2/merged_file.txt'

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
