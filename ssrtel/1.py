import random

###

with open('SsrL.txt', 'r') as file1:
    lines = file1.readlines()

non_empty_lines = [line.strip() for line in lines if line.strip()]

with open('SsrL.txt', 'w') as file2:
    file2.write('\n'.join(non_empty_lines))

###
def move_lines_randomly(source_file, destination_file, num_lines):
    lines = []
    selected_lines = []

    with open(source_file, 'r') as source:
        lines = source.readlines()

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

source_file = 'SsrL.txt'
destination_file = 'ssrtel/tel.txt'
num_lines_to_move = 5

move_lines_randomly(source_file, destination_file, num_lines_to_move)
remove_empty_lines(destination_file)
