import os
import asyncio
from datetime import datetime
import pytz
from telegram import Bot

async def edit_message():
    bot_token = os.getenv('BOT_TOKEN')
    if bot_token is None:
        raise ValueError("Telegram bot token not found in environment variables.")

    bot = Bot(token=bot_token)

    chat_id = os.getenv('CHAT_ID_1')
    if chat_id is None:
        raise ValueError("Telegram channel ID not found in environment variables.")

    message_id = 6085

    with open('urls.txt', 'r') as file:
        new_text = file.read()

    tehran_timezone = pytz.timezone('Asia/Tehran')
    current_time = datetime.now(tehran_timezone).strftime("%H:%M")

    new_text_with_time = f"{new_text}\n\nآخرین آپدیت : {current_time}"

    await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=new_text_with_time, parse_mode='Markdown')

asyncio.run(edit_message())
