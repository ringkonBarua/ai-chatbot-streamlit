import os
from openai import OpenAI

# API key environment থেকে নিন
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("বাংলা AI Chatbot শুরু হলো (শেষ করতে 'exit' বা 'quit' লিখুন)\n")

# কথোপকথন মেমরি
conversation = [
    {"role": "system", "content": "তুমি একজন সহায়ক বাংলা সহকারী, সব উত্তর বাংলায় দিবে।"}
]

while True:
    user_input = input("আপনি: ")

    if user_input.lower() in ["exit", "quit"]:
        print("চ্যাট শেষ হলো। ধন্যবাদ!")
        break

    conversation.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4o-mini",   # হালকা ও দ্রুত মডেল
        messages=conversation
    )

    bot_reply = response.choices[0].message.content
    print("চ্যাটবট:", bot_reply)

    conversation.append({"role": "assistant", "content": bot_reply})
