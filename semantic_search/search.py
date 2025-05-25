from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

# Corpus of documents (could come from a DB)
corpus = [
    "Redis is an in-memory data structure store.",
    "Transformers are state-of-the-art NLP models.",
    "Vector search finds similar documents based on embeddings."
]
corpus_embeddings = model.encode(corpus, convert_to_tensor=True)

# User query
query = "How do I use AI with fast document search?"
query_embedding = model.encode(query, convert_to_tensor=True)

# Compute cosine similarities
hits = util.semantic_search(query_embedding, corpus_embeddings, top_k=3)
for hit in hits[0]:
    print(f"Score: {hit['score']:.4f} - {corpus[hit['corpus_id']]}")
