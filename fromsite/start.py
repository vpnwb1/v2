import requests

with open("fromsite/sites.txt") as f:
    sites = f.read().splitlines()

with open("ready/fromsite.txt", "w") as f:  # Open file in append mode
    for site in sites:
        html = requests.get(site).content.decode("utf-8")
        lines = html.split("\n")
        servers = [line for line in lines if line.startswith("ss://") or line.startswith("ssr://") or line.startswith("vmess://") or line.startswith("vless://") or line.startswith("trojan://") or line.startswith("hy2://") or line.startswith("tuic://")]

        for server in servers:
            f.write(server + "\n")