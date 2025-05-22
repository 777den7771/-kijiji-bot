print("Файл main.py загружен")

try:
    import time
    from config import KIJIJI_SEARCH_URLS, CHECK_INTERVAL
    from kijiji_parser import get_kijiji_ads
    from telegram_bot import send_message
except Exception as e:
    print(f"[Ошибка при импорте]: {e}")

def load_sent_ads():
    try:
        print("Загрузка списка отправленных объявлений...")
        with open('sent_ads.txt', 'r') as f:
            return set(f.read().splitlines())
    except FileNotFoundError:
        print("Файл sent_ads.txt не найден — создаю новый.")
        return set()
    except Exception as e:
        print(f"[Ошибка при загрузке sent_ads.txt]: {e}")
        return set()

def save_sent_ad(url):
    try:
        with open('sent_ads.txt', 'a') as f:
            f.write(url + '\n')
    except Exception as e:
        print(f"[Ошибка при сохранении URL]: {e}")

def main():
    print("main() запущен.")
    sent_ads = load_sent_ads()

    while True:
        try:
            for url in KIJIJI_SEARCH_URLS:
                print(f"Проверка: {url}")
                ads = get_kijiji_ads(url)
                print(f"Найдено {len(ads)} объявлений.")
                for title, ad_url in ads:
                    if ad_url not in sent_ads:
                        print(f"Новое объявление:\n{title}\n{ad_url}")
                        send_message(f"🔔 Новое объявление:\n{title}\n{ad_url}")
                        save_sent_ad(ad_url)
                        sent_ads.add(ad_url)
            print(f"Засыпаю на {CHECK_INTERVAL} сек...")
            time.sleep(CHECK_INTERVAL)
        except Exception as e:
            print(f"[Ошибка в цикле]: {e}")
            time.sleep(60)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"[Ошибка запуска main()]: {e}")