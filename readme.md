🚀 Gemini-Ollama-Chatbot: Cloud and Local LLM 

This project demonstrates a fully functional, minimal chatbot built with LangChain and Streamlit. It features two separate implementations that share the same core logic: one using a powerful cloud API (Google Gemini) and another using a local, open-source model (Llama2 via Ollama).

This setup is ideal for developers looking to compare cloud API performance, cost, and latency against private, local inference.

✨ Features

Dual Implementation: Separate Streamlit apps for Gemini and Ollama.

LangChain Expression Language (LCEL): Efficient and modern chain setup.

Secure Secrets Management: Uses .env and .gitignore to protect API keys.

Robust Environment: Uses Conda for clean, centralized environment management.

Tracing Enabled: Configured for tracing via LangSmith for debugging and performance analysis.

🛠️ Tech Stack

Component

Technology

Purpose

Framework

LangChain (Python)

Orchestration and model chaining.

Cloud LLM

Gemini 2.5 Flash

High-speed, cost-effective cloud model.

Local LLM

Llama2

Privacy-focused, zero-cost model via Ollama.

Frontend

Streamlit

Interactive web interface.

Dependency Mgmt

Conda (Recommended)

Centralized, clean, and robust environment isolation.

⚙️ Local Setup Instructions

Prerequisites

Conda/Miniconda installed.

Python 3.10+ installed.

Git installed.

Ollama Application: Download and install Ollama to run the local LLM.

Step 1: Clone the Repository

git clone [https://github.com/Anmols243/Gemini-Ollama-Chatbot.git](https://github.com/Anmols243/Gemini-Ollama-Chatbot.git)
cd Gemini-Ollama-Chatbot


Step 2: Set Up Environment with Conda

We will create a clean, central environment and install all dependencies (Gemini, Streamlit, Ollama) into it.

Create the Environment:

conda create --name langchain-dev python=3.10 pip


Activate the Environment:

conda activate langchain-dev


Install dependencies:

pip install -r requirements.txt


Step 3: Configure Secrets and API Keys

Create a file named .env in the root directory.

Obtain your API keys and paste them into the .env file:

Variable

Value Source

Purpose

GEMINI_API_KEY

Get key from Google AI Studio

Runs the cloud model (gemini_app.py).

LANGSMITH_API_KEY

Get key from LangSmith Settings

Enables application tracing (optional).

LANGSMITH_TRACING

true

Enables tracing for all runs.

LANGSMITH_PROJECT

Chatbot-Dual-LLM

Project name for LangSmith tracking.

Step 4: Run the Applications

A. Run the Gemini (Cloud) App:

Ensure the langchain-dev environment is active, and launch the file:

streamlit run chatbot/gemini_app.py


B. Run the Ollama (Local) App:

Pull the Model: Open a separate terminal and ensure the model is downloaded locally:

ollama pull llama2


Start the Server: Ensure the Ollama server is running (usually automatic after installation).

Launch the App:

streamlit run chatbot/llamaapp.py
