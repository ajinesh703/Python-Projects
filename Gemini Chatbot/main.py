import requests
import json

API_KEY = "Your API Key Here"
URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-lite:generateContent"

HEADERS = {
    "Content-Type": "application/json",
    "X-goog-api-key": API_KEY,
}

conversation_history = []

def chat(user_message):
    conversation_history.append({
        "role": "user",
        "parts": [{"text": user_message}]
    })

    payload = {"contents": conversation_history}

    response = requests.post(URL, headers=HEADERS, json=payload)

    if response.status_code != 200:
        print(f"[Error] API returned {response.status_code}: {response.text}")
        conversation_history.pop()
        return None

    data = response.json()
    reply = data["candidates"][0]["content"]["parts"][0]["text"]

    conversation_history.append({
        "role": "model",
        "parts": [{"text": reply}]
    })

    return reply

def main():
    print("=" * 50)
    print("       Gemini Terminal Chatbot")
    print("  Type 'exit' or 'quit' to stop")
    print("  Type 'clear' to reset conversation")
    print("=" * 50)
    print()

    while True:
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\nGoodbye!")
            break

        if not user_input:
            continue

        if user_input.lower() in ("exit", "quit"):
            print("Goodbye!")
            break

        if user_input.lower() == "clear":
            conversation_history.clear()
            print("[Conversation cleared]\n")
            continue

        reply = chat(user_input)
        if reply:
            print(f"\nGemini: {reply}\n")

if __name__ == "__main__":
    main()
