


## 🧪 Manual Test Cases for IntelliFeed Pro – Error Handling

### 1. Network Error (`fetch_news.py`)

**Setup:**
- Disconnect from the internet (disable Wi-Fi or unplug Ethernet).

**Steps:**
- Run `app.py` via Gradio.
- Enter any interest (e.g., "AI").

**Expected Output:**
- **Console log:**  
  `Error fetching articles: [requests.exceptions.ConnectionError]`
- **Gradio UI:**  
  `"Could not fetch news. Please check your API key or try again later."`
- **Behavior:**  
  App returns gracefully with no recommendations.

---

###  2. Invalid API Key (`fetch_news.py`)

**Setup:**
- Set `API_KEY = "INVALID_KEY"` in `fetch_news.py`.

**Steps:**
- Run `app.py`.
- Enter any interest.

**Expected Output:**
- **Console log:**  
  `Error fetching articles: 401 Client Error: Unauthorized`
- **Gradio UI:**  
  `" Could not fetch news. Please check your API key or try again later."`
- **Behavior:**  
  App exits gracefully without attempting recommendations.

---

###  3. Empty API Response (`fetch_news.py`)

**Setup:**
- Modify `query="asdfqwertylkjh"` in `fetch_latest_headlines()` to simulate no results.

**Steps:**
- Run `app.py`.
- Enter any interest.

**Expected Output:**
- **Console log:**  
  `"No articles found."`
- **Gradio UI:**  
  `" Could not fetch news. Please check your API key or try again later."`
- **Behavior:**  
  App exits gracefully without generating recommendations.

---

###  4. Model Loading Failure (`recommender.py`)

**Setup:**
- Rename or delete the cached model directory:  
  `~/.cache/torch/sentence_transformers/all-MiniLM-L6-v2`

**Steps:**
- Run `app.py`.

**Expected Output:**
- **Console log:**  
  `Error loading SentenceTransformer model: [OSError or FileNotFoundError]`
- **Gradio UI:**  
  `"ℹ️ News fetched, but no articles matched your interests. Try broader keywords."`
- **Behavior:**  
  App fetches news but fails to generate recommendations.

---

###  5. Empty Interest Input (`app.py`)

**Setup:**
- Leave the interest textbox blank.

**Steps:**
- Click "Get News Recommendations".

**Expected Output:**
- **Gradio UI:**  
  `"⚠️ Please enter some keywords or a sentence describing your interests."`
- **Behavior:**  
  App does not fetch news or generate recommendations.

---

###  6. No Articles for Recommendation (`fetch_news.py`)

**Setup:**
- Force `fetch_latest_headlines()` to return `[]` by adding `return []` before the final return.

**Steps:**
- Run `app.py`.
- Enter any interest.

**Expected Output:**
- **Console log:**  
  `"No articles found."`
- **Gradio UI:**  
  `" Could not fetch news. Please check your API key or try again later."`
- **Behavior:**  
  App exits gracefully without generating recommendations.

---


