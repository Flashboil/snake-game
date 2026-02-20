import pygame
from snake import Snake

# Important constants for directions.
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

s = Snake()

running = True
clock = pygame.time.Clock()
FPS = 10

while running:

    clock.tick(FPS)

    s.update_direction()

    s.update_location()

    print(s.get_coordinates())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()