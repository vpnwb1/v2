import os

def separate_lines_to_protocol_files(input_file_path):
    protocols = ['ss', 'ssr', 'vmess', 'vless', 'trojan', 'hy2', 'tuic', 'hysteria', 'juicity', 'ws']
    protocol_files = {protocol: open(f"{protocol}.txt", 'w') for protocol in protocols}
    
    with open(input_file_path, 'r', encoding='utf-8', errors='replace') as input_file:
        for line in input_file:
            for protocol in protocols:
                if line.startswith(protocol + '://'):
                    protocol_files[protocol].write(line)
                    break  # Only one protocol per line

    for protocol_file in protocol_files.values():
        protocol_file.close()

    # Remove the merged input file
    os.remove(input_file_path)

# Path to the merged input file
merged_file_path = 'V2/merged_last.txt'  # Replace with the actual path

separate_lines_to_protocol_files(merged_file_path)
