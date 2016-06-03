class Game(object):
    def __init__(self):
        self.grid = [['.' for x in range(8)] for y in range(4)]
        self.set(5, 2, '*')
        self.set(4, 3, '*')
        self.set(5, 3, '*')

    def get(self, x, y):
        return self.grid[y][x]

    def set(self, x, y, value):
        self.grid[y][x] = value
