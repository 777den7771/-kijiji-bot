import requests
from bs4 import BeautifulSoup

class KijijiScraper:
    def scrape(self, url):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
            }
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            items = []
            for listing in soup.select('div.search-item'):
                title = listing.select_one('a.title').text.strip()
                price = listing.select_one('div.price').text.strip()
                location = listing.select_one('div.location').text.strip()
                url = "https://www.kijiji.ca" + listing.select_one('a.title')['href']
                
                items.append({
                    'title': title,
                    'price': price,
                    'location': location,
                    'url': url
                })
            return items
        except Exception as e:
            print(f"Ошибка парсинга: {e}")
            return []
