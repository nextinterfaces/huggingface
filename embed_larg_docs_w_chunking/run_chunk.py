from sentence_transformers import SentenceTransformer
from nltk.tokenize import sent_tokenize

model = SentenceTransformer('all-mpnet-base-v2')

long_text = """Redis is fast. Redis supports vector similarity search. 
It is widely used for real-time applications in production. 
Hugging Face models are often used in conjunction with Redis for AI services."""

# Break into sentences and embed
sentences = sent_tokenize(long_text)
sentence_embeddings = model.encode(sentences)

# Mean pooling
import numpy as np
document_embedding = np.mean(sentence_embeddings, axis=0)
print(document_embedding.shape)
