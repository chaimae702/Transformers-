from transformers import pipeline, AutoTokenizer

feature_extraction = pipeline('feature-extraction', model="distilroberta-base", tokenizer="distilroberta-base")
features = feature_extraction("HuggingFace is creating a tool that the community uses to solve NLP tasks.")
print(len(features[0]))