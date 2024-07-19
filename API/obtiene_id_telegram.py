import requests

def obtener_id():
    bot_token = '6764761192:AAEbqx6i77597a6gEEDRGZbqJCBWX4mZ0fA'
    response = requests.get(f'https://api.telegram.org/bot{bot_token}/getUpdates')
    data = response.json()
    if not data['result']:
        raise ValueError("No se encontraron actualizaciones recientes. Asegúrate de haber enviado un mensaje al bot.")
    chat_id = data['result'][-1]['message']['chat']['id']
    return chat_id

