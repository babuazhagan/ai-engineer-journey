import ollama

prompt = input("Ask me anything: ")

response = ollama.chat(
    model='mistral',
    messages=[
        {'role': 'user', 'content': prompt}
    ]
)

print("\nAI says:\n")
print(response['message']['content'])