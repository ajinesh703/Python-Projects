import pygame
import random

# Initialize pygame
pygame.init()

# Set up display
width, height = 600, 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Paddle variables
paddle_width, paddle_height = 10, 100
paddle_speed = 7

# Ball variables
ball_size = 10
ball_speed_x = 3 * random.choice((-1, 1))
ball_speed_y = 3 * random.choice((-1, 1))

# Scores
player_score, opponent_score = 0, 0

# Create paddles and ball
player = pygame.Rect(width - 20, height // 2 - paddle_height // 2, paddle_width, paddle_height)
opponent = pygame.Rect(10, height // 2 - paddle_height // 2, paddle_width, paddle_height)
ball = pygame.Rect(width // 2 - ball_size // 2, height // 2 - ball_size // 2, ball_size, ball_size)

# Font
font = pygame.font.Font(None, 40)

# Function to draw paddles, ball, and score
def draw():
    win.fill(black)
    pygame.draw.rect(win, white, player)
    pygame.draw.rect(win, white, opponent)
    pygame.draw.ellipse(win, white, ball)
    pygame.draw.aaline(win, white, (width // 2, 0), (width // 2, height))

    # Display scores
    player_text = font.render(f"{player_score}", True, white)
    win.blit(player_text, (width // 2 + 20, 20))
    opponent_text = font.render(f"{opponent_score}", True, white)
    win.blit(opponent_text, (width // 2 - 40, 20))

    pygame.display.flip()

# Function to handle ball movement and collisions
def ball_movement():
    global ball_speed_x, ball_speed_y, player_score, opponent_score

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= height:
        ball_speed_y *= -1

    if ball.left <= 0:
        player_score += 1
        reset_ball()
    if ball.right >= width:
        opponent_score += 1
        reset_ball()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

# Function to reset the ball
def reset_ball():
    global ball_speed_x, ball_speed_y
    ball.center = (width // 2, height // 2)
    ball_speed_x *= random.choice((-1, 1))
    ball_speed_y *= random.choice((-1, 1))

# Function to handle player movement
def player_movement(keys):
    if keys[pygame.K_UP] and player.top > 0:
        player.y -= paddle_speed
    if keys[pygame.K_DOWN] and player.bottom < height:
        player.y += paddle_speed

# Function to handle opponent movement (simple AI)
def opponent_movement():
    if opponent.top < ball.y:
        opponent.y += paddle_speed
    if opponent.bottom > ball.y:
        opponent.y -= paddle_speed

# Main game loop
run = True
clock = pygame.time.Clock()

while run:
    clock.tick(60)  # FPS

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Player input
    keys = pygame.key.get_pressed()
    player_movement(keys)
    opponent_movement()
    ball_movement()

    draw()

pygame.quit()
