import pygame
import random

# Initialize Pygame
pygame.init()

# Game Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GROUND_HEIGHT = 350
FPS = 60

# Load Assets
CACTUS_IMG = pygame.image.load('dragon.png')  # Dragon image, replace with actual dragon image path
CACTUS_IMG = pygame.transform.scale(CACTUS_IMG, (50, 50))

DRAGON_IMG = pygame.image.load('cactus.png')  # Cactus image, replace with actual cactus image path
DRAGON_IMG = pygame.transform.scale(DRAGON_IMG, (50, 50))

# Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dragon Run")

# Define a clock object to control the game's frame rate
clock = pygame.time.Clock()

# Cactus (Dragon) Class
class Cactus:
    def __init__(self):
        self.image = CACTUS_IMG
        self.x = 50
        self.y = GROUND_HEIGHT
        self.jump_speed = -15
        self.gravity = 1
        self.jump = False
        self.velocity = 0

    def update(self):
        if self.jump:
            self.velocity += self.gravity
            self.y += self.velocity
            if self.y >= GROUND_HEIGHT:
                self.y = GROUND_HEIGHT
                self.jump = False
                self.velocity = 0

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def do_jump(self):
        if not self.jump:
            self.jump = True
            self.velocity = self.jump_speed

# Dragon (Cactus) Class
class Dragon:
    def __init__(self):
        self.image = DRAGON_IMG
        self.x = SCREEN_WIDTH
        self.y = GROUND_HEIGHT

    def update(self):
        self.x -= 10
        if self.x < -50:
            self.x = SCREEN_WIDTH + random.randint(0, 300)

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

# Main Game Function
def game():
    cactus = Cactus()
    dragon = Dragon()
    running = True
    score = 0

    while running:
        screen.fill(WHITE)
        cactus.update()
        dragon.update()

        cactus.draw()
        dragon.draw()

        # Check for collision
        if dragon.x < cactus.x + 50 < dragon.x + 50 and cactus.y == GROUND_HEIGHT:
            running = False

        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                cactus.do_jump()

        # Draw Score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f'Score: {score}', True, BLACK)
        screen.blit(score_text, (10, 10))
        score += 1

        pygame.display.flip()
        clock.tick(FPS)

    # Show final score
    final_score_text = font.render(f'Game Over! Final Score: {score}', True, BLACK)
    screen.fill(WHITE)
    screen.blit(final_score_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(3000)  # Wait for 3 seconds before quitting

    pygame.quit()

# Run the Game
if __name__ == "__main__":
    game()
