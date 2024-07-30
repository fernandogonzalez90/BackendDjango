import requests
import os


class TelegramBot:
    def __init__(self):
        self.bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
        self.ruta_archivo = './chat_id.txt'

    def obtener_id(self):
        response = requests.get(
            f'https://api.telegram.org/bot{self.bot_token}/getUpdates'
        )
        data = response.json()
        print(data)
        if not data['result']:
            raise ValueError(
                "No se encontraron actualizaciones recientes. Asegúrate de haber enviado un mensaje al bot."
            )
        chat_id = data['result'][-1]['message']['chat']['id']
        with open(self.ruta_archivo, 'w') as file:
            file.write(str(chat_id))

    def chat_id(self):
        if os.path.exists(self.ruta_archivo):
            with open(self.ruta_archivo, 'r') as file:
                return file.read().strip()
        else:
            self.obtener_id()
            return self.chat_id()

    def send_message(self, message):
        chat_id = self.chat_id()
        url = f'https://api.telegram.org/bot{self.bot_token}/sendMessage'
        payload = {'chat_id': chat_id, 'text': message}
        response = requests.post(url, data=payload)
        response.raise_for_status()
        print(f'id: {chat_id}, mensaje: {message}')


if __name__ == '__main__':
    bot = TelegramBot()
    bot.send_message("Hola desde el bot de Telegram!")
