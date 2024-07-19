import asyncio
from telegram import Bot
from obtiene_id_telegram import obtener_id

message = "probando bot"


async def send_telegram_message(message):
    bot_token = '6764761192:AAEbqx6i77597a6gEEDRGZbqJCBWX4mZ0fA'
    chat_id = obtener_id()
    print(type(chat_id), chat_id)
    bot = Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text=message)
    print(f'id: {chat_id}, mensaje: {message}')


async def main():
    await send_telegram_message(message)

if __name__ == "__main__":
    asyncio.run(main())