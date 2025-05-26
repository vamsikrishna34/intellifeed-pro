# Manual Test Cases for Error Handling

## 1. Network Errors for `fetch_news.py`

*   **Setup**:
    1.  Disconnect the machine running the application from the internet (e.g., turn off Wi-Fi, unplug ethernet cable).
*   **Steps**:
    1.  Run `python main.py`.
    2.  Select any user when prompted.
*   **Expected Output**:
    *   **Log**:
        *   `main.py`: Logs an error similar to "Failed to fetch news. Articles list is empty." (if `fetch_news.py` returns `[]` due to the network error being caught internally) OR "An unexpected error occurred while fetching news: [Specific requests.exceptions.ConnectionError or similar]".
        *   `fetch_news.py`: Logs an error similar to "Error during API request: [Specific requests.exceptions.ConnectionError or similar]".
    *   **User Message (stdout)**: "Failed to fetch news. Please check your internet connection or API key, or there might be no news available for the selected criteria."
    *   **Application Behavior**: The application should print the user message and then exit gracefully (e.g., `main()` function returns). No attempt should be made to generate recommendations.

## 2. API Key Errors for `fetch_news.py`

*   **Setup**:
    1.  Open `fetch_news.py`.
    2.  Modify the `API_KEY` variable to an invalid or expired key (e.g., `API_KEY = "INVALID_KEY"`).
    3.  Ensure the machine has an active internet connection.
*   **Steps**:
    1.  Run `python main.py`.
    2.  Select any user when prompted.
*   **Expected Output**:
    *   **Log**:
        *   `main.py`: Logs an error similar to "Failed to fetch news. Articles list is empty."
        *   `fetch_news.py`: Logs an error indicating an issue with the API request, likely mentioning a 401 or similar HTTP error, e.g., "Error during API request: 401 Client Error: Unauthorized for url: https://newsapi.org/v2/top-headlines?..."
    *   **User Message (stdout)**: "Failed to fetch news. Please check your internet connection or API key, or there might be no news available for the selected criteria."
    *   **Application Behavior**: The application should print the user message and then exit gracefully. No attempt should be made to generate recommendations.

## 3. Empty API Response for `fetch_news.py`

*   **Setup**:
    1.  This is hard to force externally without modifying the API. As an alternative, modify `fetch_news.py` to simulate an empty list of articles from a successful API call.
    2.  In `fetch_news.py`, inside the `fetch_latest_headlines` function, before `return cleaned`, temporarily add `return []` or ensure `data.get("articles", [])` results in an empty list (e.g. by changing `category` to something extremely obscure that is unlikely to return results, like `category="asdfqwertylkjh"`).
    3.  Ensure the API key is valid and internet is connected.
*   **Steps**:
    1.  Run `python main.py`.
    2.  Select any user when prompted.
*   **Expected Output**:
    *   **Log**:
        *   `fetch_news.py`: Logs an info message like "No articles found in API response for country: us, category: [your_test_category]."
        *   `main.py`: Logs an error "Failed to fetch news. Articles list is empty." (if `fetch_news.py` returns `[]`) or an info log "Successfully fetched 0 articles." followed by a warning "Could not generate recommendations..."
    *   **User Message (stdout)**: "Failed to fetch news. Please check your internet connection or API key, or there might be no news available for the selected criteria." (if main exits due to empty articles) OR "Could not generate recommendations at this time..." (if main proceeds but recommender gets no articles). The former is more likely with current implementation.
    *   **Application Behavior**: If `fetch_latest_headlines` returns `[]`, `main.py` should print the "Failed to fetch news..." message and exit. If it somehow proceeds, it should then state no recommendations could be made.

## 4. Model Loading Failure for `recommender.py`

*   **Setup**:
    1.  Identify the local cache directory for `sentence-transformers` models. This is typically `~/.cache/torch/sentence_transformers/`.
    2.  Inside this directory, find the `all-MiniLM-L6-v2` model.
    3.  Temporarily rename the `all-MiniLM-L6-v2` model directory (e.g., to `all-MiniLM-L6-v2_RENAMED`).
*   **Steps**:
    1.  Run `python main.py`.
