import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Balloon Pop Challenge")

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

# Balloon settings
BALLOON_RADIUS = 30
BALLOON_SPEED = 2

# Game variables
score = 0
balloons = []
power_ups = []
game_over = False
timer = 60  # 60 seconds timer
power_up_active = False
power_up_type = None
power_up_duration = 5  # Seconds
power_up_start_time = 0

# Create a balloon
def create_balloon():
    x = random.randint(BALLOON_RADIUS, SCREEN_WIDTH - BALLOON_RADIUS)
    y = SCREEN_HEIGHT + BALLOON_RADIUS
    color = random.choice([RED, BLUE, GREEN, YELLOW])
    return {"x": x, "y": y, "color": color}

# Create a power-up
def create_power_up():
    x = random.randint(50, SCREEN_WIDTH - 50)
    y = random.randint(50, SCREEN_HEIGHT - 50)
    return {"x": x, "y": y, "type": random.choice(["slow", "multi-pop"])}

# Draw balloons
def draw_balloons():
    for balloon in balloons:
        pygame.draw.circle(screen, balloon["color"], (balloon["x"], balloon["y"]), BALLOON_RADIUS)

# Draw power-ups
def draw_power_ups():
    for power_up in power_ups:
        pygame.draw.rect(screen, YELLOW, (power_up["x"] - 20, power_up["y"] - 20, 40, 40))

# Handle popping balloons
def pop_balloon(pos):
    global score
    for balloon in balloons[:]:
        if (balloon["x"] - pos[0]) ** 2 + (balloon["y"] - pos[1]) ** 2 <= BALLOON_RADIUS ** 2:
            balloons.remove(balloon)
            score += 1
            break

# Activate power-up
def activate_power_up(pos):
    global power_up_active, power_up_type, power_up_start_time
    for power_up in power_ups[:]:
        if power_up["x"] - 20 <= pos[0] <= power_up["x"] + 20 and power_up["y"] - 20 <= pos[1] <= power_up["y"] + 20:
            power_up_active = True
            power_up_type = power_up["type"]
            power_up_start_time = pygame.time.get_ticks()
            power_ups.remove(power_up)
            break

# Main game loop
def game_loop():
    global balloons, power_ups, game_over, score, timer, power_up_active, power_up_type

    start_time = pygame.time.get_ticks()

    while not game_over:
        screen.fill(WHITE)

        # Timer
        elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
        remaining_time = timer - elapsed_time
        if remaining_time <= 0:
            game_over = True

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pop_balloon(event.pos)
                activate_power_up(event.pos)

        # Spawn balloons
        if random.randint(1, 20) == 1:  # 5% chance to spawn a balloon
            balloons.append(create_balloon())

        # Spawn power-ups
        if random.randint(1, 500) == 1:  # Rare chance to spawn a power-up
            power_ups.append(create_power_up())

        # Move balloons
        for balloon in balloons[:]:
            balloon["y"] -= BALLOON_SPEED if not power_up_active or power_up_type != "slow" else BALLOON_SPEED // 2
            if balloon["y"] + BALLOON_RADIUS < 0:  # Remove balloons that go off-screen
                balloons.remove(balloon)

        # Handle power-up duration
        if power_up_active and pygame.time.get_ticks() - power_up_start_time > power_up_duration * 1000:
            power_up_active = False
            power_up_type = None

        # Draw everything
        draw_balloons()
        draw_power_ups()

        # Display score and timer
        score_text = font.render(f"Score: {score}", True, BLACK)
        timer_text = font.render(f"Time: {remaining_time}s", True, BLACK)
        screen.blit(score_text, (10, 10))
        screen.blit(timer_text, (10, 50))

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
