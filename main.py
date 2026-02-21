import pygame
from snake import Snake
from renderer import Renderer

pygame.init()

MAP_SIZE = 20

s = Snake(MAP_SIZE)
renderer = Renderer(MAP_SIZE)

running = True
clock = pygame.time.Clock()
FPS = 2

while running:

    renderer.rendermap.place_apple()
    renderer.render_screen()

    clock.tick(FPS)

    print(s.get_coordinates())

    s.update_direction()

    if not s.update_location():
        print("Wall!")
        running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()