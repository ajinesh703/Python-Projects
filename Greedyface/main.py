import pandas as pd

# Load your emoji spreadsheet
df = pd.read_csv("emoji_reference.csv")

# Build emoji → meaning dictionary
emoji_data = {}
for _, row in df.iterrows():
    emoji_data[row["Emoji"]] = f"{row['Name']} — {row['Meaning']}"

# Build meaning → emoji dictionary (reverse lookup)
meaning_to_emoji = {}
for emoji, text in emoji_data.items():
    meaning_to_emoji[text.lower()] = emoji


def chatbot():
    print("Emoji Info Chatbot")
    print("Type an emoji to get its meaning.")
    print("Or type a word/meaning to get the matching emoji.")
    print("Type 'exit' to stop.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("Chatbot: Thank you for using the Emoji Info Chatbot!")
            break

        # Case 1: direct emoji input
        if user_input in emoji_data:
            print("Chatbot:", emoji_data[user_input])
            continue

        # Case 2: text meaning search
        query = user_input.lower()
        found = False

        # Search in the meaning text
        for emoji, description in emoji_data.items():
            if query in description.lower():
                print("Chatbot:", emoji, "→", description)
                found = True
                break

        if not found:
            print("Chatbot: No matching emoji or meaning found. Try another input.")


# Run it
chatbot()
