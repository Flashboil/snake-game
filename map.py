import random

class Map:
    EMPTY = 0
    APPLE = 1

    def __init__(self, size):
        self.size = size
        self.map = self.generate_map(self.size)
        self.apples = []

    def generate_map(self, size):
        """Generate a map composed of a list of lists. The size of the grid 
        depends on the size parameter, but will always be a square.
        Args:
            size (int): How big the square grid will be.
        """
        tempmap = []
        for r in range(0, size):
            temp = []
            for c in range(0, size):
                temp.append(self.EMPTY)
            tempmap.append(temp)
        return tempmap

    def get_cell(self, coordinates):
        """Return the contents of the specified grid cell, be it snake, 
        segment, or apple.
        x coordinate is signifies the column being checked and y signifies the 
        row. That means the indexes will be map[y][x].
        Args:
            coordiantes (int, int) x and y coordinates to check.
        """
        x, y = coordinates
        return self.map[y][x]
    
    def place_apple(self):
        """Randomly selects a cell in the grid, then checks if it's empty. 
        If it isn't, it checks until it finds an empty cell. When it does, 
        it places and apple at that location. "cell == True" signifies a 
        filled cell and triggers the loop to try again.
        """
        if self.apples == []:
            cell = True
            while cell == True:
                randx = random.randint(0, self.size - 1)
                randy = random.randint(0, self.size - 1)
                if self.get_cell((randx, randy)) == self.EMPTY:
                    cell = False
            
            self.apples.append((randx, randy))
            self.map[randy][randx] = self.APPLE

    def remove_apple(self):
        apple_coords = self.apples.pop()
        x, y = apple_coords
        self.map[y][x] = self.EMPTY
