import requests
from config.config import GOOGLE_API_KEY, GOOGLE_CX

class GoogleSearch:
    def __init__(self):
        self.api_key = GOOGLE_API_KEY
        self.cx = GOOGLE_CX
    
    def get_search_results(self, query, num_results=10):
        """Retrieve search results from Google Custom Search API."""
        url = "https://www.googleapis.com/customsearch/v1"
        params = {
            'key': self.api_key,
            'cx': self.cx,
            'q': query,
            'num': num_results
        }
        
        response = requests.get(url, params=params)
        data = response.json()
        
        # Check for errors
        if 'error' in data:
            print("Error:", data['error'])
            return []
        
        return data.get('items', [])

    def collect_unique_results(self, query_base, date_ranges, max_results=300):
        """Collect unique results based on date ranges."""
        all_results = []
        unique_links = set()
        
        for date_range in date_ranges:
            # Construct query with specific date range
            query = f"{query_base} after:{date_range['after']} before:{date_range['before']}"
            start_index = 1  # Start at page 1 for each date range
            
            while len(all_results) < max_results and start_index <= 91:
                results = self.get_search_results(query, start_index=start_index)
                
                for result in results:
                    link = result.get('link')
                    if link and link not in unique_links:
                        unique_links.add(link)
                        all_results.append(result)
                
                start_index += 10  # Move to the next page
                
                # Stop if there are no more pages
                if len(results) < 10:
                    break

            # Stop if we've already reached the maximum number of results
            if len(all_results) >= max_results:
                break
        
        return all_results
