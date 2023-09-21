import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Raindrop Animation")

# Create a list to store raindrop positions and speeds
raindrops = []
for _ in range(50):
    x = random.randint(0, WIDTH)
    y = random.randint(-HEIGHT, 0)
    speed = random.randint(2, 5)
    raindrops.append([x, y, speed])

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update raindrop positions
    for i in range(len(raindrops)):
        raindrops[i][1] += raindrops[i][2]
        if raindrops[i][1] > HEIGHT:
            raindrops[i][1] = 0
            raindrops[i][0] = random.randint(0, WIDTH)

    # Clear the screen
    screen.fill(WHITE)

    # Draw raindrops
    for x, y, _ in raindrops:
        pygame.draw.circle(screen, BLUE, (x, y), 2)

    # Update the display
    pygame.display.flip()

    # Control the frame rate (optional)
    pygame.time.delay(20)

# Quit Pygame
pygame.quit()
sys.exit()
