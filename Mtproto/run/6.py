# Read the input text file
input_file_path = "Mtproto/temp/5.txt"
output_file_path = "Mtproto/temp/6.txt"

with open(input_file_path, "r") as input_file, open(output_file_path, "w") as output_file:
    for line in input_file:
        # Check if "&@" exists in the line
        index = line.find("&@")
        if index != -1:
            line = line[:index]  # Remove everything after "&@"
        output_file.write(line + "\n")