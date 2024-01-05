import os
import requests
import base64

def decode_base64_from_url(url, output_file):
    response = requests.get(url)
    encoded_data = response.content

    missing_padding = 4 - (len(encoded_data) % 4)
    if missing_padding != 4:
        encoded_data += b'=' * missing_padding

    decoded_data = base64.b64decode(encoded_data)

    if not os.path.exists('V2/temp'):
        os.makedirs('V2/temp')

    output_path = os.path.join('V2/temp', output_file)
    with open(output_path, 'wb') as f:
        f.write(decoded_data)

# Example usage
input_file = 'V2/from64/sites.txt'
with open(input_file, 'r') as f:
    urls = f.read().splitlines()

for i, url in enumerate(urls):
    output_file = f'f64{i}.txt'
    decode_base64_from_url(url, output_file)