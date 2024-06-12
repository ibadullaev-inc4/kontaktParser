import requests
from bs4 import BeautifulSoup

url = 'https://kontakt.az/iqlim-texnikasi/kondisionerler'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    products = soup.find_all('div', class_="prodItem product-item")
    for product in products:
        product_info = {
            'product_id': product.get('id'),
            'product_title': product.find('div', class_="prodItem__title").text,
            'product_price': product.find('div', class_="prodItem__prices prodItem__prices--active").text.strip().replace('\xa0₼', ' ').replace('\n', ''),
        }

        print(product_info)