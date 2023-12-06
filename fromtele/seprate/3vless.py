with open('fromtele/mergedclean.txt', 'r') as file:
    lines = file.readlines()

result_lines = []

for i, line in enumerate(lines):
    while 'vless://' in line:
        index = line.index('vless://')
        rest_of_line = line[index:]

        # Find the index of the first '<' after 'vless://'
        closing_tag_index = rest_of_line.index('<')

        # Extract the substring from 'vless://' to the first '<'
        vless_substr = rest_of_line[:closing_tag_index]

        # Append the extracted substring to the result_lines list
        result_lines.append(vless_substr)

        # Update the line to exclude the processed substring
        line = rest_of_line[closing_tag_index:]

# Save the result to '2.txt'
with open('fromtele/vless.txt', 'w') as result_file:
    for line in result_lines:
        result_file.write(line + '\n')
