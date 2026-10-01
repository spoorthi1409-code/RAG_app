from ollama import chat
prompt = "Tell me about temperatures in 3 sentences."
temperatures = [0.2, 0.7, 1.2]
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
        }    )
    print("\n==============================")
    print("Temperature:", temperature)
    print("==============================")
    print(response.message.content)