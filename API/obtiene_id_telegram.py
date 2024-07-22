import os
import requests


def obtener_id():
    bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    response = requests.get(
        f'https://api.telegram.org/bot{bot_token}/getUpdates')
    directorio_script = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo = os.path.join(directorio_script, 'chat_id.txt')
    data = response.json()
    if not data['result']:
        raise ValueError(
            "No se encontraron actualizaciones recientes. Asegúrate de haber enviado un mensaje al bot.")
    chat_id = data['result'][-1]['message']['chat']['id']
    with open(ruta_archivo, 'w') as file:
        file.write(str(chat_id))

obtener_id()