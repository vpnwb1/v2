import random

def move_lines_randomly(source_file, destination_file, num_lines):
    lines = []

    with open(source_file, 'r') as source:
        lines = source.readlines()

    random.shuffle(lines)
    selected_lines = lines[:num_lines]

    with open(destination_file, 'w') as destination:
        for i, line in enumerate(selected_lines):
            embedded_text = f"[Socks5 | ساکس5{i + 1}]({line.strip()})\n\n"
            destination.write(embedded_text)


        destination.write("این پیام بروز میشود . \n@VpnWb🔑\n")

    with open(source_file, 'w') as source:
        source.writelines(lines[num_lines:])


source_file = 'socksv5.txt'
destination_file = 'urls.txt'
num_lines_to_move = 10

move_lines_randomly(source_file, destination_file, num_lines_to_move)
