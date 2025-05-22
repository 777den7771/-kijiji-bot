from telegram import Bot
from config import TELEGRAM_TOKEN, CHAT_ID

try:
    bot = Bot(token=TELEGRAM_TOKEN)
except Exception as e:
    print(f"[Ошибка при создании Bot]: {e}")

def send_message(text):
    try:
        print("Отправка в Telegram...")
        bot.send_message(chat_id=CHAT_ID, text=text)
    except Exception as e:
        print(f"[Ошибка при отправке сообщения]: {e}")