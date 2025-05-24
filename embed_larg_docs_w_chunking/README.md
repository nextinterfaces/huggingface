# Document Chunking and Embedding Example

A demonstration of how to handle large documents by breaking them into chunks, embedding each chunk, and combining the embeddings. This script shows how to:
- Break long text into sentences using NLTK
- Generate embeddings for each sentence using a powerful model
- Combine sentence embeddings into a document-level representation

## Setup

1. Install dependencies:
```bash
pip install sentence-transformers nltk
python3 -c "import nltk; nltk.download('punkt')"
```

## How it Works

1. Uses the `all-mpnet-base-v2` model (one of the best performing models on many tasks)
2. Breaks text into sentences using NLTK's sentence tokenizer
3. Generates embeddings for each sentence
4. Uses mean pooling to create a single document embedding

## Example

Input text:
```python
"""Redis is fast. Redis supports vector similarity search. 
It is widely used for real-time applications in production. 
Hugging Face models are often used in conjunction with Redis for AI services."""
```

The script:
1. Splits this into individual sentences
2. Generates embeddings for each sentence
3. Combines them into a single document embedding
4. Outputs the shape of the final embedding (should be a vector of size 768)

## Use Cases

This approach is useful for:
- Processing long documents that exceed model token limits
- Creating document-level embeddings for similarity search
- Maintaining semantic meaning across longer texts
- Building document retrieval systems 