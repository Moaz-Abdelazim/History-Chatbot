import streamlit as st
import torch
from query_handler import handle_query, DatabaseType
from inference_engine import generator

# Streamlit app configuration
st.set_page_config(page_title="History QA Bot", page_icon="📜", layout="centered")

# App title and description
st.title("History QA Bot")
st.markdown("Ask any question about history, and get detailed, accurate answers!")

# Initialize session state
if 'conversation' not in st.session_state:
    st.session_state.conversation = []
if 'models' not in st.session_state:
    st.session_state.models = {'Qwen 0.6B': None, 'Qwen 1.8B': None}
if 'model_choice' not in st.session_state:
    st.session_state.model_choice = None
if 'database_type' not in st.session_state:
    st.session_state.database_type = None
# Sidebar for settings
with st.sidebar:
    st.header("Settings")
    model_choice = st.radio(
        "Select Model:",
        ("Qwen 1.8B", "Qwen 0.6B"),
        help="Qwen 1.8B is more powerful but slower; Qwen 0.6B is faster but less detailed."
    )
    top_k = st.slider(
        "Number of context documents:",
        1, 10, 5,
        help="Select how many context documents to retrieve for answering."
    )
    Data_base_Type = st.radio(
        "Data Base Type",
        ("Faiss", "Weaviate"),
        help="Choose the Data Base Type",
        horizontal=True
    )

if Data_base_Type == 'Faiss':
    db = DatabaseType.FAISS
else:
    db = DatabaseType.WEAVIATE
# Load or reuse model
if st.session_state.model_choice != model_choice:
    with st.spinner(f"Loading {model_choice} model..."):
        # Clear previous model from memory
        if st.session_state.model_choice and st.session_state.models[st.session_state.model_choice]:
            del st.session_state.models[st.session_state.model_choice]
            if torch.cuda.is_available():
                torch.cuda.empty_cache()  # Clear GPU memory 
        st.session_state.model_choice = model_choice
        st.session_state.models[model_choice] = generator(model_choice)

llm_model = st.session_state.models[model_choice]
device = 'GPU' if torch.cuda.is_available() else 'CPU'
st.markdown(f'Working model is {llm_model.name} on {device} | Working DataBase is {Data_base_Type}')

# Input form for user question
with st.form(key="question_form"):
    user_question = st.text_input(
        "Enter your history question:",
        placeholder="e.g., What caused the Fall of the Roman Empire?",
        help="Ask specific questions for best results, e.g., 'Who was Cleopatra?'"
    )
    submit_button = st.form_submit_button(label="Ask")

# Handle form submission
if submit_button and user_question:
    with st.spinner("Fetching historical insights..."):
        try:
            bot_response = handle_query(user_question, llm_model, top_k=top_k, database_type=db)
            st.session_state.conversation.append({"question": user_question, "answer": bot_response})
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

# Display conversation history
if st.session_state.conversation:
    st.subheader("Conversation")
    for i, entry in enumerate(st.session_state.conversation):
        with st.expander(f"Q{i+1}: {entry['question'][:50]}..." if len(entry['question']) > 50 else f"Q: {entry['question']}"):
            st.markdown(f"**Question:** {entry['question']}")
            st.markdown(f"**Answer:** {entry['answer']}")

# Add a clear history button
if st.button("Clear History"):
    st.session_state.conversation = []
    st.rerun()

# Download conversation history
if st.session_state.conversation:
    history_text = "\n".join([f"Q: {entry['question']}\nA: {entry['answer']}\n---" for entry in st.session_state.conversation])
    st.download_button(
        label="Download Conversation",
        data=history_text,
        file_name="history_qa_conversation.txt",
        mime="text/plain"
    )

# Footer
st.markdown("---")