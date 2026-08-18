# DocMind AI

DocMind AI is a Retrieval-Augmented Generation (RAG) system designed to answer questions from trusted documents.

## Features

- Document loading

- Text chunking

- Embedding generation

- ChromaDB vector storage

- Similarity-based information retrieval

- Context-based answer generation

- Evaluation using 10 test questions

- Latency measurement

- Accuracy measurement

- Health check API

- Document upload API

## Architecture

The system follows this pipeline:

Documents

↓

Document Loading

↓

Text Chunking

↓

Embeddings

↓

ChromaDB

↓

Similarity Retrieval

↓

Context

↓

Answer Generation

## Technologies Used

- Python

- FastAPI

- LangChain Text Splitters

- Sentence Transformers

- ChromaDB

- React

- Vite

## Project Structure


DocMind-AI/

│

├── app/

│   ├── rag\_pipeline.py

│   ├── retriever.py

│   └── generator.py

│

├── backend/

│   └── main.py

│

├── data/

│   ├── documents/

│   └── chroma\_db/

│

├── evaluation/

│   ├── evaluate.py

│   ├── questions.json

│   └── results.json

│

├── frontend/

│

├── .venv/

└── README.md

