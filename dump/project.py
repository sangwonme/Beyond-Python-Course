import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 500, 500

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Square size
SQUARE_SIZE = 50

# Create the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Click to Draw Squares")

# Fill the background
screen.fill(WHITE)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Exit the program
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:  # Mouse click event
            x, y = event.pos  # Get mouse position
            # Draw a square centered on the mouse position
            pygame.draw.rect(screen, BLACK, (x - SQUARE_SIZE // 2, y - SQUARE_SIZE // 2, SQUARE_SIZE, SQUARE_SIZE))
    
    # Update the display
    pygame.display.flip()
