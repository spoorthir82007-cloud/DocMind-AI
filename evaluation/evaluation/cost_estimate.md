# Cost Estimate

The project uses an embedding model locally for document retrieval.

Embedding generation is performed locally, so there is no per-request API cost for embeddings.

Answer generation uses the configured language model API.

The exact cost per request depends on the model, input tokens, output tokens, and current API pricing.

For this evaluation, cost should be calculated as:

Cost per request =
(input tokens × input price) +
(output tokens × output price)
