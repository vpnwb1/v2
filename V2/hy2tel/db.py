# Open tel.txt in read mode
with open('V2/hy2tel/tel.txt', 'r') as file:
    # Read all lines from tel.txt
    lines = file.readlines()

# Open db.txt in append mode
with open('V2/hy2tel/db.txt', 'a') as file:
    # Write all lines from tel.txt to db.txt
    file.writelines(lines)
    # Add a newline character to the last line
    if lines:
        file.write('\n')

print("Lines copied from tel.txt to db.txt.")
