from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")
prompt = "In a future where AI governs society,"

result = generator(prompt, max_length=50, num_return_sequences=1)
print(result[0]['generated_text'])
