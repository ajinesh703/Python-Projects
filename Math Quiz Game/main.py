import tkinter as tk
import random
from functools import partial

# Initialize global variables
score = 0
time_left = 30
current_answer = 0
double_points_active = False

# Generate a random math question
def generate_question():
    global current_answer
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operation = random.choice(["+", "-", "*"])
    question = f"{num1} {operation} {num2}"
    current_answer = eval(question)
    return question

# Check the player's answer
def check_answer(entry, question_label, feedback_label, score_label):
    global score, double_points_active
    try:
        user_answer = int(entry.get())
        if user_answer == current_answer:
            points = 2 if double_points_active else 1
            score += points
            feedback_label.config(text=f"Correct! +{points} point(s)", fg="green")
        else:
            feedback_label.config(text="Incorrect!", fg="red")
    except ValueError:
        feedback_label.config(text="Enter a valid number!", fg="orange")

    # Update the score and display a new question
    score_label.config(text=f"Score: {score}")
    entry.delete(0, tk.END)
    question_label.config(text=generate_question())

# Activate the double points power-up
def activate_double_points(power_up_label):
    global double_points_active
    double_points_active = True
    power_up_label.config(text="Double Points Active!")
    power_up_label.after(5000, deactivate_double_points, power_up_label)

def deactivate_double_points(power_up_label):
    global double_points_active
    double_points_active = False
    power_up_label.config(text="")

# Skip the current question
def skip_question(question_label, feedback_label):
    feedback_label.config(text="Question Skipped!", fg="blue")
    question_label.config(text=generate_question())

# Countdown timer
def countdown(timer_label, question_label, entry, feedback_label):
    global time_left
    if time_left > 0:
        time_left -= 1
        timer_label.config(text=f"Time Left: {time_left}s")
        timer_label.after(1000, countdown, timer_label, question_label, entry, feedback_label)
    else:
        end_game(question_label, entry, feedback_label)

# End the game
def end_game(question_label, entry, feedback_label):
    question_label.config(text="Game Over!")
    entry.config(state="disabled")
    feedback_label.config(text=f"Final Score: {score}", fg="black")

# Main game function
def math_quiz_game():
    global time_left

    # Reset game variables
    time_left = 30
    global score
    score = 0

    # Create the main window
    root = tk.Tk()
    root.title("Math Quiz Duel")
    root.geometry("400x400")

    # Game title
    title_label = tk.Label(root, text="Math Quiz Duel", font=("Arial", 24))
    title_label.pack(pady=10)

    # Timer and score
    timer_label = tk.Label(root, text=f"Time Left: {time_left}s", font=("Arial", 16))
    timer_label.pack(pady=5)
    score_label = tk.Label(root, text=f"Score: {score}", font=("Arial", 16))
    score_label.pack(pady=5)

    # Question display
    question_label = tk.Label(root, text=generate_question(), font=("Arial", 18))
    question_label.pack(pady=10)

    # Answer input
    entry = tk.Entry(root, font=("Arial", 18))
    entry.pack(pady=10)
    entry.focus()

    # Feedback
    feedback_label = tk.Label(root, text="", font=("Arial", 14))
    feedback_label.pack(pady=10)

    # Buttons for actions
    check_button = tk.Button(root, text="Submit", font=("Arial", 14),
                             command=partial(check_answer, entry, question_label, feedback_label, score_label))
    check_button.pack(pady=5)

    skip_button = tk.Button(root, text="Skip", font=("Arial", 14),
                            command=partial(skip_question, question_label, feedback_label))
    skip_button.pack(pady=5)

    # Power-ups
    power_up_label = tk.Label(root, text="", font=("Arial", 14), fg="blue")
    power_up_label.pack(pady=10)

    double_points_button = tk.Button(root, text="Activate Double Points", font=("Arial", 14),
                                     command=partial(activate_double_points, power_up_label))
    double_points_button.pack(pady=5)

    # Start the countdown
    countdown(timer_label, question_label, entry, feedback_label)

    # Run the main loop
    root.mainloop()

# Run the game
math_quiz_game()
