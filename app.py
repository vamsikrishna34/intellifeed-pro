import gradio as gr
import time
from src.fetch_news import fetch_latest_headlines
from src.recommender import recommend_articles
import pandas as pd

def get_recommendations(user_input_interests):
    start_time = time.time()

    if not user_input_interests.strip():
        return " Please enter some keywords or a sentence describing your interests.", pd.DataFrame()

    articles = fetch_latest_headlines(page_size=10)  # Keep it fast

    if not articles:
        return " Could not fetch news. Please check your API key or try again later.", pd.DataFrame()

    recommendations_df = recommend_articles(articles, user_input_interests)

    if recommendations_df.empty:
        return "ℹNews fetched, but no articles matched your interests. Try broader keywords.", pd.DataFrame()

    elapsed = end_time = time.time() - start_time
    status = f"Top Recommendations (completed in {elapsed:.2f} seconds):"
    return status, recommendations_df[["title", "url"]]

demo = gr.Interface(
    fn=get_recommendations,
    inputs=gr.Textbox(label="Enter your interests (e.g., AI, machine learning)", lines=2, placeholder="Type your interests here..."),
    outputs=[
        gr.Textbox(label="Status"),
        gr.Dataframe(label="Recommended Articles")
    ],
    title="📰 IntelliFeed Pro - News Recommender",
    description="Get personalized news recommendations based on your interests using NLP and TF-IDF similarity."
)

if __name__ == "__main__":
    demo.launch()