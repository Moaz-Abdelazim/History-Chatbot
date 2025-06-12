import faiss
import pandas as pd
from sentence_transformers import SentenceTransformer

def ImportData(db_path, df_path, model_name):
    db = faiss.read_index(db_path)
    df = pd.read_csv(df_path)
    embedder = SentenceTransformer(model_name)
    return (db, df, embedder)

