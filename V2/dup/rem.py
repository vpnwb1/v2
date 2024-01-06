import os

files_to_remove = ['V2/tuic.txt', 'V2/hy2.txt', 'V2/Ss.txt', 'V2/Ssr.txt', 'V2/Vmess.txt', 'V2/Vless.txt', 'V2/Trojan.txt', 'V2/Tuic.txt', 'V2/Hy2.txt', 'V2/Tuicd.txt', 'V2/Hy2d.txt', 'V2/Ssd.txt', 'V2/Ssrd.txt', 'V2/Trojand.txt', 'V2/Vmessd.txt', 'V2/Vlessd.txt', 'V2/juicity.txt', 'V2/hysteria.txt', 'V2/Hysteria.txt', 'V2/ws.txt']

for file in files_to_remove:
    if os.path.exists(file):
        os.remove(file)
    else:
        print(f"File '{file}' does not exist, skipping removal.")
