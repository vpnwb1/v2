import os
import requests

url = "https://raw.githubusercontent.com/yebekhe/MTProtoCollector/main/proxy/mtproto.json"

response = requests.get(url)
data = response.json()

filtered_items = [item['link'] for item in data if 'link' in item and item['link'].startswith("https://t.me/")]

# Create the temporary directory if it doesn't exist
temp_directory = "Mtproto/temp"
if not os.path.exists(temp_directory):
    os.makedirs(temp_directory)

with open(os.path.join(temp_directory, "1.txt"), "w") as file:
    for item in filtered_items:
        file.write(item + "\n")