from transformers import pipeline

qa = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

result = qa({
    'context': "Hugging Face is a company that develops tools for natural language processing.",
    'question': "What does Hugging Face do?"
})

print(result['answer'])
