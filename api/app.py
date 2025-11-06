from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langserve import add_routes
import uvicorn
import os
from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()


app=FastAPI(
    title='Langchain Server',
    version='1.0',
    description='A simple API server'
)

model=ChatGoogleGenerativeAI(
    model= "gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"))

llm=ChatOllama(model="llama2")

prompt1= ChatPromptTemplate.from_template("Write me an essay about {topic} around 100-200 words")
prompt2= ChatPromptTemplate.from_template("Write me an poem about {topic} around 100 words")

essay_chain = prompt1|model
poem_chain = prompt2|llm

add_routes(
    app,
    essay_chain,
    path="/essay"
)

add_routes(
    app,
    poem_chain,
    path="/poem"
)

if __name__ == "__main__":
    uvicorn.run(app,host="localhost",port=8000)