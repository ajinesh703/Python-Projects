import os
import time
import random
import keyboard

WIDTH = 20
HEIGHT = 10
PLAYER_CHAR = "P"
OBSTACLE_CHAR = "X"
EMPTY_CHAR = "."

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def draw_board(player_pos, obstacles):
    clear_screen()
    for y in range(HEIGHT):
        row = ""
        for x in range(WIDTH):
            if (x, y) == player_pos:
                row += PLAYER_CHAR
            elif (x, y) in obstacles:
                row += OBSTACLE_CHAR
            else:
                row += EMPTY_CHAR
        print(row)

def get_player_move(pos):
    x, y = pos
    if keyboard.is_pressed('w') and y > 0:
        y -= 1
    if keyboard.is_pressed('s') and y < HEIGHT - 1:
        y += 1
    if keyboard.is_pressed('a') and x > 0:
        x -= 1
    if keyboard.is_pressed('d') and x < WIDTH - 1:
        x += 1
    return (x, y)

def update_obstacles(obstacles):
    updated = [(x, y + 1) for (x, y) in obstacles if y + 1 < HEIGHT]
    if random.random() < 0.3:
        updated.append((random.randint(0, WIDTH - 1), 0))
    return updated

def run_game():
    player = (WIDTH // 2, HEIGHT - 1)
    obstacles = []
    score = 0
    speed = 0.2

    while True:
        player = get_player_move(player)
        obstacles = update_obstacles(obstacles)
        draw_board(player, obstacles)

        if player in obstacles:
            print("\nGame Over!")
            print(f"Final Score: {score}")
            break

        score += 1
        speed = max(0.05, speed - 0.001)
        time.sleep(speed)

if __name__ == "__main__":
    print("Welcome to Terminal Dodge!")
    print("Use W A S D keys to move. Avoid the falling Xs.")
    print("Press Ctrl+C to quit.\nStarting in 2 seconds...")
    time.sleep(2)
    run_game()
