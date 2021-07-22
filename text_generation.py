from transformers import pipeline

text_generator_ENG = pipeline("text-generation",model="xlnet-base-cased")
print(text_generator_ENG("Hello how are ", max_length=50, do_sample=False))

text_generator_AR = pipeline("text-generation",model="mofawzy/gpt2-arabic-sentence-generator")
print(text_generator_AR("مرحبا كيف حالك", max_length=50, do_sample=False))