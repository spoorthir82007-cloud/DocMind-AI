\# DocMind AI



DocMind AI is a Retrieval-Augmented Generation (RAG) system designed to answer questions from trusted documents.



\## Features



\- Document loading

\- Text chunking

\- Embedding generation

\- ChromaDB vector storage

\- Similarity-based information retrieval

\- Context-based answer generation

\- Evaluation using 10 test questions

\- Latency measurement

\- Accuracy measurement

\- Health check API

\- Document upload API



\## Architecture



The system follows this pipeline:



Documents

&#x20;  ↓

Document Loading

&#x20;  ↓

Text Chunking

&#x20;  ↓

Embeddings

&#x20;  ↓

ChromaDB

&#x20;  ↓

Similarity Retrieval

&#x20;  ↓

Context

&#x20;  ↓

Answer Generation



\## Technologies Used



\- Python

\- FastAPI

\- LangChain Text Splitters

\- Sentence Transformers

\- ChromaDB

\- React

\- Vite



\## Project Structure



```text

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
## Evaluation Results

The system was evaluated using 10 question-answer test cases.

- Tests: 10
- Passed: 10
- Accuracy: 100%
- Average latency: 0.9908 seconds

Detailed evaluation results are available in `evaluation/results.json`.

