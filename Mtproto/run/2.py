import requests
url = "https://raw.githubusercontent.com/soroushmirzaei/telegram-proxies-collector/main/proxies"

response = requests.get(url)
data = response.text.splitlines()

filtered_lines = [line for line in data if line.startswith("tg://proxy?") or line.startswith("tg://socks?")]

with open("Mtproto/temp/2.txt", "w") as file:
    for line in filtered_lines:
        file.write(line + "\n")