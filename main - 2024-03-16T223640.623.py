import random

class Ant:
    def __init__(self, colony):
        self.colony = colony
        self.health = 100
        self.position = random.choice(colony.grid)
    
    def move(self):
        # Simulate ant movement
        neighbors = self.colony.get_neighbors(self.position)
        if neighbors:
            self.position = random.choice(neighbors)

    def interact(self, other_ant):
        # Simulate ant interaction
        if self.health > 0 and other_ant.health > 0:
            # Fighting scenario: higher health ant wins
            if self.health > other_ant.health:
                other_ant.health = 0
            elif self.health < other_ant.health:
                self.health = 0
            else:
                # If health is equal, both ants lose health
                self.health -= 20
                other_ant.health -= 20
    
    def get_infected(self):
        # Simulate ant getting infected
        self.health -= 20
    
    def heal(self):
        # Simulate ant healing
        self.health += 10
        if self.health > 100:
            self.health = 100

class Colony:
    def __init__(self, width, height, num_ants):
        self.width = width
        self.height = height
        self.grid = [(x, y) for x in range(width) for y in range(height)]
        self.ants = [Ant(self) for _ in range(num_ants)]
        self.disease_spread = 0.1
    
    def get_neighbors(self, position):
        # Get neighboring positions of an ant
        neighbors = []
        x, y = position
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                new_x, new_y = x + dx, y + dy
                if (new_x, new_y) in self.grid and (new_x, new_y) != position:
                    neighbors.append((new_x, new_y))
        return neighbors
    
    def spread_disease(self):
        # Simulate disease spread
        for ant 

