import requests
from .obtiene_id_telegram import obtener_id


def send_telegram_message(message):
    bot_token = '6764761192:AAEbqx6i77597a6gEEDRGZbqJCBWX4mZ0fA'
    chat_id = obtener_id()
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    payload = {'chat_id': chat_id, 'text': message}
    response = requests.post(url, data=payload)
    response.raise_for_status()  # Lanzará una excepción si la respuesta tiene un error HTTP
    print(f'id: {chat_id}, mensaje: {message}')

