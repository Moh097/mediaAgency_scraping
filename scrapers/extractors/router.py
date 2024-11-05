from scrapers.extractors.aljazeera_extractor import extract as aljazeera_extractor
from scrapers.extractors.alarabiya_extractor import extract as alarabiya_extractor


# Map each domain to its extractor
EXTRACTORS = {
    "www.aljazeera.net": aljazeera_extractor,
    "www.alarabiya.net": alarabiya_extractor
    # Add other mappings for each media agency
}

def get_extractor(url):
    for domain, extractor in EXTRACTORS.items():
        if domain in url:
            return extractor
    return None
