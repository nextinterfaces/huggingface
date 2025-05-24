# Redis Langcache Embedding Example

This example demonstrates how to use the `redis/langcache-embed-v1` model for generating sentence embeddings and calculating semantic similarities.

## About the Model

The [redis/langcache-embed-v1](https://huggingface.co/redis/langcache-embed-v1) model is:
- Based on Alibaba-NLP/gte-modernbert-base
- Fine-tuned on the Quora dataset
- Outputs 768-dimensional embeddings
- Optimized for semantic textual similarity and caching
- Maximum sequence length: 8192 tokens
- Achieves 0.90 cosine accuracy on binary classification

## Quick Start

1. Make sure you're in the `langcache-embed-v1` directory:
```bash
cd langcache-embed-v1
```

2. Run the example:
```bash
./run.sh
```

## Manual Setup (if needed)

If you prefer to set up manually:

1. Create a virtual environment:
```bash
python3 -m venv .venv
```

2. Activate the virtual environment:
```bash
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install sentence-transformers
```

4. Run the example:
```bash
python langcache_example.py
```

## Example Output

The script outputs:
- Model loading confirmation
- List of input sentences
- Embedding shape (3, 768)
- Sample of embedding values
- Similarity matrix showing how similar each sentence is to every other sentence

## Model Performance

Binary Classification Metrics:
- Cosine Accuracy: 0.90
- Cosine F1: 0.87
- Cosine Precision: 0.84
- Cosine Recall: 0.90
- Cosine AP: 0.92

## References

- [Model on Hugging Face](https://huggingface.co/redis/langcache-embed-v1)
- [Sentence Transformers Documentation](https://www.sbert.net/) 