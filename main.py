from scrapers.scraper import process_articles
from database.models import create_articles_table
from search.google_search import GoogleSearch
import sqlite3
import csv
import os

def export_articles_to_csv(db_path='./database/database.db', csv_path='./csv/articles.csv'):
    # Ensure CSV directory exists
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)

    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Query all entries in the articles table
    cursor.execute('SELECT * FROM articles')
    rows = cursor.fetchall()
    
    # Get column names
    column_names = [description[0] for description in cursor.description]
    
    # Write rows to CSV file
    with open(csv_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(column_names)  # Write header
        writer.writerows(rows)         # Write data
    
    # Close the connection
    conn.close()
    print(f"Data exported to {csv_path}")

def main():
    # Create articles table if it doesn't exist
    create_articles_table()
    
    # Initialize the GoogleSearch engine and set up search parameters
    google_search = GoogleSearch()
    query_base = "Your Query here"  
    
    # Retrieve articles from Google Search API without date ranges
    results = google_search.get_search_results(query_base)
    
    # Process and save the list of articles
    process_articles(results)
    
    # Export saved articles to a CSV file
    export_articles_to_csv()

if __name__ == "__main__":
    main()

