import os

####

def delete_txt_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            os.remove(file_path)

if __name__ == "__main__":
    folder_path = "split"
    delete_txt_files(folder_path)

#####

def split_file(input_file, output_prefix, lines_per_file=200):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    total_lines = len(lines)
    num_files = (total_lines + lines_per_file - 1) // lines_per_file

    for i in range(num_files):
        output_file = f"{output_prefix}_{i+1}.txt"
        with open(output_file, 'w') as f_out:
            start_idx = i * lines_per_file
            end_idx = min((i + 1) * lines_per_file, total_lines)
            f_out.writelines(lines[start_idx:end_idx])

if __name__ == "__main__":
    input_file = "SsL.txt"  # Change this to your input file
    output_prefix = "split/ss"  # Prefix for output files
    lines_per_file = 200

    split_file(input_file, output_prefix, lines_per_file)


###


def split_file(input_file, output_prefix, lines_per_file=200):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    total_lines = len(lines)
    num_files = (total_lines + lines_per_file - 1) // lines_per_file

    for i in range(num_files):
        output_file = f"{output_prefix}_{i+1}.txt"
        with open(output_file, 'w') as f_out:
            start_idx = i * lines_per_file
            end_idx = min((i + 1) * lines_per_file, total_lines)
            f_out.writelines(lines[start_idx:end_idx])

if __name__ == "__main__":
    input_file = "TrojanL.txt"  # Change this to your input file
    output_prefix = "split/tro"  # Prefix for output files
    lines_per_file = 200

    split_file(input_file, output_prefix, lines_per_file)


###


def split_file(input_file, output_prefix, lines_per_file=200):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    total_lines = len(lines)
    num_files = (total_lines + lines_per_file - 1) // lines_per_file

    for i in range(num_files):
        output_file = f"{output_prefix}_{i+1}.txt"
        with open(output_file, 'w') as f_out:
            start_idx = i * lines_per_file
            end_idx = min((i + 1) * lines_per_file, total_lines)
            f_out.writelines(lines[start_idx:end_idx])

if __name__ == "__main__":
    input_file = "TuicL.txt"  # Change this to your input file
    output_prefix = "split/tuic"  # Prefix for output files
    lines_per_file = 200

    split_file(input_file, output_prefix, lines_per_file)

###


def split_file(input_file, output_prefix, lines_per_file=200):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    total_lines = len(lines)
    num_files = (total_lines + lines_per_file - 1) // lines_per_file

    for i in range(num_files):
        output_file = f"{output_prefix}_{i+1}.txt"
        with open(output_file, 'w') as f_out:
            start_idx = i * lines_per_file
            end_idx = min((i + 1) * lines_per_file, total_lines)
            f_out.writelines(lines[start_idx:end_idx])

if __name__ == "__main__":
    input_file = "VlessL.txt"  # Change this to your input file
    output_prefix = "split/vle"  # Prefix for output files
    lines_per_file = 200

    split_file(input_file, output_prefix, lines_per_file)


###


def split_file(input_file, output_prefix, lines_per_file=200):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    total_lines = len(lines)
    num_files = (total_lines + lines_per_file - 1) // lines_per_file

    for i in range(num_files):
        output_file = f"{output_prefix}_{i+1}.txt"
        with open(output_file, 'w') as f_out:
            start_idx = i * lines_per_file
            end_idx = min((i + 1) * lines_per_file, total_lines)
            f_out.writelines(lines[start_idx:end_idx])

if __name__ == "__main__":
    input_file = "VmessL.txt"  # Change this to your input file
    output_prefix = "split/vme"  # Prefix for output files
    lines_per_file = 200

    split_file(input_file, output_prefix, lines_per_file)


###



def split_file(input_file, output_prefix, lines_per_file=200):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    total_lines = len(lines)
    num_files = (total_lines + lines_per_file - 1) // lines_per_file

    for i in range(num_files):
        output_file = f"{output_prefix}_{i+1}.txt"
        with open(output_file, 'w') as f_out:
            start_idx = i * lines_per_file
            end_idx = min((i + 1) * lines_per_file, total_lines)
            f_out.writelines(lines[start_idx:end_idx])

if __name__ == "__main__":
    input_file = "HysteriaL.txt"  # Change this to your input file
    output_prefix = "split/hy"  # Prefix for output files
    lines_per_file = 200

    split_file(input_file, output_prefix, lines_per_file)


###


def split_file(input_file, output_prefix, lines_per_file=200):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    total_lines = len(lines)
    num_files = (total_lines + lines_per_file - 1) // lines_per_file

    for i in range(num_files):
        output_file = f"{output_prefix}_{i+1}.txt"
        with open(output_file, 'w') as f_out:
            start_idx = i * lines_per_file
            end_idx = min((i + 1) * lines_per_file, total_lines)
            f_out.writelines(lines[start_idx:end_idx])

if __name__ == "__main__":
    input_file = "Hy2L.txt"  # Change this to your input file
    output_prefix = "split/hy2"  # Prefix for output files
    lines_per_file = 200

    split_file(input_file, output_prefix, lines_per_file)
###
