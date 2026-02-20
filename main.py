import ollama
import json
import os

MEMORY_FILE = "memory.json"

# Load memory if exists
if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "r") as f:
        messages = json.load(f)
else:
    messages = [
        {
            "role": "system",
            "content": "You are a helpful personal AI assistant. Keep responses concise."
        }
    ]

print("Persistent AI Agent started. Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    response = ollama.chat(
        model="mistral",
        messages=messages
    )

    assistant_reply = response["message"]["content"]

    print("\nAI:", assistant_reply, "\n")

    messages.append({
        "role": "assistant",
        "content": assistant_reply
    })

    # Save memory after every turn
    with open(MEMORY_FILE, "w") as f:
        json.dump(messages, f, indent=2)