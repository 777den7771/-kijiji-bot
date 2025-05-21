import time
from config import KIJIJI_SEARCH_URL, CHECK_INTERVAL
from kijiji_parser import get_kijiji_ads
from telegram_bot import send_message

def load_sent_ads():
    try:
        with open('sent_ads.txt', 'r') as f:
            return set(f.read().splitlines())
    except FileNotFoundError:
        return set()

def save_sent_ad(url):
    with open('sent_ads.txt', 'a') as f:
        f.write(url + '\n')

def main():
    print("Бот запущен.")
    sent_ads = load_sent_ads()

    while True:
        try:
            ads = get_kijiji_ads(KIJIJI_SEARCH_URL)
            for title, url in ads:
                if url not in sent_ads:
                    message = f"🔔 Новое объявление:\n{title}\n{url}"
                    send_message(message)
                    save_sent_ad(url)
                    sent_ads.add(url)
            time.sleep(CHECK_INTERVAL)
        except Exception as e:
            print(f"Ошибка: {e}")
            time.sleep(60)

if __name__ == '__main__':
    main()