import os
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores.cassandra import Cassandra
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
import cassio
from dotenv import load_dotenv
from operator import itemgetter
import bs4
import streamlit as st
import time
from langchain_core.runnables import RunnablePassthrough,  RunnableLambda
load_dotenv()


groq_api_key = os.environ["GROQ_API_KEY"]
astra_db_tok = os.environ["ASTRA_DB_TOKEN"]
astra_db_id = os.environ["ASTRA_DB_ID"]
astra_db_ep = os.environ["ASTRA_DB_ENDPOINT"]

if "astra" not in st.session_state:

    cassio.init(token=astra_db_tok, 
                database_id=astra_db_id,
                )
    
    st.session_state.embeddings = HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-en-v1.5",
        model_kwargs={"device":"cpu"},
        encode_kwargs={'normalize_embeddings': True})
    
    st.session_state.loader = WebBaseLoader(web_path=("https://lilianweng.github.io/posts/2023-06-23-agent/"),
                       bs_kwargs=dict(parse_only=bs4.SoupStrainer(
                           class_=("post-title","post-content","post-header")
                       )))
    st.session_state.docs = st.session_state.loader.load()

    st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
    st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.docs)
    st.session_state.astra_db = Cassandra(embedding=st.session_state.embeddings,
                                          table_name="wl_app",
                                          )
    
st.title("Application Demo")
llm = ChatGroq(groq_api_key=groq_api_key,
               model="openai/gpt-oss-120b")
retriever = st.session_state.astra_db.as_retriever()

prompt = ChatPromptTemplate.from_template("""
Answer the following question based only on the provided context.
Think step by step before providinga detailed answer

Context:
{context}

Question:
{input} 
                                            
Give ONLY the final answer. Do NOT include:
- Explanation
- Context
- Thinking
- Extra sections
- Markdown headers                                                                                                                           
""")

def format_docs(docs):
    return "\n\n".join(d.page_content for d in docs)

rag_chain = (
    RunnablePassthrough.assign(
        context=itemgetter("input") 
        | retriever
        | RunnableLambda(format_docs)
    )  
    | prompt
    | llm
)

query = st.text_input("Write your question here")

if query:
    start = time.process_time()
    response = rag_chain.invoke({"input": query})
    print("Response Time: ", time.process_time() - start)
    st.write(response.content if hasattr(response, "content") else response)