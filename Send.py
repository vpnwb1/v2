import os
import requests
import json
import random

BOT_TOKEN = os.environ['BOT_TOKEN']
BASE_URL = f'https://api.telegram.org/bot{BOT_TOKEN}/'

CHAT_ID_4 = os.environ['CHAT_ID_4']

file_path = 'SsL.txt'

with open(file_path, 'rb') as file:
    document_payload = {
        'chat_id': CHAT_ID_4,
        'document': file.read(),  # Read the file contents
    }

response = requests.post(BASE_URL + 'sendDocument', data=document_payload)

if response.status_code == 200:
    print('File sent successfully to the channel!')
else:
    print('Failed to send the file to the channel.')
    print(f'Response status code: {response.status_code}')
    print(response.text)
