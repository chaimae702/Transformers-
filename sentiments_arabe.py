from transformers import pipeline

nlp = pipeline("sentiment-analysis",model="nlptown/bert-base-multilingual-uncased-sentiment")

result = nlp("I hate you")[0]
print(f"label: {result['label']}, with score: {round(result['score'], 4)}")

result = nlp("أحبك")[0]
print(f"label: {result['label']}, with score: {round(result['score'], 4)}")