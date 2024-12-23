import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Colorblind Detective")

# Colors (grayscale and hints)
GRAY = (169, 169, 169)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLOR_HINTS = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Red, Green, Blue

# Font setup
font = pygame.font.SysFont('Arial', 24)

# Game variables
hints_used = 0
hint_positions = [(200, 150), (400, 300), (600, 450)]  # random positions for hints
objects_to_color = [(100, 100), (500, 200), (300, 400)]  # object positions to be colorized
revealed_colors = [False, False, False]  # Track which objects have been revealed

# Clock setup
clock = pygame.time.Clock()

# Function to draw the grayscale world
def draw_world():
    screen.fill(GRAY)  # Fill the screen with a grayscale background
    # Draw objects in grayscale
    for pos in objects_to_color:
        pygame.draw.circle(screen, GRAY, pos, 40)  # Gray circles
    # Draw hint positions
    for hint in hint_positions:
        pygame.draw.circle(screen, WHITE, hint, 20)

# Function to reveal colors when hint is used
def reveal_color(index):
    if index < len(objects_to_color):
        pygame.draw.circle(screen, COLOR_HINTS[index], objects_to_color[index], 40)

# Main game loop
def main():
    global hints_used
    running = True
    while running:
        screen.fill(GRAY)
        draw_world()

        # Draw instructions
        instructions = font.render("Use your logic to deduce the colors. Click on hints to reveal color.", True, WHITE)
        screen.blit(instructions, (20, 20))

        # Draw hint count
        hint_text = font.render(f"Hints used: {hints_used}/3", True, WHITE)
        screen.blit(hint_text, (WIDTH - 200, 20))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Check if the mouse was clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                # Check if the player clicked on any hint
                for i, hint_pos in enumerate(hint_positions):
                    if pygame.Rect(hint_pos[0] - 20, hint_pos[1] - 20, 40, 40).collidepoint(mouse_pos):
                        if not revealed_colors[i]:  # If not already revealed
                            revealed_colors[i] = True
                            hints_used += 1
                            reveal_color(i)

        # Update the display
        pygame.display.flip()

        # Set the game frame rate
        clock.tick(30)

    pygame.quit()

# Run the game
if __name__ == "__main__":
    main()
