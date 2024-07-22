import requests
from obtiene_id_telegram import obtener_id
import os


def chat_id():
    directorio_script = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo = os.path.join(directorio_script, 'chat_id.txt')
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'r') as file:
            f = file.read().strip()
            return f
        
    else:
        obtener_id()
        return chat_id()


def send_telegram_message(message):
    chat_id_value = chat_id()
    bot_token = os.getenv('TELEGRAM_BOT_TOKEN')

    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    payload = {'chat_id': chat_id_value, 'text': message}
    response = requests.post(url, data=payload)
    response.raise_for_status()
    print(f'id: {chat_id_value}, mensaje: {message}')


send_telegram_message('saludos!')
