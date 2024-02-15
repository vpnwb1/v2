import requests

with open("V2/fromsite/sites.txt") as f:
    sites = f.read().splitlines()

with open("V2/temp/fromsite.txt", "w") as f:
    for site in sites:
        try:
            html = requests.get(site).content.decode("utf-8")
            lines = html.split("\n")
            servers = [line for line in lines if line.startswith("ss://") or line.startswith("ssr://") or line.startswith("vmess://") or line.startswith("vless://") or line.startswith("trojan://") or line.startswith("hy2://") or line.startswith("tuic://")]

            for server in servers:
                f.write(server + "\n")
        except Exception as e:
            print(f"An error occurred while fetching content from {site}: {e}")
            continue  # Skip to the next site if there's an error
