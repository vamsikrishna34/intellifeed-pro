from sentence_transformers import SentenceTransformer, util
import pandas as pd

# Define an empty DataFrame structure for error returns
EMPTY_DF = pd.DataFrame(columns=['title', 'publishedAt', 'score'])

try:
    model = SentenceTransformer('all-MiniLM-L6-v2')
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

        df['text'] = df['title'].fillna('') + " " + df['description'].fillna('') + " " + df['content'].fillna('')
        article_embeddings = model.encode(df['text'].tolist(), convert_to_tensor=True)
        user_embedding = model.encode(user_interest, convert_to_tensor=True)

        cosine_scores = util.cos_sim(user_embedding, article_embeddings)[0].cpu().numpy()
        df['score'] = cosine_scores
        top_articles = df.sort_values(by='score', ascending=False).head(top_n)

        return top_articles[['title', 'publishedAt', 'score']]
    except Exception as e:
        print(f"Error during recommendation: {e}")
        return EMPTY_DF.copy()