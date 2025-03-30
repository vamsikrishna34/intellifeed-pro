from sentence_transformers import SentenceTransformer, util
import pandas as pd

model = SentenceTransformer('all-MiniLM-L6-v2')

def recommend_articles(articles, user_interest, top_n=5):
    df = pd.DataFrame(articles)
    df['text'] = df['title'].fillna('') + " " + df['description'].fillna('') + " " + df['content'].fillna('')

    article_embeddings = model.encode(df['text'].tolist(), convert_to_tensor=True)
    user_embedding = model.encode(user_interest, convert_to_tensor=True)

    cosine_scores = util.cos_sim(user_embedding, article_embeddings)[0].cpu().numpy()
    df['score'] = cosine_scores
    top_articles = df.sort_values(by='score', ascending=False).head(top_n)
    return top_articles[['title', 'publishedAt', 'score']]
