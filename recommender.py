from sentence_transformers import SentenceTransformer, util
import pandas as pd

# Define an empty DataFrame structure for fallback
EMPTY_DF = pd.DataFrame(columns=['title', 'publishedAt', 'score'])

# Load a lightweight model for fast Hugging Face deployment
try:
    model = SentenceTransformer('paraphrase-MiniLM-L3-v2')
except Exception as e:
    print(f"Error loading SentenceTransformer model: {e}")
    model = None

def recommend_articles(articles, user_interest, top_n=5):
    if model is None:
        print("Model not loaded. Cannot recommend articles.")
        return EMPTY_DF.copy()

    if not articles or not user_interest.strip():
        return EMPTY_DF.copy()

    try:
        df = pd.DataFrame(articles)
        if df.empty:
            return EMPTY_DF.copy()

        # Combine title, description, and content for embedding
        df['text'] = df['title'].fillna('') + " " + df['description'].fillna('') + " " + df['content'].fillna('')

        # Encode articles and user interest
        article_embeddings = model.encode(df['text'].tolist(), convert_to_tensor=True)
        user_embedding = model.encode(user_interest, convert_to_tensor=True)

        # Compute cosine similarity
        cosine_scores = util.cos_sim(user_embedding, article_embeddings)[0].cpu().numpy()
        df['score'] = cosine_scores

        # Return top N articles
        top_articles = df.sort_values(by='score', ascending=False).head(top_n)
        return top_articles[['title', 'publishedAt', 'score']]

    except Exception as e:
        print(f"Error during recommendation: {e}")
        return EMPTY_DF.copy()