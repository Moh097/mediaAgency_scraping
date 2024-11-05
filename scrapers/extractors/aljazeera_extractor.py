import requests
from bs4 import BeautifulSoup

def extract(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract author
    author = 'Unknown'
    author_info = soup.find('div', class_='article-author__info')
    if author_info:
        author_name = author_info.find('div', class_='article-author__name')
        if author_name:
            author_link = author_name.find('a', class_='author-link')
            if author_link:
                author = author_link.get_text(strip=True)

    # Extract publication date
    date_div = soup.find('span', class_='article-dates__published')
    publication_date = date_div.get_text(strip=True) if date_div else 'Unknown'

    # Extract content
    content_div = soup.find('div', class_='wysiwyg--all-content')
    if not content_div:
        return {'content': '', 'author': author, 'publication_date': publication_date}

    # Remove ads and other non-content elements
    for ad in content_div.find_all(class_='container--ads'):
        ad.decompose()
    for ad in content_div.find_all(class_='jetpack-video-wrapper'):
        ad.decompose()

    # Extract text content
    paragraphs = [p.get_text(strip=True) for p in content_div.find_all('p')]
    content = '\n'.join(paragraphs)

    return {'content': content, 'author': author, 'publication_date': publication_date}
