import requests
from bs4 import BeautifulSoup

def get_kijiji_ads(url):
    print(f"Запрос: {url}")
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        ads = []
        for ad in soup.select('.search-item'):
            title_tag = ad.select_one('.title')
            if not title_tag:
                continue
            title = title_tag.get_text(strip=True)
            link_tag = ad.select_one('a.title')
            if link_tag and 'href' in link_tag.attrs:
                full_url = 'https://www.kijiji.ca' + link_tag['href']
                ads.append((title, full_url))

        return ads
    except Exception as e:
        print(f"[Ошибка парсинга]: {e}")
        return []