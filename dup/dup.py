import hashlib

input_file_path = "Ss.txt"
output_file_path = "SsL.txt"

completed_lines_hash = set()

input_file = open(input_file_path, "r")
output_file = open(output_file_path, "w")

for line in input_file:
  hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
  if hashValue not in completed_lines_hash:
    output_file.write(line)
    completed_lines_hash.add(hashValue)
output_file.close()
input_file.close()

####

import hashlib

input_file_path = "Ssr.txt"
output_file_path = "SsrL.txt"

completed_lines_hash = set()

input_file = open(input_file_path, "r")
output_file = open(output_file_path, "w")

for line in input_file:
  hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
  if hashValue not in completed_lines_hash:
    output_file.write(line)
    completed_lines_hash.add(hashValue)
output_file.close()
input_file.close()

####

import hashlib

input_file_path = "Trojan.txt"
output_file_path = "TrojanL.txt"

completed_lines_hash = set()

input_file = open(input_file_path, "r")
output_file = open(output_file_path, "w")

for line in input_file:
  hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
  if hashValue not in completed_lines_hash:
    output_file.write(line)
    completed_lines_hash.add(hashValue)
output_file.close()
input_file.close()

####

import hashlib

input_file_path = "Vmess.txt"
output_file_path = "VmessL.txt"

completed_lines_hash = set()

input_file = open(input_file_path, "r")
output_file = open(output_file_path, "w")

for line in input_file:
  hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
  if hashValue not in completed_lines_hash:
    output_file.write(line)
    completed_lines_hash.add(hashValue)
output_file.close()
input_file.close()

####

import hashlib

input_file_path = "Vless.txt"
output_file_path = "VlessL.txt"

completed_lines_hash = set()

input_file = open(input_file_path, "r")
output_file = open(output_file_path, "w")

for line in input_file:
  hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
  if hashValue not in completed_lines_hash:
    output_file.write(line)
    completed_lines_hash.add(hashValue)
output_file.close()
input_file.close()

####








import hashlib

input_file_path = "hy2.txt"
output_file_path = "Hy2L.txt"

completed_lines_hash = set()

input_file = open(input_file_path, "r")
output_file = open(output_file_path, "w")

for line in input_file:
  hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
  if hashValue not in completed_lines_hash:
    output_file.write(line)
    completed_lines_hash.add(hashValue)
output_file.close()
input_file.close()

####







import hashlib

input_file_path = "tuic.txt"
output_file_path = "TuicL.txt"

completed_lines_hash = set()

input_file = open(input_file_path, "r")
output_file = open(output_file_path, "w")

for line in input_file:
  hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
  if hashValue not in completed_lines_hash:
    output_file.write(line)
    completed_lines_hash.add(hashValue)
output_file.close()
input_file.close()

####
