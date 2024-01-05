import os

files_to_remove = ['V2/ss.txt', 'V2/ssr.txt', 'V2/ssr1.txt', 'V2/ssr2.txt', 'V2/ssr3.txt', 'V2/vless.txt', 'V2/trojan.txt', 'V2/vmess.txt', 'V2/vmess1.txt', 'V2/vmess2.txt', 'V2/vmess3.txt', 'V2/vmess4.txt', 'V2/vmess5.txt', 'V2/vmess6.txt', 'V2/hy2.txt', 'V2/tuic.txt']

for file in files_to_remove:
    if os.path.exists(file):
        os.remove(file)
    else:
        print(f"File '{file}' does not exist, skipping removal.")
