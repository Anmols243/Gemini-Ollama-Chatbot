🚀 Gemini-Ollama-Chatbot: Cloud vs. Local LLM Demo

This project features a powerful, minimal chatbot built with LangChain and Streamlit. It provides two parallel implementations—one connecting to the Google Gemini cloud API and one using a local Llama2 model via Ollama—for comparing performance and cost.

This is a great starting point for developers (especially those skilled in Python/ML) looking to build scalable LLM applications.

✨ Key Features

Dual Implementation: Separate Streamlit apps (gemini_app.py and llamaapp.py) for easy A/B testing of LLMs.

Core Logic: Uses LangChain Expression Language (LCEL) for efficient, readable model orchestration.

Secure Secrets: Utilizes .env and .gitignore to securely manage all API keys.

Clean Environment: Managed centrally using Conda to prevent dependency conflicts.

Tracing Enabled: Configured for debugging and monitoring via LangSmith (optional).

🛠️ Project Stack

Component

Technology

Model / Tool

Purpose

Framework

Python / LangChain

LCEL

Orchestration and model chaining.

Cloud LLM

langchain_google_genai

Gemini 2.5 Flash

High-speed, cost-effective cloud solution.

Local LLM

langchain_ollama

Llama2

Private, zero-cost local inference.

Frontend

Streamlit



Interactive web interface.

Environment

Conda



Centralized environment management.

⚙️ Local Setup and Installation

Prerequisites

Conda/Miniconda installed.

Git installed.

Ollama Application: Download and install Ollama.

Step 1: Clone and Prepare

# 1. Clone the repository (Use the correct URL from GitHub)
git clone [https://github.com/Anmols243/Gemini-Ollama-Chatbot.git](https://github.com/Anmols243/Gemini-Ollama-Chatbot.git)
cd Gemini-Ollama-Chatbot


Step 2: Set Up Environment with Conda

We create one clean, central environment and install all dependencies:

# 1. Create environment
conda create --name langchain-dev python=3.10 pip

# 2. Activate environment
conda activate langchain-dev

# 3. Install dependencies from requirements.txt
pip install -r requirements.txt


Step 3: Configure Secrets (.env File)

Create a file named .env in the project's root directory.

Obtain your keys and paste them into the .env file:

# Required for Google Gemini API Access
GEMINI_API_KEY="YOUR_GEMINI_API_KEY_HERE"

# Required for LangSmith Tracing (Optional for viewing logs)
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=[https://api.smith.langchain.com](https://api.smith.langchain.com)
LANGSMITH_API_KEY="ls__YOUR_LANGSMITH_KEY_HERE"
LANGSMITH_PROJECT=Chatbot-Dual-LLM


🚀 Running the Applications

Option A: Gemini (Cloud) Chatbot

Runs the cloud-based LLM via Google's API.

conda activate langchain-dev
streamlit run chatbot/gemini_app.py


Option B: Ollama (Local) Chatbot

Runs the local Llama2 model.

Pull the Model:

ollama pull llama2


Launch the App:

conda activate langchain-dev
streamlit run chatbot/llamaapp.py
