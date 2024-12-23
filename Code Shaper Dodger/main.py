import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Shape Dodger")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Fonts
font = pygame.font.Font(None, 36)

# Clock
clock = pygame.time.Clock()

# Player settings
PLAYER_SIZE = 50
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT - PLAYER_SIZE - 10
player_speed = 8

# Shape settings
shapes = []
SHAPE_MIN_SIZE = 20
SHAPE_MAX_SIZE = 60
SHAPE_MIN_SPEED = 2
SHAPE_MAX_SPEED = 8

# Game variables
score = 0
game_over = False

# Create a new falling shape
def create_shape():
    size = random.randint(SHAPE_MIN_SIZE, SHAPE_MAX_SIZE)
    x = random.randint(0, SCREEN_WIDTH - size)
    y = -size
    speed = random.randint(SHAPE_MIN_SPEED, SHAPE_MAX_SPEED)
    color = random.choice([RED, BLUE, GREEN, YELLOW])
    return {"x": x, "y": y, "size": size, "speed": speed, "color": color}

# Draw shapes
def draw_shapes():
    for shape in shapes:
        pygame.draw.rect(screen, shape["color"], (shape["x"], shape["y"], shape["size"], shape["size"]))

# Main game loop
def game_loop():
    global player_x, player_y, shapes, score, game_over

    while not game_over:
        screen.fill(WHITE)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Handle player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - PLAYER_SIZE:
            player_x += player_speed
        if keys[pygame.K_UP] and player_y > 0:
            player_y -= player_speed
        if keys[pygame.K_DOWN] and player_y < SCREEN_HEIGHT - PLAYER_SIZE:
            player_y += player_speed

        # Spawn shapes
        if random.randint(1, 20) == 1:  # 5% chance to spawn a shape each frame
            shapes.append(create_shape())

        # Move shapes
        for shape in shapes[:]:
            shape["y"] += shape["speed"]
            if shape["y"] > SCREEN_HEIGHT:  # Remove shapes that go off-screen
                shapes.remove(shape)
                score += 1

        # Check for collisions
        for shape in shapes:
            if (
                player_x < shape["x"] + shape["size"]
                and player_x + PLAYER_SIZE > shape["x"]
                and player_y < shape["y"] + shape["size"]
                and player_y + PLAYER_SIZE > shape["y"]
            ):
                game_over = True

        # Draw player
        pygame.draw.rect(screen, BLACK, (player_x, player_y, PLAYER_SIZE, PLAYER_SIZE))

        # Draw shapes
        draw_shapes()

        # Display score
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        # Update screen
        pygame.display.flip()
        clock.tick(60)

    # Game Over Screen
    screen.fill(WHITE)
    game_over_text = font.render("Game Over!", True, BLACK)
    final_score_text = font.render(f"Final Score: {score}", True, BLACK)
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50))
    screen.blit(final_score_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(3000)

# Run the game
game_loop()
pygame.quit()
