import asyncio
import qrcode
from telegram import Bot, InputMediaPhoto
import os

async def generate_qr_code(text, output_path='tro.png'):
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
    message_id_secret = os.environ.get('MESSAGE_TRO')  

    bot = Bot(token=bot_token)

    # Convert chat_id and message_id to integers
    chat_id = int(chat_id_secret)
    message_id = int(message_id_secret)

    with open('tel.txt', 'r') as file:
        text_to_encode = file.read()

    qr_code_path = await generate_qr_code(text_to_encode)

    with open(qr_code_path, 'rb') as qr_file:
        await bot.edit_message_media(
            chat_id=chat_id,
            message_id=message_id,
            media=InputMediaPhoto(
                media=qr_file,
                caption=text_to_encode,
            )
        )

asyncio.run(edit_message_with_qr_code())