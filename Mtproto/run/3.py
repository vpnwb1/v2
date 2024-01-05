import requests

# URL of the JSON data
url = "https://raw.githubusercontent.com/hookzof/socks5_list/master/tg/mtproto.json"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Parse the JSON data

    with open("Mtproto/temp/3.txt", "w") as file:
        # Iterate through each entry in the data
        for entry in data:
            server = entry["host"]
            port = entry["port"]
            secret = entry["secret"]
            link = f"https://t.me/proxy?server={server}&port={port}&secret={secret}"
            file.write(link + "\n")
else:
    print("Failed to retrieve data from the URL.")