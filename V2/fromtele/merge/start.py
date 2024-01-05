import os

def merge_files(folder_path, output_file, encoding='utf-8'):
    with open(output_file, 'w', encoding=encoding) as outfile:
        for file_name in os.listdir(folder_path):
            if file_name.endswith('.txt'):
                file_path = os.path.join(folder_path, file_name)
                with open(file_path, 'r', encoding=encoding, errors='ignore') as infile:
                    for line in infile:
                        outfile.write(line)
                os.remove(file_path)  # Remove the .txt file after merging

# Example usage
folder_path = 'V2/fromtele/fetch'
output_file = 'V2/fromtele/merged.txt'

merge_files(folder_path, output_file)