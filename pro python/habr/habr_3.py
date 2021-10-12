import requests
from bs4 import BeautifulSoup

KEYWORDS = ['дизайн', 'фото', 'web', 'python']
satisfying_articles = []

response = requests.get('https://habr.com/ru/all/')
response.raise_for_status()
soup = BeautifulSoup(response.text, features='html.parser')
articles = soup.find_all('article')

for article in articles:
    href = article.find(class_='tm-article-snippet__title-link').attrs['href']
    link = 'https://habr.com' + href
    response_article = requests.get(link)
    response_article.raise_for_status()
    soup_article = BeautifulSoup(response_article.text, features='html.parser')
    hub = soup_article.find(id='post-content-body')
    
    if hub == None:
        continue  
    else:
        hub = soup_article.find(id='post-content-body').text
    
    if any(keyword in hub for keyword in KEYWORDS):
        date = article.find('time').get('title')
        title = article.find('h2').text
        href = article.find(class_='tm-article-snippet__title-link').attrs['href']
        link = 'https://habr.com' + href
        satisfying_articles.append(f"{date} - {title} - {link}")

for article in satisfying_articles:
    print(article)