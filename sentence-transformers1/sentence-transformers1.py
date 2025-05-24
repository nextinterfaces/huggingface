from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

sentences = ["This is an example sentence", "Each sentence is converted"]

embeddings = model.encode(sentences)

print(embeddings.shape)  # (2, 384) for this model
print(embeddings)
