# Failure Cases

## Failure Case 1 — Empty Retrieval

Question:
What is the capital of Japan?

Expected behavior:
The system should not invent an answer because the information is not present in the uploaded document.

Expected result:
The system should respond that the information is not available in the provided documents.

Lesson:
The RAG system should avoid hallucinating when relevant information cannot be retrieved.

## Failure Case 2 — Irrelevant Question

Question:
How do I bake a chocolate cake?

Expected behavior:
The system should recognize that the uploaded document does not contain information about baking.

Expected result:
The system should state that the answer is not available in the provided documents.

Lesson:
The system should rely only on retrieved document information instead of generating unsupported answers.
