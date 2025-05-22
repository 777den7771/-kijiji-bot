from telegram import Bot
from config import TELEGRAM_TOKEN, CHAT_ID

bot = Bot(token=TELEGRAM_TOKEN)

def send_message(text):
    try:
        print(f"Отправляю сообщение в Telegram...")
        bot.send_message(chat_id=CHAT_ID, text=text)
    except Exception as e:
        print(f"Ошибка при отправке сообщения: {e}")