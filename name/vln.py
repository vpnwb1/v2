with open('vless.txt', 'r') as file:
    lines = file.readlines()

# Remove the server name after the # symbol in each line
modified_lines = [line.split('#')[0] for line in lines]

# Write the modified lines to a new output file
with open('Vless.txt', 'w') as file:
    file.write('\n'.join(modified_lines))

