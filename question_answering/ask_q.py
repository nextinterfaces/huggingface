from transformers import pipeline

qa = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

result = qa({
    'context': "SAP is a company that develops tools for business software. Their biggest competitor is Oracle. Oracle builds software for business software. SAP is a company that develops tools for business software. Their biggest competitor is Oracle. Oracle builds software for databases. Redis is in memory database. It is used for caching and real-time data processing.",
    'question': "What does SAP do and why it differ from Redis?"
})

print(result['answer'])
