import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55

# Colors
WHITE = (255, 255, 255)
LINE_COLOR = (28, 170, 156)
CIRCLE_COLOR = (242, 85, 96)
CROSS_COLOR = (28, 170, 156)
BG_COLOR = (28, 170, 156)
BUTTON_COLOR = (28, 170, 156)
TEXT_COLOR = (255, 255, 255)
GAME_OVER_COLOR = (239, 231, 200)

# Initialize the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Game board
board = [[None, None, None],
         [None, None, None],
         [None, None, None]]

# Player and AI symbols
PLAYER_X = "X"
PLAYER_O = "O"

# Game state
current_player = PLAYER_X
game_over = False


def draw_lines():
    # Draw the grid lines
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (WIDTH, 200), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (WIDTH, 400), LINE_WIDTH)


def draw_figures():
    # Draw the X and O symbols on the board
    for row in range(3):
        for col in range(3):
            if board[row][col] == PLAYER_X:
                pygame.draw.line(screen, CROSS_COLOR, (col * 200 + 50, row * 200 + 50), (col * 200 + 150, row * 200 + 150), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * 200 + 150, row * 200 + 50), (col * 200 + 50, row * 200 + 150), CROSS_WIDTH)
            elif board[row][col] == PLAYER_O:
                pygame.draw.circle(screen, CIRCLE_COLOR, (col * 200 + 100, row * 200 + 100), CIRCLE_RADIUS, CIRCLE_WIDTH)


def check_winner(player):
    # Check for a winner (horizontal, vertical, and diagonal)
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == player:
            pygame.draw.line(screen, GAME_OVER_COLOR, (0, row * 200 + 100), (WIDTH, row * 200 + 100), LINE_WIDTH)
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            pygame.draw.line(screen, GAME_OVER_COLOR, (col * 200 + 100, 0), (col * 200 + 100, HEIGHT), LINE_WIDTH)
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        pygame.draw.line(screen, GAME_OVER_COLOR, (0, 0), (WIDTH, HEIGHT), LINE_WIDTH)
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        pygame.draw.line(screen, GAME_OVER_COLOR, (0, HEIGHT), (WIDTH, 0), LINE_WIDTH)
        return True
    return False


def check_draw():
    # Check for a draw (no empty spaces left)
    for row in range(3):
        for col in range(3):
            if board[row][col] is None:
                return False
    return True


def minimax(board, depth, maximizing_player):
    # Minimax algorithm to choose the best move for AI
    winner = None
    if check_winner(PLAYER_X):
        winner = PLAYER_X
    elif check_winner(PLAYER_O):
        winner = PLAYER_O

    if winner == PLAYER_X:
        return -1
    elif winner == PLAYER_O:
        return 1
    elif check_draw():
        return 0

    if maximizing_player:
        best_score = -math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] is None:
                    board[row][col] = PLAYER_O
                    score = minimax(board, depth + 1, False)
                    board[row][col] = None
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] is None:
                    board[row][col] = PLAYER_X
                    score = minimax(board, depth + 1, True)
                    board[row][col] = None
                    best_score = min(score, best_score)
        return best_score


def ai_move():
    # Make the best move for the AI
    best_score = -math.inf
    move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] is None:
                board[row][col] = PLAYER_O
                score = minimax(board, 0, False)
                board[row][col] = None
                if score > best_score:
                    best_score = score
                    move = (row, col)
    return move


def restart_game():
    global board, current_player, game_over
    board = [[None, None, None],
             [None, None, None],
             [None, None, None]]
    current_player = PLAYER_X
    game_over = False
    screen.fill(BG_COLOR)
    draw_lines()


# Main game loop
screen.fill(BG_COLOR)
draw_lines()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if not game_over:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX = event.pos[0]
                mouseY = event.pos[1]

                clicked_row = mouseY // 200
                clicked_col = mouseX // 200

                if board[clicked_row][clicked_col] is None:
                    board[clicked_row][clicked_col] = current_player
                    if check_winner(current_player):
                        game_over = True
                    elif check_draw():
                        game_over = True
                    current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X

        if current_player == PLAYER_O and not game_over:
            row, col = ai_move()
            board[row][col] = PLAYER_O
            if check_winner(PLAYER_O):
                game_over = True
            elif check_draw():
                game_over = True
            current_player = PLAYER_X

        draw_figures()
        pygame.display.update()

    if game_over:
        pygame.time.wait(3000)
        restart_game()
        draw_lines()
        pygame.display.update()
