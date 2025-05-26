import requests
import logging



def fetch_latest_headlines(country="us", category="technology", page_size=20):
    logging.info(f"Fetching headlines for country: {country}, category: {category}, page_size: {page_size}")
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "country": country,
        "category": category,
        "pageSize": page_size
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4XX or 5XX)
    except requests.exceptions.RequestException as e:
        logging.error(f"Error during API request: {e}")
        return []

    try:
        data = response.json()
    except ValueError as e: # Catches JSON decoding errors
        logging.error(f"Error decoding JSON response: {e}")
        return []
        
    articles = data.get("articles", [])
    if not articles: # Handles empty or missing 'articles'
        logging.info(f"No articles found in API response for country: {country}, category: {category}.")
        return []
    
    cleaned = []
    for art in articles:
        cleaned.append({
            "title": art["title"] or "",
            "description": art["description"] or "",
            "content": art["content"] or "",
            "publishedAt": art["publishedAt"]
        })
    logging.info(f"Successfully fetched and cleaned {len(cleaned)} articles.")
    return cleaned
