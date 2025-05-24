# Hugging Face Sentence-Transformers Setup

This project demonstrates how to use Hugging Face sentence-transformers to generate vector embeddings in Python.

## Prerequisites

- Python 3.7 or higher
- pip package manager

## Setup

### 1. Create and Activate Virtual Environment

Create a Python virtual environment to isolate project dependencies:

```bash
python -m venv hf-env
```

Activate the virtual environment:

**Linux/Mac:**
```bash
source hf-env/bin/activate
```

**Windows:**
```bash
hf-env\Scripts\activate
```

### 2. Install Required Packages

Install the necessary Python packages:

```bash
pip install transformers sentence-transformers torch
```

### 3. Fix urllib3 Compatibility Issue

To avoid the `NotOpenSSLWarning` caused by urllib3 v2 requiring OpenSSL 1.1.1+, downgrade urllib3 to a version < 2:

```bash
pip install "urllib3<2"
```

## Usage

Once the setup is complete, you can start using sentence-transformers to generate embeddings:

```python
from sentence_transformers import SentenceTransformer

# Load a pre-trained model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Generate embeddings
sentences = ['This is an example sentence', 'Each sentence is converted']
embeddings = model.encode(sentences)

print(embeddings.shape)
```

## Troubleshooting

- If you encounter SSL warnings, ensure you've downgraded urllib3 as shown in step 3
- Make sure your virtual environment is activated before installing packages
- For GPU support, install the appropriate PyTorch version for your system

## Deactivating Environment

When you're done working on the project, deactivate the virtual environment:

```bash
deactivate
```