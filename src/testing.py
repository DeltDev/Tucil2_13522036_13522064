import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Delay Example")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw a red circle
    pygame.draw.circle(screen, RED, (screen_width // 2, screen_height // 2), 50)

    # Update the display
    pygame.display.flip()

    # Wait for 2 seconds (using pygame.time.wait)
    pygame.time.wait(2000)

    # Clear the screen again
    screen.fill(WHITE)

    # Update the display to clear the previous circle
    pygame.display.flip()

    # Wait for 2 seconds (using pygame.time.delay)
    pygame.time.delay(2000)

# Quit Pygame properly
pygame.quit()
sys.exit()
