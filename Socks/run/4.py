with open("Socks/temp/raw3.txt", "r") as file:
    lines = file.readlines()

converted_lines = []
for line in lines:
    line = line.strip()
    values = line.split(":")
    if len(values) >= 2:
        ip, port = values[:2]
        converted_line = f"tg://socks?server={ip}&port={port}\n"
        converted_lines.append(converted_line)

with open("Socks/temp/socks3.txt", "w") as file:
    file.writelines(converted_lines)