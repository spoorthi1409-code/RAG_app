from ollama import chat
from datetime import datetime
# System personality
system_message = {
    "role": "system",
    "content": "You are Anuska AI, a friendly and helpful AI assistant."
}
messages = [system_message]
print("=" * 40)
print("🤖 ANUSKA AI")
print("=" * 40)
print("Type '/personality' to change personality")
print("Type 'exit' to close")
print("=" * 40)
while True:
    question = input("\n👤 You: ").strip()
    if not question:
        continue
    # Exit
    if question.lower() == "exit":
        print("🤖 Anuska: Goodbye! 👋")
        break
    # Change personality
    if question.lower() == "/personality":
        new_personality = input("🎭 Type the personality: ").strip()
        if new_personality:
            system_message = {
                "role": "system",
                "content": new_personality
            }
            messages = [system_message]
            print("✅ System message reset successfully!")
            print("🤖 Anuska: Personality updated.")
        continue
    # Add user message
    messages.append({
        "role": "user",
        "content": question
    })
    try:
        response = chat(
            model="llama3.2",
            messages=messages
        )
        answer = response.message.content
        time = datetime.now().strftime("%H:%M:%S")
        print(f"\n🤖 Anuska [{time}]:")
        print(answer)
        messages.append({
            "role": "assistant",
            "content": answer
        })
    except Exception as e:
        print(f"❌ Error: {e}")