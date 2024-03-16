import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Point with Name and Coordinates")

# Define the point's properties
point_name = "A"
point_x = 200
point_y = 300
point_color = (255, 0, 0)  # Red color
font = pygame.font.Font(None, 36)  # Font for text rendering

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill((255, 255, 255))  # White background

    # Draw the point
    pygame.draw.circle(screen, point_color, (point_x, point_y), 5)  # Draw a small circle as a point

    # Render text (point name and coordinates)
    text_surface = font.render(f"{point_name} ({point_x}, {point_y})", True, (0, 0, 0))  # Black color
    text_rect = text_surface.get_rect()
    text_rect.topleft = (point_x + 10, point_y - 20)  # Position the text near the point
    screen.blit(text_surface, text_rect)

    # Update the display
    pygame.display.flip()
