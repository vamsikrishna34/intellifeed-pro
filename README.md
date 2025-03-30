# IntelliFeed Pro – Personalized News Recommender

This is a personal project I built to explore how natural language processing can be used to match user interests with news articles. The system pulls live headlines from NewsAPI and ranks them based on how closely they relate to a user’s interest profile using sentence embeddings.

The goal was to create something that feels realistic, is easy to extend, and helps me apply what I’ve learned about NLP, semantic similarity, and modular Python development.

## What It Does

- Takes a user’s interest profile (e.g., AI, AR, healthcare)
- Fetches recent tech news from NewsAPI
- Uses Sentence-BERT (SBERT) to create embeddings of the news content
- Compares the user’s interest to the articles using cosine similarity
- Returns a list of the top 5 most relevant articles

## How It Works

1. User selects a profile (there are 3 predefined users)
2. The app fetches recent headlines
3. The user's interest string is converted into an embedding
4. Each article is converted into an embedding
5. The most relevant articles are selected using cosine similarity

## Tech Stack

- Python
- sentence-transformers (SBERT)
- pandas
- NewsAPI
- requests

Why I Built This
I wanted to learn more about how embeddings work in NLP, and how they can be applied to real-world problems like recommendations. I also wanted to practice building modular code that could be extended later into a web app or support multiple users.

## How to Run

Install the requirements:

```bash
pip install pandas sentence-transformers requests

python main.py
