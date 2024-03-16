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
point_x = 1000
point_y = 2000
point_color = (255, 0, 0)  # Red color
font = pygame.font.Font(None, 36)  # Font for text rendering

# Define the range of coordinates you want to display on the screen
# You can adjust these values based on your needs
min_x = -2000
max_x = 2000
min_y = -2000
max_y = 2000

# Function to scale the coordinates dynamically
def scale_coordinates(x, y):
    scaled_x = int((x - min_x) / (max_x - min_x) * screen_width)
    scaled_y = int((y - min_y) / (max_y - min_y) * screen_height)
    return scaled_x, scaled_y

# Scale the coordinates
scaled_point_x, scaled_point_y = scale_coordinates(point_x, point_y)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill((255, 255, 255))  # White background

    # Draw the point
    pygame.draw.circle(screen, point_color, (scaled_point_x, scaled_point_y), 5)  # Draw a small circle as a point

    # Render text (point name and coordinates)
    text_surface = font.render(f"{point_name} ({point_x}, {point_y})", True, (0, 0, 0))  # Black color
    text_rect = text_surface.get_rect()
    text_rect.topleft = (scaled_point_x + 10, scaled_point_y - 20)  # Position the text near the point
    screen.blit(text_surface, text_rect)

    # Update the display
    pygame.display.flip()
