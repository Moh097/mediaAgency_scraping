from selenium import webdriver
from bs4 import BeautifulSoup
import time

def extract(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    # Allow time for the page to load
    time.sleep(3)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    # Extracting article content
    content = ''
    paragraphs = soup.find_all('p', {'class': 'body-1 paragraph'})
    for p in paragraphs:
        content += p.get_text(strip=True) + "\n"

    # Extracting author information
    author = soup.find('span', {'class': 'avatar_name'})
    author_name = author.get_text(strip=True) if author else "Unknown"

    # Extracting publication date
    time_element = soup.find('time')
    publication_date = time_element.get('datetime') if time_element else "Unknown"

    return {
        'content': content,
        'author': author_name,
        'publication_date': publication_date
    }
