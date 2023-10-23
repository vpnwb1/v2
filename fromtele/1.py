import re

def process_line(line):
    if "ss://" in line:
        if not re.search(r'veme|vle', line):
            line = line[line.find("ss://"):]
    return line.strip()

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = [process_line(line) for line in file]

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('\n'.join(lines))


file_path = 'ready/fromtele.txt'
process_file(file_path)