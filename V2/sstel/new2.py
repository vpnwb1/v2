import asyncio
import qrcode
from telegram import Bot, InputMediaPhoto
import os
from datetime import datetime
import pytz

async def generate_qr_code(text, output_path='ss.png'):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    img.save(output_path)

    return output_path

async def edit_message_with_qr_code():
    bot_token = os.environ.get('BOT_TOKEN')  
    chat_id_secret = os.environ.get('CHAT_ID_1')
    message_id_secret = os.environ.get('MESSAGE_SS')  

    bot = Bot(token=bot_token)

    # Convert chat_id and message_id to integers
    chat_id = int(chat_id_secret)
    message_id = int(message_id_secret)

    with open('sstel/tel.txt', 'r') as file:
        text_to_encode = file.read()

    # Enclose the caption in backticks and append @vpnwb
    caption = f'`{text_to_encode}` \n\n @vpnwb 🔑'

    # Add time to the caption
    tehran_timezone = pytz.timezone('Asia/Tehran')
    current_time = datetime.now(tehran_timezone).strftime("%H:%M:%S")
    caption_with_time = f'{caption}\n\nآخرین آپدیت: {current_time}'

    qr_code_path = await generate_qr_code(text_to_encode)

    with open(qr_code_path, 'rb') as qr_file:
        await bot.edit_message_media(
            chat_id=chat_id,
            message_id=message_id,
            media=InputMediaPhoto(
                media=qr_file,
                caption=caption_with_time,
                parse_mode='Markdown',
            )
        )

asyncio.run(edit_message_with_qr_code())
