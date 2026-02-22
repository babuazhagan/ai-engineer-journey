import ollama
import json
import os

MEMORY_FILE = "memory.json"

# Permanent persona (never changes)
SYSTEM_PERSONA = {
    "role": "system",
    "content": (
        "You are a concise, practical personal AI assistant. "
        "You help with learning, building projects, and problem solving. "
        "You remember user preferences when relevant."
    )
}

# How many recent messages to keep in context
MAX_HISTORY = 8


def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return []


def save_memory(messages):
    with open(MEMORY_FILE, "w") as f:
        json.dump(messages, f, indent=2)


def get_context(messages):
    """
    Returns persona + last N messages
    """
    return [SYSTEM_PERSONA] + messages[-MAX_HISTORY:]


# Load full history (for persistence)
full_history = load_memory()

print("Persistent AI Agent started. Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    full_history.append({
        "role": "user",
        "content": user_input
    })

    context = get_context(full_history)

    response = ollama.chat(
        model="mistral",
        messages=context
    )

    assistant_reply = response["message"]["content"]

    print("\nAI:", assistant_reply, "\n")

    full_history.append({
        "role": "assistant",
        "content": assistant_reply
    })

    save_memory(full_history)