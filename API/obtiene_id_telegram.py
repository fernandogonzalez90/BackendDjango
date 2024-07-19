import requests


def obtener_id():
    bot_token = '6764761192:AAEbqx6i77597a6gEEDRGZbqJCBWX4mZ0fA'  # Reemplaza con el token de tu bot
    response = requests.get(f'https://api.telegram.org/bot{bot_token}/getUpdates')
    data = response.json()
    chat_id = data['result'][0]['message']['chat']['id']
    return chat_id
