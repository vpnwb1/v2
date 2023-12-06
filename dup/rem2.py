import os

files_to_remove = ['fromtele/merged.txt', 'fromtele/mergedclean.txt', 'fromtele/juicity.txt', 'fromtele/ss.txt', 'fromtele/ssr.txt', 'fromtele/vmess.txt', 'fromtele/vless.txt', 'fromtele/trojan.txt', 'fromtele/tuic.txt', 'fromtele/hy2.txt', 'fromtele/hysteria.txt', 'merged.txt', 'merged_file.txt', 'hysteria.txt', 'Hysteria.txt' ]

for file in files_to_remove:
    if os.path.exists(file):
        os.remove(file)
    else:
        print(f"File '{file}' does not exist, skipping removal.")
