input_file = "Mtproto/temp/6.txt"
output_file = "Mtproto/temp/7.txt"

with open(input_file, "r") as file:
    lines = file.readlines()

# Remove empty lines
non_empty_lines = [line.strip() for line in lines if line.strip()]

with open(output_file, "w") as file:
    file.write("\n".join(non_empty_lines))