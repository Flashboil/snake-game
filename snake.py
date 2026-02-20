import pygame

class Snake:
    # Important constants for directions.
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    def __init__(self):
        self.direction = self.NORTH
        self.curr_x = 0
        self.curr_y = 0

    def get_coordinates(self):
        return self.curr_x, self.curr_y

    def update_direction(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_UP] == True or key[pygame.K_w] == True:
            self.direction = self.NORTH
        elif key[pygame.K_RIGHT] == True or key[pygame.K_d] == True:
            self.direction = self.EAST
        elif key[pygame.K_DOWN] == True or key[pygame.K_s] == True:
            self.direction = self.SOUTH
        elif key[pygame.K_LEFT] == True or key[pygame.K_a] == True:
            self.direction = self.WEST

    def update_location(self):
        """Method updates coordinates of the snake based on its current 
        location and current heading.
        """
        match self.direction:
            case self.NORTH:
                self.curr_y -= 1
            case self.SOUTH:
                self.curr_y += 1
            case self.EAST:
                self.curr_x += 1
            case self.WEST:
                self.curr_x -= 1