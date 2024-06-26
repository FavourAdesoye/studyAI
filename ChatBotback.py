import google.generativeai as genai

API_KEY = "___"
genai.configure(
    api_key=API_KEY
)

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

while(True):
    question = input("You: ")

    if (question.strip() == ''):
        break

    response = chat.send_message(question)
    print("\n")
    print(f"StudyAI: {response.text}")
    print("\n")