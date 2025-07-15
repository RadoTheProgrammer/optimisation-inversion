import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Create a NumPy array with shape (height, width, 3)
width, height = 320, 240
array = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)

# Convert NumPy array to Pygame surface
surface = pygame.surfarray.make_surface(array.swapaxes(0, 1))  # Swap axes: (H, W, 3) → (W, H, 3)

# Display it
screen = pygame.display.set_mode((width, height))
screen.blit(surface, (0, 0))
pygame.display.flip()

# Event loop to keep window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
