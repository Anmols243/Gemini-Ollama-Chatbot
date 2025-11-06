from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama

import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["LANGSMITH_API_KEY"]=os.getenv("LANGSMITH_API_KEY")
os.environ["LANGCHAIN_TRACING"]= "true"

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user's queries"),
        ("user","Question:{question}")
    ]
)

st.title("LangChain with llama2")
input_text = st.text_input("Search the topic you want")

llm = ChatOllama(model="llama2")
output_parser = StrOutputParser()

chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))