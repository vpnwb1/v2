with open('fromtele/mergedclean.txt', 'r') as file:
    lines = file.readlines()

result_lines_vless = []
result_lines_ss = []

for i, line in enumerate(lines):
    while 'vless://' in line or 'vmess://' in line or 'ss://' in line:
        vless_index = line.find('vless://')
        vmess_index = line.find('vmess://')
        ss_index = line.find('ss://')

        # Check if 'ss://' is found and it's not part of 'vless://' or 'vmess://'
        if ss_index != -1 and all(index == -1 or index > ss_index for index in [vless_index, vmess_index]):
            rest_of_line = line[ss_index:]

            # Find the index of the first '<' after 'ss://'
            closing_tag_index = rest_of_line.index('<')

            # Extract the substring from 'ss://' to the first '<'
            ss_substr = rest_of_line[:closing_tag_index]

            # Append the extracted substring to the result_lines_ss list
            result_lines_ss.append(ss_substr)

            # Update the line to exclude the processed substring
            line = rest_of_line[closing_tag_index:]
        else:
            break

with open('fromtele/ss.txt', 'w') as result_file_ss:
    for line in result_lines_ss:
        result_file_ss.write(line + '\n')
