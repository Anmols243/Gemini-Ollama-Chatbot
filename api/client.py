import requests
import streamlit as st

def get_gemini(input_text):
    response=requests.post("http://localhost:8000/essay/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']['content']

def get_ollama(input_text):
    response=requests.post("http://localhost:8000/poem/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']['content']                   

st.title('Langchain')
input_text1=st.text_input("Write an essasy on...")
input_text2=st.text_input("Write a poem on...")

if input_text1:
    st.write(get_gemini(input_text1))

if input_text2:
    st.write(get_ollama(input_text2))
   