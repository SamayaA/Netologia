import requests
from bs4 import BeautifulSoup

KEYWORDS = ['дизайн', 'фото', 'web', 'python']
satisfying_articles = []

response = requests.get('https://habr.com/ru/all/')
response.raise_for_status()

soup = BeautifulSoup(response.text, features='html.parser')
articles = soup.find_all('article')
for article in articles:
    hub = article.find(class_='article-formatted-body article-formatted-body_version-2')
    if hub==None:
        continue
    else:
        hub = article.find(class_='article-formatted-body article-formatted-body_version-2').text

    if any(keyword in hub for keyword in KEYWORDS):
        date = article.find('time').get('title')
        title = article.find('h2').text
        href = article.find(class_='tm-article-snippet__title-link').attrs['href']
        link = 'https://habr.com' + href
        satisfying_articles.append(f"{date} - {title} - {link}")

for article in satisfying_articles:
    print(article)