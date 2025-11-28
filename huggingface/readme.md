📘 HuggingFace RAG App

A Retrieval-Augmented Generation (RAG) pipeline built using LangChain, FAISS, HuggingFace Inference API, and U.S. Census PDF documents.
This project demonstrates how to load PDFs, chunk them, embed them, build a vectorstore, and query them using a HuggingFace LLM.

🚀 Features
✅ PDF Loader

Loads multiple PDFs from the us_census/ directory using PyPDFDirectoryLoader.

✅ Smart Chunking

Splits documents into overlapping chunks using
RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200).

✅ Vectorstore with FAISS

Efficient similarity search using FAISS and HuggingFace sentence embeddings.

✅ RAG Chain

Combines:

a retriever

a custom prompt

a HuggingFace LLM
using LangChain’s RunnablePassthrough.

✅ HuggingFace Inference LLM

Works with any HF text-generation model like:
meta-llama/Llama-3.1-8B-Instruct

✅ Clean, simple code in a Jupyter Notebook

Easy to follow, modify, and extend.