import base64


def encode_and_fix_base64(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    encoded_lines = []
    for line in lines:
        line = line.strip()
        
        try:
            encoded_line = base64.b64encode(line.encode('utf-8')).decode('utf-8')
            full_line = "ssr://" + encoded_line  # Add ssr:// prefix
            encoded_lines.append(full_line)
        except Exception as e:
            print(f"Error encoding line: {e}")
            encoded_lines.append(f"Error encoding line: {line}")

    with open(output_file, 'w') as f:
        f.write('\n'.join(encoded_lines))

if __name__ == "__main__":
    input_file_path = "ssr3.txt"  # Replace with your input file path (output of previous code)
    output_file_path = "Ssr.txt"  # Replace with desired output file path

    encode_and_fix_base64(input_file_path, output_file_path)
    print("Encoding and saving complete.")
