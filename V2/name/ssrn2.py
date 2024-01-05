import base64

def repair_base64_padding(s):
    missing_padding = len(s) % 4
    if missing_padding:
        s += '=' * (4 - missing_padding)
    return s

def decode_base64_and_save(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    decoded_lines = []
    for line in lines:
        line = line.strip()
        line = line.replace('_', '/')  # Replace _ with /
        line = repair_base64_padding(line)
        
        try:
            decoded_line = base64.b64decode(line).decode('utf-8')
            decoded_lines.append(decoded_line)
        except Exception as e:
            print(f"Error decoding line: {e}")
            decoded_lines.append(f"{line}")

    with open(output_file, 'w') as f:
        f.write('\n'.join(decoded_lines))

if __name__ == "__main__":
    input_file_path = "V2/ssr1.txt"  # Replace with your input file path
    output_file_path = "V2/ssr2.txt"  # Replace with desired output file path

    decode_base64_and_save(input_file_path, output_file_path)
    print("Decoding and saving complete.")
