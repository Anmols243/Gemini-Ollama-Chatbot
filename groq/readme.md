Groq RAG App (Streamlit + LangChain + FAISS + Ollama Embeddings)

This project is a fully functional Retrieval-Augmented Generation (RAG) application built using:

Groq LLMs (LLaMA 3.3 70B / Mixtral / Gemma…)

LangChain (latest v0.2 syntax with RunnableGraph)

FAISS vector store

Ollama Embeddings (mxbai-embed-large)

Streamlit UI

WebBaseLoader for scraping documentation

It loads documents from LangChain docs, splits them into chunks, embeds them locally using Ollama, stores them in FAISS, and answers user questions using a Groq LLM with retrieved context.

🚀 Features

✔ Fully working RAG pipeline
✔ Uses modern LangChain v0.2 syntax
✔ Uses RunnablePassthrough + itemgetter (recommended by LangChain)
✔ Fast embeddings using Ollama (local)
✔ Super fast inference using GroqCloud
✔ Beautiful Streamlit UI
✔ Loads + chunks + embeds + retrieves + answers

📦 Installation
1. Clone the repo
git clone <your-repo-url>
cd groq-rag-app

2. Create virtual environment (optional)
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

4. Install Ollama (for embeddings)

Download from:
https://ollama.com/download

Then pull the embedding model:

ollama pull mxbai-embed-large

🔑 Environment Variables

Create a .env file:

GROQ_API_KEY=your_api_key_here


Generate your key here:
https://console.groq.com/keys

▶️ Running the App
streamlit run app.py