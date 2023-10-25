import os

files_to_remove = ['ss.txt', 'ssr.txt', 'ssr1.txt', 'ssr2.txt', 'ssr3.txt', 'vless.txt', 'trojan.txt', 'vmess.txt', 'vmess1.txt', 'vmess2.txt', 'vmess3.txt', 'vmess4.txt', 'vmess5.txt', 'vmess6.txt', 'hy2.txt', 'tuic.txt']

for file in files_to_remove:
    if os.path.exists(file):
        os.remove(file)
    else:
        print(f"File '{file}' does not exist, skipping removal.")
