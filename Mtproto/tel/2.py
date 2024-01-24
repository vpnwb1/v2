import requests
import json
import random
import os


BOT_TOKEN = os.environ['BOT_TOKEN']
BASE_URL = f'https://api.telegram.org/bot{BOT_TOKEN}/'

CHAT_ID_1 = os.environ['CHAT_ID_1']


message_text = f'MtprotoProxy | پروکسی تلگرام\n\n@VpnWb🔑'

with open('Mtproto/names.txt', 'r') as file:
    names = [line.strip() for line in file]

if len(names) < 5:
    print('Error: The text file must contain at least 5 names.')
    exit()

random_names = random.sample(names, 5)

with open('Mtproto/urls.txt', 'r') as file:
    urls = [line.strip() for line in file]

if len(urls) < 5:
    print('Error: The text file must contain at least 5 URLs.')
    exit()

random_urls = random.sample(urls, 5)

buttons = [
    {'text': random_names[0], 'url': random_urls[0]},
    {'text': random_names[1], 'url': random_urls[1]},
    {'text': random_names[2], 'url': random_urls[2]},
    {'text': random_names[3], 'url': random_urls[3]},
    {'text': random_names[4], 'url': random_urls[4]}
]

keyboard = {
    'inline_keyboard': [
        [buttons[0], buttons[1], buttons[2]],
        [buttons[3], buttons[4]]
    ]
}

message_payload = {
    'text': message_text,
    'reply_markup': json.dumps(keyboard),
}

message_payload['chat_id'] = CHAT_ID_1
response1 = requests.post(BASE_URL + 'sendMessage', json=message_payload)


if response1.status_code == 200:
    print('Messages sent successfully to both channels!')
else:
    print('Failed to send messages to one or both channels.')
    print(f'Channel 1 response: {response1.status_code}')
    print(response1.text)
    