from openai import OpenAI

# Best practice: set OPENAI_API_KEY in your environment instead of hardcoding
client = OpenAI(api_key="YOUR_KEY")

completion = client.chat.completions.create(
    model="gpt-4o-mini",  # change to a valid available model
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud."},
        {"role": "user", "content": "what are numbers?"}
    ]
)

print(completion.choices[0].message.content)
