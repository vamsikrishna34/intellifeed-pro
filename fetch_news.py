import requests

API_KEY = "bdf6b197b973437d8e9d20e191028de8"

def fetch_latest_headlines(query="technology", page_size=10):
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "q": query,
        "pageSize": page_size,
        "language": "en",
        "apiKey": API_KEY
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(f" Error fetching articles: {e}")
        return []

    articles = data.get("articles", [])
    if not articles:
        print("ℹ️ No articles found.")
        return []

    cleaned = []
    for art in articles:
        cleaned.append({
            "title": art.get("title", ""),
            "description": art.get("description", ""),
            "content": art.get("content", ""),
            "url": art.get("url", ""),
            "publishedAt": art.get("publishedAt", "")
        })

    return cleaned