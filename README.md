Here’s a refined version of the `README.md` with clear steps and essential details:

---

### README.md

```markdown
# RAG Scraping

RAG Scraping is a Python-based web scraping tool that collects articles from specified websites based on a search query. It leverages the Google Custom Search API to locate relevant articles, extracts content details, and saves them into a SQLite database. The tool can also export scraped data to a CSV file for easy analysis.

## Features

- Retrieve articles using Google Custom Search API.
- Extract key details (title, author, content, and publication date) from selected sites (e.g., Al Jazeera, Al Arabiya).
- Save article data to a SQLite database.
- Export data to CSV for reporting or further analysis.

## Project Structure

```
project/
├── config/
│   └── config.py                # Configuration file for API keys
├── database/
│   ├── database.db              # SQLite database file
│   └── models.py                # Database functions (e.g., save, create tables)
├── scrapers/
│   ├── scraper.py               # Main scraping functions
│   └── extractors/              # Domain-specific extractors
│       ├── router.py            # Routes URLs to the correct extractor
│       ├── aljazeera_extractor.py
│       └── alarabiya_extractor.py
├── google_search/
│   └── google_search.py         # Google Search API integration
├── main.py                      # Main script to initiate scraping and export
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

## Setup

### Prerequisites

- Python 3.7 or later
- A Google Custom Search API key and Custom Search Engine ID

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/RAG_scraping.git
   cd RAG_scraping
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Credentials**:
   - Create a `config/config.py` file with your API key and Custom Search Engine ID:
     ```python
     GOOGLE_API_KEY = "your_api_key"
     GOOGLE_CX = "your_custom_search_engine_id"
     ```

## Usage

1. **Run Scraping and Export**:
   Execute the main script to scrape articles and export them to a CSV file:
   ```bash
   python main.py
   ```

2. **Results**:
   - Scraped articles are saved in `database/database.db`.
   - Exported CSV file will be located at `./csv/articles.csv`.

## License

This project is licensed under the MIT License.
```

--- 

This version is direct and provides a quick setup and usage guide. Let me know if you need any other changes!