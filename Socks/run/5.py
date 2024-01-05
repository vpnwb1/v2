file_names = ["Socks/temp/socks1.txt", "Socks/temp/socks2.txt", "Socks/temp/socks3.txt"]
output_file = "Socks/socksv5.txt"
with open(output_file, "w") as outfile:

    for file_name in file_names:
        
        with open(file_name, "r") as infile:
            
            contents = infile.read()
            
            outfile.write(contents)
            
        outfile.write("\n")
