import os

def remove_files(file_paths):
    for path in file_paths:
        try:
            os.remove(path)
            print(f"Deleted file: {path}")
        except FileNotFoundError:
            print(f"File not found: {path}")
        except IsADirectoryError:
            print(f"Cannot delete directory: {path}")

# List of file paths to be deleted
file_paths = [
    "Socks/temp/raw1.txt",
    "Socks/temp/raw2.txt",
    "Socks/temp/raw3.txt",
    "Socks/temp/socks1.txt",
    "Socks/temp/socks2.txt",
    "Socks/temp/socks3.txt"
]

remove_files(file_paths)