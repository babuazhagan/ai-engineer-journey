import ollama

def summarize_text(text):
    response = ollama.chat(
        model='mistral',
        messages=[
            {
                'role': 'system',
                'content': (
                    "You are a precise summarization assistant. "
                    "Return exactly 5 bullet points. "
                    "Each bullet must start with a hyphen and a space. "
                    "No extra commentary."
                )
            },
            {
                'role': 'user',
                'content': text
            }
        ]
    )

    return response['message']['content']



if __name__ == "__main__":
    print("Paste text to summarize. Press Enter twice when done:\n")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    full_text = "\n".join(lines)

    summary = summarize_text(full_text)

    print("\n=== SUMMARY ===\n")
    print(summary)
