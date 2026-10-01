from ollama import chat
question = "Explain how to solve a difficult problem in simple words."
# Role 1: Mathematics Teacher
response_teacher = chat(
    model="llama3.2",
    messages=[
        {
            "role": "system",
            "content": "You are a Mathematics Teacher. Explain concepts step-by-step with simple examples."
        },
        {
            "role": "user",
            "content": question
        }
    ]
)

# Role 2: Movie Director
response_director = chat(
    model="llama3.2",
    messages=[
        {
            "role": "system",
            "content": "You are a Movie Director. Explain things creatively using storytelling and movie examples."
        },
        {
            "role": "user",
            "content": question
        }
    ]
)

# Role 3: Lawyer
response_lawyer = chat(
    model="llama3.2",
    messages=[
        {
            "role": "system",
            "content": "You are a Lawyer. Explain things clearly, logically, and professionally."
        },
        {
            "role": "user",
            "content": question
        }
    ]
)

# Display responses
print("\n===== MATHEMATICS TEACHER =====")
print(response_teacher.message.content)

print("\n===== MOVIE DIRECTOR =====")
print(response_director.message.content)

print("\n===== LAWYER =====")
print(response_lawyer.message.content)