import requests

url = "https://raw.githubusercontent.com/yebekhe/MTProtoCollector/main/proxy/mtproto.json"

response = requests.get(url)
data = response.json()

filtered_items = [item['link'] for item in data if 'link' in item and item['link'].startswith("https://t.me/")]

with open("Mtproto/temp/1.txt", "w") as file:
    for item in filtered_items:
        file.write(item + "\n")