import os

files_to_remove = ['tuic.txt', 'hy2.txt', 'Ss.txt', 'Ssr.txt', 'Vmess.txt', 'Vless.txt', 'Trojan.txt', 'Tuic.txt', 'Hy2.txt', 'Tuicd.txt', 'Hy2d.txt', 'Ssd.txt', 'Ssrd.txt', 'TrojanD.txt', 'Vmessd.txt', 'Vlessd.txt']

for file in files_to_remove:
    if os.path.exists(file):
        os.remove(file)
    else:
        print(f"File '{file}' does not exist, skipping removal.")
