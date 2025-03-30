import requests

API_KEY = "31bd603a7db4444bba9287021b788465"

def fetch_latest_headlines(country="us", category="technology", page_size=20):
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "apiKey": API_KEY,
        "country": country,
        "category": category,
        "pageSize": page_size
    }
    response = requests.get(url, params=params)
    articles = response.json().get("articles", [])
    
    cleaned = []
    for art in articles:
        cleaned.append({
            "title": art["title"] or "",
            "description": art["description"] or "",
            "content": art["content"] or "",
            "publishedAt": art["publishedAt"]
        })
    return cleaned
