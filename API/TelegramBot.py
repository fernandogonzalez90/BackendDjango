from telegram import Bot
from .obtiene_id_telegram import obtener_id


def send_telegram_message(message):
    bot_token = '6764761192:AAEbqx6i77597a6gEEDRGZbqJCBWX4mZ0fA'
    chat_id = obtener_id()
    bot = Bot(token=bot_token)
    bot.send_message(chat_id=chat_id, text=message)