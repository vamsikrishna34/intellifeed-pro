# Manual Test Cases for Streamlit Web Application (`app.py`)

These test cases are designed to verify the functionality and user experience of the Streamlit web application.

## 1. Successful Recommendation

*   **Setup**:
    1.  Ensure all dependencies from `requirements.txt` are installed (`pip install -r requirements.txt`).
    2.  Ensure an active internet connection.
    3.  Verify that the NewsAPI key in `fetch_news.py` is valid and has not exceeded its quota.
    4.  Ensure the SentenceTransformer model (`all-MiniLM-L6-v2`) is available (downloaded automatically on first run of `recommender.py` if internet is available).
*   **Steps**:
    1.  In your terminal, run `streamlit run app.py`.
    2.  Open the web application in your browser (usually `http://localhost:8501`).
    3.  In the text input field labeled "Enter your interests (e.g., AI, machine learning):", enter a relevant interest like "artificial intelligence security" or "latest advancements in quantum computing".
    4.  Click the "Get News Recommendations" button.
*   **Expected Output**:
    *   **Web Interface**:
        *   A spinner message "Fetching news and generating recommendations..." appears while processing.
        *   After a short delay, the spinner disappears.
        *   A subheader "Top Recommendations for you:" is displayed.
        *   Below the subheader, a table (DataFrame) of recommended articles is shown, containing columns like 'title', 'publishedAt', and 'score'.
        *   No error messages are displayed.
    *   **Console Log (Terminal where `streamlit run app.py` was executed)**:
        *   Logs from `fetch_news.py` indicating successful fetching (e.g., "Fetching headlines...", "Successfully fetched and cleaned X articles.").
        *   Logs from `recommender.py` indicating successful model loading (if first time for this session) and recommendation generation (e.g., "SentenceTransformer model loaded successfully.", "Successfully generated Y recommendations...").

## 2. Empty Input

*   **Setup**:
    1.  Ensure all dependencies from `requirements.txt` are installed.
*   **Steps**:
    1.  In your terminal, run `streamlit run app.py`.
    2.  Open the web application in your browser.
    3.  Ensure the text input field for interests is empty.
    4.  Click the "Get News Recommendations" button.
*   **Expected Output**:
    *   **Web Interface**:
        *   A warning message "Please enter some keywords or a sentence describing your interests before clicking 'Get News Recommendations'." is displayed.
        *   No spinner should appear.
        *   No attempt should be made to fetch news or display recommendations.
    *   **Console Log**: No logs related to news fetching or recommendation processing.

## 3. Interests Yielding No Matching Articles

*   **Setup**:
    1.  Ensure all dependencies from `requirements.txt` are installed.
    2.  Ensure an active internet connection.
    3.  Verify that the NewsAPI key is valid.
*   **Steps**:
    1.  In your terminal, run `streamlit run app.py`.
    2.  Open the web application in your browser.
    3.  In the text input field, enter very obscure, nonsensical, or extremely niche interests that are unlikely to match any current technology news articles (e.g., "ancient Mesopotamian pottery techniques in modern software development", "asdfghjklqwerty", "the culinary habits of undiscovered deep-sea creatures").
    4.  Click the "Get News Recommendations" button.
*   **Expected Output**:
    *   **Web Interface**:
        *   A spinner message "Fetching news and generating recommendations..." appears.
        *   After processing, an informational message "Successfully fetched news, but no articles closely matched your specified interests. Try broadening your search terms." is displayed.
        *   No table of recommendations is shown.
    *   **Console Log**:
        *   Logs from `fetch_news.py` indicating successful fetching (e.g., "Successfully fetched and cleaned X articles.").
        *   Logs from `recommender.py` indicating it processed the request but likely found no relevant articles (e.g., "Successfully generated 0 recommendations...").

## 4. Simulated News Fetching Failure (Network Disconnected)

*   **Setup**:
    1.  Ensure all dependencies from `requirements.txt` are installed.
    2.  **Disconnect the machine from the internet** (e.g., turn off Wi-Fi, unplug the ethernet cable).
*   **Steps**:
    1.  In your terminal, run `streamlit run app.py`.
    2.  Open the web application in your browser.
    3.  Enter valid interests (e.g., "renewable energy").
    4.  Click the "Get News Recommendations" button.
*   **Expected Output**:
    *   **Web Interface**:
        *   A spinner message "Fetching news and generating recommendations..." appears.
        *   After attempting to fetch, an error message "Could not fetch news. Please check your connection/API key, ensure news service is available, or try again later." is displayed.
    *   **Console Log**:
        *   Logs from `fetch_news.py` indicating an error during the API request (e.g., "Error during API request: ConnectionError...").
        *   `app.py` itself doesn't log this specific error to the console, but relies on `fetch_news.py` logging.

## 5. Simulated Model Loading Failure (Conceptual)

*   **Note**: This test is difficult to perform reliably without code modification or manipulating the model cache in a potentially disruptive way. It's more of a thought experiment based on the implemented error handling in `recommender.py`.
*   **Ideal Setup (Hypothetical)**:
    1.  Ensure all dependencies from `requirements.txt` are installed.
    2.  Corrupt or rename the cached SentenceTransformer model directory (e.g., `~/.cache/torch/sentence_transformers/all-MiniLM-L6-v2_RENAMED`) such that `recommender.py` cannot load the model.
    3.  Prevent `recommender.py` from re-downloading the model (e.g., by also disconnecting from the internet after corrupting the cache).
*   **Steps**:
    1.  In your terminal, run `streamlit run app.py`.
    2.  Open the web application in your browser.
    3.  Enter valid interests (e.g., "cloud computing").
    4.  Click the "Get News Recommendations" button.
*   **Expected Output (based on current error handling)**:
    *   **Web Interface**:
        *   A spinner message "Fetching news and generating recommendations..." appears.
        *   If `recommender.py` fails to load the model and returns an empty DataFrame as a result:
            *   An informational message "Successfully fetched news, but no articles closely matched your specified interests. Try broadening your search terms." is displayed. (This is because `app.py` currently doesn't distinguish between "model failed" and "no articles matched" if `recommender.py` returns an empty DataFrame. The distinction is only in the logs.)
    *   **Console Log**:
        *   Critical logs from `recommender.py` indicating "Error loading SentenceTransformer model: [Specific Error]".
        *   `fetch_news.py` logs successful article fetching.
        *   `app.py` logs will show that articles were fetched but no recommendations were generated.

## 6. General UI/UX

*   **Setup**:
    1.  Ensure all dependencies from `requirements.txt` are installed.
*   **Steps**:
    1.  In your terminal, run `streamlit run app.py`.
    2.  Open the web application in your browser.
    3.  Visually inspect the application.
*   **Expected Output**:
    *   **Web Interface**:
        *   **Title**: The title "IntelliFeed Pro - News Recommender" is displayed prominently, likely at the top of the page.
        *   **Input Field**: A text input field is present, clearly labeled "Enter your interests (e.g., AI, machine learning):".
        *   **Button**: A button labeled "Get News Recommendations" is visible and clickable.
        *   **Responsiveness (Basic)**: If the browser window is resized, the elements should adjust without significant layout issues (Streamlit handles much of this by default).
        *   **Readability**: When recommendations are displayed, the text in the table (article titles, publication dates, scores) should be clear and easy to read. Error and warning messages should also be easily readable.
    *   **Console Log**: No errors related to rendering UI elements.

These test cases should provide good coverage for the Streamlit application's main functionalities and error states.
