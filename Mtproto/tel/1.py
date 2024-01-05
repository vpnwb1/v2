import random
import os

def move_lines_randomly(source_file, destination_file, num_lines):
    lines = []
    selected_lines = []

    with open(source_file, 'r') as source:
        lines = source.readlines()

    random.shuffle(lines)
    selected_lines = lines[:num_lines]

    with open(destination_file, 'w') as destination:
        destination.writelines(selected_lines)

    with open(source_file, 'w') as source:
        source.writelines(lines[num_lines:])

# Usage
source_file = 'Mtproto/mtproto.txt'
destination_file = 'Mtproto/urls.txt'
num_lines_to_move = 5

move_lines_randomly(source_file, destination_file, num_lines_to_move)
