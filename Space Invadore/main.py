import pygame
import random
import math

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Title and Icon
pygame.display.set_caption("Space Invaders")

# Player
player_img = pygame.Surface((64, 64))
player_img.fill((0, 255, 0))
player_x = 370
player_y = 480
player_x_change = 0

# Enemy
enemy_img = pygame.Surface((64, 64))
enemy_img.fill((255, 0, 0))
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemy_x.append(random.randint(0, 736))
    enemy_y.append(random.randint(50, 150))
    enemy_x_change.append(4)
    enemy_y_change.append(40)

# Bullet
bullet_img = pygame.Surface((8, 24))
bullet_img.fill((255, 255, 0))
bullet_x = 0
bullet_y = player_y
bullet_y_change = 10
bullet_state = "ready"  # "ready" - not visible, "fire" - moving

# Score
score_value = 0
font = pygame.font.Font(None, 36)

# Game Over
over_font = pygame.font.Font(None, 64)

def show_score(x, y):
    score = font.render(f"Score : {score_value}", True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over, (200, 250))

def player(x, y):
    screen.blit(player_img, (x, y))

def enemy(x, y, i):
    screen.blit(enemy_img, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 28, y))

def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.hypot(enemy_x - bullet_x, enemy_y - bullet_y)
    return distance < 27

# Game loop
running = True
while running:
    screen.fill((0, 0, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keydown events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -5
            if event.key == pygame.K_RIGHT:
                player_x_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)
        # Keyup events
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                player_x_change = 0

    # Player movement
    player_x += player_x_change
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    # Enemy movement
    for i in range(num_of_enemies):
        # Game Over
        if enemy_y[i] > 440:
            for j in range(num_of_enemies):
                enemy_y[j] = 2000
            game_over_text()
            break

        enemy_x[i] += enemy_x_change[i]
        if enemy_x[i] <= 0:
            enemy_x_change[i] = 4
            enemy_y[i] += enemy_y_change[i]
        elif enemy_x[i] >= 736:
            enemy_x_change[i] = -4
            enemy_y[i] += enemy_y_change[i]

        # Collision
        if is_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y):
            bullet_y = player_y
            bullet_state = "ready"
            score_value += 1
            enemy_x[i] = random.randint(0, 736)
            enemy_y[i] = random.randint(50, 150)

        enemy(enemy_x[i], enemy_y[i], i)

    # Bullet movement
    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change
    if bullet_y <= 0:
        bullet_y = player_y
        bullet_state = "ready"

    player(player_x, player_y)
    show_score(10, 10)
    pygame.display.update()
