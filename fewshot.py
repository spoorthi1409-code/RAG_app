from ollama import chat

response = chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": "Review: The movie was amazing. Great acting, beautiful visuals, and an excellent story.\nSentiment: Positive"
        },
        {
            "role": "user",
            "content": "Review: The story was boring and the acting was poor. I did not enjoy the movie.\nSentiment: Negative"
        },
        {
            "role": "user",
            "content": "Review: The movie was okay. The story was average and the acting was decent.\nSentiment: Neutral"
        },
        {
            "role": "user",
            "content": "Review: The movie had excellent music and the actors gave wonderful performances. I really enjoyed it.\nSentiment:"
        }
    ]
)

print("Movie Review Sentiment:")
print(response.message.content)