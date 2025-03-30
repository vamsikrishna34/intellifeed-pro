# IntelliFeed Pro: Real-Time Personalized News Recommender

IntelliFeed Pro is a modular Python application that delivers personalized news recommendations in real-time by combining sentence embeddings with user interest profiles. It is designed to demonstrate practical skills in natural language processing, embedding-based similarity matching, and modular software architecture, aligned with industry-relevant tools and workflows for AI engineering.

## Overview

The system allows a user to select from a set of simulated profiles, fetches recent news articles using NewsAPI, and ranks them based on semantic similarity to the user’s interests using Sentence-BERT embeddings.

This project showcases how modern NLP techniques can be applied to content recommendation and serves as a baseline for more advanced personalization and ranking systems.

## Features

- Fetches real-time news articles from NewsAPI
- Compares news content to user interests using SBERT embeddings
- Ranks articles by semantic similarity using cosine similarity
- Modular architecture for maintainability and extension
- Includes multiple user profiles representing diverse interest areas

## Project Structure

intellifeed_pro/
├── fetch_news.py         # Pulls real-time news from NewsAPI
├── user_profiles.py      # Contains simulated user profiles
├── recommender.py        # Uses SBERT embeddings to compute similarity
├── main.py               # CLI interface to run the full pipeline
├── README.md             # Documentation

## Installation

Install the required Python packages before running the application:

pip install pandas sentence-transformers requests

Ensure you have Python 3.7+ installed.

## How to Run

Execute the main script and follow the prompts:

python main.py

You will be asked to select a user profile. The system will then fetch the latest tech news and display the top recommendations based on that user’s interests.

## Technical Highlights

- Uses the sentence-transformers library for high-quality sentence embeddings
- Implements cosine similarity scoring for ranking
- Integrates external API data from NewsAPI
- Demonstrates basic command-line interaction for prototype testing
- Uses pandas for data handling and manipulation

## User Profiles

The system includes a set of pre-defined users, each with a different focus area:

- Ethan Brown – AI, machine learning, and automation
- Chloe Thompson – augmented reality, gaming, and consumer tech
- Maya Patel – healthcare AI and medical technology

## Future Work

This project is a working prototype and can be extended with the following:

- Add user feedback to improve personalization over time
- Store user sessions and preferences in a database
- Implement front-end interface using Streamlit or Flask
- Incorporate additional filtering and topic detection techniques

## Author

VamsiKrishna Nallagatla  
Graduate Student, DePaul University  
AI Engineering and Software Development  
LinkedIn: https://www.linkedin.com/in/vamsikrishna89/
