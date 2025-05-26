import streamlit as st
from fetch_news import fetch_latest_headlines
from recommender import recommend_articles
import pandas as pd

st.title("IntelliFeed Pro - News Recommender")

user_input_interests = st.text_input("Enter your interests (e.g., AI, machine learning):")
recommend_button_pressed = st.button("Get News Recommendations")

if recommend_button_pressed:
    if not user_input_interests.strip():
        st.warning("Please enter some keywords or a sentence describing your interests before clicking 'Get News Recommendations'.")
    else:
        with st.spinner("Fetching news and generating recommendations..."):
            # Fetch News
            # Using default parameters for country (us) and category (technology)
            articles = fetch_latest_headlines() 
            
            if not articles: # fetch_latest_headlines returns [] on error or no articles
                st.error("Could not fetch news. Please check your connection/API key, ensure news service is available, or try again later.")
            else:
                # Get Recommendations
                # recommend_articles expects a list of article dicts and a string of interests
                recommendations_df = recommend_articles(articles, user_input_interests) 
                
                if recommendations_df.empty:
                    # Assuming recommender.py logs its internal errors (e.g., model issues).
                    # An empty DataFrame here, after successfully fetching articles,
                    # implies no articles matched the specific interest.
                    st.info("Successfully fetched news, but no articles closely matched your specified interests. Try broadening your search terms.")
                else:
                    st.subheader("Top Recommendations for you:")
                    st.dataframe(recommendations_df)
