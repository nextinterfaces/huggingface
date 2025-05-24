from sentence_transformers import SentenceTransformer

def main():
    # Load the Redis langcache model
    print("Loading Redis langcache-embed-v1 model...")
    model = SentenceTransformer('redis/langcache-embed-v1')
    print("Model loaded successfully!")

    # Example sentences from Redis documentation
    sentences = [
        'Will the value of Indian rupee increase after the ban of 500 and 1000 rupee notes?',
        'What will be the implications of banning 500 and 1000 rupees currency notes on Indian economy?',
        "Are Danish Sait's prank calls fake?"
    ]

    print("\nGenerating embeddings for sentences:")
    for i, sentence in enumerate(sentences, 1):
        print(f"{i}. {sentence}")

    # Generate embeddings
    embeddings = model.encode(sentences)

    # Print shape and embeddings
    print(f"\nEmbeddings shape: {embeddings.shape}")  # Should be (3, 768) for this model
    print("\nFirst few dimensions of each embedding:")
    for i, embedding in enumerate(embeddings, 1):
        print(f"\nSentence {i} (first 10 dimensions):")
        print(embedding[:10])

    # Calculate similarity between embeddings
    similarities = model.similarity(embeddings, embeddings)
    print("\nSimilarity matrix:")
    for i in range(len(sentences)):
        for j in range(len(sentences)):
            print(f"Similarity between sentence {i+1} and {j+1}: {similarities[i][j]:.4f}")

if __name__ == "__main__":
    main() 