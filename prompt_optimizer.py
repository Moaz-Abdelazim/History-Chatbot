def optimize_prompt(context, query):
    instruction = "You are a helpful historian AI. Answer Directly the question based on the provided context."
    prompt = f"{instruction}\n\nContext:\n{context}\n\nQuestion:\n{query}?\n\nAnswer:"
    return prompt
    