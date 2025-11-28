import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from operator import itemgetter
import time

from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.environ['GROQ_API_KEY']

if "vector" not in st.session_state:
    st.session_state.embeddings = OllamaEmbeddings(model="mxbai-embed-large")
    st.session_state.loader = WebBaseLoader("https://docs.langchain.com/langsmith/home")
    st.session_state.docs = st.session_state.loader.load()

    st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    st.session_state.final_documnets = st.session_state.text_splitter.split_documents(st.session_state.docs[:50])
    st.session_state.vectors = FAISS.from_documents(st.session_state.final_documnets, st.session_state.embeddings)

st.title("ChatGroq Demo")
llm = ChatGroq(groq_api_key=groq_api_key, model="llama-3.3-70b-versatile")
prompt = ChatPromptTemplate.from_template(
"""
Answer the questions based on the provided context only.
Please provide the most accurate response based on the question.

Context:
{context}

Question:
{input}
"""
)

retriever = st.session_state.vectors.as_retriever()
rag_chain = (
    RunnablePassthrough.assign(
        context=itemgetter("input") | retriever
    )
    | prompt
    | llm
)

prompt = st.text_input("Input your prompt here")

if prompt:
    start=time.process_time()
    response=rag_chain.invoke({"input":prompt})
    print("Response Time: ", time.process_time() - start)
    st.write(response.content)