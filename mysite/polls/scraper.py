import requests
from bs4 import BeautifulSoup

def scrape_nasa():
    url = 'https://www.nasa.gov/topics/solarsystem/index.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    articles = soup.find_all('div', class_='list_of_items')
    
    news_list = []
    for article in articles:
        title = article.find('a').text.strip()
        link = 'https://www.nasa.gov' + article.find('a')['href']
        summary = article.find('p').text.strip()
        news_list.append({'title': title, 'summary': summary, 'link': link})
    
    return news_list

def scrape_astrophysical_journal_letters():
    url = 'https://iopscience.iop.org/journal/2041-8205'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    articles = soup.find_all('ol', class_='content-items')
    
    news_list = []
    for article in articles:
        title = article.find('a', class_='highwire-cite-linked-title').text.strip()
        link = 'https://iopscience.iop.org' + article.find('a', class_='highwire-cite-linked-title')['href']
        summary = article.find('div', class_='highwire-article-citation').find('p').text.strip()
        news_list.append({'title': title, 'summary': summary, 'link': link})
    
    return news_list

# Ejemplo de uso:
if __name__ == '__main__':
    nasa_news = scrape_nasa()
    print('Noticias de NASA:')
    for news in nasa_news:
        print(news)
    
    print('\n')
    
    astrophysical_journal_news = scrape_astrophysical_journal_letters()
    print('Noticias de The Astrophysical Journal Letters:')
    for news in astrophysical_journal_news:
        print(news)
