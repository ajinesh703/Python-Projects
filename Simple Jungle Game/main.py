# Simple Jungle/Guessing game by Using Random Library
import random

# Game variables
player_position = 5  # Player starts at position 5 in a 1D jungle path
jungle_length = 10   # Length of the jungle path
score = 0

# Instructions
def display_instructions():
    print("Welcome to the Jungle Adventure!")
    print("Collect fruits (F) and avoid enemies (E).")
    print("Use 'L' to move left, 'R' to move right, and 'Q' to quit.")
    print(f"The jungle path is {jungle_length} steps long.")
    print("Good luck!")

# Display the jungle path
def display_jungle(player_pos, fruit_pos, enemy_pos):
    jungle = ["_" for _ in range(jungle_length)]

    if fruit_pos != -1:
        jungle[fruit_pos] = "F"  # Place fruit
    if enemy_pos != -1:
        jungle[enemy_pos] = "E"  # Place enemy
    jungle[player_pos] = "P"      # Place player

    print("".join(jungle))

# Main game loop
def jungle_game():
    global player_position, score

    fruit_position = random.randint(0, jungle_length - 1)
    enemy_position = random.randint(0, jungle_length - 1)

    while True:
        display_jungle(player_position, fruit_position, enemy_position)
        print(f"Score: {score}")

        # Player input
        move = input("Move (L/R/Q): ").strip().upper()

        if move == "Q":
            print("Thanks for playing! Your final score is:", score)
            break
        elif move == "L" and player_position > 0:
            player_position -= 1
        elif move == "R" and player_position < jungle_length - 1:
            player_position += 1
        else:
            print("Invalid move. Try again.")
            continue

        # Check for collisions
        if player_position == fruit_position:
            print("You collected a fruit!")
            score += 1
            fruit_position = random.randint(0, jungle_length - 1)
        elif player_position == enemy_position:
            print("You were caught by an enemy! Game over.")
            break

        # Randomize enemy and fruit positions
        if random.randint(0, 1):
            enemy_position = random.randint(0, jungle_length - 1)

# Start the game
display_instructions()
jungle_game()
