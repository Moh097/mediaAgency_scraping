### README.md

```markdown
# Media Agency Scraping

A Python tool to scrape articles from specific media websites using Google Custom Search API. Extracts article details, stores them in a SQLite database, and exports to CSV.

## Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Moh097/mediaAgency_scraping.git
   cd mediaAgency_scraping
   ```

2. **Install Requirements**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Add API Keys**:
   - Create `config/config.py` with:
     ```python
     GOOGLE_API_KEY = "your_api_key"
     GOOGLE_CX = "your_search_engine_id"
     ```

## Usage

Run the main script to scrape articles and export to CSV:
```bash
python main.py
```

## Project Structure

- **config/**: API configuration
- **database/**: SQLite database and models
- **scrapers/**: Scraping logic and extractors
- **google_search/**: Google Search API integration
- **main.py**: Main script to run everything
- **requirements.txt**: Python dependencies
