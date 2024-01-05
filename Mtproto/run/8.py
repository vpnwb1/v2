import hashlib

input_file_path = "Mtproto/temp/7.txt"
output_file_path = "Mtproto/mtproto.txt"

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