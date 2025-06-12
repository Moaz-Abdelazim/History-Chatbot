# from context_retriever import retrieve_context
from search import search
from prompt_optimizer import optimize_prompt
from inference_engine import generator
from Weaviate_Client import searchForSimiliratiy
from enum import Enum
import time

class DatabaseType(Enum):
    FAISS = "FAISS"
    WEAVIATE = "WEAVIATE"
    
def handle_query(query, model, top_k=5, database_type=DatabaseType.FAISS):
    t1 = time.time()
    print('Getting Context ...')
    # Retrieve context based on the selected database type
    if database_type == DatabaseType.FAISS:
        context = search().find_similar(query, top_k)
    elif database_type == DatabaseType.WEAVIATE:
        context = searchForSimiliratiy(query=query, limit=top_k)
    else:
        raise ValueError("Invalid database type provided.")
    print('Creating Prompt ...')
    prompt = optimize_prompt(context, query)
    print("Getting Model's Answer ...")
    answer = model(prompt)
    print("Done")
    t2 = time.time()
    print(f'Time Taken : {(t2-t1)/60}')
    return answer