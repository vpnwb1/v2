import random

def move_lines_randomly(source_file, destination_file, num_lines):
    lines = []
    selected_lines = []

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
        source.write('\n'.join(line for line in lines if line not in selected_lines))

def remove_empty_lines(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]

    with open(file_path, 'w') as file:
        file.write('\n'.join(lines))

source_file = 'SsrL.txt'
destination_file = 'ssrtel/tel.txt'
num_lines_to_move = 1

move_lines_randomly(source_file, destination_file, num_lines_to_move)
remove_empty_lines(destination_file)
