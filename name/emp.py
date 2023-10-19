with open('Hy2d.txt', 'r') as file1:
    lines = file1.readlines()

non_empty_lines = [line.strip() for line in lines if line.strip()]

with open('Hy2L.txt', 'w') as file2:
    file2.write('\n'.join(non_empty_lines))
##
with open('Ssd.txt', 'r') as file1:
    lines = file1.readlines()

non_empty_lines = [line.strip() for line in lines if line.strip()]

with open('SsL.txt', 'w') as file2:
    file2.write('\n'.join(non_empty_lines))
##
with open('Ssrd.txt', 'r') as file1:
    lines = file1.readlines()

non_empty_lines = [line.strip() for line in lines if line.strip()]

with open('SsrL.txt', 'w') as file2:
    file2.write('\n'.join(non_empty_lines))
##
with open('Trojand.txt', 'r') as file1:
    lines = file1.readlines()

non_empty_lines = [line.strip() for line in lines if line.strip()]

with open('TrojanL.txt', 'w') as file2:
    file2.write('\n'.join(non_empty_lines))
##
with open('Tuicd.txt', 'r') as file1:
    lines = file1.readlines()

non_empty_lines = [line.strip() for line in lines if line.strip()]

with open('TuicL.txt', 'w') as file2:
    file2.write('\n'.join(non_empty_lines))
##
with open('Vlessd.txt', 'r') as file1:
    lines = file1.readlines()

non_empty_lines = [line.strip() for line in lines if line.strip()]

with open('VlessL.txt', 'w') as file2:
    file2.write('\n'.join(non_empty_lines))
##
with open('Vmessd.txt', 'r') as file1:
    lines = file1.readlines()

non_empty_lines = [line.strip() for line in lines if line.strip()]

with open('VmessL.txt', 'w') as file2:
    file2.write('\n'.join(non_empty_lines))
##
