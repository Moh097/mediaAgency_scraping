import sqlite3
import os

# Database connection function with the specified path to the database
def get_connection():
    db_path = os.path.join(os.path.dirname(__file__), 'database.db')
    return sqlite3.connect(db_path)

# Function to create the articles table if it does not exist
def create_articles_table():
    print("Creating articles table if it does not exist...")  # Debug line
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            url TEXT,
            snippet TEXT,
            media_agency TEXT,
            content TEXT,
            author TEXT,
            publication_date DATE
        )
    ''')
    conn.commit()
    conn.close()

# Function to save an article
def save_article(article_data):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO articles (title, url, snippet, media_agency, content, author, publication_date)
        VALUES (:title, :url, :snippet, :media_agency, :content, :author, :publication_date)
    ''', article_data)
    conn.commit()
    conn.close()
