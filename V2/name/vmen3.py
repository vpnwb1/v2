# Define the input and output file paths
input_file_path = 'V2/vmess2.txt'
output_file_path = 'V2/vmess3.txt'

# Function to remove specified HTML tags from a string
def remove_html_tags(text):
    tags_to_remove = ['</code>', '<br/>', '<br>', '<code>', '<code/>']
    for tag in tags_to_remove:
        text = text.replace(tag, '')
    return text

# Read the contents of the input file
with open(input_file_path, 'r') as input_file:
    file_contents = input_file.read()

# Remove the specified HTML tags from the file contents
cleaned_contents = remove_html_tags(file_contents)

# Write the cleaned contents to the output file
with open(output_file_path, 'w') as output_file:
    output_file.write(cleaned_contents)

