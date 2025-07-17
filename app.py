import gradio as gr
import time
import pandas as pd

from fetch_news import fetch_latest_headlines
from recommender import recommend_articles

def get_recommendations(user_input_interests):
    print(f"Received input: {user_input_interests}")
    start_time = time.time()

    if not user_input_interests.strip():
        print(" Empty input received.")
        return "Please enter some keywords or a sentence describing your interests.", pd.DataFrame()

    articles = fetch_latest_headlines(page_size=10)
    print(f" Fetched {len(articles)} articles")

    if not articles:
        print("No articles returned from fetch_news.")
        return "Could not fetch news. Please check your API key or try again later.", pd.DataFrame()

    recommendations_df = recommend_articles(articles, user_input_interests)
    print(f" Recommendations shape: {recommendations_df.shape}")

    if recommendations_df.empty:
        print("ℹ No matching articles found.")
        return "News fetched, but no articles matched your interests. Try broader keywords.", pd.DataFrame()

    elapsed = time.time() - start_time
    status = f"Top Recommendations (completed in {elapsed:.2f} seconds):"
    print(" Returning recommendations.")
    return status, recommendations_df[["title", "url"]]

demo = gr.Interface(
    fn=get_recommendations,
    inputs=gr.Textbox(
        label="Enter your interests (e.g., AI, machine learning)",
        lines=2,
        placeholder="Type your interests here..."
    ),
    outputs=[
        gr.Textbox(label="Status"),
        gr.Dataframe(label="Recommended Articles")
    ],
    title="📰 IntelliFeed Pro - News Recommender",
    description="Get personalized news recommendations based on your interests using NLP and semantic similarity."
)

if __name__ == "__main__":
    demo.launch()