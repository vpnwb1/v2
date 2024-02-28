def remove_duplicates(file1_path, file2_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        lines_file1 = set(file1.read().splitlines())
        lines_file2 = set(file2.read().splitlines())
    
    unique_lines_file1 = lines_file1 - lines_file2
    
    with open(file1_path, 'w') as file1:
        file1.write('\n'.join(unique_lines_file1))

file1_path = 'SsL.txt'
file2_path = 'V2/sstel/db.txt'
remove_duplicates(file1_path, file2_path)

##

def remove_duplicates(file1_path, file2_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        lines_file1 = set(file1.read().splitlines())
        lines_file2 = set(file2.read().splitlines())
    
    unique_lines_file1 = lines_file1 - lines_file2
    
    with open(file1_path, 'w') as file1:
        file1.write('\n'.join(unique_lines_file1))

file1_path = 'SsrL.txt'
file2_path = 'V2/ssrtel/db.txt'
remove_duplicates(file1_path, file2_path)

##

def remove_duplicates(file1_path, file2_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        lines_file1 = set(file1.read().splitlines())
        lines_file2 = set(file2.read().splitlines())
    
    unique_lines_file1 = lines_file1 - lines_file2
    
    with open(file1_path, 'w') as file1:
        file1.write('\n'.join(unique_lines_file1))

file1_path = 'Hy2L.txt'
file2_path = 'V2/hy2tel/db.txt'
remove_duplicates(file1_path, file2_path)

##

def remove_duplicates(file1_path, file2_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        lines_file1 = set(file1.read().splitlines())
        lines_file2 = set(file2.read().splitlines())
    
    unique_lines_file1 = lines_file1 - lines_file2
    
    with open(file1_path, 'w') as file1:
        file1.write('\n'.join(unique_lines_file1))

file1_path = 'HysteriaL.txt'
file2_path = 'V2/hytel/db.txt'
remove_duplicates(file1_path, file2_path)

##

def remove_duplicates(file1_path, file2_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        lines_file1 = set(file1.read().splitlines())
        lines_file2 = set(file2.read().splitlines())
    
    unique_lines_file1 = lines_file1 - lines_file2
    
    with open(file1_path, 'w') as file1:
        file1.write('\n'.join(unique_lines_file1))

file1_path = 'TrojanL.txt'
file2_path = 'V2/trotel/db.txt'
remove_duplicates(file1_path, file2_path)

##

def remove_duplicates(file1_path, file2_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        lines_file1 = set(file1.read().splitlines())
        lines_file2 = set(file2.read().splitlines())
    
    unique_lines_file1 = lines_file1 - lines_file2
    
    with open(file1_path, 'w') as file1:
        file1.write('\n'.join(unique_lines_file1))

file1_path = 'TuicL.txt'
file2_path = 'V2/tuitel/db.txt'
remove_duplicates(file1_path, file2_path)

##

def remove_duplicates(file1_path, file2_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        lines_file1 = set(file1.read().splitlines())
        lines_file2 = set(file2.read().splitlines())
    
    unique_lines_file1 = lines_file1 - lines_file2
    
    with open(file1_path, 'w') as file1:
        file1.write('\n'.join(unique_lines_file1))

file1_path = 'VlessL.txt'
file2_path = 'V2/vletel/db.txt'
remove_duplicates(file1_path, file2_path)

##

def remove_duplicates(file1_path, file2_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        lines_file1 = set(file1.read().splitlines())
        lines_file2 = set(file2.read().splitlines())
    
    unique_lines_file1 = lines_file1 - lines_file2
    
    with open(file1_path, 'w') as file1:
        file1.write('\n'.join(unique_lines_file1))

file1_path = 'VmessL.txt'
file2_path = 'V2/vmetel/db.txt'
remove_duplicates(file1_path, file2_path)