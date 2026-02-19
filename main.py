import ollama

# Conversation memory
messages = [
    {
        "role": "system",
        "content": "You are a helpful personal AI assistant. Keep responses concise."
    }
]

print("AI Agent started. Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    # Add user message to memory
    messages.append({
        "role": "user",
        "content": user_input
    })

    # Send full conversation to model
    response = ollama.chat(
        model="mistral",
        messages=messages
    )

    assistant_reply = response["message"]["content"]

    print("\nAI:", assistant_reply, "\n")

    # Add assistant reply to memory
    messages.append({
        "role": "assistant",
        "content": assistant_reply
    })
