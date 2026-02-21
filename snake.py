import pygame

class Snake:
    NORTH = (0, -1)
    EAST = (1, 0)
    SOUTH = (0, 1)
    WEST = (-1, 0)

    def __init__(self, mapsize, map):
        self.direction = self.NORTH
        self.mapsize = mapsize
        self.map = map

        self.curr_x = mapsize / 2
        self.curr_y = mapsize / 2

        self.prev_x = self.curr_x - 1
        self.prev_y = self.curr_y - 1
        
        self.body = [(mapsize / 2, mapsize / 2), 
                     (mapsize / 2, mapsize / 2 + 1),
                     (mapsize / 2, mapsize / 2 + 2)]
        
        self.score = 0

    def get_coordinates(self):
        return self.body[0]

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
            if self.direction != self.SOUTH:
                self.direction = self.NORTH
        elif key[pygame.K_RIGHT] == True or key[pygame.K_d] == True:
            if self.direction != self.WEST:
                self.direction = self.EAST
        elif key[pygame.K_DOWN] == True or key[pygame.K_s] == True:
            if self.direction != self.NORTH:
                self.direction = self.SOUTH
        elif key[pygame.K_LEFT] == True or key[pygame.K_a] == True:
            if self.direction != self.EAST:
                self.direction = self.WEST

    def update_location(self):
        head_x, head_y = self.body[0]

        dx, dy = self.direction
        next_pos = (head_x + dx, head_y + dy)

        # self collision
        if next_pos in self.body:
            return False

        # wall collision
        if not (0 <= next_pos[0] < self.mapsize and
                0 <= next_pos[1] < self.mapsize):
            return False
        
        # apple detect, add segment and remove apple
        if next_pos in self.map.apples:
            self.map.remove_apple()
            self.add_segment()
            self.score += 1

        # Make a new head and remove the tail.
        self.body.insert(0, next_pos)
        self.body.pop()

        return True
    
    
    def add_segment(self):
        tail_x, tail_y = self.body[-1]
        new_tail = (tail_x + self.direction[0], tail_y + self.direction[1])
        self.body.append(new_tail)