*   **Expected Output**:
    *   **Log**:
        *   `recommender.py`: Logs a critical error similar to "Error loading SentenceTransformer model: [Specific error like file not found or OSError]".
        *   `main.py`: Logs "Application started." then, when `recommend_articles` is called (if it gets that far), it might log "Model not loaded. Cannot recommend articles."
    *   **User Message (stdout)**:
        *   The application will still prompt for user selection.
        *   After fetching news (assuming it's successful), when trying to get recommendations: "Could not generate recommendations at this time. This might be due to an issue with the recommendation engine or no relevant articles found." (This message appears because `recommend_articles` returns an empty DataFrame when the model isn't loaded).
    *   **Application Behavior**: The application should fetch news. When it tries to generate recommendations, it should fail and print the message above. It should finish without crashing.

## 5. Invalid User Input in `main.py`

*   **Setup**:
    1.  No special setup beyond having the application ready to run.
*   **Steps**:
    1.  Run `python main.py`.
    2.  When prompted "Enter user number (1-X):", enter "abc" (text instead of a number).
    3.  Observe the response.
    4.  When prompted again, enter a number far outside the valid range (e.g., "99" if there are only 3 users, or "0").
    5.  Observe the response.
    6.  Enter a valid user number.
*   **Expected Output**:
    *   **Log**: No specific error logs expected for this, but INFO logs for application start and eventual user selection.
    *   **User Message (stdout)**:
        *   After entering "abc": "Invalid input. Please enter a number."
        *   After entering "99" or "0": "Invalid choice. Please enter a number between 1 and X." (where X is the number of users).
        *   The prompt "Enter user number (1-X):" should reappear after each invalid input.
    *   **Application Behavior**: The application should continue to prompt for user selection until a valid number within the range is entered. It should then proceed normally.

## 6. Empty Interest String for `recommender.py`

*   **Setup**:
    1.  Open `user_profiles.py`.
    2.  Modify one of the user entries to have an empty list for interests, e.g., `{"id": "user3", "name": "User Three", "interests": []}`. Or, if it's a single string, `interests: ""`. (Based on `main.py` usage `', '.join(selected_user['interests'])`, it seems `interests` is a list of strings. So `[]` is the correct modification).
*   **Steps**:
    1.  Run `python main.py`.
    2.  Select the user that was modified to have empty interests.
*   **Expected Output**:
    *   **Log**:
        *   `recommender.py`: Logs a warning: "User interest is empty. Returning empty recommendations."
        *   `main.py`: Logs "Generating recommendations for user [Selected User] based on interests: " (with an empty string for interests), followed by "Could not generate recommendations. Recommendation engine returned no results or encountered an issue."
    *   **User Message (stdout)**: After fetching articles successfully: "Could not generate recommendations at this time. This might be due to an issue with the recommendation engine or no relevant articles found."
    *   **Application Behavior**: The application should fetch news successfully. When it attempts to generate recommendations, it should fail gracefully and print the message above, then finish.

## 7. No Articles for Recommendation (from `fetch_news.py`)

*   **Setup**:
    1.  This is similar to Test Case #3 (Empty API Response). Modify `fetch_news.py` so that `fetch_latest_headlines` returns an empty list `[]`. This simulates the case where news fetching was technically "successful" (no network/API key errors) but yielded no articles.
    2.  In `fetch_news.py`, inside `fetch_latest_headlines` function, before `return cleaned`, add a line: `return []`.
*   **Steps**:
    1.  Run `python main.py`.
    2.  Select any user.
*   **Expected Output**:
    *   **Log**:
        *   `fetch_news.py`: Logs might vary depending on where `return []` is inserted. If after logging successful fetch of 0 articles: "Successfully fetched and cleaned 0 articles."
        *   `main.py`: Logs "Failed to fetch news. Articles list is empty."
    *   **User Message (stdout)**: "Failed to fetch news. Please check your internet connection or API key, or there might be no news available for the selected criteria."
    *   **Application Behavior**: The application should print the user message and then exit gracefully. No attempt should be made to generate recommendations.

This set of test cases covers the specified scenarios and should help verify the robustness of the error handling implemented.
