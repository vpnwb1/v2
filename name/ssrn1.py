# Open the file for reading
with open("ssr.txt", "r") as file:
    lines = file.readlines()

# Remove "ssr://" from the beginning of each line
cleaned_lines = [line.replace("ssr://", "", 1) for line in lines]

# Open a new file for writing and save the cleaned lines
with open("ssr1.txt", "w") as file:
    file.writelines(cleaned_lines)

print("Cleaning complete. Cleaned content saved in 'ssr1.txt'.")
