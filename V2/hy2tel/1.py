import random
import os

###

source_file = 'Hy2L.txt'
destination_file = 'V2/hy2tel/tel.txt'
num_lines_to_move = 5

with open(source_file, 'r') as file1:
    lines = file1.readlines()

non_empty_lines = [line.strip() for line in lines if line.strip()]

with open(source_file, 'w') as file2:
    file2.write('\n'.join(non_empty_lines))

if not any(len(line) >= 8 for line in non_empty_lines):
    print("No lines with at least 8 characters found. Removing file:", destination_file)
    os.remove(destination_file)
else:
    def move_lines_randomly(source_file, destination_file, num_lines):
        lines = []

        with open(source_file, 'r') as source:
            lines = [line.strip() for line in source if len(line.strip()) >= 8]

        if not lines:
            print("No lines with at least 8 characters found.")
            return

        random.shuffle(lines)
        selected_lines = lines[:num_lines]

        with open(destination_file, 'w') as destination:
            destination.write('\n'.join(selected_lines))

        with open(source_file, 'w') as source:
            source.write('\n'.join(lines[num_lines:]))

    def remove_empty_lines(file_path):
        with open(file_path, 'r') as file:
            lines = [line.strip() for line in file if line.strip()]

        with open(file_path, 'w') as file:
            file.write('\n'.join(lines))

    move_lines_randomly(source_file, destination_file, num_lines_to_move)
    remove_empty_lines(destination_file)
