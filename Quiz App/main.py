import requests
import random
import threading
import time

def fetch_questions(category=9, difficulty="easy", num_questions=5):
    """Fetch quiz questions from the Open Trivia Database API."""
    url = f"https://opentdb.com/api.php?amount={num_questions}&category={category}&difficulty={difficulty}&type=multiple"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["results"]
    else:
        print("Failed to fetch questions from the API.")
        return []

def shuffle_options(correct_answer, incorrect_answers):
    """Shuffle the options for the question."""
    options = incorrect_answers + [correct_answer]
    random.shuffle(options)
    return options

def display_question(question_data, timer_event):
    """Display a question and handle user input with a timer."""
    question = question_data["question"]
    correct_answer = question_data["correct_answer"]
    incorrect_answers = question_data["incorrect_answers"]

    # Shuffle options
    options = shuffle_options(correct_answer, incorrect_answers)

    print(f"\nQuestion: {question}")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    # Start a timer
    user_answer = None

    def timer():
        nonlocal user_answer
        print("\nTime's up! Moving to the next question.")
        timer_event.set()

    timer_event.clear()
    timer_thread = threading.Timer(10.0, timer)
    timer_thread.start()

    while not timer_event.is_set():
        try:
            user_input = input("\nEnter the number of your choice (1-4): ")
            if user_input.isdigit() and 1 <= int(user_input) <= 4:
                user_answer = options[int(user_input) - 1]
                timer_event.set()
                break
            else:
                print("Invalid input. Please enter a number between 1 and 4.")
        except Exception:
            print("An error occurred. Try again.")

    timer_thread.cancel()
    return user_answer == correct_answer

def end_quiz():
    """Handle the end of the quiz with options to restart or exit."""
    while True:
        user_input = input("\nDo you want to restart the quiz? (R to restart, Y to exit): ").strip().lower()
        if user_input == 'r':
            return True
        elif user_input == 'y':
            print("Thank you for playing! Goodbye.")
            return False
        else:
            print("Invalid input. Please enter 'R' to restart or 'Y' to exit.")

def quiz_app():
    """Main function for the quiz app."""
    print("Welcome to the Quiz App!")
    print("You have 10 seconds to answer each question.")

    while True:
        # Fetch questions from the API
        category = 9  # General Knowledge
        difficulty = "easy"
        num_questions = 5
        questions = fetch_questions(category, difficulty, num_questions)

        if not questions:
            print("No questions available. Please try again later.")
            return

        # Start the quiz
        score = 0
        timer_event = threading.Event()

        for i, question_data in enumerate(questions, 1):
            print(f"\nQuestion {i} of {num_questions}:")
            if display_question(question_data, timer_event):
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer was: {question_data['correct_answer']}")

        print("\nQuiz over!")
        print(f"Your final score is {score}/{num_questions}.")

        # End quiz options
        if not end_quiz():
            break

if __name__ == "__main__":
    quiz_app()
