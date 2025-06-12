# History-Chatbot
Chat bot for history
## Describtion
This project is a Rag System that answers questions about general and famous historical events , places or characters for some counteries
### Data
the data was got from kaggle (https://www.kaggle.com/datasets/budibudi/history-from-wikipedia)
the System is able to answer question about 6 counteries which are (China - Egypt - England - France - Germany - Greece)
### Models
the project contained 2 small models (affected it's acuurcy) which are Qwen3 0.6 and Qwen 1.8
## Run
### First download the requirments : (Bash) <br>
  cd History Chatbot Weaviate <br>
  pip install -r requirements.txt <br>

### Second download the models after installing requirments  : (Bash) <br>
  python download_model.py <br>

### Finally run the app : (Bash) <br>
  streamlit run app.py --server.fileWatcherType none
