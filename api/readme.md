🤖 LangChain Dual-Deployment Chatbots (Gemini & Ollama)

This repository is a comprehensive portfolio project showcasing two common architectures for deploying Large Language Models (LLMs) with LangChain, using Google Gemini 2.5 Flash (Cloud) and Llama2 via Ollama (Local).

It demonstrates skills in application prototyping (Streamlit) and API deployment (FastAPI/LangServe).

🗂️ Project Structure

The project is organized by deployment type:

Folder / File

Content Type

Purpose

/

README.md, .gitignore, requirements.txt

Root: Project metadata and instructions.

chatbot/

gemini_app.py, llamaapp.py, README.md

Standalone Applications: Simple, all-in-one Streamlit files for quick prototyping and testing.

api/

app.py, client.py, README.md

Client-Server Deployment: Robust architecture using FastAPI/LangServe for scalable API deployment.

🌟 Deployable Architectures Demonstrated

1. Standalone Chatbots (/chatbot Folder)

Description: For fast local development and testing. The application handles the model invocation directly from the Streamlit file.

Models:

chatbot/gemini_app.py (Cloud)

chatbot/llamaapp.py (Local)

To Run:

conda activate langchain-dev
streamlit run chatbot/gemini_app.py 
# OR
streamlit run chatbot/llamaapp.py 


2. API Server & Client (/api Folder)

Description: A professional, decoupled service architecture. The Streamlit client calls the FastAPI server, which hosts two different LangChain runnables.

Endpoints:

/essay: Hosted on Gemini 2.5 Flash.

/poem: Hosted on Llama2 (Ollama).

To Run (Requires Two Terminals):

Start Server (Terminal 1):

conda activate langchain-dev
uvicorn api.app:app --reload --host 0.0.0.0 --port 8000


Start Client UI (Terminal 2):

conda activate langchain-dev
streamlit run api/client.py


🛠️ Setup and Environment (Conda)

Prerequisites

Conda/Miniconda and Git installed.

[Ollama Application] installed (required for Llama2).

API Keys: GEMINI_API_KEY and LANGSMITH_API_KEY in your .env file.

Installation Steps

# 1. Clone the repository
git clone [YOUR REPO URL HERE] 
cd [YOUR REPO FOLDER]

# 2. Create and activate environment
conda create --name langchain-dev python=3.10 pip
conda activate langchain-dev

# 3. Install all dependencies (from the comprehensive list)
pip install -r requirements.txt

# 4. Prepare local model (only needs to be done once)
ollama pull llama2


🔐 Secrets Configuration (.env file)

Do not commit this file.

GEMINI_API_KEY="YOUR_GEMINI_API_KEY_HERE"
LANGSMITH_TRACING=true
LANGSMITH_API_KEY="ls__YOUR_LANGSMITH_KEY_HERE"
LANGSMITH_PROJECT=LangChain-Dual-Deployment
