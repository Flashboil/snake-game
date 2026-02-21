import pygame
from map import Map

class Renderer:
    def __init__(self, mapsize):
        self.rendermap = Map(mapsize)

        self.TILE = 16
        SCREEN_WIDTH = mapsize * self.TILE
        SCREEN_HEIGHT = mapsize * self.TILE
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    def render_screen(self):
        self.screen.fill((0, 0, 0))

        for row in range(len(self.rendermap.map)):
            for col in range(len(self.rendermap.map)):
                x = col * self.TILE
                y = row * self.TILE

                if self.rendermap.map[row][col] == self.rendermap.EMPTY:
                    if (row + col) % 2 == 0:
                        color = (155, 188, 15)
                    else:
                        color = (139, 172, 15)
                elif self.rendermap.map[row][col] == self.rendermap.APPLE:
                    color = (48, 98, 48)

                pygame.draw.rect(self.screen, color, (x, y, self.TILE, self.TILE))
            

        pygame.display.flip()