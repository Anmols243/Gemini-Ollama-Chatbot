🚀 Webloader RAG App (Groq + AstraDB + HuggingFace)

A streamlit-based Retrieval-Augmented Generation (RAG) application that:

Scrapes and loads content from a web page

Splits it into chunks

Generates embeddings using HuggingFace

Stores & retrieves relevant chunks from AstraDB (Cassandra)

Uses Groq LLM for fast, intelligent answers

Wraps everything into an interactive frontend (Streamlit)

This project transforms the earlier groq.ipynb notebook version into a fully functional web app.

📌 Features

✔ Web page loader using WebBaseLoader
✔ Text chunking using recursive character splitter
✔ BGE-small embeddings for efficient high-quality vectorization
✔ AstraDB vector store to persist embeddings
✔ Groq LLM (LLaMA/OpenAI OSS models) for ultra-fast inference
✔ RAG pipeline with context + question answering
✔ Streamlit UI for real-time interaction
✔ Session-state caching to avoid recomputing embeddings and DB writes

🧩 Architecture Overview
Web Page → Loader → Chunk Splitter → Embeddings → AstraDB Vector Store
                              ↓
                        Retriever
                              ↓
                          RAG Chain
                              ↓
                         Groq LLM
                              ↓
                    Streamlit Frontend

🛠️ Installation
1. Clone the repo
git clone <your-repo-url>
cd Webloader_app

2. Install dependencies
pip install -r requirements.txt

3. Set environment variables

Create a .env file:

GROQ_API_KEY=your_key
ASTRA_DB_TOKEN=your_token
ASTRA_DB_ID=your_id
ASTRA_DB_ENDPOINT=your_endpoint

▶️ Run the App
streamlit run app.py

🧠 How It Works
1. Session-state Initialization

Connect to AstraDB

Load embeddings model

Load + scrape web content

Split into chunks

Upload vectors to Cassandra/AstraDB once

2. Retrieval

The query passes through:

Input → Retriever → Relevant Docs → LLM Prompt → Groq LLM → Answer

3. Prompting

The LLM receives:

Clean formatted context

Clean question

Instructions to output only the final answe