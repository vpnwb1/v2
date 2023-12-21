import os
import requests
import json

BOT_TOKEN = os.environ['BOT_TOKEN']
BASE_URL = f'https://api.telegram.org/bot{BOT_TOKEN}/'

CHAT_ID_4 = os.environ['CHAT_ID_4']

file_paths = ['SsL.txt', 'SsrL.txt', 'VmessL.txt']  # List of file paths to send

for file_path in file_paths:
    with open(file_path, 'rb') as file:
        document_payload = {
            'chat_id': CHAT_ID_4,
        }

        files = {
            'document': file,
        }

        response = requests.post(BASE_URL + 'sendDocument', data=document_payload, files=files)

    if response.status_code == 200:
        print(f'File "{file_path}" sent successfully to the channel!')
    else:
        print(f'Failed to send the file "{file_path}" to the channel.')
        print(f'Response status code: {response.status_code}')
        print(response.text)
