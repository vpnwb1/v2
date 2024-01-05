import requests
import json

# URL of the JSON proxy list
url = "https://raw.githubusercontent.com/hookzof/socks5_list/master/tg/socks.json"

# Get the JSON content of the proxy list
response = requests.get(url)
proxy_data = response.json()

# Extract proxies and save in the specified formats
with open("Socks/temp/raw2.txt", "w") as file1, open("Socks/temp/socks2.txt", "w") as file2:
    for proxy_info in proxy_data:
        ip = proxy_info["ip"]
        port = proxy_info["port"]

        # Format for file 1
        file1.write(f"{ip}:{port}\n")

        # Format for file 2
        socks_proxy = f"tg://socks?server={ip}&port={port}"
        file2.write(f"{socks_proxy}\n")