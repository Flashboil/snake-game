import pygame
from snake import Snake
from map import Map
from renderer import Renderer

pygame.init()

MAP_SIZE = 20

map = Map(MAP_SIZE)
s = Snake(MAP_SIZE, map)
renderer = Renderer(MAP_SIZE, s, map)

# Game loop initalize
running = True
clock = pygame.time.Clock()
FPS = 60
MOVE_DELAY = 0.25
accumulator = 0

while running:
    s.update_direction()

    dt = clock.tick(60) / 1000

    accumulator += dt

    if accumulator >= MOVE_DELAY:
        if not s.update_location():
            running = False
        renderer.rendermap.place_apple()
        accumulator = 0

    renderer.render_screen()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()