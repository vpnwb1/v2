import requests
from bs4 import BeautifulSoup

def save_messages(channel_url, file_name):
    response = requests.get(channel_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        messages = soup.find_all('div', class_='tgme_widget_message_text')

        with open(file_name, 'w', encoding='utf-8') as file:
            # Write the HTML content of each message to the file
            for message in messages[-20:]:
                html_content = str(message)
                file.write(f"{html_content}\n")

        print(f"Messages from {channel_url} saved to '{file_name}'")
    else:
        print(f"Error: Unable to fetch the webpage for {channel_url}. Status code: {response.status_code}")

# Read usernames from user.txt
with open('fromtele/user.txt', 'r', encoding='utf-8') as user_file:
    usernames = user_file.read().splitlines()

# Loop through each username and save messages
for username in usernames:
    channel_url = f'https://t.me/s/{username}'
    file_name = f'fromtele/fetch/{username}_messages.txt'
    save_messages(channel_url, file_name)
