# IntelliFeed Pro – Personalized News Recommender

This is a personal project I built to explore how natural language processing can be used to match user interests with news articles. The system pulls live headlines from NewsAPI and ranks them based on how closely they relate to a user’s interest profile using sentence embeddings.

The goal was to create something that feels realistic, is easy to extend, and helps me apply what I’ve learned about NLP, semantic similarity, and modular Python development.

## What It Does

- Fetches recent tech news from NewsAPI.
- Allows users to input their interests (e.g., "AI safety", "quantum computing advancements") via an interactive web interface or select a predefined profile in the command-line version.
- Uses Sentence-BERT (SBERT) to create embeddings of the news content and user interests.
- Compares the user’s interest to the articles using cosine similarity.
- Returns a list of the most relevant articles, displayed in the web app or console.

## Features

- **Interactive Web Interface**: Built with Streamlit, allowing users to dynamically enter interests and receive news recommendations.
- **Command-Line Interface**: Original version allowing selection from predefined user profiles.
- **Semantic Search**: Leverages sentence embeddings for nuanced understanding of article content and user interests.
- **Modular Design**: Core logic for news fetching and recommendation is separated, making it easier to maintain and extend.

## How It Works

The core logic involves:
1. **Input**: User provides interests via the Streamlit app or selects a profile in the CLI.
2. **News Fetching**: The application fetches the latest technology headlines from NewsAPI.
3. **Embedding Generation**: Both the user's interests and the fetched articles are converted into numerical representations (embeddings) using a Sentence-BERT model.
4. **Similarity Calculation**: Cosine similarity is used to measure the relevance between the user's interest embedding and each article's embedding.
5. **Ranking & Display**: Articles are ranked by their similarity score, and the top results are presented to the user.

## Tech Stack

- Python
- Streamlit (for the web interface)
- sentence-transformers (SBERT for embeddings)
- pandas (for data manipulation)
- requests (for NewsAPI communication)
- NewsAPI (as the news source)

Why I Built This
I wanted to learn more about how embeddings work in NLP, and how they can be applied to real-world problems like recommendations. I also wanted to practice building modular code and explore tools like Streamlit for creating simple data applications.

## How to Run

First, install the required libraries using the provided `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### Running the Web Application (Recommended)
To run the interactive web application:
```bash
streamlit run app.py
```
This will open the application in your web browser, where you can type your interests and get news recommendations.

### Running the Original Command-Line Version
To run the original command-line interface (for predefined user profiles):
```bash
python main.py
```
This will prompt you to select a predefined user profile.
