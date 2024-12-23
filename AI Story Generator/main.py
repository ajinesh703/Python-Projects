import random
import tkinter as tk
from tkinter import messagebox
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# Initialize the model and tokenizer from Hugging Face
model_name = "gpt2"  # You can switch to other models like "EleutherAI/gpt-neo-2.7B" for better results
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Function to generate story using the Transformer model
def generate_story_part(prompt):
    try:
        # Encode the input text
        inputs = tokenizer.encode(prompt, return_tensors="pt")

        # Generate the story part
        outputs = model.generate(
            inputs, 
            max_length=200, 
            num_return_sequences=1, 
            no_repeat_ngram_size=2,
            temperature=0.7,
            top_p=0.9,
            top_k=50,
            pad_token_id=tokenizer.eos_token_id
        )

        # Decode the generated output
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        # Return only the generated part after the prompt
        return generated_text[len(prompt):].strip()
    except Exception as e:
        print(f"Error generating story: {e}")
        return "Sorry, there was an error generating the story part."

# Function to handle player's input
def add_player_input():
    player_input = input_box.get("1.0", "end-1c").strip()
    if player_input:
        story_text.insert(tk.END, f"Player: {player_input}\n")
        story_text.yview(tk.END)
        input_box.delete("1.0", tk.END)
        ai_response = generate_story_part(player_input)
        story_text.insert(tk.END, f"AI: {ai_response}\n\n")
        story_text.yview(tk.END)

        # Give the next challenge
        next_challenge = generate_challenge()
        challenge_label.config(text=f"Next Challenge: {next_challenge}")
    else:
        messagebox.showwarning("Input Error", "Please enter a part of the story.")

# Function to generate a random challenge
def generate_challenge():
    challenges = [
        "Write about a plot twist.",
        "Introduce a new character.",
        "Describe an unexpected event.",
        "Write a suspenseful moment.",
        "Introduce a new location.",
        "Write a dialogue between two characters.",
        "Add a moral or lesson."
    ]
    return random.choice(challenges)

# Function to initialize the game
def start_game():
    story_text.delete("1.0", tk.END)
    story_text.insert(tk.END, "The Infinite Story Begins!\n\n")
    challenge_label.config(text=f"Next Challenge: {generate_challenge()}")

# Setting up the Tkinter window
root = tk.Tk()
root.title("Infinite Story Generator")

# Game UI setup
frame = tk.Frame(root)
frame.pack(pady=20)

story_text = tk.Text(frame, width=80, height=20, wrap=tk.WORD)
story_text.pack()

challenge_label = tk.Label(root, text="Next Challenge: ", font=("Helvetica", 14))
challenge_label.pack(pady=10)

input_box = tk.Text(root, width=80, height=4, wrap=tk.WORD)
input_box.pack(pady=10)

submit_button = tk.Button(root, text="Submit Your Part", font=("Helvetica", 14), command=add_player_input)
submit_button.pack(pady=10)

start_button = tk.Button(root, text="Start New Story", font=("Helvetica", 14), command=start_game)
start_button.pack(pady=10)

# Start the game when the window opens
start_game()

# Run the Tkinter event loop
root.mainloop()
