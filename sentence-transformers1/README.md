# Sentence Transformers Example

This project demonstrates how to use the `sentence-transformers` library to generate embeddings from text sentences.

## Setup

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
pip install transformers sentence-transformers torch  
```

## Usage

The example script `sentence-transformers1/sentence-transformers1.py` shows how to:
- Load a pre-trained sentence transformer model
- Generate embeddings for text sentences
- View the embedding dimensions and values

To run the script:
```bash
# Make sure you're using the virtual environment's Python
.venv/bin/python3 sentence-transformers1/sentence-transformers1.py
```

## Example Output

The script will output:
- The shape of the embeddings (2, 384) - representing 2 sentences with 384-dimensional embeddings each
- The actual embedding vectors for each sentence

## Troubleshooting

If you get a "ModuleNotFoundError: No module named 'sentence_transformers'" error:
1. Make sure you've activated the virtual environment
2. Ensure you're using the Python interpreter from the virtual environment (`.venv/bin/python3`)
3. Try reinstalling the package: `pip install sentence-transformers`

### Fix urllib3 Compatibility Issue

To avoid the `NotOpenSSLWarning` caused by urllib3 v2 requiring OpenSSL 1.1.1+, downgrade urllib3 to a version < 2:

```bash
pip install "urllib3<2"
```