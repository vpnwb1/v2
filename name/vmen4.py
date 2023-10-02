import base64
import json

# Open the input file for reading
with open("vmess3.txt", "r", encoding="utf-8") as input_file:
    # Open the output file for writing
    with open("vmess4.txt", "w", encoding="utf-8") as output_file:
        # Iterate over each line in the input file
        for line in input_file:
            try:
                # Decode the line as base64
                decoded_line = base64.b64decode(line.encode("utf-8")).decode("utf-8")

                # Assuming decoded_data is a JSON string, load it as a dictionary
                vmess_data = json.loads(decoded_line)

                # Serialize the dictionary to a single line JSON string and write it to the output file
                output_line = json.dumps(vmess_data, separators=(",", ":"), ensure_ascii=False)
                output_file.write(output_line + "\n")
            except (base64.binascii.Error, UnicodeDecodeError, json.JSONDecodeError):
                # Skip lines that cannot be decoded as base64, contain non-UTF-8 characters, or are not valid JSON
                continue