import pygame

class Snake:
    NORTH = (0, -1)
    EAST = (1, 0)
    SOUTH = (0, 1)
    WEST = (-1, 0)

    def __init__(self, mapsize):
        self.direction = self.NORTH
        self.curr_x = mapsize / 2
        self.curr_y = mapsize / 2
        self.mapsize = mapsize

    def get_coordinates(self):
        return self.curr_x, self.curr_y

    def get_next(self):
        """Return the coordinates of the next cell the snake is going to enter
          based on current driection and coordinates. This is to be used for 
          following and to check for collisions.
        """
        next_pos = (self.curr_x + self.direction[0], 
                self.curr_y + self.direction[1])
        return next_pos

    def update_direction(self):
        """Update the direction based on what key is being pressed. WASD and 
        direction arros are accepted inputs.
        """
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
        location and current heading. If the direction is north or south, 
        curr_y is updated by adding the direction, otherwise curr_x is updated
          by adding the direction.
        """
        next_pos = self.get_next()

        if self.direction == self.NORTH or self.direction == self.SOUTH:
            if 0 <= next_pos[1] < self.mapsize:
                self.curr_y += self.direction[1]
                return True
            else:
                return False
        else:
            if 0 <= next_pos[0] < self.mapsize:
                self.curr_x += self.direction[0]
                return True
            else:
                return False