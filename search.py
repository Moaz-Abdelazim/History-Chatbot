from ImportData import ImportData
db_path = 'data\history_index.faiss'
df_path = 'data\history_dataset.csv'
model_name = 'all-MiniLM-L6-v2'

db, df, embedder = ImportData(db_path, df_path, model_name)

class search:
    
    def embed(self, query):
        query_emb = embedder.encode([query])
        return query_emb


    def get_ids(self, query_emb, top_k):
        _, ids = db.search(query_emb, k=top_k)
        return ids[0]

    def get_text(self, ids):

        return df.iloc[ids, -1].tolist()
    
    def find_similar(self, query, top_k):
        q_e = self.embed(query) #Query embedding
        ids = self.get_ids(q_e, top_k) #Ids of most similar
        return self.get_text(ids) #Text