import google.generativeai as genai

# Initialize Gemini
genai.configure(api_key="YOUR_API_KEY_HERE")

# Create the Generative Model
model = genai.GenerativeModel('gemini-pro')

# Initialize the chat session
chat = model.start_chat(history=[])

def chat_with_gemini():
    print("👋 Welcome to Gemini Chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("🚪 Exiting... Have a great day!")
            break
        try:
            response = chat.send_message(user_input)
            print(f"Gemini: {response.text}")
        except Exception as e:
            print(f"❗ Error: {str(e)}")
            break

if __name__ == "__main__":
    chat_with_gemini()
