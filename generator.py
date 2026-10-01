from ollama import chat
prompt = "Tell me about temperatures in 3 sentences."
temperatures = [0.1, 0.5, 1.0]
for temperature in temperatures:
    response = chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        options={
            "temperature": temperature
        }
    )
    print("\n==============================")
    print("Temperature:", temperature)
    print("==============================")
    print(response.message.content)