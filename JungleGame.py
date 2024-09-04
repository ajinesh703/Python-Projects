import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Forest Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (34, 139, 34)
RED = (255, 0, 0)

# Character settings
character_width = 50
character_height = 60
character_x = SCREEN_WIDTH // 2
character_y = SCREEN_HEIGHT - character_height - 10
character_speed = 5

# Obstacle settings
obstacle_width = 50
obstacle_height = 50
obstacle_speed = 18
obstacle_color = (139, 69, 19)

# Load character image
character_img = pygame.image.load("character.png")
character_img = pygame.transform.scale(character_img, (character_width, character_height))

# Font settings
font = pygame.font.Font(None, 36)

# Set up clock
clock = pygame.time.Clock()

# Function to draw character
def draw_character(x, y):
    screen.blit(character_img, (x, y))

# Function to draw obstacle
def draw_obstacle(obstacle_x, obstacle_y):
    pygame.draw.rect(screen, obstacle_color, [obstacle_x, obstacle_y, obstacle_width, obstacle_height])

# Function to display text
def display_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Main game loop
def game_loop():
    global character_x, character_y

    obstacle_list = []
    score = 0
    game_over = False
    run_game = True

    def spawn_obstacles():
        num_obstacles = random.choice([2, 3])
        new_obstacles = []
        for _ in range(num_obstacles):
            obstacle_x = random.randint(0, SCREEN_WIDTH - obstacle_width)
            obstacle_y = -obstacle_height
            new_obstacles.append([obstacle_x, obstacle_y])
        return new_obstacles

    obstacle_list = spawn_obstacles()

    while run_game:
        while game_over:
            screen.fill(GREEN)
            display_text(f"Game Over! Your Score: {score}", font, RED, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 3)
            display_text("Press 'A' to play again or 'Q' to quit.", font, WHITE, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run_game = False
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        run_game = False
                        game_over = False
                    if event.key == pygame.K_a:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False

        # Get key presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            character_x -= character_speed
        if keys[pygame.K_RIGHT]:
            character_x += character_speed

        # Update obstacle positions
        for obstacle in obstacle_list:
            obstacle[1] += obstacle_speed

        # Check for collision
        for obstacle in obstacle_list:
            if character_y < obstacle[1] + obstacle_height and character_y + character_height > obstacle[1]:
                if character_x < obstacle[0] + obstacle_width and character_x + character_width > obstacle[0]:
                    game_over = True

        # Remove obstacles that have gone off-screen and spawn new ones
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle[1] <= SCREEN_HEIGHT]
        if len(obstacle_list) == 0:
            obstacle_list = spawn_obstacles()
            score += 10  # Increase score by 10 for each successful round

        # Fill screen with green (forest) color
        screen.fill(GREEN)

        # Draw character and obstacles
        draw_character(character_x, character_y)
        for obstacle in obstacle_list:
            draw_obstacle(obstacle[0], obstacle[1])

        # Display the score
        display_text(f"Score: {score}", font, WHITE, 10, 10)

        # Update display
        pygame.display.update()

        # Set FPS
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    game_loop()
