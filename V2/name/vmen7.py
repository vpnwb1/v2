# Open the input file for reading
with open("V2/vmess6.txt", "r") as input_file:
    # Read the lines from the input file
    lines = input_file.readlines()

# Add "vmess://" to the beginning of each line
modified_lines = ["vmess://" + line.strip() for line in lines]

# Open the output file for writing
with open("V2/Vmess.txt", "w") as output_file:
    # Write the modified lines to the output file
    output_file.write("\n".join(modified_lines))

