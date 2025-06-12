
# 🏛️ History-Chatbot

A retrieval-augmented chatbot that answers questions about famous historical events, figures, and places across six countries. This project uses a combination of local language models (Qwen series) and vector search databases (FAISS or Weaviate) to deliver intelligent, context-aware answers.

---

## 📌 Description

**History-Chatbot** is a RAG (Retrieval-Augmented Generation) system built to answer history-related questions using information sourced from Wikipedia. It supports user-configurable options such as:

- Choice of local LLMs: **Qwen 0.6B** or **Qwen 1.8B**
- Retrieval of a custom number of text chunks
- Selection of vector store: **FAISS** or **Weaviate**

---

## 🌍 Supported Countries

The chatbot currently supports historical data related to the following countries:

- 🇨🇳 China  
- 🇪🇬 Egypt  
- 🏴 England  
- 🇫🇷 France  
- 🇩🇪 Germany  
- 🇬🇷 Greece  

---

## 📚 Dataset

Historical data is sourced from a Kaggle dataset:  
[📎 History from Wikipedia](https://www.kaggle.com/datasets/budibudi/history-from-wikipedia)

---

## 🚀 Features

- Lightweight and local — no external API calls
- Switch between small Qwen models based on performance needs
- Choose between FAISS (local) or Weaviate (cloud/local) vector database
- Streamlit-powered frontend for a simple UI
- Modular codebase for easy extension

---

## 🛠️ Setup Instructions

### 1️⃣ Install Dependencies

> ✅ **Python 3.11 is required**  
> Make sure you have Python 3.11 installed before proceeding.

```bash
git clone https://github.com/Moaz-Abdelazim/History-Chatbot.git
cd History-Chatbot
pip install -r requirements.txt
```

> 💡 You can create a virtual environment (optional but recommended):
```bash
python3.11 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 2️⃣ Download the LLMs

```bash
python download_model.py
```

This will fetch the Qwen models used in the inference pipeline.

### 3️⃣ Run the Application

```bash
streamlit run app.py --server.fileWatcherType none
```

---

## 💡 Example Query

> **Question**: *"What events led to the unification of Germany?"*  
> **Expected Output**: The chatbot will retrieve relevant chunks and summarize an answer using the selected model.

---

## 🧠 File Structure Overview

```
History-Chatbot/
├── app.py                  # Streamlit UI
├── create_llm_model.py     # Model instantiation logic
├── download_model.py       # Downloads Qwen models
├── inference_engine.py     # Handles inference
├── prompt_optimizer.py     # Refines user queries
├── query_handler.py        # Full RAG pipeline logic
├── search.py               # Chunk retrieval
├── Weaviate_Client.py      # Weaviate vector DB interface
├── ImportData.py           # Loads and processes dataset
├── README.md               # Project overview
└── requirements.txt        # Project dependencies
```

---

## ✨ Future Enhancements

- ✅ Add support for more countries and regions  
- 🔍 Use larger or more accurate language models with quantization or GPU acceleration  
- 📊 Integrate answer evaluation metrics (e.g., semantic similarity, factual accuracy)  
- 🖼️ Improve UI using Streamlit components like dropdowns, expandable sections, and history view  
- 🧪 Add unit tests and CI/CD integration  

---

## 📬 Contact

Developed by [**Moaz Abdelazim**](https://github.com/Moaz-Abdelazim)  
Feel free to open issues or pull requests with suggestions, bugs, or contributions!

---
