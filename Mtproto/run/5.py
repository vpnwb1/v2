# Read the input text file
input_file_path = "Mtproto/temp/4.txt"
output_file_path = "Mtproto/temp/5.txt"

def modify_link(link):
    # Extract server, port, and secret from the link
    server_start = link.find("server=") + len("server=")
    server_end = link.find("&", server_start)
    server = link[server_start:server_end]

    port_start = link.find("port=") + len("port=")
    port_end = link.find("&", port_start)
    port = link[port_start:port_end]

    secret_start = link.find("secret=") + len("secret=")
    secret_end = len(link)
    secret = link[secret_start:secret_end]

    # Construct the modified link
    modified_link = f"tg://proxy?server={server}&port={port}&secret={secret}"
    return modified_link

with open(input_file_path, "r") as input_file, open(output_file_path, "w") as output_file:
    for line in input_file:
        modified_line = modify_link(line.strip())
        output_file.write(modified_line + "\n")