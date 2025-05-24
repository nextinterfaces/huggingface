# Semantic Search Example

A simple demonstration of semantic search using sentence transformers. The script shows how to:
- Encode a corpus of documents into embeddings
- Encode a query into the same vector space
- Find the most semantically similar documents using cosine similarity

## Quick Start

```bash
python3 search.py
```

## How it Works

1. Uses the `all-MiniLM-L6-v2` model to create embeddings
2. Maintains a small corpus of example documents about databases, AI, and search
3. Converts a user query into the same embedding space
4. Finds the top 2 most similar documents using semantic search
5. Displays similarity scores and matching documents

## Example Output

For the query "How do I use AI with fast document search?", it returns:
```
Score: 0.4834 - Vector search finds similar documents based on embeddings.
Score: 0.2742 - Transformers are state-of-the-art NLP models.
```

The higher scores indicate better semantic matches, regardless of exact word matches. 