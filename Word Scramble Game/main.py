import random

WORDS = ["python", "coding", "algorithm", "function", "variable",
         "keyboard", "computer", "program", "syntax", "compile"]

def scramble_word(word):
    word_letters = list(word)
    random.shuffle(word_letters)
    return "".join(word_letters)

def play_game():
    score = 0
    while True:
        word = random.choice(WORDS)
        scrambled = scramble_word(word)
        print(f"\nScrambled word: {scrambled}")
        while True:
            guess = input("Your guess (or 'q' to quit): ").strip().lower()
            if guess == "q":
                print(f"Final score: {score}")
                return
            if guess == word:
                print("Correct!")
                score += 1
                break
            else:
                print("Wrong, try again.")

if __name__ == "__main__":
    play_game()
