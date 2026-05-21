import requests
from bs4 import BeautifulSoup

# Отправляем GET-запрос
response = requests.get('https://quotes.toscrape.com/')
soup = BeautifulSoup(response.text, 'html.parser')

# Извлекаем первую цитату и автора
quote = soup.find('span', class_='text').text
author = soup.find('small', class_='author').text

# Выводим результат
print(f'Цитата: {quote}')
print(f'Автор: {author}')
