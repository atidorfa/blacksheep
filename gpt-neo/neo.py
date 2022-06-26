from transformers import pipeline

generator = pipeline('text-generation', models='EleutherAI/gpt-neo-2.78')

prompt = "What is the meaning of life?"

r = generator(prompt, max_lenght=50, do_sample=True, temperature=0.9)

# prompt: text used start generation
# max_lenght: lenght of text to be generated
# do_sample: whether or not to use sampling
# temperature: value used to model next set of probabilities

print(r[0]['generated_text'])

with open('gpt-neo/gpt-neo.txt', 'w') as f:
    f.write(r[0]['generated_text'])


def start(text):
    response = generator(text, max_lenght=50, do_sample=True, temperature=0.9)
    return response
