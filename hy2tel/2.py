import os
import requests
import json
import random

BOT_TOKEN = os.environ['BOT_TOKEN']
BASE_URL = f'https://api.telegram.org/bot{BOT_TOKEN}/'

CHAT_ID_1 = os.environ['CHAT_ID_1']
CHAT_ID_2 = os.environ['CHAT_ID_2']

with open('hy2tel/tel.txt', 'r') as file:
    urls = [line.strip() for line in file]

if len(urls) < 1:
    print('Error: The text file must contain at least 1 URL.')
    exit()

# Use all available URLs if there are less than 5
num_urls_to_send = min(5, len(urls))
random_urls = random.sample(urls, num_urls_to_send)

# Format each URL in monospaced type
formatted_urls = [f'`{url}`' for url in random_urls]

message_text = 'Hysteria2 | هیستریا  \n\n{}\n@UncensorX '.format('\n'.join(formatted_urls))

message_payload = {
    'text': message_text,
    'parse_mode': 'Markdown',
}

message_payload['chat_id'] = CHAT_ID_1
response1 = requests.post(BASE_URL + 'sendMessage', json=message_payload)

message_payload['chat_id'] = CHAT_ID_2
response2 = requests.post(BASE_URL + 'sendMessage', json=message_payload)

if response1.status_code == 200 and response2.status_code == 200:
    print('Messages sent successfully to both channels!')
else:
    print('Failed to send messages to one or both channels.')
    print(f'Channel 1 response: {response1.status_code}')
    print(f'Channel 2 response: {response2.status_code}')
    print(response1.text)
    print(response2.text)
