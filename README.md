# DocMind AI

### Retrieval-Augmented Generation for Trusted Document Question Answering

DocMind AI is an end-to-end Retrieval-Augmented Generation (RAG) system designed to answer questions using information retrieved from trusted documents.

The project demonstrates document processing, text chunking, semantic embeddings, vector storage, similarity-based retrieval, and context-based answer generation.


## Overview

Large language models can sometimes generate information that is not supported by a user's documents.

DocMind AI follows a retrieval-first approach:

**Question → Retrieve Relevant Information → Provide Context → Generate Answer**

This approach helps ground generated responses in the information available in the document collection.


## Features

* Document loading
* Text chunking
* Semantic embedding generation
* ChromaDB vector storage
* Similarity-based information retrieval
* Context-based answer generation
* Configurable prompts
* Document upload API
* Health check API
* Automated evaluation
* Accuracy measurement
* Response latency measurement
* JSON-based evaluation results


## Architecture

text
                Trusted Documents
                       |
                       v
               Document Loading
                       |
                       v
                 Text Chunking
                       |
                       v
              Embedding Generation
                       |
                       v
                  ChromaDB
                Vector Storage
                       |
                       v
User Question ---> Similarity Retrieval
                       |
                       v
                Relevant Context
                       |
                       v
                Answer Generation
                       |
                       v
                  Final Answer



## RAG Pipeline

### 1. Document Loading

The system loads trusted source documents and prepares them for processing.

### 2. Text Chunking

Large documents are divided into smaller chunks so that relevant sections can be retrieved efficiently.

### 3. Embedding Generation

Document chunks are converted into numerical vector representations using a sentence-transformer embedding model.

### 4. Vector Storage

The generated embeddings are stored in ChromaDB for similarity-based search.

### 5. Information Retrieval

When a user asks a question, the retriever searches the vector database and identifies relevant document chunks.

### 6. Answer Generation

The retrieved information is provided as context to the answer-generation model, which generates the final response.

---

## Technology Stack

| Technology               | Purpose                              |
| ------------------------ | ------------------------------------ |
| Python                   | Core application logic               |
| FastAPI                  | Backend API                          |
| React                    | Frontend                             |
| Vite                     | Frontend development                 |
| Sentence Transformers    | Semantic embeddings                  |
| ChromaDB                 | Vector storage and similarity search |
| LangChain Text Splitters | Document chunking                    |
| Gemini API               | Answer generation                    |
| GitHub                   | Source-code hosting                  |

---

## Project Structure
text
DocMind-AI/
│
├── app/
│   ├── __init__.py
│   ├── embeddings.py
│   ├── generator.py
│   ├── main.py
│   ├── prompts.py
│   ├── rag_pipeline.py
│   └── retriever.py
│
├── backend/
│   └── main.py
│
├── data/
│   └── documents/
│       └── docmind_test.txt
│
├── evaluation/
│   ├── evaluate.py
│   ├── questions.json
│   └── results.json
│
├── README.md
└── .gitignore


## Evaluation

The system was evaluated using **10 question-answer test cases** to measure answer accuracy and response latency.

### Evaluation Results

| Metric           |             Result |
| ---------------- | -----------------: |
| Total test cases |             **10** |
| Passed           |             **10** |
| Pass rate        |           **100%** |
| Average latency  | **0.9908 seconds** |

### Evaluation Summary

text
==============================
Evaluation Summary
Tests: 10
Passed: 10
Accuracy: 100.0%
Average latency: 0.9908 seconds
==============================


Detailed evaluation results are available in:

evaluation/results.json



## Evaluation Method

For each test case:

1. A question is provided to the system.
2. Relevant document chunks are retrieved.
3. Retrieved context is passed to the answer generator.
4. A generated answer is produced.
5. The generated answer is compared with the expected answer.
6. An accuracy score is calculated.
7. Response latency is recorded.

The current evaluation uses a **word-overlap scoring method**.


## Limitations

* The evaluation dataset currently contains 10 test cases.
* The accuracy metric uses word-overlap scoring.
* The first request can have higher latency because the embedding model is initialized.
* Latency can vary depending on external model/API conditions.
* The current document collection is small.


## Future Improvements

* Larger and more diverse evaluation datasets
* Semantic evaluation metrics
* Retrieval precision and recall measurements
* Improved source and citation tracking
* Support for additional document formats
* Improved error and timeout handling
* Authentication and authorization
* Production deployment
* Monitoring and observability
* Automated testing and CI/CD


## Learning Outcomes

This project provided practical experience with:

* Retrieval-Augmented Generation
* Semantic embeddings
* Vector databases
* Similarity search
* Prompt engineering
* Document processing
* FastAPI
* React
* Evaluation methodology
* Performance measurement


## Project Status

**Completed Prototype**

The core RAG pipeline and automated evaluation workflow have been implemented and tested.

**Evaluation: 10/10 tests passed — 100% pass rate.**


## Author

**Spoorthi R.**

Computer Science and Engineering Student


## Repository

[DocMind AI on GitHub](https://github.com/spoorthir82007-cloud/DocMind-AI)
