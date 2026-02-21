import pygame
import random
from map import Map
from snake import Snake

class Renderer:
    def __init__(self, mapsize, snake, map):
        self.rendermap = map
        self.rendersnake = snake

        self.TILE = 16
        SCREEN_WIDTH = mapsize * self.TILE
        SCREEN_HEIGHT = mapsize * self.TILE
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        # Color palette randomization
        self.PALETTES = {
            "classic_gameboy": {
                "snake": (15, 56, 15),
                "apple": (48, 98, 48),
                "grid1": (155, 188, 15),
                "grid2": (139, 172, 15)
            },

            "sunset_contrast": {
                "snake": (70, 30, 30),
                "apple": (220, 80, 80),
                "grid1": (240, 180, 100),
                "grid2": (200, 150, 80)
            },

            "neon_retro": {
                "snake": (80, 0, 150),
                "apple": (255, 50, 100),
                "grid1": (15, 15, 40),
                "grid2": (30, 30, 70)
            },

            "tropical": {
                "snake": (0, 120, 80),
                "apple": (255, 90, 0),
                "grid1": (220, 240, 200),
                "grid2": (200, 220, 180)
            },

            "ice_fire": {
                "snake": (30, 60, 90),
                "apple": (255, 100, 30),
                "grid1": (190, 230, 240),
                "grid2": (160, 210, 220)
            }
        }

        palette = random.choice(list(self.PALETTES.values()))

        self.snake_color = palette["snake"]
        self.apple_color = palette["apple"]
        self.grid1_color = palette["grid1"]
        self.grid2_color = palette["grid2"]


    def render_snake(self):
        col, row = self.rendersnake.get_coordinates()
        x = col * self.TILE
        y = row * self.TILE
        pygame.draw.rect(self.screen, self.snake_color, (x, y, self.TILE, self.TILE))
        for col, row in self.rendersnake.body:
            x = col * self.TILE
            y = row * self.TILE
            pygame.draw.rect(self.screen, self.snake_color, (x, y, self.TILE, self.TILE))

    def render_apple(self):
        if self.rendermap.apples != []:
            col, row = self.rendermap.apples[0]
            x = col * self.TILE
            y = row * self.TILE
            pygame.draw.rect(self.screen, self.apple_color, (x, y, self.TILE, self.TILE))

    def render_screen(self):
        self.screen.fill((0, 0, 0))

        for row in range(len(self.rendermap.map)):
            for col in range(len(self.rendermap.map)):
                x = col * self.TILE
                y = row * self.TILE

                if (row + col) % 2 == 0:
                    color = self.grid1_color
                else:
                    color = self.grid2_color

                pygame.draw.rect(self.screen, color, (x, y, self.TILE, self.TILE))

        self.render_apple()
            
        self.render_snake()

        pygame.display.flip()