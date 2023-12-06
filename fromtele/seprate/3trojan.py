with open('fromtele/mergedclean.txt', 'r') as file:
    lines = file.readlines()

result_lines = []

for i, line in enumerate(lines):
    while 'trojan://' in line:
        index = line.index('trojan://')
        rest_of_line = line[index:]

        # Find the index of the first '<' after 'trojan://'
        closing_tag_index = rest_of_line.index('<')

        # Extract the substring from 'trojan://' to the first '<'
        trojan_substr = rest_of_line[:closing_tag_index]

        # Append the extracted substring to the result_lines list
        result_lines.append(trojan_substr)

        # Update the line to exclude the processed substring
        line = rest_of_line[closing_tag_index:]

# Save the result to '2.txt'
with open('fromtele/trojan.txt', 'w') as result_file:
    for line in result_lines:
        result_file.write(line + '\n')
