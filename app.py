from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
from config import TOKEN, ADMIN_ID
from scraper import KijijiScraper

# Настройка логов
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

scraper = KijijiScraper()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет! Отправь мне ссылку на поиск Kijiji")

@dp.message_handler()
async def handle_url(message: types.Message):
    url = message.text
    if "kijiji.ca" not in url:
        return await message.answer("Некорректная ссылка Kijiji")
    
    await message.answer("Начинаю мониторинг...")
    results = scraper.scrape(url)
    
    if not results:
        return await message.answer("Объявления не найдены")
    
    for item in results[:3]:  # Отправляем первые 3
        await message.answer(
            f"🏠 {item['title']}\n"
            f"💰 {item['price']}\n"
            f"📍 {item['location']}\n"
            f"🔗 {item['url']}"
        )

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp)
