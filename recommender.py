from sentence_transformers import SentenceTransformer, util
import pandas as pd
import logging

# Define an empty DataFrame structure for error returns
EMPTY_DF = pd.DataFrame(columns=['title', 'publishedAt', 'score'])

try:
    model = SentenceTransformer('all-MiniLM-L6-v2')
    model_loaded = True
    logging.info("SentenceTransformer model loaded successfully.")
except Exception as e:
    logging.error(f"Error loading SentenceTransformer model: {e}")
    model = None
    model_loaded = False

def recommend_articles(articles, user_interest, top_n=5):
    if not model_loaded:
        logging.error("Model not loaded. Cannot recommend articles.")
        return EMPTY_DF.copy()

    if not articles:
        logging.warning("Input 'articles' list is empty. Returning empty recommendations.")
        return EMPTY_DF.copy()
    
    if not user_interest or not user_interest.strip():
        logging.warning("User interest is empty. Returning empty recommendations.")
        return EMPTY_DF.copy()

    try:
        df = pd.DataFrame(articles)
        if df.empty: # Handles case where articles is not empty but results in an empty DataFrame
            logging.warning("Input 'articles' resulted in an empty DataFrame. Returning empty recommendations.")
            return EMPTY_DF.copy()
            
        df['text'] = df['title'].fillna('') + " " + df['description'].fillna('') + " " + df['content'].fillna('')
    except Exception as e:
        logging.error(f"Error creating DataFrame or 'text' column: {e}")
        return EMPTY_DF.copy()

    try:
        article_embeddings = model.encode(df['text'].tolist(), convert_to_tensor=True)
    except Exception as e:
        logging.error(f"Error encoding article embeddings: {e}")
        return EMPTY_DF.copy()
        
    try:
        user_embedding = model.encode(user_interest, convert_to_tensor=True)
    except Exception as e:
        logging.error(f"Error encoding user interest embedding: {e}")
        return EMPTY_DF.copy()

    try:
        cosine_scores = util.cos_sim(user_embedding, article_embeddings)[0].cpu().numpy()
        df['score'] = cosine_scores
        top_articles = df.sort_values(by='score', ascending=False).head(top_n)
        logging.info(f"Successfully generated {len(top_articles)} recommendations for user interest: {user_interest[:50]}...") # Log first 50 chars of interest
        return top_articles[['title', 'publishedAt', 'score']]
    except Exception as e:
        logging.error(f"Error during similarity calculation or ranking: {e}")
        return EMPTY_DF.copy()
