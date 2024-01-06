import os

files_to_remove = ['V2/fromtele/merged.txt', 'V2/fromtele/mergedclean.txt', 'V2/fromtele/juicity.txt', 'V2/fromtele/ss.txt', 'V2/fromtele/ssr.txt', 'V2/fromtele/vmess.txt', 'V2/fromtele/vless.txt', 'V2/fromtele/trojan.txt', 'V2/fromtele/tuic.txt', 'V2/fromtele/hy2.txt', 'V2/fromtele/hysteria.txt', 'V2/merged.txt', 'V2/merged_file.txt', 'V2/hysteria.txt', 'V2/Hysteria.txt', 'V2/hysteriaL.txt' ]

for file in files_to_remove:
    if os.path.exists(file):
        os.remove(file)
    else:
        print(f"File '{file}' does not exist, skipping removal.")
