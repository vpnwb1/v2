input_files = ["Mtproto/temp/1.txt", "Mtproto/temp/2.txt", "Mtproto/temp/3.txt"]
output_file = "Mtproto/temp/4.txt"

with open(output_file, "w") as merged_file:
    for input_file in input_files:
        with open(input_file, "r") as current_file:
            merged_file.write(current_file.read())