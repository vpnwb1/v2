import os

files_to_remove = ['tuic.txt', 'hy2.txt', 'Ss.txt', 'Ssr.txt', 'Vmess.txt', 'Vless.txt', 'Trojan.txt']

for file in files_to_remove:
    if os.path.exists(file):
        os.remove(file)
    else:
        print(f"File '{file}' does not exist, skipping removal.")
