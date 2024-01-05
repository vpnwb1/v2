def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                destination.write(source.read())
        print(f"Successfully copied {source_file} to {destination_file}!")
    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")

copy_file("Socks/socksv5.txt", "socksF.txt")
