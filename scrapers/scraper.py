from datetime import datetime
import re
from database.models import save_article  # Function to save an article in the database
from scrapers.extractors.router import get_extractor  # Router to fetch the right extractor for a URL

# Function to extract the date from the snippet
def extract_publication_date(snippet):
    date_match = re.search(r'\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{1,2}, \d{4}\b', snippet)
    if date_match:
        date_str = date_match.group()
        return datetime.strptime(date_str, "%b %d, %Y").date()
    return None

def scrape_article_data(article):
    url = article.get('link')
    title = article.get('title', 'Untitled')
    snippet = article.get('snippet', '')
    media_agency = article.get('displayLink', 'Unknown')
    
    # Extract publication date from snippet
    publication_date = extract_publication_date(snippet)
    
    # Retrieve the appropriate extractor for the URL
    extractor = get_extractor(url)
    if extractor:
        content_data = extractor(url)  # Each extractor should return a dictionary with 'content' and 'author'
        content = content_data.get('content', '')
        author = content_data.get('author', 'Unknown')
    else:
        print(f"No extractor found for {media_agency}. Skipping article.")
        return
    
    # Combine all data into a dictionary for database saving
    article_data = {
        'title': title,
        'url': url,
        'snippet': snippet,
        'media_agency': media_agency,
        'content': content,
        'author': author,
        'publication_date': publication_date
    }
    
    # Save to database
    save_article(article_data)
    print(f"Article saved: {title}")

# Main function to loop through articles and process each one
def process_articles(results):
    for article in results:
        scrape_article_data(article)
