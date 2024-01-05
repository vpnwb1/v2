import requests

# List of URLs to fetch proxy data from
urls = [
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt",
    "https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/socks5_proxies.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt",
    "https://www.proxy-list.download/api/v1/get/?type=socks5",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks5.txt",
    "https://api.proxylist.to/socks5?key=PROXY-6A6D110A-LIST-14A498E1-TO",
    "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
]

# Container for all proxy data
all_proxy_data = []

# Iterate through each URL
for url in urls:
    response = requests.get(url)
    if response.status_code == 200:
        proxy_data = response.json() if url.endswith(".json") else response.text.split("\n")
        all_proxy_data.extend(proxy_data)
    else:
        print(f"Failed to fetch data from {url}")

# Save all proxy data in socks5.txt
with open("Socks/temp/raw3.txt", "w") as file:
    for proxy_info in all_proxy_data:
        file.write(f"{proxy_info}\n")