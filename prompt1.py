from ollama import chat

response = chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": "Explain what Data Science is and why it is important. Answer in a simple 2-line paragraph."
        }
    ]
)

print(response.message.content)